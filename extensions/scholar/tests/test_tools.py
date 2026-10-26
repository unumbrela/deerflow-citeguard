import json
from datetime import date
from types import MappingProxyType

import httpx
import pytest
from deerflow_extension_api import ModelInvocationFailed, ModelInvocationResult, ModelUsage
from deerflow_extension_api.auth import ExtensionPrincipal
from deerflow_extension_api.plugins import ToolContext
from helpers import atom_feed, paper

from deerflow_extension_scholar import Screener, arxiv, build_tools
from deerflow_extension_scholar.store import PaperStore

THREAD = "0f8e3c2a-1111-4222-8333-444455556666"


def ctx(user="alice", thread=THREAD):
    return ToolContext(ExtensionPrincipal(user), MappingProxyType({"enabled": True}), thread)


@pytest.fixture
def store(tmp_path):
    return PaperStore(str(tmp_path / "scholar"))


class FakeInvoker:
    """Scores papers by a fixed table, as the host's model invoker would return them."""

    def __init__(self, scores=None, fail=False):
        self.scores, self.fail, self.requests = scores or {}, fail, []

    async def invoke(self, request):
        self.requests.append(request)
        if self.fail:
            raise ModelInvocationFailed("Model invocation timed out")
        ids = [line.split(": ", 1)[1] for line in request.messages[0].content.splitlines() if line.startswith("id: ")]
        data = {"scores": [{"id": i, "score": self.scores.get(i, 3), "reason": "test"} for i in ids] + [{"id": "9999.99999", "score": 3}]}
        return ModelInvocationResult(content=json.dumps(data), structured_output=data, usage=ModelUsage(total_tokens=100))


def screener(invoker=None):
    s = Screener()
    s.invoker = invoker
    return s


def tools(store, handler, invoker=None, expand=True):
    search, screen, get_batch = build_tools(store, transport=httpx.MockTransport(handler), today=lambda: date(2026, 10, 25), pause=0, screener=screener(invoker), expand=expand)
    return search.handler, screen.handler, get_batch.handler


def routes(pool, refs=None, referenced=(), requests=None):
    """arXiv search -> ``pool``; Semantic Scholar -> ``refs``; arXiv id_list -> ``referenced``."""

    def handler(request):
        if requests is not None:
            requests.append(request)
        if request.url.host == "api.semanticscholar.org":
            ids = [i.removeprefix("arXiv:") for i in json.loads(request.content)["ids"]]
            return httpx.Response(200, json=[{"references": [{"externalIds": {"ArXiv": r}} for r in (refs or {}).get(i, [])]} for i in ids])
        if "id_list" in request.url.params:
            wanted = request.url.params["id_list"].split(",")
            return httpx.Response(200, text=atom_feed([p for p in referenced if p["id"] in wanted]))
        return httpx.Response(200, text=atom_feed(pool))

    return handler


def ref_paper(i, primary="cs.CL", published="2025-06-01"):
    return {**paper(i, primary), "id": f"2506.{i:05d}", "published": published, "abs_url": f"http://arxiv.org/abs/2506.{i:05d}v1"}


SEARCH = MappingProxyType({"query": "agent evaluation", "max_results": 3, "category": "cs.CL", "years": 2})
TOPIC = MappingProxyType({"topic": "Agent evaluation"})


