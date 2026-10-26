"""Plugin-owned per-thread storage. No imports from DeerFlow host internals.

One directory per thread under a deployment-owned root:
``search.json`` (the latest search: owner, constraints, papers, batches) and
``gate.jsonl`` (one line per citation-gate decision, read by the eval).
Shared across threads: ``refs/<arXiv id>.json``, a paper's arXiv references
from Semantic Scholar. A paper's reference list does not depend on who asked,
and caching it keeps citation expansion working when Semantic Scholar throttles.
"""

from __future__ import annotations

import json
import os
import re
import tempfile
from pathlib import Path

_THREAD_ID = re.compile(r"^[A-Za-z0-9_-]{1,128}$")
_ARXIV_ID = re.compile(r"^\d{4}\.\d{4,5}$")


class PaperStore:
    def __init__(self, root: str):
        self.root = Path(root)
        if not self.root.is_absolute():
            raise ValueError("storage_path must be an absolute deployment-owned path")
        self.root.mkdir(parents=True, exist_ok=True)

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
