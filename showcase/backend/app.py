"""Read-only API over runs/ for the showcase site. Run: uvicorn app:app --port 8787"""

from __future__ import annotations

from pathlib import Path

import data
import tasks
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles

manager = tasks.Manager()
# A custom header forces a CORS preflight, so another web page cannot make the browser start a paid run here.
LIVE_HEADER = "live"

app = FastAPI(
    title="deerflow-citeguard showcase",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)


def _found(fn, *args):
    try:
        return fn(*args)
    except data.NotFound:
        raise HTTPException(404, "not found") from None


@app.get("/api/overview")
def overview() -> dict:
    return data.overview()


@app.get("/api/suites")
def suites() -> list[dict]:
    return data.suites()


@app.get("/api/suites/{name}")
def suite(name: str) -> dict:
    return _found(data.suite, name)


@app.get("/api/suites/{name}/runs/{run_id}")
def run(name: str, run_id: str) -> dict:
    return _found(data.run, name, run_id)


def _live(fn, *args):
    try:
        return fn(*args)
    except tasks.TaskError as e:
        raise HTTPException(e.status, str(e)) from None


def _require_header(value: str | None) -> None:
    if value != LIVE_HEADER:
        raise HTTPException(403, "缺少请求头 X-CiteGuard")


@app.get("/api/live/health")
def live_health() -> dict:
    return {**tasks.health(), "busy": manager.active() is not None}


@app.get("/api/live/tasks")
def live_tasks() -> list[dict]:
    return manager.list()


@app.post("/api/live/tasks", status_code=201)
def live_start(body: dict, x_citeguard: str | None = Header(default=None)) -> dict:
    _require_header(x_citeguard)
    if not tasks.health()["ok"]:
        raise HTTPException(503, "DeerFlow 未就绪，请先检查连接状态")
    task = _live(manager.start, body)
    return tasks.snapshot(task)


@app.get("/api/live/tasks/{task_id}")
def live_task(task_id: str) -> dict:
    return tasks.snapshot(_live(manager.get, task_id))


@app.post("/api/live/tasks/{task_id}/cancel")
def live_cancel(task_id: str, x_citeguard: str | None = Header(default=None)) -> dict:
    _require_header(x_citeguard)
    return tasks.snapshot(_live(manager.cancel, task_id))


def _download(text: str, media: str, filename: str) -> Response:
    return Response(
        text,
        media_type=media,
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@app.get("/api/suites/{name}/runs/{run_id}/references.bib")
def references_bib(name: str, run_id: str) -> Response:
    text = _found(data.bibtex, name, run_id)
    return _download(
        text, "application/x-bibtex; charset=utf-8", f"{name}-{run_id}.bib"
    )


@app.get("/api/suites/{name}/runs/{run_id}/evidence.csv")
def evidence_csv(name: str, run_id: str) -> Response:
    text = _found(data.evidence_csv, name, run_id)
    return _download(text, "text/csv; charset=utf-8", f"{name}-{run_id}-evidence.csv")


# Serve the built frontend when it exists, so one process is enough for a demo.
DIST = Path(__file__).resolve().parent.parent / "frontend" / "dist"
if DIST.exists():
    app.mount("/assets", StaticFiles(directory=DIST / "assets"), name="assets")

    @app.get("/{path:path}", include_in_schema=False)
    def spa(path: str) -> FileResponse:
        # Top-level files of the build (favicon) are served as is; every other path is a client route.
        if path.startswith("api/"):
            raise HTTPException(404, "not found")
        file = DIST / path
        if path and "/" not in path and file.is_file():
            return FileResponse(file)
        return FileResponse(DIST / "index.html")
