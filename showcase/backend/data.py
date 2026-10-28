"""Read-only access to the eval artifacts tracked under runs/.

Only small tracked files are read (meta, citations, gate, claims, evidence, summaries);
raw traces (events.jsonl, final.json) are never touched. Suite and run names are only
accepted when they match an existing directory, so a request cannot leave runs/.
"""

from __future__ import annotations

import csv
import io
import json
import re
import statistics
import sys
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNS = ROOT / "runs"

sys.path.insert(0, str(ROOT / "eval"))
import claims as claim_eval
from holdout_report import clean, wilson  # same run-level metric as README

# Short labels for the suites the README and BASELINE talk about; the rest show their directory name.
LABELS = {
    "live": "在线任务",
    "holdout3-v3": "第二轮留出 · v3",
    "holdout3-base": "第二轮留出 · 上游 skill",
    "holdout-base": "第一轮留出 · 上游 skill",
    "holdout-v21": "第一轮留出 · v2.1",
    "coverage-holdout-v32": "覆盖率留出 · v3.2",
    "coverage-holdout-v4": "覆盖率留出 · v4",
    "coverage-dev-v31-plus": "覆盖率开发集 · v3.1",
    "coverage-dev-v4-plus": "覆盖率开发集 · v4",
    "pre-01": "开发集 30 主题 · 上游 skill",
    "pre-02": "开发集 30 主题 · 上游 skill（重跑）",
    "v2-01": "开发集 30 主题 · v2",
    "v2-02": "开发集 30 主题 · v2（重跑）",
    **{f"smoke-v5-plus-0{i}": f"v5 全文证据冒烟 0{i}" for i in range(2, 7)},
}

# Same decision events as eval/aggregate.py; other gate events are bookkeeping.
DECISIONS = ("accepted", "rejected", "released_unverified")


class NotFound(Exception):
    pass


def _json(path: Path, default=None):
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def _jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text().splitlines():
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def _kind(name: str) -> str:
    if name == "live":
        return "live"
    if "infra-failed" in name:
        return "archive"
    if "holdout" in name:
        return "holdout"
    if "smoke" in name:
        return "smoke"
    return "dev"


def _suite_dir(name: str) -> Path:
    if name not in _suite_names():
        raise NotFound(name)
    return RUNS / f"suite-{name}"


def _suite_names() -> list[str]:
    """Labelled suites first, in LABELS order, then the rest by name."""
    names = sorted(p.name[len("suite-") :] for p in RUNS.glob("suite-*") if p.is_dir())
    order = {n: i for i, n in enumerate(LABELS)}
    return sorted(names, key=lambda n: (order.get(n, len(order)), n))


def _run_ids(suite_dir: Path) -> list[str]:
    return sorted(p.parent.name for p in suite_dir.glob("*/meta.json"))


@lru_cache(maxsize=1)
def _run_records() -> dict:
    data = _json(RUNS / "token-run-record-20261027.json", {})
    return {
        (g, r["run"]): r.get("run_record")
        for g, rows in data.get("groups", {}).items()
        for r in rows
    }


def _tokens(suite: str, run: str, meta: dict) -> tuple[int | None, str | None]:
    """DeerFlow's run record is the authoritative count (README); older fields undercount."""
    rec = _run_records().get((suite, run)) or meta.get("usage_run_record")
    if rec and rec.get("total_tokens"):
        return rec["total_tokens"], "run_record"
    for key in ("usage_events_total", "usage_attributed_total"):
        if meta.get(key):
            return meta[key]["total_tokens"], key
    return None, None


def _topic(prompt: str) -> str:
    m = re.search(r"review on (.+?)\.\s", prompt or "")
    return m.group(1) if m else ""


