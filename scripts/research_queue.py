#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""聚合質化筆記、領先假說、事件、財報覆蓋與市場議題的唯讀研究佇列。"""

import argparse
import csv
import datetime as dt
import glob
import io
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from urllib.parse import parse_qsl, urlencode, urlparse, urlsplit, urlunsplit

import db_ro
from leading_hypotheses import load_reports
from qual_notes import load_events, load_notes, note_review_status


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
UNIVERSE_CSV = os.path.join(ROOT, "config", "universe.csv")
GROUPS_CSV = os.path.join(ROOT, "config", "groups.csv")
TOPICS_DIR = os.path.join(ROOT, "notes", "research_topics")
SCAN_LOG = os.path.join(TOPICS_DIR, "scan_log.csv")
ROTATION_ANCHOR = dt.date(2026, 7, 27)  # 星期一；A cohort 的第一個營運週
TAIPEI_TZ = dt.timezone(dt.timedelta(hours=8))

TOPIC_META_RE = re.compile(r"<!--\s*research_topic\b(.*?)-->", re.S | re.I)
IMPACT_RE = re.compile(r"<!--\s*impact\b(.*?)-->", re.S | re.I)
TRANSITION_RE = re.compile(r"<!--\s*transition\b(.*?)-->", re.S | re.I)
SOURCE_RE = re.compile(r"<!--\s*research_source\b(.*?)-->", re.S | re.I)
CLAIM_RE = re.compile(r"<!--\s*research_claim\b(.*?)-->", re.S | re.I)
COMPARISON_RE = re.compile(r"<!--\s*metric_comparison\b(.*?)-->", re.S | re.I)
MONITOR_RE = re.compile(r"<!--\s*monitoring_item\b(.*?)-->", re.S | re.I)
TOPIC_ID_RE = re.compile(r"^MI-\d{4}-\d{2}-\d{2}-[A-Z0-9-]+$")
HYPOTHESIS_REF_RE = re.compile(r"^(\d{4}):H(\d+)$")
SOURCE_ID_RE = re.compile(r"^S[1-9]\d*$")
CLAIM_ID_RE = re.compile(r"^C[1-9]\d*$")
COMPARISON_ID_RE = re.compile(r"^M[1-9]\d*$")
OBSERVATION_ID_RE = re.compile(r"^M[1-9]\d*-O[1-9]\d*$")
MONITOR_ID_RE = re.compile(r"^T[1-9]\d*$")
V3_CUTOVER_DATE = dt.date(2026, 8, 2)
BEGINNER_HEADING = "新手先讀：這篇在講什麼"
BEGINNER_SUBHEADINGS = (
    "名詞小字典",
    "三句話抓重點",
    "為什麼重要",
    "接下來怎麼追",
    "想一想",
)

TOPIC_STATUSES = {"inbox", "triaged", "promoted", "dismissed", "resolved"}
TOPIC_PRIORITIES = {"p0", "p1", "p2", "p3"}
SOURCE_TYPES = {
    "official_company", "official_policy", "official_exchange", "management_direct",
    "management_relay", "broker_relay", "media_report", "mixed",
}
EVIDENCE_ROLES = {"candidate_source", "trigger_only"}
SOURCE_ROLES = {
    "company_release", "company_filing", "regulator_or_policy", "exchange",
    "standard", "competitor_primary", "management_commentary", "market_estimate",
    "media", "other_primary",
}
VERIFIED_SUPPORT_ROLES = SOURCE_ROLES - {"market_estimate", "media"}
SOURCE_STATUSES = {"active", "superseded", "rejected"}
SOURCE_KINDS = {"document", "living_index"}
CLAIM_LABELS = {
    "verified": "證實",
    "inference": "推論",
    "unverified": "待驗證",
}
CLAIM_STATUSES = {"active", "superseded", "refuted"}
COMPARABILITY = {
    "directly_comparable": "可直接比較",
    "normalized_comparable": "正規化後可比",
    "not_comparable": "不可比",
}
COMPARISON_KINDS = {"aligned_metric", "heterogeneous_evidence"}
VALUE_KINDS = {"point", "range", "lower_bound", "upper_bound"}
MONITOR_STATUSES = {"active", "retired"}
MONITOR_FREQUENCIES = {"event_driven", "weekly", "monthly", "quarterly", "annual"}
CONFIDENCE_LABELS = {
    "high": "高", "medium": "中", "low": "低",
    "needs_revalidation": "待重新驗證", "unstructured": "未結構化",
}
CONFIDENCE_ORDER = ("needs_revalidation", "low", "medium", "high")
ROUTES = {
    "undecided", "market_issue_watch", "formal_note_candidate",
    "hypothesis_candidate", "event_anchor_candidate", "policy_watch",
}
DIRECTIONS = {"tailwind", "headwind", "mixed", "uncertain"}
NOTE_ACTIONS = {"none", "watch", "review_due", "update_required", "done"}
ACTIVE_NOTE_ACTIONS = {"watch", "review_due", "update_required"}
ALLOWED_TRANSITIONS = {
    "initial": {"inbox"},
    "inbox": {"inbox", "triaged", "dismissed"},
    "triaged": {"triaged", "promoted", "dismissed", "resolved"},
    "promoted": {"promoted", "resolved"},
    "dismissed": {"triaged"},
    "resolved": {"triaged"},
}


def _parse_fields(body):
    fields = {}
    for raw in body.strip().splitlines():
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def _csv_values(value):
    return [part.strip() for part in (value or "").split(",") if part.strip()]


def _semicolon_values(value):
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def _valid_date(value):
    try:
        dt.date.fromisoformat(value)
        return True
    except (TypeError, ValueError):
        return False


def _transition_source_ids(evidence):
    """Return strict revision evidence ids; ``source_chain`` is initial-only."""
    match = re.fullmatch(r"sources:(S[1-9]\d*(?:,S[1-9]\d*)*)", evidence or "")
    return _csv_values(match.group(1)) if match else None


def _visible_history_lines(text):
    """保留可見文字的標點與 URL；逐行比對仍允許在任意位置追加新行。"""
    visible = re.sub(r"<!--.*?-->", "", text or "", flags=re.S)
    return [
        normalized
        for raw in visible.splitlines()
        if (normalized := re.sub(r"\s+", " ", raw).strip())
    ]


def _is_subsequence(before, after):
    """Whether every historical item is still present, in the original order."""
    cursor = iter(after)
    return all(any(candidate == item for candidate in cursor) for item in before)


def _canonical_source_url(value):
    """Normalize identity-only URL differences without erasing document selectors."""
    parsed = urlsplit(value or "")
    scheme = parsed.scheme.lower()
    host = (parsed.hostname or "").lower()
    try:
        port = parsed.port
    except ValueError:
        port = None
    if port and not (scheme == "https" and port == 443):
        host = f"{host}:{port}"
    path = re.sub(r"/{2,}", "/", parsed.path or "/")
    if path != "/":
        path = path.rstrip("/")
    query = urlencode(sorted(
        (key, item) for key, item in parse_qsl(parsed.query, keep_blank_values=True)
        if not key.lower().startswith("utm_")
        and key.lower() not in {"fbclid", "gclid", "mc_cid", "mc_eid"}
    ), doseq=True)
    return urlunsplit((scheme, host, path, query, ""))


def taipei_today():
    return dt.datetime.now(TAIPEI_TZ).date()


def _load_universe(path=UNIVERSE_CSV):
    with open(path, encoding="utf-8") as handle:
        return [row for row in csv.DictReader(handle) if row.get("stock_id")]


def _load_groups(path=GROUPS_CSV):
    with open(path, encoding="utf-8") as handle:
        return {row["group"] for row in csv.DictReader(handle) if row.get("group")}


def _publisher_matches_url(publisher_domain, url):
    hostname = (urlparse(url).hostname or "").lower()
    domain = (publisher_domain or "").lower()
    return bool(domain and hostname and (hostname == domain or hostname.endswith("." + domain)))


def _source_independence_key(source):
    """用內容來源群組判斷獨立消息鏈；hosted filing 可用顯式 override。"""
    override = (source.get("independence_group") or "").strip().lower()
    if override:
        return override
    hostname = (urlparse(source.get("url") or "").hostname or "").lower()
    if hostname.startswith("www."):
        hostname = hostname[4:]
    parts = hostname.split(".")
    if len(parts) <= 2:
        return hostname
    common_second_level = {
        "com.tw", "org.tw", "net.tw", "gov.tw", "edu.tw",
        "co.uk", "org.uk", "com.au", "co.jp", "co.kr",
    }
    return ".".join(parts[-3:] if ".".join(parts[-2:]) in common_second_level
                    else parts[-2:])


def _heading_sections(text, level):
    """依 Markdown heading 切段；只處理研究 topic 需要的 H2/H3 結構。"""
    marks = "#" * level
    pattern = re.compile(rf"^{re.escape(marks)}\s+(.+?)\s*$", re.M)
    matches = list(pattern.finditer(text))
    return [
        (match.group(1).strip(), text[match.end():matches[index + 1].start()]
         if index + 1 < len(matches) else text[match.end():])
        for index, match in enumerate(matches)
    ]


def _top_level_bullets(body):
    return [
        match.group(1).strip()
        for match in re.finditer(r"^-\s+(.+?)\s*$", body, re.M)
    ]


def _visible_markdown_text(body):
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", body)
    body = re.sub(r"[*_`#>|-]+", " ", body)
    return re.sub(r"\s+", " ", body).strip()


def _validate_beginner_section(text):
    """schema v2+ 的新手導讀是內容契約，不只檢查標題存在。"""
    errors = []
    h2_sections = _heading_sections(text, 2)
    beginner = [(index, body) for index, (heading, body) in enumerate(h2_sections)
                if heading == BEGINNER_HEADING]
    if len(beginner) != 1:
        return [f"schema v2+ 必須且只能有一個 H2：{BEGINNER_HEADING}"]
    index, body = beginner[0]
    if index != 0:
        errors.append(f"schema v2+ 的第一個 H2 必須是：{BEGINNER_HEADING}")

    h3_sections = _heading_sections(body, 3)
    headings = [heading for heading, _section_body in h3_sections]
    required_found = [heading for heading in headings if heading in BEGINNER_SUBHEADINGS]
    if required_found != list(BEGINNER_SUBHEADINGS):
        errors.append(
            "新手導讀 H3 必須依序包含：" + "、".join(BEGINNER_SUBHEADINGS))
    for heading in BEGINNER_SUBHEADINGS:
        if headings.count(heading) != 1:
            errors.append(f"新手導讀必須且只能有一個 H3：{heading}")

    bodies = {heading: section_body for heading, section_body in h3_sections}
    glossary = _top_level_bullets(bodies.get("名詞小字典", ""))
    glossary_pattern = re.compile(r"^\*\*[^*]+\*\*[：:].+")
    if len(glossary) < 3 or any(not glossary_pattern.match(item) for item in glossary):
        errors.append("名詞小字典至少需要 3 個「- **術語**：白話解釋」")

    summary = _top_level_bullets(bodies.get("三句話抓重點", ""))
    if len(summary) != 3:
        errors.append("三句話抓重點必須恰好有 3 個頂層 bullet")
    elif any(len(_visible_markdown_text(item)) < 12 for item in summary):
        errors.append("三句話抓重點每句至少需要 12 個可見字元")

    if len(_visible_markdown_text(bodies.get("為什麼重要", ""))) < 40:
        errors.append("為什麼重要至少需要 40 個可見字元，說明與讀者判斷的關係")

    tracking = _top_level_bullets(bodies.get("接下來怎麼追", ""))
    if len(tracking) < 2:
        errors.append("接下來怎麼追至少需要 2 個可觀察節點")

    questions = _top_level_bullets(bodies.get("想一想", ""))
    if len(questions) < 2 or any(not item.rstrip().endswith(("？", "?")) for item in questions):
        errors.append("想一想至少需要 2 個以問號結尾的問題")
    return errors


def _topic_summary(text):
    """v2+ 用三句導讀形成列表摘要；v1 保持空值，由既有 UI fallback 處理。"""
    h2 = dict(_heading_sections(text, 2))
    beginner = h2.get(BEGINNER_HEADING, "")
    h3 = dict(_heading_sections(beginner, 3))
    return " ".join(
        _visible_markdown_text(item)
        for item in _top_level_bullets(h3.get("三句話抓重點", ""))
    ).strip()


def _require_fields(item, required, label, errors):
    for key in required:
        if not item.get(key):
            errors.append(f"{label} 缺少必填欄位:{key}")


def _parse_contract_fields(body, allowed, label, errors):
    """v3 block 採 strict key:value；拒絕壞行、未知欄位與重複 key。"""
    fields = {}
    for line_no, raw in enumerate(body.strip().splitlines(), 1):
        if not raw.strip():
            continue
        if ":" not in raw:
            errors.append(f"{label} 第 {line_no} 行不是 key:value")
            continue
        key, value = (part.strip() for part in raw.split(":", 1))
        if not key:
            errors.append(f"{label} 第 {line_no} 行 key 空白")
            continue
        if key not in allowed:
            errors.append(f"{label} 含未知欄位:{key}")
        if key in fields:
            errors.append(f"{label} 欄位重複:{key}")
        fields[key] = value
    return fields


def _referenced_ids(value, known_ids, label, errors, required=True):
    ids = _csv_values(value)
    if required and not ids:
        errors.append(f"{label} 至少需要一個 evidence/source id")
    for source_id in ids:
        if source_id not in known_ids:
            errors.append(f"{label} 找不到 source id:{source_id}")
    return ids


