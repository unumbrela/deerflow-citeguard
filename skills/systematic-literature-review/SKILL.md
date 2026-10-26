---
name: systematic-literature-review
description: Use this skill when the user wants a systematic literature review, survey, or synthesis across multiple academic papers on a topic. Also covers annotated bibliographies and cross-paper comparisons. Searches arXiv and outputs reports in APA, IEEE, or BibTeX format. Not for single-paper tasks — use academic-paper-review for reviewing one paper.
---

# Systematic Literature Review Skill

## Overview

This skill produces a structured **systematic literature review (SLR)** across multiple academic papers on a research topic. Given a topic query, it searches arXiv, extracts structured metadata (research question, methodology, key findings, limitations) from each paper in parallel, synthesizes themes across the full set, and emits a final report with consistent citations.

**Distinct from `academic-paper-review`:** that skill does deep peer review of a single paper. This skill does breadth-first synthesis across many papers. If the user hands you one paper URL and asks "review this paper", route to `academic-paper-review` instead.

## When to Use This Skill

Use this skill when the user wants any of the following:

- A literature survey on a topic ("survey transformer attention variants", "review the literature on diffusion models")
- A synthesis across multiple papers ("what do recent papers say about X", "compare methodologies across papers on Y")
- A systematic review with consistent citation format ("do an SLR on Z in APA format")
- An annotated bibliography on a topic
- An overview of research trends in a field over a time window

Do **not** use this skill when:

- The user provides exactly one paper and asks to review it (use `academic-paper-review`)
- The user asks a factual question that does not require synthesizing multiple sources (answer directly)
- The user wants general web research without academic rigor (use standard web search)

## Workflow

The workflow has five phases. Follow them in order.

### Phase 1: Plan

Before doing any retrieval, confirm the following with the user. If any of these are unclear, ask **one** clarifying question that covers the missing pieces. Do not ask one question at a time.

- **Topic**: the research area in plain English (e.g. "transformer attention variants").
- **Scope**: how many papers (default 20, hard upper bound 50), optional time window (e.g. "last 2 years"), optional arXiv category (e.g. `cs.CL`, `cs.CV`).
- **Citation format**: APA, IEEE, or BibTeX (default APA if the user does not specify and does not seem to be writing for a specific venue).
- **Output location**: where to save the final report (default `/mnt/user-data/outputs/`).

If the user says "50+ papers", politely cap it at 50 and explain that synthesis quality degrades quickly past that — for larger surveys they should split by sub-topic.

### Phase 2: Search arXiv

Call the **scholar search tool** (its name starts with `ext_community_scholar_search`). It is provided by the scholar plugin and runs inside DeerFlow, so no shell is needed. Do **not** search arXiv by any other means (no `web_search`, `web_fetch`, or your own HTTP client), and do not re-filter its output.

```json
{"query": "<2-3 core keywords>", "max_results": <N>, "category": "<cat, optional>", "years": <N, optional>}
```

What it does for you, so you do not have to:

- Turns `years: 2` into an exact start date from today's date. Use `years` for "last N years"; never compute dates yourself. (`start_date` / `end_date` in `YYYY-MM-DD` are also accepted.)
- Keeps only papers whose **primary** category equals `category` (set `include_cross_lists: true` only if the user explicitly accepts cross-listed papers).
- Stores the full results for this conversation and splits them into **batches** sized to fit in one tool result.
- Returns a **compact index** (id, short title, first author, date, category) and the list of batch numbers.

**This index is the only list of papers that exists.** Every arXiv id you ever write must appear in it. Never type, guess, or "recall" a paper, id, title, or author that is not in the index or in a subagent's output derived from a batch. If you catch yourself about to add a paper from memory, stop: report the real count instead.

**Query phrasing — keep it short.** Multi-word queries are first matched as an exact phrase, so use 2-3 core keywords (e.g. `"agent evaluation"`) and put the field in `category`, not in the query. Drop words like "recent", "variants", "benchmarks for" — time belongs in `years`.

**Never drop or change `category` or `years` to get more papers.** They are the user's constraints. When the exact phrase returns fewer papers than requested, the tool itself widens the query (all words present, any order) and reports `"match":"phrase+all_terms"`; you do not need to retry.