def _row(
    suite: str, run: str, summary_row: dict | None, coverage_row: dict | None
) -> dict:
    d = RUNS / f"suite-{suite}" / run
    meta = _json(d / "meta.json", {})
    cites = (_json(d / "citations.json", {}) or {}).get("metrics", {})
    decisions = [
        e["event"] for e in _jsonl(d / "gate.jsonl") if e.get("event") in DECISIONS
    ]
    tokens, source = _tokens(suite, run, meta)
    row = {
        "run": run,
        "topic": _topic(meta.get("prompt", "")),
        "seconds": meta.get("wall_seconds"),
        "tokens": tokens,
        "token_source": source,
        "status": "ok" if (d / "report.md").exists() else "no_report",
        "error": meta.get("error"),
        "refs": cites.get("references"),
        "verified": cites.get("verified", {}).get("ok"),
        "in_window": cites.get("in_window", {}).get("ok"),
        "in_category": cites.get("in_category", {}).get("ok"),
        "gate_final": decisions[-1] if decisions else None,
        "gate_rejections": decisions.count("rejected"),
        "evidence": len(_jsonl(d / "evidence.jsonl")),
    }
    if summary_row:
        row["status"] = summary_row.get("status", row["status"])
    row["clean"] = clean(row) if row["refs"] is not None else None
    if coverage_row:
        row["coverage_hits"] = coverage_row.get("hits")
        row["coverage_gold"] = coverage_row.get("gold")
    return row


def suite(name: str) -> dict:
    d = _suite_dir(name)
    summary = _json(d / "summary.json", {}) or {}
    coverage = _json(d / "coverage.json", {}) or {}
    by_run = {r["run"]: r for r in summary.get("rows", [])}
    cov_by_run = {r["run"]: r for r in coverage.get("rows", [])}
    rows = [_row(name, r, by_run.get(r), cov_by_run.get(r)) for r in _run_ids(d)]
    return {**_suite_head(name, rows, coverage), "rows": rows}


def _suite_head(name: str, rows: list[dict], coverage: dict) -> dict:
    timed = [r["seconds"] for r in rows if r["seconds"]]
    counted = [r["tokens"] for r in rows if r["tokens"]]
    judged = [r for r in rows if r["clean"] is not None]
    checked = [r for r in judged if r["status"] == "ok"]
    refs = sum(r["refs"] for r in checked)
    return {
        "name": name,
        "label": LABELS.get(name, name),
        "kind": _kind(name),
        "runs": len(rows),
        "delivered": sum(r["status"] == "ok" for r in rows),
        "clean_runs": sum(bool(r["clean"]) for r in judged) if judged else None,
        "mean_seconds": round(statistics.mean(timed), 1) if timed else None,
        "mean_tokens": round(statistics.mean(counted)) if counted else None,
        # Over the references of delivered reports, as aggregate.py does.
        "verified_rate": round(sum(r["verified"] or 0 for r in checked) / refs, 3)
        if refs
        else None,
        "coverage_precision": (coverage.get("summary") or {}).get("mean_precision"),
    }


def suites() -> list[dict]:
    out = []
    for name in _suite_names():
        s = suite(name)
        s.pop("rows")
        out.append(s)
    return out


def run(suite_name: str, run_id: str) -> dict:
    d = _run_dir(suite_name, run_id)
    meta = _json(d / "meta.json", {})
    tokens, source = _tokens(suite_name, run_id, meta)
    citations = _json(d / "citations.json")
    return {
        "suite": suite_name,
        "run": run_id,
        "topic": _topic(meta.get("prompt", "")),
        "prompt": meta.get("prompt"),
        "model": meta.get("model"),
        "seconds": meta.get("wall_seconds"),
        "tokens": tokens,
        "token_source": source,
        "error": meta.get("error"),
        "report": (d / "report.md").read_text() if (d / "report.md").exists() else None,
        "citations": citations,
        "gate": _jsonl(d / "gate.jsonl"),
        "claims": _claims(d),
        "evidence": _jsonl(d / "evidence.jsonl"),
        "papers": _paper_list(d, citations),
    }


