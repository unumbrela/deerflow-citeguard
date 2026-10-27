"""evidence_index: the lead's paper -> cite_as -> evidence ids map."""

import json

from helpers import paper
from test_evidence_tools import args, selected, store  # noqa: F401 - fixture
from test_tools import THREAD, ctx

from deerflow_extension_scholar import cite_as, evidence_index_payload


def test_cite_as_follows_apa_and_disambiguates_shared_author_years():
    one = {**paper(1), "authors": ["Kuan Li"]}
    two = {**paper(2), "authors": ["Xiaoxi Li", "Bo Wu"]}
    walker = {**paper(3), "title": "WebWalker: Benchmarking LLMs", "authors": ["Jialong Wu", "A B", "C D"]}
    dancer = {**paper(4), "title": "WebDancer: Towards Autonomous Agency", "authors": ["Jialong Wu", "E F", "G H"]}
    assert cite_as([one, two, walker, dancer]) == {
        "2501.00001": "Li, 2025",
        "2501.00002": "Li & Wu, 2025",
        "2501.00003": "Wu et al., 2025b",  # titles in order: WebDancer before WebWalker
        "2501.00004": "Wu et al., 2025a",
    }


def test_payload_gives_ready_made_bullets_and_pages_instead_of_cutting():
    papers = [paper(i) for i in range(1, 11)]
    evidence = [{"e": f"E{n}", "paper": papers[n % 9]["id"], "claim": f"Finding number {n} " + "x" * 300} for n in range(1, 61)]
    payload = evidence_index_payload(papers, evidence)
    assert len(json.dumps(payload)) <= 8500
    listed = [p["id"] for p in payload["papers"]] + payload["more"]
    assert sorted(listed) == [p["id"] for p in papers]  # every paper exactly once, here or in `more`
    assert payload["more"] and payload["without_evidence"] == ["2501.00010"]
    first = payload["papers"][0]
    assert first["findings_md"].splitlines()[0] == f"- Finding number 9 {'x' * 300} (Smith1 & Jones0, 2025) [E9]."
    # Paged: one paper at a time, whole bullets.
    one = evidence_index_payload(papers, evidence, only=payload["more"][0])
    assert [p["id"] for p in one["papers"]] == [payload["more"][0]] and "more" not in one


async def test_tool_lists_this_searchs_evidence(store):  # noqa: F811
    t = await selected(store, [])
    item = {"paper": "2501.00001", "paragraph": "S2.p3", "quote": "the agent solved 3 of twenty long web tasks", "claim": "Solves 3 of 20 tasks."}
    await t["cite_evidence"](args(evidence=[item]), ctx())
    result = json.loads((await t["evidence_index"](args(), ctx())).content)
    by_id = {p["id"]: p for p in result["papers"]}
    assert by_id["2501.00001"]["findings_md"] == "- Solves 3 of 20 tasks (Smith1 & Jones0, 2025) [E1]."
    assert by_id["2501.00001"]["cite_as"] == "Smith1 & Jones0, 2025"
    assert set(result["without_evidence"]) == {"2501.00002", "2501.00003"}
    assert "another user" in (await t["evidence_index"](args(), ctx(user="mallory"))).content


async def test_a_screened_search_is_not_replaced_without_restart(store):  # noqa: F811
    t = await selected(store, [])
    before = store.load_search(THREAD)
    result = await t["search"](args(query="something else entirely", max_results=3), ctx())
    assert result.content.startswith("ERROR: this conversation's review is built on a screened search")
    assert store.load_search(THREAD)["search_id"] == before["search_id"]
    restarted = json.loads((await t["search"](args(query="something else entirely", max_results=3, restart=True), ctx())).content)
    assert restarted["pool"] == 3 and store.load_search(THREAD)["search_id"] != before["search_id"]


async def test_a_search_before_screening_or_after_rejection_can_be_redone(store):  # noqa: F811
    t = await selected(store, [])
    store.save_search(THREAD, {**store.load_search(THREAD), "rejected": "wrong category"})
    assert not (await t["search"](args(query="agents", max_results=3), ctx())).content.startswith("ERROR")
    # Unscreened: the lead may refine its query before screening.
    assert not (await t["search"](args(query="agents again", max_results=3), ctx())).content.startswith("ERROR")


def test_a_pasted_bullet_passes_the_gates_attachment_check():
    from deerflow_extension_scholar.core import misattached_evidence

    papers = [paper(1), paper(2)]
    evidence = [{"e": "E1", "paper": "2501.00001", "claim": "Agents fail on long tasks"}, {"e": "E2", "paper": "2501.00002", "claim": "Planning helps"}]
    bullets = "\n".join(p["findings_md"] for p in evidence_index_payload(papers, evidence)["papers"])
    report = f"# Review\n\n## Themes\n\nSome synthesis.\n\n### Key findings\n\n{bullets}\n"
    assert misattached_evidence(report, {e["e"]: e for e in evidence}, {p["id"]: p for p in papers}) == []
