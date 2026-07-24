from __future__ import annotations

import json
from unittest.mock import MagicMock

import httpx
import pytest

from src.setup import presets as presets_mod
from src.setup.presets import (
    _source_unique_key,
    _transform_api_response,
    collect_sources_from_domains,
    fetch_presets,
    load_presets,
    match_domains,
    match_sources,
)


SAMPLE_PRESETS = {
    "domains": [
        {
            "id": "ai-ml",
            "name": "AI / ML",
            "keywords": ["ai", "machine learning", "llm"],
            "sources": [
                {
                    "type": "rss",
                    "description": "Latest research on large language models",
                    "tags": ["ai", "research"],
                    "config": {"url": "https://example.com/ai.xml"},
                },
                {
                    "type": "reddit_subreddit",
                    "description": "ML community discussion",
                    "tags": ["ml"],
                    "config": {"subreddit": "MachineLearning"},
                },
            ],
        },
        {
            "id": "web",
            "name": "Web Dev",
            "keywords": ["javascript", "frontend"],
            "sources": [
                {
                    "type": "rss",
                    "description": "Frontend news",
                    "tags": ["frontend"],
                    "config": {"url": "https://example.com/web.xml"},
                },
            ],
        },
    ]
}


def test_match_domains_scores_and_sorts() -> None:
    results = match_domains("I love ai and llm topics", SAMPLE_PRESETS)
    assert results
    top_domain, top_score = results[0]
    assert top_domain["id"] == "ai-ml"
    assert top_score > 0
    # Descending sort by score
    scores = [score for _, score in results]
    assert scores == sorted(scores, reverse=True)


def test_match_domains_threshold_filters_out_weak_matches() -> None:
    results = match_domains("cooking recipes", SAMPLE_PRESETS, threshold=0.5)
    assert results == []


def test_match_domains_tag_contributes_partial_score() -> None:
    # "research" is only a source tag, not a domain keyword.
    results = match_domains("research", SAMPLE_PRESETS, threshold=0.01)
    ids = {d["id"] for d, _ in results}
    assert "ai-ml" in ids


def test_collect_sources_dedups_and_tags_origin() -> None:
    matched = match_domains("ai javascript", SAMPLE_PRESETS, threshold=0.01)
    sources = collect_sources_from_domains(matched)
    # Three unique sources across the two domains.
    assert len(sources) == 3
    assert all(s["origin"] == "preset" for s in sources)
    keys = {_source_unique_key(s) for s in sources}
    assert len(keys) == 3


def test_match_sources_returns_individual_sources() -> None:
    results = match_sources("machine learning research", SAMPLE_PRESETS, threshold=0.01)
    assert results
    for src, score in results:
        assert src["origin"] == "preset"
        assert score > 0
    scores = [s for _, s in results]
    assert scores == sorted(scores, reverse=True)


def test_match_sources_dedups_across_domains() -> None:
    presets = {
        "domains": [
            {"id": "a", "keywords": ["x"], "sources": [
                {"type": "rss", "config": {"url": "https://dup.com/f.xml"}, "tags": ["x"]},
            ]},
            {"id": "b", "keywords": ["x"], "sources": [
                {"type": "rss", "config": {"url": "https://dup.com/f.xml"}, "tags": ["x"]},
            ]},
        ]
    }
    results = match_sources("x", presets, threshold=0.0)
    keys = [_source_unique_key(s) for s, _ in results]
    assert len(keys) == len(set(keys))


@pytest.mark.parametrize(
    "source, expected",
    [
        ({"type": "rss", "config": {"url": "u"}}, "rss:u"),
        ({"type": "reddit_subreddit", "config": {"subreddit": "s"}}, "reddit:s"),
        ({"type": "reddit_user", "config": {"username": "u"}}, "reddit_user:u"),
        ({"type": "github_user", "config": {"username": "u"}}, "github_user:u"),
        ({"type": "github_repo", "config": {"owner": "o", "repo": "r"}}, "github_repo:o/r"),
        ({"type": "telegram", "config": {"channel": "c"}}, "telegram:c"),
    ],
)
def test_source_unique_key_known_types(source, expected) -> None:
    assert _source_unique_key(source) == expected


def test_source_unique_key_fallback_is_stable() -> None:
    src = {"type": "custom", "config": {"b": 2, "a": 1}}
    key1 = _source_unique_key(src)
    key2 = _source_unique_key({"type": "custom", "config": {"a": 1, "b": 2}})
    assert key1 == key2
    assert key1.startswith("custom:")


def test_transform_api_response_maps_fields() -> None:
    api_data = {
        "categories": [
            {
                "id": "AI_ML",
                "name": "AI & ML",
                "keywords": ["ai"],
                "sources": [
                    {
                        "type": "rss",
                        "name": "My Feed",
                        "description": "desc",
                        "tags": ["ai"],
                        "config": {"url": "https://x.com/f.xml"},
                    },
                    {
                        "type": "github_user",
                        "description": "gh",
                        "config": {"username": "octocat", "subtype": "user"},
                    },
                ],
            }
        ]
    }
    result = _transform_api_response(api_data)
    domain = result["domains"][0]
    assert domain["id"] == "ai-ml"
    rss_src = domain["sources"][0]
    # RSS name is injected into config.
    assert rss_src["config"]["name"] == "My Feed"
    gh_src = domain["sources"][1]
    # Internal subtype is stripped for github sources.
    assert "subtype" not in gh_src["config"]


def test_load_presets_offline_reads_local_file(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("HORIZON_OFFLINE", "1")
    path = tmp_path / "presets.json"
    path.write_text(json.dumps(SAMPLE_PRESETS), encoding="utf-8")
    loaded = load_presets(presets_path=str(path))
    assert loaded == SAMPLE_PRESETS


def test_load_presets_raises_when_file_missing(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("HORIZON_OFFLINE", "1")
    with pytest.raises(FileNotFoundError):
        load_presets(presets_path=str(tmp_path / "nope.json"))


def test_load_presets_prefers_api(monkeypatch) -> None:
    monkeypatch.delenv("HORIZON_OFFLINE", raising=False)
    api_result = {"domains": [{"id": "from-api"}]}
    monkeypatch.setattr(presets_mod, "fetch_presets", lambda: api_result)
    assert load_presets() == api_result


def test_fetch_presets_success(monkeypatch) -> None:
    response = MagicMock()
    response.raise_for_status.return_value = None
    response.json.return_value = {
        "categories": [
            {"id": "WEB", "name": "Web", "keywords": [], "sources": []}
        ]
    }
    monkeypatch.setattr(httpx, "get", lambda *a, **k: response)
    result = fetch_presets()
    assert result is not None
    assert result["domains"][0]["id"] == "web"


def test_fetch_presets_missing_categories_returns_none(monkeypatch) -> None:
    response = MagicMock()
    response.raise_for_status.return_value = None
    response.json.return_value = {"unexpected": True}
    monkeypatch.setattr(httpx, "get", lambda *a, **k: response)
    assert fetch_presets() is None


def test_fetch_presets_http_error_returns_none(monkeypatch) -> None:
    def _raise(*a, **k):
        raise httpx.ConnectError("boom")

    monkeypatch.setattr(httpx, "get", _raise)
    assert fetch_presets() is None
