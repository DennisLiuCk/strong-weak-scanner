#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""唯讀稽核正式 SQLite 的五張原始表與 market_index。

退出碼：0=五表完整且公式正確（可含非阻斷 warning）、1=資料契約失敗、2=參數／檔案錯誤。
預設 universe 來自 config/universe.csv；交易日 spine 使用該 universe 的 price ∪ market。
"""
import argparse
import csv
import json
import sqlite3
import sys
from datetime import date
from pathlib import Path

import fetch_daily as fd


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "data" / "findmind.db"
DEFAULT_UNIVERSE = ROOT / "config" / "universe.csv"
TABLE_ORDER = tuple(fd.DATASET_TABLE[dataset] for dataset in fd.DATASETS)
MAX_SAMPLES = 10


def load_universe_ids(path=DEFAULT_UNIVERSE):
    with Path(path).open(encoding="utf-8") as handle:
        ids = [row["stock_id"].strip() for row in csv.DictReader(handle)
               if row.get("stock_id", "").strip()]
    return list(dict.fromkeys(ids))


def open_readonly(path):
    db_path = Path(path).resolve()
    if not db_path.is_file():
        raise FileNotFoundError(db_path)
    con = sqlite3.connect(f"{db_path.as_uri()}?mode=ro", uri=True)
    con.execute("PRAGMA query_only=ON")
    return con


def _table_exists(con, table):
    return con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)
    ).fetchone() is not None


def _table_columns(con, table):
    return {row[1] for row in con.execute(f'PRAGMA table_info("{table}")')}


def _in_bounds(value, start, end):
    return (not start or value >= start) and (not end or value <= end)


def _scope_dates(con, stock_ids, start, end):
    dates = set()
    if _table_exists(con, "price") and stock_ids:
        marks = ",".join("?" for _ in stock_ids)
        dates.update(row[0] for row in con.execute(
            f"SELECT DISTINCT date FROM price WHERE stock_id IN ({marks})", stock_ids))
    if _table_exists(con, "market"):
        dates.update(row[0] for row in con.execute("SELECT date FROM market"))
    return {day for day in dates if day and _in_bounds(day, start, end)}


def _raw_rows(con, table, stock_ids, first, last, columns):
    marks = ",".join("?" for _ in stock_ids)
    selected = ",".join(f'"{column}"' for column in columns)
    return con.execute(
        f"""SELECT date,stock_id,{selected} FROM "{table}"
            WHERE stock_id IN ({marks}) AND date BETWEEN ? AND ?""",
        (*stock_ids, first, last)).fetchall()


def _pair_text(pair):
    return f"{pair[0]}/{pair[1]}"


def _check_formula(report, raw_maps, name, table, columns, predicate):
    mismatches = []
    for pair, values in raw_maps.get(table, {}).items():
        selected = [values[column] for column in columns]
        if any(value is None for value in selected):
            continue
        if not predicate(*selected):
            mismatches.append(_pair_text(pair))
    report["invariants"][name] = {
        "mismatches": len(mismatches),
        "samples": mismatches[:MAX_SAMPLES],
    }
    if mismatches:
        report["errors"].append(f"{name} 公式不符 {len(mismatches)} 筆")


def _audit_market_index(con, dates, report):
    columns = {"date", "market", "index_key", "index_type", "close"}
    if not _table_exists(con, "market_index"):
        report["warnings"].append("market_index 不存在（觀察層、非阻斷）")
        return
    missing_columns = columns - _table_columns(con, "market_index")
    if missing_columns:
        report["warnings"].append(
            f"market_index 缺欄 {','.join(sorted(missing_columns))}（觀察層、非阻斷）")
        return
    first, last = min(dates), max(dates)
    rows = con.execute(
        """SELECT date,market,index_key,close FROM market_index
           WHERE date BETWEEN ? AND ?""", (first, last)).fetchall()
    twse_dates = {day for day, market, key, close in rows
                  if day in dates and market == "TWSE"
                  and key == fd.TWSE_TOTAL_RETURN_KEY and close is not None}
    latest_month = last[:7]
    tpex_expected = {day for day in dates if day[:7] == latest_month}
    tpex_dates = {day for day, market, key, close in rows
                  if day in tpex_expected and market == "TPEx"
                  and key == fd.TPEX_TOTAL_RETURN_KEY and close is not None}
    twse_missing = sorted(dates - twse_dates)
    tpex_missing = sorted(tpex_expected - tpex_dates)
    report["market_index"] = {
        "twse": {
            "complete_dates": len(twse_dates), "expected_dates": len(dates),
            "missing_dates": len(twse_missing), "samples": twse_missing[:MAX_SAMPLES],
        },
        "tpex_latest_month": {
            "month": latest_month, "complete_dates": len(tpex_dates),
            "expected_dates": len(tpex_expected), "missing_dates": len(tpex_missing),
            "samples": tpex_missing[:MAX_SAMPLES],
        },
    }
    if twse_missing:
        report["warnings"].append(
            f"TWSE market_index 缺 {len(twse_missing)} 個交易日（觀察層、非阻斷）")
    if tpex_missing:
        report["warnings"].append(
            f"TPEx market_index 最新月缺 {len(tpex_missing)} 個交易日（觀察層、非阻斷）")


def audit_connection(con, stock_ids, start=None, end=None):
    """回傳 JSON-safe 稽核報告；不建立 table、不更新任何資料。"""
    stock_ids = list(dict.fromkeys(stock_ids))
    report = {
        "ok": False,
        "integrity_check": None,
        "scope": {"stocks": len(stock_ids), "trading_dates": 0,
                  "expected_rows_per_table": 0, "start": start, "end": end},
        "tables": {},
        "invariants": {},
        "market_index": {},
        "warnings": [],
        "errors": [],
    }
    try:
        integrity = [row[0] for row in con.execute("PRAGMA integrity_check")]
    except sqlite3.Error as exc:
        integrity = [f"error:{exc}"]
    report["integrity_check"] = integrity
    if integrity != ["ok"]:
        report["errors"].append(f"SQLite integrity_check 失敗:{integrity[:MAX_SAMPLES]}")
    if not stock_ids:
        report["errors"].append("universe 為空")
        return report

    schema_ok = True
    for table in TABLE_ORDER:
        if not _table_exists(con, table):
            report["errors"].append(f"缺少原始表 {table}")
            schema_ok = False
            continue
        required = {"date", "stock_id", *fd.RAW_AUDIT_COLUMNS[table]}
        missing = required - _table_columns(con, table)
        if missing:
            report["errors"].append(f"{table} 缺欄 {','.join(sorted(missing))}")
            schema_ok = False
    if not schema_ok:
        return report

    dates = _scope_dates(con, stock_ids, start, end)
    if not dates:
        report["errors"].append("指定範圍找不到 price∪market 交易日")
        return report
    first, last = min(dates), max(dates)
    expected_pairs = {(day, sid) for day in dates for sid in stock_ids}
    expected_count = len(expected_pairs)
    report["scope"] = {
        "stocks": len(stock_ids), "trading_dates": len(dates),
        "expected_rows_per_table": expected_count, "start": first, "end": last,
    }

    raw_maps = {}
    for table in TABLE_ORDER:
        columns = fd.RAW_AUDIT_COLUMNS[table]
        expanded = set(fd.RAW_EXPANDED_COLUMNS[table])
        in_scope = {}
        off_spine = []
        for row in _raw_rows(con, table, stock_ids, first, last, columns):
            pair = (row[0], row[1])
            if row[0] not in dates:
                off_spine.append(pair)
                continue
            in_scope[pair] = dict(zip(columns, row[2:]))
        raw_maps[table] = in_scope
        missing_pairs = sorted(expected_pairs - set(in_scope))
        null_by_column = {
            column: sum(values[column] is None for values in in_scope.values())
            for column in columns
        }
        null_by_column = {key: value for key, value in null_by_column.items() if value}
        required_complete = sum(
            all(values[column] is not None for column in columns)
            for values in in_scope.values())
        expanded_complete = sum(
            all(values[column] is not None for column in expanded)
            for values in in_scope.values())
        report["tables"][table] = {
            "rows": len(in_scope), "expected_rows": expected_count,
            "required_complete_rows": required_complete,
            "expanded_complete_rows": expanded_complete,
            "missing_pairs": len(missing_pairs),
            "missing_samples": [_pair_text(pair) for pair in missing_pairs[:MAX_SAMPLES]],
            "null_by_column": null_by_column,
            "off_spine_rows": len(off_spine),
            "off_spine_dates": sorted({pair[0] for pair in off_spine})[:MAX_SAMPLES],
        }
        if missing_pairs:
            report["errors"].append(f"{table} 缺 {len(missing_pairs)} 個交易日×股票 pair")
        if null_by_column:
            detail = ",".join(f"{key}={value}" for key, value in null_by_column.items())
            report["errors"].append(f"{table} 必備欄為 NULL:{detail}")
        if off_spine:
            report["warnings"].append(
                f"{table} 有 {len(off_spine)} 筆不在 price∪market spine 的既有資料；"
                "保留但不列入完整度")

    _check_formula(report, raw_maps, "inst.foreign_net", "inst",
                   ("foreign_net", "foreign_buy", "foreign_sell"),
                   lambda net, buy, sell: net == buy - sell)
    _check_formula(report, raw_maps, "inst.trust_net", "inst",
                   ("trust_net", "trust_buy", "trust_sell"),
                   lambda net, buy, sell: net == buy - sell)
    _check_formula(report, raw_maps, "inst.dealer_self_net", "inst",
                   ("dealer_self_net", "dealer_self_buy", "dealer_self_sell"),
                   lambda net, buy, sell: net == buy - sell)
    _check_formula(report, raw_maps, "inst.dealer_hedge_net", "inst",
                   ("dealer_hedge_net", "dealer_hedge_buy", "dealer_hedge_sell"),
                   lambda net, buy, sell: net == buy - sell)
    _check_formula(report, raw_maps, "inst.dealer_net", "inst",
                   ("dealer_net", "dealer_self_net", "dealer_hedge_net"),
                   lambda total, self_net, hedge_net: total == self_net + hedge_net)
    _check_formula(report, raw_maps, "sbl.balance", "sbl",
                   ("sbl_bal", "sbl_prev_bal", "sbl_sell", "sbl_return",
                    "sbl_adjustment"),
                   lambda bal, prev, sell, returned, adjustment:
                   bal == prev + sell - returned + adjustment)
    _audit_market_index(con, dates, report)
    report["ok"] = not report["errors"]
    return report


def format_report(report):
    scope = report["scope"]
    lines = [
        f"SQLite integrity_check: {','.join(report['integrity_check'] or [])}",
        (f"稽核範圍: {scope['stocks']} 檔 × {scope['trading_dates']} 交易日 = "
         f"每表 {scope['expected_rows_per_table']} 筆 "
         f"({scope['start']} .. {scope['end']})"),
    ]
    for table in TABLE_ORDER:
        if table not in report["tables"]:
            continue
        item = report["tables"][table]
        lines.append(
            f"{table}: rows {item['rows']}/{item['expected_rows']} · "
            f"required {item['required_complete_rows']}/{item['expected_rows']} · "
            f"expanded {item['expanded_complete_rows']}/{item['expected_rows']}")
    for name, item in report["invariants"].items():
        lines.append(f"公式 {name}: mismatch {item['mismatches']}")
    if report["market_index"]:
        twse = report["market_index"]["twse"]
        tpex = report["market_index"]["tpex_latest_month"]
        lines.append(
            f"market_index TWSE: {twse['complete_dates']}/{twse['expected_dates']} 交易日")
        lines.append(
            f"market_index TPEx({tpex['month']}): "
            f"{tpex['complete_dates']}/{tpex['expected_dates']} 交易日")
    lines.extend(f"WARN {message}" for message in report["warnings"])
    lines.extend(f"ERROR {message}" for message in report["errors"])
    result = "PASS" if report["ok"] else "FAIL"
    lines.append(
        f"RESULT {result} · errors {len(report['errors'])} · warnings {len(report['warnings'])}")
    return "\n".join(lines)


def _iso_date(value):
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise argparse.ArgumentTypeError("日期必須是 YYYY-MM-DD") from exc


def main(argv=None):
    parser = argparse.ArgumentParser(description="唯讀稽核五張原始表、公式與 market_index")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="SQLite 路徑")
    parser.add_argument("--universe", default=str(DEFAULT_UNIVERSE), help="universe.csv 路徑")
    parser.add_argument("--stocks", help="逗號分隔；省略時使用 --universe 全部股票")
    parser.add_argument("--start", type=_iso_date, help="限制稽核起日 YYYY-MM-DD")
    parser.add_argument("--end", type=_iso_date, help="限制稽核迄日 YYYY-MM-DD")
    parser.add_argument("--json", action="store_true", help="輸出 machine-readable JSON")
    args = parser.parse_args(argv)
    if args.start and args.end and args.start > args.end:
        parser.error("--start 不可晚於 --end")
    try:
        stock_ids = ([item.strip() for item in args.stocks.split(",") if item.strip()]
                     if args.stocks else load_universe_ids(args.universe))
        con = open_readonly(args.db)
        try:
            report = audit_connection(con, stock_ids, args.start, args.end)
        finally:
            con.close()
    except (OSError, sqlite3.Error, ValueError) as exc:
        print(f"audit setup error:{exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(format_report(report))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