def _topic_confidence(meta, last_evidence_at=None, as_of=None):
    """保留人工宣告值；活躍 topic 逾期且未更新證據時只自動降一級。"""
    as_of = as_of or taipei_today()
    declared = meta.get("base_confidence")
    due = meta.get("review_due")
    active = meta.get("status") not in {"dismissed", "resolved"}
    stale = bool(
        active and declared in CONFIDENCE_ORDER and _valid_date(due)
        and _valid_date(last_evidence_at) and as_of > dt.date.fromisoformat(due)
        and dt.date.fromisoformat(last_evidence_at) <= dt.date.fromisoformat(due)
    )
    effective = declared
    if stale and declared in CONFIDENCE_ORDER:
        effective = CONFIDENCE_ORDER[max(0, CONFIDENCE_ORDER.index(declared) - 1)]
    days_overdue = ((as_of - dt.date.fromisoformat(due)).days
                    if stale and _valid_date(due) else 0)
    return {
        "declared": declared or "unrated",
        "declared_label": CONFIDENCE_LABELS.get(declared, "未評級"),
        "effective": effective or "unrated",
        "effective_label": CONFIDENCE_LABELS.get(effective, "未評級"),
        "stale": stale,
        "days_overdue": days_overdue,
        "reason": "overdue_no_new_evidence" if stale else "current",
        "as_of": as_of.isoformat(),
        "last_evidence_at": last_evidence_at or "-",
        "review_due": due or "-",
        "basis": meta.get("confidence_basis") or "",
    }


