"""Snapshots detect mutations and exclude credentials."""

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "capture_snapshot.py"
spec = importlib.util.spec_from_file_location("capture_snapshot", SCRIPT)
snapshot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(snapshot)


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        self.out = Path(self.temp.name) / "release"
        for name in snapshot.REQUIRED:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                '[project]\nversion = "0.3.5"\n'
                if name.endswith("toml")
                else "sample\n"
            )

    def test_roundtrip_excludes_credentials_and_does_not_overwrite(self):
        for name in (
            ".env",
            "deer-flow/config.yaml",
            "extensions/scholar/.env",
            ".local/cookies.txt",
        ):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("PRIVATE")
        created = snapshot.create(self.root, self.out)
        self.assertEqual(snapshot.verify(self.out), created)
        self.assertEqual(created["project"], {"commit": None, "dirty": None})
        self.assertEqual(set(created["files"]), set(snapshot.REQUIRED))
        self.assertNotIn("PRIVATE", (self.out / "manifest.json").read_text())
        with self.assertRaisesRegex(ValueError, "already exists"):
            snapshot.create(self.root, self.out)

    def test_modification_deletion_and_extra_files_are_detected(self):
        snapshot.create(self.root, self.out)
        file = self.out / "source" / snapshot.REQUIRED[0]
        original = file.read_bytes()
        file.write_text("changed")
        with self.assertRaisesRegex(ValueError, "checksum mismatch"):
            snapshot.verify(self.out)
        file.unlink()
        with self.assertRaisesRegex(ValueError, "checksum mismatch"):
            snapshot.verify(self.out)
        file.write_bytes(original)
        (self.out / "source" / "unexpected.py").write_text("extra")
        with self.assertRaisesRegex(ValueError, "checksum mismatch"):
            snapshot.verify(self.out)

    def test_symlinks_cannot_copy_files_outside_the_project(self):
        target = self.root / snapshot.REQUIRED[0]
        target.unlink()
        outside = Path(self.temp.name) / "private"
        outside.write_text("PRIVATE")
        target.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "regular file"):
            snapshot.create(self.root, self.out)
        self.assertFalse(self.out.exists())

    def test_concurrent_edits_abort_capture(self):
        read_sources = snapshot.sources
        calls = 0

        def changing(root):
            nonlocal calls
            calls += 1
            if calls == 2:
                (root / snapshot.REQUIRED[0]).write_text("concurrent edit")
            return read_sources(root)

        with (
            patch.object(snapshot, "sources", side_effect=changing),
            self.assertRaisesRegex(ValueError, "source changed"),
        ):
            snapshot.create(self.root, self.out)
        self.assertFalse(self.out.exists())
        self.assertFalse(list(self.out.parent.glob(".citeguard-snapshot-*")))


if __name__ == "__main__":
    unittest.main()
