"""screen.py CLI 契約:查用法不得產生報告,錯誤路徑不得建立資料庫。

原本 screen.py 沒有 argparse,任何參數都被默默忽略——下 `--help` 會跑完整篩選並寫出
一份看起來正式的 `reports/screen_<今日>.md`,容易被誤讀成真的做過季度 universe 治理。
本測試不觸發 §B 候選體檢,零 FinMind API call。
"""
import datetime
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCREEN = ROOT / "scripts" / "screen.py"


def run(*args):
    return subprocess.run([sys.executable, str(SCREEN), *args],
                          cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
                          env={**os.environ, "PYTHONIOENCODING": "utf-8"})


class ScreenCliTest(unittest.TestCase):
    def _report_path(self):
        return ROOT / "reports" / f"screen_{datetime.date.today().isoformat()}.md"

    def test_help_exits_without_writing_report(self):
        existed = self._report_path().exists()
        r = run("--help")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("--no-candidates", r.stdout)
        if not existed:
            self.assertFalse(self._report_path().exists(),
                             "--help 不得產生 reports/screen_<今日>.md")

    def test_unknown_argument_is_rejected(self):
        existed = self._report_path().exists()
        r = run("--bogus")
        self.assertEqual(r.returncode, 2, "未知參數必須報錯,不得默默跑完整篩選")
        if not existed:
            self.assertFalse(self._report_path().exists(),
                             "參數錯誤時不得產生報告")

    def test_missing_db_errors_without_creating_file(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "missing.db"
            r = run("--no-candidates", "--dry-run", "--db", str(db))
            self.assertFalse(db.exists(), "不存在的資料庫不得被建立")
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("資料庫不存在", r.stderr)
            self.assertIn(str(db), r.stderr)
            self.assertEqual(len(r.stderr.splitlines()), 1, r.stderr)


if __name__ == "__main__":
    unittest.main()
