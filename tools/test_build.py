"""Exercise generation and cleanup in isolated temporary datapacks."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

BUILDER = Path(__file__).resolve().parent / "build.py"


class Build(unittest.TestCase):
    def setUp(self):
        approved = Path(os.environ.get("LOCALAPPDATA", "")) / "Temp/opencode"
        self.temp = tempfile.TemporaryDirectory(dir=approved if approved.is_dir() else None)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "tools").mkdir()
        shutil.copyfile(BUILDER, self.root / "tools/build.py")
        self.build()

    def build(self, *args, success=True):
        result = subprocess.run([sys.executable, str(self.root / "tools/build.py"), *args],
                                cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode == 0, success, result.stdout + result.stderr)
        return result

    def obsolete(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        manifest = self.root / "tools/generated.json"
        entries = json.loads(manifest.read_text(encoding="utf-8"))
        entries[path] = hashlib.sha256(content.encode("utf-8")).hexdigest()
        manifest.write_text(json.dumps(entries), encoding="utf-8")
        return target

    def test_rebuild_is_identical(self):
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.build()
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        self.build("--check")

    def test_unknown_files_are_preserved(self):
        custom = self.root / "data/mtga/function/custom.mcfunction"
        custom.write_text("# user work\n", encoding="utf-8")
        self.build()
        self.assertEqual(custom.read_text(), "# user work\n")
        self.build("--check")

    def test_unchanged_obsolete_file_is_removed(self):
        old = self.obsolete("data/mtga/function/old.mcfunction", "# generated\n")
        self.build("--check", success=False)
        self.assertTrue(old.exists())
        self.build()
        self.assertFalse(old.exists())
        self.build("--check")

    def test_modified_obsolete_file_is_protected(self):
        old = self.obsolete("data/mtga/function/old.mcfunction", "# generated\n")
        old.write_text("# user edit\n", encoding="utf-8")
        result = self.build(success=False)
        self.assertIn("Refusing to remove modified", result.stderr)
        self.assertEqual(old.read_text(), "# user edit\n")

    def test_cleanup_cannot_escape_function_directory(self):
        outside = self.obsolete("README.md", "# keep\n")
        result = self.build(success=False)
        self.assertIn("outside function directory", result.stderr)
        self.assertEqual(outside.read_text(), "# keep\n")

    def test_check_detects_stale_outputs_without_writing(self):
        pack = self.root / "pack.mcmeta"
        pack.write_text("{}\n", encoding="utf-8")
        self.build("--check", success=False)
        self.assertEqual(pack.read_text(), "{}\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