async def test_search_then_screen_selects_cocited_central_papers(store):
    requests = []
    pool = [paper(i) for i in range(6)]
    # Every pool paper cites 2506.00001 (in scope); 2506.00002 is cs.CV; 2506.00003 is outside the window.
    common = ["2506.00001", "2506.00002", "2506.00003", "2501.00004"]
    refs = {p["id"]: common for p in pool}
    referenced = [ref_paper(1), ref_paper(2, "cs.CV"), ref_paper(3, published="2020-01-01")]
    invoker = FakeInvoker({"2501.00004": 0})
    search, screen, get_batch = tools(store, routes(pool, refs, referenced, requests), invoker)

    summary = json.loads((await search(SEARCH, ctx())).content)
    assert summary["pool"] == 6 and summary["shortlist"] == 7 and "screen" in summary["next"]
    assert summary["citation_expansion"] == {"status": "ok", "pool_papers_with_references": 6, "cached": 0, "references_checked": 3, "added": 1}
    assert summary["report_dates"]["published_between"] == ["2024-10-25", "2026-10-25"]
    assert requests[0].url.params["max_results"] == "100"  # pool, over-fetched for the primary filter
    assert "not been selected" in (await get_batch(MappingProxyType({"batch": 1}), ctx())).content

    result = json.loads((await screen(TOPIC, ctx())).content)
    # 2506.00001 is cited by all 6, then 2501.00004 by 5 (but scored off-topic), then the pool in arXiv order.
    assert [row["id"] for row in result["index"]] == ["2506.00001", "2501.00000", "2501.00001"]
    assert result["index"][0]["cited_by"] == 6
    assert result["screening"] == {"identified_by_search": 6, "added_from_references": 1, "shortlisted": 7, "screened": 7, "scores": {"0": 1, "1": 0, "2": 0, "3": 6}, "included": 3, "included_from_references": 1}
    assert "Agent evaluation" in invoker.requests[0].messages[0].content
    papers = json.loads((await get_batch(MappingProxyType({"batch": 1}), ctx())).content)
    assert papers[0]["id"] == "2506.00001" and papers[0]["abstract"]

    stored = store.load_search(THREAD)
    assert [p["id"] for p in stored["papers"]] == ["2506.00001", "2501.00000", "2501.00001"]
    assert {r["id"]: r["included"] for r in stored["screening"]["table"]}["2501.00004"] is False
    # Screening again returns the stored selection without calling the model.
    await screen(TOPIC, ctx())
    assert len(invoker.requests) == 1


async def test_screen_without_a_model_grant_falls_back_to_cocitation_order(store):
    search, screen, _ = tools(store, routes([paper(i) for i in range(5)]))
    await search(SEARCH, ctx())
    result = json.loads((await screen(TOPIC, ctx())).content)
    assert [row["id"] for row in result["index"]] == ["2501.00000", "2501.00001", "2501.00002"]
    assert "unavailable" in result["note"] and store.load_search(THREAD)["screening"]["status"] == "unavailable"


async def test_failed_model_calls_do_not_fail_the_review(store):
    search, screen, _ = tools(store, routes([paper(i) for i in range(5)]), FakeInvoker(fail=True))
    await search(SEARCH, ctx())
    result = json.loads((await screen(TOPIC, ctx())).content)
    assert result["count"] == 3 and "unavailable" in result["note"]
    assert store.load_search(THREAD)["screening"]["failed_batches"] == 1


async def test_semantic_scholar_outage_means_no_expansion_not_a_failed_search(store, monkeypatch):
    async def no_sleep(seconds):
        return None

    monkeypatch.setattr("deerflow_extension_scholar.s2.asyncio.sleep", no_sleep)

    def handler(request):
        if request.url.host == "api.semanticscholar.org":
            return httpx.Response(403)
        return httpx.Response(200, text=atom_feed([paper(i) for i in range(4)]))

    search, _, _ = tools(store, handler)
    summary = json.loads((await search(SEARCH, ctx())).content)
    assert summary["pool"] == 4 and summary["citation_expansion"]["status"] == "unavailable"


async def test_references_are_cached_across_threads(store):
    requests = []
    pool = [paper(i) for i in range(3)]
    handler = routes(pool, {p["id"]: ["2506.00001"] for p in pool}, [ref_paper(1)], requests)
    search, _, _ = tools(store, handler)
    await search(SEARCH, ctx())
    other = "1f8e3c2a-1111-4222-8333-444455556666"
    summary = json.loads((await search(SEARCH, ctx(thread=other))).content)
    assert summary["citation_expansion"]["cached"] == 3 and summary["citation_expansion"]["added"] == 1
    assert sum(r.url.host == "api.semanticscholar.org" for r in requests) == 1


