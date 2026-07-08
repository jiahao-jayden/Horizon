from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock
from unittest.mock import MagicMock

from src.models import BAAIHubConfig, SourceType
from src.scrapers.baaihub import BAAIHubScraper


def test_baaihub_scraper_parses_nuxt_payload() -> None:
    html = """
    <html><body>
    <script>window.__NUXT__=(function(a,b,c,d){return {data:[{resources:{data:[{story_info:{id:b,title:"智源\\u002F测试",created_at:c,url:"https:\\u002F\\u002Fexample.com\\u002Fa",content:"正文",summary:"摘要",story_show_user_name:d,host:"mp.weixin.qq.com",tag_names:[{title:"AI",id:1}]},is_event:a,story_id:b}],pageIndex:1}}]}}(false,56169,"2026-07-08 13:30 分享","智源社区助手"));</script>
    </body></html>
    """
    response = MagicMock()
    response.text = html
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    config = BAAIHubConfig(enabled=True)
    scraper = BAAIHubScraper(config, client)
    since = datetime(2026, 7, 8, 0, 0, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))

    assert len(items) == 1
    assert items[0].id == "baaihub:story:56169"
    assert items[0].source_type == SourceType.BAAIHUB
    assert items[0].title == "智源/测试"
    assert str(items[0].url) == "https://example.com/a"
    assert items[0].author == "智源社区助手"
    assert items[0].published_at == datetime(2026, 7, 8, 5, 30, tzinfo=timezone.utc)
    assert items[0].metadata["tags"] == ["AI"]
    assert items[0].metadata["hub_url"] == "https://hub.baai.ac.cn/view/56169"


def test_baaihub_scraper_filters_old_items() -> None:
    html = """
    <html><body>
    <script>window.__NUXT__=(function(a,b,c){return {data:[{resources:{data:[{story_info:{id:b,title:"Old",created_at:c,url:"https:\\u002F\\u002Fexample.com\\u002Fold",content:"正文",summary:"摘要",tag_names:[]},is_event:a,story_id:b}],pageIndex:1}}]}}(false,1,"2026-07-07 10:00 分享"));</script>
    </body></html>
    """
    response = MagicMock()
    response.text = html
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    config = BAAIHubConfig(enabled=True)
    scraper = BAAIHubScraper(config, client)
    since = datetime(2026, 7, 8, 0, 0, tzinfo=timezone.utc)

    assert asyncio.run(scraper.fetch(since)) == []
