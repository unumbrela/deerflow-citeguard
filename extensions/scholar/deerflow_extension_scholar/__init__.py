"""Scholar plugin: arXiv search and batch tools plus a citation gate. No imports from DeerFlow host internals.

- ``search``: query arXiv inside the Gateway (no ``allow_host_bash``), filter by
  date window and primary category in code, store the result per thread, and
  return a compact index.
- ``get_batch``: hand one batch of stored papers to a subagent, so paper data
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

from . import arxiv
from .core import batch_paper, compact_index, make_batches, resolve_window, select_papers
from .gate import CitationGateMiddleware
from .store import PaperStore

NAMESPACE = "community.scholar"
SEARCH_BUDGET_SECONDS = 25.0  # the host cancels a plugin tool call at 30 s
ARXIV_PAUSE_SECONDS = 3.0  # arXiv asks for at least 3 s between calls

SEARCH_DESCRIPTION = (
    "Search arXiv for a literature review. Filters by submission date window and PRIMARY arXiv category in code, "
    "stores the full results for this conversation, and returns a compact index (id, short title, first author, date, category) "
    "plus the batch numbers to hand to subagents. The index is the only list of papers that exists: never cite a paper that is not in it. "
    "Keep `query` to 2-3 core keywords; put the field in `category` and time in `years`. "
    "Never drop or change `category` or `years` to get more papers; if fewer papers come back, that is the real result size."
)
SEARCH_SCHEMA = {
    "type": "object",
    "properties": {
        "query": {"type": "string", "minLength": 2, "maxLength": 200, "description": "2-3 core keywords, e.g. 'agent evaluation'."},
        "max_results": {"type": "integer", "minimum": 1, "maximum": 50, "description": "Number of papers requested by the user."},
        "category": {"type": "string", "pattern": "^[a-z-]+(\\.[A-Za-z-]+)?$", "description": "arXiv category such as cs.CL; matched against the primary category."},
        "include_cross_lists": {"type": "boolean", "description": "Also accept papers only cross-listed in `category`. Only if the user explicitly accepts that."},
        "years": {"type": "integer", "minimum": 1, "maximum": 40, "description": "Only papers submitted in the last N years (computed from today in code)."},
        "start_date": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$", "description": "YYYY-MM-DD; overrides `years`."},
        "end_date": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$", "description": "YYYY-MM-DD."},
    },
    "required": ["query", "max_results"],
    "additionalProperties": False,
}

BATCH_DESCRIPTION = (
    "Return one batch of the papers stored by the scholar search tool in this conversation, as a JSON array "
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


def build_tools(store: PaperStore, *, transport: httpx.AsyncBaseTransport | None = None, today: Any = date.today, pause: float = ARXIV_PAUSE_SECONDS) -> tuple[ModelTool, ModelTool]:
    """The two model tools; ``transport``, ``today`` and ``pause`` are injectable for offline tests."""

    async def search(payload: Mapping[str, Any], context: Any) -> PluginToolResult:
        if not context.thread_id:
            return _error("no conversation context")
        window = resolve_window(today(), payload.get("years"), payload.get("start_date"), payload.get("end_date"))
        deadline = time.monotonic() + SEARCH_BUDGET_SECONDS
        calls = 0
        async with httpx.AsyncClient(transport=transport, headers={"User-Agent": arxiv.USER_AGENT}, follow_redirects=True) as client:

            async def fetch(match: str, n: int) -> list[dict]:
                nonlocal calls
                if calls:
                    await asyncio.sleep(pause)
                calls += 1
                return await arxiv.fetch(client, query=payload["query"], max_results=n, category=payload.get("category"), start_date=window["start"], end_date=window["end"], match=match, deadline=deadline)

            try:
                papers, match = await select_papers(fetch, query=payload["query"], max_results=payload["max_results"], category=payload.get("category"), include_cross_lists=payload.get("include_cross_lists", False))
            except arxiv.ArxivError as exc:
                return _error(f"{exc}. Report this to the user; do not search arXiv by other means.")

        batches = make_batches(papers)
        record = {
            "search_id": uuid.uuid4().hex,
            "owner": context.principal.user_id,
            "query": payload["query"],
            "category": payload.get("category"),
            "include_cross_lists": payload.get("include_cross_lists", False),
            "window": window,
            "requested": payload["max_results"],
            "match": match,
            "retrieved_on": today().isoformat(),
            "papers": papers,
            "batches": batches,
        }
        await asyncio.to_thread(store.save_search, context.thread_id, record)
        summary = {
            "count": len(papers),
            "requested": payload["max_results"],
            "window": window,
            "category": payload.get("category"),
            "match": match,
            "batches": [{"batch": n, "ids": ids} for n, ids in enumerate(batches, 1)],
            "index": compact_index(papers),
        }
        if not papers:
            summary["note"] = "0 papers matched. Tell the user and suggest broadening the topic or removing the category; do not relax the filters yourself."
        elif len(papers) < payload["max_results"]:
            summary["note"] = "Fewer papers than requested under the user's constraints. Do not pad; state the shortfall in the report."
        return PluginToolResult(content=json.dumps(summary, ensure_ascii=False, separators=(",", ":")), artifact=None)

    async def get_batch(payload: Mapping[str, Any], context: Any) -> PluginToolResult:
        search, problem = await asyncio.to_thread(_owned_search, store, context)
        if problem:
            return _error(problem)
        batches = search["batches"]
        n = payload["batch"]
        if n > len(batches):
            return _error(f"batch {n} does not exist; this search has {len(batches)} batch(es)")
        by_id = {p["id"]: p for p in search["papers"]}
        papers = [batch_paper(by_id[pid]) for pid in batches[n - 1]]
        return PluginToolResult(content=json.dumps(papers, ensure_ascii=False), artifact=None)

    return (
        ModelTool("search", SEARCH_DESCRIPTION, SEARCH_SCHEMA, search, response_format="content_and_artifact"),
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
    if not enabled:
        return
    store = PaperStore(config["storage_path"])
    contribution = PluginContribution(
        namespace=NAMESPACE,
        title="学术检索与引用核查 / Scholar search and citation gate",
        description="arXiv 检索(代码过滤日期与类别)、分批交给子 Agent,交付前由代码核对引用。 / arXiv search with code-side filtering, batch hand-off to subagents, and a citation gate on delivery.",
        enabled=True,
        tools=build_tools(store),
    )
    if registry.plugin(contribution) is not True:
        raise RuntimeError("The scholar plugin requires the full-stack plugin host contract")
    registry.middlewares(_GateContributor(store, max_blocks))


__all__ = ["CitationGateMiddleware", "PaperStore", "build_tools", "install"]
