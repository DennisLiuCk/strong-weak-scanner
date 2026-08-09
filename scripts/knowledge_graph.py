#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Evidence-backed knowledge graph for the research center.

The graph is intentionally a curated projection of existing research.  Every
published edge must point to an active research-topic claim or to an exact
source in an independently verified qualitative note.  It never promotes
keyword co-occurrence into a company relationship.

Usage:
    python scripts/knowledge_graph.py --lint
    python scripts/knowledge_graph.py --json
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
from collections import Counter
from decimal import Decimal, InvalidOperation


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

CONCEPTS_CSV = os.path.join(ROOT, "config", "knowledge_concepts.csv")
ENTITIES_CSV = os.path.join(ROOT, "config", "external_entities.csv")
UNIVERSE_CSV = os.path.join(ROOT, "config", "universe.csv")
GROUPS_CSV = os.path.join(ROOT, "config", "groups.csv")
GRAPH_DIR = os.path.join(ROOT, "notes", "knowledge_graph")
TOPICS_DIR = os.path.join(ROOT, "notes", "research_topics")
NOTES_DIR = os.path.join(ROOT, "notes", "qualitative")
HYPOTHESES_DIR = os.path.join(ROOT, "notes", "leading_hypotheses")

GRAPH_META_RE = re.compile(r"<!--\s*knowledge_graph_meta\b(.*?)-->", re.S | re.I)
GRAPH_EDGE_RE = re.compile(r"<!--\s*knowledge_edge\b(.*?)-->", re.S | re.I)
FINANCIAL_MATERIALITY_RE = re.compile(
    r"<!--\s*financial_materiality\b(.*?)-->", re.S | re.I)
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
CLAIM_REF_RE = re.compile(r"(MI-[A-Z0-9-]+)#(C[1-9]\d*)")
NOTE_REF_RE = re.compile(r"(\d{4})#(S[1-9]\d*)")

NODE_TYPES = {
    "company", "organization", "concept", "product", "standard", "component",
    "process", "capability", "metric", "stage", "industry",
}
VIEWS = {"company", "industry"}
EVIDENCE_STATES = {"verified", "inference", "unverified"}
EDGE_STATUSES = {"active", "retired"}
MATERIALITY_LEVELS = {"unknown", "adjacent", "named_product", "financial"}
EXCLUSIVITY_LEVELS = {"unknown", "multi_source", "limited_source", "sole_source"}
FINANCIAL_SCOPES = {"company_total", "segment", "product", "unit_economics"}
FINANCIAL_ATTRIBUTION_STATUSES = {"direct", "bounded_proxy", "not_disclosed"}
FINANCIAL_VALUE_KINDS = {"reported", "derived"}
FINANCIAL_PERIOD_BASES = {
    "month", "quarter", "half_year", "nine_months", "fiscal_year",
    "trailing_twelve_months", "point_in_time",
}

RELATION_LABELS = {
    # Company / entity exposure view.
    "produces": "生產／出貨",
    "samples": "樣品階段",
    "provides_tooling": "提供製程工具",
    "qualified_at": "客戶資格節點",
    "cites_demand": "揭露需求方向",
    "develops_ip": "開發／驗證 IP",
    "has_capability": "揭露技術能力",
    "names_application": "列為應用機會",
    "platform_lists": "平台列名",
    "validated_for": "通過平台驗證",
    "integrates": "系統整合",
    "runs_poc": "場域 PoC",
    "owns_platform": "平台提供者",
    "planned_customer": "具名規劃節點",
    "tests": "測試／驗證",
    "plans_deployment": "規劃部署",
    "builds_systems": "協助打造系統",
    "develops_packaging": "封裝開發／資格",
    "supports_substrate": "載板／基板生態系",
    "plans_production": "規劃量產",
    "uses_standard": "採用／整合標準",
    "reports_financials": "揭露公司財務結果",
    # Industry dependency view.
    "generation_of": "世代／變體",
    "alternative_standard": "替代介面路徑",
    "uses_component": "使用元件",
    "changes_signal_path": "改變訊號路徑",
    "enables_substrate_path": "導向基板路徑",
    "integrated_with": "整合關係",
    "raises_need": "提高工程需求",
    "routes_to": "價值搜尋路由",
    "contains": "系統包含",
    "measured_by": "以此欄位觀察",
    "passes_through": "經過成熟度節點",
    "requires": "依賴／需要",
    "moves_to": "進入下一階段",
    "includes": "涵蓋",
    "reaches_stage": "到達階段",
    "uses_packaging": "使用封裝路徑",
    "uses_substrate": "需要載板／基板",
    "competes_with": "替代／競爭路徑",
}

