from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from app import app

client = TestClient(app)


def test_overview_matches_readme():
    arms = {a["suite"]: a for a in client.get("/api/overview").json()["arms"]}
    base, v3 = arms["holdout3-base"], arms["holdout3-v3"]
    assert (base["clean_runs"], base["runs"]) == (1, 30)
    assert (v3["clean_runs"], v3["runs"]) == (29, 30)
    assert (base["delivered"], v3["delivered"]) == (28, 30)
    assert (base["mostly_fabricated"], v3["mostly_fabricated"]) == (9, 0)
    assert (base["mean_tokens"], v3["mean_tokens"]) == (264709, 222812)
    assert (round(base["mean_seconds"]), round(v3["mean_seconds"])) == (310, 191)
    assert (base["topics_clean_every_repeat"], v3["topics_clean_every_repeat"]) == (
        0,
        9,
    )
    assert v3["claims"]["supported_rate"] == 0.926
    assert base["claims"]["supported_rate"] == 0.606


def test_suites_list():
    names = {s["name"]: s for s in client.get("/api/suites").json()}
    assert names["holdout3-v3"]["kind"] == "holdout"
    assert names["smoke-v5-plus-06"]["kind"] == "smoke"
    assert names["v2-02-infra-failed"]["kind"] == "archive"


def test_run_detail_v3():
    r = client.get("/api/suites/holdout3-v3/runs/h01-r1").json()
    assert r["topic"] == "speculative decoding for LLM inference"
    assert r["citations"]["metrics"]["verified"] == {"ok": 10, "of": 10}
    assert r["gate"][-1]["event"] == "accepted"
    assert r["claims"]["judge"] == "v2"
    assert "# Systematic Literature Review" in r["report"]


def test_run_detail_v5_evidence():
    r = client.get("/api/suites/smoke-v5-plus-06/runs/c09-r1").json()
    assert len(r["evidence"]) == 30
    assert r["evidence"][0]["e"] == "E1"
    assert len(r["papers"]) >= 10


@pytest.mark.parametrize(
    "url",
    [
        "/api/suites/nope",
        "/api/suites/holdout3-v3/runs/nope",
        "/api/suites/..%2F..%2Fetc/runs/passwd",
        "/api/suites/holdout3-v3/runs/..%2Fsummary.json",
    ],
)
def test_unknown_names_are_404(url):
    assert client.get(url).status_code == 404


def test_frontend_routes_and_files():
    if not (Path(__file__).resolve().parents[2] / "frontend" / "dist").exists():
        pytest.skip("frontend not built")
    assert "<svg" in client.get("/favicon.svg").text
    assert '<div id="root">' in client.get("/experiments/holdout3-v3").text
    assert client.get("/api/nope").status_code == 404


def test_v5_run_has_citation_check():
    r = client.get("/api/suites/smoke-v5-plus-06/runs/c09-r1").json()
    assert r["citations"]["metrics"]["verified"] == {"ok": 10, "of": 10}


def test_bibtex_exports_only_verified():
    res = client.get("/api/suites/holdout3-base/runs/h01-r2/references.bib")
    assert res.status_code == 200
    assert 'filename="holdout3-base-h01-r2.bib"' in res.headers["content-disposition"]
    assert res.text.count("@misc{") == 1
    assert "Not exported, failed the arXiv check" in res.text
    # search.json supplies titles without the local arXiv cache; special characters are escaped
    v5 = client.get("/api/suites/smoke-v5-plus-06/runs/c09-r1/references.bib").text
    assert v5.count("@misc{") == 10
    assert r"Stronger, Fewer, \& Superior" in v5


def test_evidence_csv():
    res = client.get("/api/suites/smoke-v5-plus-06/runs/c09-r1/evidence.csv")
    assert res.status_code == 200
    rows = list(csv.reader(io.StringIO(res.text.lstrip("﻿"))))
    assert rows[0][:2] == ["evidence", "arxiv_id"]
    assert len(rows) == 31
    assert rows[1][7].startswith("https://arxiv.org/html/2312.04265#")


def test_exports_reject_unknown_runs():
    assert (
        client.get("/api/suites/holdout3-v3/runs/nope/references.bib").status_code
        == 404
    )
    assert client.get("/api/suites/nope/runs/c09-r1/evidence.csv").status_code == 404


def test_titles_only_for_verified_citations():
    r = client.get("/api/suites/holdout3-base/runs/h01-r2").json()
    verified = {c["id"] for c in r["citations"]["rows"] if c["verified"]}
    titled = {p["id"] for p in r["papers"] if p["title"]}
    assert titled == verified
