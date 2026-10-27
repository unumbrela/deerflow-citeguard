from types import SimpleNamespace

import pytest
from helpers import paper
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

from deerflow_extension_scholar.gate import MARKER, CitationGateMiddleware
from deerflow_extension_scholar.store import PaperStore

THREAD = "0f8e3c2a-1111-4222-8333-444455556666"
GOOD = "Smith1, A. (2025). Benchmarking Agents Part 1. arXiv:2501.00001\n"
BAD = GOOD + "Doe, J. (2025). Invented Paper. arXiv:2506.45678\n"


@pytest.fixture
def setup(tmp_path):
    store = PaperStore(str(tmp_path / "scholar"))
    store.save_search(THREAD, {"search_id": "s1", "owner": "alice", "papers": [paper(1), paper(2)], "batches": [["2501.00001", "2501.00002"]]})
    outputs = tmp_path / "outputs"
    outputs.mkdir()
    return store, outputs


def state_after_present(outputs, filename="slr-agents.md", report=GOOD, call_id="call-1"):
    (outputs / filename).write_text(report, encoding="utf-8")
    return {
        "messages": [
            HumanMessage("review", id="h1"),
            AIMessage("", id="a1", tool_calls=[{"id": call_id, "name": "present_files", "args": {"filepaths": [f"/mnt/user-data/outputs/{filename}"]}}]),
            ToolMessage("Successfully presented files", id="t1", name="present_files", tool_call_id=call_id),
        ],
        "thread_data": {"outputs_path": str(outputs)},
    }


RUNTIME = SimpleNamespace(context={"thread_id": THREAD})


def test_report_with_invented_id_is_rejected(setup):
    store, outputs = setup
    update = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=BAD), RUNTIME)
    [msg] = update["messages"]
    assert msg.id == "t1"  # replaced in place by the messages reducer
    assert "NOT verified" in msg.content and "2506.45678" in msg.content
    assert "unchanged" not in msg.content
    assert "Successfully presented" not in msg.content
    assert [r["event"] for r in store.read_log(THREAD)] == ["rejected"]


def test_clean_report_is_accepted_with_a_note(setup):
    store, outputs = setup
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs), RUNTIME)["messages"]
    assert msg.content.startswith("Successfully presented files")
    assert "Citation check passed: 1 arXiv ids" in msg.content
    assert store.read_log(THREAD)[0]["event"] == "accepted"


def test_released_with_warning_after_max_rejections(setup):
    store, outputs = setup
    gate = CitationGateMiddleware(store, max_blocks=2)
    contents = [gate.before_model(state_after_present(outputs, report=BAD, call_id=f"c{i}"), RUNTIME)["messages"][0].content for i in range(3)]
    assert "rejection 1 of 2" in contents[0] and "rejection 2 of 2" in contents[1]
    assert "unchanged since the previous rejection" in contents[1]
    assert "MUST tell the user" in contents[2]
    assert [r["event"] for r in store.read_log(THREAD)] == ["rejected", "rejected", "released_unverified"]


def test_threads_without_a_search_are_untouched(setup):
    store, outputs = setup
    runtime = SimpleNamespace(context={"thread_id": "another-thread"})
    assert CitationGateMiddleware(store).before_model(state_after_present(outputs, report=BAD), runtime) is None


def test_already_gated_results_are_not_checked_twice(setup):
    store, outputs = setup
    state = state_after_present(outputs, report=BAD)
    state["messages"][-1] = state["messages"][-1].model_copy(update={"content": f"{MARKER} CITATION CHECK FAILED"})
    assert CitationGateMiddleware(store).before_model(state, RUNTIME) is None


def test_only_the_latest_step_is_inspected(setup):
    store, outputs = setup
    state = state_after_present(outputs, report=BAD)
    state["messages"].append(AIMessage("thinking", id="a2"))
    assert CitationGateMiddleware(store).before_model(state, RUNTIME) is None


def test_non_markdown_and_escaping_paths_are_ignored(setup):
    store, outputs = setup
    state = state_after_present(outputs, report=BAD)
    state["messages"][1].tool_calls[0]["args"]["filepaths"] = ["/mnt/user-data/outputs/chart.png", "/mnt/user-data/outputs/../../etc/passwd.md"]
    assert CitationGateMiddleware(store).before_model(state, RUNTIME) is None


