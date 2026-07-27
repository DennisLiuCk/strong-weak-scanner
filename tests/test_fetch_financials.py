import io
import json
import sqlite3
import sys
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
