import io
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import fetch_financials as ff


class _Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()


class OfficialMonthRevenueTest(unittest.TestCase):
    def test_official_rows_filter_period_convert_roc_and_thousand_dollars(self):
        listed = [{
            "資料年月": "11506",
            "公司代號": "3016",
            "營業收入-當月營收": "448219",
        }, {
            "資料年月": "11505",
            "公司代號": "3661",
            "營業收入-當月營收": "1",
        }]
        otc = [{
            "資料年月": "11506",
            "公司代號": "3680",
            "營業收入-當月營收": "752,110",
        }]
        payloads = iter((listed, otc))

        def opener(request, timeout):
            self.assertEqual(timeout, 30)
            self.assertIn(request.full_url, {
                ff.TWSE_MONTH_REVENUE_URL, ff.TPEX_MONTH_REVENUE_URL})
            return _Response(json.dumps(next(payloads), ensure_ascii=False).encode())

        rows = ff.official_month_revenue_rows(
            ["3016", "3661", "3680"], 2026, 6, opener=opener)

        self.assertEqual(set(rows), {"3016", "3680"})
        self.assertEqual(rows["3016"]["date"], "2026-07-01")
        self.assertEqual(rows["3016"]["revenue"], 448_219_000)
        self.assertEqual(rows["3680"]["revenue"], 752_110_000)

    def test_fallback_only_inserts_missing_rows(self):
        con = sqlite3.connect(":memory:")
        con.executescript(ff.SCHEMA)
        con.execute(
            "INSERT INTO month_revenue VALUES(?,?,?,?,?)",
            ("2026-07-01", "3016", 111, 6, 2026),
        )
        con.execute(
            "INSERT INTO month_revenue VALUES(?,?,?,?,?)",
            ("2026-07-01", "3680", None, 6, 2026),
        )

        def fetcher(stock_ids, year, month):
            self.assertEqual(stock_ids, ["3680"])
            self.assertEqual((year, month), (2026, 6))
            return {
                "3680": {
                    "date": "2026-07-01", "stock_id": "3680",
                    "revenue": 752_110_000, "revenue_month": 6, "revenue_year": 2026,
                }
            }

        before, filled, after = ff.fill_official_month_revenue(
            con, ["3016", "3680"], 2026, 6, fetcher=fetcher)

        self.assertEqual(before, ["3680"])
        self.assertEqual(filled, ["3680"])
        self.assertEqual(after, [])
        self.assertEqual(con.execute(
            "SELECT revenue FROM month_revenue WHERE stock_id='3016'"
        ).fetchone()[0], 111)
        con.close()

    def test_upsert_records_first_seen_without_overwriting_it(self):
        con = sqlite3.connect(":memory:")
        ff.ensure_schema(con)
        data = [{
            "date": "2026-08-01", "stock_id": "3016", "revenue": 100,
            "revenue_month": 7, "revenue_year": 2026,
        }]
        ff.up_month_revenue(
            con, data, first_seen_at="2026-08-13T01:00:00+00:00", source="FinMind")
        ff.up_month_revenue(
            con, data, first_seen_at="2026-08-14T01:00:00+00:00", source="FinMind")
        row = con.execute(
            "SELECT first_seen_at,source FROM fundamental_availability"
        ).fetchone()
        self.assertEqual(row, ("2026-08-13T01:00:00+00:00", "FinMind"))
        con.close()

    def test_upsert_and_availability_ledger_share_the_callers_transaction(self):
        con = sqlite3.connect(":memory:")
        ff.ensure_schema(con)
        con.commit()
        con.execute(
            "INSERT INTO month_revenue VALUES(?,?,?,?,?)",
            ("2026-07-01", "OLD", 1, 6, 2026),
        )
        ff.up_month_revenue(con, [{
            "date": "2026-08-01", "stock_id": "3016", "revenue": 100,
            "revenue_month": 7, "revenue_year": 2026,
        }], first_seen_at="2026-08-13T01:00:00+00:00")
        con.rollback()
        self.assertEqual(con.execute("SELECT COUNT(*) FROM month_revenue").fetchone()[0], 0)
        self.assertEqual(con.execute(
            "SELECT COUNT(*) FROM fundamental_availability").fetchone()[0], 0)
        con.close()

    def test_existing_history_is_only_available_from_migration_time(self):
        con = sqlite3.connect(":memory:")
        ff.ensure_schema(con)
        con.execute(
            "INSERT INTO month_revenue VALUES(?,?,?,?,?)",
            ("2026-08-01", "3016", 100, 7, 2026),
        )
        inserted = ff.initialize_existing_availability(
            con, first_seen_at="2026-08-13T01:00:00+00:00")
        self.assertEqual(inserted, 1)
        row = con.execute(
            "SELECT source_published_at,first_seen_at,source FROM fundamental_availability"
        ).fetchone()
        self.assertEqual(row, (
            None, "2026-08-13T01:00:00+00:00", "migration_existing_rows"))
        con.close()

    def test_offline_ledger_initializer_is_idempotent_and_does_not_change_source_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "financials.db"
            con = sqlite3.connect(path)
            ff.ensure_schema(con)
            con.execute(
                "INSERT INTO month_revenue VALUES(?,?,?,?,?)",
                ("2026-08-01", "3016", 100, 7, 2026),
            )
            con.commit()
            con.close()

            first = ff.initialize_availability_ledger(
                str(path), first_seen_at="2026-08-13T01:00:00+00:00")
            second = ff.initialize_availability_ledger(
                str(path), first_seen_at="2026-08-14T01:00:00+00:00")
            con = sqlite3.connect(path)
            self.assertEqual((first, second), (1, 0))
            self.assertEqual(
                con.execute("SELECT COUNT(*),SUM(revenue) FROM month_revenue").fetchone(),
                (1, 100))
            self.assertEqual(con.execute(
                "SELECT first_seen_at FROM fundamental_availability"
            ).fetchone()[0], "2026-08-13T01:00:00+00:00")
            con.close()


class FinancialWorkflowContractTest(unittest.TestCase):
    def test_monthly_retry_is_strict_and_quarter_writes_remain_serialized(self):
        text = (ROOT / ".github" / "workflows" / "fetch-financials.yml").read_text(
            encoding="utf-8")
        retry = '0 2 17 1,2,3,4,6,7,9,10,12 *'
        self.assertIn(f'cron: "{retry}"', text)
        self.assertIn(
            'elif [ "${{ github.event.schedule }}" = "' + retry + '" ]; then', text)
        self.assertIn("--require-latest-month-complete", text)
        for month in ("5", "8", "11"):
            self.assertIn(
                f'[ "${{{{ github.event.schedule }}}}" = "0 2 17 {month} *" ]',
                text)
        self.assertIn(
            "python scripts/fetch_financials.py --require-latest-month-complete",
            text)
        self.assertIn("group: repo-main-writer", text)
        self.assertIn("queue: max", text)

        tests_workflow = (
            ROOT / ".github" / "workflows" / "tests.yml"
        ).read_text(encoding="utf-8")
        self.assertGreaterEqual(
            tests_workflow.count('".github/workflows/fetch-financials.yml"'), 2)


if __name__ == "__main__":
    unittest.main()