async def test_async_hook_matches_sync(setup):
    store, outputs = setup
    update = await CitationGateMiddleware(store).abefore_model(state_after_present(outputs, report=BAD), RUNTIME)
    assert "NOT verified" in update["messages"][0].content


def test_edited_file_is_not_reported_as_unchanged(setup):
    store, outputs = setup
    gate = CitationGateMiddleware(store)
    gate.before_model(state_after_present(outputs, report=BAD, call_id="c1"), RUNTIME)
    edited = BAD + "Some extra synthesis.\n"
    content = gate.before_model(state_after_present(outputs, report=edited, call_id="c2"), RUNTIME)["messages"][0].content
    assert "rejection 2 of 3" in content and "unchanged" not in content


def test_wrong_year_in_report_is_rejected(setup):
    store, outputs = setup
    search = store.load_search(THREAD)
    store.save_search(THREAD, {**search, "retrieved_on": "2026-10-26", "window": {"start": "2024-10-26", "end": None}})
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report="**Date**: 2025-10-26\n" + GOOD), RUNTIME)["messages"]
    assert "NOT verified" in msg.content and "2025-10-26 (search used 2026-10-26 / 2024-10-26)" in msg.content
    assert "may be invented" not in msg.content
    assert store.read_log(THREAD)[-1]["date_errors"] == ["2025-10-26 (search used 2026-10-26 / 2024-10-26)"]


def test_window_end_sharing_todays_month_day_is_accepted(setup):
    store, outputs = setup
    search = store.load_search(THREAD)
    store.save_search(THREAD, {**search, "retrieved_on": "2026-10-26", "window": {"start": "2023-10-27", "end": "2025-10-26"}})
    report = "**Date**: 2026-10-26\nPublished between 2023-10-27 and 2025-10-26.\n" + GOOD
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=report), RUNTIME)["messages"]
    assert "Citation check passed" in msg.content
    assert store.read_log(THREAD)[-1]["date_errors"] == []


def test_report_short_of_the_requested_count_is_rejected(setup):
    store, outputs = setup
    search = store.load_search(THREAD)
    store.save_search(THREAD, {**search, "requested": 2})
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=GOOD), RUNTIME)["messages"]
    assert "asked for 2 papers" in msg.content and "2501.00002" in msg.content
    assert store.read_log(THREAD)[-1]["missing"] == ["2501.00002"]


def test_fewer_requested_than_retrieved_is_fine(setup):
    store, outputs = setup
    search = store.load_search(THREAD)
    store.save_search(THREAD, {**search, "requested": 1})
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=GOOD), RUNTIME)["messages"]
    assert "Citation check passed" in msg.content


SEARCH_TOOL = "ext_community_scholar_search_1607103162c3"


def state_after_search(request="Review agents. 10 papers, category cs.CL.", args=None):
    return {
        "messages": [
            HumanMessage(request, id="h1"),
            AIMessage("", id="a1", tool_calls=[{"id": "s-call", "name": SEARCH_TOOL, "args": args or {"query": "agents", "max_results": 10}}]),
            ToolMessage('{"count":2,"index":[]}', id="t1", name=SEARCH_TOOL, tool_call_id="s-call"),
        ],
    }


def test_search_without_the_users_category_is_rejected(setup):
    store, _ = setup
    [msg] = CitationGateMiddleware(store).before_model(state_after_search(), RUNTIME)["messages"]
    assert msg.id == "t1" and "SEARCH REJECTED" in msg.content and "category cs.CL" in msg.content and '"count"' not in msg.content
    assert "rejected" in store.load_search(THREAD)
    assert store.read_log(THREAD)[-1]["event"] == "search_rejected"


def test_search_with_the_users_category_passes(setup):
    store, _ = setup
    store.save_search(THREAD, {**store.load_search(THREAD), "category": "cs.CL"})
    assert CitationGateMiddleware(store).before_model(state_after_search(), RUNTIME) is None
    assert CitationGateMiddleware(store).before_model(state_after_search(request="Review agents, last 2 years."), RUNTIME) is None


