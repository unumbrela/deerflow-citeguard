"""Capture/verify a local source snapshot without credentials or runtime configuration.

Usage: python scripts/capture_snapshot.py create --out .local/releases/u0
       python scripts/capture_snapshot.py verify .local/releases/u0
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import shutil
import subprocess
import tempfile
import tomllib
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATTERNS = (
    "extensions/scholar/deerflow_extension_scholar/*.py",
    "extensions/scholar/tests/*.py",
    "extensions/scholar/pyproject.toml",
    "extensions/scholar/README.md",
    "extensions/scholar/deploy/subagents.yaml",
    "skills/systematic-literature-review/*.md",
    "skills/systematic-literature-review/templates/*.md",
    "scripts/*.py",
    "scripts/*.sh",
)
REQUIRED = (
    "extensions/scholar/deerflow_extension_scholar/core.py",
    "extensions/scholar/deerflow_extension_scholar/gate.py",
    "extensions/scholar/pyproject.toml",
    "skills/systematic-literature-review/SKILL.md",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_state(root: Path) -> dict:
    def git(*args: str) -> str | None:
        result = subprocess.run(
            ["git", "-C", str(root), *args], check=False, capture_output=True, text=True
        )
        return result.stdout.strip() if result.returncode == 0 else None

    # A missing upstream checkout must not report the outer repository's commit.
    top = git("rev-parse", "--show-toplevel") if root.is_dir() else None
    if top is None or Path(top).resolve() != root.resolve():
        return {"commit": None, "dirty": None}
    status = git("status", "--porcelain", "--untracked-files=normal")
    return {
        "commit": git("rev-parse", "HEAD"),
        "dirty": bool(status) if status is not None else None,
    }


def sources(root: Path) -> dict[str, bytes]:
    paths = sorted({p for pattern in PATTERNS for p in root.glob(pattern)})
    result = {}
    for path in paths:
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(
                f"source must be a regular file inside the project: {path}"
            )
        result[path.relative_to(root).as_posix()] = path.read_bytes()
    missing = set(REQUIRED) - result.keys()
    if missing:
        raise ValueError(f"missing required sources: {sorted(missing)}")
    return result


def file_hashes(files: dict[str, bytes]) -> dict[str, str]:
    return {name: sha256(data) for name, data in sorted(files.items())}


def tree_hash(hashes: dict[str, str]) -> str:
    return sha256(json.dumps(hashes, sort_keys=True, separators=(",", ":")).encode())


def create(root: Path, out: Path) -> dict:
    root, out = root.resolve(), out.absolute()
    if out.exists():
        raise ValueError(f"snapshot already exists: {out}")
    for name in ("extensions", "skills", "scripts"):
        if out.resolve().is_relative_to(root / name):
            raise ValueError("snapshot output must be outside the source directories")
    before = git_state(root)
    files = sources(root)
    hashes = file_hashes(files)
    manifest = {
        "schema_version": 1,
        "created_at": datetime.now(UTC).isoformat(),
        "project": before,
        "upstream": git_state(root / "deer-flow"),
        "plugin_version": tomllib.loads(
            files["extensions/scholar/pyproject.toml"].decode()
        )["project"]["version"],
        "source_sha256": tree_hash(hashes),
        "files": hashes,
        "capture_environment": {
            "python": platform.python_version(),
            "packages": dict(
                sorted(
                    (d.metadata["Name"], d.version)
                    for d in importlib.metadata.distributions()
                    if d.metadata["Name"]
                )
            ),
        },
        "limits": (
            "Source snapshot only. Capture-environment packages are not a lockfile "
            "or the deployed runtime. Runtime configuration, secrets, model "
            "settings and evaluation data are not included."
        ),
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    temp = Path(tempfile.mkdtemp(prefix=".citeguard-snapshot-", dir=out.parent))
    try:
        for name, data in files.items():
            target = temp / "source" / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            target.chmod((root / name).stat().st_mode & 0o777)
        (temp / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        if (
            file_hashes(sources(root)) != hashes
            or git_state(root)["commit"] != before["commit"]
        ):
            raise ValueError(
                "source changed during capture; retry after the edit finishes"
            )
        verify(temp)
        if out.exists():
            raise ValueError(f"snapshot already exists: {out}")
        temp.rename(out)
    finally:
        if temp.exists():
            shutil.rmtree(temp)
    return manifest


def verify(snapshot: Path) -> dict:
    manifest = json.loads((snapshot / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1:
        raise ValueError("unsupported snapshot schema")
    source = snapshot / "source"
    paths = list(source.rglob("*"))
    if source.is_symlink() or any(p.is_symlink() for p in paths):
        raise ValueError("snapshot must not contain symlinks")
    hashes = file_hashes(
        {p.relative_to(source).as_posix(): p.read_bytes() for p in paths if p.is_file()}
    )
    expected = manifest["files"]
    if not set(REQUIRED) <= expected.keys():
        raise ValueError("snapshot is missing required sources")
    if hashes != expected or tree_hash(hashes) != manifest["source_sha256"]:
        changed = sorted(
            name
            for name in hashes.keys() | expected.keys()
            if hashes.get(name) != expected.get(name)
        )
        raise ValueError(f"snapshot checksum mismatch: {changed}")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    commands = parser.add_subparsers(dest="command", required=True)
    capture = commands.add_parser("create")
    capture.add_argument("--root", type=Path, default=ROOT)
    capture.add_argument("--out", type=Path, required=True)
    check = commands.add_parser("verify")
    check.add_argument("snapshot", type=Path)
    args = parser.parse_args()
    try:
        result = (
            create(args.root, args.out)
            if args.command == "create"
            else verify(args.snapshot)
        )
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, f"snapshot failed: {exc}\n")
    print(
        json.dumps(
            {
                "plugin_version": result["plugin_version"],
                "source_sha256": result["source_sha256"],
                "files": len(result["files"]),
                "project": result["project"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