**Run the search once.** If it returns `count: 0`, tell the user and suggest broadening the topic or removing the category. If it returns fewer than requested, that is the real size of the result set under the user's constraints: do not pad, do not relax the filters, and state the shortfall plainly in the report. If it returns `ERROR: ...`, report the error to the user and stop. The tool already retries transient arXiv rate limits itself.

### Phase 3: Extract metadata in parallel

**You MUST delegate extraction to subagents via the `task` tool.** Do not extract metadata yourself.

**Pass batch numbers, not paper text.** Re-typing abstracts into a prompt is exactly where invented papers come from. Dispatch one subagent per batch listed in the search result, using this prompt (only the batch number changes):

```
Execute this task: extract structured metadata from arXiv papers.

Call the tool whose name starts with `ext_community_scholar_get_batch` with
{"batch": 1}. It returns a JSON array of papers (id, title, authors, published,
abstract, ...). Work ONLY from that result. Do not search the web, do not use
any paper that is not in it.

For each paper return a JSON object with:
- arxiv_id (copy `id` exactly)
- title (copy exactly)
- authors (copy the list exactly; if `authors_total` is present, add "et al.")
- published_date (copy `published` exactly)
- research_question (1 sentence)
- methodology (1-2 sentences)
- key_findings (3-5 bullet points, only what the abstract supports)
- limitations (1-2 sentences, or "not stated in abstract")

Return a JSON array, one object per paper, same order as the tool result. No
text outside the JSON.
```

**Concurrency limit: at most 3 subagents per turn.** The runtime silently drops extra dispatches. Dispatch batches 1-3, wait for them to finish, then dispatch the next up to 3, and so on until every batch is covered.

**Parsing results**: `task` returns strings prefixed with `Task Succeeded. Result: ` (or `Task failed.` / `Task timed out.`). Strip the prefix before parsing. If a batch fails, note which papers are affected and continue; you may re-dispatch that single batch once.

After all rounds, flatten the arrays into one list, preserving order.

### Phase 4: Synthesize and format

Now produce the final SLR report. Two things happen here: cross-paper synthesis (thematic analysis) and citation formatting.

**Cross-paper synthesis**: the report must do more than list papers. At minimum, identify:

- **Themes**: 3-6 recurring research directions, approaches, or problem framings across the set.
- **Convergences**: findings that multiple papers agree on.
- **Disagreements**: where papers reach different conclusions or use incompatible methodologies.
- **Gaps**: what the collective literature does not yet address (often stated explicitly in the "limitations" fields).

If the paper set is too small or too heterogeneous to support thematic synthesis (e.g. 5 papers on wildly different sub-topics), say so explicitly in the report — do not force themes that are not there.

**Citation formatting**: the exact format depends on user preference. Read **only** the template file that matches the user's requested format, not all three:

- [templates/apa.md](templates/apa.md) — APA 7th edition. Default for social sciences and most CS journals. Use when the user requests APA or does not specify a format.
- [templates/ieee.md](templates/ieee.md) — IEEE numeric citations. Use when the user targets an IEEE conference or journal, or explicitly asks for IEEE.
- [templates/bibtex.md](templates/bibtex.md) — BibTeX entries. Use when the user mentions BibTeX, LaTeX, or wants machine-readable references. **Important**: arXiv papers are cited as `@misc`, not `@article` — the BibTeX template covers this explicitly.

**Dates come from the search result, never from memory.** Fill the report's `Date`, "retrieved on" and "published between" fields from `report_dates` in the search result, and use `report_dates.today` in the file name. Your own sense of today's date is often a year off; the citation gate rejects reports whose dates contradict the search.

Each template contains both the citation rules and a full report structure (executive summary, themes, per-paper annotations, references, methodology section). Follow the template's structure verbatim for the report body, then fill in content from your Phase 3 metadata.

### Phase 5: Save and present