def _analyse_v3_contract(text, meta, errors, warnings, as_of):
    """解析可持續驗證契約；所有結構均保留在 Markdown 的 append-friendly blocks。"""
    is_closed = meta.get("status") in {"dismissed", "resolved"}
    sources, source_ids = [], set()
    source_allowed = {
        "source_id", "role", "publisher", "title", "published_at", "captured_at",
        "accepted_at", "status", "url", "locator", "limitation", "source_kind",
        "independence_group",
    }
    source_required = (
        "source_id", "role", "publisher", "title", "captured_at",
        "accepted_at", "status", "url", "locator", "limitation",
    )
    for idx, body in enumerate(SOURCE_RE.findall(text), 1):
        label = f"research_source {idx}"
        source = _parse_contract_fields(body, source_allowed, label, errors)
        _require_fields(source, source_required, label, errors)
        source_id = source.get("source_id", "")
        if source_id and not SOURCE_ID_RE.fullmatch(source_id):
            errors.append(f"{label} source_id 格式錯誤:{source_id}")
        elif source_id in source_ids:
            errors.append(f"{label} source_id 重複:{source_id}")
        else:
            source_ids.add(source_id)
        if source.get("role") and source["role"] not in SOURCE_ROLES:
            errors.append(f"{label} role 不在值域:{source['role']}")
        source["source_kind"] = source.get("source_kind") or "document"
        if source["source_kind"] not in SOURCE_KINDS:
            errors.append(f"{label} source_kind 不在值域:{source['source_kind']}")
        if source["source_kind"] == "document" and not source.get("published_at"):
            errors.append(f"{label} document 缺少必填欄位:published_at")
        if source["source_kind"] == "living_index" and source.get("published_at"):
            errors.append(f"{label} living_index 的 published_at 必須留空")
        if source.get("status") and source["status"] not in SOURCE_STATUSES:
            errors.append(f"{label} status 不在值域:{source['status']}")
        for key in ("published_at", "captured_at", "accepted_at"):
            if source.get(key) and not _valid_date(source[key]):
                errors.append(f"{label} {key} 不是 YYYY-MM-DD:{source[key]}")
            elif (_valid_date(source.get(key))
                  and dt.date.fromisoformat(source[key]) > as_of):
                errors.append(f"{label} {key} 晚於研究判定日 {as_of.isoformat()}")
        captured, accepted = source.get("captured_at"), source.get("accepted_at")
        if (all(_valid_date(value) for value in (captured, accepted))
                and captured > accepted):
            errors.append(f"{label} 日期必須符合 captured_at <= accepted_at")
        published = source.get("published_at")
        if (all(_valid_date(value) for value in (published, captured))
                and published > captured):
            errors.append(f"{label} 日期必須符合 published_at <= captured_at")
        url = source.get("url", "")
        parsed = urlparse(url)
        if url and (parsed.scheme != "https" or not parsed.hostname):
            errors.append(f"{label} url 必須是有效 https URL")
        source["id"] = source_id
        source["document"] = source.get("title", "")
        sources.append(source)
    active_sources = [source for source in sources if source.get("status") == "active"]
    minimum_active_sources = 1 if is_closed else 2
    if len(active_sources) < minimum_active_sources:
        errors.append(
            f"schema v3 至少需要 {minimum_active_sources} 個 active research_source")
    active_urls = [source.get("url") for source in active_sources if source.get("url")]
    active_url_keys = [_canonical_source_url(url) for url in active_urls]
    if len(active_url_keys) != len(set(active_url_keys)):
        errors.append("schema v3 active research_source 不可重複使用同一 URL")
    if len(set(active_url_keys)) < minimum_active_sources:
        errors.append(
            f"schema v3 至少需要 {minimum_active_sources} 個不同 URL 的 active research_source")

    visible_text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    linked_urls = set(re.findall(r"\]\((https://[^)]+)\)", visible_text))
    all_source_urls = {source.get("url") for source in sources if source.get("url")}
    missing_link_sources = sorted(linked_urls - all_source_urls)
    if missing_link_sources:
        errors.append(
            "正文 Markdown 來源連結未納入 research_source ledger:" +
            "、".join(missing_link_sources))

    source_by_id = {source.get("source_id"): source for source in sources}

    def source_refs(value, label, required=True, require_active=True):
        ids = _referenced_ids(value, source_ids, label, errors, required=required)
        for source_id in ids:
            source = source_by_id.get(source_id) or {}
            if require_active and source.get("status") != "active":
                errors.append(f"{label} 引用非 active source:{source_id}")
        return ids

    claims, claim_ids = [], set()
    claim_allowed = {
        "claim_id", "label", "claim", "supporting_source_ids", "contrary_source_ids",
        "as_of", "basis", "boundary", "verification_needed", "resolution", "status",
        "correction_kind", "corrects_claim_id", "corrected_by_claim_id",
    }
    claim_required = (
        "claim_id", "label", "status", "claim", "as_of", "basis", "boundary")
    for idx, body in enumerate(CLAIM_RE.findall(text), 1):
        label = f"research_claim {idx}"
        claim = _parse_contract_fields(body, claim_allowed, label, errors)
        _require_fields(claim, claim_required, label, errors)
        claim_id = claim.get("claim_id", "")
        if claim_id and not CLAIM_ID_RE.fullmatch(claim_id):
            errors.append(f"{label} claim_id 格式錯誤:{claim_id}")
        elif claim_id in claim_ids:
            errors.append(f"{label} claim_id 重複:{claim_id}")
        else:
            claim_ids.add(claim_id)
        if claim.get("label") and claim["label"] not in CLAIM_LABELS:
            errors.append(f"{label} label 不在值域:{claim['label']}")
        if claim.get("status") and claim["status"] not in CLAIM_STATUSES:
            errors.append(f"{label} status 不在值域:{claim['status']}")
        if claim.get("as_of") and not _valid_date(claim["as_of"]):
            errors.append(f"{label} as_of 不是 YYYY-MM-DD:{claim['as_of']}")
        elif (_valid_date(claim.get("as_of"))
              and dt.date.fromisoformat(claim["as_of"]) > as_of):
            errors.append(f"{label} as_of 晚於研究判定日 {as_of.isoformat()}")
        needs_support = claim.get("label") in {"verified", "inference"}
        is_active = claim.get("status") == "active"
        claim["supporting_source_ids"] = source_refs(
            claim.get("supporting_source_ids"), label, required=needs_support,
            require_active=is_active)
        claim["contrary_source_ids"] = source_refs(
            claim.get("contrary_source_ids"), label, required=False,
            require_active=is_active)
        if claim.get("label") == "verified" and claim["supporting_source_ids"]:
            eligible = [
                source_id for source_id in claim["supporting_source_ids"]
                if (source_by_id.get(source_id) or {}).get("role")
                in VERIFIED_SUPPORT_ROLES
            ]
            if not eligible:
                errors.append(
                    f"{label} verified 不可只由 media／market_estimate 支持")
        if _valid_date(claim.get("as_of")):
            for source_id in (claim["supporting_source_ids"]
                              + claim["contrary_source_ids"]):
                source = source_by_id.get(source_id) or {}
                source_as_of = source.get("published_at") or source.get("captured_at")
                if (_valid_date(source_as_of) and source_as_of > claim["as_of"]):
                    errors.append(
                        f"{label} as_of 早於引用來源 {source_id} 的資訊日期 {source_as_of}")
        if claim.get("label") == "unverified" and not claim.get("verification_needed"):
            errors.append(f"{label} 待驗證 claim 必須填 verification_needed")
        if (claim.get("label") == "verified" and claim["contrary_source_ids"]
                and not claim.get("resolution")):
            errors.append(f"{label} 有 contrary source 時必須填 resolution")
        claim["label_text"] = CLAIM_LABELS.get(claim.get("label"), claim.get("label", ""))
        claim["status_text"] = {
            "active": "現行", "superseded": "已取代", "refuted": "已推翻",
        }.get(claim.get("status"), claim.get("status", ""))
        claims.append(claim)
    active_claims = [claim for claim in claims if claim.get("status") == "active"]
    if is_closed:
        if not active_claims:
            errors.append("closed schema v3 至少需要 1 個 active final claim")
        if any(claim.get("label") == "unverified" for claim in active_claims):
            errors.append("closed schema v3 不可保留 active unverified claim")
    else:
        if len(active_claims) < 2:
            errors.append("schema v3 至少需要 2 個 active research_claim")
        missing_labels = {"verified", "unverified"} - {
            claim.get("label") for claim in active_claims}
        if missing_labels:
            errors.append(
                "schema v3 的 claim ledger 至少必須包含證實與待驗證；缺少:"
                + "、".join(
                    CLAIM_LABELS[label] for label in CLAIM_LABELS
                    if label in missing_labels))

    claim_by_id = {claim.get("claim_id"): claim for claim in claims}
    active_claim_source_ids = {
        source_id
        for claim in active_claims
        for key in ("supporting_source_ids", "contrary_source_ids")
        for source_id in claim.get(key, [])
        if (source_by_id.get(source_id) or {}).get("status") == "active"
    }
    minimum_claim_sources = 1 if is_closed else 2
    if len(active_claim_source_ids) < minimum_claim_sources:
        errors.append(
            f"schema v3 至少需要 {minimum_claim_sources} 個被 active claim 實際引用的來源")
    thesis_claim_id = meta.get("thesis_claim_id")
    if thesis_claim_id not in claim_by_id:
        errors.append(f"schema v3 thesis_claim_id 找不到:{thesis_claim_id or '-'}")
    else:
        thesis_claim = claim_by_id[thesis_claim_id]
        if thesis_claim.get("status") != "active":
            errors.append("schema v3 thesis_claim_id 必須指向 active claim")
        if thesis_claim.get("label") == "unverified":
            errors.append("schema v3 thesis_claim_id 不可指向 unverified claim")
        thesis_source_ids = {
            source_id
            for key in ("supporting_source_ids", "contrary_source_ids")
            for source_id in thesis_claim.get(key, [])
            if (source_by_id.get(source_id) or {}).get("status") == "active"
        }
        independence = {
            _source_independence_key(source_by_id[source_id])
            for source_id in thesis_source_ids if source_id in source_by_id
        }
        if len(independence) < 2:
            warnings.append(
                "schema v3 主命題證據只有一個獨立來源群組；尚未形成交叉驗證")

    forward_links = {}
    reverse_links = {}
    for claim in claims:
        claim_id = claim.get("claim_id")
        kind = claim.get("correction_kind") or ""
        target_id = claim.get("corrects_claim_id") or ""
        corrected_by = claim.get("corrected_by_claim_id") or ""
        if bool(kind) != bool(target_id):
            errors.append(
                f"research_claim {claim_id} correction_kind 與 corrects_claim_id 必須同時填寫")
        elif kind:
            if kind not in {"supersedes", "refutes"}:
                errors.append(
                    f"research_claim {claim_id} correction_kind 不在值域:{kind}")
            elif not CLAIM_ID_RE.fullmatch(target_id):
                errors.append(
                    f"research_claim {claim_id} corrects_claim_id 格式錯誤:{target_id}")
            else:
                forward_links[claim_id] = (kind, target_id)
            if f"correction_of:{target_id}" not in (claim.get("basis") or ""):
                errors.append(
                    f"research_claim {claim_id} basis 必須標明 correction_of:{target_id}")
        elif re.search(r"(?<![A-Z0-9])correction_of:C[1-9]\d*", claim.get("basis") or ""):
            errors.append(
                f"research_claim {claim_id} basis 有 correction_of 但缺少結構化修正欄位")
        if corrected_by:
            if not CLAIM_ID_RE.fullmatch(corrected_by):
                errors.append(
                    f"research_claim {claim_id} corrected_by_claim_id 格式錯誤:{corrected_by}")
            else:
                reverse_links[claim_id] = corrected_by
        if claim.get("status") in {"superseded", "refuted"} and not corrected_by:
            errors.append(
                f"research_claim {claim_id} 歷史狀態必須填 corrected_by_claim_id")
        if claim.get("status") == "active" and corrected_by:
            errors.append(
                f"research_claim {claim_id} active 狀態不可填 corrected_by_claim_id")
    for claim_id, (verb, target_id) in forward_links.items():
        target = claim_by_id.get(target_id)
        expected_status = "superseded" if verb == "supersedes" else "refuted"
        if not target:
            errors.append(f"research_claim {claim_id} corrects_claim_id 找不到:{target_id}")
        elif target_id == claim_id:
            errors.append(f"research_claim {claim_id} 不可修正自己")
        elif target.get("status") != expected_status:
            errors.append(
                f"research_claim {claim_id} 的 {verb} 目標必須標為 {expected_status}")
        if reverse_links.get(target_id) != claim_id:
            errors.append(
                f"research_claim {claim_id} 與 {target_id} 的修正關係未雙向對齊")
    for claim_id, correcting_id in reverse_links.items():
        expected_kind = (
            "supersedes" if (claim_by_id.get(claim_id) or {}).get("status") == "superseded"
            else "refutes")
        if forward_links.get(correcting_id) != (expected_kind, claim_id):
            errors.append(
                f"research_claim {claim_id} 與 {correcting_id} 的修正關係未雙向對齊")

    for start_id in forward_links:
        seen_chain = set()
        current_id = start_id
        while current_id in forward_links:
            if current_id in seen_chain:
                errors.append(f"research_claim 修正關係形成循環:{start_id}")
                break
            seen_chain.add(current_id)
            current_id = forward_links[current_id][1]

    comparisons, observation_ids = [], set()
    comparison_allowed = {
        "comparison_id", "observation_id", "claim_id", "entity", "metric",
        "reported_value", "period_start", "period_end", "period_basis", "unit",
        "definition_key", "definition", "evidence_ids", "comparability",
        "comparability_reason", "normalization_method", "normalized_value",
        "normalized_unit", "comparison_kind", "value_kind",
        "normalized_period_start", "normalized_period_end",
        "normalized_definition_key",
    }
    comparison_required = (
        "comparison_id", "observation_id", "claim_id", "entity", "metric",
        "reported_value", "period_start", "period_end", "period_basis", "unit",
        "definition_key", "definition", "evidence_ids", "comparability",
        "comparability_reason",
    )
    for idx, body in enumerate(COMPARISON_RE.findall(text), 1):
        label = f"metric_comparison {idx}"
        comparison = _parse_contract_fields(body, comparison_allowed, label, errors)
        _require_fields(comparison, comparison_required, label, errors)
        comparison_id = comparison.get("comparison_id", "")
        if comparison_id and not COMPARISON_ID_RE.fullmatch(comparison_id):
            errors.append(f"{label} comparison_id 格式錯誤:{comparison_id}")
        observation_id = comparison.get("observation_id", "")
        if observation_id and not OBSERVATION_ID_RE.fullmatch(observation_id):
            errors.append(f"{label} observation_id 格式錯誤:{observation_id}")
        elif observation_id in observation_ids:
            errors.append(f"{label} observation_id 重複:{observation_id}")
        else:
            observation_ids.add(observation_id)
        if (comparison_id and observation_id
                and not observation_id.startswith(comparison_id + "-O")):
            errors.append(f"{label} observation_id 必須隸屬 comparison_id")
        if comparison.get("claim_id") not in claim_by_id:
            errors.append(f"{label} 找不到 claim_id:{comparison.get('claim_id') or '-'}")
        linked_claim = claim_by_id.get(comparison.get("claim_id")) or {}
        for key in ("period_start", "period_end"):
            if comparison.get(key) and not _valid_date(comparison[key]):
                errors.append(f"{label} {key} 不是 YYYY-MM-DD:{comparison[key]}")
        if (all(_valid_date(comparison.get(key)) for key in ("period_start", "period_end"))
                and comparison["period_start"] > comparison["period_end"]):
            errors.append(f"{label} period_start 不可晚於 period_end")
        if _valid_date(comparison.get("period_end")):
            if (_valid_date(linked_claim.get("as_of"))
                    and comparison["period_end"] > linked_claim["as_of"]):
                errors.append(
                    f"{label} period_end 不可晚於關聯 claim as_of:"
                    f"{linked_claim['as_of']}")
            if dt.date.fromisoformat(comparison["period_end"]) > as_of:
                errors.append(
                    f"{label} period_end 晚於研究判定日 {as_of.isoformat()}")
        if (comparison.get("comparability")
                and comparison["comparability"] not in COMPARABILITY):
            errors.append(f"{label} comparability 不在值域:{comparison['comparability']}")
        comparison["value_kind"] = comparison.get("value_kind") or "point"
        if comparison["value_kind"] not in VALUE_KINDS:
            errors.append(f"{label} value_kind 不在值域:{comparison['value_kind']}")
        value = comparison.get("reported_value", "")
        number = r"-?\d+(?:\.\d+)?"
        if comparison["value_kind"] == "range":
            match = re.fullmatch(rf"({number})\.\.({number})", value)
            if not match:
                errors.append(f"{label} range reported_value 必須是 min..max 數字")
            elif float(match.group(1)) > float(match.group(2)):
                errors.append(f"{label} range reported_value 下限不可大於上限")
        elif not re.fullmatch(number, value):
            errors.append(f"{label} reported_value 必須是可重算數字")
        comparison["comparison_kind"] = comparison.get("comparison_kind") or "aligned_metric"
        if comparison["comparison_kind"] not in COMPARISON_KINDS:
            errors.append(
                f"{label} comparison_kind 不在值域:{comparison['comparison_kind']}")
        comparison["evidence_ids"] = source_refs(
            comparison.get("evidence_ids"), label,
            require_active=linked_claim.get("status") == "active")
        linked_evidence = set(
            linked_claim.get("supporting_source_ids", [])
            + linked_claim.get("contrary_source_ids", []))
        extra_evidence = set(comparison["evidence_ids"]) - linked_evidence
        if extra_evidence:
            errors.append(
                f"{label} evidence_ids 未納入關聯 claim 的證據鏈:"
                + ",".join(sorted(extra_evidence)))
        comparison["claim_status"] = linked_claim.get("status")
        if comparison.get("comparability") == "normalized_comparable":
            _require_fields(
                comparison, (
                    "normalization_method", "normalized_value", "normalized_unit",
                    "normalized_period_start", "normalized_period_end",
                    "normalized_definition_key",
                ),
                label, errors)
        if (comparison.get("normalized_value")
                and not re.fullmatch(number, comparison["normalized_value"])):
            errors.append(f"{label} normalized_value 必須是可重算數字")
        for key in ("normalized_period_start", "normalized_period_end"):
            if comparison.get(key) and not _valid_date(comparison[key]):
                errors.append(f"{label} {key} 不是 YYYY-MM-DD:{comparison[key]}")
        if (all(_valid_date(comparison.get(key)) for key in (
                "normalized_period_start", "normalized_period_end"))
                and comparison["normalized_period_start"]
                > comparison["normalized_period_end"]):
            errors.append(
                f"{label} normalized_period_start 不可晚於 normalized_period_end")
        if _valid_date(comparison.get("normalized_period_end")):
            if (_valid_date(linked_claim.get("as_of"))
                    and comparison["normalized_period_end"] > linked_claim["as_of"]):
                errors.append(
                    f"{label} normalized_period_end 不可晚於關聯 claim as_of:"
                    f"{linked_claim['as_of']}")
            if dt.date.fromisoformat(comparison["normalized_period_end"]) > as_of:
                errors.append(
                    f"{label} normalized_period_end 晚於研究判定日 "
                    f"{as_of.isoformat()}")
        comparison["comparability_text"] = COMPARABILITY.get(
            comparison.get("comparability"), comparison.get("comparability", ""))
        comparisons.append(comparison)
    has_cross_company = meta.get("cross_company_numbers")
    if has_cross_company not in {"true", "false"}:
        errors.append("schema v3 cross_company_numbers 必須是 true 或 false")
    elif has_cross_company == "true" and not comparisons:
        errors.append("cross_company_numbers=true 時至少需要一個 metric_comparison")
    elif has_cross_company == "false" and comparisons:
        errors.append("cross_company_numbers=false 不可同時宣告 metric_comparison")

    grouped = defaultdict(list)
    for observation in comparisons:
        grouped[observation.get("comparison_id")].append(observation)
    for comparison_id, rows in grouped.items():
        label = f"metric_comparison {comparison_id}"
        if len({row.get("entity") for row in rows}) < 2:
            errors.append(f"{label} 至少需要 2 個不同 entity")
        if len(rows) != len({row.get("entity") for row in rows}):
            errors.append(f"{label} 同一 entity 不可重複 observation")
        for key in ("claim_id", "comparability", "comparison_kind"):
            if len({row.get(key) for row in rows}) != 1:
                errors.append(f"{label} 所有 observation 的 {key} 必須一致")
        kind = rows[0].get("comparison_kind") if rows else "aligned_metric"
        if kind == "aligned_metric" and len({row.get("metric") for row in rows}) != 1:
            errors.append(f"{label} aligned_metric 的 metric 必須一致")
        if kind == "heterogeneous_evidence":
            if rows and rows[0].get("comparability") != "not_comparable":
                errors.append(
                    f"{label} heterogeneous_evidence 只能標為 not_comparable")
            if len({row.get("metric") for row in rows}) < 2:
                errors.append(
                    f"{label} heterogeneous_evidence 至少需要 2 種不同 metric")
        if rows and rows[0].get("comparability") == "directly_comparable":
            for key in (
                    "period_start", "period_end", "period_basis", "unit",
                    "definition_key", "definition"):
                if len({row.get(key) for row in rows}) != 1:
                    errors.append(f"{label} 標為可直接比較但 {key} 不一致")
        if rows and rows[0].get("comparability") == "normalized_comparable":
            for key in (
                    "normalized_unit", "normalized_period_start", "normalized_period_end",
                    "normalized_definition_key"):
                if len({row.get(key) for row in rows}) != 1:
                    errors.append(f"{label} 正規化後的 {key} 必須一致")
        if not re.search(rf"(?<![A-Z0-9]){re.escape(comparison_id)}(?![A-Z0-9-])", visible_text):
            errors.append(
                f"{label} 必須在可見正文以 ID 標註對應的跨公司數字段落")

    monitoring, monitor_ids = [], set()
    monitor_allowed = {
        "monitor_id", "claim_ids", "metric", "source_ids", "frequency", "next_check",
        "trigger", "invalidation", "status", "frequency_detail", "retired_at",
        "retirement_reason", "watch_source_ids",
    }
    monitor_required = (
        "monitor_id", "status", "claim_ids", "metric", "source_ids", "frequency",
        "next_check", "trigger", "invalidation",
    )
    for idx, body in enumerate(MONITOR_RE.findall(text), 1):
        label = f"monitoring_item {idx}"
        monitor = _parse_contract_fields(body, monitor_allowed, label, errors)
        _require_fields(monitor, monitor_required, label, errors)
        monitor_id = monitor.get("monitor_id", "")
        if monitor_id and not MONITOR_ID_RE.fullmatch(monitor_id):
            errors.append(f"{label} monitor_id 格式錯誤:{monitor_id}")
        elif monitor_id in monitor_ids:
            errors.append(f"{label} monitor_id 重複:{monitor_id}")
        else:
            monitor_ids.add(monitor_id)
        if monitor.get("status") and monitor["status"] not in MONITOR_STATUSES:
            errors.append(f"{label} status 不在值域:{monitor['status']}")
        is_active = monitor.get("status") == "active"
        monitor["source_ids"] = source_refs(
            monitor.get("source_ids"), label, require_active=is_active)
        monitor["watch_source_ids"] = source_refs(
            monitor.get("watch_source_ids"), label, required=is_active,
            require_active=is_active)
        if (is_active and monitor["watch_source_ids"]
                and not any(
                    (source_by_id.get(source_id) or {}).get("source_kind")
                    == "living_index"
                    for source_id in monitor["watch_source_ids"])):
            errors.append(
                f"{label} active monitor 的 watch_source_ids 至少需要一個 living_index")
        monitor["claim_ids"] = _csv_values(monitor.get("claim_ids"))
        if not monitor["claim_ids"]:
            errors.append(f"{label} 至少需要一個 claim_id")
        for claim_id in monitor["claim_ids"]:
            if claim_id not in claim_by_id:
                errors.append(f"{label} 找不到 claim_id:{claim_id}")
            elif is_active and claim_by_id[claim_id].get("status") != "active":
                errors.append(f"{label} active monitor 不可追蹤歷史 claim:{claim_id}")
        if monitor.get("frequency") and monitor["frequency"] not in MONITOR_FREQUENCIES:
            errors.append(f"{label} frequency 不在值域:{monitor['frequency']}")
        if monitor.get("next_check") and not _valid_date(monitor["next_check"]):
            errors.append(f"{label} next_check 不是 YYYY-MM-DD:{monitor['next_check']}")
        if monitor.get("status") == "retired":
            _require_fields(
                monitor, ("retired_at", "retirement_reason"), label, errors)
            if monitor.get("retired_at") and not _valid_date(monitor["retired_at"]):
                errors.append(f"{label} retired_at 不是 YYYY-MM-DD:{monitor['retired_at']}")
            elif (_valid_date(monitor.get("retired_at"))
                  and dt.date.fromisoformat(monitor["retired_at"]) > as_of):
                errors.append(f"{label} retired_at 晚於研究判定日 {as_of.isoformat()}")
        monitoring.append(monitor)
    active_monitoring = [item for item in monitoring if item.get("status") == "active"]
    if is_closed and active_monitoring:
        errors.append("closed schema v3 不可保留 active monitoring_item")
    elif not is_closed and len(active_monitoring) < 2:
        errors.append("schema v3 至少需要 2 個 active monitoring_item")

    signatures = set()
    for monitor in active_monitoring:
        signature = (
            tuple(monitor.get("claim_ids") or []), monitor.get("metric"),
            tuple(monitor.get("source_ids") or []), monitor.get("frequency"),
            tuple(monitor.get("watch_source_ids") or []),
            monitor.get("next_check"), monitor.get("trigger"), monitor.get("invalidation"),
        )
        if signature in signatures:
            errors.append("active monitoring_item 不可只改 ID 後重複")
        signatures.add(signature)

    due_dates = [monitor.get("next_check") for monitor in active_monitoring
                 if _valid_date(monitor.get("next_check"))]
    if not is_closed and due_dates and meta.get("review_due") != min(due_dates):
        errors.append("schema v3 review_due 必須等於所有 monitoring_item 最早的 next_check")

    ledger_referenced = {
        source_id
        for claim in active_claims
        for key in ("supporting_source_ids", "contrary_source_ids")
        for source_id in claim.get(key, [])
        if (source_by_id.get(source_id) or {}).get("status") == "active"
    }
    def _evidence_clock(referenced):
        """Clock follows publication recency; accepted_at only breaks ties.

        Taking max(accepted_at) alone let a newly located but OLD document refresh
        freshness, because accepted_at is whatever day the researcher accepted it.
        A back-filled source strengthens independent source chains, but it is not
        newer evidence, so only the newest-published sources may set the clock.
        A living_index has no published_at; its captured_at is the observation date.
        """
        dated = []
        for source_id in referenced:
            source = source_by_id[source_id]
            accepted = source.get("accepted_at")
            effective = source.get("published_at") or source.get("captured_at")
            if _valid_date(accepted) and _valid_date(effective):
                dated.append((effective, accepted))
        if not dated:
            return None
        newest_published = max(item[0] for item in dated)
        return max(accepted for effective, accepted in dated
                   if effective == newest_published)

    ledger_last_evidence_at = _evidence_clock(ledger_referenced)
    thesis = claim_by_id.get(thesis_claim_id) or {}
    thesis_referenced = {
        source_id
        for key in ("supporting_source_ids", "contrary_source_ids")
        for source_id in thesis.get(key, [])
        if (source_by_id.get(source_id) or {}).get("status") == "active"
    }
    last_evidence_at = _evidence_clock(thesis_referenced)
    if not last_evidence_at:
        errors.append("schema v3 無法由 active thesis claim source 推導 last_evidence_at")
    if (_valid_date(last_evidence_at) and _valid_date(meta.get("last_reviewed_at"))
            and last_evidence_at > meta["last_reviewed_at"]):
        errors.append("衍生 last_evidence_at 不可晚於 last_reviewed_at")
    if (_valid_date(last_evidence_at) and _valid_date(meta.get("review_due"))
            and last_evidence_at >= meta["review_due"]):
        errors.append("新增 evidence 後必須把 review_due 往 last_evidence_at 之後移動")

    return (sources, claims, comparisons, monitoring, last_evidence_at,
            ledger_last_evidence_at)


