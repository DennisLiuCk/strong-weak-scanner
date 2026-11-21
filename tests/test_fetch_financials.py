import io
import json
import sqlite3
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import fetch_financials as ff


class _Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()


class OfficialMonthRevenueTest(unittest.TestCase):
    def test_market_failures_are_isolated_and_identified(self):
        for failed_url, market in ((ff.TWSE_MONTH_REVENUE_URL, "TWSE"),
                                   (ff.TPEX_MONTH_REVENUE_URL, "TPEx")):
            for payload in (b"not json", json.dumps([
                    {"公司代號": "2330"}]).encode()):
                with self.subTest(market=market, payload=payload):
                    calls = []

                    def opener(request, timeout):
                        calls.append(request.full_url)
                        if request.full_url == failed_url:
                            return _Response(payload)
                        return _Response(json.dumps([{
                            "資料年月": "11506", "公司代號": "2330",
                            "營業收入-當月營收": "123",
                        }]).encode())

                    if payload == b"not json":
                        with self.assertRaises(ff.OfficialMonthRevenueError) as caught:
                            ff.official_month_revenue_rows(["2330"], 2026, 6, opener)
                        self.assertEqual(set(caught.exception.failures), {market})
                        self.assertEqual(caught.exception.rows["2330"]["revenue"], 123_000)
                    else:
                        rows = ff.official_month_revenue_rows(["2330"], 2026, 6, opener)
                        self.assertEqual(rows["2330"]["revenue"], 123_000)
                    self.assertEqual(len(calls), 2)

    def test_strict_cli_commits_partial_rows_before_reporting_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = str(Path(tmp) / "financials.db")
            failure = ff.OfficialMonthRevenueError({"2330": {
                "date": "2026-07-01", "stock_id": "2330", "revenue": 123_000,
                "revenue_year": 2026, "revenue_month": 6,
            }}, {"TPEx": urllib.error.URLError("unavailable")})

            def fill(con, ids, year, month):
                def fetcher(*args):
                    raise failure
                return original_fill(con, ids, year, month, fetcher=fetcher)

            original_fill = ff.fill_official_month_revenue
            stderr = io.StringIO()
            with patch.object(sys, "argv", ["fetch_financials.py", "--db", db,
                    "--end", "2026-07-17", "--stocks", "2330",
                    "--official-month-revenue-only", "--require-latest-month-complete"]), \
                    patch.object(ff, "fill_official_month_revenue", side_effect=fill), \
                    patch.object(sys, "stderr", stderr):
                with self.assertRaises(SystemExit) as caught:
                    ff.main()
            self.assertEqual(caught.exception.code, 1)
            self.assertIn("TPEx: URLError", stderr.getvalue())
            with sqlite3.connect(db) as con:
                self.assertEqual(con.execute(
                    "SELECT stock_id,revenue FROM month_revenue").fetchall(),
                    [("2330", 123_000)])

    def test_fallback_saves_twse_rows_when_tpex_fails(self):
        con = sqlite3.connect(":memory:")
        self.addCleanup(con.close)
        ff.ensure_schema(con)

        def opener(request, timeout):
            if request.full_url == ff.TPEX_MONTH_REVENUE_URL:
                raise urllib.error.URLError("TPEx unavailable")
            return _Response(json.dumps([{
                "資料年月": "11506", "公司代號": "2330",
                "營業收入-當月營收": "123,456",
            }]).encode())

        def fetcher(stock_ids, year, month):
            return ff.official_month_revenue_rows(stock_ids, year, month, opener=opener)

        with self.assertRaisesRegex(Exception, "TPEx unavailable"):
            ff.fill_official_month_revenue(con, ["2330", "3680"], 2026, 6,
                                          fetcher=fetcher)
        self.assertEqual(con.execute(
            "SELECT stock_id,revenue FROM month_revenue").fetchall(),
            [("2330", 123_456_000)])
        self.assertEqual(ff.missing_month_revenue(con, ["2330", "3680"], 2026, 6),
                         ["3680"])

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
        ff.ensure_schema(con)
        con.execute(
            "INSERT INTO month_revenue(date,stock_id,revenue,revenue_month,revenue_year) VALUES(?,?,?,?,?)",
            ("2026-07-01", "3016", 111, 6, 2026),
        )
        con.execute(
            "INSERT INTO month_revenue(date,stock_id,revenue,revenue_month,revenue_year) VALUES(?,?,?,?,?)",
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
        self.assertEqual(con.execute("SELECT COUNT(*) FROM fundamental_revisions").fetchone()[0], 0)
        self.assertEqual(con.execute("SELECT revenue,observed_at FROM month_revenue").fetchone(),
                         (100, "2026-08-13T01:00:00+00:00"))
        con.close()

    def test_all_eav_datasets_keep_distinct_items_and_reversions(self):
        con = sqlite3.connect(":memory:")
        self.addCleanup(con.close)
        ff.ensure_schema(con)
        first = "2026-08-13T01:00:00+00:00"
        second = "2026-08-14T01:00:00+00:00"
        for dataset in ff.UPSERT.keys() - {"TaiwanStockMonthRevenue"}:
            upsert = ff.UPSERT[dataset]
            item = {"date": "2026-06-30", "stock_id": "3016", "type": "X", "value": 10}
            upsert(con, [item, dict(item, type="Y")], first_seen_at=first)
            upsert(con, [dict(item, value=20)], first_seen_at=second)
            upsert(con, [item], first_seen_at=second)
            upsert(con, [item], first_seen_at=second)
            self.assertEqual(con.execute(
                """SELECT item_type,value,observed_at FROM fundamental_revisions
                   WHERE dataset=? ORDER BY id""", (dataset,),
            ).fetchall(), [("X", 10, first), ("X", 20, second)])
            self.assertEqual(con.execute(
                f"SELECT type,value,observed_at FROM {ff.DATASET_TABLES[dataset]} ORDER BY type"
            ).fetchall(), [("X", 10, second), ("Y", 10, first)])

    def test_upsert_and_availability_ledger_share_the_callers_transaction(self):
        con = sqlite3.connect(":memory:")
        ff.ensure_schema(con)
        data = {
            "date": "2026-08-01", "stock_id": "3016", "revenue": 100,
            "revenue_month": 7, "revenue_year": 2026,
        }
        ff.up_month_revenue(con, [data], first_seen_at="2026-08-13T01:00:00+00:00")
        con.commit()
        ff.up_month_revenue(con, [dict(data, revenue=200), dict(data, stock_id="NEW")],
                            first_seen_at="2026-08-14T01:00:00+00:00")
        self.assertEqual(con.execute(
            "SELECT value FROM fundamental_revisions").fetchall(), [(100,)])
        con.rollback()
        self.assertEqual(con.execute("SELECT stock_id,revenue FROM month_revenue").fetchall(),
                         [("3016", 100)])
        self.assertEqual(con.execute(
            "SELECT stock_id FROM fundamental_availability").fetchall(), [("3016",)])
        self.assertEqual(con.execute(
            "SELECT COUNT(*) FROM fundamental_revisions").fetchone()[0], 0)
        con.close()

    def test_existing_history_is_only_available_from_migration_time(self):
        con = sqlite3.connect(":memory:")
        ff.ensure_schema(con)
        con.execute(
            "INSERT INTO month_revenue(date,stock_id,revenue,revenue_month,revenue_year) VALUES(?,?,?,?,?)",
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
            con.executescript(ff.SCHEMA)
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
            self.assertEqual(con.execute("SELECT COUNT(*) FROM fundamental_revisions").fetchone()[0], 0)
            self.assertEqual(con.execute(
                "SELECT observed_at FROM fundamental_revision_baseline"
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
