"""BAAI Hub scraper implementation."""

from __future__ import annotations

import ast
import json
import logging
import re
from datetime import datetime, timedelta, timezone
from typing import Any, List, Optional
from urllib.parse import urljoin

import httpx

from .base import BaseScraper
from ..models import BAAIHubConfig, ContentItem, SourceType

logger = logging.getLogger(__name__)


class BAAIHubScraper(BaseScraper):
    """Scraper for BAAI Hub's SSR-rendered latest story list."""

    def __init__(self, config: BAAIHubConfig, http_client: httpx.AsyncClient):
        """Initialize BAAI Hub scraper."""
        super().__init__(
            {
                "enabled": config.enabled,
                "url": str(config.url),
                "fetch_limit": config.fetch_limit,
                "category": config.category,
            },
            http_client,
        )
        self.cfg = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch latest BAAI Hub stories from the homepage SSR payload."""
        if not self.cfg.enabled:
            return []

        try:
            response = await self.client.get(
                str(self.cfg.url),
                follow_redirects=True,
                headers={
                    "Accept": "text/html,application/xhtml+xml",
                    "User-Agent": "Horizon/1.0",
                },
            )
            response.raise_for_status()
        except httpx.HTTPError as e:
            logger.warning("Error fetching BAAI Hub: %s", e)
            return []

        try:
            stories = self._extract_stories(response.text)
        except Exception as e:
            logger.warning("Error parsing BAAI Hub: %s", e)
            return []

        items: List[ContentItem] = []
        for story in stories[: self.cfg.fetch_limit]:
            item = self._story_to_item(story)
            if item is None or item.published_at < since:
                continue
            items.append(item)

        return items

    def _extract_stories(self, html: str) -> List[dict]:
        """Extract story_info objects from the Nuxt SSR payload."""
        payload = self._extract_nuxt_payload(html)
        stories: List[dict] = []
        self._walk(payload, stories)
        return stories

    def _extract_nuxt_payload(self, html: str) -> Any:
        """Parse window.__NUXT__ assignment into Python data."""
        match = re.search(r"<script>\s*window\.__NUXT__=(.*?)</script>", html, re.S)
        if not match:
            return {}

        script = match.group(1).strip()
        try:
            return json.loads(script)
        except json.JSONDecodeError:
            pass

        if script.startswith("(function"):
            return self._parse_iife_payload(script)

        return {}

    def _parse_iife_payload(self, script: str) -> Any:
        """Parse Nuxt's compact IIFE payload format used by BAAI Hub."""
        return_match = re.search(r"return\s+(.+)\}\((.*)\)\s*;?$", script, re.S)
        if not return_match:
            return {}

        expr = return_match.group(1).strip()
        args_src = return_match.group(2).strip()
        if args_src.endswith(")"):
            args_src = args_src[:-1]
        args = self._parse_iife_args(script, args_src)
        expr = self._replace_identifiers(expr, args)
        expr = self._js_object_to_python_literal(expr)
        return ast.literal_eval(expr)

    def _parse_iife_args(self, script: str, args_src: str) -> dict[str, Any]:
        """Map IIFE parameter letters to the literal argument values."""
        names_match = re.match(r"\(function\(([^)]*)\)", script)
        if not names_match:
            return {}
        parts = self._split_top_level(args_src)
        names = [part.strip() for part in names_match.group(1).split(",")]
        values = [self._js_literal_to_python(part) for part in parts]
        return dict(zip(names, values))

    def _replace_identifiers(self, expr: str, values: dict[str, Any]) -> str:
        """Replace compact variable references in a JS object expression."""
        out: list[str] = []
        i = 0
        in_string: str | None = None
        while i < len(expr):
            ch = expr[i]
            if in_string:
                out.append(ch)
                if ch == "\\" and i + 1 < len(expr):
                    i += 1
                    out.append(expr[i])
                elif ch == in_string:
                    in_string = None
                i += 1
                continue

            if ch in {"'", '"'}:
                in_string = ch
                out.append(ch)
                i += 1
                continue

            if re.match(r"[A-Za-z_$]", ch):
                j = i + 1
                while j < len(expr) and re.match(r"[A-Za-z0-9_$]", expr[j]):
                    j += 1
                token = expr[i:j]
                if token in values:
                    out.append(repr(values[token]))
                elif token == "void":
                    k = j
                    while k < len(expr) and expr[k].isspace():
                        k += 1
                    if expr[k : k + 1] == "0":
                        out.append("None")
                        j = k + 1
                    else:
                        out.append(token)
                else:
                    out.append(token)
                i = j
                continue

            out.append(ch)
            i += 1

        return "".join(out)

    def _js_object_to_python_literal(self, expr: str) -> str:
        """Convert a small JS object literal subset into a Python literal."""
        expr = expr.replace("\\u002F", "/")
        expr = re.sub(r"\btrue\b", "True", expr)
        expr = re.sub(r"\bfalse\b", "False", expr)
        expr = re.sub(r"\bnull\b", "None", expr)
        expr = re.sub(r"\bundefined\b", "None", expr)
        expr = re.sub(r"([{,])\s*([A-Za-z_$][A-Za-z0-9_$]*)\s*:", r"\1'\2':", expr)
        return expr

    def _js_literal_to_python(self, value: str) -> Any:
        """Convert one JS literal argument into a Python value."""
        value = self._js_object_to_python_literal(value.strip())
        try:
            return ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value

    def _split_top_level(self, text: str) -> list[str]:
        """Split comma-separated JS arguments without splitting nested strings."""
        parts: list[str] = []
        start = 0
        depth = 0
        in_string: str | None = None
        i = 0
        while i < len(text):
            ch = text[i]
            if in_string:
                if ch == "\\":
                    i += 2
                    continue
                if ch == in_string:
                    in_string = None
                i += 1
                continue
            if ch in {"'", '"'}:
                in_string = ch
            elif ch in "([{":
                depth += 1
            elif ch in ")]}":
                depth -= 1
            elif ch == "," and depth == 0:
                parts.append(text[start:i].strip())
                start = i + 1
            i += 1
        if start < len(text):
            parts.append(text[start:].strip())
        return parts

    def _walk(self, node: Any, stories: List[dict]) -> None:
        """Collect nested story_info dictionaries."""
        if isinstance(node, dict):
            story = node.get("story_info")
            if isinstance(story, dict):
                stories.append(story)
            for value in node.values():
                self._walk(value, stories)
        elif isinstance(node, list):
            for value in node:
                self._walk(value, stories)

    def _story_to_item(self, story: dict) -> Optional[ContentItem]:
        """Convert a BAAI Hub story_info dict into a ContentItem."""
        story_id = story.get("id")
        title = (story.get("title") or "").strip()
        if not story_id or not title:
            return None

        url = story.get("url") or urljoin(str(self.cfg.url), f"/view/{story_id}")
        published_at = self._parse_created_at(story.get("created_at"))
        if published_at is None:
            published_at = datetime.now(timezone.utc)

        tag_names = [
            tag.get("title")
            for tag in story.get("tag_names", [])
            if isinstance(tag, dict) and tag.get("title")
        ]

        content_parts = [
            (story.get("summary") or "").strip(),
            (story.get("content") or "").strip(),
        ]
        content = "\n\n".join(part for part in content_parts if part)

        return ContentItem(
            id=self._generate_id(
                SourceType.BAAIHUB.value,
                "story",
                str(story_id),
            ),
            source_type=SourceType.BAAIHUB,
            title=title,
            url=url,
            content=content,
            author=story.get("story_show_user_name") or story.get("user_name"),
            published_at=published_at,
            metadata={
                "category": self.cfg.category,
                "hub_url": str(urljoin(str(self.cfg.url), f"/view/{story_id}")),
                "cover_url": story.get("cover_url"),
                "host": story.get("host"),
                "tags": tag_names,
            },
        )

    def _parse_created_at(self, value: Any) -> Optional[datetime]:
        """Parse BAAI Hub date strings like '2026-07-08 13:30 分享'."""
        if not value:
            return None
        text = str(value)
        match = re.search(r"(\d{4}-\d{1,2}-\d{1,2}\s+\d{1,2}:\d{2})", text)
        if not match:
            return None
        try:
            local_tz = timezone(timedelta(hours=8))
            return (
                datetime.strptime(match.group(1), "%Y-%m-%d %H:%M")
                .replace(tzinfo=local_tz)
                .astimezone(timezone.utc)
            )
        except ValueError:
            return None
