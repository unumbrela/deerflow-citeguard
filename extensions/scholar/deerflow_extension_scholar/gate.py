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
"""

from __future__ import annotations

import asyncio
import hashlib
import time
from collections.abc import Mapping
from pathlib import Path, PurePosixPath
from typing import Any

from langchain.agents.middleware import AgentMiddleware
from langchain_core.messages import AIMessage, ToolMessage

from .core import verify_report
from .store import PaperStore

MARKER = "[citation-gate]"
OUTPUTS_PREFIX = "/mnt/user-data/outputs/"
PRESENT_TOOL = "present_files"
MAX_WARNINGS_SHOWN = 8


def _thread_id(runtime: Any) -> str | None:
    context = getattr(runtime, "context", None)
    value = context.get("thread_id") if isinstance(context, Mapping) else getattr(context, "thread_id", None)
    return value if isinstance(value, str) else None


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


def _rejection(path: str, result: dict, attempt: int, max_blocks: int, unchanged: bool) -> str:
    lines = [
        f"{MARKER} CITATION CHECK FAILED: {path} is visible to the user but NOT verified (rejection {attempt} of {max_blocks}).",
        f"These arXiv ids are not in this thread's search results, so they may be invented: {', '.join(result['unknown_ids'])}.",
    ]
    if unchanged:
        lines.append("The file is unchanged since the previous rejection: presenting it again without editing will fail again.")
    lines += [
        "Remove those papers (or replace them with papers from the search index that you have not cited yet), fix every sentence and reference that mentions them, save the file, then call present_files again.",
        "Never add a paper, id, title or author from memory. If the user explicitly asked for one of these references and you keep it, tell the user plainly that it is not from the search and could not be verified.",
    ]
    if result["warnings"]:
        lines.append("Also fix: " + "; ".join(result["warnings"][:MAX_WARNINGS_SHOWN]))
    return "\n".join(lines)


def _released(path: str, result: dict, max_blocks: int) -> str:
    return (
        f"{MARKER} CITATION CHECK FAILED again after {max_blocks} rejections; {path} is presented as-is. "
        f"You MUST tell the user plainly that these arXiv ids could not be traced to the search and may be invented: {', '.join(result['unknown_ids'])}."
    )


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

    def _check(self, state: Any, runtime: Any) -> dict | None:
        thread_id = _thread_id(runtime)
        if not thread_id or not isinstance(state, Mapping):
            return None
        turn, results = _latest_step(list(state.get("messages") or []))
        presented = [m for m in results if m.name == PRESENT_TOOL and MARKER not in _text(m.content)]
        if turn is None or not presented:
            return None
        search = self.store.load_search(thread_id)
        if search is None:
            return None  # not a literature-review thread
        outputs_path = (state.get("thread_data") or {}).get("outputs_path")
        if not outputs_path:
            self.store.log(thread_id, {"event": "skipped", "reason": "no outputs_path", "search_id": search["search_id"], "at": time.time()})
            return None
        args_by_call = {c.get("id"): c.get("args") or {} for c in turn.tool_calls}
        updates = []
        for message in presented:
            paths = [p for p in args_by_call.get(message.tool_call_id, {}).get("filepaths", []) if isinstance(p, str) and p.endswith(".md")]
            checks = [c for c in (self._verify_one(thread_id, search, v, outputs_path) for v in paths) if c]
            if not checks:
                continue
            notes = "\n\n".join(note for _, note in checks)
            # A rejection replaces the success text, so the model cannot read the delivery as done.
            content = notes if any(rejected for rejected, _ in checks) else f"{_text(message.content)}\n\n{notes}"
            updates.append(message.model_copy(update={"content": content}))
        return {"messages": updates} if updates else None

    def _verify_one(self, thread_id: str, search: dict, virtual: str, outputs_path: str) -> tuple[bool, str] | None:
        """Return ``(rejected, note)`` for one presented report, or None when it is not a readable output file."""
        host = _host_path(virtual, outputs_path)
        if host is None or not host.is_file():
            return None
        text = host.read_text(encoding="utf-8", errors="replace")
        result = verify_report(text, search["papers"])
        prior = [r for r in self.store.read_log(thread_id) if r.get("search_id") == search["search_id"] and r.get("event") == "rejected"]
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        record = {"search_id": search["search_id"], "path": virtual, "sha256": digest, "at": time.time(), **{k: result[k] for k in ("cited", "retrieved", "unknown_ids", "warnings")}}
        if result["ok"]:
            self.store.log(thread_id, {"event": "accepted", **record})
            return False, _accepted(result)
        if len(prior) < self.max_blocks:
            self.store.log(thread_id, {"event": "rejected", "attempt": len(prior) + 1, **record})
            unchanged = any(r.get("path") == virtual and r.get("sha256") == digest for r in prior)
            return True, _rejection(virtual, result, len(prior) + 1, self.max_blocks, unchanged)
        self.store.log(thread_id, {"event": "released_unverified", **record})
        return False, _released(virtual, result, self.max_blocks)
