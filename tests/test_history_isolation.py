"""歷史延伸隔離契約:回補 2026-03-02 之前的資料不得落進正式 db。

為什麼是硬性規則(2026-07-26 實測結果):把 2026-02 一個月接到既有歷史前面之後,
**3~4 月既有的個股綜合分有 51% 改變**——因為評分是族群內排名,而 rs20/dist_hi60 的
視窗一旦有了更早的資料就從 NULL 變成有值。正式 db 正在累積 as-seen 快照,那些快照
是不可改寫的證據;底下的重算歷史若被延伸改掉,快照與歷史就不再可比,且不可逆。
"""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import fetch_daily as fd


def run(script, *args):
    return subprocess.run([sys.executable, str(SCRIPTS / script), *args],
                          cwd=ROOT, capture_output=True, text=True, encoding="utf-8")


class HistoryIsolationTest(unittest.TestCase):
    def test_history_floor_matches_production_start(self):
        """護欄的門檻就是正式 db 的起算日;兩者脫鉤會讓護欄失去意義。"""
        self.assertEqual(fd.HISTORY_FLOOR, "2026-03-02")

    def test_backfill_before_floor_into_production_db_is_rejected(self):
        r = run("fetch_daily.py", "--start", "2026-02-02", "--end", "2026-02-05", "--raw-only")
        self.assertEqual(r.returncode, 2, "早於起算日又指向正式 db,必須擋下")
        self.assertIn("--db", r.stderr, "錯誤訊息要指出正確做法")
        self.assertIn(fd.HISTORY_FLOOR, r.stderr)

    def test_backfill_before_floor_is_allowed_with_separate_db(self):
        """指向別的檔案就放行——用 --metrics-only 走完參數檢查但不連外抓資料。"""
        with tempfile.TemporaryDirectory() as tmp:
            r = run("fetch_daily.py", "--start", "2026-02-02", "--end", "2026-02-05",
                    "--metrics-only", "--db", os.path.join(tmp, "hist.db"))
            self.assertEqual(r.returncode, 0, f"指定 --db 後不該被擋:{r.stderr[:300]}")
            self.assertTrue(os.path.exists(os.path.join(tmp, "hist.db")),
                            "--db 沒有被實際採用")

    def test_production_db_is_untouched_by_separate_db_run(self):
        prod = ROOT / "data" / "findmind.db"
        before = prod.stat().st_size, prod.stat().st_mtime_ns
        with tempfile.TemporaryDirectory() as tmp:
            run("fetch_daily.py", "--metrics-only", "--db", os.path.join(tmp, "hist.db"))
        self.assertEqual((prod.stat().st_size, prod.stat().st_mtime_ns), before,
                         "指定 --db 之後正式 db 仍被寫入")

    def test_score_also_supports_separate_db(self):
        """整條鏈(抓取→評分→驗證)都要能改道,否則歷史檢定場只做得到一半。"""
        r = run("score.py", "--help")
        self.assertEqual(r.returncode, 0)
        self.assertIn("--db", r.stdout)


if __name__ == "__main__":
    unittest.main()
