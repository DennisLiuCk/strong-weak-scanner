"""零成交值納入流動性中位數，僅排除缺值。"""
from contextlib import closing, redirect_stdout
import io
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from test_screen_cli import run

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import screen


class ScreenLiquidityTest(unittest.TestCase):
    def make_db(self, db, amounts):
        with closing(sqlite3.connect(db)) as con, con:
            con.executescript("""
                CREATE TABLE groups (grp TEXT, ord INTEGER);
                CREATE TABLE universe (stock_id TEXT, name TEXT, grp TEXT, biz TEXT);
                CREATE TABLE price (stock_id TEXT, date TEXT, close REAL, amount REAL);
                CREATE TABLE holding (stock_id TEXT, date TEXT, shares_issued REAL);
                INSERT INTO groups VALUES ('test', 1);
                INSERT INTO universe VALUES ('0001', 'Member', 'test', '');
                INSERT INTO holding VALUES ('0001', '2026-01-20', 50000000);
            """)
            con.executemany("INSERT INTO price VALUES ('0001', ?, 100, ?)",
                            [(f"2026-01-{i:02d}", amount)
                             for i, amount in enumerate(amounts, 1)])

    def test_member_report_counts_zero_amount_days(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "screen.db"
            self.make_db(db, [0] * 11 + [100000000] * 9)
            result = run("--db", str(db), "--no-candidates", "--dry-run")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("| 0001 | Member | test | 50 | 0M | 👀 緩衝觀察", result.stdout)
            self.assertNotIn("✅ 續留", result.stdout)

    def test_member_report_excludes_only_null_amounts(self):
        for amounts, expected in (([None] * 11 + [100000000] * 9, "100M | ✅ 續留"),
                                  ([None] * 20, "— | ⚪ 資料不足")):
            with self.subTest(amounts=amounts), tempfile.TemporaryDirectory() as directory:
                db = Path(directory) / "screen.db"
                self.make_db(db, amounts)
                result = run("--db", str(db), "--no-candidates", "--dry-run")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(f"| 0001 | Member | test | 50 | {expected}", result.stdout)

    def test_candidate_report_counts_zero_amount_days_even_without_close(self):
        for low_amount, expected in ((0, "0M | ❌ 不納入"),
                                     (None, "100M | ✅ 建議納入")):
            with self.subTest(low_amount=low_amount), tempfile.TemporaryDirectory() as directory:
                db = Path(directory) / "screen.db"
                self.make_db(db, [])
                prices = ([{"close": 100, "Trading_money": 100000000}] * 60
                          + [{"close": None, "Trading_money": low_amount}] * 11
                          + [{"close": 100, "Trading_money": 100000000}] * 9)
                responses = [[{"stock_id": "0002", "stock_name": "Candidate"}],
                             prices, [{"NumberOfSharesIssued": 50000000}]]
                output = io.StringIO()
                with patch.object(sys, "argv", ["screen.py", "--db", str(db), "--dry-run"]), \
                        patch.object(screen, "get_token", return_value="unused"), \
                        patch.object(screen, "api_get", side_effect=responses), \
                        patch("builtins.open", unittest.mock.mock_open(
                            read_data="stock_id,group,biz\n0002,test,test\n")), \
                        redirect_stdout(output):
                    screen.main()
                self.assertIn(f"| 0002 | Candidate | test | - | 50 | {expected}", output.getvalue())


if __name__ == "__main__":
    unittest.main()
