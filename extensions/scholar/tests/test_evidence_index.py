"""evidence_index: the lead's paper -> cite_as -> evidence ids map."""

import json

from helpers import paper
from test_evidence_tools import args, selected, store  # noqa: F401 - fixture
from test_tools import ctx

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


def test_payload_groups_evidence_by_paper_and_fits_the_budget():
    papers = [paper(i) for i in range(1, 11)]
    evidence = [{"e": f"E{n}", "paper": papers[n % 9]["id"], "claim": "x" * 400} for n in range(1, 61)]
    payload = evidence_index_payload(papers, evidence)
    assert len(json.dumps(payload)) <= 8500
    assert payload["without_evidence"] == ["2501.00010"]
    second = payload["papers"][1]
    assert second["cite_as"] == "Smith2 & Jones0, 2025"
    # Over budget, findings were shortened before anything else was dropped: every id is still listed.
    assert sum(len(p["evidence"]) for p in payload["papers"]) == 60
    assert all(len(e["finding"]) < 400 for p in payload["papers"] for e in p["evidence"] if isinstance(e, dict))


async def test_tool_lists_this_searchs_evidence(store):  # noqa: F811
    t = await selected(store, [])
    item = {"paper": "2501.00001", "paragraph": "S2.p3", "quote": "the agent solved 3 of twenty long web tasks", "claim": "Solves 3 of 20 tasks."}
    await t["cite_evidence"](args(evidence=[item]), ctx())
    result = json.loads((await t["evidence_index"](args(), ctx())).content)
    by_id = {p["id"]: p for p in result["papers"]}
    assert by_id["2501.00001"]["evidence"] == [{"e": "E1", "finding": "Solves 3 of 20 tasks."}]
    assert by_id["2501.00001"]["cite_as"] == "Smith1 & Jones0, 2025"
    assert set(result["without_evidence"]) == {"2501.00002", "2501.00003"}
    assert "another user" in (await t["evidence_index"](args(), ctx(user="mallory"))).content
