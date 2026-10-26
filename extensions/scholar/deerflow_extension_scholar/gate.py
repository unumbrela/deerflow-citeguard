"""Citation gate: a report is not accepted until code has checked its arXiv ids.

The SKILL.md used to ask the model to run ``verify`` before presenting; in a
smoke run it skipped that and wrote its own check. A request the model can
ignore is not a gate, so this middleware enforces it.

Extension tool-call wrappers are observational (the host returns the
downstream result whatever the wrapper returns), so the gate cannot veto
``present_files`` itself. It uses ``before_model`` instead: after a step that
presented a markdown report, and before the model sees the result, the report
is verified against this thread's search and the ``present_files`` result is
replaced by ID. On failure the model is told the report is unverified and why;
after ``max_blocks`` rejections it must tell the user which ids are unverified.

Limit: the host's ``artifacts`` reducer only appends, so the file stays visible
to the user even when rejected. The gate can withhold the "delivered" signal
from the model, not withdraw the file; the messages say so instead of
pretending otherwise.

Two more checks close ways around the gate:
- A report saved but never presented was never checked (2 of 16 flash runs).
  ``after_model`` sees the model about to finish and adds the ``present_files``
  call itself, so the check above runs. Extension hooks cannot ``jump_to``
  (the host's wrapper does not carry the declaration), but the agent loop
  routes on the last message's tool calls, so adding one is enough.
- A search without the category the user named searched the wrong field (9 of
  16 flash runs). The search result is replaced by an error and the stored
  search is marked rejected, so ``get_batch`` refuses it and a report built on
  it fails the check.
"""

from __future__ import annotations

import asyncio
import hashlib
import time
import uuid
from collections.abc import Mapping
from pathlib import Path, PurePosixPath
from typing import Any

from langchain.agents.middleware import AgentMiddleware
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

from .core import ID_RE, normalise_category, user_categories, verify_report, wrong_year_dates
from .store import PaperStore

MARKER = "[citation-gate]"
OUTPUTS_PREFIX = "/mnt/user-data/outputs/"
PRESENT_TOOL = "present_files"
AUTO_PRESENT_ID = "citation-gate-present-"
DECISIONS = {"accepted", "rejected", "released_unverified"}
MAX_WARNINGS_SHOWN = 8


def _thread_id(runtime: Any) -> str | None:
    context = getattr(runtime, "context", None)
    value = context.get("thread_id") if isinstance(context, Mapping) else getattr(context, "thread_id", None)
    return value if isinstance(value, str) else None


def _is_search(name: str | None) -> bool:
    # The host exposes plugin tools as ext_<namespace>_<tool>_<hash>, e.g. ext_community_scholar_search_1607103162c3.
    return name == "search" or bool(name and name.startswith("ext_") and "_scholar_search" in name)


def _user_request(messages: list[Any]) -> str:
    """The latest message the user typed; host reminders are hidden from the UI and skipped."""
    for message in reversed(messages):
        if isinstance(message, HumanMessage) and not (message.additional_kwargs or {}).get("hide_from_ui"):
            return _text(message.content)
    return ""


def _latest_step(messages: list[Any]) -> tuple[AIMessage | None, list[ToolMessage]]:
    """Tool results after the most recent model turn, plus that turn."""
    results: list[ToolMessage] = []
    for message in reversed(messages):
        if isinstance(message, AIMessage):
            return message, results
        if isinstance(message, ToolMessage):
            results.append(message)
    return None, results


def _host_path(virtual: str, outputs_path: str) -> Path | None:
    """Map a presented path to the thread's real outputs directory, refusing escapes."""
    if virtual.startswith(OUTPUTS_PREFIX):
        rel = virtual[len(OUTPUTS_PREFIX) :]
    elif virtual.startswith("outputs/"):
        rel = virtual[len("outputs/") :]
    else:
        return None
    root = Path(outputs_path).resolve()
    candidate = (root / PurePosixPath(rel)).resolve()
    return candidate if candidate.is_relative_to(root) else None


