"""Scholar plugin: arXiv search, screening and batch tools plus a citation gate. No imports from DeerFlow host internals.

- ``search``: query arXiv inside the Gateway (no ``allow_host_bash``) for a
  50-paper candidate pool, filtered by date window and primary category in
  code; add the in-scope papers the pool cites (Semantic Scholar references)
  and shortlist the most co-cited candidates.
- ``screen``: a model scores each shortlisted paper for how central it is to
  the topic; code selects the papers for the review and stores the screening
  table.
- ``get_batch``: hand one batch of selected papers to a subagent, so paper data
  never passes through the lead model's own words.
- ``CitationGateMiddleware``: reject a presented report whose arXiv ids did not
  come from this thread's search.
"""

from __future__ import annotations

import asyncio
import json
import time
import uuid
from collections.abc import Mapping, Sequence
from datetime import date
from typing import Any

import httpx
from deerflow_extension_api import (
    AgentBuildContext,
    AgentScope,
    ExtensionData,
    ExtensionRegistry,
    MiddlewarePlacement,
    ModelTool,
    Placement,
    PluginContribution,
    PluginToolResult,
    extension,
)

from . import arxiv, s2
from .core import (
    POOL_SIZE,
    batch_paper,
    cocitation_counts,
    compact_index,
    in_scope,
    in_window,
    make_batches,
    normalise_category,
    rank_candidates,
    refs_to_fetch,
    resolve_window,
    select_papers,
    select_screened,
    shortlist_size,
)
from .gate import CitationGateMiddleware
from .screening import Screener
from .store import PaperStore

NAMESPACE = "community.scholar"
SEARCH_BUDGET_SECONDS = 25.0  # the host cancels a plugin tool call at 30 s
ARXIV_PAUSE_SECONDS = 3.0  # arXiv asks for at least 3 s between calls
EXPANSION_MIN_SECONDS = 8.0  # skip citation expansion when less is left of the budget
SCREEN_EXPANSION_SECONDS = 12.0  # a retry inside screen leaves the rest of its budget to the model calls

SEARCH_DESCRIPTION = (
    "Search arXiv for a literature review. Builds a candidate pool in code: arXiv matches plus the papers they cite, "
    "filtered by submission date window and PRIMARY arXiv category, and shortlists the candidates the field cites most. "
    "Next, call the scholar screen tool: it selects the papers for the review and returns their index and batch numbers. "
    "Keep `query` to 2-3 core keywords; put the field in `category` and time in `years`. "
    "Never drop or change `category` or `years` to get more papers; if fewer papers come back, that is the real result size."
)
SEARCH_SCHEMA = {
    "type": "object",
    "properties": {
        "query": {"type": "string", "minLength": 2, "maxLength": 200, "description": "2-3 core keywords, e.g. 'agent evaluation'."},
        "max_results": {"type": "integer", "minimum": 1, "maximum": 50, "description": "Number of papers requested by the user (the review's size, not the pool's)."},
        "category": {"type": "string", "pattern": "^[a-z-]+(\\.[A-Za-z-]+)?$", "description": "arXiv category such as cs.CL; matched against the primary category."},
        "include_cross_lists": {"type": "boolean", "description": "Also accept papers only cross-listed in `category`. Only if the user explicitly accepts that."},
        "years": {"type": "integer", "minimum": 1, "maximum": 40, "description": "Only papers submitted in the last N years (computed from today in code)."},
        "start_date": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$", "description": "YYYY-MM-DD; overrides `years`."},
        "end_date": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$", "description": "YYYY-MM-DD."},
    },
    "required": ["query", "max_results"],
    "additionalProperties": False,
}