def test_hidden_host_reminders_are_not_the_users_request(setup):
    store, _ = setup
    state = state_after_search(request="Review agents, last 2 years.")
    state["messages"].insert(1, HumanMessage("reminder: category cs.CV", id="h2", additional_kwargs={"hide_from_ui": True}))
    assert CitationGateMiddleware(store).before_model(state, RUNTIME) is None


def test_search_without_category_is_released_with_a_warning_after_max_rejections(setup):
    store, _ = setup
    gate = CitationGateMiddleware(store, max_blocks=1)
    gate.before_model(state_after_search(), RUNTIME)
    store.save_search(THREAD, {k: v for k, v in store.load_search(THREAD).items() if k != "rejected"})  # the model searched again, still without it
    [msg] = gate.before_model(state_after_search(), RUNTIME)["messages"]
    assert msg.content.startswith('{"count"') and "MUST tell the user" in msg.content
    assert [r["event"] for r in store.read_log(THREAD)] == ["search_rejected", "search_released"]


def test_report_from_a_rejected_search_is_rejected(setup):
    store, outputs = setup
    store.save_search(THREAD, {**store.load_search(THREAD), "rejected": "wrong category"})
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs), RUNTIME)["messages"]
    assert "NOT verified" in msg.content and "rejected for using the wrong category" in msg.content


def finishing(outputs, report=GOOD, filename="slr-agents.md"):
    if report is not None:
        (outputs / filename).write_text(report, encoding="utf-8")
    return {"messages": [HumanMessage("review", id="h1"), AIMessage("Saved the review to slr-agents.md.", id="a9")], "thread_data": {"outputs_path": str(outputs)}}


def test_saved_but_unpresented_report_is_presented_by_the_gate(setup):
    store, outputs = setup
    gate = CitationGateMiddleware(store)
    [final] = gate.after_model(finishing(outputs), RUNTIME)["messages"]
    assert final.id == "a9" and final.content == "Saved the review to slr-agents.md."
    [call] = final.tool_calls
    assert call["name"] == "present_files" and call["args"] == {"filepaths": ["/mnt/user-data/outputs/slr-agents.md"]}
    # The loop routes to the tool node; after present_files runs, the usual check sees it.
    state = finishing(outputs)
    state["messages"][-1] = final
    state["messages"].append(ToolMessage("Successfully presented files", id="t9", name="present_files", tool_call_id=call["id"]))
    [msg] = gate.before_model(state, RUNTIME)["messages"]
    assert "did not call present_files" in msg.content and "Citation check passed" in msg.content
    assert [r["event"] for r in store.read_log(THREAD)] == ["auto_presented", "accepted"]


def test_gate_presents_at_most_once_and_not_after_a_decision(setup):
    store, outputs = setup
    gate = CitationGateMiddleware(store)
    assert gate.after_model(finishing(outputs), RUNTIME) is not None
    assert gate.after_model(finishing(outputs), RUNTIME) is None
    store.save_search(THREAD, {**store.load_search(THREAD), "search_id": "s2"})
    store.log(THREAD, {"event": "accepted", "search_id": "s2"})
    assert gate.after_model(finishing(outputs), RUNTIME) is None


def test_nothing_to_present_is_left_alone(setup):
    store, outputs = setup
    gate = CitationGateMiddleware(store)
    assert gate.after_model(finishing(outputs, report=None), RUNTIME) is None
    assert gate.after_model(finishing(outputs, report="# Notes without citations\n"), RUNTIME) is None
    store.save_search(THREAD, {**store.load_search(THREAD), "searched_at": 4102444800})  # files older than the search
    assert gate.after_model(finishing(outputs), RUNTIME) is None
    state = finishing(outputs)
    state["messages"][-1] = AIMessage("", id="a9", tool_calls=[{"id": "c", "name": "write_file", "args": {}}])
    assert gate.after_model(state, RUNTIME) is None


async def test_async_after_model_matches_sync(setup):
    store, outputs = setup
    update = await CitationGateMiddleware(store).aafter_model(finishing(outputs), RUNTIME)
    assert update["messages"][0].tool_calls[0]["name"] == "present_files"


