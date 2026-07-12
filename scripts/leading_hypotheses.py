#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""領先假說報告的載入與品質檢查（純 stdlib）。"""
import argparse
import datetime as dt
import glob
import os
import re
import sys
from urllib.parse import urlparse

from qual_notes import _extract_sections, _parse_meta_details, _today, load_notes, note_review_status

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(ROOT, "notes", "leading_hypotheses")
NOTES_DIR = os.path.join(ROOT, "notes", "qualitative")
REPORT_VERSION = 2
REPORT_STATUSES = {"active_monitoring", "closed"}
CAPTURE_MODES = {"retrospective", "prospective"}
LIFECYCLES = {"open", "confirmed", "refuted", "expired_unresolved"}
TERMINAL_LIFECYCLES = {"confirmed", "refuted", "expired_unresolved"}
EVIDENCE_STRENGTHS = {"weak", "medium", "strong"}
EVIDENCE_FLAGS = {
    "none", "attribution_error", "unsupported_specificity",
    "anonymous_source", "relay_only",
}
SOURCE_TYPES = {
    "official_company", "management_direct", "management_relay", "broker_relay",
    "media_report", "anonymous_supply_chain", "social_post", "self_media", "mixed",
}
HYPOTHESIS_META_FIELDS = (
    "source_published_at", "research_captured_at", "capture_mode", "lifecycle",
    "evidence_strength", "evidence_flags", "source_type", "source_publishers",
    "source_accessed_at", "source_chain_ids", "independent_chain_count", "review_due",
)
HYPOTHESIS_STATUS_INFO = {
    "management_quoted": {
        "label": "管理層說法・待驗證", "stage": "持續觀察", "order": 10, "terminal": False,
        "description": "具名管理層談話或媒體轉述，尚未由正式文件或實績完成核對。",
    },
    "consistent_unconfirmed": {
        "label": "方向相符・細節待證", "stage": "持續觀察", "order": 20, "terminal": False,
        "description": "方向與正式資料一致，但客戶、數量、占比或時程仍未證實。",
    },
    "plausible_lead": {
        "label": "合理線索・證據不足", "stage": "持續觀察", "order": 30, "terminal": False,
        "description": "產業邏輯合理且可驗證，目前仍缺少足夠的公司層級證據。",
    },
    "attribution_error": {
        "label": "歸因錯置", "stage": "證據警示", "order": 40, "terminal": False,
        "description": "把產業、客戶或供應鏈數字錯誤歸因為這家公司本身。",
    },
    "unsupported_specificity": {
        "label": "精確細節無法核實", "stage": "證據警示", "order": 50, "terminal": False,
        "description": "客戶名、台數、單價、占比或時程過度精確，但原始依據不可追溯。",
    },
    "contradicted": {
        "label": "已驗證不成立", "stage": "驗證終態", "order": 70, "terminal": True,
        "description": "較強、較新的正式證據已否定這則主張。",
    },
    "resolved": {
        "label": "已驗證成立", "stage": "驗證終態", "order": 60, "terminal": True,
        "description": "後續正式證據或可重算實績已證實這則主張。",
    },
    "expired_unresolved": {
        "label": "到期仍無法判定", "stage": "驗證終態", "order": 65, "terminal": True,
        "description": "觀察期限已過，但公開證據仍不足以判定成立或不成立。",
    },
}
HYPOTHESIS_STATUSES = set(HYPOTHESIS_STATUS_INFO)
REQUIRED_FIELDS = (
    "市場主張", "消息日期", "研究收錄", "來源層級", "目前狀態", "正式資料基準",
    "可證偽條件", "驗證期限", "下次驗證", "研究判讀", "來源",
)
META_RE = re.compile(r"<!--\s*meta\s*(.*?)-->", re.S | re.I)
HYP_RE = re.compile(r"^##\s+(H\d+)\s*[｜|]\s*(.+?)\s*$", re.M)
FIELD_RE = re.compile(r"^-\s+\*\*(.+?)：\*\*\s*(.*?)\s*$", re.M)
URL_RE = re.compile(r"https://[^\s)>]+")
HYP_META_RE = re.compile(r"<!--\s*hypothesis_meta\s*(.*?)-->", re.S | re.I)
TRANSITION_RE = re.compile(r"<!--\s*transition\s*(.*?)-->", re.S | re.I)