SCREEN_DESCRIPTION = (
    "Select the papers for the review from the shortlist of the latest scholar search. A model scores each shortlisted paper "
    "for how central it is to the topic; code keeps the most co-cited central papers, up to the requested count. "
    "Returns the index of selected papers (id, short title, first author, date, category), the screening counts for the "
    "report's methodology section, and the batch numbers to hand to subagents. The index is the only list of papers that exists: "
    "never cite a paper that is not in it."
)
SCREEN_SCHEMA = {
    "type": "object",
    "properties": {
        "topic": {"type": "string", "minLength": 2, "maxLength": 300, "description": "The research topic in the user's own words, e.g. 'World Models for Robotic Manipulation'."},
        "criteria": {"type": "string", "maxLength": 500, "description": "Inclusion criteria the user stated beyond topic, date and category, if any."},
    },
    "required": ["topic"],
    "additionalProperties": False,
}

BATCH_DESCRIPTION = (
    "Return one batch of the papers selected by the scholar screen tool in this conversation, as a JSON array "
    "(id, title, authors, published, primary_category, abs_url, abstract). Use this instead of re-typing paper data: "
    "work only from what it returns."
)
BATCH_SCHEMA = {
    "type": "object",
    "properties": {"batch": {"type": "integer", "minimum": 1, "maximum": 50, "description": "Batch number from the search result."}},
    "required": ["batch"],
    "additionalProperties": False,
}


def _error(message: str) -> PluginToolResult:
    return PluginToolResult(content=f"ERROR: {message}", artifact=None)


def _owned_search(store: PaperStore, context: Any) -> tuple[dict | None, str | None]:
    if not context.thread_id:
        return None, "no conversation context"
    search = store.load_search(context.thread_id)
    if search is None:
        return None, "no search has been run in this conversation; call the scholar search tool first"
    if search.get("owner") != context.principal.user_id:
        return None, "the stored search belongs to another user"
    return search, None


def _shortfall_note(count: int, requested: int) -> str | None:
    if not count:
        return "0 papers matched. Tell the user and suggest broadening the topic or removing the category; do not relax the filters yourself."
    if count < requested:
        return "Fewer papers than requested under the user's constraints. Do not pad; state the shortfall in the report."
    return None


async def _expand(
    client: httpx.AsyncClient, store: PaperStore, pool: list[dict], window: dict, category: str | None, include_cross_lists: bool, *, deadline: float, pause: float, s2_api_key: str | None
) -> tuple[list[dict], dict[str, int], dict]:
    """In-scope papers the pool cites, and how many pool papers cite each. Failure means no expansion, not a failed search."""
    if deadline - time.monotonic() < EXPANSION_MIN_SECONDS:
        return [], {}, {"status": "skipped", "reason": "time budget"}
    ids = [p["id"] for p in pool]
    refs = await asyncio.to_thread(store.load_refs, ids)
    cached = len(refs)
    problem = None
    missing = [i for i in ids if i not in refs]
    if missing:
        try:
            fetched = await s2.references(client, missing, deadline=deadline - 4.0, api_key=s2_api_key)
        except s2.S2Error as exc:
            problem = str(exc)
        else:
            refs.update(fetched)
            await asyncio.to_thread(store.save_refs, fetched)
    if problem and not refs:
        return [], {}, {"status": "unavailable", "reason": problem}
    counts = cocitation_counts(pool, refs)
    wanted = refs_to_fetch(pool, counts, window)
    try:
        await asyncio.sleep(pause)
        found = await arxiv.fetch_ids(client, wanted, deadline=deadline)
    except arxiv.ArxivError as exc:
        return [], {}, {"status": "unavailable", "reason": str(exc)}
    pool_ids = set(ids)
    expanded = [p for p in found if p["id"] not in pool_ids and in_scope(p, category, include_cross_lists) and in_window(p, window)]
    info = {
        "status": "partial" if problem else "ok",
        "pool_papers_with_references": sum(refs.get(i) is not None for i in ids),
        "cached": cached,
        "references_checked": len(wanted),
        "added": len(expanded),
    }
    if problem:
        info["reason"] = problem
    return expanded, counts, info