# Full text (P2.4): evidence ids in the report must have been issued by cite_evidence in this search.

TWO = "Agents fail on long tasks (Smith1, 2025) [E1], and planning helps (Smith2, 2025) [E2].\n\n## References\nSmith1, A. (2025). Benchmarking Agents Part 1. arXiv:2501.00001\nSmith2, A. (2025). Benchmarking Agents Part 2. arXiv:2501.00002\n"


@pytest.fixture
def evidence_setup(setup):
    store, outputs = setup
    store.save_search(THREAD, {**store.load_search(THREAD), "full_text": True, "retrieved_on": "2026-10-27"})
    store.add_evidence(
        THREAD,
        "s1",
        [
            {"paper": "2501.00001", "para": "S2.p3", "section": "2 Experiments", "quote": "Agents fail on | long tasks in every setting", "claim": "c", "source": "html"},
            {"paper": "2501.00002", "para": "abstract", "section": "Abstract", "quote": "planning helps most on long tasks", "claim": "c", "source": "abstract_only"},
        ],
    )
    return store, outputs


def test_report_with_checked_evidence_gets_the_appendix_written_by_code(evidence_setup):
    store, outputs = evidence_setup
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=TWO), RUNTIME)["messages"]
    assert "2 evidence ids checked" in msg.content
    text = (outputs / "slr-agents.md").read_text(encoding="utf-8")
    assert text.startswith(TWO.rstrip())
    assert "| E1 | arXiv:2501.00001 | [2 Experiments](https://arxiv.org/html/2501.00001#S2.p3) | “Agents fail on \\| long tasks in every setting” |" in text
    assert "or its abstract where no HTML exists" in text and "checked on 2026-10-27" in text
    assert store.read_log(THREAD)[0]["used"] == ["E1", "E2"]


def test_presenting_again_replaces_the_appendix_instead_of_stacking_it(evidence_setup):
    store, outputs = evidence_setup
    gate = CitationGateMiddleware(store)
    gate.before_model(state_after_present(outputs, report=TWO), RUNTIME)
    first = (outputs / "slr-agents.md").read_text(encoding="utf-8")
    gate.before_model(state_after_present(outputs, report=first, call_id="c2"), RUNTIME)
    assert (outputs / "slr-agents.md").read_text(encoding="utf-8") == first


@pytest.mark.parametrize(
    ("report", "expected"),
    [
        (TWO.replace("[E2]", "[E2, E7]"), "never issued by cite_evidence in this review: E7"),
        (TWO.replace("and planning helps (Smith2, 2025) [E2]", "and planning helps [E2]").replace("Smith2, A. (2025). Benchmarking Agents Part 2. arXiv:2501.00002\n", ""), "quote papers the report does not cite: E2 (2501.00002)"),
        (TWO.replace(" [E1]", "").replace(" [E2]", ""), "recorded 2 checked quotes, but the report uses none"),
    ],
)
def test_invented_misattached_or_missing_evidence_is_rejected(evidence_setup, report, expected):
    store, outputs = evidence_setup
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=report), RUNTIME)["messages"]
    assert "NOT verified" in msg.content and expected in msg.content
    assert "## Evidence" not in (outputs / "slr-agents.md").read_text(encoding="utf-8")


def test_evidence_from_an_earlier_search_does_not_count(evidence_setup):
    store, outputs = evidence_setup
    store.save_search(THREAD, {**store.load_search(THREAD), "search_id": "s2"})
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=TWO), RUNTIME)["messages"]
    assert "never issued by cite_evidence in this review: E1, E2" in msg.content


def test_searches_without_full_text_ignore_evidence_markers(setup):
    store, outputs = setup
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=GOOD.replace("Part 1.", "Part 1 [E9].")), RUNTIME)["messages"]
    assert "Citation check passed" in msg.content and "evidence" not in msg.content


