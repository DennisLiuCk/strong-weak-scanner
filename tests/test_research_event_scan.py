# -*- coding: utf-8 -*-
import datetime as dt
import sys
import unittest
from pathlib import Path


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
