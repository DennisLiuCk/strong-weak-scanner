#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""管理與稽核 notes/qualitative/*.md 個股質化研究筆記。

筆記有兩條互不取代的狀態軸：

* freshness：missing / draft / fresh / due，只回答內容是否需要更新。
* verification：ai_draft / partially_verified /
  independently_verified / conflicted，只回答內容查核到什麼程度。

`last_updated` 絕不會自動把筆記升級成已查核。查核狀態必須通過來源、
獨立 reviewer、查核範圍與內容雜湊等契約；dashboard 與 CLI 共用本檔的判斷。
"""

import argparse
import csv
import glob
import hashlib
import os
import re
import sys
from datetime import date, datetime, timedelta, timezone
from urllib.parse import parse_qs, urlparse

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(ROOT, "notes", "qualitative")
TEMPLATE_MD = os.path.join(NOTES_DIR, "_template.md")
UNIVERSE_CSV = os.path.join(ROOT, "config", "universe.csv")

# 改了 _template.md 的研究結構或品質契約就必須遞增。
TEMPLATE_VERSION = 2
VERIFICATION_STATUSES = (
    "ai_draft",
    "partially_verified",
    "independently_verified",
    "conflicted",
)
VERIFICATION_LABEL = {
    "ai_draft": "AI 草稿・未獨立查核",
    "partially_verified": "部分核驗",
    "independently_verified": "已獨立核對來源",
    "conflicted": "來源衝突・待釐清",
}

_META_RE = re.compile(r"<!--\s*meta\s*(.*?)-->", re.S | re.I)
_KV_RE = re.compile(r"^\s*([\w_]+)\s*:\s*(.*?)\s*$")
_DATE_SHAPE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)
_REF_RE = re.compile(r"\[(S\d+)\]")
_SOURCE_DEF_RE = re.compile(
    r"^\s*-\s*\[(S\d+)\]\s*\*\*(一手|二手|衍生)\*\*\s*[｜|]\s*"
    r"(.+?)\s*[｜|]\s*(.+?)\s*[｜|]\s*(https?://\S+)\s*$"
)
_SOURCE_LIKE_RE = re.compile(r"^\s*-\s*\[(S\d+)\]")
_TABLE_SEP_RE = re.compile(r":?-+:?")
_INVALID_FILENAME_RE = re.compile(r'[<>:"/\\|?*]')
_PLACEHOLDER_RE = re.compile(r"(?:待填|TBD|TODO|尚待|\{\{.+?\}\})", re.I)
_GENERIC_SOURCE_RE = re.compile(
    r"mops(?:ov)?\.twse\.com\.tw/(?:mops/)?(?:$|[#?]|web(?:/|$))",
    re.I,
)
_TOKEN_RE = re.compile(
    r"\*\*(?P<bold>.+?)\*\*"
    r"|\[(?P<ltext>[^\]]+)\]\((?P<lurl>https?://[^\s)]+)\)"
    r"|(?P<url>https?://[A-Za-z0-9\-._~:/?#\[\]@!$&'*+,;=%]+)",
    re.S,
)

_EXCLUDED_CLAIM_SECTION_RE = re.compile(
    r"^(?:(?:資料來源|證據索引|證據索引與資料來源)(?:\s*[（(].*[）)])?"
    r"|下次更新|下次更新建議時機|下次更新與事件觸發|事件觸發)$"
)
_LIST_ITEM_RE = re.compile(r"^(?P<marker>[-*+]|\d+[.)])\s+(?P<text>.+)$")
_SUBHEADING_RE = re.compile(r"^#{3,6}\s+(.+?)\s*$")
_REVIEWER_PLACEHOLDERS = {"", "-", "tbd", "todo", "ai", "agent", "待填", "未定"}
_V2_REQUIRED_SECTIONS = (
    "30 秒摘要",
    "產業位置與競爭格局",
    "業務與獲利模式",
    "客戶、產品與地區結構",
    "財務品質與資本配置",
    "優勢、弱點與護城河",
    "成長動能、催化劑與驗證 KPI",
    "風險與預警指標",
    "管理層與治理",
    "證據索引與資料來源",
    "下次更新與事件觸發",
)


def _is_exact_mops_announcement_url(url):
    """辨識可唯一回到單筆重大訊息的 MOPS URL，而非泛用查詢入口。"""
    parsed = urlparse(url)
    if (parsed.hostname or "").lower() not in {
        "mops.twse.com.tw",
        "mopsov.twse.com.tw",
    }:
        return False
    if parsed.path.rstrip("/").lower() not in {
        "/mops/web/ajax_t05st01",
        "/mops/web/t05st01",
    }:
        return False

    query = parse_qs(parsed.query)
    if query.get("step") != ["2"]:
        return False
    required = {
        "TYPEK": r"[A-Za-z]+",
        "co_id": r"\d{4,6}",
        "spoke_date": r"\d{8}",
        "spoke_time": r"\d{1,6}",
        "seq_no": r"\d+",
    }
    return all(
        len(query.get(key, [])) == 1
        and re.fullmatch(pattern, query[key][0] or "") is not None
        for key, pattern in required.items()
    )


_TAIPEI_TZ = timezone(timedelta(hours=8))


def _today():
    """研究日期固定採台灣 UTC+8；GitHub runner 的 UTC 不得造成跨午夜誤判。"""
    return datetime.now(_TAIPEI_TZ).date()


def _valid_date(value):
    """同時驗證 YYYY-MM-DD 字形與真實日曆日期。"""
    if not value or not _DATE_SHAPE_RE.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _parse_meta_details(text):
    matches = list(_META_RE.finditer(text))
    if not matches:
        return {}, ["缺少 <!-- meta ... --> 區塊"]
    match = matches[0]
    errors = []
    if len(matches) > 1:
        errors.append("同一筆記只能有一個 meta 區塊")
    meta, seen = {}, set()
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        item = _KV_RE.match(line)
        if not item:
            errors.append(f"meta 格式無法解析：{line.strip()}")
            continue
        key, value = item.group(1), item.group(2)
        if key in seen:
            errors.append(f"meta key 重複：{key}")
        seen.add(key)
        meta[key] = value
    return meta, errors


def _parse_meta(text):
    return _parse_meta_details(text)[0]


def content_digest(text):
    """回傳 reviewer 所簽內容的 SHA-256；雜湊欄本身不納入計算。

    換行統一為 LF，避免 Windows/Actions 僅因 checkout 換行而讓簽核失效。
    任何其他 meta 或正文變更都會使既有簽核失效。
    """
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    meta_match = _META_RE.search(normalized)
    if meta_match:
        meta_block = re.sub(
            r"^[ \t]*reviewed_content_sha256[ \t]*:.*$",
            "reviewed_content_sha256:",
            meta_match.group(0),
            flags=re.M,
        )
        normalized = (
            normalized[:meta_match.start()] + meta_block + normalized[meta_match.end():]
        )
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _plain_text(value):
    value = re.sub(r"<!--.*?-->", " ", value, flags=re.S)
    value = re.sub(r"\[(S\d+)\]", "", value)
    value = re.sub(r"\[([^\]]+)\]\(https?://[^)]+\)", r"\1", value)
    value = re.sub(r"https?://\S+", "", value)
    value = re.sub(r"[*_`>#|]", " ", value)
    return re.sub(r"\s+", " ", value).strip(" -｜")


def _is_placeholder_claim(plain):
    """只略過整個 block 都是骨架提示者，不因句中出現「尚待/TODO」漏掉真主張。"""
    value = plain.strip()
    if re.fullmatch(r"(?:待填|TBD|TODO|尚待補充|尚待查證)[。.]?", value, re.I):
        return True
    if re.fullmatch(r"[（(]\s*(?:待填|TBD|TODO)\s*[：:].*?[）)]", value, re.I):
        return True
    if re.fullmatch(r"\{\{.+?\}\}", value):
        return True
    return False


def _is_system_boilerplate(plain):
    """排除模板自己的狀態／免責說明，但不吞掉同段後續的公司主張。"""
    value = plain.strip()
    if re.fullmatch(
        r"族群[:：].+?[。.]本筆記為 Universe 質化參考[,，]非投資建議[。.]?",
        value,
    ):
        return True
    if (re.match(r"^查核狀態以 meta 與 qual\s+notes\.py --lint 為準", value)
            and value.endswith("不代表內容已被獨立核驗。")):
        return True
    return False


def _extract_summary(text, limit=160):
    """優先取「30 秒摘要」，舊版則退回「業務概況」。"""
    body = _META_RE.sub("", text)
    matches = list(_SECTION_RE.finditer(body))
    section_text = ""
    for wanted in ("30 秒摘要", "業務概況"):
        for idx, match in enumerate(matches):
            if wanted in match.group(1):
                end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
                section_text = body[match.end():end]
                break
        if section_text:
            break
    if not section_text:
        return ""
    summary = _plain_text(section_text)
    if len(summary) <= limit:
        return summary
    cut = max(summary.rfind(mark, 0, limit + 1) for mark in "。；！？")
    if cut >= max(60, limit // 2):
        return summary[:cut + 1]
    return summary[:limit].rstrip() + "…"


def _runs(text):
    """把有限 Markdown 轉成前端安全建立 DOM 所需的 runs。"""
    runs, pos = [], 0
    for match in _TOKEN_RE.finditer(text):
        if match.start() > pos:
            runs.append({"s": text[pos:match.start()]})
        if match.group("bold") is not None:
            runs.append({"s": match.group("bold"), "b": True})
        elif match.group("ltext") is not None:
            runs.append({"s": match.group("ltext"), "a": match.group("lurl")})
        else:
            runs.append({"s": match.group("url"), "a": match.group("url")})
        pos = match.end()
    if pos < len(text):
        runs.append({"s": text[pos:]})
    return runs


def _parse_body(text):
    """把章節內文轉為 paragraph/list/table blocks。"""
    lines = text.strip("\n").split("\n")
    blocks, para, items, list_type, idx = [], [], [], None, 0

    def flush():
        nonlocal list_type
        if para:
            blocks.append({"t": "p", "runs": _runs(" ".join(para))})
            para.clear()
        if items:
            blocks.append({"t": list_type or "ul", "items": [_runs(item) for item in items]})
            items.clear()
            list_type = None

    while idx < len(lines):
        line = lines[idx].strip()
        if not line:
            flush()
        elif line.startswith("|"):
            flush()
            rows = []
            while idx < len(lines) and lines[idx].strip().startswith("|"):
                rows.append([cell.strip() for cell in lines[idx].strip().strip("|").split("|")])
                idx += 1
            if len(rows) >= 2 and all(_TABLE_SEP_RE.fullmatch(cell) for cell in rows[1]):
                rows.pop(1)
            if rows:
                blocks.append({
                    "t": "table",
                    "head": [_runs(cell) for cell in rows[0]],
                    "rows": [[_runs(cell) for cell in row] for row in rows[1:]],
                })
            continue
        elif _LIST_ITEM_RE.match(line):
            item_match = _LIST_ITEM_RE.match(line)
            incoming_type = "ol" if item_match.group("marker")[0].isdigit() else "ul"
            if para:
                flush()
            elif items and list_type != incoming_type:
                flush()
            list_type = incoming_type
            items.append(item_match.group("text"))
        elif _SUBHEADING_RE.match(line):
            flush()
            blocks.append({"t": "h3", "runs": _runs(_SUBHEADING_RE.match(line).group(1))})
        elif items:
            items[-1] += " " + line
        else:
            para.append(re.sub(r"^>\s?", "", line))
        idx += 1
    flush()
    return blocks


def _extract_sections(text):
    """解析所有 H2；舊筆記 H2 前的重要警語也保留下來。"""
    body = _META_RE.sub("", text)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    matches = list(_SECTION_RE.finditer(body))
    out = []
    preamble_end = matches[0].start() if matches else len(body)
    preamble = body[:preamble_end]
    preamble = re.sub(r"^#\s+.*$", "", preamble, flags=re.M)
    preamble = re.sub(r"<!--.*?-->", "", preamble, flags=re.S)
    preamble = re.sub(r"^---+\s*$", "", preamble, flags=re.M)
    preamble = re.sub(r"^>\s?", "", preamble, flags=re.M).strip()
    if _plain_text(preamble):
        out.append({"h": "研究定位與重要註記", "blocks": _parse_body(preamble)})
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        out.append({"h": match.group(1).strip(), "blocks": _parse_body(body[start:end])})
    return out


def _parse_sources(text):
    sources, errors, warnings, duplicate_ids = {}, [], [], set()
    # 保留換行數，lint 的來源行號才仍對應原始檔。
    scan_text = re.sub(
        r"<!--.*?-->",
        lambda match: "\n" * match.group(0).count("\n"),
        text,
        flags=re.S,
    )
    for line_no, line in enumerate(scan_text.splitlines(), 1):
        match = _SOURCE_DEF_RE.match(line)
        if match:
            source_id, source_type, document, locator, url = match.groups()
            url = url.rstrip(".,;，；。")
            if source_id in sources:
                duplicate_ids.add(source_id)
                continue
            sources[source_id] = {
                "id": source_id,
                "type": source_type,
                "document": document.strip(),
                "locator": locator.strip(),
                "url": url,
                "line": line_no,
                "generic": (
                    bool(_GENERIC_SOURCE_RE.search(url))
                    and not _is_exact_mops_announcement_url(url)
                ),
            }
            if source_type == "一手":
                if not url.startswith("https://"):
                    errors.append(f"{source_id} 一手來源必須使用直接 HTTPS URL")
                if _PLACEHOLDER_RE.search(document) or not _plain_text(document):
                    errors.append(f"{source_id} 一手來源缺文件名稱與日期")
                elif not re.search(r"(?:19|20)\d{2}", document):
                    errors.append(f"{source_id} 一手來源文件名稱必須含發布、資料或擷取年份")
                if _PLACEHOLDER_RE.search(locator) or locator.strip() in {"", "-", "首頁"}:
                    errors.append(f"{source_id} 一手來源缺頁碼、表格或章節定位")
            if sources[source_id]["generic"]:
                warnings.append(f"{source_id} 可能是 MOPS 查詢入口，應改用直接公告或 PDF")
        elif _SOURCE_LIKE_RE.match(line):
            source_id = _SOURCE_LIKE_RE.match(line).group(1)
            errors.append(f"第 {line_no} 行 {source_id} 不符合固定來源格式")
    for source_id in sorted(duplicate_ids):
        errors.append(f"來源 ID 重複定義：{source_id}")
    return sources, errors, warnings


def _claim_units(text):
    """取出核心章節的實質 paragraph、bullet 與每一列 table data。"""
    body = _META_RE.sub("", text)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    units, current, section, table_row, in_table = [], [], "", 0, False

    def excluded():
        return bool(_EXCLUDED_CLAIM_SECTION_RE.fullmatch(section.strip()))

    def add(raw, kind="paragraph"):
        plain = _plain_text(raw)
        if not plain or _is_placeholder_claim(plain) or _is_system_boilerplate(plain):
            return
        refs = sorted(set(_REF_RE.findall(raw)))
        units.append({"text": plain, "raw": raw.strip(), "refs": refs, "kind": kind})

    def flush():
        if current:
            add(" ".join(current))
            current.clear()

    lines = body.splitlines()
    idx = 0
    while idx < len(lines):
        raw, line = lines[idx], lines[idx].strip()
        heading = re.match(r"^##\s+(.+?)\s*$", line)
        if heading:
            flush()
            section = heading.group(1)
            table_row = 0
            in_table = False
        elif (excluded() or not line or line == ">"
              or line.startswith(("# ", "###", "<!--", "-->", "---"))):
            flush()
            in_table = False
            table_row = 0
        elif line.startswith("|"):
            flush()
            if not in_table:
                in_table = True
                table_row = 0
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if all(_TABLE_SEP_RE.fullmatch(cell) for cell in cells):
                pass
            elif table_row == 0:
                table_row += 1  # 表頭不是主張。
            else:
                add(raw, "table_row")
                table_row += 1
        elif _LIST_ITEM_RE.match(line):
            flush()
            in_table = False
            table_row = 0
            item = _LIST_ITEM_RE.match(line).group("text")
            lookahead = idx + 1
            while lookahead < len(lines):
                continuation = lines[lookahead].strip()
                if (not continuation or _LIST_ITEM_RE.match(continuation)
                        or continuation.startswith(("|", "#"))):
                    break
                item += " " + continuation
                lookahead += 1
            add(item, "bullet")
            idx = lookahead - 1
        elif line.startswith(">"):
            in_table = False
            table_row = 0
            current.append(re.sub(r"^>\s?", "", line))
        else:
            in_table = False
            table_row = 0
            current.append(line)
        idx += 1
    flush()
    return units


def _raw_section_map(text):
    body = _META_RE.sub("", text)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    matches = list(_SECTION_RE.finditer(body))
    sections = {}
    for idx, match in enumerate(matches):
        heading = re.sub(r"\s*[（(].*[）)]\s*$", "", match.group(1)).strip()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        sections.setdefault(heading, body[match.end():end])
    return sections


def _section_raw(text, marker):
    return _raw_section_map(text).get(marker, "")


def _update_section_errors(section_body):
    """更新區只容許結構化研究排程，不作為藏公司主張的免引用區。"""
    clean = re.sub(r"<!--.*?-->", "", section_body, flags=re.S)
    labels = set()
    errors = []
    for line in clean.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        item = _LIST_ITEM_RE.match(stripped)
        if not item:
            errors.append("下次更新與事件觸發只能使用固定複核／事件觸發清單")
            continue
        plain = _plain_text(item.group("text"))
        label = next((name for name in ("固定複核", "事件觸發") if plain.startswith(name)), None)
        if not label:
            errors.append("更新清單項目必須以「固定複核」或「事件觸發」開頭")
            continue
        labels.add(label)
        if _PLACEHOLDER_RE.search(plain):
            errors.append(f"{label} 仍是模板占位")
        if _REF_RE.search(stripped):
            errors.append(f"{label} 是研究排程，不得用來承載 [S#] 公司主張")
    for required in ("固定複核", "事件觸發"):
        if required not in labels:
            errors.append(f"下次更新與事件觸發缺少「{required}」項目")
    return errors


def _effective_verification(declared, errors):
    if declared not in VERIFICATION_STATUSES:
        return "ai_draft"
    # 已知來源矛盾是風險下限；即使 hash/schema 另有錯，也不能把衝突隱成灰色草稿。
    if declared == "conflicted":
        return "conflicted"
    if errors and declared != "ai_draft":
        return "ai_draft"
    return declared


def _analyse_note(path, text):
    meta, errors = _parse_meta_details(text)
    warnings = []
    sources, source_errors, source_warnings = _parse_sources(text)
    errors.extend(source_errors)
    warnings.extend(source_warnings)

    sid_from_name = os.path.basename(path).split("_", 1)[0]
    sid = meta.get("stock_id") or sid_from_name
    if not re.fullmatch(r"\d{4}", sid or ""):
        errors.append("stock_id 必須是四位數字")
    if meta.get("stock_id") and sid_from_name != meta["stock_id"]:
        errors.append(f"檔名 stock_id {sid_from_name} 與 meta {meta['stock_id']} 不一致")

    try:
        template_version = int(meta.get("template_version") or 0)
    except ValueError:
        template_version = 0
        errors.append("template_version 必須是整數")
    if template_version > TEMPLATE_VERSION:
        errors.append(
            f"template_version {template_version} 高於目前可理解的 {TEMPLATE_VERSION}"
        )

    for field in ("last_updated", "next_review", "content_as_of", "reviewed_at"):
        if meta.get(field) and not _valid_date(meta[field]):
            errors.append(f"{field} 不是合法 YYYY-MM-DD 日期：{meta[field]}")
    today = _today().isoformat()
    for field in ("last_updated", "content_as_of", "reviewed_at"):
        if _valid_date(meta.get(field, "")) and meta[field] > today:
            errors.append(f"{field} 不可晚於今天 {today}：{meta[field]}")

    declared = meta.get("verification_status") or meta.get("review_status") or "ai_draft"
    if declared not in VERIFICATION_STATUSES:
        errors.append(f"非法 verification_status：{declared}")

    reference_body = _META_RE.sub("", text)
    reference_body = re.sub(r"<!--.*?-->", "", reference_body, flags=re.S)
    body_without_definitions = "\n".join(
        line for line in reference_body.splitlines() if not _SOURCE_LIKE_RE.match(line)
    )
    body_refs = sorted(set(_REF_RE.findall(body_without_definitions)))
    for ref in body_refs:
        if ref not in sources:
            errors.append(f"正文引用未定義來源：{ref}")
    unused = sorted(set(sources) - set(body_refs))
    if unused:
        warnings.append("來源已定義但正文未引用：" + ", ".join(unused))
    used_generic = sorted(
        ref for ref in body_refs if sources.get(ref, {}).get("generic")
    )
    if declared in {"partially_verified", "independently_verified", "conflicted"} and used_generic:
        errors.append(
            "已核驗主張不可使用 MOPS 查詢入口，請改直接公告或 PDF："
            + ", ".join(used_generic)
        )

    units = _claim_units(text)
    cited = [unit for unit in units if unit["refs"]]
    primary_cited = [
        unit for unit in units
        if any(sources.get(ref, {}).get("type") == "一手" for ref in unit["refs"])
    ]

    drafted_by = meta.get("drafted_by", "").strip()
    reviewed_by = meta.get("reviewed_by", "").strip()
    reviewed_at = meta.get("reviewed_at", "").strip()
    review_scope = meta.get("review_scope", "").strip()
    signed_digest = meta.get("reviewed_content_sha256", "").strip().lower()

    if declared in {"partially_verified", "independently_verified", "conflicted"}:
        if (drafted_by.lower() in _REVIEWER_PLACEHOLDERS
                or _PLACEHOLDER_RE.search(drafted_by)):
            errors.append(f"{declared} 缺少 drafted_by")
        if (reviewed_by.lower() in _REVIEWER_PLACEHOLDERS
                or _PLACEHOLDER_RE.search(reviewed_by)):
            errors.append(f"{declared} 缺少具名 reviewed_by")
        if drafted_by and reviewed_by and drafted_by.casefold() == reviewed_by.casefold():
            errors.append("reviewed_by 必須與 drafted_by 不同，才能稱為獨立 reviewer")
        if not _valid_date(reviewed_at):
            errors.append(f"{declared} 缺少合法 reviewed_at")
        if not review_scope or _PLACEHOLDER_RE.search(review_scope):
            errors.append(f"{declared} 缺少明確 review_scope")
        if not _valid_date(meta.get("last_updated", "")):
            errors.append(f"{declared} 缺少合法 last_updated")
        if not _valid_date(meta.get("next_review", "")):
            errors.append(f"{declared} 缺少合法 next_review")
        if not re.fullmatch(r"[0-9a-f]{64}", signed_digest):
            errors.append(f"{declared} 缺少合法 reviewed_content_sha256")
        elif signed_digest != content_digest(text):
            errors.append("正文或 meta 已在簽核後變更；reviewed_content_sha256 不一致")
        if (_valid_date(reviewed_at) and _valid_date(meta.get("last_updated", ""))
                and reviewed_at < meta["last_updated"]):
            errors.append("reviewed_at 早於 last_updated，內容需重新簽核")
        if (_valid_date(reviewed_at) and _valid_date(meta.get("content_as_of", ""))
                and meta["content_as_of"] > reviewed_at):
            errors.append("content_as_of 晚於 reviewed_at，reviewer 尚未能查核該時點資料")

    if declared == "partially_verified":
        deletion_only = review_scope == "confirmed_correction_deletion_only"
        if not cited and not deletion_only:
            errors.append("partially_verified 的核驗範圍沒有任何可稽核 claim block 引用")
        if deletion_only and cited:
            errors.append("deletion_only 範圍不應宣告仍存續的已核驗正文引用")
        secondary_only_units = [unit for unit in cited if unit not in primary_cited]
        if not deletion_only and secondary_only_units:
            errors.append(
                f"partially_verified 有 {len(secondary_only_units)} 個已引用 claim block "
                "沒有實際指向一手來源"
            )

    if declared == "independently_verified":
        if template_version != TEMPLATE_VERSION:
            errors.append(f"independently_verified 必須使用 template_version {TEMPLATE_VERSION}")
        if review_scope != "all_material_claims":
            errors.append("完整獨立核驗的 review_scope 必須是 all_material_claims")
        for field in ("content_as_of", "latest_financial_period"):
            if not meta.get(field) or _PLACEHOLDER_RE.search(meta.get(field, "")):
                errors.append(f"independently_verified 缺少 {field}")
        section_map = _raw_section_map(text)
        for heading in _V2_REQUIRED_SECTIONS:
            section_body = section_map.get(heading)
            if section_body is None:
                errors.append(f"independently_verified 缺少 v2 章節：{heading}")
                continue
            if heading == "證據索引與資料來源":
                indexed_sources, _, _ = _parse_sources(section_body)
                if not indexed_sources:
                    errors.append("證據索引與資料來源章節沒有固定格式來源")
                elif set(indexed_sources) != set(sources):
                    errors.append("所有固定格式來源都必須集中在證據索引與資料來源章節")
                residual_lines = [
                    line.strip() for line in section_body.splitlines()
                    if line.strip() and not _SOURCE_LIKE_RE.match(line)
                ]
                if residual_lines:
                    errors.append("證據索引只能放固定格式來源，不得夾帶免引用的實質主張")
            elif heading == "下次更新與事件觸發":
                errors.extend(_update_section_errors(section_body))
            elif not _claim_units(f"## {heading}\n{section_body}"):
                errors.append(f"v2 章節仍是空白或模板占位：{heading}")
        if not units:
            errors.append("independently_verified 沒有可稽核的實質 claim block")
        missing_citation = [unit for unit in units if not unit["refs"]]
        if missing_citation:
            errors.append(
                f"仍有 {len(missing_citation)}/{len(units)} 個 claim block 沒有 [S#] 引用"
            )
        missing_primary = [unit for unit in units if unit not in primary_cited]
        if missing_primary:
            errors.append(
                f"仍有 {len(missing_primary)}/{len(units)} 個 claim block 沒有一手來源"
            )

    if declared == "conflicted":
        conflict_summary = meta.get("conflict_summary") or meta.get("open_questions") or ""
        conflict_body = _section_raw(text, "未決衝突")
        conflict_refs = sorted(set(_REF_RE.findall(conflict_body)))
        if not conflict_summary or _PLACEHOLDER_RE.search(conflict_summary):
            errors.append("conflicted 缺少 conflict_summary")
        if not _plain_text(conflict_body):
            errors.append("conflicted 缺少「未決衝突」章節")
        if len(conflict_refs) < 2:
            errors.append("未決衝突至少必須並列兩個來源")
        primary_conflict_refs = {
            ref for ref in conflict_refs if sources.get(ref, {}).get("type") == "一手"
        }
        if len(primary_conflict_refs) < 2:
            errors.append("未決衝突的雙方主張都必須實際指向一手來源")

    effective = _effective_verification(declared, errors)
    claim_count = len(units)
    return {
        "path": path,
        "relpath": os.path.relpath(path, ROOT).replace("\\", "/"),
        "stock_id": sid,
        "template_version": template_version,
        "last_updated": meta.get("last_updated") or None,
        "content_as_of": meta.get("content_as_of") or None,
        "latest_financial_period": meta.get("latest_financial_period") or None,
        "next_review": meta.get("next_review") or None,
        "declared_verification": declared,
        "verification": effective,
        "quality_invalid": bool(errors),
        "drafted_by": drafted_by or None,
        "reviewed_by": reviewed_by or None,
        "reviewed_at": reviewed_at or None,
        "review_scope": review_scope or None,
        "conflict_summary": meta.get("conflict_summary") or None,
        "reviewed_content_sha256": signed_digest or None,
        "summary": _extract_summary(text),
        "sections": _extract_sections(text),
        "sources": list(sources.values()),
        "primary_source_count": sum(1 for source in sources.values() if source["type"] == "一手"),
        "claim_count": claim_count,
        "cited_claim_count": len(cited),
        "primary_cited_claim_count": len(primary_cited),
        "citation_coverage": round(len(cited) / claim_count, 4) if claim_count else 0.0,
        "primary_coverage": round(len(primary_cited) / claim_count, 4) if claim_count else 0.0,
        "quality_errors": errors,
        "quality_warnings": warnings,
    }


def load_notes(notes_dir=NOTES_DIR):
    """載入筆記並執行同一套品質分析；重複 stock_id 不再靜默覆寫。"""
    out = {}
    if not os.path.isdir(notes_dir):
        return out
    for path in sorted(glob.glob(os.path.join(notes_dir, "*.md"))):
        if os.path.basename(path).startswith("_"):
            continue
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        info = _analyse_note(path, text)
        sid = info["stock_id"]
        if not sid:
            continue
        if sid in out:
            message = (
                f"stock_id {sid} 重複：{os.path.basename(out[sid]['path'])}、"
                f"{os.path.basename(path)}"
            )
            out[sid]["quality_errors"].append(message)
            out[sid]["quality_invalid"] = True
            out[sid]["verification"] = "ai_draft"
            continue
        out[sid] = info
    if os.path.normcase(os.path.abspath(notes_dir)) == os.path.normcase(os.path.abspath(NOTES_DIR)):
        universe_ids = {row["stock_id"] for row in _load_universe()}
        for sid, info in out.items():
            if sid not in universe_ids:
                info["quality_errors"].append(f"stock_id {sid} 不在 config/universe.csv")
                info["quality_invalid"] = True
                info["verification"] = "ai_draft"
    return out


def note_status(info, asof):
    """回傳 freshness；這個結果不代表資料正確或已查核。"""
    if info is None:
        return "missing"
    last_updated = info.get("last_updated")
    if not _valid_date(last_updated):
        return "draft"
    next_review = info.get("next_review")
    if not _valid_date(next_review):
        return "unscheduled"
    if next_review <= asof:
        return "due"
    return "fresh"


def note_review_status(info):
    """回傳通過品質契約後的有效查核狀態。"""
    return "ai_draft" if info is None else info.get("verification", "ai_draft")


def _load_universe():
    with open(UNIVERSE_CSV, encoding="utf-8") as handle:
        return [row for row in csv.DictReader(handle) if row.get("stock_id")]


def _status_rows(asof):
    notes = load_notes()
    rows = []
    for universe_row in _load_universe():
        sid = universe_row["stock_id"]
        info = notes.get(sid)
        rows.append({
            "stock_id": sid,
            "name": universe_row["name"],
            "group": universe_row["group"],
            "status": note_status(info, asof),
            "verification": note_review_status(info) if info else None,
            "declared_verification": (info or {}).get("declared_verification") or "ai_draft",
            "quality_invalid": bool(info and info.get("quality_invalid")),
            "template_old": bool(info and info["template_version"] < TEMPLATE_VERSION),
            "last_updated": (info or {}).get("last_updated") or "-",
            "next_review": (info or {}).get("next_review") or "-",
            "reviewed_by": (info or {}).get("reviewed_by") or "-",
            "review_scope": (info or {}).get("review_scope") or "-",
            "quality_errors": (info or {}).get("quality_errors", []),
        })
    return rows


def _safe_filename(value):
    cleaned = _INVALID_FILENAME_RE.sub("", value).strip().rstrip(".")
    return cleaned or "unnamed"


def _scaffold(stock_id, force=False):
    universe = {row["stock_id"]: row for row in _load_universe()}
    if stock_id not in universe:
        print(f"{stock_id} 不在 config/universe.csv，請先補入 name/group/biz")
        return 1
    existing = load_notes().get(stock_id)
    row = universe[stock_id]
    out_path = existing["path"] if existing else os.path.join(
        NOTES_DIR, f"{stock_id}_{_safe_filename(row['name'])}.md"
    )
    if os.path.exists(out_path) and not force:
        print(f"已存在：{out_path}（若確定要清空重建才使用 --force）")
        return 1
    with open(TEMPLATE_MD, encoding="utf-8") as handle:
        template = handle.read()
    text = (template.replace("{{STOCK_ID}}", stock_id)
            .replace("{{NAME}}", row["name"])
            .replace("{{GROUP}}", row["group"])
            .replace("{{BIZ}}", row.get("biz", ""))
            .replace("{{TEMPLATE_VERSION}}", str(TEMPLATE_VERSION))
            .replace("{{TODAY}}", _today().isoformat()))
    os.makedirs(NOTES_DIR, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(f"已建立筆記骨架：{out_path}")
    return 0


STATUS_LABEL = {
    "missing": "尚無筆記",
    "draft": "未填更新日",
    "unscheduled": "未排複核日",
    "fresh": "時效內",
    "due": "待更新",
}


def _lint(notes, target=None):
    selected = [note for sid, note in sorted(notes.items()) if not target or sid == target]
    if target and not selected:
        print(f"找不到 stock_id {target}")
        return 1
    error_count = warning_count = 0
    if not target:
        missing_ids = sorted(
            {row["stock_id"] for row in _load_universe()} - set(notes)
        )
        for sid in missing_ids:
            print(f"ERROR\t{sid}\tuniverse 成員缺少質化研究筆記")
            error_count += 1
    for note in selected:
        for issue in note["quality_errors"]:
            print(f"ERROR\t{note['stock_id']}\t{issue}")
            error_count += 1
        for issue in note["quality_warnings"]:
            print(f"WARN\t{note['stock_id']}\t{issue}")
            warning_count += 1
    print(f"品質契約：{len(selected)} 篇，{error_count} errors，{warning_count} warnings")
    return 1 if error_count else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--asof", help="freshness 判斷日（YYYY-MM-DD）")
    parser.add_argument("--missing", action="store_true", help="只列尚無筆記")
    parser.add_argument("--stale", action="store_true", help="只列已逾 next_review")
    parser.add_argument("--outdated", action="store_true", help="只列模板版本落後")
    parser.add_argument("--needs-review", action="store_true", help="列出未完整獨立核驗、逾期或品質無效者")
    parser.add_argument("--invalid", action="store_true", help="只列品質契約有 error 的筆記")
    parser.add_argument("--quality", choices=VERIFICATION_STATUSES, help="依有效查核狀態篩選")
    parser.add_argument("--lint", nargs="?", const="ALL", metavar="STOCK_ID", help="稽核全部或指定股票，error 時 exit 1")
    parser.add_argument("--hash", dest="hash_stock", metavar="STOCK_ID", help="輸出供 reviewer 簽核的內容 SHA-256")
    parser.add_argument("--new", metavar="STOCK_ID", help="從 _template.md 建立骨架")
    parser.add_argument("--force", action="store_true", help="搭配 --new 覆寫既有筆記（會清空內容）")
    args = parser.parse_args()

    if args.new:
        return _scaffold(args.new, force=args.force)

    notes = load_notes()
    if args.lint:
        return _lint(notes, None if args.lint == "ALL" else args.lint)
    if args.hash_stock:
        note = notes.get(args.hash_stock)
        if not note:
            print(f"找不到 stock_id {args.hash_stock}")
            return 1
        with open(note["path"], encoding="utf-8") as handle:
            print(content_digest(handle.read()))
        return 0

    asof = args.asof or _today().isoformat()
    if not _valid_date(asof):
        parser.error("--asof 必須是合法 YYYY-MM-DD 日期")
    rows = _status_rows(asof)
    if args.missing:
        rows = [row for row in rows if row["status"] == "missing"]
    elif args.stale:
        rows = [row for row in rows if row["status"] == "due"]
    elif args.outdated:
        rows = [row for row in rows if row["template_old"]]
    elif args.needs_review:
        rows = [row for row in rows if (
            row["verification"] != "independently_verified"
            or row["status"] in {"missing", "draft", "unscheduled", "due"}
            or row["quality_invalid"]
        )]
    elif args.invalid:
        rows = [row for row in rows if row["quality_invalid"]]
    elif args.quality:
        rows = [row for row in rows if row["verification"] == args.quality]

    if not rows:
        print("（無符合項目）")
        return 0
    for row in rows:
        flags = []
        if row["template_old"]:
            flags.append("模板待升級")
        if row["quality_invalid"]:
            flags.append(f"品質錯誤 {len(row['quality_errors'])}")
        suffix = "；" + "、".join(flags) if flags else ""
        print(
            f"{row['stock_id']}\t{row['name']}\t{row['group']}\t"
            f"{STATUS_LABEL[row['status']]}\t"
            f"{VERIFICATION_LABEL.get(row['verification'], '無筆記・無品質狀態')}\t"
            f"最後更新:{row['last_updated']}\t下次複核:{row['next_review']}{suffix}"
        )

    all_rows = _status_rows(asof)
    quality_counts = {
        status: sum(1 for row in all_rows if row["verification"] == status)
        for status in VERIFICATION_STATUSES
    }
    print(
        f"\n共 {len(rows)} 筆；universe {len(all_rows)} 檔（缺筆記 "
        f"{sum(1 for row in all_rows if row['status'] == 'missing')}、"
        f"未排複核 {sum(1 for row in all_rows if row['status'] == 'unscheduled')}、"
        f"待更新 {sum(1 for row in all_rows if row['status'] == 'due')}；"
        + "、".join(f"{VERIFICATION_LABEL[key]} {value}" for key, value in quality_counts.items())
        + "）"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
