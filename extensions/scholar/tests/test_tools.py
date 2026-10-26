import json
from datetime import date
from types import MappingProxyType

import httpx
import pytest
from deerflow_extension_api.auth import ExtensionPrincipal
from deerflow_extension_api.plugins import ToolContext
from helpers import atom_feed, paper

from deerflow_extension_scholar import arxiv, build_tools
from deerflow_extension_scholar.store import PaperStore

THREAD = "0f8e3c2a-1111-4222-8333-444455556666"


def ctx(user="alice", thread=THREAD):
    return ToolContext(ExtensionPrincipal(user), MappingProxyType({"enabled": True}), thread)


@pytest.fixture
def store(tmp_path):
    return PaperStore(str(tmp_path / "scholar"))


def tools(store, handler):
    search, get_batch = build_tools(store, transport=httpx.MockTransport(handler), today=lambda: date(2026, 10, 25), pause=0)
    return search.handler, get_batch.handler


async def test_search_stores_results_and_returns_compact_index(store):
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(200, text=atom_feed([paper(i, abstract_chars=1500) for i in range(12)]))

    search, get_batch = tools(store, handler)
    result = await search(MappingProxyType({"query": "agent evaluation", "max_results": 10, "category": "cs.CL", "years": 2}), ctx())
    summary = json.loads(result.content)
    assert summary["count"] == 10 and summary["match"] == "phrase"
    assert summary["window"] == {"start": "2024-10-25", "end": None}
    assert "submittedDate:[202410250000" in requests[0].url.params["search_query"]
    assert len(result.content) < 12000 and "abstract" not in result.content
    assert sum(len(b["ids"]) for b in summary["batches"]) == 10

    first = await get_batch(MappingProxyType({"batch": 1}), ctx())
    papers = json.loads(first.content)
    assert papers[0]["id"] == "2501.00000" and papers[0]["abstract"] == "x" * 1500
    assert len(first.content) < 12000


async def test_shortfall_is_stated_not_padded(store):
    search, _ = tools(store, lambda r: httpx.Response(200, text=atom_feed([paper(1)])))
    summary = json.loads((await search(MappingProxyType({"query": "agents", "max_results": 10}), ctx())).content)
    assert summary["count"] == 1 and "Do not pad" in summary["note"]


async def test_arxiv_failure_becomes_an_explicit_error(store, monkeypatch):
    async def no_sleep(seconds):
        return None

    monkeypatch.setattr(arxiv.asyncio, "sleep", no_sleep)
    search, _ = tools(store, lambda r: httpx.Response(400))
    result = await search(MappingProxyType({"query": "agents", "max_results": 10}), ctx())
    assert result.content.startswith("ERROR: arXiv returned HTTP 400")
    assert store.load_search(THREAD) is None


async def test_get_batch_requires_a_search_and_the_same_owner(store):
    search, get_batch = tools(store, lambda r: httpx.Response(200, text=atom_feed([paper(1)])))
    assert "call the scholar search tool first" in (await get_batch(MappingProxyType({"batch": 1}), ctx())).content
    await search(MappingProxyType({"query": "agents", "max_results": 1}), ctx())
    assert "another user" in (await get_batch(MappingProxyType({"batch": 1}), ctx(user="mallory"))).content
    assert "does not exist" in (await get_batch(MappingProxyType({"batch": 2}), ctx())).content