1. Write the full report to `/mnt/user-data/outputs/slr-<topic-slug>-<YYYYMMDD>.md` (lowercase, hyphenated topic; today's date).
2. Call `present_files` with the report path. **A citation gate checks the report when you present it**: every arXiv id in it must come from this conversation's search.
   - If the result says `CITATION CHECK FAILED ... NOT verified`, the report is **not** done: the user can see the file, but it cites ids that are not from the search. Edit the file first (presenting an unchanged file fails again): remove the listed ids or replace them with papers from the index you have not cited yet, fix every sentence and reference that mentioned them, save, and call `present_files` again. If the user explicitly demanded one of those references and you keep it, tell the user plainly that it is not from the search and could not be verified.
   - If it says `Citation check passed` with entries to fix (title not verbatim, first author missing from the reference line), correct them to match the subagent output exactly, save, and present again.
   - If it says the check failed again after the maximum number of rejections, tell the user plainly which ids could not be verified.
3. If the report promises N papers, it must cite N papers from the index (or state the shortfall).

**In the chat message**, show a short preview: the executive summary verbatim, the theme names with a one-line gloss each, and the paper count with a pointer to the file. Do **not** dump the full report inline.

## Examples

**Example 1: Typical SLR request**

User: "Do a systematic literature review of recent transformer attention variants, 20 papers, APA format."

Your flow:
1. Phase 1: confirm topic (transformer attention variants), scope (20 papers, default time window), format (APA). Ask **one** clarification only if something is missing (e.g. "Any particular time window, or should I default to the last 3 years?").
2. Phase 2: scholar search with `{"query": "transformer attention", "max_results": 20, "years": 3}`.
3. Phase 3: one subagent per batch, at most 3 per round (e.g. 4 batches = a round of 3, then a round of 1). Aggregate.
4. Phase 4: read `templates/apa.md`, write the report using its structure, fill in themes + per-paper annotations from Phase 3 metadata.
5. Phase 5: save to `slr-transformer-attention-20260409.md` and call `present_files`; if the citation gate rejects it, fix the listed ids and present again.

**Example 2: Small-set request with ambiguity**

User: "Survey a few papers on diffusion models for me."

Your flow:
1. Phase 1: "a few" is ambiguous. Ask one question: "How many papers would you like — 10, 20, or 30? And any citation format preference (APA is the default)?"
2. User responds "10, BibTeX".
3. Phase 2: scholar search with `{"query": "diffusion models", "max_results": 10, "category": "cs.CV"}`.
4. Phase 3: one round, one subagent per batch.
5. Phase 4: read `templates/bibtex.md`, format with `@misc` entries (not `@article`).
6. Phase 5: save, verify, present.

**Example 3: Out-of-scope request**

User: "Here's one paper (https://arxiv.org/abs/1706.03762). Can you review it?"

This is a single-paper peer review, not a literature survey. Do not use this skill. Route to `academic-paper-review` instead.

## Notes

- **Prerequisite: `subagent_enabled` must be `true`**. Phase 3 requires the `task` tool for parallel metadata extraction. This tool is only loaded when `subagent_enabled` is set to `true` in the runtime config (`config.configurable.subagent_enabled`). Without it, the `task` tool will not appear in the available tools and Phase 3 cannot execute as designed.
- **arXiv only, by design**. This skill does not query Semantic Scholar, PubMed, or Google Scholar. arXiv covers the bulk of CS/ML/physics/math preprints, which is what DeerFlow users most often want to survey. Multi-source academic search belongs in a dedicated MCP server, not inside this skill.
- **Requires the scholar plugin** (`deerflow-extension-scholar`). It provides the search and batch tools and the citation gate; without it, tell the user the skill is not installed correctly instead of searching by other means.
- **Hard upper bound of 50 papers**. Surveys larger than 50 papers degrade in synthesis quality and are better done by splitting into sub-topics.
- **Phase 3 requires subagents to be enabled**. This skill's parallel extraction step hard-requires the `task` tool, which is only available when `subagent_enabled=true` at runtime. If subagents are unavailable, do not claim to execute the Phase 3 parallel plan; instead, tell the user that subagents must be enabled for the full workflow, or offer to narrow/split the request into a smaller manual review.
- **Subagent results are strings, not objects**. Always strip the `Task Succeeded. Result: ` / `Task failed.` / `Task timed out.` prefixes before parsing the JSON payload.
- **The `id` field is a bare arXiv id** (e.g. `1706.03762`), not a URL and not with a version suffix. `abs_url` / `pdf_url` hold the full URLs if you need them.
- **Synthesis, not listing**. The final report must identify themes and compare findings across papers. A report that only lists papers one after another is a failure mode — if you cannot find themes, say so explicitly instead of faking them.