def _candidates(record: dict, pool: list[dict], expanded: list[dict], counts: dict[str, int], expansion: dict) -> dict:
    """Rank the pool and its references and shortlist them; screening and selection come later."""
    ranked = rank_candidates(pool, expanded, counts)
    kept = {p["id"] for p in ranked}
    return {
        **record,
        "pool_ids": [p["id"] for p in pool],
        "expansion": expansion,
        "candidates": ranked,
        "cited_by": {pid: n for pid, n in counts.items() if pid in kept},
        "shortlist": [p["id"] for p in ranked[: shortlist_size(record["requested"])]],
    }


def build_tools(
    store: PaperStore,
    *,
    transport: httpx.AsyncBaseTransport | None = None,
    today: Any = date.today,
    pause: float = ARXIV_PAUSE_SECONDS,
    screener: Screener | None = None,
    s2_api_key: str | None = None,
    expand: bool = True,
) -> tuple[ModelTool, ModelTool, ModelTool]:
    """The three model tools; ``transport``, ``today``, ``pause`` and ``screener`` are injectable for offline tests."""
    screener = screener or Screener()

    async def search(payload: Mapping[str, Any], context: Any) -> PluginToolResult:
        if not context.thread_id:
            return _error("no conversation context")
        window = resolve_window(today(), payload.get("years"), payload.get("start_date"), payload.get("end_date"))
        category = normalise_category(payload.get("category"))  # the primary-category filter compares exactly, so "cs.cl" would keep nothing
        cross = payload.get("include_cross_lists", False)
        requested = payload["max_results"]
        deadline = time.monotonic() + SEARCH_BUDGET_SECONDS
        calls = 0
        async with httpx.AsyncClient(transport=transport, headers={"User-Agent": arxiv.USER_AGENT}, follow_redirects=True) as client:

            async def fetch(match: str, n: int) -> list[dict]:
                nonlocal calls
                if calls:
                    await asyncio.sleep(pause)
                calls += 1
                return await arxiv.fetch(client, query=payload["query"], max_results=n, category=category, start_date=window["start"], end_date=window["end"], match=match, deadline=deadline)

            try:
                pool, match = await select_papers(fetch, query=payload["query"], max_results=max(POOL_SIZE, requested), category=category, include_cross_lists=cross)
            except arxiv.ArxivError as exc:
                return _error(f"{exc}. Report this to the user; do not search arXiv by other means.")
            if expand and pool:
                expanded, counts, expansion = await _expand(client, store, pool, window, category, cross, deadline=deadline, pause=pause, s2_api_key=s2_api_key)
            else:
                expanded, counts, expansion = [], {}, {"status": "off" if not expand else "skipped", "reason": "disabled" if not expand else "empty pool"}

        retrieved_on = today().isoformat()
        record = {
            "search_id": uuid.uuid4().hex,
            "owner": context.principal.user_id,
            "query": payload["query"],
            "category": category,
            "include_cross_lists": cross,
            "window": window,
            "requested": requested,
            "match": match,
            "retrieved_on": retrieved_on,
            # The model's own sense of "today" was wrong in about half the reports; these come from code.
            "report_dates": {"today": retrieved_on, "retrieved_on": retrieved_on, "published_between": [window["start"] or "any", window["end"] or retrieved_on]},
            "searched_at": time.time(),  # the gate presents only reports saved after this
            # Filled by the screen tool; until then nothing can be fetched or cited.
            "papers": [],
            "batches": [],
            "screening": None,
        }
        record = _candidates(record, pool, expanded, counts, expansion)
        shortlist = record["shortlist"]
        await asyncio.to_thread(store.save_search, context.thread_id, record)
        summary = {
            "report_dates": record["report_dates"],
            "requested": requested,
            "window": window,
            "category": category,
            "match": match,
            "pool": len(pool),
            "citation_expansion": expansion,
            "shortlist": len(shortlist),
            "next": "Call the scholar screen tool with the user's topic to select the papers. There is no paper list yet: do not write about papers before screening.",
        }
        note = _shortfall_note(len(shortlist), requested)
        if note:
            summary["note"] = note
        return PluginToolResult(content=json.dumps(summary, ensure_ascii=False, separators=(",", ":")), artifact=None)

    async def screen(payload: Mapping[str, Any], context: Any) -> PluginToolResult:
        found, problem = await asyncio.to_thread(_owned_search, store, context)
        if problem:
            return _error(problem)
        if found.get("rejected"):
            return _error(f"the latest search was rejected: {found['rejected']}")
        if found.get("screening") is None:
            if expand and found["expansion"].get("status") in ("unavailable", "partial", "skipped") and found["pool_ids"]:
                found = await _retry_expansion(found)
            found = await _run_screening(found, payload)
            await asyncio.to_thread(store.save_search, context.thread_id, found)
        return PluginToolResult(content=json.dumps(_screen_result(found), ensure_ascii=False, separators=(",", ":")), artifact=None)

    async def _retry_expansion(found: dict) -> dict:
        """Semantic Scholar throttled during search (2 of 16 dev runs); try once more on screen's own time budget."""
        by_id = {p["id"]: p for p in found["candidates"]}
        pool = [by_id[pid] for pid in found["pool_ids"]]
        deadline = time.monotonic() + SCREEN_EXPANSION_SECONDS
        async with httpx.AsyncClient(transport=transport, headers={"User-Agent": arxiv.USER_AGENT}, follow_redirects=True) as client:
            expanded, counts, expansion = await _expand(client, store, pool, found["window"], found["category"], found["include_cross_lists"], deadline=deadline, pause=pause, s2_api_key=s2_api_key)
        if expansion["status"] not in ("ok", "partial"):
            return {**found, "expansion": {**found["expansion"], "retry": expansion}}
        return _candidates(found, pool, expanded, counts, {**expansion, "retried_in_screen": True})

    async def _run_screening(found: dict, payload: Mapping[str, Any]) -> dict:
        by_id = {p["id"]: p for p in found["candidates"]}
        shortlist = [by_id[pid] for pid in found["shortlist"]]
        scores, tokens, failed = {}, 0, 0
        status = "unavailable"
        if screener.available and shortlist:
            scores, tokens, failed = await screener.score(payload["topic"], found["category"], payload.get("criteria"), shortlist)
            status = "ok" if scores else "failed"
        if scores:
            selected = select_screened(shortlist, {pid: s["score"] for pid, s in scores.items()}, found["requested"])
        else:
            selected = shortlist[: found["requested"]]  # co-citation order, unscreened; the result says so
        pool_ids = set(found["pool_ids"])
        chosen = {p["id"] for p in selected}
        table = [{"id": p["id"], "source": "search" if p["id"] in pool_ids else "reference", "cited_by": found["cited_by"].get(p["id"], 0), **scores.get(p["id"], {}), "included": p["id"] in chosen} for p in shortlist]
        histogram = {str(k): sum(s["score"] == k for s in scores.values()) for k in range(4)}
        counts = {
            "identified_by_search": len(pool_ids),
            "added_from_references": len(found["candidates"]) - len(pool_ids),
            "shortlisted": len(shortlist),
            "screened": len(scores),
            "scores": histogram,
            "included": len(selected),
            "included_from_references": sum(p["id"] not in pool_ids for p in selected),
        }
        screening = {"status": status, "topic": payload["topic"], "criteria": payload.get("criteria"), "tokens": tokens, "failed_batches": failed, "counts": counts, "table": table}
        if status != "ok":
            screening["note"] = "Screening by model was unavailable; papers were selected by how often the candidate pool cites them. Say so in the methodology section."
        return {**found, "papers": selected, "batches": make_batches(selected), "screening": screening}

    def _screen_result(found: dict) -> dict:
        result = {
            "report_dates": found["report_dates"],
            "count": len(found["papers"]),
            "requested": found["requested"],
            "screening": found["screening"]["counts"],
            "batches": [{"batch": n, "ids": ids} for n, ids in enumerate(found["batches"], 1)],
            "index": [{**row, "cited_by": found["cited_by"].get(row["id"], 0)} for row in compact_index(found["papers"])],
        }
        notes = [n for n in (_shortfall_note(len(found["papers"]), found["requested"]), found["screening"].get("note")) if n]
        if notes:
            result["note"] = " ".join(notes)
        return result

    async def get_batch(payload: Mapping[str, Any], context: Any) -> PluginToolResult:
        found, problem = await asyncio.to_thread(_owned_search, store, context)
        if problem:
            return _error(problem)
        if found.get("rejected"):
            return _error(f"the latest search was rejected: {found['rejected']}")
        if found.get("screening") is None:
            return _error("the papers have not been selected yet; call the scholar screen tool first")
        batches = found["batches"]
        n = payload["batch"]
        if n > len(batches):
            return _error(f"batch {n} does not exist; this search has {len(batches)} batch(es)")
        by_id = {p["id"]: p for p in found["papers"]}
        papers = [batch_paper(by_id[pid]) for pid in batches[n - 1]]
        return PluginToolResult(content=json.dumps(papers, ensure_ascii=False), artifact=None)

    return (
        ModelTool("search", SEARCH_DESCRIPTION, SEARCH_SCHEMA, search, response_format="content_and_artifact"),
        ModelTool("screen", SCREEN_DESCRIPTION, SCREEN_SCHEMA, screen, response_format="content_and_artifact"),
        ModelTool("get_batch", BATCH_DESCRIPTION, BATCH_SCHEMA, get_batch, response_format="content_and_artifact"),
    )


