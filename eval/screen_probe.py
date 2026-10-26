"""Does model screening of a candidate pool pick more gold papers than arXiv's relevance order? (P2 2.1, offline)

Usage:
    python3 -I pool_probe.py --out /tmp/pool.json          # candidate pools first
    python3 -I screen_probe.py --pools /tmp/pool.json [--pool 50] [--batch 10] [--model qwen3.5-plus]

Simulates the planned workflow without the agent: the top ``--pool`` candidates are split into batches of
``--batch`` (as screening subagents would see them: title + truncated abstract), the model scores each paper
0-3 for how central it is to the topic, and the top 10 by score (ties: arXiv rank) are compared with arXiv's
own top 10. Development set only.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from claims import _api_key, load_abstracts  # noqa: E402

ABSTRACT_CHARS = 600
PROMPT = """You are screening candidate papers for a systematic literature review on "{topic}" (arXiv {category}).
Score each paper by how central it is to that topic:
3 = its main contribution is about the topic itself (a method, benchmark, analysis or system for it)
2 = substantially about the topic, but as one part of a broader contribution
1 = only touches the topic (uses it as a tool, mentions it, applies a neighbouring idea)
0 = not about the topic
Judge from the title and abstract only. Return JSON: {{"scores": [{{"id": "<id>", "score": <0-3>, "reason": "<at most 12 words>"}}, ...]}} with one entry per paper, in order.

Papers:
{papers}"""


def call(prompt: str, model: str, key: str) -> tuple[dict, dict]:
    body = {"model": model, "temperature": 0, "messages": [{"role": "user", "content": prompt}], "response_format": {"type": "json_object"}, "enable_thinking": False}
    req = urllib.request.Request("https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions", data=json.dumps(body).encode(), headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                out = json.loads(resp.read())
            return json.loads(out["choices"][0]["message"]["content"]), out.get("usage", {})
        except Exception:  # noqa: BLE001
            time.sleep(2 * 2**attempt)
    raise SystemExit("model call failed")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pools", required=True)
    ap.add_argument("--pool", type=int, default=50)
    ap.add_argument("--batch", type=int, default=10)
    ap.add_argument("--model", default="qwen3.5-plus")
    ap.add_argument("--out")
    args = ap.parse_args()
    key = _api_key()
    topics = {t["id"]: t for t in json.loads((HERE / "coverage_topics.json").read_text())["topics"]}
    rows = json.loads(Path(args.pools).read_text())
    meta = load_abstracts({p for r in rows for p in r["pool_ids"][: args.pool]})
    tokens = 0
    results = []
    for r in rows:
        topic = topics[r["id"]]
        gold = set(topic["gold"])
        cands = r["pool_ids"][: args.pool]
        scores: dict[str, int] = {}
        for i in range(0, len(cands), args.batch):
            chunk = cands[i : i + args.batch]
            papers = "\n\n".join(f"id: {p}\ntitle: {meta[p]['title']}\nabstract: {meta[p]['abstract'][:ABSTRACT_CHARS]}" for p in chunk)
            out, usage = call(PROMPT.format(topic=topic["topic"], category=topic["category"], papers=papers), args.model, key)
            tokens += usage.get("total_tokens", 0)
            for s in out.get("scores", []):
                if s.get("id") in chunk:
                    scores[s["id"]] = int(s.get("score", 0))
        ranked = sorted(cands, key=lambda p: (-scores.get(p, 0), cands.index(p)))
        top_rank, top_screen = cands[:10], ranked[:10]
        row = {
            "id": r["id"],
            "pool_gold": sum(p in gold for p in cands),
            "rank_top10": sum(p in gold for p in top_rank),
            "screen_top10": sum(p in gold for p in top_screen),
            "score_hist": {s: sum(v == s for v in scores.values()) for s in range(4)},
            "gold_scores": [scores.get(p) for p in cands if p in gold],
            "scores": scores,
        }
        results.append(row)
        print(f"{r['id']} pool_gold={row['pool_gold']:3} rank@10={row['rank_top10']} screen@10={row['screen_top10']} hist={row['score_hist']} gold_scores={row['gold_scores']}", flush=True)
    print(f"total: rank@10={sum(x['rank_top10'] for x in results)} screen@10={sum(x['screen_top10'] for x in results)} of {10 * len(results)}; tokens={tokens}")
    if args.out:
        Path(args.out).write_text(json.dumps(results, indent=1))


if __name__ == "__main__":
    main()