def _hypothesis_ids(reports):
    return {
        f"{sid}:{item['id']}"
        for sid, report in reports.items()
        for item in report.get("hypotheses", [])
    }


def analyse_topic(path, text, universe_rows=None, group_ids=None, reports=None, as_of=None):
    """解析單一候選議題；議題只負責路由，不把主張升格成正式公司事實。"""
    universe_rows = universe_rows if universe_rows is not None else _load_universe()
    group_ids = group_ids if group_ids is not None else _load_groups()
    reports = reports or {}
    universe = {row["stock_id"]: row for row in universe_rows}
    known_hypotheses = _hypothesis_ids(reports)
    errors, warnings = [], []
    if as_of is None:
        as_of = taipei_today()
    elif isinstance(as_of, dt.datetime):
        as_of = as_of.date()
    elif isinstance(as_of, str) and _valid_date(as_of):
        as_of = dt.date.fromisoformat(as_of)
    elif not isinstance(as_of, dt.date):
        errors.append("as_of 必須是 date、datetime 或 YYYY-MM-DD")
        as_of = taipei_today()
    matches = TOPIC_META_RE.findall(text)
    if len(matches) != 1:
        errors.append("每個議題必須且只能有一個 research_topic meta")
    raw_meta = matches[0] if matches else ""
    version_values = re.findall(
        r"^\s*schema_version\s*:\s*([^\r\n]+?)\s*$", raw_meta, re.M)
    if len(version_values) != 1:
        errors.append("research_topic meta 的 schema_version 必須且只能出現一次")
    # 任一重複值宣告 v3 時仍走最嚴格 parser，不能用最後一個 v2 覆蓋繞過契約。
    schema_version = (version_values[0] if len(version_values) == 1
                      else "3" if "3" in version_values
                      else version_values[-1] if version_values else "")
    meta = _parse_fields(raw_meta) if matches else {}
    if schema_version == "3" and matches:
        meta_allowed = {
            "topic_id", "schema_version", "status", "priority", "captured_at",
            "source_published_at", "last_reviewed_at", "review_due", "source_type",
            "publisher", "publisher_domain", "canonical_url", "source_chain_id",
            "stock_ids", "group_ids", "trigger_type", "evidence_role", "route",
            "thesis_claim_id", "base_confidence", "confidence_basis",
            "cross_company_numbers", "schema_migrated_at",
        }
        meta = _parse_contract_fields(
            matches[0], meta_allowed, "research_topic meta", errors)
    if schema_version:
        meta["schema_version"] = schema_version
    required = (
        "topic_id", "schema_version", "status", "priority", "captured_at",
        "source_published_at", "last_reviewed_at", "review_due", "source_type",
        "publisher_domain", "canonical_url", "source_chain_id", "trigger_type",
        "evidence_role", "route",
    )
    for key in required:
        if not meta.get(key):
            errors.append(f"research_topic meta 缺少必填欄位:{key}")

    if schema_version == "3":
        for key in ("thesis_claim_id", "base_confidence", "confidence_basis",
                    "cross_company_numbers"):
            if not meta.get(key):
                errors.append(f"research_topic meta 缺少必填欄位:{key}")

    topic_id = meta.get("topic_id", "")
    if topic_id and not TOPIC_ID_RE.fullmatch(topic_id):
        errors.append(f"topic_id 格式錯誤:{topic_id}")
    schema_version = meta.get("schema_version")
    if schema_version and schema_version not in {"1", "2", "3"}:
        errors.append("schema_version 必須是 1、2 或 3")
    if (schema_version != "3" and _valid_date(meta.get("captured_at"))
            and dt.date.fromisoformat(meta["captured_at"]) >= V3_CUTOVER_DATE):
        errors.append(
            f"{V3_CUTOVER_DATE.isoformat()} 起新建議題必須使用 schema_version: 3")
    if schema_version in {"2", "3"}:
        errors.extend(_validate_beginner_section(text))
    if meta.get("status") and meta["status"] not in TOPIC_STATUSES:
        errors.append(f"status 不在值域:{meta['status']}")
    if meta.get("priority") and meta["priority"] not in TOPIC_PRIORITIES:
        errors.append(f"priority 不在值域:{meta['priority']}")
    if meta.get("source_type") and meta["source_type"] not in SOURCE_TYPES:
        errors.append(f"source_type 不在值域:{meta['source_type']}")
    if meta.get("evidence_role") and meta["evidence_role"] not in EVIDENCE_ROLES:
        errors.append(f"evidence_role 不在值域:{meta['evidence_role']}")
    if meta.get("route") and meta["route"] not in ROUTES:
        errors.append(f"route 不在值域:{meta['route']}")
    if (schema_version == "3" and meta.get("base_confidence")
            and meta["base_confidence"] not in {"high", "medium", "low"}):
        errors.append(f"base_confidence 不在值域:{meta['base_confidence']}")

    for key in ("source_published_at", "captured_at", "last_reviewed_at", "review_due",
                "schema_migrated_at"):
        value = meta.get(key)
        if value and not _valid_date(value):
            errors.append(f"{key} 不是 YYYY-MM-DD:{value}")
        elif (key != "review_due" and _valid_date(value)
              and dt.date.fromisoformat(value) > as_of):
            errors.append(f"{key} 晚於研究判定日 {as_of.isoformat()}")
    if (_valid_date(meta.get("source_published_at"))
            and _valid_date(meta.get("captured_at"))
            and meta["source_published_at"] > meta["captured_at"]):
        errors.append("source_published_at 不可晚於 captured_at")
    if (_valid_date(meta.get("captured_at"))
            and _valid_date(meta.get("last_reviewed_at"))
            and meta["last_reviewed_at"] < meta["captured_at"]):
        errors.append("last_reviewed_at 不可早於 captured_at")
    if (_valid_date(meta.get("captured_at"))
            and _valid_date(meta.get("review_due"))
            and meta["review_due"] < meta["captured_at"]):
        errors.append("review_due 不可早於 captured_at")
    if (schema_version == "3"
            and meta.get("status") not in {"dismissed", "resolved"}
            and _valid_date(meta.get("last_reviewed_at"))
            and _valid_date(meta.get("review_due"))
            and meta["review_due"] <= meta["last_reviewed_at"]):
        errors.append("schema v3 review_due 必須晚於 last_reviewed_at")

    canonical_url = meta.get("canonical_url", "")
    if canonical_url:
        parsed = urlparse(canonical_url)
        if parsed.scheme != "https" or not parsed.hostname:
            errors.append("canonical_url 必須是有效 https URL")
        elif not _publisher_matches_url(meta.get("publisher_domain"), canonical_url):
            errors.append("publisher_domain 與 canonical_url 主機不一致")

    declared_stocks = _csv_values(meta.get("stock_ids"))
    declared_groups = _csv_values(meta.get("group_ids"))
    for sid in declared_stocks:
        if sid not in universe:
            errors.append(f"stock_ids 含非 universe 成員:{sid}")
    for group_id in declared_groups:
        if group_id not in group_ids:
            errors.append(f"group_ids 含未知族群:{group_id}")

    impacts = []
    impact_stocks, impact_groups = set(), set()
    for idx, body in enumerate(IMPACT_RE.findall(text), 1):
        impact = _parse_fields(body)
        group_id = impact.get("group_id", "")
        stock_ids = _csv_values(impact.get("stock_ids"))
        hypothesis_refs = _csv_values(impact.get("hypothesis_refs"))
        if not group_id:
            errors.append(f"impact {idx} 缺少 group_id")
        elif group_id not in group_ids:
            errors.append(f"impact {idx} 未知 group_id:{group_id}")
        else:
            impact_groups.add(group_id)
        if impact.get("direction") not in DIRECTIONS:
            errors.append(f"impact {idx} direction 不在值域")
        action = impact.get("note_action")
        if action not in NOTE_ACTIONS:
            errors.append(f"impact {idx} note_action 不在值域")
        if action in ACTIVE_NOTE_ACTIONS:
            due = impact.get("action_due")
            if not _valid_date(due):
                errors.append(f"impact {idx} 的 {action} 必須有合法 action_due")
        if not impact.get("rationale"):
            errors.append(f"impact {idx} 缺少 rationale")
        if not impact.get("evidence_boundary"):
            errors.append(f"impact {idx} 缺少 evidence_boundary")
        for sid in stock_ids:
            impact_stocks.add(sid)
            if sid not in universe:
                errors.append(f"impact {idx} 含非 universe 成員:{sid}")
            elif group_id in group_ids and universe[sid]["group"] != group_id:
                errors.append(
                    f"impact {idx} 的 {sid} 實際屬 {universe[sid]['group']}，非 {group_id}")
        for ref in hypothesis_refs:
            if not HYPOTHESIS_REF_RE.fullmatch(ref):
                errors.append(f"impact {idx} hypothesis_ref 格式錯誤:{ref}")
            elif ref not in known_hypotheses:
                errors.append(f"impact {idx} 找不到 hypothesis_ref:{ref}")
        impact["stock_ids"] = stock_ids
        impact["hypothesis_refs"] = hypothesis_refs
        impacts.append(impact)

    if set(declared_stocks) != impact_stocks:
        errors.append("meta stock_ids 必須等於所有 impact stock_ids 聯集")
    if set(declared_groups) != impact_groups:
        errors.append("meta group_ids 必須等於所有 impact group_id 聯集")

    if schema_version == "3":
        transition_allowed = {"date", "from", "to", "reason", "evidence"}
        transitions = [
            _parse_contract_fields(
                body, transition_allowed, f"transition {idx}", errors)
            for idx, body in enumerate(TRANSITION_RE.findall(text), 1)
        ]
    else:
        transitions = [_parse_fields(body) for body in TRANSITION_RE.findall(text)]
    if not transitions:
        errors.append("議題必須保留至少一筆 transition")
    historical_replay = as_of < taipei_today()
    state, previous_date = "initial", None
    for idx, transition in enumerate(transitions, 1):
        value = transition.get("date")
        later_editorial_in_historical_replay = (
            historical_replay
            and transition.get("from") == transition.get("to")
            and EDITORIAL_EVIDENCE_RE.match(
                (transition.get("evidence") or "").strip())
        )
        if not _valid_date(value):
            errors.append(f"transition {idx} 日期不合法")
        elif (dt.date.fromisoformat(value) > as_of
              and not later_editorial_in_historical_replay):
            errors.append(f"transition {idx} 日期晚於研究判定日 {as_of.isoformat()}")
        elif previous_date and value < previous_date:
            errors.append(f"transition {idx} 日期早於前一筆")
        if transition.get("from") != state:
            errors.append(f"transition {idx} 未銜接上一狀態 {state}")
        target = transition.get("to", "")
        if target not in ALLOWED_TRANSITIONS.get(state, set()):
            errors.append(f"transition {idx} 不允許 {state}→{target}")
        if not transition.get("reason"):
            errors.append(f"transition {idx} 缺少 reason")
        if not transition.get("evidence"):
            errors.append(f"transition {idx} 缺少 evidence")
        state = target or state
        previous_date = value if _valid_date(value) else previous_date
    if transitions and meta.get("status") and state != meta["status"]:
        errors.append(f"最後 transition 狀態 {state} 與 meta status {meta['status']} 不一致")

    title_match = re.search(r"^#\s+(.+?)\s*$", TOPIC_META_RE.sub("", text), re.M)
    if not title_match:
        errors.append("議題缺少 H1 標題")
    title = title_match.group(1).strip() if title_match else os.path.basename(path)
    if not impacts:
        warnings.append("尚無 impact；在完成產業/個股映射前不可路由進正式筆記")

    sources, claims, comparisons, monitoring = [], [], [], []
    last_evidence_at = ledger_last_evidence_at = None
    if schema_version == "3":
        (sources, claims, comparisons, monitoring, last_evidence_at,
         ledger_last_evidence_at) = _analyse_v3_contract(
            text, meta, errors, warnings, as_of)
        analyse_readability(text, meta, errors, warnings)
        known_source_ids = {source.get("source_id") for source in sources}
        source_by_id = {source.get("source_id"): source for source in sources}
        for idx, transition in enumerate(transitions, 1):
            evidence = transition.get("evidence") or ""
            is_initial = idx == 1 and transition.get("from") == "initial"
            if is_initial:
                expected = f"source_chain:{meta.get('source_chain_id') or ''}"
                if evidence != expected:
                    errors.append(
                        f"transition {idx} initial evidence 必須等於 {expected}")
                continue
            if EDITORIAL_EVIDENCE_RE.match(evidence.strip()):
                if transition.get("from") != transition.get("to"):
                    errors.append(
                        f"transition {idx} editorial revision 不可改變 lifecycle 狀態")
                continue
            evidence_ids = _transition_source_ids(evidence)
            if evidence_ids is None:
                errors.append(
                    f"transition {idx} evidence 必須使用 sources:S1[,S2...]，"
                    "source_chain 僅限 initial transition")
                continue
            for source_id in evidence_ids:
                source = source_by_id.get(source_id)
                if source_id not in known_source_ids:
                    errors.append(f"transition {idx} evidence 找不到 source:{source_id}")
                    continue
                if (_valid_date(transition.get("date"))
                        and _valid_date((source or {}).get("accepted_at"))
                        and transition["date"] < source["accepted_at"]):
                    errors.append(
                        f"transition {idx} 日期早於 evidence {source_id} accepted_at")
        confidence = _topic_confidence(meta, last_evidence_at, as_of)
        if confidence["stale"]:
            warnings.append(
                f"review_due 已逾 {confidence['days_overdue']} 天且無新 evidence；"
                f"可信度自動由 {confidence['declared_label']} 降為"
                f"{confidence['effective_label']}")
    else:
        confidence = {
            "declared": "unstructured", "declared_label": "未結構化",
            "effective": "unstructured", "effective_label": "未結構化",
            "stale": False, "days_overdue": 0, "reason": "legacy_schema",
            "as_of": as_of.isoformat(), "last_evidence_at": "-",
            "review_due": meta.get("review_due") or "-", "basis": "舊制未建立 v3 帳本",
        }

    return {
        "path": path,
        "relpath": os.path.relpath(path, ROOT).replace("\\", "/"),
        "title": title,
        "summary": _topic_summary(text) if schema_version in {"2", "3"} else "",
        "meta": meta,
        "topic_id": topic_id,
        "status": meta.get("status"),
        "priority": meta.get("priority"),
        "captured_at": meta.get("captured_at"),
        "review_due": meta.get("review_due"),
        "stock_ids": declared_stocks,
        "group_ids": declared_groups,
        "impacts": impacts,
        "transitions": transitions,
        "sources": sources,
        "claims": claims,
        "comparisons": comparisons,
        "monitoring": monitoring,
        "last_evidence_at": last_evidence_at,
        "ledger_last_evidence_at": ledger_last_evidence_at,
        "confidence": confidence,
        "quality_errors": errors,
        "quality_warnings": warnings,
        "quality_invalid": bool(errors),
    }


