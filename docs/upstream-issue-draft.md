# 上游 issue(已发布)

已发布为 [bytedance/deer-flow#7601](https://github.com/bytedance/deer-flow/issues/7601)(2026-10-27)。下面是发出的原文;发布前把标题里的运行数从 57 改成了 50(表里两组外置运行 22 + 28),并注明当前 main 上 skill 和外置阈值都没变。

目标仓库：bytedance/deer-flow。已查过：没有重复（#3416 讲的是外置文件读不到，跟这里不是一回事）。

---

**Title:** systematic-literature-review fabricates papers when the arXiv search output is externalized and not read back (measured on 50 runs)

### Problem summary

With `allow_host_bash: true`, the public `systematic-literature-review` skill runs `arxiv_search.py`; for 10 papers its output is ~19,600 chars, above `tool_output.externalize_min_chars` (12,000). The model then receives the synopsis (structure + head/tail samples + a hint to `read_file` the raw log). When it does not read the log back, it re-types a "list of 10 papers" into the subagent prompts and invents the ones it never saw: ids, titles and authors (one report listed "Various authors").

### Evidence

`qwen3.5-plus`, memory off, upstream commit `3fdd9bd`. The skill is unchanged on current `main` (`68c9fce`), and so is the 12,000-char externalization default. Every citation was checked against the arXiv API (the id exists **and** the title matches). The first set was traced by hand; in the held-out set a script counts a run as "read back" when its event stream has a `read_file` call on `.tool-results/`.

| externalized search output … | 30 topics × 1 run: runs | ≥ half fabricated | 10 held-out topics × 3 runs: runs | ≥ half fabricated |
|---|---|---|---|---|
| read back with `read_file` | 18 | 0 | 18 | 0 |
| not read back | 4 | 4 | 10 | 9 |

Fisher exact p = 0.00014 (first set) and 1.4 × 10⁻⁶ (held-out set). This is an observational grouping, not a controlled experiment. Raw reports, citation checks and run metadata: https://github.com/unumbrela/deerflow-citeguard (`BASELINE.md`, `runs/`).

The synopsis already tells the model to read the file back, so prompt wording alone did not prevent it.

### What worked for us (no core changes)

Keep paper data out of the model's own words: code filters and stores the search, subagents fetch their batch directly, and a check on delivery requires every arXiv id in the report to come from the search. On 10 held-out topics × 3 runs, runs that delivered 10 papers with every citation verified, in the date window and in the category went from 1/30 to 29/30 (95% CI 83%–99%); runs with at least half the citations fabricated went from 9/28 to 0/30. We packaged it as an extension (`search` / `get_batch` plugin tools + a `before_model` citation gate), which also removes the need for `allow_host_bash`.

### Two questions for maintainers

1. Would a PR to the public skill be welcome? For example, writing search results to a file and passing file paths (not paper text) to subagents.
2. Extension `wrap_tool_call` hooks are observational and the `artifacts` reducer only appends, so an extension cannot withdraw a delivered file that fails a check. Is a generic "intercepting" contribution, or artifact removal, something you would consider?
