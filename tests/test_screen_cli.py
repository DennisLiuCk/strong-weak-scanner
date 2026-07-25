"""screen.py CLI 契約:查用法不得產生報告。

原本 screen.py 沒有 argparse,任何參數都被默默忽略——下 `--help` 會跑完整篩選並寫出
一份看起來正式的 `reports/screen_<今日>.md`,容易被誤讀成真的做過季度 universe 治理。
本測試只走 argparse 提早退出的路徑,不觸發 §B 候選體檢,零 FinMind API call。
"""
import datetime
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCREEN = ROOT / "scripts" / "screen.py"


def run(*args):
    return subprocess.run([sys.executable, str(SCREEN), *args],
                          cwd=ROOT, capture_output=True, text=True, encoding="utf-8")


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


if __name__ == "__main__":
    unittest.main()
