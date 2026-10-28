"""Live literature reviews: start a run on the local DeerFlow gateway, follow it, archive it like an eval run.

The backend, not the browser, holds DeerFlow's event stream: the gateway cancels a run when its stream
disconnects, so a page reload must not end the task. The browser polls `snapshot()`.

A finished task is written to runs/suite-live/<id>/ with the same files as an eval run (meta.json,
report.md, gate.jsonl, search.json, evidence.jsonl, citations.json), so the run pages work unchanged.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import threading
import time
import urllib.error
import uuid
from datetime import date, datetime
from pathlib import Path

from data import ROOT, RUNS

sys.path.insert(0, str(ROOT / "eval"))
import run_suite
import run_task

LIVE = RUNS / "suite-live"
MODEL = "qwen3.5-plus"
# The coverage eval's prompt, so a live run behaves like the measured ones.
PROMPT = (
    "Do a systematic literature review on {topic}. {count} papers, "
    "published between {start} and {end}, category {category}, APA format. "
    "Save to default output location."
)
CATEGORIES = {
    "cs.CL": "计算语言学",
    "cs.CV": "计算机视觉",
    "cs.LG": "机器学习",
    "cs.AI": "人工智能",
    "cs.SE": "软件工程",
    "cs.CR": "密码与安全",
    "cs.RO": "机器人",
    "cs.IR": "信息检索",
    "stat.ML": "统计机器学习",
}
STAGES = [
    ("method", "读取方法"),
    ("search", "检索"),
    ("screen", "筛选"),
    ("read", "阅读全文"),
    ("index", "汇总证据"),
    ("write", "撰写报告"),
    ("gate", "关卡核查"),
    ("check", "引用核查"),
]
ORDER = [s for s, _ in STAGES]
ACTIVE = ("starting", "running", "archiving", "checking")
DECISIONS = ("accepted", "rejected", "released_unverified")


class TaskError(Exception):
    def __init__(self, status: int, message: str):
        super().__init__(message)
        self.status = status


def _stage_of(tool: str, args: dict) -> str | None:
    """Which pipeline stage a tool call belongs to; plugin tools carry a hashed suffix."""
    m = re.search(r"scholar_([a-z_]+?)(?:_[0-9a-f]{8,})?$", tool)
    name = m.group(1) if m else tool
    if name in ("search",):
        return "search"
    if name in ("screen",):
        return "screen"
    if name in ("task", "get_batch", "read_paper", "cite_evidence"):
        return "read"
    if name == "evidence_index":
        return "index"
    if name in ("write_file", "str_replace"):
        return "write"
    if name == "present_files":
        return "gate"
    if name == "read_file" and "SKILL.md" in str(args.get("path", "")):
        return "method"
    return None


def validate(body: dict) -> dict:
    topic = " ".join(str(body.get("topic", "")).split())
    if not 3 <= len(topic) <= 120:
        raise TaskError(400, "主题长度需在 3–120 个字符之间")
    category = body.get("category")
    if category not in CATEGORIES:
        raise TaskError(400, "不支持的 arXiv 类别")
    try:
        start = date.fromisoformat(str(body.get("start")))
        end = date.fromisoformat(str(body.get("end")))
    except ValueError:
        raise TaskError(400, "日期格式应为 YYYY-MM-DD") from None
    if not start < end <= date.today():
        raise TaskError(400, "时间范围无效：开始须早于结束，结束不晚于今天")
    try:
        count = int(body.get("count", 10))
    except (TypeError, ValueError):
        raise TaskError(400, "论文篇数无效") from None
    if not 5 <= count <= 15:
        raise TaskError(400, "论文篇数需在 5–15 之间")
    return {
        "topic": topic,
        "category": category,
        "start": start.isoformat(),
        "end": end.isoformat(),
        "count": count,
    }


class Task:
    def __init__(self, task_id: str, params: dict):
        self.id = task_id
        self.params = params
        self.prompt = PROMPT.format(**params)
        self.status = "starting"
        self.error: str | None = None
        self.created = time.time()
        self.started: float | None = None
        self.finished: float | None = None
        self.thread_id: str | None = None
        self.run_id: str | None = None
        self.marks: list[
            tuple[float, str]
        ] = []  # (seconds since start, stage) per tool call
        self.feed: list[dict] = []  # human-readable activity
        self.subagents = {"started": 0, "done": 0}
        self.decisions = 0  # gate decisions already reported in the feed
        self.tokens = 0
        self.cancel_requested = False
        self.lock = threading.Lock()

    @property
    def dir(self) -> Path:
        return LIVE / self.id

    def elapsed(self) -> float:
        if self.started is None:
            return 0.0
        return round((self.finished or time.time()) - self.started, 1)

    def mark(self, stage: str, text: str | None = None) -> None:
        with self.lock:
            t = self.elapsed()
            if not self.marks or self.marks[-1][1] != stage:
                self.marks.append((t, stage))
            if text:
                self.feed.append({"t": t, "stage": stage, "text": text})

    def note(
        self, text: str, stage: str | None = None, tone: str | None = None
    ) -> None:
        with self.lock:
            self.feed.append(
                {"t": self.elapsed(), "stage": stage, "text": text, "tone": tone}
            )

    def save(self) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        state = {
            k: getattr(self, k)
            for k in ("id", "params", "prompt", "status", "error", "created", "started")
        }
        state.update(
            finished=self.finished,
            thread_id=self.thread_id,
            run_id=self.run_id,
            marks=self.marks,
            feed=self.feed,
            subagents=self.subagents,
            decisions=self.decisions,
            tokens=self.tokens,
        )
        tmp = self.dir / "task.json.tmp"
        tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1))
        tmp.replace(self.dir / "task.json")

    @classmethod
    def load(cls, path: Path) -> Task:
        state = json.loads(path.read_text())
        task = cls(state["id"], state["params"])
        for k, v in state.items():
            if k == "marks":
                v = [tuple(m) for m in v]
            setattr(task, k, v)
        return task


def _send_cancel(task: Task) -> None:
    if not (task.thread_id and task.run_id):
        return
    try:
        path = (
            f"/api/threads/{task.thread_id}/runs/{task.run_id}/cancel?action=interrupt"
        )
        run_task.request("POST", path, {}, run_task.load_cookies()).close()
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        task.note(f"取消请求失败：{e}", tone="critical")


def _plugin_dir(thread_id: str | None) -> Path | None:
    return run_suite.GATE_LOGS / thread_id if thread_id else None


def _read_json(path: Path | None):
    try:
        return json.loads(path.read_text()) if path else None
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def _read_jsonl(path: Path | None) -> list[dict]:
    if not path or not path.exists():
        return []
    out = []
    for line in path.read_text().splitlines():
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def _stages(task: Task) -> list[dict]:
    """Done when a later stage was reached after its last appearance; active when it is the latest."""
    last_seen = {s: i for i, (_, s) in enumerate(task.marks)}
    current = task.marks[-1][1] if task.marks else None
    reached = max((ORDER.index(s) for _, s in task.marks), default=-1)
    out = []
    for key, label in STAGES:
        first = next((t for t, s in task.marks if s == key), None)
        if key == current and task.status in ACTIVE:
            status = "active"
        elif key in last_seen:
            status = (
                "done" if task.status in ACTIVE or task.status == "done" else "stopped"
            )
            if key == current and task.status in ("failed", "cancelled", "interrupted"):
                status = "failed"
        elif ORDER.index(key) < reached:
            status = "skipped"
        else:
            status = "pending"
        out.append({"key": key, "label": label, "status": status, "started": first})
    return out


def snapshot(task: Task) -> dict:
    """Task state plus what the plugin has written for the thread so far."""
    plugin = _plugin_dir(task.thread_id)
    search = (
        _read_json(plugin / "search.json" if plugin else None)
        or _read_json(task.dir / "search.json")
        or {}
    )
    evidence = _read_jsonl(
        plugin / "evidence.jsonl" if plugin else None
    ) or _read_jsonl(task.dir / "evidence.jsonl")
    gate = _read_jsonl(plugin / "gate.jsonl" if plugin else None) or _read_jsonl(
        task.dir / "gate.jsonl"
    )
    screening = search.get("screening") or {}
    counts = screening.get("counts") or {}
    per_paper: dict[str, int] = {}
    for e in evidence:
        per_paper[e.get("paper", "")] = per_paper.get(e.get("paper", ""), 0) + 1
    citations = _read_json(task.dir / "citations.json")
    with task.lock:
        return {
            "id": task.id,
            "params": task.params,
            "prompt": task.prompt,
            "model": MODEL,
            "status": task.status,
            "error": task.error,
            "created": task.created,
            "elapsed": task.elapsed(),
            "stages": _stages(task),
            "feed": task.feed[-60:],
            "subagents": task.subagents,
            "tokens": task.tokens,
            "funnel": {
                "searched": counts.get(
                    "identified_by_search", len(search.get("pool_ids") or []) or None
                ),
                "expanded": counts.get("added_from_references"),
                "shortlisted": counts.get("shortlisted"),
                "included": counts.get(
                    "included", len(search.get("papers") or []) or None
                ),
            },
            "papers": [
                {
                    "id": p.get("id"),
                    "title": p.get("title"),
                    "authors": (p.get("authors") or [])[:3],
                    "published": p.get("published"),
                    "evidence": per_paper.get(p.get("id"), 0),
                }
                for p in search.get("papers") or []
            ],
            "batches": search.get("batches") or [],
            "evidence": [
                {k: e.get(k) for k in ("e", "paper", "section", "para", "quote")}
                for e in evidence[-8:]
            ],
            "evidence_total": len(evidence),
            "gate": [
                {k: g.get(k) for k in ("event", "at", "cited", "retrieved")}
                for g in gate
                if g.get("event") in DECISIONS
            ],
            "citations": (citations or {}).get("metrics"),
            "has_report": (task.dir / "report.md").exists(),
        }


class Manager:
    """At most one live run at a time: each costs about a million tokens."""

    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.tasks: dict[str, Task] = {}
        self._load()

    def _load(self) -> None:
        for path in sorted(LIVE.glob("*/task.json")):
            try:
                task = Task.load(path)
            except (json.JSONDecodeError, KeyError, TypeError):
                continue
            if task.status in ACTIVE:
                # The process that held the stream is gone, and with it the run.
                task.status, task.error = "interrupted", "展示站点后端重启，任务中断"
                task.save()
            self.tasks[task.id] = task

    def active(self) -> Task | None:
        return next((t for t in self.tasks.values() if t.status in ACTIVE), None)

    def get(self, task_id: str) -> Task:
        task = self.tasks.get(task_id)
        if task is None:
            raise TaskError(404, "没有找到这个任务")
        return task

    def list(self) -> list[dict]:
        out = []
        for t in sorted(self.tasks.values(), key=lambda t: t.created, reverse=True):
            meta = _read_json(t.dir / "citations.json") or {}
            out.append(
                {
                    "id": t.id,
                    "topic": t.params["topic"],
                    "category": t.params["category"],
                    "status": t.status,
                    "created": t.created,
                    "elapsed": t.elapsed(),
                    "verified": (meta.get("metrics") or {}).get("verified"),
                }
            )
        return out

    def start(self, body: dict) -> Task:
        params = validate(body)
        with self.lock:
            if self.active():
                raise TaskError(409, "已有任务在运行，请等它结束或先取消")
            stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            task = Task(f"{stamp}-{uuid.uuid4().hex[:4]}", params)
            self.tasks[task.id] = task
            task.save()
        threading.Thread(
            target=self._run, args=(task,), daemon=True, name=f"live-{task.id}"
        ).start()
        return task

    def cancel(self, task_id: str) -> Task:
        task = self.get(task_id)
        if task.status not in ACTIVE:
            raise TaskError(409, "任务已经结束")
        task.cancel_requested = True
        task.note("已请求取消", tone="warning")
        _send_cancel(
            task
        )  # before the stream reports its run id, the worker sends it instead
        return task

    # --- worker -----------------------------------------------------------------------------------

    def _run(self, task: Task) -> None:
        try:
            self._stream(task)
            if task.cancel_requested:
                task.status = "cancelled"
            elif task.status == "running":
                task.status = "archiving"
            task.save()
            self._archive(task)
            if task.status == "archiving":
                task.status = "checking"
                task.mark("check", "对照 arXiv 官方 API 逐条核查引用")
                task.save()
                self._check(task)
                task.status = "done"
        except Exception as e:  # noqa: BLE001 - any failure must end the task visibly
            task.status = "failed"
            task.error = task.error or f"{type(e).__name__}: {e}"
            task.note(task.error, tone="critical")
        finally:
            task.finished = task.finished or time.time()
            task.save()

    def _stream(self, task: Task) -> None:
        cookies = run_task.load_cookies()
        with run_task.request(
            "POST",
            "/api/langgraph/threads",
            {"metadata": {"purpose": "showcase"}},
            cookies,
        ) as r:
            task.thread_id = json.load(r)["thread_id"]
        body = {
            "input": {
                "messages": [
                    {"role": "user", "content": task.prompt, "id": str(uuid.uuid4())}
                ]
            },
            "config": {
                "recursion_limit": 1000,
                "configurable": {
                    "model_name": MODEL,
                    "thinking_enabled": False,
                    "is_plan_mode": False,
                    "subagent_enabled": True,
                },
            },
            "stream_mode": ["values"],
        }
        task.started = time.time()
        task.status = "running"
        task.note("已连接 DeerFlow，任务开始")
        task.save()
        seen: dict[str, dict] = {}
        last_values: dict | None = None
        counts: dict[str, int] = {}
        path = f"/api/langgraph/threads/{task.thread_id}/runs/stream"
        try:
            with (
                run_task.request("POST", path, body, cookies, timeout=1800) as r,
                (task.dir / "events.jsonl").open("w") as ev,
            ):
                location = r.headers.get("Content-Location") or ""
                task.run_id = location.rstrip("/").rsplit("/", 1)[-1] or None
                if task.cancel_requested:
                    _send_cancel(task)
                event = None
                for raw in r:
                    line = raw.decode("utf-8", "replace").rstrip("\n")
                    if line.startswith("event:"):
                        event = line[6:].strip()
                        continue
                    if not line.startswith("data:"):
                        continue
                    counts[event or "?"] = counts.get(event or "?", 0) + 1
                    try:
                        data = json.loads(line[5:].strip())
                    except json.JSONDecodeError:
                        continue
                    ev.write(
                        json.dumps(
                            {"t": task.elapsed(), "event": event, "data": data},
                            ensure_ascii=False,
                        )
                        + "\n"
                    )
                    if event == "error":
                        task.error = f"DeerFlow 报错：{str(data)[:300]}"
                    if event == "values" and isinstance(data, dict):
                        last_values = data
                        self._observe(task, data, seen)
                        task.save()
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            if not task.cancel_requested:
                task.error = f"与 DeerFlow 的连接中断：{e}"
        task.finished = time.time()
        if last_values is not None:
            (task.dir / "final.json").write_text(
                json.dumps(last_values, ensure_ascii=False, indent=1)
            )
        messages = (last_values or {}).get("messages", [])
        meta = {
            "thread_id": task.thread_id,
            "model": MODEL,
            "prompt": task.prompt,
            "wall_seconds": task.elapsed(),
            "event_counts": counts,
            "message_count": len(messages),
            "usage_attributed_total": run_task.sum_usage(messages),
            "usage_events_total": run_task.usage_over_stream(seen),
            "usage_run_record": run_task.usage_from_run_record(task.thread_id, cookies),
            "artifacts": (last_values or {}).get("artifacts"),
            "subagents_config_sha256": run_task.subagents_config_digest(),
            "error": task.error,
            "source": "showcase-live",
        }
        record = meta["usage_run_record"] or {}
        task.tokens = (
            record.get("total_tokens") or meta["usage_events_total"]["total_tokens"]
        )
        (task.dir / "meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=1)
        )
        if task.error and not task.cancel_requested:
            task.status = "failed"

    def _observe(self, task: Task, values: dict, seen: dict[str, dict]) -> None:
        """Turn newly seen messages into stage marks and feed lines."""
        for m in values.get("messages", []):
            mid = m.get("id")
            if not mid or (mid in seen and m.get("type") != "ai"):
                continue
            first = mid not in seen
            if m.get("type") == "ai":
                seen[mid] = m
            else:
                seen[mid] = {}
            if not first:
                continue
            if m.get("type") == "ai":
                for call in m.get("tool_calls") or []:
                    self._on_call(task, call.get("name", ""), call.get("args") or {})
            elif m.get("type") == "tool":
                self._on_result(task, m.get("name", ""), str(m.get("content", "")))
        task.tokens = run_task.usage_over_stream({k: v for k, v in seen.items() if v})[
            "total_tokens"
        ]
        self._gate_decisions(task)

    def _gate_decisions(self, task: Task) -> None:
        """The gate decides before the next model call, so its log is read on every event, not on the tool result."""
        gate = _read_jsonl((_plugin_dir(task.thread_id) or Path()) / "gate.jsonl")
        decisions = [g for g in gate if g.get("event") in DECISIONS]
        for g in decisions[task.decisions :]:
            text, tone = {
                "accepted": ("关卡通过：编号均出自本次检索，证据标记有效", "good"),
                "rejected": ("关卡拒收，Agent 按原因修改后重新交付", "critical"),
                "released_unverified": (
                    "关卡多次拒收后放行，报告标为未核实",
                    "warning",
                ),
            }[g["event"]]
            task.note(text, stage="gate", tone=tone)
        task.decisions = len(decisions)

    def _on_call(self, task: Task, tool: str, args: dict) -> None:
        stage = _stage_of(tool, args)
        if stage is None:
            return
        p = task.params
        text = {
            "method": "读取综述方法（Skill）",
            "search": f"检索 arXiv：{args.get('query', p['topic'])}",
            "screen": "按主题相关度筛选候选论文",
            "index": "汇总已登记的证据，准备写作",
            "write": "撰写报告",
            "gate": "交付报告，关卡开始核查",
        }.get(stage)
        if tool == "task":
            task.subagents["started"] += 1
            text = f"派出子 Agent 阅读全文（第 {task.subagents['started']} 个）"
        elif stage == "read":
            text = None  # subagent tool calls are not in the lead's stream
        task.mark(stage, text)

    def _on_result(self, task: Task, tool: str, content: str) -> None:
        if tool == "task":
            task.subagents["done"] += 1
            ok = content.startswith("Task Succeeded")
            task.note(
                f"子 Agent 完成（{task.subagents['done']}/{task.subagents['started']}）"
                if ok
                else "子 Agent 未成功完成",
                stage="read",
                tone=None if ok else "warning",
            )
        elif _stage_of(tool, {}) in ("search", "screen"):
            search = (
                _read_json((_plugin_dir(task.thread_id) or Path()) / "search.json")
                or {}
            )
            counts = (search.get("screening") or {}).get("counts") or {}
            if _stage_of(tool, {}) == "search":
                n = len(search.get("pool_ids") or search.get("papers") or [])
                task.note(
                    f"检索返回 {n} 篇候选论文" if n else "检索完成", stage="search"
                )
            elif counts:
                task.note(
                    f"筛选：检索 {counts.get('identified_by_search', 0)} 篇 + 引用扩展 "
                    f"{counts.get('added_from_references', 0)} 篇 → 初选 {counts.get('shortlisted', 0)} → "
                    f"入选 {counts.get('included', 0)}",
                    stage="screen",
                )

    def _archive(self, task: Task) -> None:
        """Copy the plugin's per-thread files and the delivered report, as eval/run_suite.py does."""
        plugin = _plugin_dir(task.thread_id)
        for name in ("gate.jsonl", "search.json", "evidence.jsonl"):
            if plugin and (plugin / name).exists():
                shutil.copy(plugin / name, task.dir / name)
        meta = _read_json(task.dir / "meta.json") or {}
        try:
            got = (
                run_suite.download_report(meta, task.dir / "report.md")
                if meta.get("artifacts")
                else False
            )
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            got = False
            task.note(f"下载报告失败：{e}", tone="critical")
        if got:
            task.note("报告已保存", stage="write")
        elif task.status == "archiving":
            task.status = "failed"
            task.error = "运行结束，但没有交付报告"

    def _check(self, task: Task) -> None:
        p = task.params
        cmd = [
            sys.executable,
            "-I",
            str(ROOT / "eval" / "check_citations.py"),
            str(task.dir / "report.md"),
            "--since",
            p["start"],
            "--until",
            p["end"],
            "--category",
            p["category"],
            "--json",
            str(task.dir / "citations.json"),
        ]
        try:
            # A failed check leaves no citations.json; that is reported below, not raised.
            subprocess.run(
                cmd,
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=900,
            )
        except subprocess.TimeoutExpired:
            pass
        m = (_read_json(task.dir / "citations.json") or {}).get("metrics")
        if not m:
            task.note(
                "引用核查未完成（arXiv 接口不可用）", stage="check", tone="warning"
            )
            return
        v = m["verified"]
        tone = "good" if v["ok"] == v["of"] else "critical"
        task.note(
            f"引用核查：{v['ok']}/{v['of']} 条可在 arXiv 查到且标题一致",
            stage="check",
            tone=tone,
        )