def load_topics(topics_dir=TOPICS_DIR, universe_rows=None, group_ids=None, reports=None,
                as_of=None, require_v3=True):
    universe_rows = universe_rows if universe_rows is not None else _load_universe()
    group_ids = group_ids if group_ids is not None else _load_groups()
    reports = reports or {}
    topics, seen = [], {}
    if not os.path.isdir(topics_dir):
        return topics
    for path in sorted(glob.glob(os.path.join(topics_dir, "*.md"))):
        if os.path.basename(path).startswith("_"):
            continue
        with open(path, encoding="utf-8") as handle:
            topic = analyse_topic(
                path, handle.read(), universe_rows, group_ids, reports, as_of=as_of)
        if require_v3 and topic.get("meta", {}).get("schema_version") != "3":
            topic["quality_errors"].append(
                "live research register 僅接受 schema_version: 3；"
                "舊格式只供 analyse_topic 歷史相容")
            topic["quality_invalid"] = True
        if topic["topic_id"] in seen:
            topic["quality_errors"].append(
                f"topic_id 重複:{os.path.basename(seen[topic['topic_id']]['path'])}")
            topic["quality_invalid"] = True
            seen[topic["topic_id"]]["quality_errors"].append(
                f"topic_id 重複:{os.path.basename(path)}")
            seen[topic["topic_id"]]["quality_invalid"] = True
        else:
            seen[topic["topic_id"]] = topic
        topics.append(topic)
    return topics


READABILITY_CUTOVER = "2026-08-09"
READABILITY_PLAIN_LANGUAGE_CUTOVER = "2026-08-10"
READABILITY_HARD_USES = 5
READABILITY_SOFT_USES = 3
READABILITY_MIN_PROSE_RATIO = 0.50
READABILITY_MAX_LEAD_BLOCK_CHARS = 180

# Reader-facing ledger fields. title/locator/url are citation metadata: a reader
# does not need a document's English title glossed, so they are excluded.
READER_FACING_FIELDS = (
    "claim", "basis", "boundary", "verification_needed", "rationale",
    "evidence_boundary", "metric", "trigger", "invalidation", "confidence_basis",
)
# Abbreviations a Taiwan equity reader already shares with the author.
READABILITY_COMMON_TERMS = {
    "ai", "q1", "q2", "q3", "q4", "1h", "2h", "ir", "asp", "us", "eps", "ceo",
    "cfo", "gpu", "cpu", "odm", "oem", "pcb", "tam", "mou", "pdf", "url", "api",
    "csp", "hpc", "it", "ot", "id", "cagr", "yoy", "qoq", "roe", "capex", "r&d",
    "ip", "bom", "kpi", "nre", "mvp",
    # 單位與規模詞
    "gb", "tb", "mb", "kb", "kw", "mw", "gw", "multi-gw", "nm", "ghz", "mhz",
    "hz", "vdc", "vac", "kv", "ma", "usd", "twd", "jpy", "pcs", "sq", "ft",
    # 出現在英文片語裡、本身不是術語的常見英文字
    "supply", "chain", "status", "design", "reference", "production", "business",
    "review", "report", "guide", "overview", "summary", "note", "notes", "page",
    "table", "figure", "section", "appendix", "press", "release", "results",
    "quarter", "full", "year", "first", "second", "third", "fourth", "next",
    "and", "for", "with", "from", "the", "of", "in", "on", "to", "by", "at",
}
# C7 / S12 / T3 / M1-O2 / MI-2026-08-07-... are record IDs, not terms to look up.
_LEDGER_ID_RE = re.compile(
    r"^(?:[CSTM][1-9]\d*(?:-O[1-9]\d*)?|H\d+|MI-\d{4}-\d{2}-\d{2}-.*)$", re.I)
# 負向後查:避免把 "2nd" 切成 "nd"、"115Q2" 切成 "Q2"。
_LATIN_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9])[A-Za-z][A-Za-z0-9.\-]*")
_ANY_BLOCK_RE = re.compile(r"<!--(.*?)-->", re.S)
_MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\((?:[^()\s]|\([^)]*\))+\)")
_BARE_URL_RE = re.compile(r"https?://\S+", re.I)
READABILITY_INTERNAL_LEAD_PATTERNS = (
    ("active claim/source/monitor", re.compile(
        r"\bactive\s+(?:claim|source|monitor)s?\b", re.I)),
    ("內部狀態碼", re.compile(
        r"\b(?:update_required|review_due|bounded_proxy|not_disclosed|"
        r"independently_verified|early_trigger)\b", re.I)),
    ("內部研究欄位", re.compile(
        r"\b(?:impact route|evidence boundary|evidence posture|selection log|"
        r"focused evidence pack|independent reviewer|financial edge|curated edges?|"
        r"schema_version|registry|ledger|stale|watch)\b", re.I)),
    ("內部紀錄 ID", re.compile(
        r"(?<![A-Za-z0-9])(?:H\d+|(?:claim|monitor|impact|assessment)\s*ID)"
        r"(?![A-Za-z0-9-])", re.I)),
)

# 已發布文章原本只能靠「綁定 sources 的 revision transition」改寫正文，也就是預設
# 每次改寫都由新證據驅動。可讀性修正沒有新證據，於是唯一的路是假裝有——這會讓
# 文章一旦難讀就永遠難讀。editorial revision 是給這種情況的窄口：它只允許改敘述，
# 且必須證明沒有動到任何一條 source／claim／comparison／monitor 與所有 meta 時鐘。
EDITORIAL_EVIDENCE_RE = re.compile(r"^editorial:[a-z0-9_]+$")
EDITORIAL_LOCKED_META = (
    "thesis_claim_id", "base_confidence", "confidence_basis", "status",
    "review_due", "last_reviewed_at", "stock_ids", "group_ids", "route",
    "cross_company_numbers",
)


def _entity_terms(universe_rows=None):
    """Names already carried by the entity registries are entities, not jargon."""
    terms = set()
    files = (
        (os.path.join(ROOT, "config", "external_entities.csv"), ("label", "aliases")),
        (UNIVERSE_CSV, ("name",)),
    )
    for path, columns in files:
        if not os.path.exists(path):
            continue
        try:
            with open(path, encoding="utf-8-sig", newline="") as handle:
                for row in csv.DictReader(handle):
                    for column in columns:
                        for token in _LATIN_TOKEN_RE.findall(row.get(column) or ""):
                            terms.add(token.strip(".-").lower())
        except OSError:
            continue
    return terms


def _is_jargon(token):
    text = token.strip(".-")
    if len(text) < 2 or text.lower() in READABILITY_COMMON_TERMS:
        return False
    if _LEDGER_ID_RE.match(text):
        return False
    return (
        any(ch.isdigit() for ch in text)
        or text.isupper()
        or text[0].isupper()
        or any(ch.isupper() for ch in text[1:])
    )


def _reader_visible_link_text(text):
    """Keep rendered link labels, but drop destinations a reader never sees.

    Percent-encoded URLs previously produced phantom terms such as ``EC`` and
    repeated endpoint names.  Bare URLs are citation plumbing too, not prose a
    glossary should explain.
    """
    value = _MARKDOWN_LINK_RE.sub(r"\1", text)
    return _BARE_URL_RE.sub(" ", value)


def _beginner_body(text):
    """Return only the first-screen reader guide, excluding later audit prose."""
    return dict(_heading_sections(text, 2)).get(BEGINNER_HEADING, "")


def _beginner_visible_blocks(body):
    """Approximate rendered paragraphs/bullets for a sentence-length guard."""
    visible = _ANY_BLOCK_RE.sub("", body or "")
    blocks, paragraph = [], []

    def flush():
        if paragraph:
            value = _visible_markdown_text(" ".join(paragraph))
            if value:
                blocks.append(value)
            paragraph.clear()

    for raw in visible.splitlines():
        line = raw.strip()
        if not line:
            flush()
            continue
        if re.match(r"^#{1,6}\s+", line):
            flush()
            continue
        if re.match(r"^(?:[-*+]\s+|\d+[.)]\s+)", line):
            flush()
            value = _visible_markdown_text(line)
            if value:
                blocks.append(value)
            continue
        paragraph.append(line)
    flush()
    return blocks


def analyse_readability(text, meta, errors, warnings, entity_terms=None):
    """雙讀者 gate 的可判定部分：讀者看得到的術語必須解釋，帳本不得吃掉正文。

    這一關原本只驗結構（新手導讀在不在、幾個 bullet），可以完全機械式通過而
    文章仍不可讀。2026-08-08 的 AI 機櫃信任根一文即是：SPDM 出現 31 次、
    Caliptra 28 次，兩個主角都沒進小字典，讀者從第一句就無法解析。
    衡量基準必須是「讀者看得到的文字」——正文加上研究中心會渲染成表格的帳本
    欄位；只量 markdown 正文會把帳本裡的術語全部漏掉。
    """
    entity_terms = _entity_terms() if entity_terms is None else entity_terms
    # 若某個名字已被登錄為引用來源的 publisher，它是一個實體，不是讀者要查字典的
    # 概念。從文章自己的 source block 收割，比另外維護一份公司清單更不會過期。
    entity_terms = set(entity_terms)
    for body in _ANY_BLOCK_RE.findall(text):
        for line in body.splitlines():
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            if key.strip() in {"publisher", "independence_group"}:
                for token in _LATIN_TOKEN_RE.findall(value):
                    entity_terms.add(token.strip(".-").lower())
    prose = _reader_visible_link_text(_ANY_BLOCK_RE.sub(" ", text))
    shown = [prose]
    for body in _ANY_BLOCK_RE.findall(text):
        for line in body.splitlines():
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            if key.strip() in READER_FACING_FIELDS:
                shown.append(value)
    shown_text = _reader_visible_link_text(" ".join(shown))

    start, end = prose.find("名詞小字典"), prose.find("三句話抓重點")
    glossary = prose[start:end].lower() if 0 <= start < end else ""

    counts = {}
    for match in _LATIN_TOKEN_RE.finditer(shown_text):
        token = match.group(0).strip(".-")
        if _is_jargon(token) and token.lower() not in entity_terms:
            counts[token.lower()] = counts.get(token.lower(), 0) + 1

    hard = sorted(
        ((term, n) for term, n in counts.items()
         if n >= READABILITY_HARD_USES and term not in glossary),
        key=lambda item: (-item[1], item[0]),
    )
    soft = sorted(
        ((term, n) for term, n in counts.items()
         if READABILITY_SOFT_USES <= n < READABILITY_HARD_USES and term not in glossary),
        key=lambda item: (-item[1], item[0]),
    )

    prose_chars = len(re.sub(r"\s+", "", prose))
    shown_chars = len(re.sub(r"\s+", "", shown_text))
    ratio = prose_chars / shown_chars if shown_chars else 1.0

    captured = meta.get("captured_at") or ""
    enforced = _valid_date(captured) and captured >= READABILITY_CUTOVER
    sink = errors if enforced else warnings

    if hard:
        shown_terms = "、".join(f"{term}×{n}" for term, n in hard[:6])
        sink.append(
            f"讀者看得到的文字裡有 {len(hard)} 個術語出現 {READABILITY_HARD_USES} 次以上"
            f"卻沒進名詞小字典：{shown_terms}")
    if soft:
        warnings.append(
            f"另有 {len(soft)} 個術語出現 {READABILITY_SOFT_USES}~"
            f"{READABILITY_HARD_USES - 1} 次未解釋："
            + "、".join(f"{term}×{n}" for term, n in soft[:6]))
    if ratio < READABILITY_MIN_PROSE_RATIO:
        sink.append(
            f"正文解釋只占讀者可見文字的 {ratio:.0%}，低於 "
            f"{READABILITY_MIN_PROSE_RATIO:.0%}；帳本渲染後會蓋過說明")

    # The first screen has a stricter contract than the audit appendix.  Internal
    # state codes may remain in machine-readable blocks, but the beginner guide
    # must be understandable without knowing the repository's schema vocabulary.
    beginner = _beginner_body(text)
    beginner_text = _reader_visible_link_text(_ANY_BLOCK_RE.sub(" ", beginner))
    beginner_h3 = dict(_heading_sections(beginner, 3))
    beginner_glossary = _reader_visible_link_text(
        _ANY_BLOCK_RE.sub(" ", beginner_h3.get("名詞小字典", ""))).lower()
    internal_lead_terms = [
        label for label, pattern in READABILITY_INTERNAL_LEAD_PATTERNS
        if pattern.search(beginner_text)
    ]
    undefined_lead_terms = sorted({
        token
        for match in _LATIN_TOKEN_RE.finditer(beginner_text)
        if (token := match.group(0).strip(".-"))
        and _is_jargon(token)
        and token.lower() not in entity_terms
        and token.lower() not in beginner_glossary
    }, key=str.lower)
    long_lead_blocks = [
        block for block in _beginner_visible_blocks(beginner)
        if len(re.sub(r"\s+", "", block)) > READABILITY_MAX_LEAD_BLOCK_CHARS
    ]
    plain_enforced = (
        _valid_date(captured) and captured >= READABILITY_PLAIN_LANGUAGE_CUTOVER)
    plain_sink = errors if plain_enforced else warnings
    if internal_lead_terms:
        plain_sink.append(
            "新手導讀出現內部維運用詞，請改成一般讀者能直接理解的中文："
            + "、".join(internal_lead_terms))
    if undefined_lead_terms:
        plain_sink.append(
            "新手導讀有未在小字典解釋的英文術語："
            + "、".join(undefined_lead_terms[:8]))
    if long_lead_blocks:
        plain_sink.append(
            f"新手導讀有 {len(long_lead_blocks)} 個段落或項目超過 "
            f"{READABILITY_MAX_LEAD_BLOCK_CHARS} 個可見字，請拆成一段一個意思")
    return {
        "undefinedHard": hard, "undefinedSoft": soft,
        "proseRatio": round(ratio, 3), "enforced": enforced,
        "internalLeadTerms": internal_lead_terms,
        "undefinedLeadTerms": undefined_lead_terms,
        "longLeadBlocks": long_lead_blocks,
        "plainLanguageEnforced": plain_enforced,
    }


