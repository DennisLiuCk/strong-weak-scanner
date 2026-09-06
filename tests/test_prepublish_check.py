import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import prepublish_check as pc


class BaselineTest(unittest.TestCase):
    def test_shared_gate_runs_every_required_check_with_pinned_baseline(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            with patch.object(pc, "ROOT", root), patch.object(pc, "resolve_baseline", return_value="a" * 40), \
                    patch.object(pc, "protected_hashes", return_value={"db": "unchanged"}), \
                    patch.object(pc, "verify_build") as build, patch.object(pc.subprocess, "run") as execute:
                execute.return_value.returncode = 0
                result = pc.run("before-work", root / "tmp" / "check")
            calls = [c.args[0][1:] for c in execute.call_args_list]
            for script in ("qual_notes", "leading_hypotheses", "knowledge_graph", "research_radar"):
                self.assertIn([f"scripts/{script}.py", "--lint"], calls)
            for script in ("research_queue", "research_method_audit"):
                self.assertIn([f"scripts/{script}.py", "--lint", "--baseline-ref", "a" * 40], calls)
            self.assertIn(["-m", "unittest", "discover", "-s", "tests", "-q"], calls)
            build.assert_called_once()
            self.assertTrue(result["ok"])

    def test_nonexistent_and_unrelated_baselines_fail_without_fallback(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            def git(*args):
                return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.DEVNULL, text=True).strip()
            git("init")
            git("-c", "user.name=test", "-c", "user.email=test@example.com", "commit", "--allow-empty", "-m", "base")
            first = git("rev-parse", "HEAD")
            self.assertEqual(pc.resolve_baseline("HEAD", root), first)
            git("checkout", "--orphan", "unrelated")
            git("-c", "user.name=test", "-c", "user.email=test@example.com", "commit", "--allow-empty", "-m", "other")
            for ref in ("missing-rewritten-commit", first, "--help"):
                with self.subTest(ref=ref), self.assertRaises(ValueError):
                    pc.resolve_baseline(ref, root)
