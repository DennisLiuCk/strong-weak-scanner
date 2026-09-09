# -*- coding: utf-8 -*-
import datetime as dt
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import research_event_scan as res


def announcement(code, speech="1150806", output="1150807", *, tpex=False):
    if tpex:
        return {
            "Date": output,
            "發言日期": speech,
            "SecuritiesCompanyCode": code,
        }
    return {"出表日期": output, "發言日期": speech, "公司代號": code}


def quarter_row(code, *, tpex=False, year="115", quarter="2"):
    if tpex:
        return {
            "SecuritiesCompanyCode": code,
            "Year": year,
            "Season": quarter,
        }
    return {"公司代號": code, "年度": year, "季別": quarter}


class ResearchEventScanTest(unittest.TestCase):
    def census_dates(self, twse, tpex, start="2026-09-07", end="2026-09-08"):
        return res.compute_census(
            {"1111"},
            {
                "twse": [announcement("1111", speech=d, output="1150909") for d in twse],
                "tpex": [announcement("9999", speech=d, output="1150909", tpex=True) for d in tpex],
            }, [], [], window_start=dt.date.fromisoformat(start),
            window_end=dt.date.fromisoformat(end), quarter_year="115", quarter="2",
        )

    def test_last_day_does_not_cover_multiday_window(self):
        coverage = self.census_dates(["1150908"], ["1150908"])["coverage"]
        self.assertFalse(coverage["complete"])
        self.assertEqual(coverage["missingSpeechDatesByMarket"],
                         {"twse": ["2026-09-07"], "tpex": ["2026-09-07"]})
        self.assertIn("部分日期", coverage["limitation"])

    def test_endpoints_do_not_cover_missing_interior_day(self):
        coverage = self.census_dates(["1150906", "1150908"], ["1150906", "1150908"],
                                     start="2026-09-06")["coverage"]
        self.assertFalse(coverage["complete"])
        self.assertEqual(coverage["missingSpeechDatesByMarket"]["twse"], ["2026-09-07"])

    def test_market_union_cannot_fill_another_markets_gap(self):
        coverage = self.census_dates(["1150907"], ["1150908"])["coverage"]
        self.assertFalse(coverage["complete"])
        self.assertEqual(coverage["missingSpeechDatesByMarket"],
                         {"twse": ["2026-09-08"], "tpex": ["2026-09-07"]})

    def test_all_requested_dates_in_both_markets_can_cover_window(self):
        coverage = self.census_dates(["1150907", "1150908"], ["1150907", "1150908"])["coverage"]
        self.assertTrue(coverage["complete"])
        self.assertEqual(coverage["missingSpeechDatesByMarket"], {"twse": [], "tpex": []})

    def test_rolled_past_window_does_not_close_historical_gap(self):
        coverage = self.census_dates(["1150908"], ["1150908"], end="2026-09-07")["coverage"]
        self.assertFalse(coverage["complete"])
        self.assertIn("不含窗內任何一天", coverage["limitation"])

    def test_missing_weekend_is_unknown_not_zero(self):
        coverage = self.census_dates(["1150907", "1150908"], ["1150907", "1150908"],
                                     start="2026-09-06")["coverage"]
        self.assertFalse(coverage["complete"])
        self.assertEqual(coverage["missingSpeechDatesByMarket"]["twse"], ["2026-09-06"])

    def test_require_full_rejects_date_gap_and_output_is_utf8_lf(self):
        payload = self.census_dates(["1150908"], ["1150908"])
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "scan.json"
            with patch.object(res, "run_scan", return_value=payload):
                result = res.main(["--window-start", "2026-09-07", "--window-end", "2026-09-08",
                                   "--quarter-year", "115", "--quarter", "2", "--require-full",
                                   "--output", str(output)])
            self.assertEqual(result, 2)
            raw = output.read_bytes()
            self.assertNotIn(b"\r\n", raw)
            self.assertIn("部分日期", raw.decode("utf-8"))

    def test_current_output_batch_cannot_cover_same_day_window_end(self):
        payload = res.compute_census(
            {"1111", "2222"},
            {
                "twse": [announcement("1111")],
                "tpex": [announcement("2222", tpex=True)],
            },
            [quarter_row("1111"), quarter_row("2222", tpex=True)],
            [quarter_row("1111"), quarter_row("2222", tpex=True)],
            window_start=dt.date(2026, 8, 6),
            window_end=dt.date(2026, 8, 7),
            quarter_year="115",
            quarter="2",
        )
        self.assertFalse(payload["coverage"]["complete"])
        self.assertEqual(payload["coverage"]["scope"], "partial")
        self.assertEqual(
            payload["coverage"]["announcementCoverageThrough"],
            {"twse": "2026-08-06", "tpex": "2026-08-06"},
        )
        self.assertEqual(payload["announcements"]["rowsInUniverseWindow"], 2)
        self.assertEqual(payload["quarterlyGrid"]["pairedN"], 2)
        self.assertEqual(payload["population"]["universeN"], 2)
        self.assertFalse(payload["population"]["inferentialSample"])

    def test_next_day_output_batch_can_close_explicit_window(self):
        payload = res.compute_census(
            {"1111"},
            {
                "twse": [announcement("9999", speech="1150807", output="1150808")],
                "tpex": [announcement(
                    "9999", speech="1150807", output="1150808", tpex=True)],
            },
            [],
            [],
            window_start=dt.date(2026, 8, 7),
            window_end=dt.date(2026, 8, 7),
            quarter_year="115",
            quarter="2",
        )
        self.assertTrue(payload["coverage"]["complete"])
        self.assertEqual(payload["coverage"]["scope"], "full")
        self.assertEqual(payload["announcements"]["rowsInUniverseWindow"], 0)

    def test_quarter_pair_is_intersection_not_union(self):
        payload = res.compute_census(
            {"1111", "2222", "3333"},
            {
                "twse": [announcement("9999", output="1150808")],
                "tpex": [announcement("9999", output="1150808", tpex=True)],
            },
            [quarter_row("1111"), quarter_row("2222", tpex=True)],
            [quarter_row("2222", tpex=True), quarter_row("3333")],
            window_start=dt.date(2026, 8, 7),
            window_end=dt.date(2026, 8, 7),
            quarter_year="115",
            quarter="2",
        )
        self.assertEqual(payload["quarterlyGrid"]["incomeN"], 2)
        self.assertEqual(payload["quarterlyGrid"]["balanceN"], 2)
        self.assertEqual(payload["quarterlyGrid"]["pairedStockIds"], ["2222"])

    def test_market_output_dates_must_be_unique(self):
        with self.assertRaises(res.ResearchEventScanError):
            res.compute_census(
                {"1111"},
                {
                    "twse": [
                        announcement("1111"),
                        announcement("1111", output="1150808"),
                    ],
                    "tpex": [announcement("1111", tpex=True)],
                },
                [],
                [],
                window_start=dt.date(2026, 8, 6),
                window_end=dt.date(2026, 8, 7),
                quarter_year="115",
                quarter="2",
            )


if __name__ == "__main__":
    unittest.main()
