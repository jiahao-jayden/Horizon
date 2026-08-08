from __future__ import annotations

import asyncio
import json

from src.models import AIConfig, AIProvider
from src.setup import ai_recommend


def _ai_config() -> AIConfig:
    return AIConfig(
        provider=AIProvider.OPENAI,
        model="gpt-4o",
        api_key_env="OPENAI_API_KEY",
    )


class _FakeClient:
    def __init__(self, response: str) -> None:
        self._response = response

    async def complete(self, system: str, user: str) -> str:
        return self._response


def test_get_ai_recommendations_tags_origin(monkeypatch) -> None:
    payload = json.dumps({"sources": [{"type": "rss", "config": {"url": "u"}}]})
    monkeypatch.setattr(
        ai_recommend, "create_ai_client", lambda cfg: _FakeClient(payload)
    )
    result = asyncio.run(
        ai_recommend.get_ai_recommendations(_ai_config(), "ai news", [])
    )
    assert len(result) == 1
    assert result[0]["origin"] == "ai"


def test_get_ai_recommendations_formats_existing_sources(monkeypatch) -> None:
    captured = {}

    class _CapturingClient:
        async def complete(self, system: str, user: str) -> str:
            captured["user"] = user
            return json.dumps({"sources": []})

    monkeypatch.setattr(
        ai_recommend, "create_ai_client", lambda cfg: _CapturingClient()
    )
    existing = [{"type": "reddit", "description": "ML subreddit"}]
    asyncio.run(ai_recommend.get_ai_recommendations(_ai_config(), "ml", existing))
    assert "ML subreddit" in captured["user"]


def test_get_ai_recommendations_client_creation_failure(monkeypatch) -> None:
    def _boom(cfg):
        raise ValueError("bad config")

    monkeypatch.setattr(ai_recommend, "create_ai_client", _boom)
    assert asyncio.run(ai_recommend.get_ai_recommendations(_ai_config(), "x", [])) == []


def test_get_ai_recommendations_complete_error(monkeypatch) -> None:
    class _FailingClient:
        async def complete(self, system: str, user: str) -> str:
            raise RuntimeError("api down")

    monkeypatch.setattr(
        ai_recommend, "create_ai_client", lambda cfg: _FailingClient()
    )
    assert asyncio.run(ai_recommend.get_ai_recommendations(_ai_config(), "x", [])) == []


def test_get_ai_recommendations_unparseable_response(monkeypatch) -> None:
    monkeypatch.setattr(
        ai_recommend, "create_ai_client", lambda cfg: _FakeClient("not json")
    )
    assert asyncio.run(ai_recommend.get_ai_recommendations(_ai_config(), "x", [])) == []


def test_get_ai_recommendations_sync_wrapper(monkeypatch) -> None:
    payload = json.dumps({"sources": [{"type": "rss", "config": {}}]})
    monkeypatch.setattr(
        ai_recommend, "create_ai_client", lambda cfg: _FakeClient(payload)
    )
    result = ai_recommend.get_ai_recommendations_sync(_ai_config(), "ai", [])
    assert result[0]["origin"] == "ai"