def _text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(b.get("text", "") if isinstance(b, dict) else str(b) for b in content)
    return str(content)


def _search_rejection(wanted: set[str], got: str | None, attempt: int, max_blocks: int) -> str:
    asked = " or ".join(sorted(wanted))
    return (
        f"{MARKER} SEARCH REJECTED (rejection {attempt} of {max_blocks}): the user asked for category {asked}, "
        f"but this search used {f'category {got}' if got else 'no category'}. Its results are discarded and get_batch will refuse them. "
        f"Call the search tool again with `category` set to {asked}."
    )


def _search_released(wanted: set[str], got: str | None, max_blocks: int) -> str:
    return f"{MARKER} The search still does not use category {' or '.join(sorted(wanted))} after {max_blocks} rejections. You MUST tell the user that their category was not applied ({f'used {got}' if got else 'no category'})."


def _rejection(path: str, result: dict, attempt: int, max_blocks: int, unchanged: bool) -> str:
    lines = [f"{MARKER} CITATION CHECK FAILED: {path} is visible to the user but NOT verified (rejection {attempt} of {max_blocks})."]
    if result.get("search_rejected"):
        lines.append("This thread's latest search was rejected for using the wrong category, so no paper in the report can be verified. Search again with the user's category and rebuild the report from that search.")
    if unchanged:
        lines.append("The file is unchanged since the previous rejection: presenting it again without editing will fail again.")
    if result["unknown_ids"]:
        lines += [
            f"These arXiv ids are not among the papers selected for this review (screen tool index), so they may be invented: {', '.join(result['unknown_ids'])}.",
            "Remove those papers (or replace them with papers from the search index that you have not cited yet) and fix every sentence and reference that mentions them.",
            "Never add a paper, id, title or author from memory. If the user explicitly asked for one of these references and you keep it, tell the user plainly that it is not from the search and could not be verified.",
        ]
    if result["date_errors"]:
        lines.append(f"These dates contradict the search (wrong year): {', '.join(result['date_errors'])}. Use the dates in `report_dates` from the search result.")
    if result["missing"]:
        lines.append(
            f"The user asked for {result['expected']} papers and the search found them, but the report cites only {result['cited']}. Add these retrieved papers (their data is in the subagent results): {', '.join(result['missing'])}."
        )
    if result["warnings"]:
        lines.append("Also fix: " + "; ".join(result["warnings"][:MAX_WARNINGS_SHOWN]))
    lines.append("Save the file, then call present_files again.")
    return "\n".join(lines)


def _released(path: str, result: dict, max_blocks: int) -> str:
    problems = ["the search did not use the category they asked for"] if result.get("search_rejected") else []
    if result["unknown_ids"]:
        problems.append(f"these arXiv ids could not be traced to the search and may be invented: {', '.join(result['unknown_ids'])}")
    if result["date_errors"]:
        problems.append(f"these dates are wrong: {', '.join(result['date_errors'])}")
    if result["missing"]:
        problems.append(f"the report covers {result['cited']} of the {result['expected']} papers requested")
    return f"{MARKER} CITATION CHECK FAILED again after {max_blocks} rejections; {path} is presented as-is. You MUST tell the user plainly that {'; and '.join(problems)}."


def _accepted(result: dict) -> str:
    note = f"{MARKER} Citation check passed: {result['cited']} arXiv ids cited, all from this thread's search ({result['retrieved']} retrieved)."
    if result["warnings"]:
        note += " Fix these entries to match the search data exactly: " + "; ".join(result["warnings"][:MAX_WARNINGS_SHOWN])
    return note