def audit_topic_history(previous_text, current_text):
    """比較前版與現版 block；舊 ID 不可刪除或重寫，只能做合法 lifecycle transition。"""
    errors = []
    old_meta_match = TOPIC_META_RE.findall(previous_text)
    new_meta_match = TOPIC_META_RE.findall(current_text)
    old_meta = _parse_fields(old_meta_match[0]) if len(old_meta_match) == 1 else {}
    new_meta = _parse_fields(new_meta_match[0]) if len(new_meta_match) == 1 else {}
    both_v3 = (
        old_meta.get("schema_version") == "3"
        and new_meta.get("schema_version") == "3"
    )

    def records(pattern, id_key, text):
        return {
            item.get(id_key): item
            for item in (_parse_fields(body) for body in pattern.findall(text))
            if item.get(id_key)
        }

    specs = (
        ("source", SOURCE_RE, "source_id", {"status"}, {
            "active": {"active", "superseded", "rejected"},
            "superseded": {"superseded"}, "rejected": {"rejected"},
        }),
        ("claim", CLAIM_RE, "claim_id", {
            "status", "resolution", "corrected_by_claim_id",
        }, {
            "active": {"active", "superseded", "refuted"},
            "superseded": {"superseded"}, "refuted": {"refuted"},
        }),
        ("comparison", COMPARISON_RE, "observation_id", set(), None),
        ("monitor", MONITOR_RE, "monitor_id", {
            "status", "retired_at", "retirement_reason",
        }, {
            "active": {"active", "retired"}, "retired": {"retired"},
        }),
    )
    current_sources = records(SOURCE_RE, "source_id", current_text)

    def corroboration_backfill_errors(record_id, key, old_value, new_value, as_of):
        """Evidence lists grow only; appended sources must predate the claim as_of.

        A frozen list gave no append-only way to add a later-located independent
        source chain, so the only route was a supersede that misreports a
        correction. Appending is allowed, but restricted to backfill: an appended
        source published after the claim's as_of is new evidence and still needs a
        new claim generation, which is what forces the wording to be re-derived.
        """
        old_ids = [item.strip() for item in old_value.split(",") if item.strip()]
        new_ids = [item.strip() for item in new_value.split(",") if item.strip()]
        if new_ids[:len(old_ids)] != old_ids:
            return [f"歷史 claim {record_id} {key} 只能在既有順序後追加:{key}"]
        found = []
        for source_id in new_ids[len(old_ids):]:
            source = current_sources.get(source_id)
            if source is None:
                found.append(f"歷史 claim {record_id} {key} 追加了不存在的 source:{source_id}")
                continue
            effective = source.get("published_at") or source.get("captured_at")
            if not _valid_date(effective) or not _valid_date(as_of):
                found.append(
                    f"歷史 claim {record_id} {key} 追加 {source_id} 缺少可比對日期")
            elif effective > as_of:
                found.append(
                    f"歷史 claim {record_id} {key} 追加的 {source_id} 發布日 {effective} "
                    f"晚於 claim as_of {as_of}；新證據必須另立新 claim，不可回填舊 claim")
        return found

    record_sets = {}
    for kind, pattern, id_key, mutable, transitions in specs:
        before = records(pattern, id_key, previous_text)
        after = records(pattern, id_key, current_text)
        record_sets[kind] = (before, after)
        for record_id, old in before.items():
            if record_id not in after:
                errors.append(f"歷史 {kind} ID 不可刪除:{record_id}")
                continue
            new = after[record_id]
            for key in set(old).union(new):
                if key in mutable:
                    continue
                if new.get(key, "") == old.get(key, ""):
                    continue
                if kind == "claim" and key in {"supporting_source_ids", "contrary_source_ids"}:
                    errors.extend(corroboration_backfill_errors(
                        record_id, key, old.get(key, ""), new.get(key, ""),
                        new.get("as_of", "")))
                    continue
                errors.append(f"歷史 {kind} {record_id} immutable 欄位被改寫:{key}")
            old_status = old.get("status") or "active"
            new_status = new.get("status") or "active"
            if transitions is not None:
                if new_status not in transitions.get(old_status, {old_status}):
                    errors.append(
                        f"歷史 {kind} {record_id} lifecycle 不允許 "
                        f"{old_status}→{new_status}")
            if kind == "claim":
                status_changed = old_status != new_status
                if not status_changed and new.get("resolution", "") != old.get("resolution", ""):
                    errors.append(f"歷史 claim {record_id} 未轉歷史狀態卻改寫 resolution")
                if (not status_changed
                        and new.get("corrected_by_claim_id", "")
                        != old.get("corrected_by_claim_id", "")):
                    errors.append(
                        f"歷史 claim {record_id} 未轉歷史狀態卻改寫 "
                        "corrected_by_claim_id")
            if kind == "monitor" and old_status == new_status:
                for key in ("retired_at", "retirement_reason"):
                    if new.get(key, "") != old.get(key, ""):
                        errors.append(f"歷史 monitor {record_id} 未退役卻改寫 {key}")

    old_transitions = [_parse_fields(body) for body in TRANSITION_RE.findall(previous_text)]
    new_transitions = [_parse_fields(body) for body in TRANSITION_RE.findall(current_text)]
    transition_prefix_ok = (
        not both_v3 or new_transitions[:len(old_transitions)] == old_transitions)
    if both_v3 and not transition_prefix_ok:
        errors.append("既有 transition 不可刪除、重排或改寫；只能在尾端追加")
    appended_transitions = (
        new_transitions[len(old_transitions):]
        if both_v3 and transition_prefix_ok else [])

    if both_v3:
        current_source_ids = set(record_sets["source"][1])
        revision_transition_sources = set()
        for transition in appended_transitions:
            source_ids = _transition_source_ids(transition.get("evidence"))
            if source_ids and all(source_id in current_source_ids for source_id in source_ids):
                revision_transition_sources.update(source_ids)
        has_source_bound_revision = bool(revision_transition_sources)

        # editorial revision：只改敘述，且必須證明帳本與時鐘一個字都沒動。
        declares_editorial = any(
            EDITORIAL_EVIDENCE_RE.match((transition.get("evidence") or "").strip())
            for transition in appended_transitions)
        ledger_unchanged = all(
            record_sets[kind][0] == record_sets[kind][1]
            for kind in ("source", "claim", "comparison", "monitor"))
        meta_unchanged = all(
            old_meta.get(key, "") == new_meta.get(key, "")
            for key in EDITORIAL_LOCKED_META)
        has_editorial_revision = declares_editorial and ledger_unchanged and meta_unchanged
        if declares_editorial and not (ledger_unchanged and meta_unchanged):
            errors.append(
                "editorial revision 只能改敘述；本次同時改到 source／claim／monitor "
                "或 meta 時鐘，必須改用綁定 sources 的 revision transition")

        old_visible = _visible_history_lines(previous_text)
        new_visible = _visible_history_lines(current_text)
        if (not _is_subsequence(old_visible, new_visible)
                and not has_source_bound_revision
                and not has_editorial_revision):
            errors.append(
                "歷史可見正文不可靜默改寫；必須保留舊敘述或追加綁定 sources 的 "
                "revision transition")

        old_impacts = [_parse_fields(body) for body in IMPACT_RE.findall(previous_text)]
        new_impacts = [_parse_fields(body) for body in IMPACT_RE.findall(current_text)]
        if (not _is_subsequence(old_impacts, new_impacts)
                and not has_source_bound_revision):
            errors.append(
                "歷史 impact 不可靜默改寫；必須保留舊 block 或追加綁定 sources 的 "
                "revision transition")

        immutable_meta = (
            "topic_id", "schema_version", "captured_at", "source_published_at",
            "source_type", "publisher", "publisher_domain", "canonical_url",
            "source_chain_id", "schema_migrated_at",
        )
        for key in immutable_meta:
            if old_meta.get(key, "") != new_meta.get(key, ""):
                errors.append(f"歷史 research_topic meta immutable 欄位被改寫:{key}")

        revision_meta = (
            "priority", "stock_ids", "group_ids", "trigger_type", "evidence_role",
            "route", "thesis_claim_id", "base_confidence", "confidence_basis",
            "cross_company_numbers", "last_reviewed_at", "review_due",
        )
        changed_meta = [
            key for key in revision_meta
            if old_meta.get(key, "") != new_meta.get(key, "")
        ]
        if changed_meta and not has_source_bound_revision:
            errors.append(
                "research_topic meta 變更必須追加綁定 sources 的 revision transition:"
                + ",".join(changed_meta))

        old_sources, new_sources = record_sets["source"]
        old_claims, new_claims = record_sets["claim"]

        def thesis_evidence(meta, sources, claims):
            claim = claims.get(meta.get("thesis_claim_id")) or {}
            source_ids = {
                source_id
                for key in ("supporting_source_ids", "contrary_source_ids")
                for source_id in _csv_values(claim.get(key))
                if (sources.get(source_id) or {}).get("status", "active") == "active"
            }
            accepted = [
                sources[source_id].get("accepted_at") for source_id in source_ids
                if _valid_date((sources.get(source_id) or {}).get("accepted_at"))
            ]
            return source_ids, max(accepted) if accepted else None

        old_thesis_sources, old_last_evidence = thesis_evidence(
            old_meta, old_sources, old_claims)
        new_thesis_sources, new_last_evidence = thesis_evidence(
            new_meta, new_sources, new_claims)
        fresh_thesis_sources = new_thesis_sources - set(old_sources)
        has_new_thesis_evidence = bool(fresh_thesis_sources)
        transition_sources = set()
        for transition in appended_transitions:
            evidence_ids = _transition_source_ids(transition.get("evidence"))
            if evidence_ids:
                transition_sources.update(evidence_ids)

        if (_valid_date(old_meta.get("last_reviewed_at"))
                and _valid_date(new_meta.get("last_reviewed_at"))
                and new_meta["last_reviewed_at"] < old_meta["last_reviewed_at"]):
            errors.append("last_reviewed_at 不可往回改寫")

        confidence_rank = {"low": 0, "medium": 1, "high": 2}
        freshness_changes = []
        if (_valid_date(old_meta.get("last_reviewed_at"))
                and _valid_date(new_meta.get("last_reviewed_at"))
                and new_meta["last_reviewed_at"] > old_meta["last_reviewed_at"]):
            freshness_changes.append("last_reviewed_at")
        if (_valid_date(old_meta.get("review_due"))
                and _valid_date(new_meta.get("review_due"))
                and new_meta["review_due"] > old_meta["review_due"]):
            freshness_changes.append("review_due")
        thesis_changed = old_meta.get("thesis_claim_id") != new_meta.get("thesis_claim_id")
        if thesis_changed and new_meta.get("thesis_claim_id") in old_claims:
            errors.append("thesis_claim_id 變更必須指向本次追加的新 claim")
        if (confidence_rank.get(new_meta.get("base_confidence"), -1)
                > confidence_rank.get(old_meta.get("base_confidence"), -1)):
            freshness_changes.append("base_confidence")
        if (old_meta.get("status") in {"dismissed", "resolved"}
                and new_meta.get("status") not in {"dismissed", "resolved"}):
            freshness_changes.append("status_reopened")
        evidence_clock_advanced = (
            has_new_thesis_evidence
            and _valid_date(old_last_evidence)
            and _valid_date(new_last_evidence)
            and new_last_evidence > old_last_evidence
        )
        fresh_transition_sources = (
            fresh_thesis_sources.intersection(transition_sources))
        if thesis_changed and not has_new_thesis_evidence:
            errors.append("thesis_claim_id 變更必須引用本次追加的新 evidence")
        elif thesis_changed and not fresh_transition_sources:
            errors.append("thesis_claim_id 修正 transition 必須引用新增主命題 evidence")
        if (thesis_changed and _valid_date(old_last_evidence)
                and _valid_date(new_last_evidence)
                and new_last_evidence < old_last_evidence):
            errors.append("新主命題 evidence clock 不可早於前版")
        transition_clock_advanced = any(
            _valid_date((new_sources.get(source_id) or {}).get("accepted_at"))
            and (not _valid_date(old_last_evidence)
                 or new_sources[source_id]["accepted_at"] > old_last_evidence)
            for source_id in fresh_transition_sources
        )
        if freshness_changes and not evidence_clock_advanced:
            errors.append(
                "沒有 accepted_at 較前版更新、且由新主命題引用的 evidence，不得刷新:"
                + ",".join(freshness_changes))
        elif freshness_changes and not transition_clock_advanced:
            errors.append("刷新可信度／期限的 revision transition 必須引用新增主命題 evidence")
        if (not thesis_changed and has_new_thesis_evidence and _valid_date(old_last_evidence)
                and _valid_date(new_last_evidence)
                and new_last_evidence < old_last_evidence):
            errors.append("新主命題 evidence clock 不可早於前版")
    return errors