def health() -> dict:
    """Can a live run start? Each check is cheap; none calls a model."""
    checks = []
    cookie_ok = run_task.COOKIES.exists()
    checks.append(
        {
            "key": "session",
            "label": "DeerFlow 登录会话",
            "ok": cookie_ok,
            "detail": None if cookie_ok else "缺少 .local/cookies.txt",
        }
    )
    gateway_ok, detail = False, None
    if cookie_ok:
        try:
            with run_task.request(
                "GET", "/api/models", None, run_task.load_cookies(), timeout=5
            ) as r:
                models = [m.get("name") for m in json.load(r).get("models", [])]
            gateway_ok = MODEL in models
            detail = None if gateway_ok else f"网关未配置 {MODEL}"
        except (
            urllib.error.URLError,
            TimeoutError,
            OSError,
            json.JSONDecodeError,
        ) as e:
            detail = f"无法连接 {run_task.BASE}（{type(e).__name__}）"
    checks.append(
        {"key": "gateway", "label": "DeerFlow 网关", "ok": gateway_ok, "detail": detail}
    )
    plugin_ok = run_suite.GATE_LOGS.exists()
    checks.append(
        {
            "key": "plugin",
            "label": "scholar 插件存储",
            "ok": plugin_ok,
            "detail": None if plugin_ok else "找不到插件的线程目录",
        }
    )
    return {
        "ok": all(c["ok"] for c in checks),
        "checks": checks,
        "model": MODEL,
        "categories": CATEGORIES,
    }
