"""Utilities for normalizing app-generated Markdown."""

import html
import re
from urllib.parse import urlsplit


_DETAILS_RE = re.compile(
    r"<details>\s*<summary>(.*?)</summary>\s*(.*?)\s*</details>",
    re.IGNORECASE | re.DOTALL,
)
_ANCHOR_LINK_RE = re.compile(
    r"^\s*<a\s+[^>]*href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>\s*$",
    re.IGNORECASE | re.DOTALL,
)
_LI_RE = re.compile(r"<li>\s*(.*?)\s*</li>", re.IGNORECASE | re.DOTALL)
_ANCHOR_ID_RE = re.compile(
    r"<a\s+[^>]*id=[\"'][^\"']+[\"'][^>]*>\s*</a>", re.IGNORECASE
)
_HTML_TAG_RE = re.compile(r"<[^>]+>")
_MARKDOWN_SPECIAL_RE = re.compile(r"([\\`*_{}\[\]<>()#+!|])")
_CONTROL_CHAR_RE = re.compile(r"[\x00-\x1f\x7f]")
_UNSAFE_MARKDOWN_URL_CHAR_RE = re.compile(r"[\s<>\[\]\\]")
_SAFE_URL_SCHEMES = {"http", "https", "mailto"}


def _strip_html_tags(value: str) -> str:
    """Remove simple HTML tags and decode HTML entities."""
    return html.unescape(_HTML_TAG_RE.sub("", value)).strip()


def _escape_markdown_text(value: str) -> str:
    """Escape user-controlled text before embedding it in generated Markdown."""
    clean_value = re.sub(r"\s+", " ", value).strip()
    return _MARKDOWN_SPECIAL_RE.sub(r"\\\1", clean_value)


def _is_safe_markdown_link_url(value: str) -> bool:
    """Return True when a URL can be emitted as an active Markdown link."""
    if _CONTROL_CHAR_RE.search(value):
        return False
    if _UNSAFE_MARKDOWN_URL_CHAR_RE.search(value):
        return False
    if value.count("(") != value.count(")"):
        return False

    try:
        parsed = urlsplit(value)
    except ValueError:
        return False

    scheme = parsed.scheme.lower()
    if scheme not in _SAFE_URL_SCHEMES:
        return False

    if scheme in {"http", "https"}:
        return bool(parsed.netloc)

    return bool(parsed.path)


def _convert_details_to_markdown(value: str) -> str:
    """Convert HTML details blocks into plain Markdown sections."""

    def _replace(match: re.Match) -> str:
        title = _escape_markdown_text(_strip_html_tags(match.group(1)) or "References")
        body = match.group(2)
        items: list[str] = []

        for item in _LI_RE.findall(body):
            link_match = _ANCHOR_LINK_RE.match(item)
            if link_match:
                href, label = link_match.groups()
                clean_label = _strip_html_tags(label)
                escaped_label = _escape_markdown_text(clean_label)
                clean_href = html.unescape(href).strip()
                if escaped_label and clean_href and _is_safe_markdown_link_url(clean_href):
                    items.append(f"- [{escaped_label}]({clean_href})")
                elif escaped_label:
                    items.append(f"- {escaped_label}")
                continue

            clean_item = _escape_markdown_text(_strip_html_tags(item))
            if clean_item:
                items.append(f"- {clean_item}")

        if not items:
            fallback = _escape_markdown_text(_strip_html_tags(body))
            return f"**{title}**\n\n{fallback}" if fallback else f"**{title}**"

        return f"**{title}**\n\n" + "\n".join(items)

    return _DETAILS_RE.sub(_replace, value)


def clean_app_summary_markdown(value: str) -> str:
    """Flatten app-generated HTML snippets embedded in summary Markdown.

    Unknown raw HTML is intentionally left in place so callers can choose their
    own safety boundary. Email, for example, escapes after this cleanup step.
    """
    value = _ANCHOR_ID_RE.sub("", value)
    return _convert_details_to_markdown(value)


_HTML_URL_ATTR_RE = re.compile(
    r"""(?P<attr>\b(?:href|src)\s*=\s*)(?P<quote>["'])(?P<url>.*?)(?P=quote)""",
    re.IGNORECASE | re.DOTALL,
)


def _url_scheme(url: str) -> str | None:
    """Return the lowercased scheme of *url*, or None if it is scheme-relative."""
    cleaned = html.unescape(url).strip()
    # Strip control/whitespace characters that browsers ignore when parsing
    # schemes (e.g. "java\tscript:") so obfuscated payloads can't slip through.
    cleaned = re.sub(r"[\x00-\x20]", "", cleaned)
    match = re.match(r"^([A-Za-z][A-Za-z0-9+.-]*):", cleaned)
    return match.group(1).lower() if match else None


def sanitize_rendered_html_urls(html_str: str) -> str:
    """Neutralize dangerous URL schemes in ``href``/``src`` attributes.

    Rendered Markdown may contain attacker-influenced links (e.g. summaries
    derived from scraped titles), so links such as ``javascript:`` or
    ``data:`` must not survive into HTML that is delivered to users. Relative
    and scheme-relative URLs are preserved; only URLs whose scheme is outside
    the allowlist are dropped.
    """

    def _replace(match: re.Match) -> str:
        scheme = _url_scheme(match.group("url"))
        if scheme is None or scheme in _SAFE_URL_SCHEMES:
            return match.group(0)
        return f'{match.group("attr")}{match.group("quote")}{match.group("quote")}'

    return _HTML_URL_ATTR_RE.sub(_replace, html_str)
