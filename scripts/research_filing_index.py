#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Read-only MOPS filing-index check for explicitly selected research targets.

The company IR page and the MOPS OpenAPI grids are discovery triggers.  This
tool checks the direct ``t57sb01`` document index and records the filename,
upload time, and size without downloading or interpreting the filing itself.
It therefore cannot replace an evidence pack or an independent reviewer.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
UNIVERSE_PATH = os.path.join(ROOT, "config", "universe.csv")
MOPS_INDEX_URL = "https://doc.twse.com.tw/server-java/t57sb01"
SEASON_LABELS = {1: "第一季", 2: "第二季", 3: "第三季", 4: "第四季"}
FILENAME_RE = re.compile(r"^\d{6}_\d+_[A-Z0-9]+\.pdf$", re.IGNORECASE)


class FilingIndexError(ValueError):
    """Raised when input or the official index response violates the contract."""


class _TableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rows: list[list[str]] = []
        self._row: list[str] | None = None
        self._cell: list[str] | None = None

    def handle_starttag(self, tag: str, attrs) -> None:
        del attrs
        if tag.lower() == "tr":
            self._row = []
        elif tag.lower() in {"td", "th"} and self._row is not None:
            self._cell = []

    def handle_data(self, data: str) -> None:
        if self._cell is not None:
            self._cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"td", "th"} and self._row is not None and self._cell is not None:
            value = " ".join("".join(self._cell).replace("\xa0", " ").split())
            self._row.append(value)
            self._cell = None
        elif tag == "tr" and self._row is not None:
            self.rows.append(self._row)
            self._row = None
            self._cell = None