def _paper_list(d: Path, citations: dict | None) -> list[dict]:
    """Retrieved papers, plus arXiv metadata for verified citations the run did not record.

    Unverified ids get no metadata: the paper behind a resolvable id is not the one the report described.
    """
    papers = dict(_papers(d))
    cache = _arxiv_cache()
    for r in (citations or {}).get("rows", []):
        if r.get("verified") and r["id"] not in papers and r["id"] in cache:
            papers[r["id"]] = {"id": r["id"], **cache[r["id"]]}
    keys = ("id", "title", "authors", "published", "primary_category")
    return [{k: p.get(k) for k in keys} for p in papers.values()]


def _run_dir(suite_name: str, run_id: str) -> Path:
    d = _suite_dir(suite_name)
    if run_id not in _run_ids(d):
        raise NotFound(run_id)
    return d / run_id


@lru_cache(maxsize=1)
def _arxiv_cache() -> dict:
    """check_citations.py's arXiv metadata cache (tracked); ids checked after the last commit may be missing."""
    return _json(ROOT / "eval" / ".arxiv_cache.json", {}) or {}


def _papers(d: Path) -> dict[str, dict]:
    return {p["id"]: p for p in (_json(d / "search.json") or {}).get("papers", [])}


_TEX = str.maketrans({c: "\\" + c for c in "&%$#_{}"})


def _bib_key(meta: dict, pid: str, used: set[str]) -> str:
    last = (
        re.sub(r"[^a-z]", "", (meta.get("authors") or ["arxiv"])[0].split()[-1].lower())
        or "arxiv"
    )
    word = next(
        (
            w
            for w in re.findall(r"[a-z]+", (meta.get("title") or "").lower())
            if len(w) > 3
        ),
        pid.replace(".", ""),
    )
    key = f"{last}{(meta.get('published') or '')[:4]}{word}"
    while key in used:
        key += "x"
    used.add(key)
    return key


def bibtex(suite_name: str, run_id: str) -> str:
    """Verified citations only; ids that failed the arXiv check are listed as comments, not exported."""
    d = _run_dir(suite_name, run_id)
    rows = (_json(d / "citations.json", {}) or {}).get("rows", [])
    papers, cache = _papers(d), _arxiv_cache()
    out, used = (
        [f"% {suite_name}/{run_id}: verified citations of the delivered report"],
        set(),
    )
    for r in rows:
        if not r.get("verified"):
            continue
        pid = r["id"]
        meta = papers.get(pid) or cache.get(pid) or {}
        fields = {
            "title": "{" + meta["title"].translate(_TEX) + "}"
            if meta.get("title")
            else None,
            "author": " and ".join(meta["authors"]).translate(_TEX)
            if meta.get("authors")
            else None,
            "year": (meta.get("published") or "")[:4] or None,
            "eprint": pid,
            "archivePrefix": "arXiv",
            "primaryClass": meta.get("primary_category"),
            "url": f"https://arxiv.org/abs/{pid}",
        }
        body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields.items() if v)
        out.append(f"@misc{{{_bib_key(meta, pid, used)},\n{body}\n}}")
    rejected = [r["id"] for r in rows if not r.get("verified")]
    if rejected:
        out.append("% Not exported, failed the arXiv check: " + ", ".join(rejected))
    if not rows:
        out.append("% No citation check for this run.")
    return "\n\n".join(out) + "\n"


def evidence_csv(suite_name: str, run_id: str) -> str:
    d = _run_dir(suite_name, run_id)
    papers = _papers(d)
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(
        [
            "evidence",
            "arxiv_id",
            "title",
            "section",
            "paragraph",
            "quote",
            "claim",
            "url",
        ]
    )
    for e in _jsonl(d / "evidence.jsonl"):
        pid, para = e.get("paper", ""), e.get("para")
        url = (
            f"https://arxiv.org/html/{pid}#{para}"
            if para
            else f"https://arxiv.org/abs/{pid}"
        )
        title = papers.get(pid, {}).get("title", "")
        w.writerow(
            [
                e.get("e"),
                pid,
                title,
                e.get("section"),
                para,
                e.get("quote"),
                e.get("claim"),
                url,
            ]
        )
    return "\ufeff" + buf.getvalue()  # BOM so spreadsheet apps read UTF-8