async def test_screen_retries_expansion_that_was_throttled_during_search(store, monkeypatch):
    async def no_sleep(seconds):
        return None

    monkeypatch.setattr("deerflow_extension_scholar.s2.asyncio.sleep", no_sleep)
    throttled = [True]
    pool = [paper(i) for i in range(3)]
    ok = routes(pool, {p["id"]: ["2506.00001"] for p in pool}, [ref_paper(1)])

    def handler(request):
        if request.url.host == "api.semanticscholar.org" and throttled[0]:
            return httpx.Response(429)
        return ok(request)

    search, screen, _ = tools(store, handler, FakeInvoker())
    summary = json.loads((await search(SEARCH, ctx())).content)
    assert summary["citation_expansion"]["status"] == "unavailable"
    throttled[0] = False
    result = json.loads((await screen(TOPIC, ctx())).content)
    assert result["index"][0]["id"] == "2506.00001" and result["screening"]["added_from_references"] == 1
    assert store.load_search(THREAD)["expansion"]["retried_in_screen"] is True


async def test_expansion_can_be_switched_off(store):
    requests = []
    search, _, _ = tools(store, routes([paper(i) for i in range(4)], requests=requests), expand=False)
    summary = json.loads((await search(SEARCH, ctx())).content)
    assert summary["citation_expansion"]["status"] == "off"
    assert all(r.url.host == "export.arxiv.org" for r in requests)


async def test_shortfall_is_stated_not_padded(store):
    search, screen, _ = tools(store, routes([paper(1)]), FakeInvoker())
    assert "Do not pad" in json.loads((await search(MappingProxyType({"query": "agents", "max_results": 10}), ctx())).content)["note"]
    result = json.loads((await screen(TOPIC, ctx())).content)
    assert result["count"] == 1 and "Do not pad" in result["note"]


async def test_arxiv_failure_becomes_an_explicit_error(store, monkeypatch):
    async def no_sleep(seconds):
        return None

    monkeypatch.setattr(arxiv.asyncio, "sleep", no_sleep)
    search, _, _ = tools(store, lambda r: httpx.Response(400))
    result = await search(MappingProxyType({"query": "agents", "max_results": 10}), ctx())
    assert result.content.startswith("ERROR: arXiv returned HTTP 400")
    assert store.load_search(THREAD) is None


async def test_screen_and_get_batch_require_a_search_and_the_same_owner(store):
    search, screen, get_batch = tools(store, routes([paper(1)]), FakeInvoker())
    assert "call the scholar search tool first" in (await get_batch(MappingProxyType({"batch": 1}), ctx())).content
    assert "call the scholar search tool first" in (await screen(TOPIC, ctx())).content
    await search(MappingProxyType({"query": "agents", "max_results": 1}), ctx())
    assert "another user" in (await screen(TOPIC, ctx(user="mallory"))).content
    await screen(TOPIC, ctx())
    assert "another user" in (await get_batch(MappingProxyType({"batch": 1}), ctx(user="mallory"))).content
    assert "does not exist" in (await get_batch(MappingProxyType({"batch": 2}), ctx())).content


async def test_screen_and_get_batch_refuse_a_rejected_search(store):
    search, screen, get_batch = tools(store, routes([paper(1)]), FakeInvoker())
    await search(MappingProxyType({"query": "agents", "max_results": 1}), ctx())
    store.save_search(THREAD, {**store.load_search(THREAD), "rejected": "the user asked for category cs.CL; search again with it"})
    assert "latest search was rejected" in (await screen(TOPIC, ctx())).content
    assert "latest search was rejected" in (await get_batch(MappingProxyType({"batch": 1}), ctx())).content


async def test_category_case_is_normalised(store):
    requests = []
    search, _, _ = tools(store, routes([paper(1)], requests=requests), expand=False)
    summary = json.loads((await search(MappingProxyType({"query": "agents", "max_results": 1, "category": "cs.cl"}), ctx())).content)
    assert summary["pool"] == 1 and summary["category"] == "cs.CL"
    assert "cat:cs.CL" in requests[0].url.params["search_query"]


async def test_index_and_batches_stay_under_externalize_threshold(store):
    pool = [paper(i, abstract_chars=1500) for i in range(60)]
    search, screen, get_batch = tools(store, routes(pool), FakeInvoker())
    await search(MappingProxyType({"query": "agents", "max_results": 50}), ctx())
    result = await screen(TOPIC, ctx())
    assert json.loads(result.content)["count"] == 50 and len(result.content) < 12000
    assert len((await get_batch(MappingProxyType({"batch": 1}), ctx())).content) < 12000