class CitationGateMiddleware(AgentMiddleware):
    def __init__(self, store: PaperStore, max_blocks: int = 3) -> None:
        super().__init__()
        self.store = store
        self.max_blocks = max_blocks

    def before_model(self, state: Any, runtime: Any) -> dict | None:
        return self._check(state, runtime)

    async def abefore_model(self, state: Any, runtime: Any) -> dict | None:
        return await asyncio.to_thread(self._check, state, runtime)

    def after_model(self, state: Any, runtime: Any) -> dict | None:
        return self._deliver_saved_report(state, runtime)

    async def aafter_model(self, state: Any, runtime: Any) -> dict | None:
        return await asyncio.to_thread(self._deliver_saved_report, state, runtime)

    def _check(self, state: Any, runtime: Any) -> dict | None:
        thread_id = _thread_id(runtime)
        if not thread_id or not isinstance(state, Mapping):
            return None
        messages = list(state.get("messages") or [])
        turn, results = _latest_step(messages)
        fresh = [m for m in results if MARKER not in _text(m.content)]
        searched = [m for m in fresh if _is_search(m.name)]
        presented = [m for m in fresh if m.name == PRESENT_TOOL]
        if turn is None or not (searched or presented):
            return None
        search = self.store.load_search(thread_id)
        if search is None:
            return None  # not a literature-review thread
        updates = self._check_category(thread_id, search, searched, _user_request(messages)) if searched else []
        outputs_path = (state.get("thread_data") or {}).get("outputs_path")
        if presented and not outputs_path:
            self.store.log(thread_id, {"event": "skipped", "reason": "no outputs_path", "search_id": search["search_id"], "at": time.time()})
            presented = []
        args_by_call = {c.get("id"): c.get("args") or {} for c in turn.tool_calls}
        for message in presented:
            paths = [p for p in args_by_call.get(message.tool_call_id, {}).get("filepaths", []) if isinstance(p, str) and p.endswith(".md")]
            checks = [c for c in (self._verify_one(thread_id, search, v, outputs_path) for v in paths) if c]
            if not checks:
                continue
            notes = "\n\n".join(note for _, note in checks)
            if message.tool_call_id.startswith(AUTO_PRESENT_ID):
                notes = f"{MARKER} You saved this report but did not call present_files, so the gate presented it to check it.\n\n{notes}"
            # A rejection replaces the success text, so the model cannot read the delivery as done.
            content = notes if any(rejected for rejected, _ in checks) else f"{_text(message.content)}\n\n{notes}"
            updates.append(message.model_copy(update={"content": content}))
        return {"messages": updates} if updates else None

    def _check_category(self, thread_id: str, search: dict, searched: list[ToolMessage], request: str) -> list[ToolMessage]:
        """Reject a search that dropped or changed the category the user named."""
        wanted = user_categories(request)
        got = normalise_category(search.get("category"))
        if not wanted or got in wanted or search.get("rejected"):
            return []
        prior = sum(r.get("event") == "search_rejected" for r in self.store.read_log(thread_id))
        record = {"search_id": search["search_id"], "wanted": sorted(wanted), "got": got, "at": time.time()}
        if prior >= self.max_blocks:
            self.store.log(thread_id, {"event": "search_released", **record})
            return [m.model_copy(update={"content": f"{_text(m.content)}\n\n{_search_released(wanted, got, self.max_blocks)}"}) for m in searched]
        self.store.save_search(thread_id, {**search, "rejected": f"the user asked for category {' or '.join(sorted(wanted))}; search again with it"})
        self.store.log(thread_id, {"event": "search_rejected", "attempt": prior + 1, **record})
        note = _search_rejection(wanted, got, prior + 1, self.max_blocks)
        return [m.model_copy(update={"content": note}) for m in searched]

    def _deliver_saved_report(self, state: Any, runtime: Any) -> dict | None:
        """Present a report the model saved but is about to finish without presenting."""
        thread_id = _thread_id(runtime)
        if not thread_id or not isinstance(state, Mapping):
            return None
        messages = list(state.get("messages") or [])
        last = messages[-1] if messages else None
        if not isinstance(last, AIMessage) or last.tool_calls or last.invalid_tool_calls:
            return None
        if {"deerflow_error_fallback", "model_length_termination"} & set(last.additional_kwargs or {}):
            return None  # the host already ended this turn on an error; do not re-engage
        search = self.store.load_search(thread_id)
        outputs_path = (state.get("thread_data") or {}).get("outputs_path")
        if search is None or not outputs_path:
            return None
        handled = DECISIONS | {"auto_presented"}
        if any(r.get("search_id") == search["search_id"] and r.get("event") in handled for r in self.store.read_log(thread_id)):
            return None  # a report for this search was already checked, or already presented by the gate once
        root = Path(outputs_path)
        since = search.get("searched_at", 0) - 5  # small slack for file-system clock granularity
        reports = sorted(p for p in root.glob("**/*.md") if p.is_file() and p.stat().st_mtime >= since and ID_RE.search(p.read_text(encoding="utf-8", errors="replace")))
        if not reports:
            return None
        paths = [OUTPUTS_PREFIX + p.relative_to(root).as_posix() for p in reports]
        self.store.log(thread_id, {"event": "auto_presented", "search_id": search["search_id"], "paths": paths, "at": time.time()})
        call = {"id": f"{AUTO_PRESENT_ID}{uuid.uuid4().hex[:12]}", "name": PRESENT_TOOL, "args": {"filepaths": paths}, "type": "tool_call"}
        # Same message id, so the reducer replaces the final answer with one that also calls present_files.
        return {"messages": [last.model_copy(update={"tool_calls": [call]})]}

    def _verify_one(self, thread_id: str, search: dict, virtual: str, outputs_path: str) -> tuple[bool, str] | None:
        """Return ``(rejected, note)`` for one presented report, or None when it is not a readable output file."""
        host = _host_path(virtual, outputs_path)
        if host is None or not host.is_file():
            return None
        text = host.read_text(encoding="utf-8", errors="replace")
        # A rejected search's papers never reached the model, so nothing can be traced to it.
        result = verify_report(text, [] if search.get("rejected") else search["papers"])
        result["search_rejected"] = bool(search.get("rejected"))
        known = {p.get(k, "") for p in search["papers"] for k in ("published", "updated")}
        window = search.get("window") or {}
        # The window end is an anchor too: a coverage task ended its window on 2025-10-26 while searching on 2026-10-26.
        anchors = [search.get("retrieved_on", ""), window.get("start") or "", window.get("end") or ""]
        result["date_errors"] = wrong_year_dates(text, anchors, known)
        # h02-r2 in round two cited 9 of 10 retrieved papers; the user asked for 10, so that is a shortfall the code can see.
        result["expected"] = min(search.get("requested") or 0, len(search["papers"]))
        result["missing"] = result["not_cited"][: max(0, result["expected"] - (result["cited"] - len(result["unknown_ids"])))]
        result["ok"] = result["ok"] and not result["date_errors"] and not result["missing"] and not result["search_rejected"]
        prior = [r for r in self.store.read_log(thread_id) if r.get("search_id") == search["search_id"] and r.get("event") == "rejected"]
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        record = {"search_id": search["search_id"], "path": virtual, "sha256": digest, "at": time.time(), **{k: result[k] for k in ("cited", "retrieved", "unknown_ids", "date_errors", "missing", "warnings", "search_rejected")}}
        if result["ok"]:
            self.store.log(thread_id, {"event": "accepted", **record})
            return False, _accepted(result)
        if len(prior) < self.max_blocks:
            self.store.log(thread_id, {"event": "rejected", "attempt": len(prior) + 1, **record})
            unchanged = any(r.get("path") == virtual and r.get("sha256") == digest for r in prior)
            return True, _rejection(virtual, result, len(prior) + 1, self.max_blocks, unchanged)
        self.store.log(thread_id, {"event": "released_unverified", **record})
        return False, _released(virtual, result, self.max_blocks)
