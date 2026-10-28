"""Live runs against a fake DeerFlow gateway: no model is called and nothing touches the network."""

from __future__ import annotations

import json
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import app as app_module
import data
import run_suite
import run_task
import tasks

THREAD, RUN = "thread-1", "run-1"
SEARCH = "ext_community_scholar_search_1607103162c3"
SCREEN = "ext_community_scholar_screen_28ee5994a449"
INDEX = "ext_community_scholar_evidence_index_84c9fd959d4b"
REPORT = (
    "# Review\n\n## References\n\nWei, Z. (2023). Stronger, fewer. arXiv:2312.04265\n"
)
HEADERS = {"X-CiteGuard": "live"}
BODY = {
    "topic": "domain generalization",
    "category": "cs.CV",
    "start": "2023-10-03",
    "end": "2025-10-02",
    "count": 10,
}


def ai(mid: str, calls: list[tuple[str, dict]] | None = None, text: str = "") -> dict:
    return {
        "type": "ai",
        "id": mid,
        "content": text,
        "tool_calls": [
            {"name": n, "args": a, "id": f"{mid}-{i}"}
            for i, (n, a) in enumerate(calls or [])
        ],
        "usage_metadata": {
            "input_tokens": 100,
            "output_tokens": 10,
            "total_tokens": 110,
        },
    }


def tool(mid: str, name: str, content: str) -> dict:
    return {"type": "tool", "id": mid, "name": name, "content": content}


class Fake:
    """Replays the shape of a real v5 run; writes the plugin's files when the real plugin would."""

    def __init__(self, plugin: Path, block: bool = False):
        self.plugin = plugin / THREAD
        self.block = block
        self.release = threading.Event()
        self.cancelled = threading.Event()

    def steps(self):
        p = self.plugin
        msgs = [{"type": "human", "id": "h", "content": "review"}]
        yield msgs + [ai("a1", [("read_file", {"path": "/mnt/skills/x/SKILL.md"})])]
        msgs += [
            ai("a1", [("read_file", {"path": "/mnt/skills/x/SKILL.md"})]),
            tool("t1", "read_file", "skill"),
        ]
        yield msgs
        if self.block:
            self.release.wait(10)
            return
        p.mkdir(parents=True, exist_ok=True)
        papers = [
            {
                "id": "2312.04265",
                "title": "Stronger, Fewer",
                "authors": ["Zhixiang Wei"],
                "published": "2023-12-07",
            }
        ]
        (p / "search.json").write_text(
            json.dumps({"papers": papers, "pool_ids": ["2312.04265"] * 50})
        )
        msgs += [
            ai("a2", [(SEARCH, {"query": "domain generalization"})]),
            tool("t2", SEARCH, "{}"),
        ]
        yield msgs
        counts = {
            "identified_by_search": 50,
            "added_from_references": 110,
            "shortlisted": 30,
            "included": 1,
        }
        (p / "search.json").write_text(
            json.dumps(
                {
                    "papers": papers,
                    "batches": [["2312.04265"]],
                    "screening": {"counts": counts},
                }
            )
        )
        msgs += [ai("a3", [(SCREEN, {})]), tool("t3", SCREEN, "{}")]
        yield msgs
        msgs += [ai("a4", [("task", {"prompt": "read"})])]
        yield msgs
        (p / "evidence.jsonl").write_text(
            json.dumps(
                {
                    "e": "E1",
                    "paper": "2312.04265",
                    "section": "5",
                    "para": "S5.p1",
                    "quote": "q",
                }
            )
            + "\n"
        )
        msgs += [tool("t4", "task", "Task Succeeded. Result: ok")]
        yield msgs
        msgs += [ai("a5", [(INDEX, {})]), tool("t5", INDEX, "{}")]
        msgs += [
            ai("a6", [("write_file", {"path": "/mnt/user-data/outputs/r.md"})]),
            tool("t6", "write_file", "OK"),
        ]
        msgs += [
            ai(
                "a7",
                [("present_files", {"filepaths": ["/mnt/user-data/outputs/r.md"]})],
            )
        ]
        yield msgs
        msgs += [tool("t7", "present_files", "Successfully presented files")]
        (p / "gate.jsonl").write_text(
            json.dumps({"event": "accepted", "cited": 1, "retrieved": 1}) + "\n"
        )
        yield msgs
        msgs += [ai("a8", text="Done")]
        yield msgs

    def handler(fake):
        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def _json(self, obj, code=200):
                body = json.dumps(obj).encode()
                self.send_response(code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self):
                if self.path == "/api/models":
                    self._json({"models": [{"name": tasks.MODEL}]})
                elif self.path == f"/api/threads/{THREAD}/runs":
                    self._json([{"total_tokens": 1234}])
                elif self.path.startswith(f"/api/threads/{THREAD}/artifacts"):
                    body = REPORT.encode()
                    self.send_response(200)
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                else:
                    self._json({}, 404)

            def do_POST(self):
                self.rfile.read(int(self.headers.get("Content-Length") or 0))
                if self.path == "/api/langgraph/threads":
                    self._json({"thread_id": THREAD})
                elif self.path.startswith(f"/api/threads/{THREAD}/runs/{RUN}/cancel"):
                    fake.cancelled.set()
                    fake.release.set()
                    self._json({}, 202)
                elif self.path == f"/api/langgraph/threads/{THREAD}/runs/stream":
                    self.send_response(200)
                    self.send_header("Content-Type", "text/event-stream")
                    self.send_header(
                        "Content-Location", f"/api/threads/{THREAD}/runs/{RUN}"
                    )
                    self.end_headers()
                    for msgs in fake.steps():
                        values = {
                            "messages": msgs,
                            "artifacts": ["/mnt/user-data/outputs/r.md"],
                        }
                        self.wfile.write(
                            f"event: values\ndata: {json.dumps(values)}\n\n".encode()
                        )
                        self.wfile.flush()
                        time.sleep(0.02)
                    self.wfile.write(b"event: end\ndata: null\n\n")
                else:
                    self._json({}, 404)

        return Handler


