#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic, read-only TWSE/TPEx event and quarterly-grid census.

This tool only builds a reproducible trigger index. It never opens the project
database and cannot turn an OpenAPI row into verified filing content. Daily
announcement endpoints publish an output batch dated after the speech date, so
coverage is conservatively defined as the earlier market output date minus one
day. A requested window is full only when that derived boundary reaches the
window end for both markets.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import sys
import urllib.request
from pathlib import Path


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
DEFAULT_UNIVERSE = os.path.join(ROOT, "config", "universe.csv")

ENDPOINTS = {
    "twse_announcements": "https://openapi.twse.com.tw/v1/opendata/t187ap04_L",
    "tpex_announcements": "https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap04_O",
    "twse_income": "https://openapi.twse.com.tw/v1/opendata/t187ap06_L_ci",
    "tpex_income": "https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap06_O_ci",
    "twse_balance": "https://openapi.twse.com.tw/v1/opendata/t187ap07_L_ci",
    "tpex_balance": "https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap07_O_ci",
}


class ResearchEventScanError(ValueError):
    """Raised when an endpoint or official date cannot support a safe census."""


def _iso_date(value: str) -> dt.date:
    try:
        parsed = dt.date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise ResearchEventScanError(f"日期必須是 YYYY-MM-DD:{value or '-'}") from exc
    if parsed.isoformat() != value:
        raise ResearchEventScanError(f"日期必須是 YYYY-MM-DD:{value or '-'}")
    return parsed


def roc_date(value: str) -> dt.date:
    """Convert a seven-digit Minguo date such as 1150807 to 2026-08-07."""
    text = (value or "").strip()
    if len(text) != 7 or not text.isdigit():
        raise ResearchEventScanError(f"官方民國日期格式錯誤:{text or '-'}")
    try:
        return dt.date(int(text[:3]) + 1911, int(text[3:5]), int(text[5:7]))
    except ValueError as exc:
        raise ResearchEventScanError(f"官方民國日期無效:{text}") from exc


