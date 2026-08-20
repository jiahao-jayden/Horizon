from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock

import httpx

from src.models import GitHubSourceConfig, SourceType
from src.scrapers.github import GitHubScraper


def _client_returning(data) -> AsyncMock:
    response = MagicMock()
    response.raise_for_status.return_value = None
    response.json.return_value = data
    client = AsyncMock()
    client.get.return_value = response
    return client


def _push_event(created_at: str = "2026-01-02T00:00:00Z") -> dict:
    return {
        "id": "1",
        "type": "PushEvent",
        "created_at": created_at,
        "repo": {"name": "octocat/hello"},
        "payload": {"commits": [{"message": "fix a"}, {"message": "fix b"}]},
    }


def test_get_headers_without_token(monkeypatch) -> None:
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    scraper = GitHubScraper([], AsyncMock())
    headers = scraper._get_headers()
    assert "Authorization" not in headers
    assert headers["Accept"] == "application/vnd.github.v3+json"


def test_get_headers_with_token(monkeypatch) -> None:
    monkeypatch.setenv("GITHUB_TOKEN", "secret")
    scraper = GitHubScraper([], AsyncMock())
    assert scraper._get_headers()["Authorization"] == "token secret"


def test_fetch_user_events_filters_old_and_uninteresting() -> None:
    events = [
        _push_event("2026-01-02T00:00:00Z"),
        # Too old -> filtered out.
        {
            "id": "2",
            "type": "PushEvent",
            "created_at": "2025-01-01T00:00:00Z",
            "repo": {"name": "octocat/hello"},
            "payload": {"commits": []},
        },
        # Uninteresting event type -> filtered out.
        {
            "id": "3",
            "type": "IssueCommentEvent",
            "created_at": "2026-01-02T00:00:00Z",
            "repo": {"name": "octocat/hello"},
            "payload": {},
        },
    ]
    source = GitHubSourceConfig(type="user_events", username="octocat")
    scraper = GitHubScraper([source], _client_returning(events))
    since = datetime(2026, 1, 1, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))
    assert len(items) == 1
    assert items[0].id == "github:event:1"
    assert items[0].source_type == SourceType.GITHUB
    assert "pushed 2 commit(s)" in items[0].title
    assert items[0].metadata["event_type"] == "PushEvent"


def test_disabled_source_is_skipped() -> None:
    source = GitHubSourceConfig(type="user_events", username="octocat", enabled=False)
    scraper = GitHubScraper([source], _client_returning([_push_event()]))
    since = datetime(2026, 1, 1, tzinfo=timezone.utc)
    assert asyncio.run(scraper.fetch(since)) == []


def test_parse_event_variants() -> None:
    scraper = GitHubScraper([], AsyncMock())
    base = {"id": "x", "created_at": "2026-01-02T00:00:00Z", "repo": {"name": "o/r"}}

    create = scraper._parse_event(
        {**base, "type": "CreateEvent", "payload": {"ref_type": "branch", "description": "d"}},
        "octocat",
    )
    assert "created branch" in create.title

    release = scraper._parse_event(
        {
            **base,
            "type": "ReleaseEvent",
            "payload": {"release": {"tag_name": "v1", "body": "notes", "html_url": "https://gh/rel"}},
        },
        "octocat",
    )
    assert "released v1" in release.title
    assert str(release.url) == "https://gh/rel"

    public = scraper._parse_event({**base, "type": "PublicEvent", "payload": {}}, "octocat")
    assert "made o/r public" in public.title

    watch = scraper._parse_event({**base, "type": "WatchEvent", "payload": {}}, "octocat")
    assert "starred o/r" in watch.title

    unknown = scraper._parse_event({**base, "type": "ForkEvent", "payload": {}}, "octocat")
    assert unknown is None


def test_fetch_repo_releases() -> None:
    releases = [
        {
            "id": 10,
            "tag_name": "v2.0",
            "html_url": "https://github.com/o/r/releases/v2.0",
            "body": "changelog",
            "author": {"login": "maintainer"},
            "published_at": "2026-01-05T00:00:00Z",
            "prerelease": False,
        },
        # Too old.
        {
            "id": 11,
            "tag_name": "v1.0",
            "html_url": "https://github.com/o/r/releases/v1.0",
            "author": {"login": "maintainer"},
            "published_at": "2025-01-01T00:00:00Z",
        },
    ]
    source = GitHubSourceConfig(type="repo_releases", owner="o", repo="r")
    scraper = GitHubScraper([source], _client_returning(releases))
    since = datetime(2026, 1, 1, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))
    assert len(items) == 1
    assert items[0].id == "github:release:10"
    assert items[0].metadata["tag"] == "v2.0"
    assert items[0].author == "maintainer"


def test_fetch_user_events_handles_http_error() -> None:
    client = AsyncMock()
    client.get.side_effect = httpx.HTTPError("boom")
    source = GitHubSourceConfig(type="user_events", username="octocat")
    scraper = GitHubScraper([source], client)
    since = datetime(2026, 1, 1, tzinfo=timezone.utc)
    assert asyncio.run(scraper.fetch(since)) == []