def _parse_comment_fields(body):
    out = {}
    for raw in body.strip().splitlines():
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        out[key.strip()] = value.strip()
    return out


def _csv_values(value):
    return [part.strip() for part in (value or "").split(",") if part.strip()]


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
        meta_match = HYP_META_RE.search(body)
        transitions = [_parse_comment_fields(item) for item in TRANSITION_RE.findall(body)]
        out.append({
            "id": match.group(1), "title": match.group(2).strip(), "fields": fields,
            "meta": _parse_comment_fields(meta_match.group(1)) if meta_match else {},
            "transitions": transitions,
        })
    return out


def _status_code(fields):
    raw = fields.get("目前狀態", "")
    match = re.search(r"`([a-z_]+)`", raw)
    return match.group(1) if match else raw.split()[0].strip("`。")


def _expected_lifecycle(status):
    if status == "resolved":
        return "confirmed"
    if status == "contradicted":
        return "refuted"
    if status == "expired_unresolved":
        return "expired_unresolved"
    return "open"


def _valid_https_url(url):
    parsed = urlparse(url.rstrip("。；,、"))
    return parsed.scheme == "https" and bool(parsed.hostname) and "." in parsed.hostname


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
    for field in ("last_updated", "content_as_of"):
        value = meta.get(field, "")
        if not _valid_date(value):
            errors.append(f"{field} 缺少合法 YYYY-MM-DD 日期")
    next_review = meta.get("next_review", "")
    if meta.get("status") == "active_monitoring" and not _valid_date(next_review):
        errors.append("active_monitoring 的 next_review 必須是 YYYY-MM-DD")
    if meta.get("status") == "closed" and next_review != "none":
        errors.append("closed 的 next_review 必須是 none")
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
    open_review_dates = []
    for hypothesis in hypotheses:
        fields = hypothesis["fields"]
        hmeta = hypothesis["meta"]
        transitions = hypothesis["transitions"]
        missing = [field for field in REQUIRED_FIELDS if not fields.get(field)]
        if missing:
            errors.append(f"{hypothesis['id']} 缺少欄位：{', '.join(missing)}")
        missing_meta = [field for field in HYPOTHESIS_META_FIELDS if not hmeta.get(field)]
        if missing_meta:
            errors.append(f"{hypothesis['id']} hypothesis_meta 缺少：{', '.join(missing_meta)}")
        status = _status_code(fields)
        if status and status not in HYPOTHESIS_STATUSES:
            errors.append(f"{hypothesis['id']} 非法目前狀態：{status}")
        elif status and HYPOTHESIS_STATUS_INFO[status]["label"] not in fields.get("目前狀態", ""):
            errors.append(
                f"{hypothesis['id']} 目前狀態須顯示中文名稱："
                f"{HYPOTHESIS_STATUS_INFO[status]['label']}"
            )
        published = hmeta.get("source_published_at", "")
        captured = hmeta.get("research_captured_at", "")
        accessed = hmeta.get("source_accessed_at", "")
        review_due = hmeta.get("review_due", "")
        for key, value in (("source_published_at", published),
                           ("research_captured_at", captured),
                           ("source_accessed_at", accessed)):
            if value and not _valid_date(value):
                errors.append(f"{hypothesis['id']} {key} 必須是 YYYY-MM-DD")
        if review_due != "none" and review_due and not _valid_date(review_due):
            errors.append(f"{hypothesis['id']} review_due 必須是 YYYY-MM-DD 或 none")
        if _valid_date(captured) and captured > today:
            errors.append(f"{hypothesis['id']} research_captured_at 不可晚於今天 {today}")
        if _valid_date(published) and _valid_date(captured) and published > captured:
            errors.append(f"{hypothesis['id']} source_published_at 不可晚於 research_captured_at")
        if _valid_date(accessed) and accessed != captured:
            errors.append(f"{hypothesis['id']} 初始 source_accessed_at 必須等於 research_captured_at")
        if fields.get("消息日期", "")[:10] != published:
            errors.append(f"{hypothesis['id']} 消息日期須與 source_published_at 一致")
        if fields.get("研究收錄", "")[:10] != captured:
            errors.append(f"{hypothesis['id']} 研究收錄須與 research_captured_at 一致")
        capture_label = "前瞻捕捉" if hmeta.get("capture_mode") == "prospective" else "回溯建檔"
        if hmeta.get("capture_mode") in CAPTURE_MODES and capture_label not in fields.get("研究收錄", ""):
            errors.append(f"{hypothesis['id']} 研究收錄須標示{capture_label}")
        visible_review_due = fields.get("驗證期限", "").split("。", 1)[0]
        if visible_review_due != review_due:
            errors.append(f"{hypothesis['id']} 驗證期限須與 review_due 一致")
        if hmeta.get("capture_mode") not in CAPTURE_MODES:
            errors.append(f"{hypothesis['id']} 非法 capture_mode：{hmeta.get('capture_mode') or '-'}")
        lifecycle = hmeta.get("lifecycle")
        if lifecycle not in LIFECYCLES:
            errors.append(f"{hypothesis['id']} 非法 lifecycle：{lifecycle or '-'}")
        elif status in HYPOTHESIS_STATUSES and lifecycle != _expected_lifecycle(status):
            errors.append(f"{hypothesis['id']} lifecycle 與目前狀態不一致")
        if hmeta.get("evidence_strength") not in EVIDENCE_STRENGTHS:
            errors.append(
                f"{hypothesis['id']} 非法 evidence_strength：{hmeta.get('evidence_strength') or '-'}"
            )
        if lifecycle in {"confirmed", "refuted"} and hmeta.get("evidence_strength") != "strong":
            errors.append(f"{hypothesis['id']} 成立或否定終態必須使用 strong evidence_strength")
        flags = _csv_values(hmeta.get("evidence_flags"))
        bad_flags = sorted(set(flags) - EVIDENCE_FLAGS)
        if not flags or bad_flags or ("none" in flags and len(flags) > 1):
            errors.append(f"{hypothesis['id']} 非法 evidence_flags：{hmeta.get('evidence_flags') or '-'}")
        if status in {"attribution_error", "unsupported_specificity"} and status not in flags:
            errors.append(f"{hypothesis['id']} {status} 必須同步列入 evidence_flags")
        if hmeta.get("source_type") not in SOURCE_TYPES:
            errors.append(f"{hypothesis['id']} 非法 source_type：{hmeta.get('source_type') or '-'}")
        chains = _csv_values(hmeta.get("source_chain_ids"))
        try:
            independent_count = int(hmeta.get("independent_chain_count", ""))
        except ValueError:
            independent_count = -1
        if not chains or len(chains) != len(set(chains)) or independent_count != len(chains):
            errors.append(f"{hypothesis['id']} independent_chain_count 必須等於唯一 source_chain_ids 數")
        if lifecycle == "open" and _valid_date(review_due):
            open_review_dates.append(review_due)
        if lifecycle == "open" and not _valid_date(review_due):
            errors.append(f"{hypothesis['id']} open lifecycle 的 review_due 必須是 YYYY-MM-DD")
        if lifecycle in TERMINAL_LIFECYCLES and review_due != "none":
            errors.append(f"{hypothesis['id']} 終態 review_due 必須是 none")
        urls = URL_RE.findall(fields.get("來源", ""))
        if fields.get("來源") and not urls:
            errors.append(f"{hypothesis['id']} 來源必須至少包含一個 HTTPS URL")
        for url in urls:
            if not _valid_https_url(url):
                errors.append(f"{hypothesis['id']} 來源 URL 無有效 HTTPS 主機：{url}")
        publishers = _csv_values(hmeta.get("source_publishers"))
        actual_publishers = sorted({urlparse(url.rstrip("。；,、")).hostname.lower()
                                    for url in urls if _valid_https_url(url)})
        if sorted(publishers) != actual_publishers:
            errors.append(f"{hypothesis['id']} source_publishers 須等於來源 URL 主機集合")
        if not transitions:
            errors.append(f"{hypothesis['id']} 至少需要一筆 transition 歷程")
        else:
            transition_dates = [item.get("date", "") for item in transitions]
            if any(not _valid_date(value) for value in transition_dates):
                errors.append(f"{hypothesis['id']} transition date 必須是 YYYY-MM-DD")
            if any(_valid_date(value) and value > today for value in transition_dates):
                errors.append(f"{hypothesis['id']} transition date 不可晚於今天 {today}")
            if transition_dates != sorted(transition_dates):
                errors.append(f"{hypothesis['id']} transition 必須依日期排序")
            if transition_dates and transition_dates[0] != captured:
                errors.append(f"{hypothesis['id']} 第一筆 transition date 必須等於 research_captured_at")
            if (transitions[0].get("evidence_published_at")
                    and transitions[0].get("evidence_published_at") != published):
                errors.append(
                    f"{hypothesis['id']} 第一筆 transition 證據發布日須等於 source_published_at"
                )
            if transitions[-1].get("to") != lifecycle:
                errors.append(f"{hypothesis['id']} 最後一筆 transition 必須對應目前 lifecycle")
            previous_to = None
            for transition_idx, item in enumerate(transitions):
                missing_transition = [key for key in (
                    "date", "from", "to", "reason", "evidence", "evidence_published_at",
                    "review_due",
                )
                                      if not item.get(key)]
                if missing_transition:
                    errors.append(
                        f"{hypothesis['id']} transition 缺少：{', '.join(missing_transition)}"
                    )
                if item.get("to") not in LIFECYCLES:
                    errors.append(f"{hypothesis['id']} transition to 非法：{item.get('to') or '-'}")
                transition_due = item.get("review_due", "")
                if item.get("to") == "open" and not _valid_date(transition_due):
                    errors.append(f"{hypothesis['id']} open transition review_due 必須是 YYYY-MM-DD")
                if item.get("to") in TERMINAL_LIFECYCLES and transition_due != "none":
                    errors.append(f"{hypothesis['id']} 終態 transition review_due 必須是 none")
                evidence_published_at = item.get("evidence_published_at", "")
                if evidence_published_at and not _valid_date(evidence_published_at):
                    errors.append(f"{hypothesis['id']} transition evidence_published_at 日期不合法")
                if (_valid_date(evidence_published_at) and _valid_date(item.get("date", ""))
                        and evidence_published_at > item["date"]):
                    errors.append(f"{hypothesis['id']} transition 證據發布日不可晚於轉移日")
                expected_from = "initial" if transition_idx == 0 else previous_to
                if item.get("from") != expected_from:
                    errors.append(f"{hypothesis['id']} transition from 未銜接上一狀態")
                if previous_to in TERMINAL_LIFECYCLES:
                    errors.append(f"{hypothesis['id']} 終態後不可再轉移")
                previous_to = item.get("to")
            if transitions[-1].get("review_due") != review_due:
                errors.append(f"{hypothesis['id']} 最後一筆 transition review_due 須對應目前值")
        if status == "attribution_error" and "歸因" not in fields.get("研究判讀", ""):
            warnings.append(f"{hypothesis['id']} 為 attribution_error，研究判讀宜明示歸因問題")

    if open_review_dates and meta.get("next_review") != min(open_review_dates):
        errors.append("report next_review 必須等於所有追蹤中假說最早的 review_due")
    if hypotheses:
        lifecycles = [item["meta"].get("lifecycle") for item in hypotheses]
        expected_report_status = "closed" if all(value in TERMINAL_LIFECYCLES
                                                  for value in lifecycles) else "active_monitoring"
        if meta.get("status") != expected_report_status:
            errors.append(f"report status 應為 {expected_report_status}")

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