def _claims(d: Path) -> dict | None:
    claims = _json(d / "claims.json")
    if not claims:
        return None
    # Judge v2 is the adopted judge (holdout kappa 0.74); fall back to v1 for older runs.
    for name, version in (
        ("claim_judgments.v2.json", "v2"),
        ("claim_judgments.json", "v1"),
    ):
        judged = _json(d / name)
        if judged:
            break
    else:
        judged, version = {"judgments": []}, None
    by_claim = defaultdict(list)
    for j in judged.get("judgments", []):
        by_claim[j["claim"]].append(
            {"id": j["id"], "label": j["label"], "reason": j.get("reason")}
        )
    items = [
        {**c, "judgments": by_claim.get(i, [])}
        for i, c in enumerate(claims.get("claims", []))
    ]
    return {"judge": version, "items": items}


def _arm(name: str) -> dict:
    s = suite(name)
    rows = s["rows"]
    k, n = sum(bool(r["clean"]) for r in rows), len(rows)
    lo, hi = wilson(k, n)
    topics = defaultdict(list)
    for r in rows:
        topics[r["run"].split("-")[0]].append(bool(r["clean"]))
    summary = (_json(_suite_dir(name) / "summary.json", {}) or {}).get("summary", {})
    return {
        "suite": name,
        "label": s["label"],
        "runs": n,
        "clean_runs": k,
        "wilson95": [round(lo, 3), round(hi, 3)],
        "topics": len(topics),
        "topics_clean_every_repeat": sum(all(v) for v in topics.values()),
        "delivered": s["delivered"],
        "mostly_fabricated": summary.get("runs_mostly_fabricated"),
        "verified_rate": summary.get("verified_rate"),
        "in_window_rate": summary.get("in_window_rate"),
        "in_category_rate": summary.get("in_category_rate"),
        "mean_seconds": s["mean_seconds"],
        "mean_tokens": s["mean_tokens"],
    }


def _support(name: str, prompt: str = "v2") -> dict:
    """Share of judged (claim, paper) pairs labelled supported, as in `claims.py summary`."""
    counts = {"pairs": 0, "supported": 0, "verified_pairs": 0, "verified_supported": 0}
    for d in claim_eval.runs_of(name):
        judged = _json(d / claim_eval.judgments_file(prompt))
        if not judged:
            continue
        rows = (_json(d / "citations.json", {}) or {}).get("rows", [])
        verified = {r["id"] for r in rows if r.get("verified")}
        for j in judged["judgments"]:
            if j["label"] not in claim_eval.LABELS:
                continue
            ok = j["label"] == "supported"
            counts["pairs"] += 1
            counts["supported"] += ok
            if j["id"] in verified:
                counts["verified_pairs"] += 1
                counts["verified_supported"] += ok
    return {
        "judge": prompt,
        "pairs": counts["pairs"],
        "supported_rate": round(counts["supported"] / counts["pairs"], 3)
        if counts["pairs"]
        else None,
        "verified_only_supported_rate": (
            round(counts["verified_supported"] / counts["verified_pairs"], 3)
            if counts["verified_pairs"]
            else None
        ),
    }


def overview() -> dict:
    arms = [_arm("holdout3-base"), _arm("holdout3-v3")]
    for a in arms:
        a["claims"] = _support(a["suite"])
    return {
        "arms": arms,
        "suites": len(_suite_names()),
        "runs": sum(len(_run_ids(RUNS / f"suite-{n}")) for n in _suite_names()),
    }
