"""Offline integration: real tools/store/gate, with only HTTP and model scoring mocked."""

import json

from test_evidence_tools import ABSTRACT, args, selected
from test_gate import RUNTIME, state_after_present
from test_tools import THREAD, ctx

from deerflow_extension_scholar.core import APPENDIX_BEGIN
from deerflow_extension_scholar.gate import CitationGateMiddleware
from deerflow_extension_scholar.store import PaperStore


async def test_search_read_evidence_repair_and_delivery(tmp_path):
    store = PaperStore(str(tmp_path / "scholar"))
    requests = []
    handlers = await selected(store, requests)
    batch = json.loads((await handlers["get_batch"](args(batch=1), ctx())).content)
    reading = await handlers["read_paper"](args(paper="2501.00001", section="S2"), ctx())
    quote = "the agent solved 3 of twenty long web tasks"
    assert quote in reading.content
    evidence = [
        {"paper": "2501.00001", "paragraph": "S2.p3", "quote": quote, "claim": "Solves 3 of 20 tasks."},
        {"paper": "2501.00002", "paragraph": "abstract", "quote": ABSTRACT, "claim": "Introduces a long-task benchmark."},
        {"paper": "2501.00003", "paragraph": "S1.p2", "quote": "Agents fail on long tasks in every setting we tried.", "claim": "Finds failures on long tasks."},
    ]
    recorded = json.loads((await handlers["cite_evidence"](args(evidence=evidence), ctx())).content)
    assert len(recorded["accepted"]) == 3 and not recorded.get("rejected")
    paragraphs = [f"{item['claim']} (Smith{n}, 2025) [{entry['evidence']}]." for n, (item, entry) in enumerate(zip(evidence, recorded["accepted"], strict=True), 1)]
    refs = [f"{p['authors'][0]} (2025). {p['title']}. arXiv:{p['id']}" for p in batch]
    report = "\n\n".join([*paragraphs, "## References", *refs]) + "\n"
    outputs = tmp_path / "outputs"
    outputs.mkdir()
    gate = CitationGateMiddleware(store)
    invented = report.replace("[E1]", "[E99]")
    rejected = gate.before_model(state_after_present(outputs, report=invented), RUNTIME)["messages"][0]
    assert "never issued" in rejected.content
    assert (outputs / "slr-agents.md").read_text() == invented
    accepted = gate.before_model(state_after_present(outputs, report=report, call_id="fixed"), RUNTIME)["messages"][0]
    assert "3 evidence ids checked" in accepted.content
    delivered = (outputs / "slr-agents.md").read_text()
    assert quote in delivered and "#S2.p3" in delivered and ABSTRACT in delivered
    assert delivered.count(APPENDIX_BEGIN) == 1
    gate.before_model(state_after_present(outputs, report=delivered, call_id="again"), RUNTIME)
    assert (outputs / "slr-agents.md").read_text() == delivered
    decisions = store.read_log(THREAD)
    assert [row["event"] for row in decisions] == ["rejected", "accepted", "accepted"]
    assert all(row["evidence_schema_version"] == 1 for row in decisions)
    assert decisions[-1]["used"] == ["E1", "E2", "E3"]
    assert decisions[-1]["papers_without_evidence"] == []