def _infer_source_type(source_level):
    social = ("社群", "PTT", "論壇", "爆料", "個人貼文")
    self_media = ("自媒體", "投資網誌", "公開投資文章")
    official = ("公司正式", "公司年報", "年報管理層", "投資人簡報", "正式新聞稿")
    management = ("管理層", "法說", "股東會", "公司說法")
    broker = ("券商", "法人", "投顧")
    anonymous = ("匿名供應鏈", "匿名業界")
    if any(word in source_level for word in social):
        return "social_post"
    if any(word in source_level for word in self_media):
        return "self_media"
    if any(word in source_level for word in official):
        return "official_company"
    if any(word in source_level for word in anonymous):
        return "anonymous_supply_chain"
    has_management = any(word in source_level for word in management)
    has_broker = any(word in source_level for word in broker)
    if has_management and has_broker:
        return "mixed"
    if has_management:
        return "management_relay" if "轉述" in source_level or "媒體" in source_level else "management_direct"
    if has_broker:
        return "broker_relay"
    return "media_report"


def _infer_evidence_flags(status, source_level):
    flags = []
    if status in {"attribution_error", "unsupported_specificity"}:
        flags.append(status)
    if "匿名" in source_level:
        flags.append("anonymous_source")
    if any(word in source_level for word in ("轉述", "二手", "媒體", "轉載")):
        flags.append("relay_only")
    return flags or ["none"]