def test_markers_next_to_theme_names_are_rejected(evidence_setup):
    # The smoke-run pattern: every id in one summary sentence that cites no paper.
    report = "Approaches cluster into hybrid methods [E1] and planning [E2].\n\n" + TWO
    [msg] = CitationGateMiddleware(store := evidence_setup[0]).before_model(state_after_present(evidence_setup[1], report=report), RUNTIME)["messages"]
    assert "do not cite their paper: E1 (belongs to Benchmarking Agents Part 1 (Smith1, 2025)), E2 (belongs to Benchmarking Agents Part 2 (Smith2, 2025))" in msg.content
    assert store.read_log(THREAD)[0]["misattached_evidence"] == ["E1 (belongs to Benchmarking Agents Part 1 (Smith1, 2025))", "E2 (belongs to Benchmarking Agents Part 2 (Smith2, 2025))"]
    # Removing these markers would leave the ungrounded sentence in place. Validation must not do that.
    assert (evidence_setup[1] / "slr-agents.md").read_text(encoding="utf-8") == report


def test_full_text_review_with_no_recorded_evidence_is_rejected(setup):
    store, outputs = setup
    store.save_search(THREAD, {**store.load_search(THREAD), "full_text": True})
    report = TWO.replace(" [E1]", "").replace(" [E2]", "")
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=report), RUNTIME)["messages"]
    assert "NOT verified" in msg.content and "No checked quotes were recorded" in msg.content
    decision = store.read_log(THREAD)[0]
    assert decision["event"] == "rejected" and decision["no_evidence"]
    assert decision["evidence_schema_version"] == 1
    assert decision["papers_without_evidence"] == ["2501.00001", "2501.00002"]
    assert (outputs / "slr-agents.md").read_text(encoding="utf-8") == report


def test_partial_evidence_does_not_verify_the_whole_review(evidence_setup):
    store, outputs = evidence_setup
    # Start a new search with evidence for only one of its two cited papers.
    store.save_search(THREAD, {**store.load_search(THREAD), "search_id": "s2"})
    [entry] = store.add_evidence(THREAD, "s2", [{"paper": "2501.00001", "quote": "Agents fail on long tasks", "para": "S1.p1"}])
    report = TWO.replace("E1", entry["e"]).replace(" [E2]", "")
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=report), RUNTIME)["messages"]
    assert "NOT verified" in msg.content and "no evidence marker in the report: 2501.00002" in msg.content
    decision = store.read_log(THREAD)[0]
    assert decision["used"] == [entry["e"]] and not decision["no_evidence"]
    assert decision["papers_without_evidence"] == ["2501.00002"]


def test_rejected_evidence_can_be_corrected_and_presented_again(evidence_setup):
    store, outputs = evidence_setup
    gate = CitationGateMiddleware(store)
    bad = "An ungrounded summary [E1].\n\n" + TWO
    gate.before_model(state_after_present(outputs, report=bad), RUNTIME)
    [msg] = gate.before_model(state_after_present(outputs, report=TWO, call_id="fixed"), RUNTIME)["messages"]
    assert "2 evidence ids checked" in msg.content and "not semantic support" in msg.content
    log = store.read_log(THREAD)
    assert [row["event"] for row in log] == ["rejected", "accepted"]
    assert log[0]["sha256"] != log[1]["sha256"]
    assert log[1]["evidence_schema_version"] == 1 and not log[1]["misattached_evidence"]


def test_markers_under_a_per_paper_heading_or_lead_sentence_are_attached(evidence_setup):
    store, outputs = evidence_setup
    report = TWO.replace("## References", "### Smith1 et al. (2025)\n\n- Agents fail on long tasks [E1].\n\n**Smith2 et al. (2025)** study planning. Planning helps most [E2].\n\n## References")
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=report), RUNTIME)["messages"]
    assert "Citation check passed" in msg.content


def test_checked_quotes_left_unused_for_a_cited_paper_are_rejected(evidence_setup):
    store, outputs = evidence_setup
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=TWO.replace(" [E2]", "")), RUNTIME)["messages"]
    assert "checked quotes that the report never uses: Benchmarking Agents Part 2 (Smith2, 2025) [E2]" in msg.content