def load_universe(path: str = DEFAULT_UNIVERSE) -> set[str]:
    with open(path, encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    ids = {(row.get("stock_id") or "").strip() for row in rows}
    ids.discard("")
    if not ids:
        raise ResearchEventScanError(f"universe 無股票:{path}")
    if len(ids) != len(rows):
        raise ResearchEventScanError(f"universe stock_id 缺漏或重複:{path}")
    return ids


def _stock_id(row: dict) -> str:
    return (row.get("公司代號") or row.get("SecuritiesCompanyCode") or "").strip()


def _output_date(row: dict) -> dt.date:
    return roc_date(row.get("出表日期") or row.get("Date") or "")


def _speech_date(row: dict) -> dt.date:
    return roc_date(row.get("發言日期") or "")


def _quarter_value(row: dict, twse_key: str, tpex_key: str) -> str:
    return (row.get(twse_key) or row.get(tpex_key) or "").strip()


def fetch_json(url: str, timeout: float = 30.0) -> list[dict]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "strong-weak-scanner-research-event-scan/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.load(response)
    except Exception as exc:  # urllib exposes several platform-specific failures.
        raise ResearchEventScanError(f"官方端點失敗:{url}:{exc}") from exc
    if not isinstance(payload, list):
        raise ResearchEventScanError(f"官方端點不是 JSON array:{url}")
    return payload


def compute_census(
    universe_ids: set[str],
    announcements_by_market: dict[str, list[dict]],
    income_rows: list[dict],
    balance_rows: list[dict],
    *,
    window_start: dt.date,
    window_end: dt.date,
    quarter_year: str,
    quarter: str,
) -> dict:
    if window_start > window_end:
        raise ResearchEventScanError("window_start 不可晚於 window_end")
    if set(announcements_by_market) != {"twse", "tpex"}:
        raise ResearchEventScanError("重大訊息必須同時提供 twse 與 tpex")

    output_dates: dict[str, str] = {}
    coverage_through: dict[str, str] = {}
    observed_speech: dict[str, list[str]] = {}
    batch_covers_window: dict[str, bool] = {}
    announcement_rows: list[dict] = []
    market_source_rows: dict[str, int] = {}
    for market, rows in announcements_by_market.items():
        if not rows:
            raise ResearchEventScanError(f"{market} 重大訊息端點回傳空陣列，無法判定覆蓋")
        dates = {_output_date(row) for row in rows}
        if len(dates) != 1:
            shown = ",".join(sorted(item.isoformat() for item in dates))
            raise ResearchEventScanError(f"{market} 重大訊息出表日期不唯一:{shown}")
        output_date = dates.pop()
        through = output_date - dt.timedelta(days=1)
        output_dates[market] = output_date.isoformat()
        coverage_through[market] = through.isoformat()
        market_source_rows[market] = len(rows)
        # The daily batch is non-retentive: it carries a single speech date and is
        # replaced when the output date rolls forward. Date arithmetic alone would
        # certify a window using a batch that never contained any of its days, so
        # coverage also requires that the batch actually carries in-window content.
        speech_dates = sorted({_speech_date(row) for row in rows})
        observed_speech[market] = [item.isoformat() for item in speech_dates]
        batch_covers_window[market] = any(
            window_start <= item <= window_end for item in speech_dates
        )
        for row in rows:
            stock_id = _stock_id(row)
            speech = _speech_date(row)
            if stock_id in universe_ids and window_start <= speech <= window_end:
                announcement_rows.append({
                    "market": market,
                    "stockId": stock_id,
                    "speechDate": speech.isoformat(),
                    "outputDate": output_date.isoformat(),
                })

    def quarterly_ids(rows: list[dict]) -> set[str]:
        return {
            _stock_id(row)
            for row in rows
            if _stock_id(row) in universe_ids
            and _quarter_value(row, "年度", "Year") == quarter_year
            and _quarter_value(row, "季別", "Season") == quarter
        }

    income_ids = quarterly_ids(income_rows)
    balance_ids = quarterly_ids(balance_rows)
    paired_ids = sorted(income_ids & balance_ids)
    reached_window_end = all(
        dt.date.fromisoformat(value) >= window_end
        for value in coverage_through.values()
    )
    carries_window = all(batch_covers_window.values())
    complete = reached_window_end and carries_window
    if not reached_window_end:
        limitation = (
            "重大訊息日批次尚未覆蓋 window_end；不得把目前 0 列或最新發言日當成最終結果"
        )
    elif not carries_window:
        limitation = (
            "重大訊息日批次已滾過本窗口且不保留舊發言日，本次讀到的批次不含窗內任何一天；"
            "缺口不能由這次重跑關閉，必須沿用當時真的讀到該日的既有 scan row"
        )
    else:
        limitation = (
            "full 只涵蓋兩市場重大訊息日批次與指定季度兩張數值表，不含附件內容或全市場語意"
        )
    speech_dates = sorted({row["speechDate"] for row in announcement_rows})
    return {
        "schemaVersion": 1,
        "windowStart": window_start.isoformat(),
        "windowEnd": window_end.isoformat(),
        "population": {
            "kind": "universe_census",
            "universeN": len(universe_ids),
            "inferentialSample": False,
        },
        "coverage": {
            "scope": "full" if complete else "partial",
            "complete": complete,
            "rule": (
                "each_market_output_date_minus_one_day_reaches_window_end"
                "_and_batch_speech_dates_fall_inside_window"
            ),
            "announcementOutputDates": output_dates,
            "announcementCoverageThrough": coverage_through,
            "observedSpeechDatesByMarket": observed_speech,
            "batchCoversWindowByMarket": batch_covers_window,
            "limitation": limitation,
        },
        "announcements": {
            "rowsInUniverseWindow": len(announcement_rows),
            "stockIds": sorted({row["stockId"] for row in announcement_rows}),
            "speechDates": speech_dates,
            "sourceRowsByMarket": market_source_rows,
        },
        "quarterlyGrid": {
            "year": quarter_year,
            "quarter": quarter,
            "incomeN": len(income_ids),
            "balanceN": len(balance_ids),
            "pairedN": len(paired_ids),
            "pairedStockIds": paired_ids,
            "boundary": "OpenAPI 數值列只是申報 trigger，不是完整附件、附註或內容驗證",
        },
    }


def run_scan(
    *,
    universe_path: str,
    window_start: dt.date,
    window_end: dt.date,
    quarter_year: str,
    quarter: str,
    timeout: float,
) -> dict:
    payloads = {name: fetch_json(url, timeout) for name, url in ENDPOINTS.items()}
    return compute_census(
        load_universe(universe_path),
        {
            "twse": payloads["twse_announcements"],
            "tpex": payloads["tpex_announcements"],
        },
        payloads["twse_income"] + payloads["tpex_income"],
        payloads["twse_balance"] + payloads["tpex_balance"],
        window_start=window_start,
        window_end=window_end,
        quarter_year=quarter_year,
        quarter=quarter,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="唯讀重跑 TWSE／TPEx 重大訊息與季度兩表 universe census")
    parser.add_argument("--window-start", required=True)
    parser.add_argument("--window-end", required=True)
    parser.add_argument("--quarter-year", required=True, help="民國年，例如 115")
    parser.add_argument("--quarter", required=True, choices=("1", "2", "3", "4"))
    parser.add_argument("--universe", default=DEFAULT_UNIVERSE)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--output")
    parser.add_argument("--require-full", action="store_true")
    args = parser.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    try:
        payload = run_scan(
            universe_path=args.universe,
            window_start=_iso_date(args.window_start),
            window_end=_iso_date(args.window_end),
            quarter_year=args.quarter_year,
            quarter=args.quarter,
            timeout=args.timeout,
        )
    except (OSError, ResearchEventScanError) as exc:
        print(f"ERROR：{exc}")
        return 1
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
        print(f"已寫入 {output}")
    else:
        print(text, end="")
    if args.require_full and not payload["coverage"]["complete"]:
        print("ERROR：來源批次尚未覆蓋 window_end，scope 必須維持 partial")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