def _infer_evidence_strength(status):
    if status in {"resolved", "contradicted"}:
        return "strong"
    if status == "consistent_unconfirmed":
        return "medium"
    return "weak"


def migrate_report_text_v2(text):
    """把第一階段 v1 報告機械遷移為可前瞻稽核的 v2；不改寫主張內容。"""
    report_meta, _ = _parse_meta_details(text)
    try:
        version = int(report_meta.get("report_version", "0"))
    except ValueError:
        version = 0
    if version == REPORT_VERSION:
        return text
    if version != 1:
        raise ValueError(f"只支援 report_version 1 遷移，目前為 {version}")
    sid = report_meta.get("stock_id", "")
    captured_at = report_meta.get("last_updated", "")
    review_due = report_meta.get("next_review", "")
    matches = list(HYP_RE.finditer(text))
    migrated = text
    for idx in range(len(matches) - 1, -1, -1):
        match = matches[idx]
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[match.end():end]
        fields = {key.strip(): value.strip() for key, value in FIELD_RE.findall(body)}
        hid = match.group(1)
        status = _status_code(fields)
        published_at = fields.get("首次捕捉", "")[:10]
        source_level = fields.get("來源層級", "")
        urls = URL_RE.findall(fields.get("來源", ""))
        publishers = sorted({urlparse(url.rstrip("。；,、")).hostname.lower()
                             for url in urls if _valid_https_url(url)})
        chain_id = f"{sid}-{hid}-C1"
        lifecycle = _expected_lifecycle(status)
        hmeta = (
            "\n\n<!-- hypothesis_meta\n"
            f"source_published_at: {published_at}\n"
            f"research_captured_at: {captured_at}\n"
            "capture_mode: retrospective\n"
            f"lifecycle: {lifecycle}\n"
            f"evidence_strength: {_infer_evidence_strength(status)}\n"
            f"evidence_flags: {','.join(_infer_evidence_flags(status, source_level))}\n"
            f"source_type: {_infer_source_type(source_level)}\n"
            f"source_publishers: {','.join(publishers)}\n"
            f"source_accessed_at: {captured_at}\n"
            f"source_chain_ids: {chain_id}\n"
            "independent_chain_count: 1\n"
            f"review_due: {review_due}\n"
            "-->\n"
            "<!-- transition\n"
            f"date: {captured_at}\n"
            "from: initial\n"
            f"to: {lifecycle}\n"
            "reason: phase1_retrospective_baseline\n"
            f"evidence: source_chain:{chain_id}\n"
            f"evidence_published_at: {published_at}\n"
            f"review_due: {review_due}\n"
            "-->"
        )
        body = re.sub(
            r"^-\s+\*\*首次捕捉：\*\*\s*(.*?)$",
            lambda item: (
                f"- **消息日期：** {item.group(1)}\n"
                f"- **研究收錄：** {captured_at}（回溯建檔）。"
            ),
            body, count=1, flags=re.M,
        )
        body = re.sub(
            r"^(-\s+\*\*下次驗證：\*\*)",
            f"- **驗證期限：** {review_due}。\n\\1",
            body, count=1, flags=re.M,
        )
        migrated = migrated[:match.end()] + hmeta + body + migrated[end:]
    return re.sub(r"(?m)^report_version:\s*1\s*$", "report_version: 2", migrated, count=1)


