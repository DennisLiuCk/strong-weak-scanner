import datetime as dt
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import prepublish_check as pc
import build_dashboard as dashboard


class BuildDateTest(unittest.TestCase):
    def test_rollover_rebuild_uses_committed_as_of_and_still_detects_drift(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "archive").mkdir()
            page = 'const LIB=' + json.dumps({"asOf": "2026-08-07"}) + ', MARKET_DATE="2026-08-06";'
            (root / "research.html").write_text(page, encoding="utf-8")
            (root / "index.html").write_text("dashboard", encoding="utf-8")

            def rebuild(research_as_of=None):
                as_of = research_as_of or dashboard.research_today()
                Path(dashboard.OUT).write_text("dashboard", encoding="utf-8")
                Path(dashboard.RESEARCH_OUT).write_text(
                    page.replace("2026-08-07", as_of.isoformat()), encoding="utf-8")

            with patch.object(pc, "ROOT", root), patch.object(dashboard, "main", side_effect=rebuild), \
                    patch.object(dashboard, "research_today", return_value=dt.date(2026, 8, 8)):
                pc.verify_build(root / "build")
                (root / "research.html").write_text(page + "drift", encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "research.html"):
                    pc.verify_build(root / "drift")

    def test_missing_or_invalid_as_of_fails_closed(self):
        for page in ('', 'const LIB={};', 'const LIB={"asOf":null};',
                     'const LIB={"asOf":"2026-02-30"};'):
            with self.subTest(page=page), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                (root / "archive").mkdir()
                (root / "research.html").write_text(page, encoding="utf-8")
                with patch.object(pc, "ROOT", root), patch.object(dashboard, "main") as build:
                    with self.assertRaises(ValueError):
                        pc.verify_build(root / "build")
                    build.assert_not_called()


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