def test_a_sentence_continuing_about_the_previous_citation_is_attached(evidence_setup):
    store, outputs = evidence_setup
    report = TWO.replace("and planning helps (Smith2, 2025) [E2].", "and planning helps (Smith2, 2025). Its planner works best on long tasks [E2].")
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=report), RUNTIME)["messages"]
    assert "Citation check passed" in msg.content


def test_read_paper_by_the_lead_agent_is_replaced_by_an_instruction_to_delegate(setup):
    store, _ = setup
    state = {
        "messages": [
            HumanMessage("review", id="h1"),
            AIMessage("", id="a1", tool_calls=[{"id": "r1", "name": "ext_community_scholar_read_paper_88058358e6ca", "args": {"paper": "2501.00001", "section": "S2"}}]),
            ToolMessage("2501.00001 (arXiv HTML), section S2 ...", id="t1", name="ext_community_scholar_read_paper_88058358e6ca", tool_call_id="r1"),
        ]
    }
    [msg] = CitationGateMiddleware(store).before_model(state, RUNTIME)["messages"]
    assert msg.id == "t1" and "Dispatch one `task` subagent per batch" in msg.content
    assert store.read_log(THREAD)[0]["event"] == "lead_read_blocked"


def test_findings_in_a_per_paper_block_opened_by_its_citation_are_attached(evidence_setup):
    store, outputs = evidence_setup
    block = "### 2. Planning agents\n\n**Citation:** Smith2, A. (2025). Benchmarking Agents Part 2. arXiv:2501.00002\n\n**Key findings:**\n- Planning helps most on long tasks [E2]\n\n"
    report = TWO.replace(" [E2]", "").replace("## References", block + "## References")
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=report), RUNTIME)["messages"]
    assert "Citation check passed" in msg.content


def test_stopping_after_a_rejection_presents_the_file_again_until_released(setup):
    store, outputs = setup
    gate = CitationGateMiddleware(store, max_blocks=1)
    gate.before_model(state_after_present(outputs, report=BAD), RUNTIME)
    ending = {"messages": [HumanMessage("review", id="h1"), AIMessage("Let me fix this by rewriting the sentences.", id="a9")], "thread_data": {"outputs_path": str(outputs)}}
    [msg] = gate.after_model(ending, RUNTIME)["messages"]
    assert msg.id == "a9" and msg.tool_calls[0]["args"] == {"filepaths": ["/mnt/user-data/outputs/slr-agents.md"]}
    call_id = msg.tool_calls[0]["id"]
    presented = {
        "messages": [*ending["messages"][:1], msg, ToolMessage("Successfully presented files", id="t9", name="present_files", tool_call_id=call_id)],
        "thread_data": {"outputs_path": str(outputs)},
    }
    [result] = gate.before_model(presented, RUNTIME)["messages"]
    assert "stopped while this report was still rejected" in result.content and "MUST tell the user" in result.content
    # Released: the next ending is left alone.
    assert gate.after_model(ending, RUNTIME) is None
    assert [r["event"] for r in store.read_log(THREAD)] == ["rejected", "re_presented", "released_unverified"]


def test_misspelt_surname_is_named_in_the_rejection(evidence_setup):
    # Smoke c09: "Benigmimim" for Benigmim was rejected three times; the model never saw the typo.
    store, outputs = evidence_setup
    [msg] = CitationGateMiddleware(store).before_model(state_after_present(outputs, report=TWO.replace("(Smith1, 2025) [E1]", "(Smiith1, 2025) [E1]")), RUNTIME)["messages"]
    assert 'E1 (belongs to Benchmarking Agents Part 1 (Smith1, 2025); the report writes "Smiith1", the first author is "Smith1")' in msg.content
    assert "read_file the report once, then write_file the whole corrected report" in msg.content


def test_another_cited_surname_is_not_called_a_typo(evidence_setup):
    report = TWO.replace("(Smith1, 2025) [E1]", "(Smith2, 2025) [E1]")
    [msg] = CitationGateMiddleware(evidence_setup[0]).before_model(state_after_present(evidence_setup[1], report=report), RUNTIME)["messages"]
    assert "E1 (belongs to Benchmarking Agents Part 1 (Smith1, 2025))" in msg.content and "report writes" not in msg.content