def migrate_reports_v2(reports_dir=REPORTS_DIR):
    changed = []
    for path in sorted(glob.glob(os.path.join(reports_dir, "*.md"))):
        if os.path.basename(path).startswith("_"):
            continue
        with open(path, encoding="utf-8") as handle:
            before = handle.read()
        after = migrate_report_text_v2(before)
        if after == before:
            continue
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(after)
        changed.append(path)
    return changed


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


def due_hypotheses(reports, as_of):
    due = []
    for sid, report in reports.items():
        for hypothesis in report["hypotheses"]:
            visible = [item for item in hypothesis["transitions"]
                       if _valid_date(item.get("date", "")) and item["date"] <= as_of]
            if not visible:
                continue
            current = visible[-1]
            if (current.get("to") == "open" and _valid_date(current.get("review_due", ""))
                    and current["review_due"] <= as_of):
                due.append((current["review_due"], sid, hypothesis["id"], hypothesis["title"]))
    return sorted(due)


def prospective_metrics(reports, as_of):
    as_of_date = dt.date.fromisoformat(as_of)
    cohort = []
    for sid, report in reports.items():
        for hypothesis in report["hypotheses"]:
            hmeta = hypothesis["meta"]
            captured = hmeta.get("research_captured_at", "")
            if (hmeta.get("capture_mode") == "prospective" and _valid_date(captured)
                    and captured <= as_of):
                visible_transitions = [item for item in hypothesis["transitions"]
                                       if _valid_date(item.get("date", ""))
                                       and item["date"] <= as_of]
                terminal = next((item for item in reversed(visible_transitions)
                                 if item.get("to") in TERMINAL_LIFECYCLES), None)
                cohort.append({"sid": sid, "hypothesis": hypothesis, "meta": hmeta,
                               "captured": dt.date.fromisoformat(captured), "terminal": terminal,
                               "lifecycle_as_of": (visible_transitions[-1].get("to")
                                                    if visible_transitions else "open")})
    lifecycle_counts = {key: 0 for key in sorted(LIFECYCLES)}
    for item in cohort:
        lifecycle = item["lifecycle_as_of"]
        lifecycle_counts[lifecycle] = lifecycle_counts.get(lifecycle, 0) + 1
    windows = {}
    for days in (30, 60, 90):
        eligible = [item for item in cohort if (as_of_date - item["captured"]).days >= days]
        resolved = 0
        for item in eligible:
            terminal = item["terminal"]
            if terminal and _valid_date(terminal.get("date", "")):
                terminal_date = dt.date.fromisoformat(terminal["date"])
                if (terminal_date - item["captured"]).days <= days:
                    resolved += 1
        windows[days] = {"eligible": len(eligible), "terminal": resolved}
    lead_days = []
    for item in cohort:
        terminal = item["terminal"]
        if (terminal and terminal.get("to") in {"confirmed", "refuted"}
                and _valid_date(terminal.get("evidence_published_at", ""))):
            evidence_date = dt.date.fromisoformat(terminal["evidence_published_at"])
            lead_days.append((evidence_date - item["captured"]).days)
    lead_days.sort()
    median_lead = None
    if lead_days:
        mid = len(lead_days) // 2
        median_lead = (lead_days[mid] if len(lead_days) % 2
                       else (lead_days[mid - 1] + lead_days[mid]) / 2)
    return {"cohort": len(cohort), "lifecycle": lifecycle_counts, "windows": windows,
            "lead_days": lead_days, "median_lead_days": median_lead}


