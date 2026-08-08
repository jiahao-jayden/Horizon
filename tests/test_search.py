from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock

import httpx

from src.models import ContentItem, SourceType
from src.search import search_hn, search_reddit, search_related


def _make_item(item_id: str, title: str, url: str) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=title,
        url=url,
        published_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
    )


def _client_returning(data: dict) -> AsyncMock:
    response = MagicMock()
    response.raise_for_status.return_value = None
    response.json.return_value = data
    client = AsyncMock()
    client.get.return_value = response
    return client


def test_search_hn_parses_hits() -> None:
    data = {
        "hits": [
            {
                "title": "Cool story",
                "url": "https://example.com/story",
                "points": 120,
                "num_comments": 45,
                "created_at": "2026-01-01T00:00:00Z",
            },
            {
                # No url -> falls back to HN item permalink via objectID.
                "title": "No URL",
                "objectID": "999",
                "points": 10,
            },
        ]
    }
    results = asyncio.run(search_hn("query", _client_returning(data)))
    assert len(results) == 2
    assert results[0]["source"] == "hackernews"
    assert results[0]["score"] == 120
    assert results[1]["url"] == "https://news.ycombinator.com/item?id=999"


def test_search_hn_returns_empty_on_error() -> None:
    client = AsyncMock()
    client.get.side_effect = httpx.ConnectError("down")
    assert asyncio.run(search_hn("q", client)) == []


def test_search_reddit_parses_children() -> None:
    data = {
        "data": {
            "children": [
                {
                    "data": {
                        "title": "Reddit post",
                        "url": "https://reddit.com/r/x/1",
                        "score": 55,
                        "num_comments": 12,
                        "subreddit": "x",
                        "created_utc": 1700000000,
                    }
                }
            ]
        }
    }
    results = asyncio.run(search_reddit("q", _client_returning(data)))
    assert len(results) == 1
    assert results[0]["source"] == "reddit"
    assert results[0]["subreddit"] == "x"


def test_search_reddit_returns_empty_on_error() -> None:
    client = AsyncMock()
    client.get.side_effect = httpx.HTTPError("boom")
    assert asyncio.run(search_reddit("q", client)) == []


def test_search_related_maps_and_dedups_own_url() -> None:
    item = _make_item("rss:x:1", "My Title", "https://example.com/story/")

    hn_data = {
        "hits": [
            # This one matches the item's own URL (ignoring trailing slash) -> dropped.
            {"title": "self", "url": "https://example.com/story", "points": 1},
            {"title": "other", "url": "https://other.com/a", "points": 2},
        ]
    }
    reddit_data = {"data": {"children": []}}

    def _get(url, *args, **kwargs):
        response = MagicMock()
        response.raise_for_status.return_value = None
        response.json.return_value = hn_data if "algolia" in url else reddit_data
        return response

    client = AsyncMock()
    client.get.side_effect = _get

    mapping = asyncio.run(search_related([item], client))
    assert set(mapping.keys()) == {"rss:x:1"}
    urls = [r["url"] for r in mapping["rss:x:1"]]
    assert "https://example.com/story" not in urls
    assert "https://other.com/a" in urls


def test_search_related_empty_items() -> None:
    client = AsyncMock()
    assert asyncio.run(search_related([], client)) == {}