@pytest.fixture
def live(tmp_path, monkeypatch):
    def setup(block: bool = False):
        runs = tmp_path / "runs"
        plugin = tmp_path / "plugin"
        plugin.mkdir()
        fake = Fake(plugin, block)
        server = ThreadingHTTPServer(("127.0.0.1", 0), fake.handler())
        threading.Thread(target=server.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{server.server_port}"
        cookie = tmp_path / "cookies.txt"
        cookie.write_text("")
        monkeypatch.setattr(run_task, "BASE", base)
        monkeypatch.setattr(run_suite, "BASE", base)
        monkeypatch.setattr(run_task, "COOKIES", cookie)
        monkeypatch.setattr(run_task, "load_cookies", dict)
        monkeypatch.setattr(run_suite, "cookies", dict)
        monkeypatch.setattr(run_suite, "GATE_LOGS", plugin)
        monkeypatch.setattr(tasks, "LIVE", runs / "suite-live")
        monkeypatch.setattr(data, "RUNS", runs)

        def fake_check(self, task):  # the real check calls arXiv
            metrics = {"verified": {"ok": 1, "of": 1}, "references": 1}
            rows = [{"id": "2312.04265", "verified": True}]
            (task.dir / "citations.json").write_text(
                json.dumps({"metrics": metrics, "rows": rows})
            )

        monkeypatch.setattr(tasks.Manager, "_check", fake_check)
        manager = tasks.Manager()
        monkeypatch.setattr(app_module, "manager", manager)
        fixtures.append((server, fake))
        return TestClient(app_module.app), fake, manager

    fixtures: list = []
    yield setup
    for server, fake in fixtures:
        fake.release.set()
        server.shutdown()


def wait(client, task_id, statuses, timeout=10.0):
    end = time.time() + timeout
    while time.time() < end:
        snap = client.get(f"/api/live/tasks/{task_id}").json()
        if snap["status"] in statuses:
            return snap
        time.sleep(0.05)
    raise AssertionError(f"task stuck in {snap['status']}")


def test_full_run_is_archived_like_an_eval_run(live):
    client, _, manager = live()
    assert client.get("/api/live/health").json()["ok"]
    res = client.post("/api/live/tasks", json=BODY, headers=HEADERS)
    assert res.status_code == 201
    snap = wait(client, res.json()["id"], {"done", "failed"})
    assert snap["status"] == "done", snap["error"]
    stages = {s["key"]: s["status"] for s in snap["stages"]}
    assert stages == {k: "done" for k in tasks.ORDER}
    feed = " ".join(f["text"] for f in snap["feed"])
    assert (
        "入选 1" in feed
        and "子 Agent 完成（1/1）" in feed
        and "关卡通过" in feed
        and "1/1" in feed
    )
    assert snap["funnel"] == {
        "searched": 50,
        "expanded": 110,
        "shortlisted": 30,
        "included": 1,
    }
    assert snap["papers"][0]["evidence"] == 1 and snap["evidence_total"] == 1
    assert snap["citations"]["verified"] == {"ok": 1, "of": 1}

    task_dir = tasks.LIVE / snap["id"]
    for name in (
        "meta.json",
        "report.md",
        "search.json",
        "evidence.jsonl",
        "gate.jsonl",
        "citations.json",
    ):
        assert (task_dir / name).exists(), name
    meta = json.loads((task_dir / "meta.json").read_text())
    assert (
        meta["usage_run_record"]["total_tokens"] == 1234
        and meta["source"] == "showcase-live"
    )

    # The archived run is a normal suite run: listed, and its detail page works.
    suite = client.get("/api/suites/live").json()
    assert suite["kind"] == "live" and suite["rows"][0]["run"] == snap["id"]
    detail = client.get(f"/api/suites/live/runs/{snap['id']}").json()
    assert detail["report"] == REPORT and detail["gate"][0]["event"] == "accepted"
    assert manager.list()[0]["verified"] == {"ok": 1, "of": 1}


def test_start_needs_header_and_valid_input(live):
    client, _, _ = live()
    assert client.post("/api/live/tasks", json=BODY).status_code == 403
    bad = [
        {**BODY, "topic": "x"},
        {**BODY, "category": "cs.XX"},
        {**BODY, "start": "2025-01-01", "end": "2024-01-01"},
        {**BODY, "end": "2999-01-01"},
        {**BODY, "count": 40},
    ]
    for body in bad:
        assert (
            client.post("/api/live/tasks", json=body, headers=HEADERS).status_code
            == 400
        ), body


def test_one_task_at_a_time_and_cancel(live):
    client, fake, _ = live(block=True)
    first = client.post("/api/live/tasks", json=BODY, headers=HEADERS).json()
    wait(client, first["id"], {"running"})
    assert client.post("/api/live/tasks", json=BODY, headers=HEADERS).status_code == 409
    assert client.post(f"/api/live/tasks/{first['id']}/cancel").status_code == 403
    assert (
        client.post(
            f"/api/live/tasks/{first['id']}/cancel", headers=HEADERS
        ).status_code
        == 200
    )
    snap = wait(client, first["id"], {"cancelled", "failed", "done"})
    assert snap["status"] == "cancelled" and fake.cancelled.is_set()
    assert not (tasks.LIVE / first["id"] / "citations.json").exists()


def test_restart_marks_running_task_interrupted(live):
    client, _, _ = live(block=True)
    first = client.post("/api/live/tasks", json=BODY, headers=HEADERS).json()
    wait(client, first["id"], {"running"})
    reloaded = tasks.Manager().get(first["id"])
    assert reloaded.status == "interrupted"


def test_unknown_task_is_404(live):
    client, _, _ = live()
    assert client.get("/api/live/tasks/nope").status_code == 404
