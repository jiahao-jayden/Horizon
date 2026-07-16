from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock

import httpx

from src.models import OSSInsightConfig, SourceType
from src.scrapers.ossinsight import OSSInsightScraper


def _client_returning(rows) -> AsyncMock:
    response = MagicMock()
    response.raise_for_status.return_value = None
    response.json.return_value = {"data": {"rows": rows}}
    client = AsyncMock()
    client.get.return_value = response
    return client


def _row(name="owner/repo", repo_id="1", stars="120", **extra) -> dict:
    row = {"repo_name": name, "repo_id": repo_id, "stars": stars}
    row.update(extra)
    return row


SINCE = datetime(2026, 1, 1, tzinfo=timezone.utc)


def test_disabled_returns_empty() -> None:
    config = OSSInsightConfig(enabled=False)
    scraper = OSSInsightScraper(config, AsyncMock())
    assert asyncio.run(scraper.fetch(SINCE)) == []


def test_fetch_builds_items_and_sorts_by_stars() -> None:
    rows = [
        _row("a/low", "1", "10"),
        _row("b/high", "2", "500", description="cool tool"),
    ]
    config = OSSInsightConfig(enabled=True, languages=["Python"], min_stars=1)
    scraper = OSSInsightScraper(config, _client_returning(rows))
    items = asyncio.run(scraper.fetch(SINCE))
    assert [i.metadata["repo"] for i in items] == ["b/high", "a/low"]
    top = items[0]
    assert top.source_type == SourceType.OSSINSIGHT
    assert top.id == "ossinsight:trending:2"
    assert top.metadata["stars_gained"] == 500
    assert top.author == "b"


def test_min_stars_filter() -> None:
    rows = [_row("a/x", "1", "3"), _row("b/y", "2", "50")]
    config = OSSInsightConfig(enabled=True, languages=["All"], min_stars=10)
    scraper = OSSInsightScraper(config, _client_returning(rows))
    items = asyncio.run(scraper.fetch(SINCE))
    assert len(items) == 1
    assert items[0].metadata["repo"] == "b/y"


def test_keyword_filter_matches_description_and_name() -> None:
    rows = [
        _row("org/agent-framework", "1", "100"),
        _row("org/unrelated", "2", "100", description="a database"),
        _row("org/matcher", "3", "100", description="an LLM agent"),
    ]
    config = OSSInsightConfig(
        enabled=True, languages=["All"], min_stars=1, keywords=["agent"]
    )
    scraper = OSSInsightScraper(config, _client_returning(rows))
    items = asyncio.run(scraper.fetch(SINCE))
    repos = {i.metadata["repo"] for i in items}
    assert repos == {"org/agent-framework", "org/matcher"}


def test_dedup_across_languages() -> None:
    client = AsyncMock()
    response = MagicMock()
    response.raise_for_status.return_value = None
    response.json.return_value = {"data": {"rows": [_row("dup/repo", "9", "100")]}}
    client.get.return_value = response
    config = OSSInsightConfig(
        enabled=True, languages=["Python", "TypeScript"], min_stars=1
    )
    scraper = OSSInsightScraper(config, client)
    items = asyncio.run(scraper.fetch(SINCE))
    assert len(items) == 1


def test_max_items_limit() -> None:
    rows = [_row(f"o/r{i}", str(i), str(100 + i)) for i in range(10)]
    config = OSSInsightConfig(enabled=True, languages=["All"], min_stars=1, max_items=3)
    scraper = OSSInsightScraper(config, _client_returning(rows))
    items = asyncio.run(scraper.fetch(SINCE))
    assert len(items) == 3


def test_row_missing_required_fields_skipped() -> None:
    rows = [{"repo_name": "no/id"}, {"repo_id": "5"}]
    config = OSSInsightConfig(enabled=True, languages=["All"], min_stars=0)
    scraper = OSSInsightScraper(config, _client_returning(rows))
    assert asyncio.run(scraper.fetch(SINCE)) == []


def test_fetch_period_http_error_returns_empty() -> None:
    client = AsyncMock()
    client.get.side_effect = httpx.HTTPError("boom")
    config = OSSInsightConfig(enabled=True, languages=["All"])
    scraper = OSSInsightScraper(config, client)
    assert asyncio.run(scraper.fetch(SINCE)) == []


def test_int_coercion_helpers() -> None:
    assert OSSInsightScraper._int("42") == 42
    assert OSSInsightScraper._int(None) == 0
    assert OSSInsightScraper._int("abc") == 0
    assert OSSInsightScraper._stars_int({"stars": "7"}) == 7