def audit_git_topic_history(topics, baseline_ref):
    """以 Git 前版作不可變基線；新檔略過，既有 v1/v2 可單向遷移到 v3。"""
    check = subprocess.run(
        ["git", "rev-parse", "--verify", f"{baseline_ref}^{{commit}}"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check.returncode:
        return [f"baseline ref 無法解析:{baseline_ref}"]
    by_relpath = {topic["relpath"]: topic for topic in topics}
    global_errors = []
    listing = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", baseline_ref, "--",
         "notes/research_topics"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if listing.returncode:
        return [f"baseline topic 清單無法讀取:{baseline_ref}"]
    baseline_paths = {
        path.strip() for path in listing.stdout.splitlines()
        if path.strip().endswith(".md")
        and not os.path.basename(path.strip()).startswith("_")
    }
    for relpath in sorted(baseline_paths - set(by_relpath)):
        global_errors.append(f"歷史 topic 檔案不可刪除或重新命名:{relpath}")

    for relpath, topic in by_relpath.items():
        if relpath not in baseline_paths:
            continue
        prior = subprocess.run(
            ["git", "show", f"{baseline_ref}:{relpath}"], cwd=ROOT,
            capture_output=True, text=True, encoding="utf-8", errors="replace")
        if prior.returncode:
            global_errors.append(f"baseline topic 無法讀取:{relpath}")
            continue
        with open(topic["path"], encoding="utf-8") as handle:
            current_text = handle.read()
        for issue in audit_topic_history(prior.stdout, current_text):
            topic["quality_errors"].append(f"history:{issue}")
            topic["quality_invalid"] = True

    scan_relpath = os.path.relpath(SCAN_LOG, ROOT).replace("\\", "/")
    prior_scan = subprocess.run(
        ["git", "show", f"{baseline_ref}:{scan_relpath}"], cwd=ROOT,
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if prior_scan.returncode == 0:
        if not os.path.exists(SCAN_LOG):
            global_errors.append("歷史 scan_log.csv 不可刪除")
        else:
            with open(SCAN_LOG, encoding="utf-8") as handle:
                current_scan = handle.read()
            global_errors.extend(audit_scan_log_history(prior_scan.stdout, current_scan))
    return global_errors


def audit_scan_log_history(previous_text, current_text):
    """scan rows are append-only: an existing scan_id and every field stay immutable."""
    def rows_by_id(text):
        return {
            row.get("scan_id"): dict(row)
            for row in csv.DictReader(io.StringIO(text))
            if row.get("scan_id")
        }

    before = rows_by_id(previous_text)
    after = rows_by_id(current_text)
    errors = []
    for scan_id, old in before.items():
        if scan_id not in after:
            errors.append(f"歷史 scan_id 不可刪除:{scan_id}")
        elif after[scan_id] != old:
            errors.append(f"歷史 scan_id 不可改寫:{scan_id}")
    return errors


def load_scan_log(path=SCAN_LOG, topic_ids=None, as_of=None):
    """讀取有證據的掃描紀錄；partial 明確不等於完整涵蓋窗口。"""
    topic_ids = set(topic_ids or [])
    if as_of is None:
        as_of = taipei_today()
    elif isinstance(as_of, str) and _valid_date(as_of):
        as_of = dt.date.fromisoformat(as_of)
    rows, errors = [], []
    if not os.path.exists(path):
        return {"rows": [], "latest": None, "errors": ["缺少 scan_log.csv"]}
    required = {
        "scan_id", "window_start", "window_end", "scanned_at", "scope",
        "source_domains", "result_topic_ids", "next_scan_due", "coverage_note",
    }
    with open(path, encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = required - set(reader.fieldnames or [])
        if missing:
            errors.append(f"scan_log 缺欄:{','.join(sorted(missing))}")
        for lineno, row in enumerate(reader, 2):
            row_errors = []
            if not row.get("scan_id"):
                row_errors.append("scan_id 不可空白")
            for key in ("window_start", "window_end", "scanned_at", "next_scan_due"):
                if not _valid_date(row.get(key)):
                    row_errors.append(f"{key} 不是 YYYY-MM-DD")
            if (all(_valid_date(row.get(k)) for k in ("window_start", "window_end"))
                    and row["window_start"] > row["window_end"]):
                row_errors.append("window_start 晚於 window_end")
            if (all(_valid_date(row.get(k)) for k in ("window_end", "scanned_at"))
                    and row["window_end"] > row["scanned_at"]):
                row_errors.append("window_end 晚於 scanned_at")
            if (all(_valid_date(row.get(k)) for k in ("scanned_at", "next_scan_due"))
                    and row["scanned_at"] > row["next_scan_due"]):
                row_errors.append("scanned_at 晚於 next_scan_due")
            for key in ("window_start", "window_end", "scanned_at"):
                if (_valid_date(row.get(key))
                        and dt.date.fromisoformat(row[key]) > as_of):
                    row_errors.append(f"{key} 晚於研究判定日 {as_of.isoformat()}")
            if row.get("scope") not in {"full", "partial"}:
                row_errors.append("scope 必須是 full 或 partial")
            if not _semicolon_values(row.get("source_domains")):
                row_errors.append("source_domains 不可空白")
            if not row.get("coverage_note"):
                row_errors.append("coverage_note 不可空白")
            result_ids = _semicolon_values(row.get("result_topic_ids"))
            if result_ids == ["none"]:
                result_ids = []
            for topic_id in result_ids:
                if topic_id not in topic_ids:
                    row_errors.append(f"result_topic_ids 找不到:{topic_id}")
            row["result_topic_ids"] = result_ids
            row["quality_errors"] = row_errors
            errors.extend(f"scan_log:{lineno}:{issue}" for issue in row_errors)
            rows.append(row)
    seen = Counter(row.get("scan_id") for row in rows)
    for scan_id, count in seen.items():
        if scan_id and count > 1:
            errors.append(f"scan_id 重複:{scan_id}")
    valid = [
        row for row in rows
        if _valid_date(row.get("scanned_at")) and not row["quality_errors"]
    ]
    latest = None
    if valid:
        latest_date = max(row["scanned_at"] for row in valid)
        # scan_log 是 append-only；同一研究日可能有多輪掃描或更正，最後追加的
        # valid row 才是當日最新狀態，不能讓 scan_id 的字母排序改寫時間語意。
        latest = next(row for row in reversed(valid) if row["scanned_at"] == latest_date)
    return {"rows": rows, "latest": latest, "errors": errors}


def expected_revenue_period(as_of):
    """月營收法定申報日在次月 10 日；10 日以前只要求再前一月。"""
    target = as_of.replace(day=1)
    months_back = 1 if as_of.day >= 11 else 2
    for _ in range(months_back):
        target = (target - dt.timedelta(days=1)).replace(day=1)
    return target.year, target.month


def _quarter_token(value):
    if not value or not _valid_date(value):
        return None
    period = dt.date.fromisoformat(value)
    return f"{period.year}Q{(period.month - 1) // 3 + 1}"


def expected_quarter_date(as_of):
    """依申報截止日推導已應公布的最新季度，避免以 DB MAX(date) 自我證明完整。"""
    year = as_of.year
    if as_of >= dt.date(year, 11, 15):  # Q3 截止 11/14
        return dt.date(year, 9, 30)
    if as_of >= dt.date(year, 8, 15):   # Q2 截止 8/14
        return dt.date(year, 6, 30)
    if as_of >= dt.date(year, 5, 16):   # Q1 截止 5/15
        return dt.date(year, 3, 31)
    if as_of >= dt.date(year, 4, 1):    # 年報截止 3/31
        return dt.date(year - 1, 12, 31)
    return dt.date(year - 1, 9, 30)


def financial_snapshot(con, universe_rows, as_of):
    ids = [row["stock_id"] for row in universe_rows]
    placeholders = ",".join("?" for _ in ids)
    year, month = expected_revenue_period(as_of)
    present = {
        row["stock_id"]
        for row in con.execute(
            f"SELECT DISTINCT stock_id FROM month_revenue "
            f"WHERE revenue_year=? AND revenue_month=? AND revenue IS NOT NULL "
            f"AND stock_id IN ({placeholders})",
            (year, month, *ids),
        )
    }
    missing_revenue = [sid for sid in ids if sid not in present]
    expected_quarter = expected_quarter_date(as_of)
    expected_quarter_iso = expected_quarter.isoformat()
    expected_quarter_period = _quarter_token(expected_quarter_iso)
    quarter_tables = {}
    for table in ("financials", "balance_sheet", "cash_flow"):
        covered = {
            row["stock_id"]
            for row in con.execute(
                f"SELECT DISTINCT stock_id FROM {table} "
                f"WHERE date=? AND value IS NOT NULL AND stock_id IN ({placeholders})",
                (expected_quarter_iso, *ids),
            )
        }
        quarter_tables[table] = {
            "expected_date": expected_quarter_iso,
            "period": expected_quarter_period,
            "covered": len(covered),
            "missing": [sid for sid in ids if sid not in covered],
        }
    common_latest_period = (
        expected_quarter_period
        if all(item["covered"] == len(ids) for item in quarter_tables.values())
        else None
    )
    return {
        "expected_revenue_period": f"{year}-{month:02d}",
        "expected_quarter_period": expected_quarter_period,
        "revenue_covered": len(present),
        "revenue_missing": missing_revenue,
        "quarter_tables": quarter_tables,
        "common_latest_period": common_latest_period,
    }


def cohort_map(universe_rows):
    """把每個族群輪流分到 A–D，121 檔目前為 31/30/30/30。"""
    grouped = defaultdict(list)
    for row in universe_rows:
        grouped[row["group"]].append(row)
    cohorts = {label: [] for label in "ABCD"}
    offset = 0
    for group_id in sorted(grouped):
        members = sorted(grouped[group_id], key=lambda row: row["stock_id"])
        for index, row in enumerate(members):
            cohorts["ABCD"[(offset + index) % 4]].append(row)
        offset = (offset + len(members)) % 4
    return cohorts


def active_cohort(as_of):
    monday = as_of - dt.timedelta(days=as_of.weekday())
    weeks = (monday - ROTATION_ANCHOR).days // 7
    return "ABCD"[weeks % 4], monday


def _current_hypothesis_transition(hypothesis, as_of):
    visible = [
        item for item in hypothesis.get("transitions", [])
        if _valid_date(item.get("date")) and item["date"] <= as_of.isoformat()
    ]
    return visible[-1] if visible else None


def _append_item(items, priority, kind, due, detail):
    items.append({"priority": priority, "kind": kind, "due": due, "detail": detail})


def _topic_queue_priority(priority, due_date, as_of):
    """研究 priority 是營運優先級；期限到期至少升為 P1。"""
    if priority == "p0":
        return "P0"
    if priority == "p1" or due_date <= as_of:
        return "P1"
    return "P2"


def build_attention(as_of, db_path=DB, horizon=30, topics_dir=TOPICS_DIR,
                    scan_log_path=SCAN_LOG):
    universe_rows = _load_universe()
    names = {row["stock_id"]: row["name"] for row in universe_rows}
    notes = load_notes()
    reports = load_reports(notes=notes)
    groups = _load_groups()
    topics = load_topics(topics_dir, universe_rows, groups, reports, as_of=as_of)
    scan = load_scan_log(
        scan_log_path, [topic["topic_id"] for topic in topics], as_of=as_of)
    end = as_of + dt.timedelta(days=horizon)
    items = []

    draft_ids = []
    note_deadlines = Counter()
    for row in universe_rows:
        sid, info = row["stock_id"], notes.get(row["stock_id"])
        verification = note_review_status(info)
        if info is None or info.get("quality_invalid") or verification != "independently_verified":
            draft_ids.append(sid)
            _append_item(
                items, "P0", "formal_note_quality", as_of.isoformat(),
                f"{sid} {names[sid]}：{verification}"
                + ("，品質契約 invalid" if info and info.get("quality_invalid") else ""),
            )
        due = (info or {}).get("next_review")
        if _valid_date(due):
            due_date = dt.date.fromisoformat(due)
            note_deadlines[due] += 1
            if due_date <= as_of:
                _append_item(items, "P1", "formal_note_due", due, f"{sid} {names[sid]}")
            elif due_date <= end:
                _append_item(items, "P2", "formal_note_upcoming", due, f"{sid} {names[sid]}")

    hypothesis_deadlines = Counter()
    for sid, report in reports.items():
        for hypothesis in report.get("hypotheses", []):
            current = _current_hypothesis_transition(hypothesis, as_of)
            if not current or current.get("to") != "open":
                continue
            due = current.get("review_due")
            if not _valid_date(due):
                continue
            due_date = dt.date.fromisoformat(due)
            hypothesis_deadlines[due] += 1
            detail = f"{sid}:{hypothesis['id']} {hypothesis['title']}"
            if due_date <= as_of:
                _append_item(items, "P1", "hypothesis_due", due, detail)
            elif due_date <= end:
                _append_item(items, "P2", "hypothesis_upcoming", due, detail)

    event_deadlines = Counter()
    events = load_events()
    for event in events.get("all", []):
        due = event.get("next_review")
        if not _valid_date(due):
            continue
        event_deadlines[due] += 1
        due_date = dt.date.fromisoformat(due)
        detail = f"{event.get('subject')} {event.get('fiscal_quarter')} ({event.get('event_date')})"
        if due_date <= as_of:
            _append_item(items, "P1", "event_due", due, detail)
        elif due_date <= end:
            _append_item(items, "P2", "event_upcoming", due, detail)

    con = db_ro.connect(db_path)
    try:
        financial = financial_snapshot(con, universe_rows, as_of)
    finally:
        con.close()
    if financial["revenue_missing"]:
        detail = "、".join(
            f"{sid} {names.get(sid, '')}".strip() for sid in financial["revenue_missing"])
        _append_item(
            items, "P0", "month_revenue_gap", as_of.isoformat(),
            f"{financial['expected_revenue_period']} 缺 {len(financial['revenue_missing'])} 檔：{detail}",
        )
    for table, result in financial["quarter_tables"].items():
        if result["missing"]:
            _append_item(
                items, "P0", "quarterly_financial_gap", as_of.isoformat(),
                f"{table} {result['period']} 缺 {len(result['missing'])} 檔",
            )

    latest_period = financial["common_latest_period"]
    financial_note_stale = []
    if latest_period:
        for sid, info in notes.items():
            declared = re.sub(r"\s+", "", info.get("latest_financial_period") or "")
            if latest_period not in declared:
                financial_note_stale.append(sid)
                _append_item(
                    items, "P2", "formal_note_financial_period", as_of.isoformat(),
                    f"{sid} {names.get(sid, '')} 仍標 {info.get('latest_financial_period') or '-'}；"
                    f"DB 已有 {latest_period}",
                )

    for topic in topics:
        if topic["quality_invalid"]:
            _append_item(
                items, "P0", "topic_contract", as_of.isoformat(),
                f"{topic['relpath']}：{'; '.join(topic['quality_errors'])}",
            )
            continue
        if topic["status"] in {"dismissed", "resolved"}:
            continue
        due = topic.get("review_due")
        if _valid_date(due):
            due_date = dt.date.fromisoformat(due)
            priority = _topic_queue_priority(topic.get("priority"), due_date, as_of)
            if due_date <= end or priority in {"P0", "P1"}:
                kind = "topic_due" if due_date <= as_of else "topic_upcoming"
                _append_item(items, priority, kind, due, topic["topic_id"])
        for impact in topic["impacts"]:
            action = impact.get("note_action")
            due = impact.get("action_due")
            if action not in ACTIVE_NOTE_ACTIONS or not _valid_date(due):
                continue
            due_date = dt.date.fromisoformat(due)
            detail = (
                f"{topic['topic_id']} → {impact.get('group_id')}"
                + (f" ({','.join(impact['stock_ids'])})" if impact["stock_ids"] else "")
                + f"：{action}"
            )
            if due_date <= as_of:
                _append_item(items, "P1", "topic_action_due", due, detail)
            elif due_date <= end:
                _append_item(items, "P2", "topic_action_upcoming", due, detail)

        for sid in topic["stock_ids"]:
            report = reports.get(sid)
            narrative = (report or {}).get("narrative")
            if (narrative and _valid_date(narrative.get("updated"))
                    and _valid_date(topic.get("captured_at"))
                    and narrative["updated"] < topic["captured_at"]):
                _append_item(
                    items, "P2", "narrative_review",
                    topic.get("review_due") or as_of.isoformat(),
                    f"{sid} {names.get(sid, '')} 小作文 {narrative['updated']} 早於"
                    f"議題 {topic['topic_id']} 的捕捉日 {topic['captured_at']}；只需判斷是否相關，"
                    "不可自動改寫",
                )

    if scan["errors"]:
        for issue in scan["errors"]:
            _append_item(items, "P0", "scan_log_contract", as_of.isoformat(), issue)
    elif scan["latest"] is None:
        _append_item(items, "P1", "scan_missing", as_of.isoformat(), "尚無市場議題掃描紀錄")
    else:
        latest_scan = scan["latest"]
        if latest_scan["scope"] == "partial":
            _append_item(
                items, "P1", "scan_partial", latest_scan["next_scan_due"],
                f"最近一次掃描 {latest_scan['scan_id']} 為 partial："
                f"{latest_scan['coverage_note']}",
            )
        if (_valid_date(latest_scan.get("next_scan_due"))
                and latest_scan["next_scan_due"] <= as_of.isoformat()):
            _append_item(
                items, "P1", "scan_due", latest_scan["next_scan_due"],
                f"上次掃描 {latest_scan['scanned_at']}，下一次已到期",
            )

    items.sort(key=lambda item: (
        {"P0": 0, "P1": 1, "P2": 2}[item["priority"]],
        item["due"], item["kind"], item["detail"],
    ))
    cohorts = cohort_map(universe_rows)
    cohort, monday = active_cohort(as_of)
    return {
        "as_of": as_of.isoformat(),
        "horizon_days": horizon,
        "universe_count": len(universe_rows),
        "note_count": len(notes),
        "verified_note_count": sum(
            note_review_status(info) == "independently_verified" for info in notes.values()),
        "draft_ids": draft_ids,
        "report_count": len(reports),
        "hypothesis_count": sum(
            len(report.get("hypotheses", [])) for report in reports.values()),
        "topic_count": len(topics),
        "items": items,
        "financial": financial,
        "financial_note_stale": financial_note_stale,
        "deadline_distribution": {
            "formal_notes": dict(sorted(note_deadlines.items())),
            "hypotheses": dict(sorted(hypothesis_deadlines.items())),
            "events": dict(sorted(event_deadlines.items())),
        },
        "active_cohort": cohort,
        "active_week": monday.isoformat(),
        "cohorts": {
            label: [
                {"stock_id": row["stock_id"], "name": row["name"], "group": row["group"]}
                for row in members
            ]
            for label, members in cohorts.items()
        },
        "topic_errors": [
            f"{topic['relpath']}: {error}"
            for topic in topics for error in topic["quality_errors"]
        ],
        "topic_warnings": [
            f"{topic['relpath']}: {warning}"
            for topic in topics for warning in topic["quality_warnings"]
        ],
        "scan": scan,
    }


def _deadline_rows(snapshot):
    dates = set()
    for values in snapshot["deadline_distribution"].values():
        dates.update(values)
    return [
        (
            due,
            snapshot["deadline_distribution"]["formal_notes"].get(due, 0),
            snapshot["deadline_distribution"]["hypotheses"].get(due, 0),
            snapshot["deadline_distribution"]["events"].get(due, 0),
        )
        for due in sorted(dates)
    ]


def render_attention(snapshot):
    financial = snapshot["financial"]
    lines = [
        "# 研究維護佇列",
        "",
        f"- as_of：{snapshot['as_of']}（台灣研究日）",
        f"- universe：{snapshot['universe_count']} 檔；正式筆記 "
        f"{snapshot['note_count']} 篇（已獨立核驗 {snapshot['verified_note_count']}）",
        f"- 領先假說：{snapshot['report_count']} 份報告／"
        f"{snapshot['hypothesis_count']} 則；候選市場議題 {snapshot['topic_count']} 則",
        "- 數字是全 universe 普查，不是抽樣估計；因此不附 SE。",
        "",
        "## 財務資料覆蓋",
        "",
        "| 資料 | 最新要求／期間 | 覆蓋 | 缺口 |",
        "|---|---:|---:|---:|",
        f"| 月營收 | {financial['expected_revenue_period']} | "
        f"{financial['revenue_covered']}/{snapshot['universe_count']} | "
        f"{len(financial['revenue_missing'])} |",
    ]
    for table, result in financial["quarter_tables"].items():
        lines.append(
            f"| {table} | {result['period'] or '-'} | "
            f"{result['covered']}/{snapshot['universe_count']} | {len(result['missing'])} |")

    lines += ["", "## 需處理", ""]
    for priority in ("P0", "P1", "P2"):
        selected = [item for item in snapshot["items"] if item["priority"] == priority]
        lines.append(f"### {priority}（{len(selected)}）")
        lines.append("")
        if not selected:
            lines.append("- 無")
        else:
            for item in selected:
                lines.append(
                    f"- `{item['due']}` `{item['kind']}` — {item['detail']}")
        lines.append("")

    lines += [
        "## 硬期限分布",
        "",
        "| 日期 | 正式筆記 | H# | 事件錨點 |",
        "|---|---:|---:|---:|",
    ]
    for due, notes, hypotheses, events in _deadline_rows(snapshot):
        lines.append(f"| {due} | {notes} | {hypotheses} | {events} |")

    cohort = snapshot["active_cohort"]
    lines += [
        "",
        f"## 本週輪掃：{cohort} cohort（{snapshot['active_week']} 起）",
        "",
    ]
    grouped = defaultdict(list)
    for row in snapshot["cohorts"][cohort]:
        grouped[row["group"]].append(f"{row['stock_id']} {row['name']}")
    for group_id in sorted(grouped):
        lines.append(f"- **{group_id}：** " + "、".join(grouped[group_id]))
    lines += [
        "",
        "> 到期與輪掃是營運提示，不是新的投資訊號；月營收、價格或籌碼異常只能觸發查找，"
        "不得直接當作 H# 生命週期轉移或正式筆記事實。",
    ]
    return "\n".join(lines) + "\n"


def render_calendar(snapshot, weeks):
    as_of = dt.date.fromisoformat(snapshot["as_of"])
    monday = as_of - dt.timedelta(days=as_of.weekday())
    lines = [
        "# 研究輪掃時間表",
        "",
        f"- 產生基準：{snapshot['as_of']}",
        "- 四週一循環，每週約 30 檔；這是 delta scan，不是每月重寫完整筆記。",
        "- P0/P1 事件與正式期限永遠優先於 cohort。",
        "",
    ]
    for index in range(weeks):
        week = monday + dt.timedelta(days=7 * index)
        label = "ABCD"[((week - ROTATION_ANCHOR).days // 7) % 4]
        members = snapshot["cohorts"][label]
        lines += [
            f"## {week.isoformat()}｜{label} cohort（{len(members)} 檔）",
            "",
        ]
        grouped = defaultdict(list)
        for row in members:
            grouped[row["group"]].append(f"{row['stock_id']} {row['name']}")
        for group_id in sorted(grouped):
            lines.append(f"- **{group_id}：** " + "、".join(grouped[group_id]))
        lines.append("")
    lines += [
        "## 已登錄硬期限",
        "",
        "| 日期 | 正式筆記 | H# | 事件錨點 |",
        "|---|---:|---:|---:|",
    ]
    for due, notes, hypotheses, events in _deadline_rows(snapshot):
        lines.append(f"| {due} | {notes} | {hypotheses} | {events} |")
    return "\n".join(lines) + "\n"


def render_lint(topics, scan):
    lines = []
    error_count = warning_count = 0
    for topic in topics:
        for issue in topic["quality_errors"]:
            lines.append(f"ERROR\t{topic['relpath']}\t{issue}")
            error_count += 1
        for issue in topic["quality_warnings"]:
            lines.append(f"WARN\t{topic['relpath']}\t{issue}")
            warning_count += 1
    for issue in scan["errors"]:
        lines.append(f"ERROR\tnotes/research_topics/scan_log.csv\t{issue}")
        error_count += 1
    lines.append(
        f"研究議題:{len(topics)} 則；scan:{len(scan['rows'])} 筆；"
        f"{error_count} errors，{warning_count} warnings")
    return "\n".join(lines) + "\n", error_count


def _write_output(text, output):
    if output:
        parent = os.path.dirname(os.path.abspath(output))
        os.makedirs(parent, exist_ok=True)
        with open(output, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        print(f"output: {os.path.relpath(output, ROOT)}")
    else:
        print(text, end="")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--attention", action="store_true", help="輸出統一研究待辦（預設）")
    mode.add_argument("--calendar", action="store_true", help="輸出四週循環時間表")
    mode.add_argument("--lint", action="store_true", help="稽核 research_topics 與 scan log")
    parser.add_argument("--as-of", help="台灣研究日 YYYY-MM-DD；預設今天")
    parser.add_argument("--horizon", type=int, default=30, help="待辦前瞻日數")
    parser.add_argument("--weeks", type=int, default=8, help="--calendar 輸出週數")
    parser.add_argument("--db", default=DB, help="正式 SQLite 路徑（唯讀）")
    parser.add_argument("--output", help="UTF-8 輸出檔；省略則印 stdout")
    parser.add_argument("--json", action="store_true", help="--attention 輸出 JSON")
    parser.add_argument(
        "--baseline-ref", help="--lint 時比較 Git 前版，防止舊 source/claim/monitor 被重寫")
    args = parser.parse_args(argv)

    try:
        as_of = dt.date.fromisoformat(args.as_of) if args.as_of else taipei_today()
    except ValueError:
        parser.error("--as-of 必須是 YYYY-MM-DD")
    if args.horizon < 0:
        parser.error("--horizon 不可小於 0")
    if args.weeks < 1:
        parser.error("--weeks 必須至少 1")

    if args.lint:
        universe_rows = _load_universe()
        notes = load_notes()
        reports = load_reports(notes=notes)
        topics = load_topics(
            TOPICS_DIR, universe_rows, _load_groups(), reports, as_of=as_of)
        scan = load_scan_log(
            SCAN_LOG, [topic["topic_id"] for topic in topics], as_of=as_of)
        if args.baseline_ref:
            scan["errors"].extend(audit_git_topic_history(topics, args.baseline_ref))
        rendered, errors = render_lint(topics, scan)
        _write_output(rendered, args.output)
        return 1 if errors else 0

    snapshot = build_attention(as_of, args.db, args.horizon)
    if args.calendar:
        rendered = render_calendar(snapshot, args.weeks)
    elif args.json:
        rendered = json.dumps(snapshot, ensure_ascii=False, indent=2, default=str) + "\n"
    else:
        rendered = render_attention(snapshot)
    _write_output(rendered, args.output)
    return 1 if snapshot["topic_errors"] or snapshot["scan"]["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