STAGE_LABELS = {
    "concept": "概念／標準",
    "planned": "具名規劃／前瞻",
    "ecosystem": "生態系列名",
    "application_opportunity": "應用機會",
    "capability": "能力／研發",
    "sample": "樣品",
    "qualification": "資格認證",
    "validation": "客戶測試／驗證",
    "platform_listing": "平台列名",
    "production": "量產／生產",
    "shipment": "出貨",
    "deployment": "部署／上線",
    "integration": "系統整合",
    "poc": "PoC",
    "financial": "財務認列",
}

MATERIALITY_LABELS = {
    "unknown": "財務曝險未知",
    "adjacent": "相鄰／搜尋路由",
    "named_product": "具名產品或角色",
    "financial": "題材財務可直接歸因",
}

EXCLUSIVITY_LABELS = {
    "unknown": "供應集中度未知",
    "multi_source": "多路徑／非排他",
    "limited_source": "少數來源",
    "sole_source": "具證據的獨家",
}

FINANCIAL_SCOPE_LABELS = {
    "company_total": "公司總額",
    "segment": "事業部",
    "product": "產品類別",
    "unit_economics": "單位經濟",
}

FINANCIAL_ATTRIBUTION_LABELS = {
    "direct": "可直接歸因",
    "bounded_proxy": "有界代理",
    "not_disclosed": "題材分子未揭露",
}

FINANCIAL_VALUE_KIND_LABELS = {
    "reported": "公司原始揭露",
    "derived": "依揭露值重算",
}


class KnowledgeGraphError(ValueError):
    """Raised when graph source files violate the publishing contract."""


def _csv_values(value: str | None) -> list[str]:
    return [item.strip() for item in (value or "").split(",") if item.strip()]


def _pipe_values(value: str | None) -> list[str]:
    return [item.strip() for item in (value or "").split("|") if item.strip()]


