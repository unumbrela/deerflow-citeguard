"""Plugin-owned per-thread storage. No imports from DeerFlow host internals.

One directory per thread under a deployment-owned root:
``search.json`` (the latest search: owner, constraints, papers, batches) and
``gate.jsonl`` (one line per citation-gate decision, read by the eval) and
``evidence.jsonl`` (quotes checked against a paper's text, one per evidence id).
Shared across threads: ``refs/<arXiv id>.json``, a paper's arXiv references
from Semantic Scholar, and ``fulltext/<arXiv id>.json``, a paper's parsed
HTML. Neither depends on who asked; caching them keeps the tools inside their
time budget and working when an upstream service throttles.
"""

from __future__ import annotations

import json
import os
import re
import tempfile
import threading
import time
from pathlib import Path

_THREAD_ID = re.compile(r"^[A-Za-z0-9_-]{1,128}$")
_ARXIV_ID = re.compile(r"^\d{4}\.\d{4,5}$")
FALLBACK_RETRY_SECONDS = 6 * 3600  # a paper without HTML is looked up again later, not on every read


class PaperStore:
    def __init__(self, root: str):
        self.root = Path(root)
        if not self.root.is_absolute():
            raise ValueError("storage_path must be an absolute deployment-owned path")
        self.root.mkdir(parents=True, exist_ok=True)
        self._evidence_lock = threading.Lock()  # three subagents record evidence at once

    def _dir(self, thread_id: str) -> Path:
        if not isinstance(thread_id, str) or not _THREAD_ID.match(thread_id):
            raise ValueError("invalid thread id")
        return self.root / "threads" / thread_id

    @staticmethod
    def _write(directory: Path, name: str, data: object) -> None:
        directory.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=directory, prefix=f".{name}-", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump(data, fh, ensure_ascii=False)
            os.replace(tmp, directory / name)
        except BaseException:
            Path(tmp).unlink(missing_ok=True)
            raise

    def save_search(self, thread_id: str, record: dict) -> None:
        self._write(self._dir(thread_id), "search.json", record)

    def load_refs(self, ids: list[str]) -> dict[str, list[str] | None]:
        """Cached references; papers never looked up are absent, papers Semantic Scholar does not know map to None."""
        out: dict[str, list[str] | None] = {}
        for pid in ids:
            path = self.root / "refs" / f"{pid}.json"
            if _ARXIV_ID.match(pid) and path.is_file():
                out[pid] = json.loads(path.read_text(encoding="utf-8"))
        return out

    def save_refs(self, refs: dict[str, list[str] | None]) -> None:
        for pid, found in refs.items():
            # Unknown papers are not cached: Semantic Scholar may index a new preprint later.
            if _ARXIV_ID.match(pid) and found is not None:
                self._write(self.root / "refs", f"{pid}.json", found)

    def load_fulltext(self, pid: str) -> dict | None:
        path = self.root / "fulltext" / f"{pid}.json"
        if not _ARXIV_ID.match(pid) or not path.is_file():
            return None
        doc = json.loads(path.read_text(encoding="utf-8"))
        if doc.get("status") != "html" and time.time() - path.stat().st_mtime > FALLBACK_RETRY_SECONDS:
            return None
        return doc

    def save_fulltext(self, doc: dict) -> None:
        if _ARXIV_ID.match(doc.get("id", "")):
            self._write(self.root / "fulltext", f"{doc['id']}.json", doc)

    def add_evidence(self, thread_id: str, search_id: str, items: list[dict]) -> list[dict]:
        """Number new evidence ``E1, E2, ...`` per thread; the same quote from the same paper keeps its number."""
        directory = self._dir(thread_id)
        with self._evidence_lock:
            existing = self.read_evidence(thread_id)
            known = {(e["search_id"], e["paper"], e["quote"]): e for e in existing}
            out, new = [], []
            for item in items:
                key = (search_id, item["paper"], item["quote"])
                if key not in known:
                    known[key] = {"e": f"E{len(existing) + len(new) + 1}", "search_id": search_id, **item, "at": time.time()}
                    new.append(known[key])
                out.append(known[key])
            if new:
                directory.mkdir(parents=True, exist_ok=True)
                with (directory / "evidence.jsonl").open("a", encoding="utf-8") as fh:
                    fh.writelines(json.dumps(e, ensure_ascii=False) + "\n" for e in new)
        return out

    def read_evidence(self, thread_id: str) -> list[dict]:
        try:
            path = self._dir(thread_id) / "evidence.jsonl"
        except ValueError:
            return []
        if not path.is_file():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

    def load_search(self, thread_id: str) -> dict | None:
        try:
            path = self._dir(thread_id) / "search.json"
        except ValueError:
            return None
        if not path.is_file():
            return None
        return json.loads(path.read_text(encoding="utf-8"))

    def log(self, thread_id: str, record: dict) -> None:
        directory = self._dir(thread_id)
        directory.mkdir(parents=True, exist_ok=True)
        with (directory / "gate.jsonl").open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    def read_log(self, thread_id: str) -> list[dict]:
        try:
            path = self._dir(thread_id) / "gate.jsonl"
        except ValueError:
            return []
        if not path.is_file():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
