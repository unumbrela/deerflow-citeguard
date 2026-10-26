import time

import httpx
import pytest
from helpers import atom_feed, paper

from deerflow_extension_scholar import arxiv


def test_phrase_vs_all_terms_query():
    assert arxiv.build_search_query("a b", None, None, None) == 'all:"a b"'
    assert arxiv.build_search_query("a b", "cs.CL", None, None, "all_terms") == "(all:a AND all:b) AND cat:cs.CL"
    assert arxiv.build_search_query("agents", None, "2024-10-25", None) == "all:agents AND submittedDate:[202410250000 TO 299912312359]"


def test_normalise_id():
    assert arxiv.normalise_id("http://arxiv.org/abs/1706.03762v5") == "1706.03762"
    assert arxiv.normalise_id("http://arxiv.org/abs/hep-th/9901001v1") == "hep-th/9901001"
    assert arxiv.normalise_id("http://arxiv.org/abs/1706.03762") == "1706.03762"


def test_parse_feed_extracts_fields():
    [p] = arxiv.parse_feed(atom_feed([paper(7)]))
    assert p["id"] == "2501.00007"
    assert p["title"] == "Benchmarking Agents Part 7"
    assert p["authors"] == ["Alice Smith7", "Bob Jones0"]
    assert p["published"] == "2025-01-02"
    assert p["primary_category"] == "cs.CL"
    assert p["abstract"] == "x" * 800
    assert p["pdf_url"].endswith("2501.00007v2")


async def _fetch(handler, *, budget=20.0, monkeypatch=None):
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        return await arxiv.fetch(client, query="a b", max_results=5, category="cs.CL", start_date=None, end_date=None, match="phrase", deadline=time.monotonic() + budget)


@pytest.fixture
def no_sleep(monkeypatch):
    slept = []

    async def fake_sleep(seconds):
        slept.append(seconds)

    monkeypatch.setattr(arxiv.asyncio, "sleep", fake_sleep)
    return slept


async def test_retries_rate_limit_then_succeeds(no_sleep):
    calls = []

    def handler(request):
        calls.append(request)
        if len(calls) < 3:
            return httpx.Response(429, headers={"Retry-After": "2"})
        return httpx.Response(200, text=atom_feed([paper(1)]))

    found = await _fetch(handler)
    assert [p["id"] for p in found] == ["2501.00001"]
    assert len(calls) == 3 and no_sleep == [2.0, 2.0]
    assert calls[0].url.params["search_query"] == 'all:"a b" AND cat:cs.CL'


async def test_client_error_is_not_retried(no_sleep):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(400)

    with pytest.raises(arxiv.ArxivError, match="HTTP 400"):
        await _fetch(handler)
    assert len(calls) == 1


async def test_gives_up_inside_the_time_budget(no_sleep):
    def handler(request):
        return httpx.Response(503, headers={"Retry-After": "30"})

    with pytest.raises(arxiv.ArxivError, match="HTTP 503"):
        await _fetch(handler, budget=20.0)
    assert no_sleep == []  # waiting 30 s would overrun the 20 s budget


async def test_transport_error_is_retried(no_sleep):
    calls = []

    def handler(request):
        calls.append(request)
        if len(calls) == 1:
            raise httpx.ConnectError("boom")
        return httpx.Response(200, text=atom_feed([]))

    assert await _fetch(handler) == []
    assert len(calls) == 2
