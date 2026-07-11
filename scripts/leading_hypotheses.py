#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""領先假說報告的載入與品質檢查（純 stdlib）。"""
import argparse
import datetime as dt
import glob
import os
import re
import sys

from qual_notes import _extract_sections, _parse_meta_details, _today, load_notes, note_review_status

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(ROOT, "notes", "leading_hypotheses")
NOTES_DIR = os.path.join(ROOT, "notes", "qualitative")
REPORT_VERSION = 1
REPORT_STATUSES = {"active_monitoring", "closed"}
HYPOTHESIS_STATUSES = {
    "management_quoted",
    "consistent_unconfirmed",
    "plausible_lead",
    "attribution_error",
    "unsupported_specificity",
    "contradicted",
    "resolved",
}
REQUIRED_FIELDS = (
    "市場主張", "首次捕捉", "來源層級", "目前狀態", "正式資料基準",
    "可證偽條件", "下次驗證", "研究判讀", "來源",
)
META_RE = re.compile(r"<!--\s*meta\s*(.*?)-->", re.S | re.I)
HYP_RE = re.compile(r"^##\s+(H\d+)\s*[｜|]\s*(.+?)\s*$", re.M)
FIELD_RE = re.compile(r"^-\s+\*\*(.+?)：\*\*\s*(.*?)\s*$", re.M)
URL_RE = re.compile(r"https://[^\s)>]+")


def _valid_date(value):
    try:
        dt.date.fromisoformat(value)
        return True
    except (TypeError, ValueError):
        return False


def _hypotheses(text):
    matches = list(HYP_RE.finditer(text))
    out = []
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[match.end():end]
        fields = {key.strip(): value.strip() for key, value in FIELD_RE.findall(body)}
        out.append({"id": match.group(1), "title": match.group(2).strip(), "fields": fields})
    return out


def analyse_report(path, text, notes=None, today=None):
    meta, errors = _parse_meta_details(text)
    warnings = []
    today = today or _today().isoformat()
    sid_from_name = os.path.basename(path).split("_", 1)[0]
    sid = meta.get("stock_id") or sid_from_name
    if not re.fullmatch(r"\d{4}", sid or ""):
        errors.append("stock_id 必須是四位數字")
    if sid != sid_from_name:
        errors.append(f"檔名 stock_id {sid_from_name} 與 meta {sid} 不一致")
    try:
        version = int(meta.get("report_version", "0"))
    except ValueError:
        version = 0
    if version != REPORT_VERSION:
        errors.append(f"report_version 必須是 {REPORT_VERSION}")
    if meta.get("status") not in REPORT_STATUSES:
        errors.append(f"非法 status：{meta.get('status') or '-'}")
    for field in ("last_updated", "content_as_of", "next_review"):
        value = meta.get(field, "")
        if not _valid_date(value):
            errors.append(f"{field} 缺少合法 YYYY-MM-DD 日期")
    for field in ("last_updated", "content_as_of"):
        if _valid_date(meta.get(field, "")) and meta[field] > today:
            errors.append(f"{field} 不可晚於今天 {today}")

    notes = notes if notes is not None else load_notes(NOTES_DIR)
    note = notes.get(sid)
    if not note or note_review_status(note) != "independently_verified":
        errors.append("領先假說只可建立於有效 independently_verified 正式筆記")
    else:
        expected = note.get("reviewed_content_sha256") or ""
        anchored = meta.get("formal_note_content_sha256", "").lower()
        if anchored != expected:
            errors.append("formal_note_content_sha256 與目前正式筆記不一致，必須重新對照")

    hypotheses = _hypotheses(text)
    if not hypotheses:
        errors.append("至少需要一則 H# 領先假說")
    ids = [hypothesis["id"] for hypothesis in hypotheses]
    if ids != [f"H{i}" for i in range(1, len(ids) + 1)]:
        errors.append("假說編號必須從 H1 起連續排列")
    for hypothesis in hypotheses:
        fields = hypothesis["fields"]
        missing = [field for field in REQUIRED_FIELDS if not fields.get(field)]
        if missing:
            errors.append(f"{hypothesis['id']} 缺少欄位：{', '.join(missing)}")
        status_match = re.search(r"`([a-z_]+)`", fields.get("目前狀態", ""))
        status = status_match.group(1) if status_match else fields.get("目前狀態", "").split()[0].strip("`。")
        if status and status not in HYPOTHESIS_STATUSES:
            errors.append(f"{hypothesis['id']} 非法目前狀態：{status}")
        captured = fields.get("首次捕捉", "")[:10]
        if captured and not _valid_date(captured):
            errors.append(f"{hypothesis['id']} 首次捕捉必須以 YYYY-MM-DD 開頭")
        if fields.get("來源") and not URL_RE.search(fields["來源"]):
            errors.append(f"{hypothesis['id']} 來源必須至少包含一個 HTTPS URL")
        if status == "attribution_error" and "歸因" not in fields.get("研究判讀", ""):
            warnings.append(f"{hypothesis['id']} 為 attribution_error，研究判讀宜明示歸因問題")

    return {
        "path": path,
        "relpath": os.path.relpath(path, ROOT).replace("\\", "/"),
        "stock_id": sid,
        "report_version": version,
        "status": meta.get("status"),
        "last_updated": meta.get("last_updated"),
        "content_as_of": meta.get("content_as_of"),
        "next_review": meta.get("next_review"),
        "formal_note_content_sha256": meta.get("formal_note_content_sha256"),
        "hypotheses": hypotheses,
        "hypothesis_count": len(hypotheses),
        "sections": _extract_sections(text),
        "quality_invalid": bool(errors),
        "quality_errors": errors,
        "quality_warnings": warnings,
    }


def load_reports(reports_dir=REPORTS_DIR, notes=None):
    out = {}
    if not os.path.isdir(reports_dir):
        return out
    notes = notes if notes is not None else load_notes(NOTES_DIR)
    for path in sorted(glob.glob(os.path.join(reports_dir, "*.md"))):
        if os.path.basename(path).startswith("_"):
            continue
        with open(path, encoding="utf-8") as handle:
            info = analyse_report(path, handle.read(), notes=notes)
        sid = info["stock_id"]
        if sid in out:
            info["quality_errors"].append(f"stock_id {sid} 有重複領先假說報告")
            info["quality_invalid"] = True
            out[sid]["quality_errors"].append(f"stock_id {sid} 有重複領先假說報告")
            out[sid]["quality_invalid"] = True
        else:
            out[sid] = info
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description="領先假說報告品質檢查")
    parser.add_argument("--lint", action="store_true")
    parser.add_argument("stock_id", nargs="?")
    args = parser.parse_args(argv)
    reports = load_reports()
    if args.stock_id:
        reports = {sid: report for sid, report in reports.items() if sid == args.stock_id}
    errors = 0
    for sid, report in reports.items():
        state = "ERROR" if report["quality_invalid"] else "OK"
        print(f"{state} {sid}：{report['hypothesis_count']} 則領先假說")
        for error in report["quality_errors"]:
            print(f"  - {error}")
            errors += 1
        for warning in report["quality_warnings"]:
            print(f"  ! {warning}")
    if not reports:
        print("沒有符合條件的領先假說報告")
        return 1
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
