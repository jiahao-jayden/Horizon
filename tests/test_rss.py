from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock
from unittest.mock import MagicMock

from src.models import RSSSourceConfig
from src.scrapers.rss import RSSScraper


def test_rss_ids_are_deterministic() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>entry-1</guid>
        <title>Item 1</title>
        <link>https://example.com/item-1</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
        <description>Hello</description>
      </item>
    </channel></rss>
    """
    response = MagicMock()
    response.text = feed
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    scraper = RSSScraper([source], client)
    since = datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)

    first = asyncio.run(scraper.fetch(since))[0].id
    second = asyncio.run(scraper.fetch(since))[0].id

    assert first == second
    assert first == "rss:example.com_feed.xml:5e2d5d1e58e94d76"


def test_rss_feed_url_expands_environment_variables(monkeypatch) -> None:
    response = MagicMock()
    response.text = "<rss><channel></channel></rss>"
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    monkeypatch.setenv("RSS_HOST", " example.com ")
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    source.url = "https://${RSS_HOST}/feed.xml"
    scraper = RSSScraper([source], client)

    asyncio.run(scraper.fetch(datetime(2026, 4, 24, tzinfo=timezone.utc)))

    client.get.assert_awaited_once_with(
        "https://example.com/feed.xml",
        follow_redirects=True,
    )