class _GateContributor:
    def __init__(self, store: PaperStore, max_blocks: int) -> None:
        self._store = store
        self._max_blocks = max_blocks

    def contribute_middlewares(self, app_store: ExtensionData, ctx: AgentBuildContext) -> Sequence[MiddlewarePlacement]:
        # Only the lead agent presents files; subagents never see present_files.
        return (MiddlewarePlacement(CitationGateMiddleware(self._store, self._max_blocks), Placement.STANDARD, AgentScope.LEAD),)


@extension(api="0.2.8", name="scholar")
def install(registry: ExtensionRegistry, config: Mapping[str, Any]) -> None:
    enabled = config.get("enabled", False)
    if type(enabled) is not bool or not isinstance(config.get("storage_path"), str):
        raise ValueError("Configure boolean enabled and an absolute storage_path at deployment")
    max_blocks = config.get("max_blocks", 3)
    if type(max_blocks) is not int or not 1 <= max_blocks <= 10:
        raise ValueError("max_blocks must be an integer between 1 and 10")
    expand = config.get("citation_expansion", True)
    s2_api_key = config.get("s2_api_key")
    if type(expand) is not bool or not (s2_api_key is None or (isinstance(s2_api_key, str) and s2_api_key)):
        raise ValueError("citation_expansion must be boolean and s2_api_key a non-empty string when set")
    if not enabled:
        return
    store = PaperStore(config["storage_path"])
    # Screening needs the operator's model grant (host_access.model_invocation); without it the service gets no
    # invoker and papers are selected by co-citation alone, which the screen result tells the model.
    screener = Screener()
    contribution = PluginContribution(
        namespace=NAMESPACE,
        title="学术检索与引用核查 / Scholar search and citation gate",
        description="arXiv 检索 + 沿引用扩展 + 模型筛选(代码过滤日期与类别)、分批交给子 Agent,交付前由代码核对引用。 / arXiv search with citation expansion and model screening, code-side filtering, batch hand-off to subagents, and a citation gate on delivery.",
        enabled=True,
        tools=build_tools(store, screener=screener, s2_api_key=s2_api_key, expand=expand),
    )
    if registry.plugin(contribution) is not True:
        raise RuntimeError("The scholar plugin requires the full-stack plugin host contract")
    registry.service(screener)
    registry.middlewares(_GateContributor(store, max_blocks))


__all__ = ["CitationGateMiddleware", "PaperStore", "Screener", "build_tools", "install"]
