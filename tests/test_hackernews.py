from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock

import httpx

from src.models import HackerNewsConfig, SourceType
from src.scrapers.hackernews import HackerNewsScraper


def _ts(dt: datetime) -> int:
    return int(dt.timestamp())


def _build_client(topstories, items_by_id) -> AsyncMock:
    """AsyncMock client that routes firebase URLs to the right payloads."""

    def _make_response(payload):
        resp = AsyncMock()
        resp.raise_for_status = lambda: None
        resp.json = lambda: payload
        return resp

    async def _get(url, *args, **kwargs):
        if url.endswith("/topstories.json"):
            return _make_response(topstories)
        # url form: .../item/{id}.json
        item_id = int(url.rsplit("/item/", 1)[1].split(".json")[0])
        return _make_response(items_by_id.get(item_id))

    client = AsyncMock()
    client.get.side_effect = _get
    return client


def test_fetch_filters_by_score_and_time_and_parses_comments() -> None:
    recent = datetime(2026, 1, 2, tzinfo=timezone.utc)
    old = datetime(2025, 1, 1, tzinfo=timezone.utc)

    items_by_id = {
        1: {
            "id": 1,
            "title": "Big story",
            "url": "https://example.com/big",
            "by": "alice",
            "time": _ts(recent),
            "score": 200,
            "descendants": 10,
            "kids": [100, 101],
            "type": "story",
        },
        # Below min_score -> filtered.
        2: {"id": 2, "title": "Low", "by": "bob", "time": _ts(recent), "score": 5, "kids": []},
        # Too old -> filtered.
        3: {"id": 3, "title": "Old", "by": "carol", "time": _ts(old), "score": 500, "kids": []},
        100: {"id": 100, "by": "commenter1", "text": "<p>Great <b>post</b></p>"},
        101: {"id": 101, "by": "commenter2", "text": "agreed", "deleted": True},
    }
    client = _build_client([1, 2, 3], items_by_id)
    config = HackerNewsConfig(enabled=True, fetch_top_stories=3, min_score=100)
    scraper = HackerNewsScraper(config, client)
    since = datetime(2026, 1, 1, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))
    assert len(items) == 1
    item = items[0]
    assert item.id == "hackernews:story:1"
    assert item.source_type == SourceType.HACKERNEWS
    assert item.metadata["score"] == 200
    # Deleted comment dropped; HTML stripped from the surviving comment.
    assert item.metadata["comment_count"] == 1
    assert "commenter1" in item.content
    assert "<p>" not in item.content
    assert item.metadata["discussion_url"] == "https://news.ycombinator.com/item?id=1"


def test_fetch_disabled_returns_empty() -> None:
    config = HackerNewsConfig(enabled=False)
    scraper = HackerNewsScraper(config, AsyncMock())
    assert asyncio.run(scraper.fetch(datetime(2026, 1, 1, tzinfo=timezone.utc))) == []


def test_fetch_handles_topstories_http_error() -> None:
    client = AsyncMock()
    client.get.side_effect = httpx.HTTPError("boom")
    config = HackerNewsConfig(enabled=True)
    scraper = HackerNewsScraper(config, client)
    assert asyncio.run(scraper.fetch(datetime(2026, 1, 1, tzinfo=timezone.utc))) == []


def test_parse_story_truncates_long_comments() -> None:
    config = HackerNewsConfig()
    scraper = HackerNewsScraper(config, AsyncMock())
    story = {
        "id": 7,
        "title": "T",
        "by": "u",
        "time": _ts(datetime(2026, 1, 1, tzinfo=timezone.utc)),
        "score": 100,
    }
    long_text = "x" * 1000
    item = scraper._parse_story(story, [{"by": "c", "text": long_text}])
    assert "..." in item.content
    # Body has the 497-char truncation applied.
    assert ("x" * 497 + "...") in item.content


def test_parse_story_uses_permalink_when_no_url() -> None:
    config = HackerNewsConfig()
    scraper = HackerNewsScraper(config, AsyncMock())
    story = {
        "id": 8,
        "title": "Ask HN",
        "by": "u",
        "time": _ts(datetime(2026, 1, 1, tzinfo=timezone.utc)),
        "score": 100,
    }
    item = scraper._parse_story(story, [])
    assert str(item.url) == "https://news.ycombinator.com/item?id=8"