def load_universe(path: str = UNIVERSE_PATH) -> dict[str, str]:
    with open(path, encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    universe = {
        (row.get("stock_id") or "").strip(): (row.get("name") or "").strip()
        for row in rows
        if (row.get("stock_id") or "").strip()
    }
    if not universe:
        raise FilingIndexError(f"universe 為空:{path}")
    return universe


def parse_stock_ids(value: str, universe: dict[str, str]) -> list[str]:
    stock_ids = [item.strip() for item in value.split(",") if item.strip()]
    if not stock_ids:
        raise FilingIndexError("--stock-ids 至少要有一個代號")
    if len(stock_ids) != len(set(stock_ids)):
        raise FilingIndexError("--stock-ids 不可重複")
    invalid = [item for item in stock_ids if not re.fullmatch(r"\d{4,6}", item)]
    if invalid:
        raise FilingIndexError(f"股票代號格式錯誤:{','.join(invalid)}")
    unknown = [item for item in stock_ids if item not in universe]
    if unknown:
        raise FilingIndexError(f"股票不在 universe:{','.join(unknown)}")
    return stock_ids


def parse_filing_index_html(
    html: str, *, stock_id: str, year: int, season: int,
) -> list[dict[str, object]]:
    parser = _TableParser()
    parser.feed(html)
    if "查無所需資料" in html:
        return []
    has_filing_header = any(
        "證券代號" in cells and "電子檔案" in cells and "上傳日期" in cells
        for cells in parser.rows
    )
    if not has_filing_header:
        raise FilingIndexError(f"{stock_id} MOPS 回應不是可辨識的財報索引或查無資料頁")
    expected_period = f"{year} 年 {SEASON_LABELS[season]}"
    filings: list[dict[str, object]] = []
    for cells in parser.rows:
        if len(cells) < 11 or cells[0] != stock_id or cells[1] != expected_period:
            continue
        filename = cells[7]
        if not FILENAME_RE.fullmatch(filename):
            continue
        size_text = cells[8].replace(",", "")
        if not size_text.isdigit():
            raise FilingIndexError(f"{stock_id} 檔案大小不可解析:{cells[8] or '-'}")
        uploaded_at = cells[9]
        if not re.fullmatch(r"\d{3}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}", uploaded_at):
            raise FilingIndexError(f"{stock_id} 上傳時間不可解析:{uploaded_at or '-'}")
        filings.append({
            "filename": filename,
            "fileType": cells[5],
            "sizeBytes": int(size_text),
            "uploadedAtRoc": uploaded_at,
            "correctionStatus": cells[10],
            "downloadUrl": (
                f"{MOPS_INDEX_URL}?" + urllib.parse.urlencode({
                    "step": "9", "kind": "A", "co_id": stock_id,
                    "filename": filename,
                })
            ),
        })
    return filings


def build_index_url(stock_id: str, year: int, season: int) -> str:
    return f"{MOPS_INDEX_URL}?" + urllib.parse.urlencode({
        "step": "1",
        "colorchg": "1",
        "co_id": stock_id,
        "year": str(year),
        "seamon": str(season),
        "mtype": "A",
    })


def fetch_index(stock_id: str, year: int, season: int, timeout: float) -> tuple[str, str]:
    url = build_index_url(stock_id, year, season)
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "strong-weak-scanner-research/1.0",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = response.read()
        charset = response.headers.get_content_charset() or "big5"
    try:
        return url, payload.decode(charset)
    except (LookupError, UnicodeDecodeError) as exc:
        raise FilingIndexError(f"{stock_id} MOPS 回應無法以 {charset} 解碼") from exc


def build_report(
    *, stock_ids: list[str], universe: dict[str, str], year: int, season: int,
    checked_at: dt.date, timeout: float, delay_ms: int,
) -> dict[str, object]:
    results = []
    for offset, stock_id in enumerate(stock_ids):
        if offset and delay_ms:
            time.sleep(delay_ms / 1000)
        index_url, html = fetch_index(stock_id, year, season, timeout)
        filings = parse_filing_index_html(
            html, stock_id=stock_id, year=year, season=season,
        )
        chinese_report = next(
            (item for item in filings if str(item["filename"]).upper().endswith("_AI1.PDF")),
            None,
        )
        results.append({
            "stockId": stock_id,
            "name": universe[stock_id],
            "indexUrl": index_url,
            "found": bool(filings),
            "hasChineseConsolidatedReport": chinese_report is not None,
            "filings": filings,
        })
    found = [item["stockId"] for item in results if item["found"]]
    missing = [item["stockId"] for item in results if not item["found"]]
    return {
        "schemaVersion": 1,
        "checkedAt": checked_at.isoformat(),
        "yearRoc": year,
        "season": season,
        "scope": "explicit_stock_ids",
        "source": MOPS_INDEX_URL,
        "boundary": (
            "索引只證明檔案在 checkedAt 可取得；不證明內容、會計師結論、附註或研究主張"
            "已經 evidence pack 與獨立 reviewer 驗證。"
        ),
        "requested": len(stock_ids),
        "found": len(found),
        "missing": len(missing),
        "foundStockIds": found,
        "missingStockIds": missing,
        "results": results,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="逐檔查 MOPS t57sb01 正式財報附件索引（唯讀）",
    )
    parser.add_argument("--stock-ids", required=True, help="逗號分隔的 universe 股票代號")
    parser.add_argument("--year", required=True, type=int, help="民國年度，例如 115")
    parser.add_argument("--season", required=True, type=int, choices=range(1, 5))
    parser.add_argument("--checked-at", required=True, help="研究日 YYYY-MM-DD")
    parser.add_argument("--timeout", type=float, default=15.0, help="每檔 HTTP timeout 秒數")
    parser.add_argument("--delay-ms", type=int, default=150, help="逐檔請求間隔毫秒")
    parser.add_argument("--output", help="UTF-8 JSON 輸出；省略則以 ASCII-safe JSON 印 stdout")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        checked_at = dt.date.fromisoformat(args.checked_at)
        if checked_at.isoformat() != args.checked_at:
            raise ValueError
    except ValueError:
        print("--checked-at 必須是 YYYY-MM-DD", file=sys.stderr)
        return 2
    if args.timeout <= 0 or args.delay_ms < 0:
        print("--timeout 必須大於 0；--delay-ms 不可小於 0", file=sys.stderr)
        return 2
    try:
        universe = load_universe()
        stock_ids = parse_stock_ids(args.stock_ids, universe)
        report = build_report(
            stock_ids=stock_ids,
            universe=universe,
            year=args.year,
            season=args.season,
            checked_at=checked_at,
            timeout=args.timeout,
            delay_ms=args.delay_ms,
        )
    except (FilingIndexError, OSError) as exc:
        print(f"research filing index failed: {exc}", file=sys.stderr)
        return 2

    if args.output:
        output_path = os.path.abspath(args.output)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(report, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        print(f"output: {os.path.relpath(output_path, ROOT)}")
    else:
        print(json.dumps(report, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
