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
