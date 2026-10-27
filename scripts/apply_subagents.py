"""Merge the tracked subagent definition into DeerFlow's config.yaml, after checking it against the host.

    python3 -I scripts/apply_subagents.py            # check, then write the block (replacing a previous one)
    python3 -I scripts/apply_subagents.py --check    # check only
    python3 -I scripts/apply_subagents.py --remove   # take the block out again

The source is extensions/scholar/deploy/subagents.yaml (in git); config.yaml is not. The block is written
between BEGIN/END markers that carry the source's sha256, which eval/run_task.py copies into meta.json.
Restart the gateway afterwards (scripts/deploy_retrieval.sh does).

Checks run inside the gateway container, with DeerFlow's own code:
  1. the block validates as DeerFlow's SubagentsAppConfig;
  2. every whitelisted scholar tool name equals the host's plugin_tool_name("community.scholar", <tool>);
  3. the installed scholar plugin really provides those tools (with full_text on).
A whitelist that matches no tool would leave the subagent with no scholar tools at all, silently.
"""

from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "extensions" / "scholar" / "deploy" / "subagents.yaml"
CONFIG = ROOT / "deer-flow" / "config.yaml"
BEGIN = "# BEGIN citeguard subagents"
END = "# END citeguard subagents"

CHECK = r"""
import sys, yaml
from deerflow.config.subagents_config import SubagentsAppConfig
from deerflow.extensions.plugin_tools import plugin_tool_name
from deerflow_extension_scholar import build_tools, PaperStore
block = yaml.safe_load(sys.stdin.read())["subagents"]
SubagentsAppConfig(**block)
provided = {t.name for t in build_tools(PaperStore("/tmp/scholar-check"), full_text=True)}
problems = []
for name, agent in block["custom_agents"].items():
    for tool in agent.get("tools") or []:
        if not tool.startswith("ext_community_scholar_"):
            continue
        base = next((p for p in provided if plugin_tool_name("community.scholar", p) == tool), None)
        if base is None:
            problems.append(f"{name}: {tool} is not a tool of the installed scholar plugin")
print("\n".join(problems) if problems else "ok")
sys.exit(1 if problems else 0)
"""


def strip_block(text: str) -> str:
    if BEGIN not in text:
        return text
    start = text.index(BEGIN)
    end = text.index(END, start) + len(END)
    return (text[:start].rstrip("\n") + "\n" + text[end:].lstrip("\n")).rstrip("\n") + "\n"


def check(source: str) -> None:
    result = subprocess.run(
        ["docker", "exec", "-i", "-w", "/app/backend", "deer-flow-gateway", "uv", "run", "--no-sync", "python", "-c", CHECK],
        input=source,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        sys.exit(f"check failed:\n{result.stdout}{result.stderr[-2000:]}")
    print("check: block validates; whitelisted scholar tools exist in the installed plugin")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--remove", action="store_true")
    args = ap.parse_args()
    text = CONFIG.read_text(encoding="utf-8")
    if args.remove:
        CONFIG.write_text(strip_block(text), encoding="utf-8")
        print("removed the citeguard subagents block; restart the gateway")
        return
    source = SOURCE.read_text(encoding="utf-8")
    body = strip_block(text)
    if any(line.startswith("subagents:") for line in body.splitlines()):
        sys.exit("config.yaml already has its own top-level subagents: block; merge by hand")
    check(source)
    if args.check:
        return
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()
    CONFIG.write_text(f"{body.rstrip(chr(10))}\n\n{BEGIN} sha256={digest} (from {SOURCE.relative_to(ROOT)})\n{source.rstrip(chr(10))}\n{END}\n", encoding="utf-8")
    print(f"wrote the subagents block (sha256={digest[:12]}); restart the gateway")


if __name__ == "__main__":
    main()