def main(argv=None):
    parser = argparse.ArgumentParser(description="領先假說報告品質檢查")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--lint", action="store_true")
    mode.add_argument("--due", action="store_true", help="列出指定日期前到期且仍追蹤中的假說")
    mode.add_argument("--summary", action="store_true", help="輸出第二階段資料分布摘要")
    mode.add_argument("--metrics", action="store_true", help="只對前瞻樣本輸出 30/60/90 日成效")
    mode.add_argument("--migrate-v2", action="store_true", help="將 v1 報告機械遷移至 v2")
    parser.add_argument("--as-of", help="--due／--metrics 的截止日，預設今天（YYYY-MM-DD）")
    parser.add_argument("stock_id", nargs="?")
    args = parser.parse_args(argv)
    if args.migrate_v2:
        changed = migrate_reports_v2()
        for path in changed:
            print(f"MIGRATED {os.path.relpath(path, ROOT)}")
        print(f"完成：{len(changed)} 份報告遷移至 v2")
        return 0
    reports = load_reports()
    if args.stock_id:
        reports = {sid: report for sid, report in reports.items() if sid == args.stock_id}
    invalid_reports = [sid for sid, report in reports.items() if report["quality_invalid"]]
    if invalid_reports and (args.due or args.summary or args.metrics):
        print("資料品質未通過，請先執行 --lint：" + ", ".join(invalid_reports), file=sys.stderr)
        return 1
    if args.due:
        as_of = args.as_of or _today().isoformat()
        if not _valid_date(as_of):
            print("--as-of 必須是 YYYY-MM-DD", file=sys.stderr)
            return 2
        due = due_hypotheses(reports, as_of)
        for review_due, sid, hid, title in due:
            print(f"DUE {review_due} {sid} {hid}｜{title}")
        print(f"截至 {as_of}：{len(due)} 則待複核")
        return 0
    if args.summary:
        capture_modes = {}
        lifecycles = {}
        sources = {}
        total = 0
        for report in reports.values():
            for hypothesis in report["hypotheses"]:
                total += 1
                hmeta = hypothesis["meta"]
                for target, key in ((capture_modes, "capture_mode"),
                                    (lifecycles, "lifecycle"), (sources, "source_type")):
                    value = hmeta.get(key) or "missing"
                    target[value] = target.get(value, 0) + 1
        print(f"reports={len(reports)} hypotheses={total}")
        print("capture_mode " + " ".join(f"{key}={value}" for key, value in sorted(capture_modes.items())))
        print("lifecycle " + " ".join(f"{key}={value}" for key, value in sorted(lifecycles.items())))
        print("source_type " + " ".join(f"{key}={value}" for key, value in sorted(sources.items())))
        return 0
    if args.metrics:
        as_of = args.as_of or _today().isoformat()
        if not _valid_date(as_of):
            print("--as-of 必須是 YYYY-MM-DD", file=sys.stderr)
            return 2
        metrics = prospective_metrics(reports, as_of)
        print(f"as_of={as_of} prospective_cohort={metrics['cohort']}")
        print("lifecycle " + " ".join(
            f"{key}={value}" for key, value in sorted(metrics["lifecycle"].items())))
        for days, item in metrics["windows"].items():
            rate = "-" if not item["eligible"] else f"{item['terminal'] / item['eligible']:.1%}"
            print(f"terminal_within_{days}d={item['terminal']}/{item['eligible']} rate={rate}")
        median = metrics["median_lead_days"]
        print(f"median_formal_evidence_lead_days={median if median is not None else '-'}")
        return 0
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