def _parse_fields(body: str, label: str, errors: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        if ":" not in line:
            errors.append(f"{label} 欄位必須使用 key: value：{line}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key in result:
            errors.append(f"{label} 欄位重複：{key}")
        result[key] = value.strip()
    return result


def _read_csv(path: str) -> list[dict[str, str]]:
    with open(path, encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _node_from_concept(row: dict[str, str]) -> dict:
    return {
        "id": row["node_id"].strip(),
        "type": row["node_type"].strip(),
        "label": row["label"].strip(),
        "aliases": _pipe_values(row.get("aliases")),
        "parentId": row.get("parent_id", "").strip(),
        "description": row.get("description", "").strip(),
        "universe": False,
        "ticker": "",
        "exchange": "",
        "country": "",
        "groupId": "",
        "articleId": "",
        "url": "",
    }


def _node_from_entity(row: dict[str, str]) -> dict:
    return {
        "id": row["entity_id"].strip(),
        "type": row["entity_type"].strip(),
        "label": row["label"].strip(),
        "aliases": _pipe_values(row.get("aliases")),
        "parentId": "",
        "description": row.get("description", "").strip(),
        "universe": False,
        "ticker": row.get("ticker", "").strip(),
        "exchange": row.get("exchange", "").strip(),
        "country": row.get("country", "").strip(),
        "groupId": "",
        "articleId": "",
        "url": row.get("url", "").strip(),
    }


def load_nodes(errors: list[str] | None = None) -> dict[str, dict]:
    """Load canonical concepts and external entities, then inject repo universe/groups."""
    errors = errors if errors is not None else []
    nodes: dict[str, dict] = {}

    def add(node: dict, source: str) -> None:
        node_id = node.get("id", "")
        if not node_id:
            errors.append(f"{source} 缺少 node id")
            return
        if node_id in nodes:
            errors.append(f"知識節點重複：{node_id}")
            return
        if node.get("type") not in NODE_TYPES:
            errors.append(f"{source} node type 不在值域：{node.get('type') or '-'}")
        if not node.get("label"):
            errors.append(f"{source} 缺少 label")
        nodes[node_id] = node

    for idx, row in enumerate(_read_csv(CONCEPTS_CSV), 2):
        add(_node_from_concept(row), f"knowledge_concepts.csv:{idx}")
    for idx, row in enumerate(_read_csv(ENTITIES_CSV), 2):
        add(_node_from_entity(row), f"external_entities.csv:{idx}")

    groups = _read_csv(GROUPS_CSV)
    for row in groups:
        group_id = row.get("group", "").strip()
        add({
            "id": f"group:{group_id}", "type": "industry", "label": row.get("name", "").strip(),
            "aliases": _pipe_values(row.get("tag")), "parentId": "",
            "description": row.get("tag", "").strip(), "universe": False,
            "ticker": "", "exchange": "", "country": "TW", "groupId": group_id,
            "articleId": "", "url": "",
        }, f"groups.csv:{group_id}")

    for row in _read_csv(UNIVERSE_CSV):
        stock_id = row.get("stock_id", "").strip()
        add({
            "id": f"company:{stock_id}", "type": "company", "label": row.get("name", "").strip(),
            "aliases": [stock_id], "parentId": "", "description": row.get("biz", "").strip(),
            "universe": True, "ticker": stock_id, "exchange": "TW", "country": "TW",
            "groupId": row.get("group", "").strip(), "articleId": f"formal-{stock_id}",
            "url": "",
        }, f"universe.csv:{stock_id}")

    alias_owner: dict[str, str] = {}
    for node in nodes.values():
        for alias in [node["label"], *node.get("aliases", [])]:
            key = alias.casefold().strip()
            if not key:
                continue
            previous = alias_owner.get(key)
            if previous and previous != node["id"]:
                errors.append(f"知識節點 alias 衝突：{alias} 同時屬 {previous}、{node['id']}")
            alias_owner[key] = node["id"]
        parent = node.get("parentId")
        if parent and parent not in nodes:
            errors.append(f"知識節點 {node['id']} parent_id 不存在：{parent}")
    return nodes


def _topic_maps(topics: list[dict]) -> tuple[dict[str, dict], dict[str, dict]]:
    topic_by_id = {topic.get("topic_id"): topic for topic in topics if topic.get("topic_id")}
    claim_by_ref: dict[str, dict] = {}
    for topic_id, topic in topic_by_id.items():
        for claim in topic.get("claims") or []:
            claim_id = claim.get("claim_id")
            if claim_id:
                claim_by_ref[f"{topic_id}#{claim_id}"] = claim
    return topic_by_id, claim_by_ref


def _note_source(note: dict, source_id: str) -> dict | None:
    for source in note.get("sources") or []:
        if (source.get("id") or source.get("source_id")) == source_id:
            return source
    return None


def _source_payload(ref: str, source: dict, article_id: str) -> dict:
    return {
        "ref": ref,
        "id": source.get("source_id") or source.get("id") or "",
        "title": source.get("title") or source.get("document") or source.get("publisher") or ref,
        "url": source.get("url") or "",
        "articleId": article_id,
    }


def _evidence_rank(value: str) -> int:
    return {"unverified": 0, "inference": 1, "verified": 2}.get(value, -1)


def _claim_state(claims: list[dict]) -> str:
    labels = {claim.get("label") for claim in claims}
    if "unverified" in labels:
        return "unverified"
    if "inference" in labels:
        return "inference"
    return "verified"


def _valid_date(value: str) -> bool:
    if not DATE_RE.fullmatch(value or ""):
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _decimal_value(value: str, field: str, label: str, errors: list[str]) -> Decimal | None:
    try:
        number = Decimal(value)
    except (InvalidOperation, TypeError, ValueError):
        errors.append(f"{label} {field} 必須是十進位數字：{value or '-'}")
        return None
    if not number.is_finite():
        errors.append(f"{label} {field} 必須是有限數字：{value or '-'}")
        return None
    return number


def _edge_payload(
    fields: dict[str, str], label: str, nodes: dict[str, dict], topic_by_id: dict[str, dict],
    claim_by_ref: dict[str, dict], notes: dict[str, dict], graph_article_ids: set[str],
    errors: list[str],
) -> dict:
    required = {
        "edge_id", "view", "from_id", "to_id", "relation", "evidence_state",
        "commercial_stage", "materiality", "exclusivity", "as_of", "review_due",
        "status", "boundary", "next_trigger",
    }
    allowed = required | {"claim_refs", "note_refs", "exclusivity_scope"}
    unknown = set(fields) - allowed
    if unknown:
        errors.append(f"{label} 未知欄位：{','.join(sorted(unknown))}")
    for field in sorted(required):
        if not fields.get(field):
            errors.append(f"{label} 缺少 {field}")

    edge_id = fields.get("edge_id", "")
    view = fields.get("view", "")
    from_id, to_id = fields.get("from_id", ""), fields.get("to_id", "")
    relation = fields.get("relation", "")
    evidence_state = fields.get("evidence_state", "")
    stage = fields.get("commercial_stage", "")
    materiality = fields.get("materiality", "")
    exclusivity = fields.get("exclusivity", "")

    if view not in VIEWS:
        errors.append(f"{label} view 不在值域：{view or '-'}")
    if relation not in RELATION_LABELS:
        errors.append(f"{label} relation 不在值域：{relation or '-'}")
    if evidence_state not in EVIDENCE_STATES:
        errors.append(f"{label} evidence_state 不在值域：{evidence_state or '-'}")
    if stage not in STAGE_LABELS:
        errors.append(f"{label} commercial_stage 不在值域：{stage or '-'}")
    if materiality not in MATERIALITY_LEVELS:
        errors.append(f"{label} materiality 不在值域：{materiality or '-'}")
    if exclusivity not in EXCLUSIVITY_LEVELS:
        errors.append(f"{label} exclusivity 不在值域：{exclusivity or '-'}")
    if fields.get("status") not in EDGE_STATUSES:
        errors.append(f"{label} status 不在值域：{fields.get('status') or '-'}")
    for endpoint in (from_id, to_id):
        if endpoint not in nodes:
            errors.append(f"{label} endpoint 不存在：{endpoint or '-'}")
    if from_id == to_id and from_id:
        errors.append(f"{label} 不得形成 self-loop：{from_id}")
    if view == "company":
        endpoint_types = {nodes.get(value, {}).get("type") for value in (from_id, to_id)}
        if "company" not in endpoint_types:
            errors.append(f"{label} company view 至少一端必須是 company")
    if view == "industry":
        if any(nodes.get(value, {}).get("type") == "company" for value in (from_id, to_id)):
            errors.append(f"{label} industry view 不得直接放 company")

    as_of, review_due = fields.get("as_of", ""), fields.get("review_due", "")
    for field_name, value in (("as_of", as_of), ("review_due", review_due)):
        if not _valid_date(value):
            errors.append(f"{label} {field_name} 必須為 YYYY-MM-DD：{value or '-'}")
    if _valid_date(as_of) and _valid_date(review_due) and review_due < as_of:
        errors.append(f"{label} review_due 不得早於 as_of")
    if materiality == "financial" and (evidence_state != "verified" or stage != "financial"):
        errors.append(f"{label} financial materiality 必須同時是 verified／financial stage")
    if exclusivity != "unknown" and not fields.get("exclusivity_scope"):
        errors.append(f"{label} 非 unknown exclusivity 必須說明 exclusivity_scope")
    if exclusivity != "unknown" and evidence_state == "unverified":
        errors.append(f"{label} unverified edge 不得宣稱供應集中度")

    claim_refs = _csv_values(fields.get("claim_refs"))
    note_refs = _csv_values(fields.get("note_refs"))
    if not claim_refs and not note_refs:
        errors.append(f"{label} 至少需要 claim_refs 或 note_refs")

    claims: list[dict] = []
    claim_payloads: list[dict] = []
    source_payloads: list[dict] = []
    article_ids: list[str] = []
    for ref in claim_refs:
        match = CLAIM_REF_RE.fullmatch(ref)
        if not match:
            errors.append(f"{label} claim_ref 格式錯誤：{ref}")
            continue
        topic_id, _ = match.groups()
        topic = topic_by_id.get(topic_id)
        claim = claim_by_ref.get(ref)
        if not topic:
            errors.append(f"{label} claim_ref 找不到 topic：{ref}")
            continue
        if topic.get("quality_invalid"):
            errors.append(f"{label} claim_ref 指向品質不合格 topic：{ref}")
        if not claim:
            errors.append(f"{label} claim_ref 找不到 claim：{ref}")
            continue
        if claim.get("status") != "active":
            errors.append(f"{label} claim_ref 必須指向 active claim：{ref}")
        claims.append(claim)
        article_id = f"topic-{topic_id}"
        article_ids.append(article_id)
        claim_payloads.append({
            "ref": ref, "label": claim.get("label") or "", "text": claim.get("claim") or "",
            "articleId": article_id,
        })
        source_by_id = {
            source.get("source_id") or source.get("id"): source
            for source in topic.get("sources") or []
        }
        for source_id in [
            *(claim.get("supporting_source_ids") or []),
            *(claim.get("contrary_source_ids") or []),
        ]:
            source = source_by_id.get(source_id)
            if source:
                source_payloads.append(
                    _source_payload(f"{topic_id}#{source_id}", source, article_id))
        if topic_id not in graph_article_ids:
            errors.append(f"{label} claim topic 未列入 graph meta article_ids：{topic_id}")

    for ref in note_refs:
        match = NOTE_REF_RE.fullmatch(ref)
        if not match:
            errors.append(f"{label} note_ref 格式錯誤：{ref}")
            continue
        stock_id, source_id = match.groups()
        note = notes.get(stock_id)
        if not note:
            errors.append(f"{label} note_ref 找不到正式筆記：{ref}")
            continue
        if note.get("quality_invalid"):
            errors.append(f"{label} note_ref 指向品質不合格筆記：{ref}")
        verification = note.get("verification") or note.get("verification_status")
        if verification != "independently_verified":
            errors.append(f"{label} note_ref 必須來自 independently_verified 筆記：{ref}")
        source = _note_source(note, source_id)
        if not source:
            errors.append(f"{label} note_ref 找不到 source：{ref}")
            continue
        article_id = f"formal-{stock_id}"
        article_ids.append(article_id)
        source_payloads.append(_source_payload(f"QUAL-{ref}", source, article_id))

    if claims:
        strongest_allowed = _claim_state(claims)
        if _evidence_rank(evidence_state) > _evidence_rank(strongest_allowed):
            errors.append(
                f"{label} evidence_state 比引用 claim 更強：{evidence_state}>{strongest_allowed}")

    # Preserve deterministic order while de-duplicating evidence/source payloads.
    claim_payloads = list({item["ref"]: item for item in claim_payloads}.values())
    source_payloads = list({item["ref"]: item for item in source_payloads}.values())
    article_ids = list(dict.fromkeys(article_ids))
    return {
        "id": edge_id,
        "view": view,
        "from": from_id,
        "to": to_id,
        "relation": relation,
        "relationLabel": RELATION_LABELS.get(relation, relation),
        "evidenceState": evidence_state,
        "evidenceLabel": {
            "verified": "證實", "inference": "推論", "unverified": "待驗證",
        }.get(evidence_state, evidence_state),
        "commercialStage": stage,
        "commercialStageLabel": STAGE_LABELS.get(stage, stage),
        "materiality": materiality,
        "materialityLabel": MATERIALITY_LABELS.get(materiality, materiality),
        "exclusivity": exclusivity,
        "exclusivityLabel": EXCLUSIVITY_LABELS.get(exclusivity, exclusivity),
        "exclusivityScope": fields.get("exclusivity_scope", ""),
        "asOf": as_of,
        "reviewDue": review_due,
        "status": fields.get("status", ""),
        "boundary": fields.get("boundary", ""),
        "nextTrigger": fields.get("next_trigger", ""),
        "claimRefs": claim_payloads,
        "noteRefs": note_refs,
        "sources": source_payloads,
        "articleIds": article_ids,
        "financialAssessmentIds": [],
    }


def _financial_materiality_payload(
    fields: dict[str, str], label: str, edges: dict[str, dict], nodes: dict[str, dict],
    errors: list[str],
) -> dict:
    """Validate financial-materiality contract v2 without inventing topic attribution.

    ``company_total`` is a denominator anchor only and therefore must publish as
    ``not_disclosed``.  A ``direct`` result can only attach to a verified financial
    edge and must use a narrower segment/product/unit-economics scope.  This keeps a
    valid company tie-out from being silently promoted into topic revenue.
    """
    required = {
        "contract_version", "assessment_id", "edge_id", "financial_scope", "metric",
        "value_kind", "reported_value", "unit", "period_start", "period_end",
        "period_basis", "denominator_metric", "denominator_value", "denominator_unit",
        "attribution_status", "source_refs", "as_of", "review_due", "status",
        "metric_definition", "denominator_definition", "boundary", "next_trigger",
    }
    optional = {"share_percent", "calculation"}
    allowed = required | optional
    unknown = set(fields) - allowed
    if unknown:
        errors.append(f"{label} 未知欄位：{','.join(sorted(unknown))}")
    for field in sorted(required):
        if not fields.get(field):
            errors.append(f"{label} 缺少 {field}")

    assessment_id = fields.get("assessment_id", "")
    edge_id = fields.get("edge_id", "")
    scope = fields.get("financial_scope", "")
    value_kind = fields.get("value_kind", "")
    attribution = fields.get("attribution_status", "")
    status = fields.get("status", "")
    if fields.get("contract_version") != "2":
        errors.append(f"{label} contract_version 必須為 2")
    if scope not in FINANCIAL_SCOPES:
        errors.append(f"{label} financial_scope 不在值域：{scope or '-'}")
    if value_kind not in FINANCIAL_VALUE_KINDS:
        errors.append(f"{label} value_kind 不在值域：{value_kind or '-'}")
    if fields.get("period_basis") not in FINANCIAL_PERIOD_BASES:
        errors.append(
            f"{label} period_basis 不在值域：{fields.get('period_basis') or '-'}")
    if attribution not in FINANCIAL_ATTRIBUTION_STATUSES:
        errors.append(f"{label} attribution_status 不在值域：{attribution or '-'}")
    if status not in EDGE_STATUSES:
        errors.append(f"{label} status 不在值域：{status or '-'}")

    for field_name in ("period_start", "period_end", "as_of", "review_due"):
        value = fields.get(field_name, "")
        if not _valid_date(value):
            errors.append(f"{label} {field_name} 必須為 YYYY-MM-DD：{value or '-'}")
    period_start, period_end = fields.get("period_start", ""), fields.get("period_end", "")
    if _valid_date(period_start) and _valid_date(period_end) and period_end < period_start:
        errors.append(f"{label} period_end 不得早於 period_start")
    as_of, review_due = fields.get("as_of", ""), fields.get("review_due", "")
    if _valid_date(as_of) and _valid_date(review_due) and review_due < as_of:
        errors.append(f"{label} review_due 不得早於 as_of")

    reported = _decimal_value(
        fields.get("reported_value", ""), "reported_value", label, errors)
    denominator = _decimal_value(
        fields.get("denominator_value", ""), "denominator_value", label, errors)
    if denominator is not None and denominator <= 0:
        errors.append(f"{label} denominator_value 必須大於 0")
    share_text = fields.get("share_percent", "")
    share = None
    if share_text:
        share = _decimal_value(share_text, "share_percent", label, errors)
        if share is not None and not (Decimal("0") <= share <= Decimal("100")):
            errors.append(f"{label} share_percent 必須介於 0 與 100")
    if value_kind == "derived" and not fields.get("calculation"):
        errors.append(f"{label} derived value 必須填 calculation")

    if attribution == "not_disclosed":
        if scope != "company_total":
            errors.append(f"{label} not_disclosed 必須使用 company_total scope")
        if share_text:
            errors.append(f"{label} not_disclosed 不得填題材 share_percent")
        if (reported is not None and denominator is not None and reported != denominator):
            errors.append(f"{label} company_total anchor 的 reported_value 必須等於 denominator_value")
    elif attribution in {"direct", "bounded_proxy"}:
        if scope == "company_total":
            errors.append(f"{label} {attribution} 不得使用 company_total scope")
        if not share_text:
            errors.append(f"{label} {attribution} 必須填 share_percent")
        if fields.get("unit") != fields.get("denominator_unit"):
            errors.append(f"{label} 可比較占比的 unit 與 denominator_unit 必須相同")
        if reported is not None and denominator is not None and denominator > 0 and share is not None:
            calculated = reported / denominator * Decimal("100")
            if abs(calculated - share) > Decimal("0.5"):
                errors.append(
                    f"{label} share_percent 與 reported_value／denominator_value 不一致："
                    f"重算 {calculated.quantize(Decimal('0.01'))}%")

    edge = edges.get(edge_id)
    source_refs = _csv_values(fields.get("source_refs"))
    if not source_refs:
        errors.append(f"{label} 至少需要一個 source_ref")
    if not edge:
        errors.append(f"{label} edge_id 不存在：{edge_id or '-'}")
    else:
        if status == "active" and edge.get("status") != "active":
            errors.append(f"{label} active assessment 必須連到 active edge")
        if edge.get("view") != "company":
            errors.append(f"{label} 只能連到 company edge")
        endpoints = [nodes.get(edge.get(key), {}) for key in ("from", "to")]
        if not any(node.get("type") == "company" and node.get("universe") for node in endpoints):
            errors.append(f"{label} 必須連到 universe company")
        known_source_refs = {source.get("ref") for source in edge.get("sources", [])}
        missing_refs = set(source_refs) - known_source_refs
        if missing_refs:
            errors.append(
                f"{label} source_refs 不在 linked edge 證據中：{','.join(sorted(missing_refs))}")
        if attribution == "direct":
            if not (
                edge.get("evidenceState") == "verified"
                and edge.get("commercialStage") == "financial"
                and edge.get("materiality") == "financial"
            ):
                errors.append(
                    f"{label} direct 必須連到 verified／financial stage／financial materiality edge")
        elif attribution in {"bounded_proxy", "not_disclosed"}:
            if edge.get("materiality") == "financial":
                errors.append(f"{label} 非 direct assessment 不得連到 financial materiality edge")

    return {
        "contractVersion": 2,
        "id": assessment_id,
        "edgeId": edge_id,
        "financialScope": scope,
        "financialScopeLabel": FINANCIAL_SCOPE_LABELS.get(scope, scope),
        "metric": fields.get("metric", ""),
        "valueKind": value_kind,
        "valueKindLabel": FINANCIAL_VALUE_KIND_LABELS.get(value_kind, value_kind),
        "reportedValue": fields.get("reported_value", ""),
        "unit": fields.get("unit", ""),
        "periodStart": period_start,
        "periodEnd": period_end,
        "periodBasis": fields.get("period_basis", ""),
        "denominatorMetric": fields.get("denominator_metric", ""),
        "denominatorValue": fields.get("denominator_value", ""),
        "denominatorUnit": fields.get("denominator_unit", ""),
        "sharePercent": share_text,
        "attributionStatus": attribution,
        "attributionLabel": FINANCIAL_ATTRIBUTION_LABELS.get(attribution, attribution),
        "sourceRefs": source_refs,
        "calculation": fields.get("calculation", ""),
        "asOf": as_of,
        "reviewDue": review_due,
        "status": status,
        "metricDefinition": fields.get("metric_definition", ""),
        "denominatorDefinition": fields.get("denominator_definition", ""),
        "boundary": fields.get("boundary", ""),
        "nextTrigger": fields.get("next_trigger", ""),
    }


def build_knowledge_graph(
    topics: list[dict], notes: dict[str, dict] | None = None, graph_dir: str = GRAPH_DIR,
    strict: bool = True,
) -> dict:
    """Build the dashboard graph payload and validate every published edge."""
    notes = notes or {}
    errors: list[str] = []
    warnings: list[str] = []
    nodes = load_nodes(errors)
    topic_by_id, claim_by_ref = _topic_maps(topics or [])
    graphs: list[dict] = []
    graph_ids: set[str] = set()
    edge_ids: set[str] = set()
    financial_assessment_ids: set[str] = set()

    if not os.path.isdir(graph_dir):
        errors.append(f"knowledge graph 目錄不存在：{graph_dir}")
    else:
        for filename in sorted(os.listdir(graph_dir)):
            if not filename.endswith(".md") or filename.startswith("_"):
                continue
            path = os.path.join(graph_dir, filename)
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
            meta_matches = GRAPH_META_RE.findall(text)
            file_label = os.path.relpath(path, ROOT).replace(os.sep, "/")
            if len(meta_matches) != 1:
                errors.append(f"{file_label} 必須恰有一個 knowledge_graph_meta")
                continue
            meta = _parse_fields(meta_matches[0], f"{file_label} meta", errors)
            meta_allowed = {
                "schema_version", "graph_id", "root_node_id", "label", "summary",
                "article_ids", "status",
            }
            unknown = set(meta) - meta_allowed
            if unknown:
                errors.append(f"{file_label} meta 未知欄位：{','.join(sorted(unknown))}")
            for field in meta_allowed:
                if field not in {"article_ids"} and not meta.get(field):
                    errors.append(f"{file_label} meta 缺少 {field}")
            graph_id = meta.get("graph_id", "")
            if graph_id in graph_ids:
                errors.append(f"knowledge graph id 重複：{graph_id}")
            graph_ids.add(graph_id)
            if meta.get("schema_version") != "1":
                errors.append(f"{file_label} schema_version 必須為 1")
            if meta.get("status") not in {"active", "retired"}:
                errors.append(f"{file_label} graph status 不在值域")
            root_id = meta.get("root_node_id", "")
            if root_id not in nodes:
                errors.append(f"{file_label} root_node_id 不存在：{root_id or '-'}")
            article_ids = set(_csv_values(meta.get("article_ids")))
            for topic_id in article_ids:
                if topic_id not in topic_by_id:
                    errors.append(f"{file_label} article_id 找不到 topic：{topic_id}")

            edges: list[dict] = []
            for idx, body in enumerate(GRAPH_EDGE_RE.findall(text), 1):
                edge_label = f"{file_label} edge {idx}"
                fields = _parse_fields(body, edge_label, errors)
                edge = _edge_payload(
                    fields, edge_label, nodes, topic_by_id, claim_by_ref, notes,
                    article_ids, errors,
                )
                if edge["id"] in edge_ids:
                    errors.append(f"knowledge edge id 重複：{edge['id']}")
                edge_ids.add(edge["id"])
                if root_id and root_id not in {edge["from"], edge["to"]}:
                    errors.append(f"{edge_label} MVP 必須是 root 的一跳關係：{root_id}")
                edges.append(edge)

            edge_by_id = {edge["id"]: edge for edge in edges if edge.get("id")}
            assessments: list[dict] = []
            for idx, body in enumerate(FINANCIAL_MATERIALITY_RE.findall(text), 1):
                assessment_label = f"{file_label} financial materiality {idx}"
                fields = _parse_fields(body, assessment_label, errors)
                assessment = _financial_materiality_payload(
                    fields, assessment_label, edge_by_id, nodes, errors,
                )
                if assessment["id"] in financial_assessment_ids:
                    errors.append(f"financial materiality assessment id 重複：{assessment['id']}")
                financial_assessment_ids.add(assessment["id"])
                assessments.append(assessment)

            active_assessments = [
                item for item in assessments if item.get("status") == "active"
            ]
            assessments_by_edge: dict[str, list[dict]] = {}
            for assessment in active_assessments:
                assessments_by_edge.setdefault(assessment["edgeId"], []).append(assessment)
            for edge in edges:
                edge["financialAssessmentIds"] = [
                    item["id"] for item in assessments_by_edge.get(edge["id"], [])
                ]
                if edge.get("status") == "active" and edge.get("materiality") == "financial":
                    direct = [
                        item for item in assessments_by_edge.get(edge["id"], [])
                        if item.get("attributionStatus") == "direct"
                    ]
                    if not direct:
                        errors.append(
                            f"{file_label} edge {edge['id']} financial materiality 缺少 active v2 direct assessment")

            active_edges = [edge for edge in edges if edge.get("status") == "active"]
            for view in sorted(VIEWS):
                if not any(edge.get("view") == view for edge in active_edges):
                    errors.append(f"{file_label} 缺少 active {view} edge")
            node_ids = {root_id}
            for edge in active_edges:
                node_ids.update((edge["from"], edge["to"]))
            graph_nodes = [nodes[node_id] for node_id in node_ids if node_id in nodes]
            graph_nodes.sort(key=lambda node: (node["id"] != root_id, node["type"], node["label"]))
            counts = Counter(edge["evidenceState"] for edge in active_edges)
            graphs.append({
                "id": graph_id,
                "label": meta.get("label", ""),
                "summary": meta.get("summary", ""),
                "rootNodeId": root_id,
                "articleIds": [f"topic-{topic_id}" for topic_id in _csv_values(meta.get("article_ids"))],
                "status": meta.get("status", ""),
                "nodes": graph_nodes,
                "edges": active_edges,
                "financialAssessments": active_assessments,
                "counts": {key: counts.get(key, 0) for key in ("verified", "inference", "unverified")},
            })

    graphs.sort(key=lambda graph: graph["id"])
    payload = {
        "schemaVersion": 2,
        "graphs": graphs,
        "relationLabels": RELATION_LABELS,
        "stageLabels": STAGE_LABELS,
        "materialityLabels": MATERIALITY_LABELS,
        "exclusivityLabels": EXCLUSIVITY_LABELS,
        "financialScopeLabels": FINANCIAL_SCOPE_LABELS,
        "financialAttributionLabels": FINANCIAL_ATTRIBUTION_LABELS,
        "errors": errors,
        "warnings": warnings,
        "stats": {
            "graphs": len(graphs),
            "nodes": len({node["id"] for graph in graphs for node in graph["nodes"]}),
            "edges": sum(len(graph["edges"]) for graph in graphs),
            "financialAssessments": sum(
                len(graph["financialAssessments"]) for graph in graphs),
        },
    }
    if strict and errors:
        raise KnowledgeGraphError("\n".join(errors))
    return payload


def _load_default_context() -> tuple[list[dict], dict[str, dict]]:
    from leading_hypotheses import load_reports
    from qual_notes import load_notes
    from research_queue import load_topics, taipei_today

    notes = load_notes(NOTES_DIR)
    reports = load_reports(HYPOTHESES_DIR, notes=notes)
    topics = load_topics(TOPICS_DIR, reports=reports, as_of=taipei_today())
    return topics, notes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="研究中心證據型知識圖譜")
    parser.add_argument("--lint", action="store_true", help="只驗證 schema 與 evidence refs")
    parser.add_argument("--json", action="store_true", help="將完整 payload 印到 stdout")
    args = parser.parse_args(argv)

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    topics, notes = _load_default_context()
    payload = build_knowledge_graph(topics, notes, strict=False)
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        stats = payload["stats"]
        print(
            f"knowledge graph：{stats['graphs']} 個主題、{stats['nodes']} 個節點、"
            f"{stats['edges']} 條關係、{stats['financialAssessments']} 筆財務 v2 assessment"
        )
        for warning in payload["warnings"]:
            print(f"WARNING：{warning}")
        for error in payload["errors"]:
            print(f"ERROR：{error}")
    return 1 if payload["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
