import contextlib
import io
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import daily_brief
import operational_health


class DailyBriefTest(unittest.TestCase):
    def render_brief(self, current):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "brief.db"
            with sqlite3.connect(db) as con:
                con.executescript("""
                    CREATE TABLE universe(stock_id TEXT, name TEXT, grp TEXT);
                    INSERT INTO universe VALUES ('3529', '力旺', '矽智財'),
                                                ('2330', '台積電', '晶圓');
                    CREATE TABLE daily_scores(date TEXT, stock_id TEXT, tier TEXT,
                        tier_raw TEXT, pending TEXT, composite_s REAL);
                    INSERT INTO daily_scores VALUES
                        ('2026-01-01', '3529', '中性', '中性', '量', 0),
                        ('2026-01-01', '2330', '中性', '中性', '', 0),
                        ('2026-01-02', '2330', '中性', '中性', '', 0);
                    CREATE TABLE market_daily(date TEXT, dd20 REAL);
                    CREATE TABLE group_metrics(date TEXT, grp TEXT);
                    CREATE TABLE price(date TEXT, stock_id TEXT, close REAL);
                    CREATE TABLE price_adj(date TEXT, stock_id TEXT, close REAL);
                    CREATE TABLE daily_metrics(date TEXT, stock_id TEXT, ret1 REAL);
                """)
                for table in ('inst', 'margin', 'holding', 'sbl'):
                    con.execute(f"CREATE TABLE {table}(date TEXT)")
                if current is not None:
                    con.execute("INSERT INTO daily_scores VALUES (?, ?, ?, ?, ?, ?)",
                                ('2026-01-02', '3529', *current, 0))
            out = io.StringIO()
            with patch.object(daily_brief, 'DB', str(db)), \
                    patch.object(daily_brief.tstatus, 'verified_exclusions', return_value=[]), \
                    patch.object(daily_brief.tstatus, 'expected_ids', return_value=[]), \
                    patch.object(daily_brief.sig, 'group_rows', return_value=[]), \
                    patch.object(daily_brief.sig, 'tier_sequences', return_value={}), \
                    patch.object(operational_health, 'build_health', return_value={}), \
                    patch.object(operational_health, 'render', return_value='整合健康摘要'), \
                    contextlib.redirect_stdout(out):
                daily_brief.main()
            return out.getvalue()

    def test_missing_current_score_leaves_pending_with_explicit_reason(self):
        output = self.render_brief(None)
        self.assertIn('離開候補 → 最新日缺評分', output)
        self.assertNotIn('退出(現', output)
        self.assertIn('■ 綜合分變動 Top5:', output)
        self.assertIn('■ 基礎資料快檢:', output)
        self.assertIn('整合健康摘要', output)

    def test_existing_score_preserves_pending_transitions(self):
        for tier, raw, reason in (
                ('蓄勢', '蓄勢', '升蓄勢!'),
                ('中性', '蓄勢', '升蓄勢待確認(明日同向即轉層)'),
                ('中性', '中性', '退出(現 中性)')):
            with self.subTest(tier=tier, raw=raw):
                self.assertIn('離開候補 → ' + reason,
                              self.render_brief((tier, raw, '')))

    def test_unchanged_pending_stays_listed(self):
        output = self.render_brief(('中性', '中性', '量'))
        self.assertIn('◇量', output)
        self.assertNotIn('離開候補', output)


if __name__ == '__main__':
    unittest.main()
