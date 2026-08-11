#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_dashboard.py — 從 SQLite(daily_scores + daily_metrics)自動重生儀表板 HTML。
吃 scripts/dashboard_template.html(CSS/JS 外殼),只注入資料 → index.html,
並把同一份頁面凍結成 archive/<資料日>.html(as-seen 歷史快照,供日期選單回看)。
零第三方依賴。用法:  python scripts/build_dashboard.py
"""
import csv
import datetime as dt
import json, os, re, sqlite3, statistics, sys
from collections import Counter, defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# 個股層門檻單一事實來源(score.py CONFIG):權重 + 各元素 hint 引用的門檻,調旋鈕文字自動同步
from score import (WEIGHTS, VOLR_ACTIVE, VOLR_DRY, VOL_OVERHEAT, VOLR_OVERHEAT,
                   MARGIN_UTIL_HOT, MARGIN_UTIL_MID, MARGIN_DOWN_BIG, MARGIN_UP_BIG,
                   DZ_FOREIGN, DZ_TRUST, STEALTH_OFF_HIGH, _chip_signal)
# 族群/大盤門檻單一事實來源(fetch_daily 頂部旋鈕),族群卡與市場籤條 tooltip 顯示用
from fetch_daily import (REGIME_DD, GS_OFF_HIGH, GS_BREADTH_LOW,
                         MARKET_SOURCE_TWSE, MARKET_SOURCE_FINMIND,
                         MARKET_SOURCE_LEGACY)
import db_ro                     # 唯讀開啟的唯一入口(鐵律);這支只讀 db,只寫 html
import trading_status as tstatus
import signal_structure as sig   # 策略狀態卡的結構指標(與每日簡報、週報 §⑦⑧ 同一組函式)
import hypotheses as hyp         # 兩視角分歧的籌碼定義 = H1 檢定的同一個定義
# 個股質化筆記的時效與查核品質——單一事實來源在 qual_notes.py
from qual_notes import (_extract_sections, load_notes, note_status, note_review_status,
                        load_events, EVENT_KPI_KEYS,
                        TEMPLATE_VERSION as NOTE_TEMPLATE_VERSION)
from leading_hypotheses import (HYPOTHESIS_STATUS_INFO,
                                load_reports as load_hypothesis_reports)
from research_queue import (_topic_confidence as topic_confidence_at,
                            load_topics as load_research_topics,
                            taipei_today as research_today)
from knowledge_graph import build_knowledge_graph
from research_radar import load_research_radar
from research_method_audit import (effective_monitor_schedule, load_method_audit,
                                   load_monitor_reviews)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
TEMPLATE = os.path.join(ROOT, "scripts", "dashboard_template.html")
RESEARCH_TEMPLATE = os.path.join(ROOT, "scripts", "research_template.html")
OUT = os.path.join(ROOT, "index.html")   # 根目錄 index.html → GitHub Pages 乾淨網址
RESEARCH_OUT = os.path.join(ROOT, "research.html")
CHART_DAYS = 120   # 互動股價圖每檔保留交易日數(1f;vol=股數、含外資/投信,前端 slice 切 20/60/120)
# 歷史快照:每日 build 原樣存檔,回看的是「當天使用者看到的報告」而非以現行規則重算
# (daily_scores 等衍生表每日全量重建,事後從 db 重繪會是 restated history,不可稽核)。
ARCHIVE = os.path.join(ROOT, "archive")
NOTES_DIR = os.path.join(ROOT, "notes", "qualitative")
HYPOTHESES_DIR = os.path.join(ROOT, "notes", "leading_hypotheses")
TOPICS_DIR = os.path.join(ROOT, "notes", "research_topics")
GROUPS_CONFIG = os.path.join(ROOT, "config", "groups.csv")
RESEARCH_GROUP_GUIDE = os.path.join(ROOT, "config", "research_group_guide.csv")
RESEARCH_READER_TERMS = os.path.join(ROOT, "config", "research_reader_terms.csv")
RESEARCH_TOPIC_GUIDE = os.path.join(ROOT, "config", "research_topic_guide.csv")
READER_OPAQUE_GROUP_IDS = (
    "passive", "powersupply", "serverodm", "semiequip", "packtest", "ipdesign",
)
# GitHub 原文仍保留作為來源檔與版本歷史入口；站內研究中心另外提供適合長文閱讀的 render。
NOTE_REPO_BLOB = "https://github.com/DennisLiuCk/strong-weak-scanner/blob/main/"
NOTE_LABEL = {
    "ai_draft": "AI 草稿・未獨立查核",
    "partially_verified": "部分核驗",
    "independently_verified": "已獨立核對來源",
    "conflicted": "來源衝突・待釐清",
}
RECENT_ARTICLE_DAYS = 14
RECENT_ARTICLE_TYPES = (
    ("formal_note", "正式筆記"),
    ("narrative", "多空小作文"),
    ("topic", "市場議題"),
)


def load_research_group_guide(strict=True):
    """Load the reader-only group primer and require exact formal-group coverage."""
    errors = []
    try:
        with open(GROUPS_CONFIG, encoding="utf-8", newline="") as handle:
            formal_rows = list(csv.DictReader(handle))
    except OSError as exc:
        formal_rows = []
        errors.append(f"無法讀取正式族群設定：{exc}")
    formal_ids = [row.get("group", "").strip() for row in formal_rows]
    formal_ids = [group_id for group_id in formal_ids if group_id]

    guide = {}
    try:
        with open(RESEARCH_GROUP_GUIDE, encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            expected = ["group", "reader_role", "reader_boundary"]
            if reader.fieldnames != expected:
                errors.append(
                    "research_group_guide.csv 欄位必須是 " + ",".join(expected)
                )
            for line_no, row in enumerate(reader, 2):
                group_id = (row.get("group") or "").strip()
                role = (row.get("reader_role") or "").strip()
                boundary = (row.get("reader_boundary") or "").strip()
                if not group_id:
                    errors.append(f"research_group_guide.csv:{line_no} group 不可留空")
                    continue
                if group_id in guide:
                    errors.append(f"research_group_guide.csv:{line_no} group 重複：{group_id}")
                for key, value in (("reader_role", role), ("reader_boundary", boundary)):
                    if not value:
                        errors.append(
                            f"research_group_guide.csv:{line_no} {key} 不可留空"
                        )
                    elif not value.endswith("。"):
                        errors.append(
                            f"research_group_guide.csv:{line_no} {key} 必須是完整句"
                        )
                guide[group_id] = {
                    "readerRole": role,
                    "readerBoundary": boundary,
                }
    except OSError as exc:
        errors.append(f"無法讀取族群白話導覽：{exc}")

    missing = [group_id for group_id in formal_ids if group_id not in guide]
    extra = [group_id for group_id in guide if group_id not in set(formal_ids)]
    if missing:
        errors.append("族群白話導覽缺少正式族群：" + ",".join(missing))
    if extra:
        errors.append("族群白話導覽含未知族群：" + ",".join(extra))
    if strict and errors:
        raise ValueError("族群白話導覽契約失敗：\n- " + "\n- ".join(errors))
    return guide


def load_research_reader_terms(strict=True):
    """Load the governed, reader-only vocabulary shared across research articles."""
    errors = []
    terms = []
    seen_ids = set()
    seen_aliases = {}
    expected = ["term_id", "label", "aliases", "definition", "boundary"]
    try:
        with open(RESEARCH_READER_TERMS, encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != expected:
                errors.append(
                    "research_reader_terms.csv 欄位必須是 " + ",".join(expected)
                )
            for line_no, row in enumerate(reader, 2):
                term_id = (row.get("term_id") or "").strip()
                label = (row.get("label") or "").strip()
                aliases = [
                    alias.strip() for alias in (row.get("aliases") or "").split("|")
                    if alias.strip()
                ]
                definition = (row.get("definition") or "").strip()
                boundary = (row.get("boundary") or "").strip()
                if not re.fullmatch(r"[a-z0-9_]+", term_id):
                    errors.append(
                        f"research_reader_terms.csv:{line_no} term_id 格式錯誤：{term_id or '空白'}"
                    )
                elif term_id in seen_ids:
                    errors.append(
                        f"research_reader_terms.csv:{line_no} term_id 重複：{term_id}"
                    )
                seen_ids.add(term_id)
                if not label:
                    errors.append(f"research_reader_terms.csv:{line_no} label 不可留空")
                if not aliases:
                    errors.append(f"research_reader_terms.csv:{line_no} aliases 不可留空")
                for alias in aliases:
                    alias_key = alias.casefold()
                    if len(alias) < 2:
                        errors.append(
                            f"research_reader_terms.csv:{line_no} alias 至少 2 字元：{alias}"
                        )
                    if alias_key in seen_aliases:
                        errors.append(
                            f"research_reader_terms.csv:{line_no} alias 重複：{alias}"
                            f"（先前位於第 {seen_aliases[alias_key]} 行）"
                        )
                    else:
                        seen_aliases[alias_key] = line_no
                for key, value in (("definition", definition), ("boundary", boundary)):
                    if not value:
                        errors.append(
                            f"research_reader_terms.csv:{line_no} {key} 不可留空"
                        )
                    elif not value.endswith("。"):
                        errors.append(
                            f"research_reader_terms.csv:{line_no} {key} 必須是完整句"
                        )
                terms.append({
                    "id": term_id,
                    "label": label,
                    "aliases": aliases,
                    "definition": definition,
                    "boundary": boundary,
                })
    except OSError as exc:
        errors.append(f"無法讀取研究中心共通語：{exc}")
    if strict and errors:
        raise ValueError("研究中心共通語契約失敗：\n- " + "\n- ".join(errors))
    return terms


def load_research_topic_guide(strict=True):
    """Load manually reviewed, reader-only questions for market-topic entry points."""
    errors = []
    guide = {}
    expected = ["article_id", "reader_question"]
    try:
        with open(RESEARCH_TOPIC_GUIDE, encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != expected:
                errors.append(
                    "research_topic_guide.csv 欄位必須是 " + ",".join(expected)
                )
            for line_no, row in enumerate(reader, 2):
                article_id = (row.get("article_id") or "").strip()
                question = (row.get("reader_question") or "").strip()
                if not re.fullmatch(r"(?:topic|event)-[A-Za-z0-9-]+", article_id):
                    errors.append(
                        f"research_topic_guide.csv:{line_no} article_id 格式錯誤："
                        f"{article_id or '空白'}"
                    )
                elif article_id in guide:
                    errors.append(
                        f"research_topic_guide.csv:{line_no} article_id 重複：{article_id}"
                    )
                if not question:
                    errors.append(
                        f"research_topic_guide.csv:{line_no} reader_question 不可留空"
                    )
                else:
                    if not question.endswith("？"):
                        errors.append(
                            f"research_topic_guide.csv:{line_no} reader_question 必須是問句"
                        )
                    if not 18 <= len(question) <= 56:
                        errors.append(
                            f"research_topic_guide.csv:{line_no} reader_question 應為 18–56 字"
                        )
                    if re.search(r"[A-Za-z]", question) or "`" in question:
                        errors.append(
                            f"research_topic_guide.csv:{line_no} reader_question 必須先用中文概念"
                        )
                guide[article_id] = {"readerQuestion": question}
    except OSError as exc:
        errors.append(f"無法讀取市場議題白話導覽：{exc}")
    if strict and errors:
        raise ValueError("市場議題白話導覽契約失敗：\n- " + "\n- ".join(errors))
    return guide


def attach_research_topic_guide(research_library, guide, strict=True):
    """Attach exact, human-authored questions without altering topic research fields."""
    research_library = research_library or {"articles": []}
    topic_articles = [
        article for article in (research_library.get("articles") or [])
        if article.get("type") == "topic" and article.get("id")
    ]
    published_ids = [article["id"] for article in topic_articles]
    guide_ids = set(guide or {})
    errors = []
    missing = [article_id for article_id in published_ids if article_id not in guide_ids]
    extra = sorted(guide_ids - set(published_ids))
    if missing:
        errors.append("缺少已發布市場議題：" + ",".join(missing))
    if extra:
        errors.append("包含未發布市場議題：" + ",".join(extra))
    if strict and errors:
        raise ValueError("市場議題白話導覽覆蓋失敗：\n- " + "\n- ".join(errors))
    for article in topic_articles:
        entry = (guide or {}).get(article["id"])
        if not entry:
            continue
        article["readerQuestion"] = entry["readerQuestion"]
        article["searchText"] = (
            article.get("searchText", "") + " " + entry["readerQuestion"]
        ).strip().lower()
    return research_library


RESEARCH_LEARNING_ROUTES = [
    {
        "id": "power-cooling", "label": "供電與散熱",
        "question": "電力如何送進 AI 機櫃，產生的熱又如何被帶走？",
        "description": (
            "建議分三階段：先分清供電、保護與元件角色，再看機櫃緩衝、控制、"
            "電磁干擾驗證與信任查證，最後追液冷產品資格與迴路責任。"
        ),
        "graphIds": [
            "800v-power-tree", "800vdc-protection-layers", "ai-capacitor-role-map",
            "ai-power-buffering", "ai-rack-action-contract", "ai-rack-emc-certification",
            "ai-rack-trust-root", "liquid-cooling", "liquid-cooling-loop-boundaries",
        ],
        "phases": [
            {
                "id": "power-components",
                "label": "供電、保護與元件",
                "graphIds": [
                    "800v-power-tree", "800vdc-protection-layers",
                    "ai-capacitor-role-map",
                ],
            },
            {
                "id": "rack-operation",
                "label": "機櫃運作與驗證",
                "graphIds": [
                    "ai-power-buffering", "ai-rack-action-contract",
                    "ai-rack-emc-certification", "ai-rack-trust-root",
                ],
            },
            {
                "id": "cooling-deployment",
                "label": "液冷部署",
                "graphIds": [
                    "liquid-cooling", "liquid-cooling-loop-boundaries",
                ],
            },
        ],
    },
    {
        "id": "memory-packaging", "label": "記憶體與封裝",
        "question": "資料放在哪裡，記憶體與封裝又如何一起影響運算？",
        "description": (
            "建議分三階段：先建立記憶體層級與客製範圍，再看材料、基板與"
            "記憶體商業化，最後追鍵結與封裝路徑。"
        ),
        "graphIds": [
            "ai-memory-hierarchy", "custom-hbm-scope-ladder",
            "glass-substrate-commercialization", "hbf-commercialization", "hbm",
            "hybrid-bonding", "panel-level-packaging",
        ],
        "phases": [
            {
                "id": "memory-architecture",
                "label": "記憶體層級與客製範圍",
                "graphIds": [
                    "ai-memory-hierarchy", "custom-hbm-scope-ladder",
                ],
            },
            {
                "id": "memory-commercialization",
                "label": "材料、基板與記憶體商業化",
                "graphIds": [
                    "glass-substrate-commercialization", "hbf-commercialization", "hbm",
                ],
            },
            {
                "id": "bonding-packaging",
                "label": "鍵結與封裝路徑",
                "graphIds": ["hybrid-bonding", "panel-level-packaging"],
            },
        ],
    },
    {
        "id": "compute-connect", "label": "運算與互連",
        "question": "算力與資料如何在晶片、儲存與網路之間移動？",
        "description": (
            "建議分三階段：先看資料平面與平台部署，再補晶片供電、光網路與"
            "製程條件，最後用開放互連、PCIe 6 與 UCIe 檢查標準成熟度。"
        ),
        "graphIds": [
            "ai-storage-data-plane", "amd-helios", "backside-power", "cpo-networking",
            "high-na-euv-readiness", "open-ai-fabrics", "pcie6-compliance-ladder",
            "ucie-interoperability",
        ],
        "phases": [
            {
                "id": "data-platform",
                "label": "資料平面與平台部署",
                "graphIds": ["ai-storage-data-plane", "amd-helios"],
            },
            {
                "id": "chip-process",
                "label": "晶片供電、光網路與製程",
                "graphIds": [
                    "backside-power", "cpo-networking", "high-na-euv-readiness",
                ],
            },
            {
                "id": "interconnect-standards",
                "label": "互連與標準驗證",
                "graphIds": [
                    "open-ai-fabrics", "pcie6-compliance-ladder",
                    "ucie-interoperability",
                ],
            },
        ],
    },
    {
        "id": "company-finance", "label": "公司財務案例",
        "question": "市場題材何時能落到可辨識的收入、毛利或現金流？",
        "description": (
            "建議讀法：用國巨 Q2 案例，練習把公司總額與題材可歸因貢獻分開。"
        ),
        "graphIds": ["yageo-q2-financial-materiality"],
        "phases": [{
            "id": "financial-attribution",
            "label": "公司分母與題材歸因",
            "graphIds": ["yageo-q2-financial-materiality"],
        }],
    },
]

# 標題設定。TITLE_TAIL 是品牌尾綴、ALL_SCOPE 是「全部族群」時的範圍詞;篩選到單一族群時,
# 前端會把標題換成「族群名 · TITLE_TAIL」(見 dashboard_template.html 的 group filter JS)。
# 刻意不列舉族群、不寫死元素數——加族群或改元素都不必動這裡。PAGE_TITLE(<title>,分頁/SEO/
# 書籤)與 H1_TITLE(<h1>,頁面大標)是兩個獨立旋鈕,預設同字串,要各自演化改對應那行即可。
TITLE_TAIL = "汰弱留強掃描"          # 品牌尾綴;各族群動態標題共用
ALL_SCOPE  = "台股半導體與 AI 供應鏈"  # 「全部族群」時的範圍詞(2026-07-06 起含散熱/PCB,超出純半導體)
PAGE_TITLE = ALL_SCOPE + " · " + TITLE_TAIL   # <title> 預設(全部族群)
H1_TITLE   = ALL_SCOPE + " · " + TITLE_TAIL   # <h1> 預設(全部族群)

# 族群定義以 config/groups.csv → db `groups` 表為準;此處僅為舊 db 的退路預設
GROUP_ORDER = ["passive", "power", "packtest"]
GROUP_NM = {"passive": "被動元件", "power": "功率元件", "packtest": "封測"}
GROUP_TAG = {}
# 結論卡的族群標籤用短名(2~3 字,省空間);未列的族群自動退回全名。加族群時想更短就在這補一筆。
GROUP_SHORT = {"passive": "被動", "power": "功率", "packtest": "封測",
               "memory": "記憶體", "ipdesign": "矽智財", "semiequip": "設備"}
TIER_ORDER = ["真強", "蓄勢·外資佈局", "強但過熱", "潛在/中性", "真弱", "真弱·陷阱"]
TIER_VT = {"真強": 2, "蓄勢·外資佈局": 2, "強但過熱": 1, "潛在/中性": 0, "真弱": -2, "真弱·陷阱": -2}
TIER_COL = {"真強": "var(--strong)", "蓄勢·外資佈局": "var(--neutral)", "強但過熱": "var(--warn-line)",
            "潛在/中性": "var(--neutral)", "真弱": "var(--weak)", "真弱·陷阱": "var(--weak)"}
# DB tier key 是策略與 OOS 稽核契約,不可因 UI 改名而變動；畫面另用安全標籤，避免把
# 「族群內相對位置」誤讀成絕對買賣或保證強弱。
TIER_UI_LABEL = {
    "真強": "相對強勢",
    "蓄勢·外資佈局": "相對蓄勢",
    "強但過熱": "相對強勢·過熱",
    "潛在/中性": "中性觀察",
    "真弱": "相對弱勢",
    "真弱·陷阱": "相對弱勢·槓桿風險",
}
TIER_DESC = {
    "真強": "價格與籌碼指標多位於族群相對前段",
    "蓄勢·外資佈局": "籌碼指標相對位置靠前,價格尚未發動",
    "強但過熱": "價格相對靠前,但出現量能或融資過熱警示",
    "潛在/中性": "各指標相對位置分歧,持續觀察",
    "真弱": "價格與綜合指標位於族群相對後段",
    "真弱·陷阱": "外資相對位置靠後,且融資條件偏弱",
}

def pct(x, signed=False):
    """給『分數/比率』欄位(dist_hi、ret1、margin_chg):× 100 轉百分比。"""
    if x is None:
        return "-"
    return f"{x*100:+.1f}%" if signed else f"{x*100:.1f}%"


def pctp(x):
    """給『本身已是百分比』的欄位(turnover_pct / margin_util_pct):不再 × 100。"""
    return "-" if x is None else f"{x:.1f}%"


def market_source_text(provenance):
    """把 market_provenance 轉成使用者看得懂、可稽核的來源說明。"""
    if not provenance:
        return "大盤來源未記錄（舊資料庫）"
    source = provenance["canonical_source"]
    if source == MARKET_SOURCE_TWSE:
        checked = provenance["finmind_taiex"] is not None
        return ("TWSE 官方 MI_INDEX 發行量加權股價報酬指數"
                f"（FinMind {'已交叉驗證' if checked else '待交叉驗證'}）")
    if source == MARKET_SOURCE_FINMIND:
        return "FinMind TAIEX 含息報酬指數（TWSE 官方缺值備援）"
    if source == MARKET_SOURCE_LEGACY:
        return "FinMind TAIEX 含息報酬指數（舊資料，待來源遷移）"
    return f"大盤來源異常：{source}"

# 每個元素:score → 理由文字
R_PRICE = {2: "20日相對報酬位於族群前20%", 1: "20日相對報酬位於族群前20–40%",
           0: "20日相對報酬位於族群中段", -1: "20日相對報酬位於族群後20–40%",
           -2: "20日相對報酬位於族群後20%"}
R_RESIL = {2: "修正日抗跌程度位於族群前20%", -2: "修正日抗跌程度位於族群後20%"}
R_FOREIGN = {2: "外資變化位於族群前20%", 1: "外資變化位於族群前20–40%",
             0: "外資變化位於族群中段或雜訊區", -1: "外資變化位於族群後20–40%",
             -2: "外資變化位於族群後20%"}
R_TRUST = {2: "投信變化位於族群前20%", 1: "投信變化位於族群前20–40%",
           0: "投信變化位於族群中段或雜訊區", -1: "投信變化位於族群後20–40%",
           -2: "投信變化位於族群後20%"}
R_MARGIN = {2: "融資條件落在健康區", 1: "融資條件偏健康",
            0: "融資變化未觸發門檻", -1: "融資條件偏擁擠",
            -2: "融資增加幅度觸及高風險門檻"}
R_DIP = {2: "修正日買賣位於族群前20%", -2: "修正日買賣位於族群後20%"}
# 精簡標籤(給 vsub 用)
SALIENT = {("price", 2): "價格相對前段", ("price", -2): "價格相對後段",
           ("foreign", 2): "外資變化相對前段", ("foreign", -2): "外資變化相對後段",
           ("trust", 2): "投信變化相對前段", ("trust", -2): "投信變化相對後段",
           ("margin", 2): "融資條件偏健康", ("margin", -2): "融資槓桿風險偏高",
           ("dip", 2): "修正日買賣相對前段", ("dip", -2): "修正日買賣相對後段",
           ("resil", 2): "修正抗跌相對前段", ("resil", -2): "修正抗跌相對後段"}


def _relative_bucket(score):
    """排名分數的白話區間；0 也可能由死區強制歸零，故不可只寫「中間40%」。"""
    return {2: "族群前20%", 1: "族群前20–40%", 0: "族群中段或雜訊區",
            -1: "族群後20–40%", -2: "族群後20%"}.get(score, "族群相對位置未知")


def _cell(score, value, rows, reading, current, basis, warn=False, gfx=None):
    """固定 cell payload: [score,value,rows,reading,warn,current,basis,gfx]。

    current 是未經排名的當下方向；basis 才說明分數來自排名桶或固定門檻。兩者刻意分開，
    例如外資仍減持也可能因同業減持更多而落在族群前20%。
    gfx 是門檻制欄位(②量比/⑤融資水位)畫量尺用的原始數值;排名制欄位為 None
    (五分位條只需要分數本身)。
    """
    return [score, value, rows, reading, int(bool(warn)), current, basis, gfx]


def _value(row, key, default=None):
    """sqlite3.Row 與測試 dict 共用的安全取值。"""
    try:
        return row[key]
    except (KeyError, IndexError, TypeError):
        return default


def _fmt_price(x):
    if x is None:
        return "-"
    return f"{x:,.2f}".rstrip("0").rstrip(".")


def _fmt_volume(x):
    return "-" if x is None else f"{int(round(x)):,} 股"


def _fmt_lots(v):
    """張數帶正負號;0 不帶(避免顯示成「+0張」)。"""
    return f"{v:+,}張" if v else "0張"


def _ratio(a, b):
    return (a / b - 1) if (a is not None and b) else None


def _fmt_obs_pct(value, signed=False, digits=1):
    if value is None:
        return "-"
    sign = "+" if signed and value > 0 else ""
    return f"{sign}{value:.{digits}f}%"


def _fmt_obs_return(value):
    """Return difference stored as decimal -> percentage-point display."""
    if value is None:
        return "-"
    return f"{value * 100:+.1f}pp" if value else "0.0pp"


def _fmt_obs_lots(value, signed=True):
    if value is None:
        return "-"
    sign = "+" if signed and value > 0 else ""
    return f"{sign}{value:,.0f}張"


def _fmt_obs_share_lots(value, signed=True):
    """Institutional share count -> lots, retaining odd-lot precision."""
    if value is None:
        return "-"
    lots = value / 1000
    sign = "+" if signed and lots > 0 else ""
    return f"{sign}{lots:,.1f}張"


def _fmt_obs_shares(value, signed=True):
    if value is None:
        return "-"
    sign = "+" if signed and value > 0 else ""
    if abs(value) >= 10_000:
        return f"{sign}{value / 10_000:,.1f}萬股"
    return f"{sign}{value:,.0f}股"


def _fmt_obs_money(value):
    if value is None:
        return "-"
    if abs(value) >= 10_000:
        return f"{value / 10_000:,.1f}萬元"
    return f"{value:,.0f}元"


def _fmt_obs_breadth(value):
    return "-" if value is None else f"{value * 100:.0f}%"


def _obs_direction(name, value):
    if value is None:
        return f"{name}當日無買賣或資料不足"
    if value > 0:
        return f"{name}買方股數較多({_fmt_obs_pct(value, True)})"
    if value < 0:
        return f"{name}賣方股數較多({_fmt_obs_pct(value, True)})"
    return f"{name}買賣股數相等(0.0%)"


def build_observation_view(row):
    """個股 expanded raw fields 的數字解剖；純描述、不打分。"""
    foreign_strength = _value(row, "foreign_imbalance_pct")
    trust_strength = _value(row, "trust_imbalance_pct")
    dealer_self_strength = _value(row, "dealer_self_imbalance_pct")
    dealer_hedge_strength = _value(row, "dealer_hedge_imbalance_pct")
    inst_gross = _value(row, "inst_gross")
    participation = _value(row, "inst_participation_pct")

    avg_shares = _value(row, "avg_shares_per_trade")
    avg_value = _value(row, "avg_value_per_trade")
    trades = _value(row, "raw_trades")
    trade_value = (f"{int(trades):,}筆｜平均{avg_shares:,.0f}股／筆｜"
                   f"{_fmt_obs_money(avg_value)}／筆") if (
                       trades is not None and avg_shares is not None) else "資料不足"

    direction_value = (
        f"外資 {_fmt_obs_pct(foreign_strength, True)}"
        f"（買{_fmt_obs_share_lots(_value(row, 'raw_foreign_buy'), False)}／"
        f"賣{_fmt_obs_share_lots(_value(row, 'raw_foreign_sell'), False)}）｜"
        f"投信 {_fmt_obs_pct(trust_strength, True)}"
        f"（買{_fmt_obs_share_lots(_value(row, 'raw_trust_buy'), False)}／"
        f"賣{_fmt_obs_share_lots(_value(row, 'raw_trust_sell'), False)}）")
    direction_hint = (
        "方向強度=(買進−賣出)÷(買進＋賣出)。+100%=只有買進，−100%=只有賣出，"
        "0%=買賣一樣多；它回答單向程度，不是報酬預測。")

    activity_value = (f"四類法人合計 {_fmt_obs_share_lots(inst_gross, False)}｜"
                      f"占雙邊成交 {_fmt_obs_pct(participation)}")
    activity_hint = (
        "合計外資、投信、自營自行與避險的買進＋賣出；分母用2×成交量，因一筆成交同時有"
        "買方與賣方。數值高代表法人參與多，不代表一定淨買。")

    dealer_value = (f"自行 {_fmt_obs_share_lots(_value(row, 'raw_dealer_self_net'))}"
                    f" ({_fmt_obs_pct(dealer_self_strength, True)})｜避險 "
                    f"{_fmt_obs_share_lots(_value(row, 'raw_dealer_hedge_net'))}"
                    f" ({_fmt_obs_pct(dealer_hedge_strength, True)})")
    dealer_hint = (
        "自行買賣較接近自營商方向性庫存；避險常與權證、ETF或套利部位有關。"
        "兩者必須拆開，避險淨賣不能直接翻成自營商看空。")

    margin_flow = _value(row, "margin_net_flow")
    margin_change = _value(row, "margin_balance_change")
    margin_residual = _value(row, "margin_flow_residual")
    margin_value = (f"淨流量 {_fmt_obs_lots(margin_flow)}｜餘額實變 "
                    f"{_fmt_obs_lots(margin_change)}")
    margin_hint = (
        f"同一份官方日報：今日餘額 {_fmt_obs_lots(_value(row, 'raw_margin_bal'), False)} − "
        f"前日餘額 {_fmt_obs_lots(_value(row, 'raw_margin_prev_bal'), False)} = "
        f"餘額實變 {_fmt_obs_lots(margin_change)}。另一邊用流量驗算：資買 "
        f"{_fmt_obs_lots(_value(row, 'raw_margin_buy'), False)} − 資賣 "
        f"{_fmt_obs_lots(_value(row, 'raw_margin_sell'), False)} − 現償 "
        f"{_fmt_obs_lots(_value(row, 'raw_margin_cash_repay'), False)} = "
        f"{_fmt_obs_lots(margin_flow)}；兩式差額 {_fmt_obs_lots(margin_residual)}。"
        f"現償是用現金還掉融資；當日資券互抵 "
        f"{_fmt_obs_lots(_value(row, 'raw_offset_volume'), False)}。")

    short_flow = _value(row, "short_net_flow")
    short_change = _value(row, "short_balance_change")
    short_residual = _value(row, "short_flow_residual")
    short_value = (f"淨流量 {_fmt_obs_lots(short_flow)}｜餘額實變 "
                   f"{_fmt_obs_lots(short_change)}")
    short_hint = (
        f"同一份官方日報：今日餘額 {_fmt_obs_lots(_value(row, 'raw_short_bal'), False)} − "
        f"前日餘額 {_fmt_obs_lots(_value(row, 'raw_short_prev_bal'), False)} = "
        f"餘額實變 {_fmt_obs_lots(short_change)}。另一邊用流量驗算：券賣 "
        f"{_fmt_obs_lots(_value(row, 'raw_short_sell'), False)} − 券買 "
        f"{_fmt_obs_lots(_value(row, 'raw_short_buyback'), False)} − 券償 "
        f"{_fmt_obs_lots(_value(row, 'raw_short_stock_repay'), False)} = "
        f"{_fmt_obs_lots(short_flow)}；兩式差額 {_fmt_obs_lots(short_residual)}。"
        "券買是買回，券償是拿股票償還。")

    limit_value = (f"融資 {_fmt_obs_pct(_value(row, 'margin_limit_util_pct'))}｜"
                   f"融券 {_fmt_obs_pct(_value(row, 'short_limit_util_pct'))}")
    limit_hint = (
        "使用率=當日餘額÷交易所公告限額。這是官方信用額度使用程度；不同於既有"
        "「散戶水位」的融資餘額÷發行股數，兩個分母不能混用。")

    foreign_used = _value(row, "foreign_limit_used_pct")
    foreign_available = _value(row, "raw_foreign_available_shares")
    foreign_available_pct = _value(row, "raw_foreign_available_pct")
    foreign_value = (f"法令上限已用 {_fmt_obs_pct(foreign_used)}｜尚可投資 "
                     f"{_fmt_obs_shares(foreign_available, False)}"
                     f" ({_fmt_obs_pct(foreign_available_pct)}股本)")
    foreign_hint = (
        f"法令上限 {_fmt_obs_pct(_value(row, 'raw_foreign_limit_pct'))} 是外資最多可持有的"
        "股本比例；「已用」以實際外資持股除以法令容許股數。尚可投資空間低，只表示"
        "接近規範上限，不保證後續買賣方向。")

    sbl_flow = _value(row, "sbl_net_flow")
    sbl_change = _value(row, "sbl_balance_change")
    sbl_residual = _value(row, "sbl_flow_residual")
    sbl_value = (f"淨變動 {_fmt_obs_shares(sbl_flow)}｜餘額實變 "
                 f"{_fmt_obs_shares(sbl_change)}")
    sbl_hint = (
        f"新增賣出 {_fmt_obs_shares(_value(row, 'raw_sbl_sell'), False)} − 還券 "
        f"{_fmt_obs_shares(_value(row, 'raw_sbl_return'), False)} ＋ 調整 "
        f"{_fmt_obs_shares(_value(row, 'raw_sbl_adjustment'))} = "
        f"{_fmt_obs_shares(sbl_flow)}；公式差額 {_fmt_obs_shares(sbl_residual)}。"
        "調整若占主要部分，就不宜把餘額變化解讀成新空方部位。")
    sbl_limit_value = (f"今日新增使用昨日限額 "
                       f"{_fmt_obs_pct(_value(row, 'sbl_sell_limit_pct'))}｜"
                       f"次日公告限額 {_fmt_obs_shares(_value(row, 'raw_sbl_next_limit'), False)}")
    sbl_limit_hint = (
        "今天的借券賣出量應除以昨天公告的「次日限額」；今天欄位中的限額是明天才適用，"
        "不能拿當日餘額直接相除。")

    benchmark = _value(row, "benchmark_name") or "基準尚未配對"
    excess_value = (f"1日 {_fmt_obs_return(_value(row, 'excess_ret1'))}｜"
                    f"5日 {_fmt_obs_return(_value(row, 'excess_ret5'))}｜"
                    f"20日 {_fmt_obs_return(_value(row, 'excess_ret20'))}")
    excess_hint = (
        f"個股還原報酬−{benchmark}同期間報酬；正值=跑贏市場、負值=落後市場。"
        "上櫃報酬指數目前歷史較短，20日顯示「-」代表基準樣本不足，不是0%。")

    rows = [
        ["成交如何形成", trade_value,
         "成交量可拆成交易筆數×平均每筆股數；筆數多不等於投資人帳戶數變多。"],
        ["法人方向強度", direction_value, direction_hint],
        ["法人總活動量", activity_value, activity_hint],
        ["自營自行／避險", dealer_value, dealer_hint],
        ["融資餘額來源", margin_value, margin_hint],
        ["融券餘額來源", short_value, short_hint],
        ["官方信用限額", limit_value, limit_hint],
        ["外資法令上限", foreign_value, foreign_hint],
        ["借券新增／還券／調整", sbl_value, sbl_hint],
        ["借券賣出限額", sbl_limit_value, sbl_limit_hint],
        ["官方指數超額報酬", excess_value, excess_hint],
    ]

    summary_parts = [_obs_direction("外資", foreign_strength), _obs_direction("投信", trust_strength)]
    if participation is not None:
        summary_parts.append(f"追蹤法人占雙邊成交{participation:.1f}%")
    excess5 = _value(row, "excess_ret5")
    if excess5 is not None:
        summary_parts.append(f"近5日相對{benchmark}{'跑贏' if excess5 > 0 else '落後' if excess5 < 0 else '持平'}"
                             f"{abs(excess5) * 100:.1f}pp")
    why = "；".join(summary_parts) + "。以上回答交易與部位如何形成，不評定好壞，也不改分數。"
    return {
        "el": "新增官方資料 · 個股數據解剖", "scLabel": "觀察層 · 不計分",
        "scColor": "var(--ink-2)", "scBg": "var(--neutral-tint)",
        "rows": rows, "why": why,
        "howLabel": "建議閱讀順序",
        "how": ("先看法人方向強度與活動量，再核對融資／融券／借券餘額是由哪些流量形成，"
                "最後看限額與官方指數超額報酬。任何單日數字都只描述當下，不直接預測後續漲跌。"),
        "howLink": "前往頁尾查看交易／部位觀察指南", "howHref": "#flow-guide",
        "src": ("TWSE MI_INDEX、T86、MI_MARGN、MI_QFIIS、TWT93U；TPEx dailyQuotes、"
                "dailyTrade、margin/balance、insti/qfii、margin/sbl、tpex_reward_index"),
    }


def build_group_observation_view(row, name, tag=""):
    """族群版採成員中位與廣度，避免大型股用絕對張數支配結論。"""
    n = _value(row, "n", 0)
    foreign_breadth = _value(row, "foreign_buy_breadth")
    trust_breadth = _value(row, "trust_buy_breadth")
    rows = [
        ["法人方向中位",
         f"外資 {_fmt_obs_pct(_value(row, 'med_foreign_imbalance_pct'), True)}｜"
         f"投信 {_fmt_obs_pct(_value(row, 'med_trust_imbalance_pct'), True)}",
         f"買方較多的成員：外資 {_fmt_obs_breadth(foreign_breadth)}、投信 "
         f"{_fmt_obs_breadth(trust_breadth)}。中位數代表一半成員高於、一半低於，不讓單一大型股主導。"],
        ["法人參與中位",
         _fmt_obs_pct(_value(row, "med_inst_participation_pct")),
         "每檔先以四類法人買賣總量÷2×成交量，再取族群中位；高只代表參與多，不代表淨買。"],
        ["自營商淨額／成交量中位",
         f"自行 {_fmt_obs_pct(_value(row, 'med_dealer_self_net_volume_pct'), True, 2)}｜"
         f"避險 {_fmt_obs_pct(_value(row, 'med_dealer_hedge_net_volume_pct'), True, 2)}",
         "每檔先除以自己的成交量再取中位，讓大小型股可比；避險方向不等同自營商看多或看空。"],
        ["融資／融券淨流量中位",
         f"融資 {_fmt_obs_pct(_value(row, 'med_margin_net_flow_shares_pct'), True, 3)}股本｜"
         f"融券 {_fmt_obs_pct(_value(row, 'med_short_net_flow_shares_pct'), True, 3)}股本",
         "每檔的資買−資賣−現償、券賣−券買−券償，先除股本再取中位。"],
        ["官方限額使用中位",
         f"融資 {_fmt_obs_pct(_value(row, 'med_margin_limit_util_pct'))}｜"
         f"融券 {_fmt_obs_pct(_value(row, 'med_short_limit_util_pct'))}",
         "使用率是餘額÷交易所限額；只描述信用空間，不設本系統的新門檻。"],
        ["外資法令上限使用中位",
         _fmt_obs_pct(_value(row, "med_foreign_limit_used_pct")),
         "每檔外資實際持股÷法令容許持股，再取族群中位；接近100%代表法規空間較少。"],
        ["借券流量中位",
         f"新增 {_fmt_obs_pct(_value(row, 'med_sbl_sell_shares_pct'), True, 3)}｜"
         f"還券 {_fmt_obs_pct(_value(row, 'med_sbl_return_shares_pct'), True, 3)}｜"
         f"調整 {_fmt_obs_pct(_value(row, 'med_sbl_adjustment_shares_pct'), True, 3)}｜"
         f"淨額 {_fmt_obs_pct(_value(row, 'med_sbl_net_flow_shares_pct'), True, 3)}股本",
         "每檔先換算占股本比例再取中位，避免絕對股數把大型股放大。"],
        ["成員官方指數超額中位",
         f"1日 {_fmt_obs_return(_value(row, 'med_excess_ret1'))}｜"
         f"5日 {_fmt_obs_return(_value(row, 'med_excess_ret5'))}｜"
         f"20日 {_fmt_obs_return(_value(row, 'med_excess_ret20'))}",
         f"各成員依上市／上櫃扣除自己的官方含息指數，再取中位。有效樣本："
         f"1日 {_value(row, 'n_excess1', 0)}/{n}、5日 {_value(row, 'n_excess5', 0)}/{n}、"
         f"20日 {_value(row, 'n_excess20', 0)}/{n}；跑贏基準廣度分別為 "
         f"{_fmt_obs_breadth(_value(row, 'excess_breadth1'))}／"
         f"{_fmt_obs_breadth(_value(row, 'excess_breadth5'))}／"
         f"{_fmt_obs_breadth(_value(row, 'excess_breadth20'))}。"],
    ]
    return {
        "el": "新增官方資料 · 族群數據解剖", "who": name, "biz": tag,
        "scLabel": "觀察層 · 不計分", "scColor": "var(--ink-2)",
        "scBg": "var(--neutral-tint)", "rows": rows,
        "why": f"以{n}檔成員的中位數與廣度回答「這是普遍現象，還是少數個案」；不改族群狀態。",
        "howLabel": "聚合方式",
        "how": ("流量先按個股成交量或股本標準化，再取族群中位；超額報酬先逐檔扣除"
                "上市／上櫃官方含息指數。有效樣本少於6檔就留白。"),
        "howLink": "前往頁尾查看交易／部位觀察指南", "howHref": "#flow-guide",
        "src": "observation_metrics（TWSE／TPEx 官方五表與官方報酬指數衍生）",
    }


def _ma_price_position(close, ma_values):
    """白話列出現價相對三條均線的位置；不只拿 MA20 代表全部週期。"""
    above = [label for label, value in ma_values if close > value]
    below = [label for label, value in ma_values if close < value]
    equal = [label for label, value in ma_values if close == value]
    if len(above) == len(ma_values):
        return "現價高於MA5、MA20、MA60"
    if len(below) == len(ma_values):
        return "現價低於MA5、MA20、MA60"
    parts = []
    if above:
        parts.append("現價高於" + "、".join(above))
    if below:
        parts.append("低於" + "、".join(below))
    if equal:
        parts.append("約等於" + "、".join(equal))
    return "；".join(parts)


def _ma_distance_phrase(label, distance):
    if distance is None:
        return f"{label}距離資料不足"
    if distance > 0:
        return f"比{label}高{abs(distance)*100:.1f}%"
    if distance < 0:
        return f"比{label}低{abs(distance)*100:.1f}%"
    return f"約等於{label}"


def build_technical_view(m, history=None):
    """個股相對自身歷史的技術面觀察，不做族群排名、不影響分數或 tier。"""
    close = _value(m, "close_adj")
    ma5, ma20, ma60 = (_value(m, "ma5"), _value(m, "ma20"), _value(m, "ma60"))
    rsi = _value(m, "rsi14")
    volume, vma20, vr20 = (_value(m, "volume"), _value(m, "vol_ma20"),
                           _value(m, "vol_ratio20"))
    if any(v is None for v in (close, ma5, ma20, ma60, rsi)):
        return None

    series = list(history or [])
    current_date = _value(m, "date")
    if not series or (current_date and _value(series[-1], "date") != current_date):
        series.append(m)
    if current_date:
        series = [x for x in series if (_value(x, "date") or "") <= current_date]
    series.sort(key=lambda x: _value(x, "date", ""))
    prev = series[-2] if len(series) >= 2 else None
    five = series[-6] if len(series) >= 6 else None

    d5, d20, d60 = _ratio(close, ma5), _ratio(close, ma20), _ratio(close, ma60)
    ma_values = [("MA5", ma5), ("MA20", ma20), ("MA60", ma60)]
    price_position = _ma_price_position(close, ma_values)
    bull = ma5 > ma20 > ma60
    bear = ma5 < ma20 < ma60
    if bull:
        cls, label, structure = "up", "多頭排列", "MA5 > MA20 > MA60"
        structure_note = ("短、中、長期均線依序向上排列；" + price_position +
                          "。排列描述均線關係，不保證後續上漲")
    elif bear:
        cls, label, structure = "down", "空頭排列", "MA5 < MA20 < MA60"
        structure_note = ("短、中、長期均線依序向下排列；" + price_position +
                          "。排列描述均線關係，不代表已無反彈可能")
    elif close > ma20 and rsi >= 50:
        ordered = sorted(ma_values, key=lambda x: x[1], reverse=True)
        cls, label = "up", "趨勢偏多"
        structure = "由高到低：" + " > ".join(x[0] for x in ordered)
        structure_note = ("均線尚未形成標準多頭排列（MA5 > MA20 > MA60）；" +
                          price_position + "，價格位置偏強")
    elif close < ma20 and rsi < 50:
        ordered = sorted(ma_values, key=lambda x: x[1], reverse=True)
        cls, label = "down", "趨勢偏弱"
        structure = "由高到低：" + " > ".join(x[0] for x in ordered)
        structure_note = ("均線尚未形成標準空頭排列（MA5 < MA20 < MA60）；" +
                          price_position + "，價格位置偏弱")
    else:
        ordered = sorted(ma_values, key=lambda x: x[1], reverse=True)
        cls, label = "flat", "結構分歧"
        structure = "由高到低：" + " > ".join(x[0] for x in ordered)
        structure_note = ("均線與現價尚未形成一致方向；" + price_position +
                          "。不同週期訊號互相矛盾，單看一項指標容易誤判")

    if rsi >= 70:
        rsi_state = "上漲力道明顯較強"
        rsi_note = ("過去14個交易日的平均上漲力道明顯大於平均下跌力道；RSI≥70屬高檔區，"
                    "代表追價風險提高，但強趨勢中也可能維持高檔，不等於即將反轉")
    elif rsi <= 30:
        rsi_state = "下跌力道明顯較強"
        rsi_note = ("過去14個交易日的平均下跌力道明顯大於平均上漲力道；RSI≤30屬低檔區，"
                    "可能出現反彈，但不等於已經止跌")
    elif rsi >= 50:
        rsi_state = "上漲力道較強"
        rsi_note = ("過去14個交易日的平均上漲力道大於平均下跌力道；50是兩者的分界，"
                    "只描述近期力道，不代表股價一定續漲")
    else:
        rsi_state = "下跌力道較強"
        rsi_note = ("過去14個交易日的平均下跌力道大於平均上漲力道；50是兩者的分界，"
                    "只描述近期力道，不代表股價一定續跌")
    rsi5 = _value(five, "rsi14") if five else None
    rsi_delta = (rsi - rsi5) if rsi5 is not None else None
    rsi_display = f"{rsi:.1f} · {rsi_state}"
    if rsi_delta is not None:
        rsi_display += f"（較5日前 {rsi_delta:+.1f}）"

    ret1 = _value(m, "ret1")
    vol_state = ("量增" if vr20 is not None and vr20 >= 1.2 else
                 "量縮" if vr20 is not None and vr20 <= 0.8 else "量近平均")
    price_state = "價漲" if ret1 is not None and ret1 > 0 else "價跌" if ret1 is not None and ret1 < 0 else "價平"
    pv = price_state + vol_state
    pv_notes = {
        "價漲量增": "上漲伴隨高於20日均量的成交參與，價量方向互相確認",
        "價漲量縮": "價格上漲，但成交參與低於20日均量，延續力仍需後續量能確認",
        "價跌量增": "下跌伴隨高於20日均量的成交參與，短線賣壓較明顯",
        "價跌量縮": "價格下跌但成交參與有限，屬縮量整理或賣壓暫未擴大",
        "價平量增": "價格變化不大但成交活躍，可能處於換手，方向尚未表態",
        "價平量縮": "價格與成交都收斂，市場暫時觀望",
    }
    pv_note = pv_notes.get(pv, f"成交量約為20日均量的 {vr20:.2f}×，尚未出現明顯量增或量縮" if vr20 is not None else "量能樣本不足")

    events = []
    if prev:
        pc, pm20 = _value(prev, "close_adj"), _value(prev, "ma20")
        pm5 = _value(prev, "ma5")
        if None not in (pc, pm20):
            if pc <= pm20 and close > ma20:
                events.append("現價上穿MA20")
            elif pc >= pm20 and close < ma20:
                events.append("現價跌破MA20")
        if None not in (pm5, pm20):
            if pm5 <= pm20 and ma5 > ma20:
                events.append("MA5上穿MA20")
            elif pm5 >= pm20 and ma5 < ma20:
                events.append("MA5跌破MA20")
    if events:
        event_text = "、".join(events)
        event_note = "與前一交易日比較，發生上述跨越事件"
    elif prev:
        event_text = "無穿越事件"
        event_note = "與前一交易日比較：現價沒有跨越MA20，MA5也沒有跨越MA20"
    else:
        event_text = "穿越資料不足"
        event_note = "至少需要目前與前一個交易日的均線資料，才能判斷是否發生跨越"

    ma5_delta = _ratio(ma5, _value(five, "ma5")) if five else None
    ma20_delta = _ratio(ma20, _value(five, "ma20")) if five else None
    slope_text = (f"MA5較5日前 {pct(ma5_delta, True)}；MA20 {pct(ma20_delta, True)}"
                  if ma5_delta is not None and ma20_delta is not None else "均線5日變化樣本不足")
    distances = "、".join((_ma_distance_phrase("MA5", d5),
                            _ma_distance_phrase("MA20", d20),
                            _ma_distance_phrase("MA60", d60)))
    extension = ("其中與MA20的差距超過10%，代表現價和近20日平均價格距離較大；"
                 "不代表一定反彈或續跌" if d20 is not None and abs(d20) >= 0.10 else
                 f"與MA20的差距為{abs(d20)*100:.1f}%，仍在±10%觀察帶內"
                 if d20 is not None else "MA20距離資料不足")

    # CHART_DAYS 日互動股價圖原料(還原價+三均線+RSI14+量;外資/投信於掛 tech 處
    # 併入)。均線用全站既有 MA 識別色(橘/藍/紫,與文字列同源);MA20藍/MA60紫在
    # 綠色弱視下 ΔE 僅 6.2,故前端另以「線型」雙編碼(MA5短虛線/MA20實線/MA60
    # 長虛線)+圖例,不單靠顏色分。
    chart_rows = [x for x in series[-CHART_DAYS:]
                  if _value(x, "close_adj") is not None]     # 只要求有收盤價
    chart = None
    if len(chart_rows) >= 2:
        # 缺值填 null 佔位(不略過該日),各序列與 dates 一一對應;前端遇 null 斷線
        def _col(key, nd=2):
            return [(round(_value(x, key), nd) if _value(x, key) is not None else None)
                    for x in chart_rows]
        chart = {
            "dates": [_value(x, "date") for x in chart_rows],
            "px": _col("close_adj"),
            "ma5": _col("ma5"),
            "ma": _col("ma20"),          # 沿用舊名 ma = MA20,向後相容
            "ma60": _col("ma60"),
            "rsi": _col("rsi14", 1),
            "vol": [(int(_value(x, "volume")) if _value(x, "volume") is not None else None)
                    for x in chart_rows],
        }

    rows = [
        ["價格與均線",
         "／".join((f"現價 {_fmt_price(close)}", f"MA5 {_fmt_price(ma5)}",
                   f"MA20 {_fmt_price(ma20)}", f"MA60 {_fmt_price(ma60)}")),
         f"{price_position}：{distances}。{extension}"],
        ["均線結構", structure, structure_note],
        ["RSI14", rsi_display, rsi_note + "；括號是RSI較5個交易日前的增減，不是股價報酬率"],
        ["成交量 / 20日均量",
         f"{_fmt_volume(volume)} / {_fmt_volume(vma20)}" + (f"（{vr20:.2f}×）" if vr20 is not None else ""),
         "VOL以股數計；vol_ratio20=當日成交量÷20日平均成交量，≥1.2×視為量增、≤0.8×視為量縮"],
        ["今日價量關係", pv, pv_note],
        ["短線轉折（較前一交易日）", event_text, event_note + "；" + slope_text],
    ]
    why = f"{structure_note}；{rsi_note}；{pv_note}。"
    return {"cls": cls, "label": label, "rows": rows, "why": why,
            "chart": chart, "rsi": round(rsi, 1),
            "vr20": round(vr20, 2) if vr20 is not None else None,
            "series": [
                {"label": "現價", "value": _fmt_price(close), "cls": "price"},
                {"label": "MA5", "value": _fmt_price(ma5), "cls": "ma5"},
                {"label": "MA20", "value": _fmt_price(ma20), "cls": "ma20"},
                {"label": "MA60", "value": _fmt_price(ma60), "cls": "ma60"},
            ]}


def build_cells(sc, m, mkt20=None):
    """每格:[分數,格值,rows,相對判讀,過熱旗標,原始方向,計分依據]。

    原始方向與相對判讀不得合併：排名分數只表示「跟同族群相比」，不保證原始值為正。
    mkt20 = 大盤(報酬指數)20日報酬,全 universe 共用,僅供①價 tooltip 當基準線。"""
    cells = []
    # ① 價(族群內相對強弱;距高做輔助資訊)
    # 族群中位由定義還原(rs20 = ret20 − 族群中位),不必回 db 重算
    rs = m["rs20"]
    gmed = (m["ret20"] - rs) if (m["ret20"] is not None and rs is not None) else None
    rs_dyn = ("" if rs is None else
              (";目前=贏過至少一半同業" if rs > 0 else ";目前=輸給一半以上同業" if rs < 0 else ""))
    dist = m["dist_hi60"]
    dist_dyn = ("" if dist is None else
                (f";目前≤{STEALTH_OFF_HIGH*100:.0f}%=「價未動」(蓄勢條件之一)"
                 if dist <= STEALTH_OFF_HIGH else ";目前=接近波段高"))
    dr = m["down_rs20"]
    dr_dyn = ("" if dr is None else
              (";目前=修正日相對撐得住" if dr > 0 else ";目前=修正日跌得比同業重" if dr < 0 else ""))
    rows = [["20日報酬 − 族群中位", pct(rs, True),
             f"過去一個月跑贏同業多少——下面兩列相減;①價的分數就是此值的族群內排名{rs_dyn}"],
            ["└ 個股20日還原報酬", pct(m["ret20"], True)],
            ["└ 族群中位20日報酬", pct(gmed, True)],
            ["大盤20日(報酬指數,參考)", pct(mkt20, True),
             "全市場同窗口基準,不計分。個股與族群中位都贏大盤=強族群裡的強;只贏族群中位卻輸大盤=弱勢族群裡的相對強"],
            ["距60日高(還原價)", pct(dist),
             f"現價距近60日高點回落多少,0%=創新高附近{dist_dyn}", None, None, "",
             # 區間定位:右端=60日高(0%),刻度=蓄勢「價未動」門檻
             {"rp": [round(dist * 100, 1), min(-30.0, round(dist * 100, 1)), 0,
                     STEALTH_OFF_HIGH * 100, f"{STEALTH_OFF_HIGH*100:.0f}%蓄勢門檻"]}
             if dist is not None else None],
            ["修正日抗跌(20日)", f"{pct(dr, True)}(抗{sc['s_resil']:+d})",
             "族群下跌日平均比同業多漲(少跌)多少——大家一起跌時撐得住的才是真強"
             f"(獨立元素「抗」,權重{WEIGHTS['resil']},也是升蓄勢的品質門檻){dr_dyn}"],
            ["前一日漲跌", pct(m["ret1"], True)]]
    price_current = ("相對報酬資料不足" if rs is None else
                     f"20日相對報酬 {pct(rs, True)}，目前跑贏族群中位" if rs > 0 else
                     f"20日相對報酬 {pct(rs, True)}，目前跑輸族群中位" if rs < 0 else
                     "20日相對報酬 0.0%，目前與族群中位持平")
    # basis 只留會隨個股變動的排名桶;「分數=族群內排名」的常數語意放明細表欄位表頭
    # (dashboard_template 的 EL.sub),不跟著 Universe 長表逐格重複
    cells.append(_cell(
        sc["s_price"], pct(rs, True) if rs is not None else "-", rows, R_PRICE[sc["s_price"]],
        price_current, _relative_bucket(sc["s_price"])))
    # ② 量(量比 = 當日周轉率 / 自身60日中位)
    t = m["turnover_pct"]
    vr = m["vol_ratio60"]
    if t is not None and t >= 20:
        rv, warn = "周轉率過高、當沖過熱", 1
    elif vr is not None and vr >= 5:
        rv, warn = "量比爆增、過熱", 1
    elif sc["s_vol"] == 1:
        rv, warn = "量能健康活絡", 0
    elif sc["s_vol"] == -1:
        rv, warn = "量縮、人氣不足", 0
    else:
        rv, warn = "量能中等", 0
    vr_dyn = ("" if vr is None else
              (f";目前≥{VOLR_OVERHEAT:.0f}×=爆量過熱⚠" if vr >= VOLR_OVERHEAT else
               ";目前=健康活絡" if VOLR_ACTIVE[0] <= vr <= VOLR_ACTIVE[1] else
               f";目前<{VOLR_DRY}×=量縮無人氣" if vr < VOLR_DRY else ""))
    rows = [["量比(vs 自身60日中位)", f"{vr:.1f}×" if vr is not None else "樣本不足",
             "當日周轉率÷自己過去60日的常態(中位)——跟自己比,大型股不吃虧;"
             f"{VOLR_ACTIVE[0]}~{VOLR_ACTIVE[1]}×=健康活絡{vr_dyn}"],
            ["當日周轉率", pctp(t),
             f"成交股數佔發行股數%;≥{VOL_OVERHEAT:.0f}%=當沖過熱⚠(壓評級但不改分數)"]]
    vol_current = ("量比資料不足" if vr is None else
                   f"量比 {vr:.1f}×，高於自身60日常態" if vr > 1 else
                   f"量比 {vr:.1f}×，低於自身60日常態" if vr < 1 else
                   "量比 1.0×，與自身60日常態相當")
    # 固定門檻欄的門檻說明是常數(在欄位表頭與 tooltip),格內改放會變動的判讀語
    cells.append(_cell(
        sc["s_vol"], f"{vr:.1f}×" if vr is not None else "-", rows, rv, vol_current,
        rv,
        warn, round(vr, 2) if vr is not None else None))
    # ③ 外資
    fc = m["fpct_chg20"]
    fc_dyn = ("" if fc is None else
              (";目前=增持中" if fc > 0 else ";目前=減持中" if fc < 0 else ""))
    dp = m["dipbuy20"]
    dp_dyn = ("" if dp is None else
              (";目前=下跌日為外資淨買" if dp > 0 else ";目前=下跌日為外資淨賣" if dp < 0 else ""))
    rows = [["外資持股", f"{m['foreign_pct']:.1f}%" if m["foreign_pct"] is not None else "-",
             "外資目前持有比例(水位);看下列「變化」比看水位重要"],
            ["20日持股變化", f"{fc:+.2f}pp" if fc is not None else "-",
             f"近一個月外資增減持了多少百分點——③外資的分數即此值的族群內排名"
             f"(此檔 |變化| < {DZ_FOREIGN}pp 時視為雜訊並歸0分){fc_dyn}"],
            ["修正日買賣(20日)", f"{dp:+.2f}%股本(相對{sc['s_dip']:+d})" if dp is not None else "-",
             "族群下跌日外資買賣的20日累計佔股本%——正值是淨買,負值是淨賣"
             f"(括號分數為族群內排名,只用於蓄勢評級、不計分){dp_dyn}"]]
    # 「目前方向」句的慣例:動詞已帶方向(增持/減持、淨買/淨賣…)時數值用絕對值,
    # 避免「減持 -4.03pp」雙重否定;數據表 rows 是量值欄位,維持帶正負號。
    foreign_current = ("外資持股變化資料不足" if fc is None else
                       f"外資仍增持 {fc:.2f}pp" if fc > 0 else
                       f"外資仍減持 {abs(fc):.2f}pp" if fc < 0 else
                       "外資持股持平 0.00pp")
    cells.append(_cell(
        sc["s_foreign"], f"{fc:+.1f}pp" if fc is not None else "-", rows,
        R_FOREIGN[sc["s_foreign"]], foreign_current,
        _relative_bucket(sc["s_foreign"])))
    # ④ 投信
    t5 = m["trust5"] or 0
    tp = m["trust5_pct"]
    rows = [["近5日淨買賣", _fmt_lots(t5),
             "投信=本土基金；正值代表這5日累計淨買,負值代表累計淨賣"],
            ["佔股本", f"{tp:+.3f}%" if tp is not None else "-",
             f"上值換算佔股本%——④投信的分數即此值的族群內排名(消除股本大小差;"
             f"此檔 |佔股本變化| < {DZ_TRUST}% 時視為雜訊並歸0分)"]]
    if tp is not None:
        trust_current = (f"投信仍淨買 {abs(t5):,}張（{tp:.3f}%股本）" if tp > 0 else
                         f"投信仍淨賣 {abs(t5):,}張（{abs(tp):.3f}%股本）" if tp < 0 else
                         "投信買賣持平 0張（0.000%股本）")
    else:
        trust_current = "投信買賣資料不足"
    cells.append(_cell(
        sc["s_trust"], _fmt_lots(t5), rows, R_TRUST[sc["s_trust"]], trust_current,
        _relative_bucket(sc["s_trust"])))
    # ⑤ 融資券
    u = m["margin_util_pct"]
    u_dyn = ("" if u is None else
             (f";目前≥{MARGIN_UTIL_HOT:.0f}%=觸發過熱門檻⚠(分數封頂−1)" if u >= MARGIN_UTIL_HOT else
              f";目前≥{MARGIN_UTIL_MID:.0f}%=觸發中段水位門檻(分數封頂+1)" if u >= MARGIN_UTIL_MID else
              ";目前低於中段水位門檻"))
    mc10 = _value(m, "margin_chg10")
    mc5 = _value(m, "margin_chg5")
    mc = mc10 if mc10 is not None else mc5
    mc_window = 10 if mc10 is not None else 5 if mc5 is not None else None
    mc_dyn = ("" if mc is None else
              (";目前=融資餘額增加" if mc > 0 else ";目前=融資餘額下降" if mc < 0 else ""))
    rows = [["融資水位(融資/股本)", pctp(u),
             f"融資餘額佔股本%,用來觀察市場槓桿擁擠程度{u_dyn}"],
            [f"{mc_window}日融資變化" if mc_window else "融資變化", pct(mc, True),
             f"融資餘額增加或下降的幅度；與下列價格方向交互給分:價跌且融資下降代表槓桿同步降低,"
             f"價跌且融資明顯增加代表槓桿風險升高；10日缺值時採5日備援{mc_dyn}"],
            ["20日還原價報酬", pct(m["ret20"], True),
             "供上列交互判定的價格方向(與①價的原料同值)"],
            ["券資比", f"{(m['short_margin_ratio'] or 0):.1f}%",
             "融券餘額÷融資餘額;高=空方對作或軋空題材。參考欄位,未計分"]]
    fallback = "（5日備援）" if mc_window == 5 else ""
    margin_current = ("融資變化資料不足" if mc is None else
                      f"融資{mc_window}日仍增加 {pct(mc)}{fallback}" if mc > 0 else
                      f"融資{mc_window}日仍下降 {pct(abs(mc))}{fallback}" if mc < 0 else
                      f"融資{mc_window}日持平 0.0%{fallback}")
    if u is not None:
        margin_current += f"；目前水位 {u:.1f}%"
    cells.append(_cell(
        sc["s_margin"], pctp(u), rows, R_MARGIN[sc["s_margin"]], margin_current,
        R_MARGIN[sc["s_margin"]],
        u is not None and u >= 9, round(u, 2) if u is not None else None))
    return cells


def tier_ui_payload(sc):
    """保留策略 key，另提供不把相對排名說成絕對強弱的 UI label。"""
    confirmed = sc["tier"]
    raw = sc["tier_raw"]
    return {
        "tier_raw": raw,
        "tier_confirmed": confirmed,
        "tier_waiting": raw != confirmed,
        "tier_label": TIER_UI_LABEL.get(confirmed, confirmed),
        "tier_raw_label": TIER_UI_LABEL.get(raw, raw),
    }


def verdict(sc, comp_history=None):
    tier = sc["tier"]
    comp = sc["composite_s"]
    keys = [("price", sc["s_price"]), ("resil", sc["s_resil"]), ("vol", sc["s_vol"]),
            ("foreign", sc["s_foreign"]), ("trust", sc["s_trust"]), ("dip", sc["s_dip"]),
            ("margin", sc["s_margin"])]
    labels = [SALIENT[k] for k in keys if k in SALIENT]
    vsub = " · ".join(labels[:2]) if labels else f"綜合 {comp:+.1f}"
    chip = sc["s_foreign"] >= 2 or sc["s_dip"] >= 2
    if sc["pending"] and tier == "潛在/中性":       # 蓄勢候補(score.py 資料層算好)
        vsub = "◇ " + sc["pending"]
    elif chip and sc["s_resil"] <= -2:              # 衝突組合改方向性敘述,避免讀成自相矛盾
        vsub = "籌碼相對靠前·等抗跌轉正"
    drivers = []
    for name, ref in [("價", "s_price"), ("抗跌", "s_resil"), ("外資", "s_foreign"),
                      ("逆勢", "s_dip"), ("投信", "s_trust"), ("融資", "s_margin")]:
        s = sc[ref]
        if abs(s) >= 2:
            drivers.append({"外資": R_FOREIGN, "逆勢": R_DIP, "投信": R_TRUST,
                            "融資": R_MARGIN, "價": R_PRICE, "抗跌": R_RESIL}[name][s])
    vr = "；".join(drivers) if drivers else "訊號分歧,持續觀察"
    if sc["pending"] and tier == "潛在/中性":
        vr += (f"。◇ {sc['pending']}——籌碼相對位置條件已符；補齊後先成為今日初判,"
               "連2日相同初判才更新已確認層")
    elif chip and sc["s_resil"] <= -2:
        vr += ("。籌碼指標在族群相對靠前,但修正日價格位於相對後段——原始值未必是買超；"
               "此類歷史樣本表現分歧,詳見週報的同條件比較,等抗跌轉正再確認")
    # 元素 × 權重分解:依左側①②③④⑤自然順序(不依權重大小排,避免循環數字跳來跳去)。
    # 每列 = [標籤, 顯示值, hint(此表不用), 分數(供JS用scColor上色), 權重文字(muted顯示), flag,
    #         貢獻數值(供JS畫等尺度貢獻條;None=不畫)]
    # flag: "total"=加大加粗、"muted"=整列調淡(權重0=只供tier判定、不計入加總——由 WEIGHTS 動態判斷,
    # 不寫死是哪個元素,權重一旦調整就自動跟著變)
    def vrow(label, key, wkey):
        v = sc[key]
        weight = WEIGHTS[wkey]
        tier_only = weight == 0
        contribution = v * weight
        # 「只供分層條件」放 hint(項目第二行)而非黏在算式後——長字串會把該列算式
        # 推離右緣,破壞跨列的數字對齊
        wt = f"× {weight:g} = {contribution:+.1f}"
        return [label, f"{v:+d}",
                "權重 0:不計入加總,只作為分層判定條件" if tier_only else None,
                v, wt, "muted" if tier_only else "",
                None if tier_only else round(contribution, 2)]
    today = sc["composite"]
    vrows = [["今日分(未平滑)", f"{today:+.1f}", "下列各項元素分 × 權重的貢獻加總",
              round(today, 1), None, "total", round(today, 2)],
             vrow("①相對強弱", "s_price", "price"),
             vrow("①抗跌", "s_resil", "resil"),
             vrow("②量", "s_vol", "vol"),
             vrow("③外資", "s_foreign", "foreign"),
             vrow("③修正日相對位置", "s_dip", "dip"),
             vrow("④投信", "s_trust", "trust"),
             vrow("⑤融資券", "s_margin", "margin")]
    history = list(comp_history or [])[-3:]
    if history:
        parts, values = [], []
        for h in history:
            date, value = _value(h, "date"), _value(h, "composite")
            if value is None:
                continue
            values.append(value)
            date_label = f"{int(date[5:7])}/{int(date[8:10])}" if date else "-"
            parts.append(f"{date_label} {value:+.1f}")
        if values:
            equation = " + ".join(f"({v:+.1f})" for v in values)
            vrows.append(["近3個交易日", " → ".join(parts),
                          "每天依元素分與權重加總出的未平滑分", None, None, "", None])
            vrows.append(["3日平均(評級用)", f"{comp:+.1f}",
                          f"({equation}) ÷ {len(values)} = {comp:+.1f}", round(comp, 1), None, "total",
                          round(comp, 2)])
    else:
        vrows.append(["3日平均(評級用)", f"{comp:+.1f}",
                      "每日未平滑分歷史未提供；此值取自資料庫既有的三日平滑結果",
                      round(comp, 1), None, "total", round(comp, 2)])
    return TIER_VT.get(tier, 0), tier, vsub, vr, int(sc["warn"]), vrows


# 籌碼健康度(觀察層、純描述性,獨立於①價②量與 tier)——net_score/label 已由
# score.py 的 chip_health 表算好;這裡只重算「每個信號」的顯示明細(門檻沿用 score.py 匯入的
# 同一份常數,跟①②③④⑤ element cells 的 hint 現算是同一套慣例,不重複造輪子)。
CHIP_LABELS = ["外資20日變化(↑增持)", "投信近5日佔股本(↑買超)",
               "融資水位(低水位較健康)", "融資10日變化(↓去槓桿)",
               "大戶400張+週變化(↑集中·觀察)", "股東人數週變化(↓集中·觀察)",
               "借券餘額10日變化(↓減壓·觀察)"]


def _raw_direction(v, up, down, flat):
    if v is None:
        return "資料不足"
    if v > 0:
        return up
    if v < 0:
        return down
    return flat


def _chip_reading(direction, signal, observational=False):
    verdict = "健康訊號" if signal > 0 else "警示" if signal < 0 else "中性"
    note = "；方向尚未用規則定案後的新資料驗證" if observational else "；依既有校準門檻"
    if direction == "資料不足":
        return "資料不足 → 中性(不計健康/警示)" + ("；方向尚未用規則定案後的新資料驗證" if observational else "")
    return f"{direction} → 本欄判讀為{verdict}{note}"


def _chip_pp(v):
    """觀察欄保留微小正負方向；避免 ±0.004pp 被兩位小數顯示成 ±0.00pp。"""
    if v is None:
        return "-"
    if v == 0:
        return "0.00pp"
    if abs(v) < 0.00005:
        return ("+" if v > 0 else "-") + "<0.0001pp"
    if abs(v) < 0.005:
        return f"{v:+.4f}pp"
    return f"{v:+.2f}pp"


def build_chip_rows(m, risky):
    """回傳 (rows, n_health, n_warn)——rows 給 tooltip 表格,n_health/n_warn 給判讀句(不含官方否決項)。"""
    fc, tp, u, mc = m["fpct_chg20"], m["trust5_pct"], m["margin_util_pct"], m["margin_chg10"]
    tb, tpl, sb = m["tdcc_big400_chg"], m["tdcc_people_chg"], m["sbl_chg10"]
    sigs = [
        _chip_signal(fc, lambda v: v > DZ_FOREIGN, lambda v: v < -DZ_FOREIGN),
        _chip_signal(tp, lambda v: v > DZ_TRUST, lambda v: v < -DZ_TRUST),
        _chip_signal(u, lambda v: v < MARGIN_UTIL_MID, lambda v: v >= MARGIN_UTIL_HOT),
        _chip_signal(mc, lambda v: v <= MARGIN_DOWN_BIG, lambda v: v >= MARGIN_UP_BIG),
        _chip_signal(tb, lambda v: v > 0, lambda v: v < 0),
        _chip_signal(tpl, lambda v: v < 0, lambda v: v > 0),
        _chip_signal(sb, lambda v: v < 0, lambda v: v > 0),
    ]
    vals = [f"{fc:+.2f}pp" if fc is not None else "-",
            f"{tp:+.3f}%" if tp is not None else "-",
            pctp(u),
            pct(mc, True) if mc is not None else "-",
            _chip_pp(tb),
            pct(tpl, True) if tpl is not None else "-",
            _chip_pp(sb)]
    directions = [
        _raw_direction(fc, "外資增持", "外資減持", "外資持股持平"),
        _raw_direction(tp, "投信買超", "投信賣超", "投信持平"),
        ("資料不足" if u is None else
         "融資低水位" if sigs[2] > 0 else "融資高水位" if sigs[2] < 0 else "融資中等水位"),
        _raw_direction(mc, "融資增加(槓桿升高)", "融資下降(去槓桿)", "融資持平"),
        _raw_direction(tb, "大戶集中度上升", "大戶集中度下降", "大戶集中度持平"),
        _raw_direction(tpl, "股東人數增加(籌碼分散)", "股東人數下降(籌碼集中)", "股東人數持平"),
        _raw_direction(sb, "借券賣出餘額增加(壓力升高)", "借券賣出餘額下降(壓力減輕)",
                       "借券賣出餘額持平"),
    ]
    rows = [[lb, v, _chip_reading(direction, s, i >= 4), s, None, ""]
            for i, (lb, v, direction, s) in enumerate(zip(CHIP_LABELS, vals, directions, sigs))]
    rows.append(["官方處置/注意", "有列管" if risky else "無",
                 "交易所列管 → 一票否決為待觀察" if risky else "當天無交易所列管",
                 (-1 if risky else 0), None, ""])
    n_health = sum(1 for s in sigs if s > 0)
    n_warn = sum(1 for s in sigs if s < 0)
    return rows, n_health, n_warn


# 基本面參考(觀察層、不計分,獨立於①②③④⑤ tier)——月營收/季報由 fetch_financials.py
# 獨立排程填入(月/季頻,非每日,見 CLAUDE.md)。只用月營收 YoY/MoM + 損益表毛利率趨勢/EPS;
# 資產負債表/現金流量表型態太細(單期 ~90 個 type),不上儀表板,留供 Universe 治理(R1)查證用。
FUND_YOY_UP, FUND_YOY_DOWN = 0.10, -0.10   # 月營收年增分類門檻(僅供 badge 顏色分類,不影響 tier)


def _prev_month(y, m):
    return (y, m - 1) if m > 1 else (y - 1, 12)


def build_fund_map(con):
    """批次查詢全 universe 的基本面參考資料,回傳 {stock_id: tooltip payload}。
    缺資料(新股/尚未回補)的股票不進 dict,前端不顯示 badge——不強求每檔都有。"""
    mr_by_sid = defaultdict(list)
    for r in con.execute("""SELECT stock_id, date, revenue, revenue_year, revenue_month
                            FROM month_revenue ORDER BY stock_id, date DESC"""):
        mr_by_sid[r["stock_id"]].append(r)
    fin_by_sid = defaultdict(dict)
    for r in con.execute("""SELECT stock_id, date, type, value FROM financials
                            WHERE type IN ('Revenue','GrossProfit','EPS')"""):
        fin_by_sid[r["stock_id"]].setdefault(r["date"], {})[r["type"]] = r["value"]

    out = {}
    for sid, mrs in mr_by_sid.items():
        latest = mrs[0]
        py, pm = _prev_month(latest["revenue_year"], latest["revenue_month"])
        mom = (latest["revenue"] / mrs[1]["revenue"] - 1) if (
            len(mrs) > 1 and mrs[1]["revenue"] and
            mrs[1]["revenue_year"] == py and mrs[1]["revenue_month"] == pm) else None
        yoy_row = next((r for r in mrs[1:] if r["revenue_year"] == latest["revenue_year"] - 1
                        and r["revenue_month"] == latest["revenue_month"]), None)
        yoy = (latest["revenue"] / yoy_row["revenue"] - 1) if (yoy_row and yoy_row["revenue"]) else None

        fq = fin_by_sid.get(sid, {})
        fdates = sorted(fq)[-4:]   # 近4季,舊到新
        gms = [(d, (fq[d]["GrossProfit"] / fq[d]["Revenue"] * 100)
                if (fq[d].get("Revenue") and fq[d].get("GrossProfit") is not None) else None)
               for d in fdates]
        latest_eps = fq[fdates[-1]].get("EPS") if fdates else None

        if yoy is None and mom is None and not fdates:
            continue
        cls = ("up" if (yoy is not None and yoy >= FUND_YOY_UP) else
               "down" if (yoy is not None and yoy <= FUND_YOY_DOWN) else "flat")
        rows = [["最新月營收", f"{latest['revenue']/1e8:,.1f} 億元"
                 f"({latest['revenue_year']}/{latest['revenue_month']:02d})", None],
                ["月增(MoM)", f"{mom*100:+.1f}%" if mom is not None else "-", "與上月比"],
                ["年增(YoY)", f"{yoy*100:+.1f}%" if yoy is not None else "-",
                 "與去年同月比——台股最常見的營收動能指標"]]
        if gms:
            trend = " → ".join(f"{g:.1f}%" if g is not None else "-" for _, g in gms)
            rows.append(["近4季毛利率趨勢", trend, f"{fdates[0]} ~ {fdates[-1]},舊到新"])
        if latest_eps is not None:
            rows.append(["最新季EPS", f"{latest_eps:.2f} 元", f"季別:{fdates[-1]}"])
        # 近13個月營收柱形原料(舊到新,億元):第1柱≈最新月的去年同月,基期效應
        # (去年同月特別低造成的高YoY)看柱形一眼識破——與 why 文案的警告同源
        spark_rows = [x for x in mrs[:13] if x["revenue"] is not None][::-1]
        spark = [round(x["revenue"] / 1e8, 2) for x in spark_rows]
        spark_dates = [f"{x['revenue_year']}/{x['revenue_month']:02d}" for x in spark_rows]
        label = f"營收YoY {yoy*100:+.0f}%" if yoy is not None else "營收YoY 資料不足"
        if yoy is not None:
            direction = "增加" if yoy > 0 else "減少" if yoy < 0 else "持平"
            why = (f"最新單月營收較去年同月{direction} {abs(yoy)*100:.1f}%。這只是已公告營收的"
                   "同比描述；營收不等於獲利,也不能單獨代表需求或整體營運變強/變弱。基期、"
                   "收入認列時點、工作天數、售價、併購與產品組合都可能影響單月數字,"
                   "需搭配公司筆記與季報判讀。")
        else:
            why = ("月營收年增樣本不足(上市未滿13個月或資料尚未回補齊)。營收不等於獲利或"
                   "整體營運強弱；即使有月增資料,仍可能受基期、收入認列時點、工作天數、售價、"
                   "併購與產品組合影響。")
        out[sid] = {"cls": cls, "label": label, "rows": rows, "why": why,
                    "spark": spark if len(spark) >= 2 else None,
                    "sparkDates": spark_dates if len(spark) >= 2 else None}
    return out


# 族群狀態→顏色(狀態本身由 fetch_daily._gstate 在資料層算好,存 group_metrics.state)
# 蓄勢用 --warn 而非 --warn-line:此色會當「狀態文字」的前景色,warn-line(#d69e2e)在
# 淺色 surface 上對比僅約 2.2:1,warn 是同語彙的可讀文字版
STATE_COL = {"蓄勢·被佈局": "var(--warn)", "發動·領漲": "var(--strong)",
             "籌碼退潮": "var(--weak)"}

# 族群卡 tooltip 教學文字(門檻值 import 自 fetch_daily,改旋鈕自動同步)。
# 各指標的定義寫在每列數據自己的 hint(見 groups 組裝),這裡只留狀態判定規則。
GROUP_HOW = (
    f"族群狀態每日由上列指標判定(規則在資料層,非儀表板):蓄勢·被佈局=修正日中位買賣>0 且 "
    f"中位距60日高≤{GS_OFF_HIGH*100:+.0f}%(修正日外資為淨買,且價格尚未回高);"
    f"發動·領漲=20日動能贏全體 且 價近波段高;籌碼退潮=修正日遭調節 且 佈局廣度≤"
    f"{GS_BREADTH_LOW*100:.0f}%;其餘=中性觀察。修正日中位買賣為選族群主訊號(樣本外驗證中,"
    f"見週報)。卡片把『目前原始值』與『較5日前的變化』分欄顯示；改善不代表已轉為正值。")
GROUP_SRC = "個股五元素於族群層聚合(等權中位數/廣度);五張原始表 TWSE/TPEx 官方批次"


def _streak(series):
    """最新狀態往回連續了幾個交易日、自哪天起。series 依日期升冪。"""
    if not series:
        return None, None
    cur, n = series[-1]["state"], 0
    for x in reversed(series):
        if x["state"] != cur:
            break
        n += 1
    d = series[-n]["date"]
    return n, f"{int(d[5:7])}/{int(d[8:10])}"


def _five_day_delta(series, key, eps, scale=1.0, digits=2):
    """回傳獨立的 5 日比較文字；較高一律稱改善，並保留 delta 正負號。"""
    if len(series) < 6:
        return "5日比較資料不足"
    cur, prev = series[-1][key], series[-6][key]
    if cur is None or prev is None:
        return "5日比較資料不足"
    delta = cur - prev
    direction = "改善" if delta >= eps else "惡化" if delta <= -eps else "持平"
    return f"較5日前{direction} {delta*scale:+.{digits}f}pp"


def _five_day_value(series, key):
    """圖像化座標的五日前 raw 值；樣本或欄位不足時明確回傳 null。"""
    if len(series) < 6:
        return None
    return series[-6][key]


def _current_dip(v):
    """動詞已帶方向 → 數值用絕對值(「淨賣 -0.27%」是雙重否定,且與 build_overview
    摘要句的「仍淨賣 0.27%股本」寫法不一致)。"""
    if v is None:
        return "-"
    if v > 0:
        return f"淨買 {v:.2f}%股本"
    if v < 0:
        return f"淨賣 {abs(v):.2f}%股本"
    return "買賣持平 0.00%股本"


def _current_relative(v):
    if v is None:
        return "-"
    if v > 0:
        return f"跑贏 {v*100:.1f}%"
    if v < 0:
        return f"跑輸 {abs(v)*100:.1f}%"
    return "與全體持平 0.0%"


def build_overview(grows):
    """首頁白話結論；明確區分『相對最好』與『原始值已轉正』。"""
    if not grows:
        return {"headline": "族群資料不足", "summary": "目前無法判讀族群強弱。",
                "points": [], "note": "請先確認 group_metrics 已更新。"}
    deployed = [r for r in grows if r["state"] == "蓄勢·被佈局"]
    dips = [r for r in grows if r["med_dip"] is not None]
    rels = [r for r in grows if r["rel20"] is not None]
    best_dip = max(dips, key=lambda r: r["med_dip"]) if dips else None
    best_rel = max(rels, key=lambda r: r["rel20"]) if rels else None

    if deployed:
        names = "、".join(GROUP_NM.get(r["grp"], r["grp"]) for r in deployed)
        headline = f"{names}目前符合「被佈局」條件"
        summary = "此狀態要求修正日中位買賣為正,並同時符合價格尚未回高的條件。"
        tone = "strong"
    elif best_dip and all(r["med_dip"] <= 0 for r in dips):
        nm = GROUP_NM.get(best_dip["grp"], best_dip["grp"])
        headline = "目前沒有族群符合「被佈局」條件"
        summary = (f"{len(dips)}/{len(grows)} 族群的修正日中位皆為淨賣；{nm}的調節相對最少,"
                   f"但仍淨賣 {abs(best_dip['med_dip']):.2f}%股本；"
                   "相對最好不等於已出現買超。")
        tone = "warn"
    else:
        headline = "目前沒有族群符合「被佈局」條件"
        if best_dip:
            nm = GROUP_NM.get(best_dip["grp"], best_dip["grp"])
            summary = (f"{nm}修正日淨買相對最高（{best_dip['med_dip']:+.2f}%股本）,"
                       "但尚未同時符合完整狀態條件。")
        else:
            summary = "修正日籌碼資料不足,暫不做族群佈局判讀。"
        tone = "neutral"

    points = []
    if best_dip:
        nm = GROUP_NM.get(best_dip["grp"], best_dip["grp"])
        points.append({"label": "籌碼相對位置", "text": f"{nm}：{_current_dip(best_dip['med_dip'])}",
                       "tone": "strong" if best_dip["med_dip"] > 0 else "warn"})
    if best_rel:
        nm = GROUP_NM.get(best_rel["grp"], best_rel["grp"])
        points.append({"label": "價格相對位置", "text": f"{nm}：{_current_relative(best_rel['rel20'])}",
                       "tone": "strong" if best_rel["rel20"] > 0 else "warn"})
    return {"headline": headline, "summary": summary, "points": points, "tone": tone,
            "note": "族群比較是相對結果；請同時閱讀目前原始值與5日變化。"}


# ── 策略狀態(證據強度)────────────────────────────────────────────────
# 儀表板原本只傳達「透明可追溯」(每個分數都能點開追到原始數字),沒有傳達「這套規則
# 有多可信」。這裡補上證據強度那一軸。
#
# **只放事實,不放判斷**——這是刻意的界線:
#   可以放:IS 校準窗、OOS 快照/成熟日數(證據狀態的事實)、
#           ρ 與有效因子數、停留天數與名單換手(結構與描述統計,不需前瞻報酬)
#   不可以放:個別因子「可不可靠」的結論。那些 IC 數字絕大部分來自 IS 窗,
#           拿 in-sample 證據在使用者看得到的地方下判斷,正是鐵律禁止的事。
# tier 的績效數字(超額/勝率/IC)一律不複製到這裡,只連向週報——避免與 validate.py
# 的 §② 各算一份而漂移。
def build_strategy_status(con, last):
    """回傳首屏「策略狀態」卡片的資料;任何一段算不出來就給 None,前端略過該行。

    自己查完整交易日列表——main() 的 tier_dates 只有近 5 日,拿它算成熟度與停留期會錯。
    """
    dates = [r[0] for r in con.execute(
        "SELECT DISTINCT date FROM daily_scores WHERE date<=? ORDER BY date", (last,))]
    try:
        from validate import IS_CUTOFF          # 單一真相來源(改權重必須同步改它)
    except Exception:
        IS_CUTOFF = None
    st = {"is_start": dates[0] if dates else None, "is_cutoff": IS_CUTOFF,
          "fwd": sig.EVAL_HORIZON_DAYS, "report_url": None}

    # OOS:as-seen 快照日數,以及其中前瞻窗已走完(可判讀)的日數
    try:
        snap = [r[0] for r in con.execute(
            """SELECT DISTINCT data_date FROM oos_snapshot_runs
               WHERE is_official=1 ORDER BY data_date""")]
        didx = {d: i for i, d in enumerate(dates)}
        oos = [d for d in snap if IS_CUTOFF and d > IS_CUTOFF and d in didx]
        st["oos_days"] = len(oos)
        st["oos_mature"] = sum(1 for d in oos if didx[d] + st["fwd"] < len(dates))
    except sqlite3.OperationalError:
        st["oos_days"] = st["oos_mature"] = None

    # 結構:訊號集中度(當日橫斷面)
    try:
        s = sig.summarize(sig.group_rows(con, last))
        if s:
            st["lead"] = s["lead"]
            st["lead_rho"] = s["lead_rho"]
            st["eff"] = s["eff_factors"]
            st["n_scored"] = len(s["churn"])
    except Exception:
        pass

    # 結構:分層穩定度(以真強 = 畫面的「相對強勢」為代表)
    try:
        ch = sig.churn_summary(sig.tier_sequences(con), dates)
        if ch:
            st["dwell"] = ch["dwell"].get("真強")
            tv = ch["turnover"].get("真強") or {}
            st["turn_days"] = tv.get("full_turn_days")
            st["round_trip"] = ch["round_trip"][2]
            st["round_trip_window"] = sig.ROUND_TRIP_WINDOW
    except Exception:
        pass

    # 週報連結:報告以資料迄日命名,取實際存在的最新一份。
    # §② 的錨點用「實際掃出的行號」而非標題 anchor——GitHub 對中文標題產生的 anchor
    # 難以預測且會隨標點變動;行號每次 build 重新掃,報告改版也自動跟上。
    try:
        rdir = os.path.join(ROOT, "reports")
        rep = sorted(f for f in os.listdir(rdir)
                     if f.startswith("validate_") and f.endswith(".md"))
        if rep:
            st["report_url"] = NOTE_REPO_BLOB + "reports/" + rep[-1]
            with open(os.path.join(rdir, rep[-1]), encoding="utf-8") as fh:
                for i, line in enumerate(fh, 1):
                    if line.startswith("## ②"):
                        st["report_tier_url"] = f"{st['report_url']}#L{i}"
                        break
    except OSError:
        pass
    return st


# ── 兩視角分歧(價格 vs 籌碼)────────────────────────────────────────────
# 為什麼值得單獨一段:價格與籌碼是兩個近乎正交的視角(族群內排名相關 ρ≈0.27),分歧本身
# 就是可讀的市場狀態——動能強而籌碼弱 = 漲了但沒人接;反之 = 有人在買但價格還沒動。
#
# **這是描述,不是訊號。** 它有沒有預測力正由事先登錄的假設 H1 檢定中(週報 §⑪),
# 目前尚無結論;籌碼分數刻意直接用 hypotheses.CHIP_WEIGHTS,讓畫面顯示的與 H1 檢定的
# 是同一個東西。
#
# 單日 ρ 不可裸讀:實測全期 80 日中位 +0.25、標準差 0.15,所以一律附歷史百分位與近 5 日
# ——2026-07-24 的 −0.13 落在第 4 百分位、且近 5 日連續為負,那才是有意義的敘述。
def _names(con):
    return {r["stock_id"]: r["name"] for r in con.execute(
        "SELECT stock_id, name FROM universe")}


def build_divergence(con, last, names, group_names):
    """回傳兩視角分歧的 payload;任何一段算不出來就給 None,前端略過。"""
    try:
        today = sig.divergence_summary(sig.group_rows(con, last), hyp.CHIP_WEIGHTS)
        if not today:
            return None
        dates = [r[0] for r in con.execute(
            "SELECT DISTINCT date FROM daily_scores WHERE date<=? ORDER BY date", (last,))]
        hist = {}
        for d in dates:
            s = sig.divergence_summary(sig.group_rows(con, d), hyp.CHIP_WEIGHTS)
            if s and s["rho_median"] is not None:
                hist[d] = s["rho_median"]
        vals = sorted(hist.values())
        cur = hist.get(last)
        pct = (sum(1 for x in vals if x <= cur) / len(vals) * 100) if (vals and cur is not None) else None

        # 20 日絕對報酬:兩欄都是族群內名次,沒有它就會被讀成漲跌
        # (2026-07-24:標題原本說「價格還沒動」的 8 檔全部為負,最深 −34.3%)
        r20 = {r["stock_id"]: r["ret20"] for r in con.execute(
            "SELECT stock_id, ret20 FROM daily_metrics WHERE date=?", (last,))}

        def deco(x):
            v = r20.get(x["stock_id"])
            return {"id": x["stock_id"], "nm": names.get(x["stock_id"], x["stock_id"]),
                    "g": group_names.get(x["grp"], x["grp"]),
                    "mom": x["mom_pct"], "chip": x["chip_pct"], "gap": x["gap"],
                    "r20": round(v * 100, 1) if v is not None else None}

        first_month = dates[0][:7] if dates else None
        fm = [v for d, v in hist.items() if d[:7] == first_month]
        return {
            "rho": cur, "rho_pct": pct, "rho_median_all": statistics.median(vals) if vals else None,
            "n_days": len(vals),
            "recent": [{"d": d, "v": round(hist[d], 3)} for d in dates[-5:] if d in hist],
            "first_month": first_month,
            "first_month_median": statistics.median(fm) if fm else None,
            "threshold": sig.DIVERGE_NOTABLE,
            "price_ahead": [deco(x) for x in today["price_ahead"][:8]],
            "chips_ahead": [deco(x) for x in today["chips_ahead"][:8]],
            "n_price_ahead": len(today["price_ahead"]),
            "n_chips_ahead": len(today["chips_ahead"]),
        }
    except sqlite3.Error:
        # 只吞資料層問題(舊 db 缺表/缺欄)。程式錯誤必須炸出來——
        # 原本寫 `except Exception` 把 `statistics` 未 import 的 NameError 吃掉了,
        # 結果整段靜默消失、build 還印「已重生」看起來成功。
        return None


def build_lenses(con, last, names, group_names):
    """時間尺度視角 payload。整套訊號只有 20 日一個週期,這裡把同一檔放到
    短(5日)/波段(20日)/趨勢(20日vs60日)三個尺度上各排一次名。

    與分歧視角相同:描述用,未計分、未進 tier、不作前瞻報酬主張。"""
    try:
        s = sig.time_lens_summary(sig.group_metric_rows(con, last))
        if not s:
            return None
        # 冗餘判定不能只看一天:單日 ρ 很吵(2026-07-24 的 short-trend 是 −0.29,
        # 全期卻接近 0)。逐日算再取中位,並同時給出今日值,與分歧區同一套呈現。
        # ⚠ 這裡的歷史 ρ 用**今日的** universe 族群歸屬回推過去(group_metric_rows
        # join 的是 universe 現況),不是 as-seen。季度 universe 調整會讓已顯示過的
        # 全期中位悄悄改變。這個數字只用來判斷「三欄會不會重複」,不進 OOS、
        # 不當證據;真要當證據就得改讀 oos_signal_snapshots(欄位是齊的)。
        # 起算日 = 三個視角都排得出來的第一天(ma60 要 60 個交易日暖身),
        # 讓前端能誠實說出「這個視角只有 N 天資料」而不是看起來與其他區同齡。
        days = [r[0] for r in con.execute(
            """SELECT DISTINCT date FROM daily_metrics
               WHERE ma60 IS NOT NULL AND ma5 IS NOT NULL AND ret20 IS NOT NULL
               AND date<=? ORDER BY date""", (last,))]
        hist = {}
        for d in days:
            hs = sig.time_lens_summary(sig.group_metric_rows(con, d))
            if hs:
                for k, v in hs["rho"].items():
                    if v is not None:
                        hist.setdefault(k, []).append(v)
        rho_median = {k: round(statistics.median(v), 2) for k, v in hist.items() if v}
        first, n_days = (days[0] if days else None), len(days)
        # 這段窗口的大盤走勢由資料現算,**不可寫死**。初版把「先漲 8.2% 到 6/22
        # 再回 7.9%」直接寫在文案裡,而窗口每個交易日都會長一天:隔天動態的
        # 「41 個交易日」會變 42,旁邊那句硬字仍寫「41 天」;「再回 7.9%」是
        # 高點到最新日,每天都不同;大盤一旦收破前高,「6/22 的期間高」直接變假話。
        path = None
        if days:
            mk = [(r[0], r[1]) for r in con.execute(
                "SELECT date, taiex FROM market_daily WHERE date>=? AND date<=? ORDER BY date",
                (days[0], last)) if r[1]]
            if len(mk) >= 3:
                pk = max(mk, key=lambda x: x[1])
                path = {"rise": round((pk[1] / mk[0][1] - 1) * 100, 1),
                        "peak": pk[0], "peak_i": [d for d, _ in mk].index(pk[0]) + 1,
                        "n": len(mk),
                        "fall": round((mk[-1][1] / pk[1] - 1) * 100, 1)}
        tiers = {r["stock_id"]: r["tier"] for r in con.execute(
            "SELECT stock_id, tier FROM daily_scores WHERE date=?", (last,))}

        def deco(x):
            # r20 = 20 日絕對報酬。名次形狀旁一定要有它:族群內名次不含漲跌資訊,
            # 只給名次會讓「名次靠前」再一次被讀成「在漲」。
            return {"id": x["stock_id"], "nm": names.get(x["stock_id"], x["stock_id"]),
                    "g": group_names.get(x["grp"], x["grp"]),
                    "tier": tiers.get(x["stock_id"]),
                    "s": x["pct"]["short"], "w": x["pct"]["swing"], "t": x["pct"]["trend"],
                    "r20": x["raw"]["swing"], "raw": x["raw"], "sp": x["spread"]}

        return {
            "rho": {k: (round(v, 2) if v is not None else None) for k, v in s["rho"].items()},
            "rho_median": rho_median,
            "path": path,
            "spread_median": s["spread_median"], "threshold": sig.LENS_SPREAD_NOTABLE,
            "n_notable": len(s["notable"]), "n_total": len(s["detail"]),
            "first_date": first, "n_days": n_days,
            "all": [deco(x) for x in sorted(s["detail"], key=lambda x: -x["spread"])],
        }
    except sqlite3.Error:
        return None


def _article_date(value):
    """只接受可稽核的 YYYY-MM-DD meta；不碰檔案 mtime 或建置機器時間。"""
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def _article_excerpt(value, limit=116):
    """把既有 parser 的標題／摘要壓成首頁可讀的一行，不重新解讀文章內容。"""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", str(value or ""))
    text = re.sub(r"[*_`]+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    cut = max(text.rfind(mark, 0, limit + 1) for mark in "。；！？")
    return text[:cut + 1] if cut >= limit // 2 else text[:limit].rstrip() + "…"


def _article_metadata_usable(info):
    """契約失敗的文章不拿來推動 feed anchor，避免壞日期把整個 14 天窗帶走。"""
    return bool(info) and not info.get("quality_invalid") and not info.get("quality_errors")


def _event_research_id(event):
    """事件錨點在研究中心的穩定深連結；不依檔名語系或排序位置。"""
    subject = re.sub(r"[^a-z0-9]+", "-", (event.get("subject") or "market").lower()).strip("-")
    period = re.sub(
        r"[^a-z0-9]+", "-",
        (event.get("fiscal_quarter") or event.get("event_date") or "undated").lower(),
    ).strip("-")
    return f"event-{subject or 'market'}-{period or 'undated'}"


def build_recent_articles(market_date, notes, reports, events=None, topics=None,
                          stock_names=None, days=RECENT_ARTICLE_DAYS):
    """聚合近期研究文章；anchor=max(市場資料日,可解析文章日期)，確保快照可重現。"""
    market_anchor = _article_date(market_date)
    if market_anchor is None:
        raise ValueError(f"market_date 不是合法 YYYY-MM-DD：{market_date}")
    if days < 1:
        raise ValueError("days 必須至少為 1")

    stock_names = stock_names or {}
    candidates = []
    type_order = {key: index for index, (key, _label) in enumerate(RECENT_ARTICLE_TYPES)}
    type_labels = dict(RECENT_ARTICLE_TYPES)

    def stock_subject(stock_id, relpath=""):
        name = stock_names.get(stock_id)
        if not name and relpath:
            stem = os.path.splitext(os.path.basename(relpath))[0]
            if "_" in stem:
                name = stem.split("_", 1)[1]
        return " ".join(part for part in (stock_id, name) if part) or "未指定公司"

    def add(value, article_type, stock_id, subject, title, relpath, status, status_tone,
            research_id=None):
        parsed = _article_date(value)
        if parsed is None or not relpath:
            return
        candidates.append({
            "_date": parsed,
            "date": parsed.isoformat(),
            "type": article_type,
            "typeLabel": type_labels[article_type],
            "stockId": stock_id or "",
            "subject": subject,
            "title": _article_excerpt(title) or type_labels[article_type],
            "url": NOTE_REPO_BLOB + relpath,
            "status": status,
            "statusTone": status_tone,
            "researchId": research_id,
            "relpath": relpath,
        })

    for stock_id, note in (notes or {}).items():
        if not _article_metadata_usable(note):
            continue
        verification = note_review_status(note)
        tone = ("verified" if verification == "independently_verified"
                else "warning" if verification == "conflicted" else "draft")
        add(
            note.get("last_updated"), "formal_note", stock_id,
            stock_subject(stock_id, note.get("relpath", "")),
            note.get("summary") or f"{stock_subject(stock_id)}質化研究筆記",
            note.get("relpath"), NOTE_LABEL.get(verification, verification), tone,
            f"formal-{stock_id}",
        )

    for stock_id, report in (reports or {}).items():
        if not _article_metadata_usable(report):
            continue
        narrative = report.get("narrative")
        if not narrative:
            continue
        hypothesis_titles = [
            item.get("title", "").strip() for item in report.get("hypotheses", [])
            if item.get("title", "").strip()
        ]
        title = ("／".join(hypothesis_titles[:2]) if hypothesis_titles
                 else "看多、看空觀點與勝負手")
        add(
            narrative.get("updated"), "narrative", stock_id,
            stock_subject(stock_id, report.get("relpath", "")),
            title, report.get("relpath"), "觀察層・不等於事實認證", "observational",
            f"narrative-{stock_id}",
        )

    for topic in topics or []:
        if not _article_metadata_usable(topic):
            continue
        meta = topic.get("meta") or {}
        topic_date = (meta.get("last_reviewed_at")
                      if _article_date(meta.get("last_reviewed_at"))
                      else topic.get("captured_at"))
        stock_ids = topic.get("stock_ids") or []
        if stock_ids:
            subject = "、".join(stock_subject(sid) for sid in stock_ids)
            sort_stock = stock_ids[0]
        elif topic.get("group_ids"):
            subject = "跨族群：" + "、".join(topic["group_ids"])
            sort_stock = ""
        else:
            subject, sort_stock = "市場／政策", ""
        add(
            topic_date, "topic", sort_stock, subject, topic.get("title"),
            topic.get("relpath"), "候選議題・不等於正式公司事實", "observational",
            f"topic-{topic.get('topic_id') or os.path.basename(topic.get('relpath', 'topic'))}",
        )

    for event in (events or {}).get("all", []):
        if not _article_metadata_usable(event):
            continue
        event_date = (event.get("content_as_of")
                      if _article_date(event.get("content_as_of"))
                      else event.get("event_date"))
        subject_key = event.get("subject") or ""
        subject = "2330 台積電" if subject_key == "tsmc" else subject_key or "市場事件"
        stock_id = "2330" if subject_key == "tsmc" else ""
        verification = event.get("verification") or "ai_draft"
        tone = ("verified" if verification == "independently_verified"
                else "warning" if verification == "conflicted" else "draft")
        add(
            event_date, "topic", stock_id, subject, event.get("title"),
            event.get("relpath"), NOTE_LABEL.get(verification, verification), tone,
            _event_research_id(event),
        )

    anchor = max([market_anchor] + [item["_date"] for item in candidates])
    start = anchor - dt.timedelta(days=days - 1)
    items = [item for item in candidates if start <= item["_date"] <= anchor]
    items.sort(key=lambda item: (
        -item["_date"].toordinal(),
        type_order[item["type"]],
        item["stockId"],
        item["relpath"],
    ))
    for item in items:
        del item["_date"]
        del item["relpath"]

    counts = {key: 0 for key, _label in RECENT_ARTICLE_TYPES}
    for item in items:
        counts[item["type"]] += 1
    return {
        "anchor": anchor.isoformat(),
        "start": start.isoformat(),
        "days": days,
        "total": len(items),
        "counts": [
            {"type": key, "label": label, "count": counts[key]}
            for key, label in RECENT_ARTICLE_TYPES
        ],
        "items": items,
    }


def attach_research_library_progress(recent, research_library):
    """讓首頁摘要與研究中心使用同一份文章集合，並在不一致時直接中止 build。"""
    result = dict(recent)
    articles = research_library.get("articles") or []
    library_counts = research_library.get("counts") or {}
    result["libraryTotal"] = research_library.get("total", len(articles))
    result["libraryCounts"] = [
        {"type": key, "label": label, "count": int(library_counts.get(key, 0))}
        for key, label in RECENT_ARTICLE_TYPES
    ]

    item_dates = [item["date"] for item in result.get("items", [])
                  if _article_date(item.get("date"))]
    latest_date = max(item_dates) if item_dates else None
    result["latestDate"] = latest_date
    result["latestCount"] = sum(
        item.get("date") == latest_date for item in result.get("items", [])
    ) if latest_date else 0

    start = _article_date(result.get("start"))
    anchor = _article_date(result.get("anchor"))
    expected_ids = {
        article.get("id") for article in articles
        if article.get("id") and start and anchor
        and (article_date := _article_date(article.get("date")))
        and start <= article_date <= anchor
    }
    actual_ids = {
        item.get("researchId") for item in result.get("items", [])
        if item.get("researchId")
    }
    if expected_ids != actual_ids:
        missing = sorted(expected_ids - actual_ids)
        unexpected = sorted(actual_ids - expected_ids)
        raise ValueError(
            "首頁研究摘要與研究中心文章集合不一致；"
            f"漏列={missing or '無'}；多列={unexpected or '無'}"
        )
    return result


def _research_run(value, bold=False):
    """研究中心合成表格使用與 Markdown parser 相同的 inline run 格式。"""
    run = {"s": str(value if value not in (None, "") else "—")}
    if bold:
        run["b"] = True
    return [run]


def _research_labeled_run(label, value):
    """Make generated reader summaries scan like prose, not ledger output."""
    return [
        {"s": f"{label}：", "b": True},
        {"s": str(value if value not in (None, "") else "—")},
    ]


def _inline_script_json(value):
    """JSON 嵌入 script 時避開 HTML parser 的結束標籤與 entity 邊界。"""
    return (json.dumps(value, ensure_ascii=False)
            .replace("&", "\\u0026")
            .replace("<", "\\u003c")
            .replace(">", "\\u003e"))


def _research_source_refs(source_ids, source_by_id):
    labels = []
    for source_id in source_ids or []:
        source = source_by_id.get(source_id) or {}
        title = source.get("title") or source.get("document") or ""
        labels.append(f"{source_id} {title}".strip())
    return "、".join(labels) or "—"


def _topic_analyst_section(topic, source_by_id, group_names=None):
    """由 v3 register 合成首屏重點；只摘要既有結論、證據與追蹤項目。"""
    group_names = group_names or {}
    claims = [
        item for item in (topic.get("claims") or [])
        if item.get("status", "active") == "active"
    ]
    claim_by_id = {item.get("claim_id"): item for item in claims}
    meta = topic.get("meta") or {}
    thesis = claim_by_id.get(meta.get("thesis_claim_id"))
    if thesis is None and claims:
        thesis = claims[0]
    if thesis is None:
        return None

    supporting_ids = thesis.get("supporting_source_ids") or []
    supporting_sources = [
        source_by_id[source_id] for source_id in supporting_ids
        if source_id in source_by_id
        and source_by_id[source_id].get("status", "active") == "active"
    ]
    independence_groups = {
        (source.get("independence_group") or source.get("publisher")
         or source.get("source_id") or source.get("id") or "unknown")
        .strip().lower()
        for source in supporting_sources
    }
    confidence = topic.get("confidence") or {}
    confidence_label = (
        confidence.get("effective_label")
        or {"high": "高", "medium": "中", "low": "低"}.get(
            meta.get("base_confidence"), meta.get("base_confidence") or "未評級")
    )
    thesis_label = thesis.get("label_text") or thesis.get("label") or "—"

    unverified = [item for item in claims if item.get("label") == "unverified"]
    if unverified:
        gap = unverified[0].get("claim") or "—"
        if len(unverified) > 1:
            gap += f"（另有 {len(unverified) - 1} 項待驗證）"
    else:
        gap = "目前沒有列出待查證的主張；仍要依文章註明的適用範圍閱讀。"

    direction_labels = {
        "tailwind": "可能有利", "headwind": "可能不利", "mixed": "正反訊號並存",
        "uncertain": "方向未定",
    }
    action_labels = {
        "none": "目前不需處理", "watch": "持續觀察", "review_due": "待複核",
        "update_required": "需要更新", "done": "已完成",
    }
    routed = []
    for item in topic.get("impacts") or []:
        scope = group_names.get(item.get("group_id"), item.get("group_id") or "—")
        action = action_labels.get(
            item.get("note_action"), item.get("note_action") or "—")
        direction = direction_labels.get(item.get("direction"), item.get("direction") or "—")
        routed.append(f"{scope}（{direction}／{action}）")
    route_text = "、".join(routed) if routed else "目前尚未連到特定公司或族群。"

    active_monitors = [
        item for item in (topic.get("monitoring") or [])
        if item.get("status", "active") == "active"
    ]
    active_monitors.sort(key=lambda item: item.get("next_check") or "9999-12-31")
    if active_monitors:
        first_monitor = active_monitors[0]
        next_check = (
            f"{first_monitor.get('next_check') or '—'}："
            f"{first_monitor.get('trigger') or first_monitor.get('metric') or '—'}"
        )
    else:
        next_check = "目前沒有安排下一次檢查；本文不應被當成永久有效的結論。"

    evidence_text = (
        f"證據可信度為{confidence_label}；主結論標記為「{thesis_label}」，"
        f"目前有 {len(supporting_sources)} 份有效來源，"
        f"分屬 {len(independence_groups)} 條互相獨立的來源鏈。"
    )
    claim_key = thesis.get("label") or ""
    claim_meaning = {
        "verified": (
            "指定來源直接支持這句主張的精確措辭；"
            "仍只在來源寫明的範圍內成立。"
        ),
        "inference": (
            "這句是把已接受資料連起來後得到的研究判讀；"
            "推理材料有來源支持，但不是任一來源逐字寫出的整句結論。"
        ),
        "unverified": (
            "這句仍待下一份證據驗證；目前不能當成已發生的事實。"
        ),
    }.get(
        claim_key,
        "先回查原始主張與來源；這個標記尚未落在新制三種主張類型。",
    )
    return {
        "h": "研究摘要：已知、未知與下一步",
        "readerEvidenceGuide": {
            "claimKey": claim_key,
            "claimLabel": thesis_label,
            "claimMeaning": claim_meaning,
            "confidenceKey": (
                confidence.get("effective") or meta.get("base_confidence") or "unrated"
            ),
            "confidenceLabel": confidence_label,
            "confidenceMeaning": (
                "衡量來源品質、獨立消息鏈、反方證據與主要缺口；"
                "不是主張真假，也不是發生機率。"
            ),
            "sourceCount": len(supporting_sources),
            "independenceCount": len(independence_groups),
            "boundary": (
                "主張類型與證據可信度是兩把不同的尺；"
                "都不能直接換算成公司訂單、受惠程度或投資排名。"
            ),
        },
        "blocks": [
            {"t": "p", "runs": _research_run(
                "以下只整理原始文章已有的結論與證據，不會改變查核狀態。")},
            {"t": "ul", "items": [
                _research_labeled_run("一句話結論", thesis.get("claim") or "—"),
                _research_labeled_run("目前已知", evidence_text),
                _research_labeled_run("尚未知道", gap),
                _research_labeled_run("對哪些族群有意義", route_text),
                _research_labeled_run("下一步看什麼", next_check),
            ]},
        ],
    }


def _topic_structured_sections(topic, sections, group_names=None):
    """把 v3 ledger 轉成讀者可見段落；原始 Markdown blocks 仍是唯一事實來源。"""
    sections = [section for section in (sections or []) if section.get("blocks")]
    source_by_id = {
        source.get("source_id") or source.get("id"): source
        for source in topic.get("sources") or []
        if source.get("source_id") or source.get("id")
    }
    generated = []

    # 原文的帳本導言仍保留，但由完整結構化表格承接，避免同一文章出現兩個近義標題。
    ledger_headings = {"主張與證據帳本", "主張—證據帳本"}
    original_ledger_blocks = []
    retained_sections = []
    for section in sections:
        if section.get("h") in ledger_headings:
            original_ledger_blocks.extend(section.get("blocks") or [])
        else:
            retained_sections.append(section)
    sections = retained_sections

    claims = topic.get("claims") or []
    if claims:
        rows = []
        for claim in claims:
            supporting = _research_source_refs(
                claim.get("supporting_source_ids"), source_by_id)
            contrary = _research_source_refs(
                claim.get("contrary_source_ids"), source_by_id)
            evidence = f"支持：{supporting}；反證：{contrary}"
            next_step = claim.get("verification_needed") or "—"
            if str(next_step).lower() == "none":
                next_step = "—"
            correction = []
            if claim.get("corrects_claim_id"):
                verb = ("取代" if claim.get("correction_kind") == "supersedes"
                        else "推翻")
                correction.append(f"{verb} {claim['corrects_claim_id']}")
            if claim.get("corrected_by_claim_id"):
                correction.append(f"由 {claim['corrected_by_claim_id']} 修正")
            resolution = claim.get("resolution") or ""
            if resolution and resolution.lower() not in {"active", "open"}:
                correction.append(f"反證裁決：{resolution}")
            rows.append([
                _research_run(
                    f"{claim.get('claim_id') or '—'}｜"
                    f"{claim.get('label_text') or claim.get('label') or '—'}｜"
                    f"{claim.get('status_text') or claim.get('status') or '—'}",
                    bold=True,
                ),
                _research_run(claim.get("claim")),
                _research_run(evidence),
                _research_run(claim.get("basis")),
                _research_run(claim.get("boundary")),
                _research_run("；".join(correction) or "—"),
                _research_run(next_step),
            ])
        generated.append({
            "h": "主張—證據帳本",
            "blocks": [
                *original_ledger_blocks,
                {"t": "p", "runs": _research_run(
                    "「證實」只表示目前一手證據直接支持；「推論」與「待驗證」"
                    "仍須依後續節點更新，不能當成個股訂單或報酬保證。")},
                {"t": "table", "head": [
                    _research_run("狀態"), _research_run("主張"),
                    _research_run("支持／反證來源"), _research_run("查核／推論基礎"),
                    _research_run("證據邊界"), _research_run("修正／反證裁決"),
                    _research_run("下一步驗證"),
                ], "rows": rows},
            ],
        })

    impacts = topic.get("impacts") or []
    if impacts:
        rows = []
        for item in impacts:
            scope = item.get("group_id") or "—"
            if item.get("stock_ids"):
                scope += "｜" + "、".join(item["stock_ids"])
            action = item.get("note_action") or "—"
            if item.get("action_due"):
                action += f"；期限 {item['action_due']}"
            rows.append([
                _research_run(scope, bold=True),
                _research_run(item.get("direction")),
                _research_run(action),
                _research_run("、".join(item.get("hypothesis_refs") or []) or "—"),
                _research_run(item.get("rationale")),
                _research_run(item.get("evidence_boundary")),
            ])
        generated.append({
            "h": "影響路由與證據邊界",
            "blocks": [{"t": "table", "head": [
                _research_run("族群／個股"), _research_run("方向"),
                _research_run("筆記動作／期限"), _research_run("關聯假說"),
                _research_run("路由理由"), _research_run("證據邊界"),
            ], "rows": rows}],
        })

    comparisons = topic.get("comparisons") or []
    if comparisons:
        rows = []
        for item in comparisons:
            period = "～".join(filter(None, (
                item.get("period_start"), item.get("period_end")))) or "—"
            if item.get("period_basis"):
                period += f"（{item['period_basis']}）"
            value = str(item.get("reported_value") or "—")
            if item.get("value_kind") == "range":
                value = value.replace("..", "–")
            elif item.get("value_kind") == "lower_bound":
                value = ">" + value
            elif item.get("value_kind") == "upper_bound":
                value = "<" + value
            if item.get("normalized_value"):
                value += (f"；正規化 {item['normalized_value']} "
                          f"{item.get('normalized_unit') or ''}").rstrip()
            definition = f"{item.get('unit') or '—'}；{item.get('definition') or '—'}"
            comparability = (
                f"{item.get('comparability_text') or item.get('comparability') or '—'}："
                f"{item.get('comparability_reason') or '—'}"
            )
            if item.get("normalization_method"):
                comparability += f"；正規化方法：{item['normalization_method']}"
            evidence = _research_source_refs(item.get("evidence_ids"), source_by_id)
            claim_status = {
                "active": "現行", "superseded": "已取代", "refuted": "已推翻",
            }.get(item.get("claim_status"), item.get("claim_status") or "—")
            rows.append([
                _research_run(
                    f"{item.get('comparison_id') or '—'}｜"
                    f"{item.get('claim_id') or '—'}｜"
                    f"{claim_status}",
                    bold=True,
                ),
                _research_run(item.get("entity")),
                _research_run(f"{item.get('metric') or '—'}：{value}"),
                _research_run(period),
                _research_run(definition),
                _research_run(evidence),
                _research_run(comparability),
            ])
        generated.append({
            "h": "跨公司數字可比性",
            "blocks": [{"t": "table", "head": [
                _research_run("比較組／主張"), _research_run("公司／對象"),
                _research_run("指標與原值"), _research_run("期間"),
                _research_run("單位／定義"), _research_run("證據來源"),
                _research_run("可比性／正規化"),
            ], "rows": rows}],
        })

    monitoring = topic.get("monitoring") or []
    if monitoring:
        rows = []
        for item in monitoring:
            source_refs = _research_source_refs(item.get("source_ids"), source_by_id)
            watch_refs = _research_source_refs(
                item.get("watch_source_ids"), source_by_id)
            schedule = item.get("frequency") or "—"
            if item.get("frequency_detail"):
                schedule += f"（{item['frequency_detail']}）"
            if item.get("status") == "retired":
                schedule += (
                    f"；退役 {item.get('retired_at') or '—'}；"
                    f"原因：{item.get('retirement_reason') or '—'}")
            else:
                schedule += f"；下次 {item.get('next_check') or '—'}"
            rows.append([
                _research_run(
                    f"{item.get('monitor_id') or '—'}｜"
                    f"{'現行' if item.get('status') == 'active' else '已退役'}",
                    bold=True,
                ),
                _research_run("、".join(item.get("claim_ids") or []) or "—"),
                _research_run(f"{item.get('metric') or '—'}；基準來源：{source_refs}"),
                _research_run(watch_refs),
                _research_run(schedule),
                _research_run(item.get("trigger")),
                _research_run(item.get("invalidation")),
            ])
        generated.append({
            "h": "追蹤節點與失效條件",
            "blocks": [{"t": "table", "head": [
                _research_run("節點"), _research_run("關聯主張"),
                _research_run("指標／基準來源"), _research_run("回查入口"),
                _research_run("頻率／下次檢查"),
                _research_run("觸發條件"), _research_run("失效條件"),
            ], "rows": rows}],
        })

    analyst = _topic_analyst_section(topic, source_by_id, group_names)
    if not generated:
        return ([analyst] if analyst else []) + sections

    # 先讓讀者理解機制與研究判定，再提供完整控制表；來源清單仍留在詳細帳本之後。
    source_index = next(
        (index for index, section in enumerate(sections)
         if section.get("h") in {"來源", "來源與證據邊界"}),
        len(sections),
    )
    result = sections[:source_index] + generated + sections[source_index:]
    return ([analyst] if analyst else []) + result


def _reader_group_labels_in_sections(sections, group_names=None):
    """Replace opaque group IDs only in reader-visible runs and headings.

    Machine-readable topic metadata and source URLs keep their registered IDs.  The
    replacement is deliberately limited to identifiers that are not normal prose;
    generic technical words such as ``power`` or ``memory`` are never rewritten.
    """
    group_names = group_names or {}
    replacements = [
        (re.compile(
            rf"(?<![A-Za-z0-9_]){re.escape(group_id)}(?![A-Za-z0-9_-])",
            re.IGNORECASE,
        ), group_names.get(group_id) or group_id)
        for group_id in READER_OPAQUE_GROUP_IDS
        if group_names.get(group_id) and group_names.get(group_id) != group_id
    ]

    def replace_text(value):
        result = value
        for pattern, label in replacements:
            result = pattern.sub(label, result)
        return result

    def walk(value, key=None):
        if isinstance(value, list):
            return [walk(item) for item in value]
        if isinstance(value, dict):
            return {item_key: walk(item, item_key) for item_key, item in value.items()}
        if isinstance(value, str) and key in {"s", "h"}:
            return replace_text(value)
        return value

    return walk(sections or [])


def _research_reading_minutes(sections):
    """用實際可見中文字數估計閱讀時間；只作 UI 導覽，不是研究統計量。"""
    def walk(value):
        if isinstance(value, str):
            return len(re.sub(r"https?://\S+", "", value))
        if isinstance(value, dict):
            return sum(walk(item) for item in value.values())
        if isinstance(value, (list, tuple)):
            return sum(walk(item) for item in value)
        return 0

    # 中文研究長文含表格與數字，採每分鐘約 500 字並向上取整；至少顯示 2 分鐘。
    return max(2, (walk(sections) + 499) // 500)


def _structured_runs_text(runs):
    """Flatten parser inline runs without rewording their research content."""
    return "".join(
        str(run.get("s") or "")
        for run in (runs or [])
        if isinstance(run, dict)
    ).strip()


def _reader_orientation_excerpt(value, limit=180):
    """Lift enough complete opening sentences to orient a reader without rewording."""
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if not text:
        return ""
    sentences = re.findall(r"[^。！？]*[。！？]", text)
    lifted = ""
    for sentence in sentences:
        lifted += sentence.strip()
        if len(lifted) >= 24:
            break
    if lifted:
        return lifted if len(lifted) <= limit else _article_excerpt(lifted, limit=limit)
    return _article_excerpt(text, limit=limit)


def _research_reading_mission(sections):
    """Reuse novice-section passages for the opening mission and closing check.

    This is presentation metadata only. The strings stay anchored to the existing
    ``三句話抓重點``, ``為什麼重要`` and ``想一想`` blocks, so the reader UI
    cannot introduce a new claim.
    """
    beginner = next((
        section for section in (sections or [])
        if section.get("h") == "新手先讀：這篇在講什麼"
    ), None)
    if not beginner:
        return None

    current_heading = ""
    orientation = ""
    question = ""
    key_points = []
    for item in beginner.get("blocks") or []:
        item_type = item.get("t")
        if item_type == "h3":
            current_heading = _structured_runs_text(item.get("runs"))
            continue
        if (current_heading == "三句話抓重點" and not key_points
                and item_type in {"ul", "ol"}):
            key_points = [
                _structured_runs_text(runs)
                for runs in (item.get("items") or [])
                if _structured_runs_text(runs)
            ][:3]
        elif current_heading == "為什麼重要" and not orientation and item_type == "p":
            orientation = _reader_orientation_excerpt(
                _structured_runs_text(item.get("runs"))
            )
        elif (current_heading == "想一想" and not question
              and item_type in {"ul", "ol"} and item.get("items")):
            question = _structured_runs_text(item["items"][0])

    if not orientation or not question:
        return None
    return {
        "orientation": orientation,
        "question": question,
        "keyPoints": key_points,
        "source": "本文既有的「三句話抓重點」、「為什麼重要」與「想一想」",
    }


def _section_list_points(sections, section_heading, block_heading=None):
    """Return an existing list from one named section without rewording it."""
    section = next((
        item for item in (sections or [])
        if item.get("h") == section_heading
    ), None)
    if not section:
        return []

    active_heading = block_heading is None
    for item in section.get("blocks") or []:
        if item.get("t") == "h3":
            active_heading = _structured_runs_text(item.get("runs")) == block_heading
            continue
        if active_heading and item.get("t") in {"ul", "ol"}:
            return [
                _structured_runs_text(runs)
                for runs in (item.get("items") or [])
                if _structured_runs_text(runs)
            ]
    return []


def _research_reader_boundary_brief(sections):
    """Lift a novice conclusion boundary from text already authored in the topic.

    The research summary deliberately keeps ledger-level wording.  The opening reader
    card instead reuses the same article's novice key points and first tracking action,
    so it can be easier to read without creating a second research claim.
    """
    key_points = _section_list_points(
        sections, "新手先讀：這篇在講什麼", "三句話抓重點",
    )
    next_steps = _section_list_points(
        sections, "新手先讀：這篇在講什麼", "接下來怎麼追",
    )
    if len(key_points) < 2 or not next_steps:
        return None
    return {
        "known": key_points[0],
        "unknown": key_points[-1],
        "next": next_steps[0],
        "source": "同篇既有的「三句話抓重點」與「接下來怎麼追」",
    }


def _research_article_reading_mission(article):
    """Build a type-aware opening task from text already present in the article."""
    sections = article.get("sections") or []
    beginner_mission = _research_reading_mission(sections)
    if beginner_mission:
        return beginner_mission

    article_type = article.get("type")
    subject = str(article.get("subject") or "本文").strip() or "本文"
    if article_type == "formal_note":
        points = _section_list_points(sections, "30 秒摘要")[:3]
        if not points:
            return None
        return {
            "orientation": points[0],
            "question": (
                f"讀完後，你能用自己的話說明「{subject}」的本業、收入來源，"
                "以及最容易誤讀的證據邊界嗎？"
            ),
            "keyPoints": points,
            "source": "本文既有的「30 秒摘要」",
            "sourceLabel": "30 秒摘要",
            "sourceSection": "30 秒摘要",
            "sourceHeading": "",
            "startLabel": "開始讀 30 秒摘要",
            "startHeading": "",
            "followup": "摘要之後，再確認本文的公司本業、收入來源與證據邊界。",
            "sourceBoundary": "這裡只重排原文，不新增主張或改寫結論。",
        }
    if article_type == "narrative":
        points = _section_list_points(
            sections, "多空觀點（小作文）", "勝負手",
        )[:3]
        if not points:
            return None
        return {
            "orientation": points[0],
            "question": (
                f"讀完後，你能分別說出「{subject}」的看多與看空論點各需要哪些證據，"
                "以及哪個勝負手會改變判斷嗎？"
            ),
            "keyPoints": points,
            "source": "本文既有的「多空觀點（小作文）」與「勝負手」",
            "sourceLabel": "勝負手",
            "sourceSection": "多空觀點（小作文）",
            "sourceHeading": "勝負手",
            "startLabel": "開始讀多空觀點",
            "startHeading": "",
            "followup": "先讀完看多與看空兩邊，再用勝負手檢查哪一邊正在獲得證據。",
            "sourceBoundary": "這裡只重排原文，不新增主張或改寫結論。",
        }
    return None


def _research_reading_mission_notations(article, mission, group_names=None):
    """Explain recurring research notation without changing the source sentence."""
    group_names = group_names or {}
    lead = next((
        str(point) for point in (mission.get("keyPoints") or []) if point
    ), str(mission.get("orientation") or ""))
    text = f"{lead} {mission.get('question') or ''}".strip()
    if not text:
        return []

    entries = []

    def unique_matches(pattern, flags=0):
        found = []
        for match in re.finditer(pattern, text, flags):
            token = match.group(1) if match.lastindex else match.group(0)
            if token not in found:
                found.append(token)
        return found

    def add(kind, position, tokens, label, definition, boundary):
        if tokens:
            entries.append({
                "kind": kind,
                "position": position,
                "tokens": tokens,
                "label": label,
                "definition": definition,
                "boundary": boundary,
            })

    source_refs = unique_matches(r"\[(S\d+)\]", re.IGNORECASE)
    if source_refs:
        add(
            "source_index", text.find(f"[{source_refs[0]}]"), source_refs,
            "、".join(source_refs) + "（來源編號）",
            "這些 S 編號指向本文來源索引，可在文末的來源與證據區對照原始文件。",
            "編號只用來定位來源，不代表證據強弱、重要性或排序。",
        )

    if article.get("type") == "narrative":
        hypothesis_ids = unique_matches(
            r"(?<![A-Za-z0-9])(H\d+)(?![A-Za-z0-9])", re.IGNORECASE,
        )
        if hypothesis_ids:
            match = re.search(
                r"(?<![A-Za-z0-9])H\d+(?![A-Za-z0-9])", text, re.IGNORECASE,
            )
            add(
                "hypothesis_id", match.start(), hypothesis_ids,
                "、".join(hypothesis_ids) + "（假說編號）",
                "H 編號是本文預先登錄、可由後續資料證明或否定的假說代號。",
                "這裡的 H 編號不是上、下半年，也不表示假說已獲證實。",
            )

    quarter_matches = list(re.finditer(
        r"(?<![A-Za-z0-9])((?:20\d{2})?Q[1-4])(?![A-Za-z0-9])",
        text, re.IGNORECASE,
    ))
    quarters = list(dict.fromkeys(match.group(1).upper() for match in quarter_matches))
    if quarters:
        add(
            "quarter", quarter_matches[0].start(), quarters,
            "、".join(quarters) + "（季度）",
            "Q1、Q2、Q3、Q4 分別表示一年的第一、第二、第三、第四季；前面的年份指出所屬年度。",
            "季度標記只說明期間，不代表營收或獲利必然成長。",
        )

    half_year_matches = list(re.finditer(
        r"(?<![A-Za-z0-9])(20\d{2}H[12])(?![A-Za-z0-9])",
        text, re.IGNORECASE,
    ))
    half_years = list(dict.fromkeys(match.group(1).upper() for match in half_year_matches))
    if half_years:
        add(
            "half_year", half_year_matches[0].start(), half_years,
            "、".join(half_years) + "（半年期間）",
            "年度後的 H1 表示上半年，H2 表示下半年。",
            "半年標記只說明期間；不要和本文的 H 編號假說混讀。",
        )

    mops_match = re.search(
        r"(?<![A-Za-z0-9])(MOPS)(?![A-Za-z0-9])", text, re.IGNORECASE,
    )
    if mops_match:
        add(
            "mops", mops_match.start(), [mops_match.group(1).upper()],
            "MOPS（公開資訊觀測站）",
            "台灣上市櫃公司公告月營收、財報與重大訊息的官方資訊平台。",
            "資料公布後仍要依本文指定的期間與門檻核對，不能只因公告出現就判定假說成立。",
        )

    taxonomy_ids = {
        "serverodm", "semiequip", "packtest", "ipdesign", "powersupply",
    }
    taxonomy_matches = list(re.finditer(
        r"(?<![A-Za-z0-9])(Universe|serverodm|semiequip|packtest|ipdesign|powersupply)"
        r"(?![A-Za-z0-9])",
        text, re.IGNORECASE,
    ))
    taxonomy_tokens = list(dict.fromkeys(match.group(1) for match in taxonomy_matches))
    if taxonomy_tokens:
        translations = []
        for token in taxonomy_tokens:
            token_key = token.lower()
            if token_key == "universe":
                translations.append(f"{token}＝研究中心追蹤範圍")
            elif token_key in taxonomy_ids:
                translations.append(f"{token}＝{group_names.get(token_key, token_key)}族群")
        add(
            "internal_taxonomy", taxonomy_matches[0].start(), taxonomy_tokens,
            "、".join(taxonomy_tokens) + "（研究分類）",
            "；".join(translations) + "。",
            "這些名稱只說明追蹤範圍或族群歸屬，不代表收入純度、受惠或投資排序。",
        )

    entries.sort(key=lambda item: (item["position"], item["kind"]))
    for entry in entries:
        entry.pop("position", None)
    return entries


def build_research_library(notes, reports, topics=None, stock_meta=None, group_names=None,
                           events=None, as_of=None, reader_terms=None):
    """建立獨立研究中心 payload；事件錨點歸入市場議題，不另造第四種閱讀模式。"""
    stock_meta = stock_meta or {}
    group_names = group_names or {}
    articles = []
    topic_by_article_id = {}
    type_order = {"formal_note": 0, "narrative": 1, "topic": 2}

    def stock_subject(stock_id):
        row = stock_meta.get(stock_id, {})
        name = row.get("name") or ""
        return " ".join(part for part in (stock_id, name) if part) or "未指定公司"

    def stock_groups(stock_ids, declared=None):
        result = [group for group in (declared or []) if group]
        result.extend(
            stock_meta.get(stock_id, {}).get("group")
            for stock_id in stock_ids
            if stock_meta.get(stock_id, {}).get("group")
        )
        return list(dict.fromkeys(result))

    def add(article):
        date = _article_date(article.get("date"))
        if date is None:
            return
        article["date"] = date.isoformat()
        article["groups"] = list(dict.fromkeys(article.get("groups") or []))
        article["groupLabels"] = [group_names.get(group, group) for group in article["groups"]]
        article["readingMinutes"] = _research_reading_minutes(article.get("sections") or [])
        reading_mission = _research_article_reading_mission(article)
        if reading_mission:
            notations = _research_reading_mission_notations(
                article, reading_mission, group_names,
            )
            if notations:
                reading_mission["readerNotations"] = notations
            article["readingMission"] = reading_mission
        elif article.get("type") in {"formal_note", "narrative"}:
            raise ValueError(
                f"發布文章缺少可逐字回查的新手閱讀任務來源：{article.get('id') or '未命名'}"
            )
        if article.get("type") == "topic":
            reader_boundary = _research_reader_boundary_brief(article.get("sections") or [])
            if reader_boundary:
                article["readerBoundaryBrief"] = reader_boundary
        article["searchText"] = " ".join(str(value) for value in (
            article.get("subject", ""), article.get("title", ""),
            article.get("summary", ""), " ".join(article["groupLabels"]),
            article.get("typeLabel", ""), article.get("status", ""),
        )).lower()
        articles.append(article)

    for stock_id, note in (notes or {}).items():
        if not _article_metadata_usable(note):
            continue
        verification = note_review_status(note)
        tone = ("verified" if verification == "independently_verified"
                else "warning" if verification == "conflicted" else "draft")
        subject = stock_subject(stock_id)
        sections = note.get("sections") or []
        add({
            "id": f"formal-{stock_id}", "type": "formal_note", "typeLabel": "正式筆記",
            "date": note.get("last_updated"), "stockIds": [stock_id],
            "subject": subject, "readerTitle": f"{subject} — 質化研究筆記",
            "title": _article_excerpt(note.get("summary")) or f"{subject} 質化研究筆記",
            "summary": _article_excerpt(note.get("summary")),
            "status": NOTE_LABEL.get(verification, verification), "statusTone": tone,
            "statusKey": "verified" if verification == "independently_verified" else "review",
            "groups": stock_groups([stock_id]), "sections": sections,
            "sources": note.get("sources") or [],
            "sourceUrl": NOTE_REPO_BLOB + note["relpath"],
            "meta": {
                "contentAsOf": note.get("content_as_of") or "-",
                "latestPeriod": note.get("latest_financial_period") or "-",
                "nextReview": note.get("next_review") or "-",
                "reviewedAt": note.get("reviewed_at") or "-",
                "reviewedBy": note.get("reviewed_by") or "-",
                "primarySources": note.get("primary_source_count", 0),
                "claimCount": note.get("claim_count", 0),
                "citedClaims": note.get("cited_claim_count", 0),
            },
        })

    for stock_id, report in (reports or {}).items():
        if not _article_metadata_usable(report) or not report.get("narrative"):
            continue
        subject = stock_subject(stock_id)
        hypothesis_titles = [
            item.get("title", "").strip() for item in report.get("hypotheses", [])
            if item.get("title", "").strip()
        ]
        title = "／".join(hypothesis_titles[:2]) or "看多、看空觀點與勝負手"
        sections = report.get("sections") or []
        add({
            "id": f"narrative-{stock_id}", "type": "narrative", "typeLabel": "多空小作文",
            "date": report.get("narrative", {}).get("updated"), "stockIds": [stock_id],
            "subject": subject, "readerTitle": f"{subject} — 領先假說報告",
            "title": title, "summary": "看多、看空兩篇對立敘事與可觀測勝負手。",
            "status": "觀察層・不等於事實認證", "statusTone": "observational",
            "statusKey": "observational", "groups": stock_groups([stock_id]),
            "sections": sections, "sources": [],
            "sourceUrl": NOTE_REPO_BLOB + report["relpath"],
            "meta": {
                "contentAsOf": report.get("content_as_of") or "-",
                "nextReview": report.get("next_review") or "-",
                "hypothesisCount": report.get("hypothesis_count", 0),
                "reportStatus": report.get("status") or "-",
            },
        })

    for topic in topics or []:
        if not _article_metadata_usable(topic):
            continue
        meta = topic.get("meta") or {}
        topic_date = (meta.get("last_reviewed_at")
                      if _article_date(meta.get("last_reviewed_at"))
                      else topic.get("captured_at"))
        stock_ids = topic.get("stock_ids") or []
        if stock_ids:
            subject = "、".join(stock_subject(stock_id) for stock_id in stock_ids)
        elif topic.get("group_ids"):
            subject = "跨族群：" + "、".join(
                group_names.get(group, group) for group in topic["group_ids"]
            )
        else:
            subject = "市場／政策"
        sections = topic.get("sections")
        if sections is None and topic.get("path") and os.path.exists(topic["path"]):
            with open(topic["path"], encoding="utf-8") as handle:
                sections = _extract_sections(handle.read())
        sections = _topic_structured_sections(topic, sections or [], group_names)
        sections = _reader_group_labels_in_sections(sections, group_names)
        article_id = (
            f"topic-{topic.get('topic_id') or os.path.basename(topic.get('relpath', 'topic'))}"
        )
        topic_by_article_id[article_id] = topic
        add({
            "id": article_id,
            "type": "topic", "typeLabel": "市場議題", "date": topic_date,
            "stockIds": stock_ids, "subject": subject,
            "readerTitle": topic.get("title") or "市場議題",
            "title": topic.get("title") or "市場議題",
            "summary": (_article_excerpt(topic.get("summary"))
                        or "跨公司研究線索與後續驗證路由。"),
            "status": "候選議題・不等於正式公司事實", "statusTone": "observational",
            "statusKey": "observational",
            "groups": stock_groups(stock_ids, topic.get("group_ids")),
            "sections": sections, "sources": topic.get("sources") or [],
            "confidence": dict(topic.get("confidence") or {}),
            "sourceUrl": NOTE_REPO_BLOB + topic["relpath"],
            "meta": {
                "capturedAt": topic.get("captured_at") or "-",
                "reviewDue": topic.get("review_due") or "-",
                "priority": topic.get("priority") or "-",
                "topicStatus": topic.get("status") or "-",
                "publisher": meta.get("publisher") or meta.get("publisher_domain") or "-",
                "canonicalUrl": meta.get("canonical_url") or "",
            },
        })

    for event in (events or {}).get("all", []):
        if not _article_metadata_usable(event):
            continue
        event_date = (event.get("content_as_of")
                      if _article_date(event.get("content_as_of"))
                      else event.get("event_date"))
        subject_key = event.get("subject") or ""
        stock_ids = ["2330"] if subject_key == "tsmc" else []
        subject = "2330 台積電" if subject_key == "tsmc" else subject_key or "跨市場事件"
        verification = event.get("verification") or "ai_draft"
        tone = ("verified" if verification == "independently_verified"
                else "warning" if verification == "conflicted" else "draft")
        guidance = event.get("guidance") or {}
        declared_groups = [group for group in GROUP_ORDER if group in guidance]
        kpis = [
            {"key": key, "label": label, "value": event.get("kpi", {}).get(key) or "—"}
            for key, label in EVENT_KPI_KEYS.items()
        ]
        add({
            "id": _event_research_id(event), "type": "topic", "typeLabel": "市場議題",
            "date": event_date, "stockIds": stock_ids, "subject": subject,
            "readerTitle": event.get("title") or "市場事件錨點",
            "title": event.get("title") or "市場事件錨點",
            "summary": "法說會事件脈絡、關鍵 KPI 與各族群方向指引。",
            "status": NOTE_LABEL.get(verification, verification), "statusTone": tone,
            "statusKey": "verified" if verification == "independently_verified" else "review",
            "groups": stock_groups(stock_ids, declared_groups),
            "sections": _reader_group_labels_in_sections(
                event.get("sections") or [], group_names,
            ), "sources": [],
            "sourceUrl": NOTE_REPO_BLOB + event["relpath"],
            "meta": {
                "eventKind": "tsmc_earnings" if subject_key == "tsmc" else "market_event",
                "fiscalQuarter": event.get("fiscal_quarter") or "-",
                "eventDate": event.get("event_date") or "-",
                "contentAsOf": event.get("content_as_of") or "-",
                "nextReview": event.get("next_review") or "-",
                "verification": verification,
                "kpis": kpis,
                "guidanceCount": len(declared_groups),
            },
        })

    article_anchor = max((item["date"] for item in articles), default=None)
    if isinstance(as_of, dt.datetime):
        passed_as_of = as_of.date()
    else:
        passed_as_of = as_of if isinstance(as_of, dt.date) else _article_date(as_of)
    as_of_candidates = [value for value in (
        _article_date(article_anchor), passed_as_of,
    ) if value is not None]
    library_as_of = max(as_of_candidates) if as_of_candidates else None
    if library_as_of:
        for article in articles:
            topic = topic_by_article_id.get(article["id"])
            if not topic:
                continue
            confidence = topic.get("confidence") or {}
            if confidence.get("declared") in {"high", "medium", "low"}:
                confidence = topic_confidence_at(
                    topic.get("meta") or {}, topic.get("last_evidence_at"), library_as_of)
            else:
                confidence = dict(confidence)
                confidence["as_of"] = library_as_of.isoformat()
            article["confidence"] = confidence
            article["searchText"] += " " + " ".join(str(value) for value in (
                confidence.get("declared_label", ""),
                confidence.get("effective_label", ""),
                "已到期" if confidence.get("stale") else "",
            )).strip().lower()

    articles.sort(key=lambda item: (
        -dt.date.fromisoformat(item["date"]).toordinal(),
        type_order[item["type"]], item["stockIds"][0] if item["stockIds"] else "",
        item["id"],
    ))
    counts = {key: 0 for key in type_order}
    group_counts = defaultdict(int)
    for article in articles:
        counts[article["type"]] += 1
        for group in article["groups"]:
            group_counts[group] += 1
    return {
        "anchor": article_anchor,
        "asOf": library_as_of.isoformat() if library_as_of else None,
        "total": len(articles),
        "counts": counts,
        "groups": [
            {"id": group, "label": group_names.get(group, group), "count": group_counts[group]}
            for group in group_names if group_counts[group]
        ],
        "readerTerms": [
            {**term, "aliases": list(term.get("aliases") or [])}
            for term in (reader_terms or [])
        ],
        "articles": articles,
    }


def attach_research_learning_paths(research_library, knowledge_graph):
    """Attach a novice-safe continuation path using only existing library links.

    The path is navigation, not a new research assertion: every route station uses
    the first existing articleId already registered on that graph, so the article
    station count stays identical to the graph-route count. Other article suggestions
    must share a named company or declared group, while graph suggestions must already
    cite the article or contain one of its companies on a visible graph relation.  When
    a shared company is the only bridge, the card must disclose that company and guide
    the reader through an edge that touches the same company node.
    """
    research_library = research_library or {"articles": []}
    articles = research_library.get("articles") or []
    graphs = (knowledge_graph or {}).get("graphs") or []
    routes = (knowledge_graph or {}).get("learningRoutes") or []
    article_by_id = {article.get("id"): article for article in articles if article.get("id")}
    graph_by_id = {graph.get("id"): graph for graph in graphs if graph.get("id")}

    def route_phase_map(route):
        """Map each registered station to one explicit, contiguous learning phase."""
        graph_ids = list(route.get("graphIds") or [])
        declared = route.get("phases")
        if not declared:
            # Legacy fixtures remain valid; published routes all declare phases.
            declared = [{
                "id": (route.get("id") or "route") + "-all",
                "label": route.get("label") or "學習路線",
                "graphIds": graph_ids,
            }]
        flattened = []
        phase_ids = set()
        mapped = {}
        total = len(declared)
        for phase_index, phase in enumerate(declared, 1):
            phase_id = str(phase.get("id") or "").strip()
            phase_label = str(phase.get("label") or "").strip()
            phase_graph_ids = list(phase.get("graphIds") or [])
            if not phase_id or not phase_label or not phase_graph_ids:
                raise ValueError(
                    f"學習路線階段缺少 id、label 或 graphIds：{route.get('id') or 'route'}"
                )
            if phase_id in phase_ids:
                raise ValueError(
                    f"學習路線階段 id 重複：{route.get('id') or 'route'} / {phase_id}"
                )
            phase_ids.add(phase_id)
            flattened.extend(phase_graph_ids)
            for station_index, graph_id in enumerate(phase_graph_ids, 1):
                if graph_id in mapped:
                    raise ValueError(
                        f"學習路線站點重複分組：{route.get('id') or 'route'} / {graph_id}"
                    )
                mapped[graph_id] = {
                    "phaseId": phase_id,
                    "phaseLabel": phase_label,
                    "phaseStep": phase_index,
                    "phaseTotal": total,
                    "phaseStationStep": station_index,
                    "phaseStationTotal": len(phase_graph_ids),
                }
        if flattened != graph_ids:
            raise ValueError(
                "學習路線階段必須逐站、依原順序完整覆蓋 graphIds："
                f"{route.get('id') or 'route'}"
            )
        return mapped

    phase_maps = {
        route.get("id") or "": route_phase_map(route)
        for route in routes
    }

    def graph_reader_handoff(graph, preferred_stock_ids=None):
        """Describe the exact graph projection opened from an article card.

        The frontend enters the company projection by default.  Counts and the
        guided relation therefore must use that same projection instead of the
        graph-wide node/edge totals, which combine company and industry views.
        Legacy test fixtures without an explicit view remain company-facing.
        """
        graph_edges = list(graph.get("edges") or [])
        company_edges = [
            edge for edge in graph_edges if edge.get("view") == "company"
        ]
        industry_edges = [
            edge for edge in graph_edges if edge.get("view") == "industry"
        ]
        if company_edges:
            view, view_label, visible_edges = "company", "公司曝險", company_edges
        elif industry_edges:
            view, view_label, visible_edges = "industry", "產業依賴", industry_edges
        else:
            view, view_label, visible_edges = "company", "公司曝險", graph_edges

        node_map = {
            node.get("id"): node for node in graph.get("nodes") or []
            if node.get("id")
        }
        visible_node_ids = {graph.get("rootNodeId")}
        for edge in visible_edges:
            visible_node_ids.update((edge.get("from"), edge.get("to")))
        visible_node_ids.discard(None)
        node_count = sum(node_id in node_map for node_id in visible_node_ids)

        preferred_stock_ids = set(preferred_stock_ids or [])
        preferred_node_ids = {
            node_id for node_id, node in node_map.items()
            if node.get("ticker") in preferred_stock_ids
        }
        guided_edges = visible_edges
        if preferred_stock_ids:
            guided_edges = [
                edge for edge in visible_edges
                if edge.get("from") in preferred_node_ids
                or edge.get("to") in preferred_node_ids
            ]
            if not guided_edges:
                raise ValueError(
                    "圖譜推薦的共同公司沒有出現在可見關係："
                    f"{graph.get('id') or 'unknown'} / "
                    + "、".join(sorted(preferred_stock_ids))
                )

        guided = next((
            edge for edge in guided_edges
            if edge.get("evidenceState") == "verified"
        ), guided_edges[0] if guided_edges else None)
        relation = None
        if guided:
            relation = {
                "edgeId": guided.get("id") or "",
                "fromLabel": (
                    (node_map.get(guided.get("from")) or {}).get("label")
                    or guided.get("from") or "未命名節點"
                ),
                "toLabel": (
                    (node_map.get(guided.get("to")) or {}).get("label")
                    or guided.get("to") or "未命名節點"
                ),
                "relationLabel": guided.get("relationLabel") or "已登錄關係",
                "evidenceLabel": guided.get("evidenceLabel") or "待確認",
                "commercialStageLabel": (
                    guided.get("commercialStageLabel") or "階段未標示"
                ),
                "boundary": guided.get("boundary") or "",
            }
        return {
            "graphView": view,
            "graphViewLabel": view_label,
            "nodeCount": node_count,
            "edgeCount": len(visible_edges),
            "guidedRelation": relation,
        }

    route_sequences = []
    routed_article_ids = set()
    for route in routes:
        sequence = []
        for graph_id in route.get("graphIds") or []:
            graph = graph_by_id.get(graph_id) or {}
            article_id = next((
                candidate for candidate in graph.get("articleIds") or []
                if candidate in article_by_id
            ), None)
            if not article_id:
                continue
            if article_id in routed_article_ids:
                raise ValueError(
                    f"學習路線主文章不可重複：{article_id}（graph {graph_id}）"
                )
            routed_article_ids.add(article_id)
            sequence.append({"graphId": graph_id, "articleId": article_id})
        if sequence:
            route_sequences.append((route, sequence))

    for route, sequence in route_sequences:
        total = len(sequence)
        phase_map = phase_maps.get(route.get("id") or "", {})
        for index, station in enumerate(sequence):
            phase = phase_map.get(station["graphId"], {})
            article_by_id[station["articleId"]]["learningRoute"] = {
                "id": route.get("id") or "",
                "label": route.get("label") or "學習路線",
                "description": route.get("description") or "",
                "step": index + 1,
                "total": total,
                "graphId": station["graphId"],
                "graphLabel": (graph_by_id.get(station["graphId"]) or {}).get("label") or "",
                **phase,
            }

    missing_reading_missions = sorted(
        article_id for article_id in routed_article_ids
        if not article_by_id[article_id].get("readingMission")
    )
    if missing_reading_missions:
        raise ValueError(
            "學習路線主文章缺少由新手段落產生的閱讀任務："
            + "、".join(missing_reading_missions)
        )
    missing_learning_checks = sorted(
        article_id for article_id in routed_article_ids
        if not (article_by_id[article_id].get("readingMission") or {}).get("keyPoints")
    )
    if missing_learning_checks:
        raise ValueError(
            "學習路線主文章缺少可逐字回查的三句重點："
            + "、".join(missing_learning_checks)
        )

    # 路線地圖只重排同一份 route graphIds 與各 graph 的第一篇既有文章。
    # question 逐字沿用該文章已通過契約的 readingMission，不另寫站點摘要。
    for route, sequence in route_sequences:
        route["stations"] = []
        phase_map = phase_maps.get(route.get("id") or "", {})
        for index, station in enumerate(sequence):
            graph = graph_by_id.get(station["graphId"]) or {}
            article = article_by_id[station["articleId"]]
            route["stations"].append({
                "step": index + 1,
                "graphId": station["graphId"],
                "graphLabel": graph.get("label") or "第 " + str(index + 1) + " 站",
                "articleId": article.get("id") or "",
                "articleTitle": (
                    article.get("readerTitle") or article.get("title") or "研究文章"
                ),
                "question": (article.get("readingMission") or {}).get("question") or "",
                "readingMinutes": article.get("readingMinutes") or 1,
                "groupLabels": list(article.get("groupLabels") or []),
                **phase_map.get(station["graphId"], {}),
            })

    def overlap(left, right):
        return set(left or []).intersection(right or [])

    group_label_by_id = {
        row.get("id"): row.get("label") or row.get("id")
        for row in (research_library.get("groups") or [])
        if row.get("id")
    }
    stock_label_by_id = {}
    for article in articles:
        if article.get("type") != "formal_note":
            continue
        stock_ids = list(article.get("stockIds") or [])
        subject = str(article.get("subject") or "").strip()
        if len(stock_ids) == 1 and subject:
            stock_label_by_id[stock_ids[0]] = subject

    def article_relation_basis(source, candidate):
        """Expose the exact existing tag that made a generic handoff eligible.

        A named company is more specific than a declared group, so prefer it when
        both exist.  This is navigation provenance, not a new supply-chain edge.
        """
        candidate_stocks = set(candidate.get("stockIds") or [])
        shared_stocks = [
            stock_id for stock_id in (source.get("stockIds") or [])
            if stock_id in candidate_stocks
        ]
        if shared_stocks:
            return {
                "kind": "stock",
                "ids": shared_stocks,
                "labels": [
                    stock_label_by_id.get(stock_id, stock_id)
                    for stock_id in shared_stocks
                ],
            }
        candidate_groups = set(candidate.get("groups") or [])
        shared_groups = [
            group_id for group_id in (source.get("groups") or [])
            if group_id in candidate_groups
        ]
        if shared_groups:
            return {
                "kind": "group",
                "ids": shared_groups,
                "labels": [
                    group_label_by_id.get(group_id, group_id)
                    for group_id in shared_groups
                ],
            }
        return None

    def article_comparison_question(source, candidate, relation_basis):
        """Give a generic article handoff one bounded question to compare.

        The prompt uses only the two article types and the already-proven shared
        company/group label.  It does not inspect prose or infer a new relation.
        """
        labels = [
            str(label).strip() for label in (relation_basis.get("labels") or [])
            if str(label).strip()
        ]
        if not labels:
            raise ValueError("一般文章推薦的比較問題缺少共同標記名稱")
        basis_kind = relation_basis.get("kind")
        anchor = labels[0]
        if len(labels) > 1:
            unit = "家公司" if basis_kind == "stock" else "個族群"
            anchor += f"等 {len(labels)} {unit}"

        source_type = source.get("type") or ""
        target_type = candidate.get("type") or ""
        if source_type == "formal_note" and target_type == "narrative":
            return (
                f"下一篇對「{anchor}」的多空說法，哪些能由本篇公司事實支持，"
                "哪些仍待驗證？"
            )
        if source_type == "formal_note" and target_type == "topic":
            if basis_kind == "stock":
                return (
                    f"下一篇把「{anchor}」放進什麼市場情境？"
                    "哪些內容仍不能當成公司事實？"
                )
            return (
                f"兩篇都談「{anchor}」；下一篇多了什麼市場情境？"
                "哪些內容仍不能套回本篇公司？"
            )
        if source_type == "narrative" and target_type == "formal_note":
            return (
                f"回到「{anchor}」的公司底稿，哪些事實能支持或限制本篇的多空說法？"
            )
        if source_type == "narrative" and target_type == "topic":
            if basis_kind == "stock":
                return (
                    f"下一篇為「{anchor}」補了哪些市場證據與待驗證問題？"
                    "是否改變本篇的多空假說？"
                )
            return (
                f"兩篇都談「{anchor}」；下一篇補了哪些產業機制與待驗證問題？"
            )
        if source_type == "topic" and target_type == "formal_note":
            return (
                f"回到「{anchor}」的公司底稿，哪些是已確認本業，"
                "哪些仍只是本篇的題材情境？"
            )
        return (
            f"兩篇都談「{anchor}」；它們各自回答什麼問題，證據邊界有何不同？"
        )

    def best_related(article, article_type, require_stock=False):
        matches = []
        for candidate in articles:
            if candidate.get("id") == article.get("id"):
                continue
            if candidate.get("type") != article_type:
                continue
            shared_stocks = overlap(article.get("stockIds"), candidate.get("stockIds"))
            shared_groups = overlap(article.get("groups"), candidate.get("groups"))
            if require_stock and not shared_stocks:
                continue
            if not shared_stocks and not shared_groups:
                continue
            matches.append((
                len(shared_stocks), len(shared_groups), candidate.get("date") or "",
                candidate.get("id") or "", candidate,
            ))
        matches.sort(key=lambda item: item[:4], reverse=True)
        return matches[0][-1] if matches else None

    def article_card(label, candidate, description, meta=None, source=None):
        card = {
            "kind": "article", "label": label,
            "title": candidate.get("readerTitle") or candidate.get("title") or "研究文章",
            "description": description,
            "meta": meta or (f"{candidate.get('typeLabel') or '研究文章'} · "
                             f"閱讀約 {candidate.get('readingMinutes') or 1} 分鐘"),
            "articleId": candidate.get("id") or "",
        }
        if source is not None:
            relation_basis = article_relation_basis(source, candidate)
            if not relation_basis:
                raise ValueError(
                    "一般文章推薦缺少共同公司或共同族群："
                    f"{source.get('id') or 'unknown'} → "
                    f"{candidate.get('id') or 'unknown'}"
                )
            card["relationBasis"] = relation_basis
            card["questionLabel"] = "讀下一篇時比較"
            card["question"] = article_comparison_question(
                source, candidate, relation_basis,
            )
        return card

    def next_route_article(article):
        article_id = article.get("id")
        for route, sequence in route_sequences:
            article_ids = [station["articleId"] for station in sequence]
            if article_id not in article_ids:
                continue
            index = article_ids.index(article_id)
            if index + 1 >= len(sequence):
                return None
            candidate = article_by_id[sequence[index + 1]["articleId"]]
            return route, candidate, index + 2, len(sequence)
        return None

    def matching_graph(article):
        stock_ids = set(article.get("stockIds") or [])
        ranked = []
        for graph in graphs:
            graph_articles = set(graph.get("articleIds") or [])
            graph_stocks = {
                node.get("ticker") for node in graph.get("nodes") or []
                if node.get("ticker")
            }
            direct = int(article.get("id") in graph_articles)
            shared_stock_ids = [
                stock_id for stock_id in (article.get("stockIds") or [])
                if stock_id in graph_stocks
            ]
            if not direct and not shared_stock_ids:
                continue
            if not direct:
                try:
                    graph_reader_handoff(graph, shared_stock_ids)
                except ValueError:
                    continue
            ranked.append((
                direct, len(shared_stock_ids), graph.get("id") or "",
                graph, shared_stock_ids,
            ))
        ranked.sort(key=lambda item: item[:3], reverse=True)
        if not ranked:
            return None
        direct, _, _, graph, shared_stock_ids = ranked[0]
        return {
            "graph": graph,
            "direct": bool(direct),
            "sharedStockIds": shared_stock_ids,
        }

    for article in articles:
        cards = []
        article_type = article.get("type")
        if article_type == "topic":
            route_next = next_route_article(article)
            route_context = article.get("learningRoute") or {}
            if route_next:
                route, candidate, step, total = route_next
                current_route = article.get("learningRoute") or {}
                candidate_route = candidate.get("learningRoute") or {}
                next_phase = candidate_route.get("phaseLabel") or ""
                phase_transition = ""
                if next_phase:
                    phase_transition = (
                        f"下一站仍在「{next_phase}」階段；"
                        if next_phase == current_route.get("phaseLabel")
                        else f"下一站進入「{next_phase}」階段；"
                    )
                next_card = article_card(
                    "沿學習路線往下讀", candidate,
                    phase_transition
                    + "這只是閱讀順序，不新增供應鏈或受惠關係。",
                    (f"{route.get('label') or '學習路線'}"
                     + (f" · {next_phase}" if next_phase else "")
                     + f" · 第 {step}/{total} 站 · "
                     f"閱讀約 {candidate.get('readingMinutes') or 1} 分鐘"),
                )
                next_card["routeStep"] = step
                next_card["routeTotal"] = total
                next_card["phaseLabel"] = next_phase
                next_card["phaseStep"] = candidate_route.get("phaseStep") or 0
                next_card["phaseTotal"] = candidate_route.get("phaseTotal") or 0
                route_bridge = {
                    "fromGraphLabel": current_route.get("graphLabel") or "",
                    "fromPhaseLabel": current_route.get("phaseLabel") or "",
                    "toGraphLabel": candidate_route.get("graphLabel") or "",
                    "toPhaseLabel": candidate_route.get("phaseLabel") or "",
                }
                if not all(route_bridge.values()):
                    raise ValueError(
                        "學習路線文章交接缺少 graph／phase label："
                        f"{article.get('id') or 'unknown'} → "
                        f"{candidate.get('id') or 'unknown'}"
                    )
                next_card["routeBridge"] = route_bridge
                next_card["question"] = (
                    (candidate.get("readingMission") or {}).get("question") or ""
                )
                cards.append(next_card)
            elif route_context and route_context.get("step") == route_context.get("total"):
                cards.append({
                    "kind": "route", "label": "已完成這條學習路線",
                    "title": route_context.get("label") or "學習路線",
                    "description": (
                        "你已讀到這條路線最後一站；回到知識圖譜可選下一條路線。"
                        "這只表示閱讀順序完成，不代表研究結論已完成。"
                    ),
                    "meta": (f"第 {route_context.get('step')}/{route_context.get('total')} 站 · "
                             f"共 {route_context.get('total')} 個主題"),
                    "graphId": route_context.get("graphId") or "",
                })
            formal = best_related(article, "formal_note", require_stock=True)
            if formal:
                cards.append(article_card(
                    "先認識公司", formal,
                    "先了解公司實際賣什麼、收入從哪裡來，再回頭判斷題材敘事。",
                    source=article,
                ))
            related_topic = None if route_next else best_related(article, "topic")
            if related_topic:
                cards.append(article_card(
                    "補一篇相關研究", related_topic,
                    "用同公司或同族群的另一篇研究，補上不同環節與待驗證問題。",
                    source=article,
                ))
        elif article_type == "formal_note":
            related_topic = best_related(article, "topic")
            if related_topic:
                cards.append(article_card(
                    "連到市場題材", related_topic,
                    "把公司本業放進近期題材，並保留題材尚未證實的邊界。",
                    source=article,
                ))
            narrative = best_related(article, "narrative", require_stock=True)
            if narrative:
                cards.append(article_card(
                    "比較正反說法", narrative,
                    "比較看多、看空與失效條件，練習分辨公司事實與研究假說。",
                    source=article,
                ))
        elif article_type == "narrative":
            formal = best_related(article, "formal_note", require_stock=True)
            if formal:
                cards.append(article_card(
                    "回到公司底稿", formal,
                    "先核對公司本業與收入來源，再判斷多空故事是否跨過證據邊界。",
                    source=article,
                ))
            related_topic = best_related(article, "topic")
            if related_topic:
                cards.append(article_card(
                    "補上市場脈絡", related_topic,
                    "用相關市場議題補上產業機制、外部證據與下一個查證節點。",
                    source=article,
                ))

        graph_match = matching_graph(article)
        if graph_match:
            graph = graph_match["graph"]
            preferred_stock_ids = (
                [] if graph_match["direct"] else graph_match["sharedStockIds"]
            )
            handoff = graph_reader_handoff(graph, preferred_stock_ids)
            graph_card = {
                "kind": "graph", "label": "看產業關聯",
                "title": graph.get("label") or "產業知識圖譜",
                "description": (
                    f"先用一條既有關係理解「{handoff['graphViewLabel']}」怎麼讀，"
                    "再進完整圖譜回查；關係線只代表證據層級，不是投資強弱。"
                ),
                "meta": (f"{handoff['graphViewLabel']} · "
                         f"{handoff['nodeCount']} 個節點 · "
                         f"{handoff['edgeCount']} 條關係"),
                "graphId": graph.get("id") or "",
                "graphView": handoff["graphView"],
                "graphViewLabel": handoff["graphViewLabel"],
                "guidedRelation": handoff["guidedRelation"],
            }
            if preferred_stock_ids:
                graph_card["relationBasis"] = {
                    "kind": "stock",
                    "ids": preferred_stock_ids,
                    "labels": [
                        stock_label_by_id.get(stock_id, stock_id)
                        for stock_id in preferred_stock_ids
                    ],
                }
            cards.append(graph_card)

        # A cross-market article can declare nearly the whole universe (for example
        # an event anchor with 11 guidance fields).  Turning that into one giant
        # "related group" filter teaches nothing, so only offer the shortcut when
        # the article actually narrows the reader to at most three groups.
        group_ids = list(article.get("groups") or [])
        if 0 < len(group_ids) <= 3:
            cards.append({
                "kind": "group", "label": "建立族群全貌",
                "title": "、".join(article.get("groupLabels") or group_ids),
                "description": "查看同族群的公司筆記與市場議題，分清公司角色和題材敘事。",
                "meta": f"{len(group_ids)} 個相關族群",
                "groupIds": group_ids,
            })

        if not cards:
            cards.append({
                "kind": "collection", "label": "先比較其他議題",
                "title": "市場議題資料庫",
                "description": (
                    "這篇尚未建立可驗證的公司或族群連結；先比較其他議題的"
                    "已知、未知與追蹤方式。"
                ),
                "meta": f"{(research_library.get('counts') or {}).get('topic', 0)} 篇市場議題",
                "articleType": "topic",
            })

        article["learningPath"] = {
            "title": "從這篇接著學",
            "description": (
                "以下只串起既有文章、族群與可追溯關係，不會把相似題材"
                "當成已證實的供應鏈。"
            ),
            "cards": cards[:3],
        }

    research_library["learningPathVersion"] = 91
    return research_library


def attach_group_learning_starts(research_library):
    """Give every maturity row a novice-safe entrance using existing routes only.

    This is editorial navigation, not a relevance or investment score.  Prefer a
    routed article whose declared primary group matches the row, then preserve the
    existing route order and station order.  A missing route stays explicit instead
    of silently promoting a latest or popular article.
    """
    research_library = research_library or {}
    maturity = research_library.get("groupMaturity") or {}
    rows = maturity.get("rows") or []
    articles = research_library.get("articles") or []
    routes = ((research_library.get("knowledgeGraph") or {}).get("learningRoutes")
              or [])
    route_order = {
        route.get("id"): index for index, route in enumerate(routes)
        if route.get("id")
    }
    article_counts = Counter(
        group_id
        for article in articles
        for group_id in article.get("groups") or []
        if group_id
    )
    groups_with_start = 0
    for row in rows:
        group_id = row.get("id") or ""
        candidates = [
            article for article in articles
            if group_id in (article.get("groups") or [])
            and article.get("learningRoute")
        ]
        candidates.sort(key=lambda article: (
            0 if (article.get("groups") or [""])[0] == group_id else 1,
            route_order.get((article.get("learningRoute") or {}).get("id"), 99),
            (article.get("learningRoute") or {}).get("step", 999),
            article.get("id") or "",
        ))
        row["articleCount"] = article_counts[group_id]
        if not candidates:
            row["learningStart"] = None
            continue
        article = candidates[0]
        route = article.get("learningRoute") or {}
        groups_with_start += 1
        row["learningStart"] = {
            "articleId": article.get("id") or "",
            "articleTitle": article.get("readerTitle") or article.get("title") or "研究文章",
            "routeId": route.get("id") or "",
            "routeLabel": route.get("label") or "學習路線",
            "graphId": route.get("graphId") or "",
            "graphLabel": route.get("graphLabel") or "",
            "step": route.get("step") or 0,
            "total": route.get("total") or 0,
            "phaseLabel": route.get("phaseLabel") or "",
            "phaseStep": route.get("phaseStep") or 0,
            "phaseTotal": route.get("phaseTotal") or 0,
            "scope": (
                "primary_group"
                if (article.get("groups") or [""])[0] == group_id
                else "cross_group"
            ),
        }
    row_labels = {
        row.get("id"): row.get("label") or row.get("id")
        for row in rows if row.get("id")
    }
    route_guides = []
    for route in routes:
        route_id = route.get("id") or ""
        stations = sorted(
            (
                article for article in articles
                if (article.get("learningRoute") or {}).get("id") == route_id
            ),
            key=lambda article: (
                (article.get("learningRoute") or {}).get("step", 999),
                article.get("id") or "",
            ),
        )
        if not stations:
            continue
        station_group_ids = {
            group_id
            for article in stations
            for group_id in article.get("groups") or []
            if group_id in row_labels
        }
        ordered_group_ids = [
            row.get("id") for row in rows
            if row.get("id") in station_group_ids
        ]
        first = stations[0]
        first_route = first.get("learningRoute") or {}
        route_guides.append({
            "id": route_id,
            "label": route.get("label") or "學習路線",
            "question": route.get("question") or "這條路線先回答什麼系統問題？",
            "description": route.get("description") or "",
            "firstArticleId": first.get("id") or "",
            "firstArticleTitle": (
                first.get("readerTitle") or first.get("title") or "研究文章"
            ),
            "firstGraphId": first_route.get("graphId") or "",
            "firstGraphLabel": first_route.get("graphLabel") or "第一站",
            "stationCount": len(stations),
            "groupIds": ordered_group_ids,
            "groupLabels": [row_labels[group_id] for group_id in ordered_group_ids],
        })
    maturity["learningRoutes"] = route_guides
    summary = maturity.setdefault("summary", {})
    summary["groupsWithLearningStart"] = groups_with_start
    maturity["learningBoundary"] = (
        "系統問題卡只沿用已登錄學習路線、第一站與主文章宣告的 group IDs，"
        "不會因文字相似新增跨族群關係。族群起讀文章優先使用把該族群列在第一位的文章，"
        "再沿用既有路線順序與站次；這不是熱門度、研究完整度或投資排序。"
    )
    return research_library


def build_group_maturity(notes, topics, stock_meta, group_names, knowledge_graph,
                         reviews, method_audit, as_of, candidate_radar=None,
                         group_guide=None):
    """Build an orthogonal group-research matrix without collapsing it to a score.

    Coverage, named-company linkage, evidence state, commercial materiality and
    maintenance are deliberately separate axes.  All values are full registry counts,
    not estimates from a sample.
    """
    if isinstance(as_of, dt.datetime):
        as_of = as_of.date()
    elif not isinstance(as_of, dt.date):
        as_of = _article_date(as_of) or research_today()
    date_text = as_of.isoformat()
    notes = notes or {}
    topics = topics or []
    stock_meta = stock_meta or {}
    group_names = group_names or {}
    knowledge_graph = knowledge_graph or {"graphs": []}
    reviews = reviews or []
    method_audit = method_audit or {}
    candidate_radar = candidate_radar or {"candidates": []}
    group_guide = group_guide or {}

    group_ids = list(group_names)
    for row in stock_meta.values():
        group_id = row.get("group")
        if group_id and group_id not in group_ids:
            group_ids.append(group_id)
    universe_ids = defaultdict(set)
    for stock_id, row in stock_meta.items():
        if row.get("group"):
            universe_ids[row["group"]].add(stock_id)

    note_available = defaultdict(set)
    note_verified = defaultdict(set)
    for stock_id, note in notes.items():
        group_id = (stock_meta.get(stock_id) or {}).get("group")
        if not group_id or not _article_metadata_usable(note):
            continue
        note_available[group_id].add(stock_id)
        if note_review_status(note) == "independently_verified":
            note_verified[group_id].add(stock_id)

    def mapped_groups(topic):
        result = [group for group in topic.get("group_ids", []) if group]
        result.extend(
            (stock_meta.get(stock_id) or {}).get("group")
            for stock_id in topic.get("stock_ids", [])
        )
        return list(dict.fromkeys(group for group in result if group))

    active_topics = [
        topic for topic in topics
        if topic.get("status") not in {"dismissed", "resolved"}
    ]
    topics_by_group = defaultdict(list)
    unrouted_topics = []
    for topic in active_topics:
        groups = mapped_groups(topic)
        if not groups:
            unrouted_topics.append(topic)
        for group_id in groups:
            topics_by_group[group_id].append(topic)

    missing_source_topics = set(
        (method_audit.get("sources") or {}).get(
            "thesesNeedingSecondIndependentGroup", []
        )
    )
    review_pairs = defaultdict(list)
    for row in reviews:
        review_pairs[(row.get("topic_id"), row.get("monitor_id"))].append(row)
    effective_due = effective_monitor_schedule(topics, reviews)

    company_any = defaultdict(set)
    company_by_materiality = defaultdict(lambda: defaultdict(set))
    company_by_evidence = defaultdict(lambda: defaultdict(set))
    edge_counts = defaultdict(lambda: defaultdict(int))
    company_routes = defaultdict(list)
    materiality_rank = {"financial": 3, "named_product": 2, "adjacent": 1,
                        "unknown": 0}
    evidence_rank = {"verified": 2, "inference": 1, "unverified": 0}
    financial_assessment_ids = defaultdict(set)
    financial_companies = defaultdict(set)
    financial_by_attribution = defaultdict(Counter)
    financial_by_scope = defaultdict(Counter)
    financial_routes = defaultdict(list)
    for graph in knowledge_graph.get("graphs", []):
        nodes = {node.get("id"): node for node in graph.get("nodes", [])}
        graph_edges = {edge.get("id"): edge for edge in graph.get("edges", [])}
        for edge in graph.get("edges", []):
            if edge.get("status") != "active" or edge.get("view") != "company":
                continue
            edge_key = f"{graph.get('id')}:{edge.get('id')}"
            companies = []
            for node_id in (edge.get("from"), edge.get("to")):
                node = nodes.get(node_id) or {}
                if node.get("type") == "company" and node.get("universe"):
                    companies.append(node)
            for node in companies:
                stock_id = node.get("ticker") or node.get("id", "").split(":")[-1]
                group_id = (node.get("groupId")
                            or (stock_meta.get(stock_id) or {}).get("group"))
                if not group_id:
                    continue
                company_any[group_id].add(stock_id)
                company_by_materiality[group_id][
                    edge.get("materiality") or "unknown"
                ].add(stock_id)
                company_by_evidence[group_id][
                    edge.get("evidenceState") or "unverified"
                ].add(stock_id)
                edge_counts[group_id][edge_key] += 1
                company_name = (node.get("label")
                                or (stock_meta.get(stock_id) or {}).get("name")
                                or "")
                company_routes[group_id].append({
                    "stockId": stock_id,
                    "companyName": company_name,
                    "companyLabel": f"{stock_id} {company_name}".strip(),
                    "formalArticleId": (
                        f"formal-{stock_id}"
                        if stock_id in note_available[group_id] else ""
                    ),
                    "formalVerified": stock_id in note_verified[group_id],
                    "graphId": graph.get("id") or "",
                    "graphLabel": graph.get("label") or "",
                    "edgeId": edge.get("id") or "",
                    "articleIds": list(edge.get("articleIds") or []),
                    "relationLabel": (
                        edge.get("relationLabel") or edge.get("relation") or ""
                    ),
                    "materiality": edge.get("materiality") or "unknown",
                    "materialityLabel": (
                        edge.get("materialityLabel") or edge.get("materiality") or ""
                    ),
                    "evidenceState": edge.get("evidenceState") or "unverified",
                    "evidenceLabel": (
                        edge.get("evidenceLabel") or edge.get("evidenceState") or ""
                    ),
                    "commercialStage": edge.get("commercialStage") or "",
                    "commercialStageLabel": (
                        edge.get("commercialStageLabel")
                        or edge.get("commercialStage") or ""
                    ),
                    "reviewDue": edge.get("reviewDue") or "",
                })
        for assessment in graph.get("financialAssessments", []):
            if assessment.get("status") != "active":
                continue
            edge = graph_edges.get(assessment.get("edgeId")) or {}
            for node_id in (edge.get("from"), edge.get("to")):
                node = nodes.get(node_id) or {}
                if node.get("type") != "company" or not node.get("universe"):
                    continue
                stock_id = node.get("ticker") or node.get("id", "").split(":")[-1]
                group_id = (node.get("groupId")
                            or (stock_meta.get(stock_id) or {}).get("group"))
                if not group_id:
                    continue
                assessment_id = assessment.get("id") or ""
                if assessment_id in financial_assessment_ids[group_id]:
                    continue
                financial_assessment_ids[group_id].add(assessment_id)
                financial_companies[group_id].add(stock_id)
                financial_by_attribution[group_id][
                    assessment.get("attributionStatus") or "not_disclosed"
                ] += 1
                financial_by_scope[group_id][
                    assessment.get("financialScope") or "company_total"
                ] += 1
                financial_routes[group_id].append({
                    "assessmentId": assessment_id,
                    "stockId": stock_id,
                    "graphId": graph.get("id") or "",
                    "edgeId": edge.get("id") or "",
                    "articleIds": list(edge.get("articleIds") or []),
                    "attributionStatus": assessment.get("attributionStatus") or "",
                    "financialScope": assessment.get("financialScope") or "",
                    "reviewDue": assessment.get("reviewDue") or "",
                    "boundary": assessment.get("boundary") or "",
                    "nextTrigger": assessment.get("nextTrigger") or "",
                })

    def reader_company_evidence(group_id):
        """Choose one deterministic, traceable starting relation per company.

        This is a reader route, not a company or evidence ranking.  Every active
        relation remains available in the graph; the matrix only needs one stable
        doorway for each already-counted universe company.
        """
        by_company = defaultdict(list)
        for route in company_routes[group_id]:
            by_company[route["stockId"]].append(route)

        def route_key(route):
            review_due = route.get("reviewDue") or ""
            stale = bool(
                re.fullmatch(r"\d{4}-\d{2}-\d{2}", review_due)
                and review_due < date_text
            )
            return (
                stale,
                -materiality_rank.get(route.get("materiality"), -1),
                -evidence_rank.get(route.get("evidenceState"), -1),
                route.get("graphId") or "",
                route.get("edgeId") or "",
            )

        result = []
        for stock_id in sorted(by_company):
            routes = sorted(by_company[stock_id], key=route_key)
            route = dict(routes[0])
            route["routeCount"] = len(routes)
            result.append(route)
        return result

    reviewed_stale_ids = set()
    unique_due_pairs = set()
    for topic in active_topics:
        topic_id = topic.get("topic_id") or (topic.get("meta") or {}).get("topic_id")
        due_pairs = []
        has_review_after_topic_due = False
        for monitor in topic.get("monitoring", []):
            if monitor.get("status") != "active":
                continue
            pair = (topic_id, monitor.get("monitor_id"))
            due = effective_due.get(pair, monitor.get("next_check", ""))
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", due or "") and due <= date_text:
                due_pairs.append(pair)
                unique_due_pairs.add(pair)
            for row in review_pairs.get(pair, []):
                if row.get("checked_at", "") >= (topic.get("review_due") or ""):
                    has_review_after_topic_due = True
        if ((topic.get("confidence") or {}).get("stale")
                and has_review_after_topic_due and not due_pairs):
            reviewed_stale_ids.add(topic_id)

    rows = []
    for group_id in group_ids:
        universe = universe_ids[group_id]
        group_topics = topics_by_group[group_id]
        topic_ids = {
            topic.get("topic_id") or (topic.get("meta") or {}).get("topic_id")
            for topic in group_topics
        }
        stale_topics = {
            topic.get("topic_id") or (topic.get("meta") or {}).get("topic_id")
            for topic in group_topics if (topic.get("confidence") or {}).get("stale")
        }
        due_pairs = set()
        for topic in group_topics:
            topic_id = topic.get("topic_id") or (topic.get("meta") or {}).get("topic_id")
            for monitor in topic.get("monitoring", []):
                if monitor.get("status") != "active":
                    continue
                pair = (topic_id, monitor.get("monitor_id"))
                due = effective_due.get(pair, monitor.get("next_check", ""))
                if re.fullmatch(r"\d{4}-\d{2}-\d{2}", due or "") and due <= date_text:
                    due_pairs.add(pair)

        materiality = {
            key: len(company_by_materiality[group_id][key])
            for key in ("financial", "named_product", "adjacent", "unknown")
        }
        evidence = {
            key: len(company_by_evidence[group_id][key])
            for key in ("verified", "inference", "unverified")
        }
        financial = {
            "assessments": len(financial_assessment_ids[group_id]),
            "companies": len(financial_companies[group_id]),
            "attribution": {
                key: financial_by_attribution[group_id][key]
                for key in ("direct", "bounded_proxy", "not_disclosed")
            },
            "scopes": {
                key: financial_by_scope[group_id][key]
                for key in ("company_total", "segment", "product", "unit_economics")
            },
        }
        deepest = (
            "financial" if materiality["financial"]
            else "named_product" if materiality["named_product"]
            else "adjacent" if materiality["adjacent"]
            else "unknown"
        )
        verified_notes = len(note_verified[group_id])
        source_gaps = len(topic_ids.intersection(missing_source_topics))
        bridge_count = len(company_any[group_id])
        company_evidence = reader_company_evidence(group_id)
        if verified_notes < len(universe):
            action, tone = "補正式公司筆記", "critical"
            reason = f"尚缺 {len(universe) - verified_notes} 檔獨立核驗筆記"
        elif due_pairs:
            action, tone = "先完成到期查證", "critical"
            reason = f"仍有 {len(due_pairs)} 個追蹤項目已到期"
        elif bridge_count == 0:
            action, tone = "補上具名公司證據", "critical"
            reason = "已有公司筆記，但尚未把題材連到具名公司證據"
        elif source_gaps:
            action, tone = "補第二條來源鏈", "warning"
            reason = f"有 {source_gaps} 篇主命題仍只有一個獨立來源群組"
        elif financial["attribution"]["direct"] == 0 and financial["assessments"]:
            action, tone = "等待可拆分的題材財務資料", "progress"
            reason = (
                f"已完成 {financial['assessments']} 筆財務檢查，但尚無法直接拆出題材貢獻"
            )
        elif financial["attribution"]["direct"] == 0:
            action, tone = "補上題材財務影響", "warning"
            reason = "已有具名公司證據，但尚未檢查題材對收入或獲利的實際影響"
        else:
            action, tone = "持續追蹤", "progress"
            reason = "公司覆蓋、交叉驗證與可直接辨識的財務影響都有可追溯證據"

        reader_guide = group_guide.get(group_id) or {}
        rows.append({
            "id": group_id,
            "label": group_names.get(group_id, group_id),
            "readerRole": reader_guide.get("readerRole", ""),
            "readerBoundary": reader_guide.get("readerBoundary", ""),
            "universe": len(universe),
            "formalNotes": len(note_available[group_id]),
            "verifiedNotes": verified_notes,
            "topics": len(topic_ids),
            "companyBridges": bridge_count,
            "companyEvidence": company_evidence,
            "materiality": materiality,
            "deepestMateriality": deepest,
            "financialMateriality": financial,
            "evidence": evidence,
            "activeCompanyEdges": len(edge_counts[group_id]),
            "staleTopics": len(stale_topics),
            "reviewedStaleTopics": len(stale_topics.intersection(reviewed_stale_ids)),
            "dueMonitors": len(due_pairs),
            "sourceGaps": source_gaps,
            "action": action,
            "actionTone": tone,
            "actionReason": reason,
        })

    all_stale_ids = {
        topic.get("topic_id") or (topic.get("meta") or {}).get("topic_id")
        for topic in active_topics if (topic.get("confidence") or {}).get("stale")
    }
    topic_by_id = {
        topic.get("topic_id") or (topic.get("meta") or {}).get("topic_id"): topic
        for topic in active_topics
    }
    candidates = {
        candidate.get("id"): candidate
        for candidate in candidate_radar.get("candidates", [])
        if candidate.get("id")
    }
    bridge_candidate_ids = {
        "power": "RC-SIC-AI-POWER-QUALIFICATION",
        "material": "RC-224G-PCB-MATERIAL-QUALIFICATION",
    }

    def topic_title(topic):
        return topic.get("title") or (topic.get("meta") or {}).get("title") or (
            topic.get("topic_id") or (topic.get("meta") or {}).get("topic_id") or "研究議題"
        )

    def topic_next_check(topic):
        topic_id = topic.get("topic_id") or (topic.get("meta") or {}).get("topic_id")
        values = []
        for monitor in topic.get("monitoring", []):
            if monitor.get("status") != "active":
                continue
            due = effective_due.get(
                (topic_id, monitor.get("monitor_id")), monitor.get("next_check", ""))
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", due or ""):
                values.append(due)
        return min(values) if values else ""

    def topic_next_evidence(topic):
        active = [
            monitor for monitor in topic.get("monitoring", [])
            if monitor.get("status") == "active"
        ]
        if not active:
            return "取得能直接支持或否定主命題的第二條獨立一手來源。"
        active.sort(key=lambda monitor: (
            effective_due.get(
                (topic.get("topic_id") or (topic.get("meta") or {}).get("topic_id"),
                 monitor.get("monitor_id")),
                monitor.get("next_check", "9999-12-31")),
            monitor.get("monitor_id", ""),
        ))
        monitor = active[0]
        return monitor.get("trigger") or monitor.get("metric") or (
            "取得能直接支持或否定主命題的新一手文件。")

    def group_payload(group_values):
        return [
            {"id": group_id, "label": group_names.get(group_id, group_id)}
            for group_id in dict.fromkeys(group_values) if group_id
        ]

    actions = []
    action_ids = set()

    def add_action(item):
        if not item.get("id") or item["id"] in action_ids:
            return
        action_ids.add(item["id"])
        item.setdefault("articleId", "")
        item.setdefault("graphId", "")
        item.setdefault("candidateId", "")
        item.setdefault("companyIds", [])
        item.setdefault("nextCheck", "")
        item.setdefault("status", "open")
        item.setdefault("statusLabel", "待處理")
        item.setdefault("tone", "warning")
        actions.append(item)

    # Formal-note gaps are one root task per group, not one repeated table cell.
    for row in rows:
        missing = row["universe"] - row["verifiedNotes"]
        if missing <= 0:
            continue
        group_id = row["id"]
        add_action({
            "id": f"formal-note:{group_id}",
            "category": "formal_note",
            "categoryLabel": "正式筆記覆蓋",
            "priorityRank": 0,
            "priorityLabel": "P0",
            "title": f"補齊{row['label']}的 {missing} 檔獨立核驗公司筆記",
            "affectedGroups": group_payload([group_id]),
            "boundary": "只計已完成獨立核驗的正式公司筆記；篇數不足不能用題材文章替代。",
            "nextEvidence": "取得年報、季報與法說等核心一手文件，完成數字重算與第二人核對後逐篇簽核。",
            "tone": "critical",
        })

    # A monitor is keyed by topic+monitor.  A topic mapped to five groups still appears once.
    for topic in active_topics:
        topic_id = topic.get("topic_id") or (topic.get("meta") or {}).get("topic_id")
        groups = mapped_groups(topic)
        for monitor in topic.get("monitoring", []):
            if monitor.get("status") != "active":
                continue
            monitor_id = monitor.get("monitor_id") or "monitor"
            due = effective_due.get((topic_id, monitor_id), monitor.get("next_check", ""))
            if not (re.fullmatch(r"\d{4}-\d{2}-\d{2}", due or "") and due <= date_text):
                continue
            add_action({
                "id": f"monitor:{topic_id}:{monitor_id}",
                "category": "due_monitor",
                "categoryLabel": "到期查證",
                "priorityRank": 0,
                "priorityLabel": "P0",
                "title": f"{topic_title(topic)} · 到期查證",
                "affectedGroups": group_payload(groups),
                "articleId": f"topic-{topic_id}",
                "boundary": monitor.get("metric") or "只依文章預先寫下的檢驗標準判斷，不因市場說法改變就延長有效期限。",
                "nextEvidence": monitor.get("trigger") or monitor.get("metric") or "完成一手來源查證並記錄結果。",
                "nextCheck": due,
                "tone": "critical",
                "statusLabel": "已到期",
            })

    # Independent-source gaps are root-deduplicated by thesis topic ID.
    for topic_id in sorted(missing_source_topics):
        topic = topic_by_id.get(topic_id)
        if not topic:
            continue
        groups = mapped_groups(topic)
        add_action({
            "id": f"source-gap:{topic_id}",
            "category": "source_gap",
            "categoryLabel": "獨立來源鏈",
            "priorityRank": 1,
            "priorityLabel": "P1",
            "title": f"{topic_title(topic)} · 補第二條獨立來源鏈",
            "affectedGroups": group_payload(groups),
            "articleId": f"topic-{topic_id}",
            "boundary": f"同一個主結論目前影響 {len(groups)} 個族群，但缺口只有一個；不按族群重複計成 {len(groups)} 件。",
            "nextEvidence": topic_next_evidence(topic),
            "nextCheck": topic_next_check(topic),
            "tone": "warning",
        })

    # A group without a company edge gets one bridge task.  Power/material reuse the
    # frozen radar candidate so the queue points to the exact pre-registered rejection rule.
    for row in rows:
        if row["verifiedNotes"] < row["universe"] or row["companyBridges"]:
            continue
        group_id = row["id"]
        candidate = candidates.get(bridge_candidate_ids.get(group_id, ""), {})
        add_action({
            "id": f"company-bridge:{group_id}",
            "category": "company_bridge",
            "categoryLabel": "具名公司證據",
            "priorityRank": 2,
            "priorityLabel": "P1",
            "title": candidate.get("title") or f"為{row['label']}補上第一條具名公司證據",
            "affectedGroups": group_payload([group_id]),
            "candidateId": candidate.get("id", ""),
            "articleId": candidate.get("articleId", ""),
            "graphId": candidate.get("graphId", ""),
            "boundary": "公司筆記已存在，但研究中心尚未找到可把題材連到具名公司的直接證據；0 不表示產業關係不存在。",
            "nextEvidence": candidate.get("nextEvidence") or "從公司一手文件找出具名產品或製程角色，並寫清楚適用範圍與下一個查證條件。",
            "nextCheck": candidate.get("nextCheck", ""),
            "tone": "critical",
        })

    # Once a bridge exists, push the same named company/product to a verifiable financial
    # denominator.  A completed bounded/not-disclosed assessment becomes a watch rather
    # than remaining an open research task; only direct attribution closes the gap.
    for row in rows:
        group_id = row["id"]
        financial = row["financialMateriality"]
        if not row["companyBridges"] or financial["attribution"]["direct"]:
            continue
        assessed_routes = sorted(financial_routes[group_id], key=lambda route: (
            {"direct": 0, "bounded_proxy": 1, "not_disclosed": 2}.get(
                route["attributionStatus"], 9),
            route["reviewDue"] or "9999-12-31", route["stockId"], route["assessmentId"],
        ))
        if assessed_routes:
            route = assessed_routes[0]
            stock_ids = sorted(financial_companies[group_id])
            attribution = financial["attribution"]
            scopes = financial["scopes"]
            scope_text = "、".join(
                f"{({'company_total': '公司整體', 'segment': '事業部', 'product': '產品', 'unit_economics': '單位經濟'}.get(key, key))} {value}"
                for key, value in scopes.items() if value
            )
            add_action({
                "id": f"financial-watch:{group_id}",
                "category": "financial_materiality_watch",
                "categoryLabel": "題材財務影響",
                "priorityRank": 4,
                "priorityLabel": "WATCH",
                "title": f"{row['label']}已有財務資料，但還無法拆出題材貢獻",
                "affectedGroups": group_payload([group_id]),
                "companyIds": stock_ids,
                "articleId": (route.get("articleIds") or [""])[0],
                "graphId": route.get("graphId", ""),
                "boundary": (
                    f"全數盤點已有 {financial['assessments']} 筆財務檢查（{scope_text or '—'}）；"
                    f"可直接辨識 {attribution['direct']} 筆、只能當參考 {attribution['bounded_proxy']} 筆、"
                    f"題材金額未揭露 {attribution['not_disclosed']} 筆。參考值不能改寫為題材收入。"
                ),
                "nextEvidence": route.get("nextTrigger") or "取得同期間、同合併分母的題材收入或毛利揭露。",
                "nextCheck": route.get("reviewDue", ""),
                "status": "watch",
                "statusLabel": "等待可拆分資料",
                "tone": "progress",
            })
            continue
        routes = sorted(company_routes[group_id], key=lambda route: (
            -materiality_rank.get(route["materiality"], -1),
            -evidence_rank.get(route["evidenceState"], -1),
            route["graphId"], route["stockId"],
        ))
        route = routes[0] if routes else {}
        stock_ids = sorted(company_any[group_id])
        names = [
            f"{stock_id} {(stock_meta.get(stock_id) or {}).get('name', '')}".strip()
            for stock_id in stock_ids
        ]
        add_action({
            "id": f"financial:{group_id}",
            "category": "financial_materiality",
            "categoryLabel": "題材財務影響",
            "priorityRank": 3,
            "priorityLabel": "P2",
            "title": f"檢查{row['label']}題材對收入或獲利的實際影響",
            "affectedGroups": group_payload([group_id]),
            "companyIds": stock_ids,
            "articleId": (route.get("articleIds") or [""])[0],
            "graphId": route.get("graphId", ""),
            "candidateId": (
                bridge_candidate_ids.get(group_id, "")
                if bridge_candidate_ids.get(group_id, "") in candidates else ""
            ),
            "boundary": f"目前具名公司為{'、'.join(names) or '—'}；尚未用一致期間與口徑，檢查題材金額占公司收入或獲利多少。",
            "nextEvidence": "先確認同期間的公司總收入，再找同一具名產品或角色的收入、毛利、現金流，或可重算的出貨量乘單價。只有公司總額時，不能宣稱為題材收入。",
            "nextCheck": route.get("reviewDue", ""),
            "tone": "warning",
        })

    # Unrouted policy watches are explicit non-errors: they wait for a transmission
    # mechanism before mapping to groups, instead of being labelled as a generic routing gap.
    for topic in unrouted_topics:
        topic_id = topic.get("topic_id") or (topic.get("meta") or {}).get("topic_id")
        add_action({
            "id": f"policy-watch:{topic_id}",
            "category": "policy_watch",
            "categoryLabel": "政策觀察（暫不路由）",
            "priorityRank": 4,
            "priorityLabel": "WATCH",
            "title": topic_title(topic),
            "affectedGroups": [],
            "articleId": f"topic-{topic_id}",
            "boundary": "尚未連到族群是刻意保留的限制；在條文、適用範圍與產業傳導可確認前，不把政策事件硬套進族群。",
            "nextEvidence": topic_next_evidence(topic),
            "nextCheck": topic_next_check(topic),
            "status": "watch",
            "statusLabel": "等待傳導證據",
            "tone": "progress",
        })

    actions.sort(key=lambda item: (
        item.get("priorityRank", 99), item.get("nextCheck") or "9999-12-31",
        item.get("title", ""), item.get("id", ""),
    ))
    action_order = {item["id"]: index for index, item in enumerate(actions)}
    actions_by_group = defaultdict(list)
    for item in actions:
        for group in item.get("affectedGroups", []):
            actions_by_group[group["id"]].append(item["id"])
    for row in rows:
        row["actionIds"] = sorted(
            actions_by_group[row["id"]], key=lambda action_id: action_order[action_id])

    return {
        "asOf": date_text,
        "summary": {
            "groups": len(rows),
            "universe": sum(len(value) for value in universe_ids.values()),
            "verifiedNotes": sum(len(value) for value in note_verified.values()),
            "groupsWithoutTopics": sum(row["topics"] == 0 for row in rows),
            "groupsWithoutCompanyBridge": sum(row["companyBridges"] == 0 for row in rows),
            "groupsWithFinancialMateriality": sum(
                row["financialMateriality"]["attribution"]["direct"] > 0 for row in rows
            ),
            "groupsWithFinancialAssessment": sum(
                row["financialMateriality"]["assessments"] > 0 for row in rows
            ),
            "groupsWithDirectFinancialAttribution": sum(
                row["financialMateriality"]["attribution"]["direct"] > 0 for row in rows
            ),
            "financialAssessments": sum(
                row["financialMateriality"]["assessments"] for row in rows
            ),
            "dueMonitors": len(unique_due_pairs),
            "staleTopics": len(all_stale_ids),
            "reviewedStaleTopics": len(all_stale_ids.intersection(reviewed_stale_ids)),
            "sourceGapTopics": len(missing_source_topics),
            "unroutedTopics": len(unrouted_topics),
            "rootActions": len(actions),
            "openActions": sum(item["status"] == "open" for item in actions),
            "watchActions": sum(item["status"] == "watch" for item in actions),
            "financialAssessmentWatches": sum(
                item["category"] == "financial_materiality_watch" for item in actions
            ),
            "policyWatchTopics": sum(item["category"] == "policy_watch" for item in actions),
        },
        "rows": rows,
        "actionQueue": actions,
        "materialityLabels": {
            "unknown": "未建立具名公司橋接",
            "adjacent": "相鄰／搜尋路由",
            "named_product": "具名產品或角色",
            "financial": "題材財務可直接歸因",
        },
        "financialScopeLabels": {
            "company_total": "公司總額",
            "segment": "事業部",
            "product": "產品類別",
            "unit_economics": "單位經濟",
        },
        "financialAttributionLabels": {
            "direct": "可直接歸因",
            "bounded_proxy": "有界代理",
            "not_disclosed": "題材分子未揭露",
        },
        "boundary": (
            "這是 11 個族群、121 檔股票與目前全部研究資料的完整盤點，不是抽樣；"
            "公司筆記、題材文章、具名公司證據、財務影響與更新時效分開顯示，刻意不合成分數。"
            "財務檢查會區分公司整體、事業部、產品與單位經濟；只有參考值或未揭露題材金額時，"
            "不能把它改寫成題材收入。"
            "待辦按共同缺口去重：同一議題即使影響多個族群也只算一件；"
            "0 代表研究中心尚未建立可追溯證據，不代表產業關係不存在。"
        ),
    }


def main():
    # 唯讀開啟(鐵律:唯讀一律走 db_ro)。這支只從 db 讀、寫的是 index.html 與
    # archive/,不曾寫 db;bare sqlite3.connect 會在路徑打錯時無聲建一個空 db,
    # 然後產出一份「0 檔」的頁面覆蓋掉正常的那份。
    con = db_ro.connect(DB)
    last = con.execute("SELECT MAX(date) FROM daily_scores").fetchone()[0]
    if not last:
        print("daily_scores 沒有資料,請先跑 score.py")
        return
    rows = con.execute("""SELECT u.stock_id, u.name, u.grp, u.biz, sc.*, m.*
        FROM daily_scores sc JOIN universe u USING(stock_id) JOIN daily_metrics m USING(date, stock_id)
        WHERE sc.date=?""", (last,)).fetchall()
    active_n = len(rows)
    universe_n = con.execute("SELECT COUNT(*) FROM universe").fetchone()[0]
    trading_map = {}
    active_ids = {r["stock_id"] for r in rows}
    status_rows = tstatus.verified_exclusions(con, last)
    eligible_n = universe_n - len(status_rows)
    for status in status_rows:
        sid, state, source, reason = status
        # 停牌日不產生新分數；畫面只展示最近一次正式訊號，並明確標出其資料日期。
        stale = con.execute("""SELECT u.stock_id, u.name, u.grp, u.biz, sc.*, m.*
            FROM daily_scores sc JOIN universe u USING(stock_id)
            JOIN daily_metrics m USING(date, stock_id)
            WHERE sc.stock_id=? AND sc.date<? ORDER BY sc.date DESC LIMIT 1""",
            (sid, last)).fetchone()
        if stale and sid not in active_ids:
            rows.append(stale)
            trading_map[sid] = {
                "status": state, "source": source, "reason": reason,
                "date": last, "signalDate": stale["date"],
                "label": "暫停／未交易",
            }
    # 使用每日未平滑 composite 讓使用者能驗算 composite_s；同一份近5日歷史也供
    # 「五日變層軌跡」使用。verdict() 仍只取最後3筆驗算 composite_s。
    tier_dates = [r[0] for r in con.execute(
        "SELECT DISTINCT date FROM daily_scores WHERE date<=? ORDER BY date DESC LIMIT 5",
        (last,))][::-1]
    score_hist = defaultdict(list)
    for h in con.execute("""SELECT date, stock_id, composite, tier, tier_raw FROM daily_scores
                            WHERE date<=? ORDER BY stock_id, date DESC""", (last,)):
        if len(score_hist[h["stock_id"]]) < 5:
            score_hist[h["stock_id"]].insert(0, h)
    # 個股技術面:穿越/變化解讀需今日、昨日與5個交易日前;互動股價圖需 CHART_DAYS 日
    # 還原價+均線+RSI+量 → 每檔保留最近 CHART_DAYS 個交易日,舊到新。
    tech_hist = defaultdict(list)
    for h in con.execute("""SELECT date, stock_id, close_adj, ma5, ma20, ma60, rsi14,
                                    volume, vol_ma20, vol_ratio20, ret1
                             FROM daily_metrics WHERE date<=?
                             ORDER BY stock_id, date DESC""", (last,)):
        if len(tech_hist[h["stock_id"]]) < CHART_DAYS:
            tech_hist[h["stock_id"]].insert(0, h)
    # 外資/投信每日淨買賣(股→張),供互動股價圖兩條副圖;窗口與 tech_hist 對齊即可
    inst_hist = defaultdict(dict)
    for r in con.execute("""SELECT date, stock_id, foreign_buy, foreign_sell,
                                   trust_buy, trust_sell
                            FROM inst WHERE date<=? ORDER BY date""", (last,)):
        fn = (r["foreign_buy"] or 0) - (r["foreign_sell"] or 0)
        tn = (r["trust_buy"] or 0) - (r["trust_sell"] or 0)
        inst_hist[r["stock_id"]][r["date"]] = (round(fn / 1000), round(tn / 1000))
    try:   # 族群定義配置化:讀 groups 表(舊 db 缺表時退回檔頭預設)
        gmeta = con.execute("SELECT grp, name, tag FROM groups ORDER BY ord").fetchall()
        if gmeta:
            GROUP_ORDER[:] = [g["grp"] for g in gmeta]
            GROUP_NM.update({g["grp"]: g["name"] for g in gmeta})
            GROUP_TAG.update({g["grp"]: g["tag"] for g in gmeta})
    except sqlite3.OperationalError:
        pass
    try:   # 舊 db 尚無族群/大盤表 → 雷達留空(跑一次 fetch_daily 即補齊)
        grows = con.execute("SELECT * FROM group_metrics WHERE date=?", (last,)).fetchall()
        # 指數資料可能落後個股一日 → 取 ≤last 的最近一筆(顯示時標註日期)
        mk = con.execute("""SELECT * FROM market_daily WHERE date<=? AND dd20 IS NOT NULL
                            ORDER BY date DESC LIMIT 1""", (last,)).fetchone()
        # 大盤 20 日報酬(含息報酬指數):①價 tooltip 的基準線,與個股 ret20 同窗口
        mkrows = con.execute("""SELECT taiex FROM market_daily WHERE taiex IS NOT NULL
                                AND date<=? ORDER BY date""", (last,)).fetchall()
        mkt20 = (mkrows[-1]["taiex"] / mkrows[-21]["taiex"] - 1) if len(mkrows) >= 21 else None
        # 族群歷史:狀態連續天數 + 各欄獨立的 5 日變化說明
        ghist = con.execute("""SELECT date, grp, state, med_dip, breadth_f, rel20,
                                      med_dist60, breadth_t FROM group_metrics
                               WHERE date<=? ORDER BY date""", (last,)).fetchall()
    except sqlite3.OperationalError:
        grows, mk, mkt20, ghist = [], None, None, []
    market_provenance = None
    if mk:
        try:
            market_provenance = con.execute(
                """SELECT canonical_source,official_taiex,finmind_taiex,abs_diff
                   FROM market_provenance WHERE date=?""", (mk["date"],)).fetchone()
        except sqlite3.OperationalError:
            pass
    gseries = {}
    for x in ghist:
        gseries.setdefault(x["grp"], []).append(x)
    # 廣度的分子/分母(與 fetch_daily 口徑一致:分母=當日有值的成員數)——tooltip 顯示 x/N 檔
    bcnt = {r["grp"]: r for r in con.execute("""SELECT u.grp,
            SUM(CASE WHEN m.fpct_chg20>0 THEN 1 ELSE 0 END) f_pos, COUNT(m.fpct_chg20) f_n,
            SUM(CASE WHEN m.trust5_pct>0 THEN 1 ELSE 0 END) t_pos, COUNT(m.trust5_pct) t_n
            FROM daily_metrics m JOIN universe u USING(stock_id)
            WHERE m.date=? GROUP BY u.grp""", (last,))}
    # 族群「絕對」20 日中位報酬。group_metrics 只存 rel20(跨族群相對),整套訊號也都是
    # 相對排名——沒有絕對值時,「這族群相對強」會被讀成「這族群在漲」。族群卡與個股列
    # 並列絕對報酬後,才分得出「它強」與「它跌得比較少」。
    gabs = {}
    _gret = defaultdict(list)
    for r in con.execute("""SELECT u.grp, m.ret20 FROM daily_metrics m JOIN universe u USING(stock_id)
            WHERE m.date=? AND m.ret20 IS NOT NULL""", (last,)):
        _gret[r["grp"]].append(r["ret20"])
    for g, v in _gret.items():
        gabs[g] = {"med": round(statistics.median(v) * 100, 1),
                   "pos": sum(1 for x in v if x > 0), "n": len(v)}
    # 處置/注意股票(觀察層、不計分):交易所官方認證的異常價量列管,五元素分數看不到——
    # 只顯示當天名單,不判斷起訖(risk_flags 由 fetch_daily 每日整表重建)
    risk = {}
    try:
        for r in con.execute("SELECT stock_id, kind, reason, period FROM risk_flags WHERE date=?", (last,)):
            risk.setdefault(r["stock_id"], []).append(
                {"kind": r["kind"], "reason": r["reason"], "period": r["period"]})
    except sqlite3.OperationalError:
        pass
    # 籌碼健康度(觀察層、獨立新表,舊 db 未跑過新版 score.py 時沒有此表 → 全部從缺,不擋主管線)
    chip = {}
    try:
        for r in con.execute(
                "SELECT stock_id, label FROM chip_health WHERE date=?", (last,)):
            chip[r["stock_id"]] = {"label": r["label"]}
    except sqlite3.OperationalError:
        pass
    # 新增官方欄位的觀察解剖：獨立衍生表，不進 daily_metrics/daily_scores。
    observation_map, group_observation_map = {}, {}
    try:
        for r in con.execute("""SELECT o.*,
                p.trades AS raw_trades,p.volume AS raw_volume,p.amount AS raw_amount,
                i.foreign_buy AS raw_foreign_buy,i.foreign_sell AS raw_foreign_sell,
                i.trust_buy AS raw_trust_buy,i.trust_sell AS raw_trust_sell,
                i.dealer_self_net AS raw_dealer_self_net,
                i.dealer_hedge_net AS raw_dealer_hedge_net,
                m.margin_bal AS raw_margin_bal,m.margin_buy AS raw_margin_buy,
                m.margin_sell AS raw_margin_sell,
                m.margin_cash_repay AS raw_margin_cash_repay,m.margin_limit AS raw_margin_limit,
                m.margin_prev_bal AS raw_margin_prev_bal,
                m.short_bal AS raw_short_bal,m.short_sell AS raw_short_sell,
                m.short_buyback AS raw_short_buyback,
                m.short_stock_repay AS raw_short_stock_repay,m.short_limit AS raw_short_limit,
                m.short_prev_bal AS raw_short_prev_bal,
                m.offset_volume AS raw_offset_volume,
                h.foreign_shares AS raw_foreign_shares,
                h.foreign_available_shares AS raw_foreign_available_shares,
                h.foreign_available_pct AS raw_foreign_available_pct,
                h.foreign_limit_pct AS raw_foreign_limit_pct,
                s.sbl_sell AS raw_sbl_sell,s.sbl_return AS raw_sbl_return,
                s.sbl_adjustment AS raw_sbl_adjustment,s.sbl_next_limit AS raw_sbl_next_limit
            FROM observation_metrics o
            LEFT JOIN price p USING(date,stock_id)
            LEFT JOIN inst i USING(date,stock_id)
            LEFT JOIN margin m USING(date,stock_id)
            LEFT JOIN holding h USING(date,stock_id)
            LEFT JOIN sbl s USING(date,stock_id)
            WHERE o.date=?""", (last,)):
            observation_map[r["stock_id"]] = r
        for r in con.execute(
                "SELECT * FROM group_observation_metrics WHERE date=?", (last,)):
            group_observation_map[r["grp"]] = r
    except sqlite3.OperationalError:
        # 舊 DB 尚未跑過 metrics-only 時從缺，不阻止既有儀表板發布。
        observation_map, group_observation_map = {}, {}
    # 基本面參考(觀察層、獨立新表,fetch_financials.py 尚未跑過的 db 沒有這些表 → 從缺,不擋主管線)
    try:
        fund_map = build_fund_map(con)
    except sqlite3.OperationalError:
        fund_map = {}
    # 事件錨點是研究中心的市場議題來源；目錄不存在時回 latest=None，不擋主管線。
    events = load_events()
    # 策略狀態(證據強度)與兩視角分歧——都必須在 con.close() 之前算
    strategy = build_strategy_status(con, last)
    diverge = build_divergence(con, last, _names(con), GROUP_NM)
    lenses = build_lenses(con, last, _names(con), GROUP_NM)
    con.close()
    # 質化筆記(觀察層、AI 協作＋獨立 reviewer,見 notes/qualitative/):無筆記時 load_notes
    # 回傳空 dict,同 fund_map 的「從缺不擋主管線」慣例
    notes_map = load_notes(NOTES_DIR)
    # 領先假說是獨立觀察層；lint 會要求其錨定有效 independently_verified 正式筆記。
    hypotheses_map = load_hypothesis_reports(HYPOTHESES_DIR, notes=notes_map)
    # 最近研究文章使用各層既有 parser 的可稽核 meta；不讀 git/檔案 mtime。
    # anchor 取市場資料日與文章日期較晚者，避免市場資料尚未換日時漏掉今天剛更新的文章。
    # 研究 freshness 跟日曆日走，不跟最後交易日走；否則週末與休市日會延後降級。
    research_as_of = research_today()
    research_topics = load_research_topics(
        TOPICS_DIR, reports=hypotheses_map, as_of=research_as_of)
    stock_names = {r["stock_id"]: r["name"] for r in rows}
    stock_meta = {
        r["stock_id"]: {"name": r["name"], "group": r["grp"], "biz": r["biz"] or ""}
        for r in rows
    }
    recent_articles = build_recent_articles(
        last, notes_map, hypotheses_map, events, research_topics, stock_names,
    )
    research_group_guide = load_research_group_guide(strict=True)
    research_reader_terms = load_research_reader_terms(strict=True)
    research_topic_guide = load_research_topic_guide(strict=True)
    research_library = build_research_library(
        notes_map, hypotheses_map, research_topics, stock_meta, GROUP_NM, events,
        as_of=research_as_of,
        reader_terms=research_reader_terms,
    )
    attach_research_topic_guide(
        research_library, research_topic_guide, strict=True,
    )
    for group in research_library.get("groups", []):
        group.update(research_group_guide.get(group.get("id"), {}))
    # 首頁不再自行解讀「研究總進度」；總數、分類數與最新批次都以研究中心 library
    # 為準，且同一時間窗有任何 article id 漏列都直接讓 build 失敗。
    recent_articles = attach_research_library_progress(recent_articles, research_library)
    # 證據型知識圖譜只投影既有 active claim／獨立核驗筆記來源；任何失效引用都讓
    # build 直接標紅，避免圖上關係悄悄與研究帳本分岔。
    research_library["knowledgeGraph"] = build_knowledge_graph(
        research_topics, notes_map, strict=True,
    )
    # 每次 build 使用獨立 route dict；attach_research_learning_paths 會在輸出物上
    # 加入由既有 graph／article 產生的 stations，不可污染模組級常數或下一次 build。
    research_library["knowledgeGraph"]["learningRoutes"] = [
        dict(route) for route in RESEARCH_LEARNING_ROUTES
    ]
    # 新手延伸閱讀只串接 library 中已存在的文章、族群與圖譜；它是導覽層，
    # 不新增供應鏈關係，也不把共享族群誤寫成已驗證的公司曝險。
    attach_research_learning_paths(
        research_library, research_library["knowledgeGraph"],
    )
    # 候選雷達與正式文章／圖譜分層：它可以排序「下一題研究什麼」，但候選來源本身
    # 不會繞過 knowledge_graph 的 active claim 契約。升格連結也在 build 時查存在性。
    research_library["candidateRadar"] = load_research_radar(
        topic_ids={topic.get("meta", {}).get("topic_id", "") for topic in research_topics},
        graph_ids={graph["id"] for graph in research_library["knowledgeGraph"]["graphs"]},
        strict=True,
    )
    # 方法稽核讀取 versioned、append-only snapshot；不在 build 當下動態重算後假裝成歷史。
    # registry 變動卻沒有新 snapshot 會由 research_method_audit.py --lint 標紅。
    research_library["methodAudit"] = load_method_audit(strict=True)
    # 族群成熟度不是 article count 排名：公司筆記、題材、具名公司橋接、材料性、
    # 證據層級與維護期限分軸顯示。到期狀態重播 append-only monitor review ledger，
    # 避免已檢查但沒有新 evidence 的 stale topic 被誤標成「從未處理」。
    research_reviews = load_monitor_reviews(
        research_topics, research_as_of, strict=True,
    )
    research_library["groupMaturity"] = build_group_maturity(
        notes_map, research_topics, stock_meta, GROUP_NM,
        research_library["knowledgeGraph"], research_reviews,
        research_library["methodAudit"], research_as_of,
        candidate_radar=research_library["candidateRadar"],
        group_guide=research_group_guide,
    )
    attach_group_learning_starts(research_library)

    CHIP_CLS = {"健康": "health", "中性": "neutral", "待觀察": "warn"}
    chip_by_grp = {}
    for r in rows:
        c = chip.get(r["stock_id"])
        if not c:
            continue
        cc = chip_by_grp.setdefault(r["grp"], {"health": 0, "neutral": 0, "warn": 0, "dots": []})
        cls = CHIP_CLS[c["label"]]
        cc[cls] += 1
        cc["dots"].append(cls)

    dip_rows = [x for x in grows if x["med_dip"] is not None]
    best_dip_row = max(dip_rows, key=lambda x: x["med_dip"]) if dip_rows else None
    best_dip = best_dip_row["grp"] if best_dip_row else None
    groups = []
    for g in GROUP_ORDER:
        r = next((x for x in grows if x["grp"] == g), None)
        if not r:
            continue
        note = r["note"] or ""
        if g == best_dip:
            if r["med_dip"] > 0:
                note += f"(★ 修正日淨買為 {len(GROUP_ORDER)} 族群最高)"
            elif r["med_dip"] < 0:
                note += f"(★ 修正日調節為 {len(GROUP_ORDER)} 族群相對最少,但仍是淨賣)"
            else:
                note += f"(★ 修正日買賣為 {len(GROUP_ORDER)} 族群相對最高,目前持平)"
        ser = gseries.get(g, [])
        n, since = _streak(ser)
        bc = bcnt.get(g)
        # stats 每列 = [標籤, 當下原始值, 白話解讀, 5日變化]；不可把方向箭頭黏在原始值後面。
        # 解讀句由「當下數值」生成(方向、對照門檻),不是通用定義——這是看得懂的關鍵。
        dip = r["med_dip"]
        dip_dyn = ("" if dip is None else
                   (";目前=族群修正日外資淨買" if dip > 0 else
                    ";目前=族群修正日外資淨賣" if dip < 0 else ";目前買賣持平"))
        rel = r["rel20"]
        rel_dyn = ("" if rel is None else
                   (";目前=跑贏其他族群" if rel > 0 else ";目前=落後其他族群" if rel < 0 else ""))
        dist = r["med_dist60"]
        dist_dyn = ("" if dist is None else
                    (f";目前≤{GS_OFF_HIGH*100:.0f}%=「價未回高」(蓄勢的前提)" if dist <= GS_OFF_HIGH
                     else ";目前接近波段高"))
        bf = r["breadth_f"]
        bf_dyn = ("" if bf is None else
                  (f";目前≤{GS_BREADTH_LOW*100:.0f}%=廣度低(個案而非族群現象)" if bf <= GS_BREADTH_LOW
                   else ";過半成員被增持=族群現象" if bf > 0.5 else ""))
        dist_value = ("-" if dist is None else
                      f"低於60日高 {abs(dist)*100:.1f}%" if dist < 0 else
                      "位於60日高 0.0%" if dist == 0 else
                      f"高於參考高點 {dist*100:+.1f}%")
        # stats 第5欄=圖形規格(前端渲染):{"spark":trend鍵}=30日迷你趨勢線、
        # {"meter":[值,滿格,門檻]}=廣度量尺;None=純文字列。文字欄完全不動。
        bt = r["breadth_t"]
        gobj = {"g": g, "nm": GROUP_NM.get(g, g), "state": r["state"],
                "col": STATE_COL.get(r["state"], "var(--neutral)"), "note": note,
                "abs20": gabs.get(g),
                "axis": {"price": rel, "dip": dip,
                         "price5": _five_day_value(ser, "rel20"),
                         "dip5": _five_day_value(ser, "med_dip"),
                         "date": ser[-1]["date"] if ser else None,
                         "date5": ser[-6]["date"] if len(ser) >= 6 else None},
                # 族群熱圖使用原始數值與五日前數值；所有欄位皆是「越高越靠前」，
                # 前端可用同一套跨族群名次色階，不把不同單位硬塞進同一數值尺度。
                "heat": {
                    "dip": [round(dip, 4) if dip is not None else None,
                            _five_day_value(ser, "med_dip")],
                    "breadth_f": [round(bf, 4) if bf is not None else None,
                                  _five_day_value(ser, "breadth_f")],
                    "rel20": [round(rel, 5) if rel is not None else None,
                              _five_day_value(ser, "rel20")],
                    "dist60": [round(dist, 5) if dist is not None else None,
                               _five_day_value(ser, "med_dist60")],
                    "breadth_t": [round(bt, 4) if bt is not None else None,
                                  _five_day_value(ser, "breadth_t")],
                },
                # 30個交易日的走勢原料(缺值日剔除,迷你圖只看形狀)
                "trend": {"dip": [round(x["med_dip"], 3) for x in ser[-30:]
                                  if x["med_dip"] is not None],
                          "dipDates": [x["date"] for x in ser[-30:]
                                       if x["med_dip"] is not None],
                          "rel": [round(x["rel20"] * 100, 2) for x in ser[-30:]
                                  if x["rel20"] is not None],
                          "relDates": [x["date"] for x in ser[-30:]
                                       if x["rel20"] is not None]},
                "stats": [
            ["修正日外資買賣中位",
             _current_dip(dip),
             "族群下跌日外資買賣的20日累計佔股本%(取成員中位)。"
             f"正=淨買、負=淨賣{dip_dyn}",
             _five_day_delta(ser, "med_dip", 0.01, 1, 2),
             {"spark": "dip"}],
            ["外資增持廣度",
             f"{bf*100:.0f}%成員增持({bc['f_pos']}/{bc['f_n']}檔)" if (bf is not None and bc) else "-",
             f"近20日外資持股增加的成員比例；用來分辨普遍現象或少數個案{bf_dyn}",
             _five_day_delta(ser, "breadth_f", 0.01, 100, 0),
             {"meter": [round(bf, 3), 1, 0.5]} if bf is not None else None],
            ["20日動能 vs 全體",
             _current_relative(rel),
             "族群中位20日報酬 − 全部掃描標的中位——族群跟其他族群比"
             f"(個股卡的①價是族群內比){rel_dyn}",
             _five_day_delta(ser, "rel20", 0.005, 100, 1),
             {"spark": "rel"}],
            ["中位距60日高",
             dist_value,
             f"成員距自己60日高點的中位數,衡量族群整體回檔深度{dist_dyn}",
             _five_day_delta(ser, "med_dist60", 0.001, 100, 1),
             {"rp": [round(dist * 100, 1), min(-30.0, round(dist * 100, 1)), 0,
                     GS_OFF_HIGH * 100]} if dist is not None else None],
            ["投信買超廣度",
             f"{bt*100:.0f}%成員淨買({bc['t_pos']}/{bc['t_n']}檔)"
             if (bt is not None and bc) else "-",
             "近5日投信(本土基金)買超的成員比例,與外資廣度對照看參與度",
             _five_day_delta(ser, "breadth_t", 0.01, 100, 0),
             {"meter": [round(bt, 3), 1, 0.5]} if bt is not None else None],
        ]}
        if n:
            gobj["dur"] = f"第 {n} 個交易日(自 {since})"
        if g in chip_by_grp:
            gobj["chip"] = chip_by_grp[g]
        if g in group_observation_map:
            gobj["flow"] = build_group_observation_view(
                group_observation_map[g], GROUP_NM.get(g, g), GROUP_TAG.get(g, ""))
        groups.append(gobj)
    overview = build_overview(grows)
    mtip = None
    if mk and mk["dd20"] is not None:
        regime = bool(mk["regime"])
        mtip = {
            "el": "市場環境", "scLabel": "⚠ 修正" if regime else "多頭/中性",
            "scColor": "var(--warn-line)" if regime else "var(--neutral)",
            "scBg": "var(--neutral-tint)", "who": "加權報酬指數(含息)",
            "rows": [["指數日期", mk["date"]],
                     ["距20日高", f"{mk['dd20']*100:+.1f}%",
                      "含息指數距近20個交易日最高點回落多少;回檔深度的量尺"],
                     ["修正門檻", f"≤ {REGIME_DD*100:.0f}%",
                      "回落超過此值即判為修正市場情境,頁首籤條會轉「⚠ 修正」"],
                     ["20日報酬", pct(mkt20, True),
                      "全市場近一個月的基準線;個股①價 tooltip 的「大盤20日」同此值"]],
            "why": ("報酬指數距 20 日高回落超過門檻,判定為修正市場情境——此時「修正日抗跌」"
                    "「修正日外資買賣」等訊號較有辨識力,適合觀察哪個族群先止穩轉強。" if regime else
                    "距 20 日高回落未達門檻,市場處於多頭/中性,個股訊號以族群內相對強弱為主。"),
            "how": (f"距20日高 ≤ {REGIME_DD*100:.0f}% → 修正市場情境。使用「含息」報酬指數而非"
                    "價格指數,避免除息季的機械性下跌扭曲市場比較。"),
            "src": market_source_text(market_provenance)}

    data, tiers_map = [], {}
    for r in rows:
        tier_meta = tier_ui_payload(r)
        hist = score_hist.get(r["stock_id"]) or []
        comp_hist = [h for h in hist[-3:] if h["composite"] is not None]
        vt, tier, vsub, vr, warn, vrows = verdict(r, hist)
        obj = {"g": r["grp"], "id": r["stock_id"], "nm": r["name"], "biz": r["biz"] or "",
               "vt": vt, "vlabel": tier_meta["tier_label"], "vkey": tier,
               "vsub": vsub, "vr": vr, "vrows": vrows,
               # 詳情面板的七因子發散條：條長固定看元素分(-2~+2)，權重與貢獻另列，
               # 避免高權重把「族群相對位置」的原始分數尺度扭曲。
               "factors": [
                   {"k": "price", "label": "①相對強弱", "score": r["s_price"],
                    "weight": WEIGHTS["price"]},
                   {"k": "resil", "label": "①抗跌", "score": r["s_resil"],
                    "weight": WEIGHTS["resil"]},
                   {"k": "vol", "label": "②量", "score": r["s_vol"],
                    "weight": WEIGHTS["vol"]},
                   {"k": "foreign", "label": "③外資", "score": r["s_foreign"],
                    "weight": WEIGHTS["foreign"]},
                   {"k": "dip", "label": "③修正日買賣", "score": r["s_dip"],
                    "weight": WEIGHTS["dip"]},
                   {"k": "trust", "label": "④投信", "score": r["s_trust"],
                    "weight": WEIGHTS["trust"]},
                   {"k": "margin", "label": "⑤融資券", "score": r["s_margin"],
                    "weight": WEIGHTS["margin"]},
               ],
               # 綜評條原料:3日平滑分(實條)+近3日未平滑分(殘影點),與 vrows 文字同源
               "comp": round(r["composite_s"], 2) if r["composite_s"] is not None else None,
               "comp3": [round(h["composite"], 2) for h in comp_hist],
               "comp3Dates": [h["date"] for h in comp_hist],
               # 20 日**絕對**報酬。整套系統都是族群內相對,所以「相對強勢」可能與
               # 「絕對在跌」並存——2026-07-24 實測 11 檔真強裡有 7 檔 20 日為負,
               # 最深一檔 −21.8%。不把絕對值放在同一列,讀者會把「相對強」讀成「在漲」。
               "ret20": round(r["ret20"] * 100, 1) if r["ret20"] is not None else None,
               "cells": build_cells(r, r, mkt20)}
        if r["stock_id"] in trading_map:
            obj["trading"] = trading_map[r["stock_id"]]
        obj.update(tier_meta)
        tech = build_technical_view(r, tech_hist.get(r["stock_id"]))
        if tech:
            if tech.get("chart"):
                ih = inst_hist.get(r["stock_id"], {})
                ch = tech["chart"]
                ch["foreign"] = [ih.get(d, (None, None))[0] for d in ch["dates"]]
                ch["trust"] = [ih.get(d, (None, None))[1] for d in ch["dates"]]
            obj["tech"] = tech
        observation = observation_map.get(r["stock_id"])
        if observation:
            obj["flow"] = build_observation_view(observation)
            obj["flow"].update({"who": r["name"] + "(" + r["stock_id"] + ")",
                                "biz": r["biz"] or ""})
        if warn:
            obj["warn"] = True
        risky = r["stock_id"] in risk
        if risky:
            obj["risk"] = risk[r["stock_id"]]
        c = chip.get(r["stock_id"])
        if c:
            chip_rows, n_health, n_warn = build_chip_rows(r, risky)
            why = f"{n_health} 項健康信號、{n_warn} 項警示；原始正負號不直接代表好壞"
            if risky:
                why += "；當天列處置/注意,官方警示一票否決"
            obj["chip"] = {"cls": CHIP_CLS[c["label"]], "label": c["label"],
                           "rows": chip_rows, "why": why}
        f = fund_map.get(r["stock_id"])
        if f:
            obj["fund"] = f
        n = notes_map.get(r["stock_id"])
        if n:
            # asof 用資料日(last)而非 wall-clock today——archive 快照才可重現(同一資料日重建,
            # 「建議複核」判定不會因為隔幾天重跑而改變)
            st = note_status(n, last)
            verification = note_review_status(n)
            label = NOTE_LABEL[verification]
            if n.get("quality_invalid"):
                label += "・品質契約未通過"
            if st == "due":
                label += "・待更新"
            elif st == "draft":
                label += "・未填更新日"
            elif st == "unscheduled":
                label += "・未排複核日"
            obj["note"] = {
                "cls": verification, "label": label,
                "freshness": st, "due": st == "due",
                "updated": n["last_updated"] or "-", "next": n["next_review"] or "-",
                "contentAsOf": n.get("content_as_of") or "-",
                "latestPeriod": n.get("latest_financial_period") or "-",
                "reviewedAt": n.get("reviewed_at") or "-",
                "reviewedBy": n.get("reviewed_by") or "-",
                "reviewScope": n.get("review_scope") or "-",
                "qualityInvalid": n.get("quality_invalid", False),
                "qualityErrors": n.get("quality_errors", []),
                "claimCount": n.get("claim_count", 0),
                "citedClaims": n.get("cited_claim_count", 0),
                "primaryClaims": n.get("primary_cited_claim_count", 0),
                "primarySources": n.get("primary_source_count", 0),
                "summary": n["summary"], "tmplOld": n["template_version"] < NOTE_TEMPLATE_VERSION,
                "url": NOTE_REPO_BLOB + n["relpath"],
                "researchUrl": f"research.html#formal-{r['stock_id']}",
            }
        hypothesis = hypotheses_map.get(r["stock_id"])
        if hypothesis:
            status_counts = defaultdict(int)
            capture_mode_counts = defaultdict(int)
            lifecycle_counts = defaultdict(int)
            due_count = 0
            independent_chains = 0
            for item in hypothesis.get("hypotheses", []):
                raw = item.get("fields", {}).get("目前狀態", "")
                match = re.search(r"`([a-z_]+)`", raw)
                status_counts[match.group(1) if match else "unknown"] += 1
                hmeta = item.get("meta", {})
                capture_mode_counts[hmeta.get("capture_mode") or "unknown"] += 1
                lifecycle_counts[hmeta.get("lifecycle") or "unknown"] += 1
                try:
                    independent_chains += int(hmeta.get("independent_chain_count") or 0)
                except ValueError:
                    pass
                if (hmeta.get("lifecycle") == "open"
                        and re.fullmatch(r"\d{4}-\d{2}-\d{2}", hmeta.get("review_due", ""))
                        and hmeta["review_due"] <= last):
                    due_count += 1
            count = hypothesis.get("hypothesis_count", 0)
            obj["hypothesis"] = {
                "label": f"領先假說 {count} 則",
                "count": count,
                "updated": hypothesis.get("last_updated") or "-",
                "contentAsOf": hypothesis.get("content_as_of") or "-",
                "next": hypothesis.get("next_review") or "-",
                "qualityInvalid": hypothesis.get("quality_invalid", False),
                "qualityErrors": hypothesis.get("quality_errors", []),
                "statusCounts": dict(status_counts),
                "statusInfo": HYPOTHESIS_STATUS_INFO,
                "captureModeCounts": dict(capture_mode_counts),
                "lifecycleCounts": dict(lifecycle_counts),
                "dueCount": due_count,
                "independentChains": independent_chains,
                "schemaVersion": hypothesis.get("report_version", 0),
                "researchUrl": f"research.html#narrative-{r['stock_id']}",
                "url": NOTE_REPO_BLOB + hypothesis["relpath"],
            }
        obj["_comp"] = r["composite_s"]
        data.append(obj)
        if r["stock_id"] not in trading_map:
            tiers_map.setdefault(tier, []).append((r["composite_s"], r["stock_id"]))

    # 排序:族群順序,族群內綜合分數由高到低
    data.sort(key=lambda o: (GROUP_ORDER.index(o["g"]), -o["_comp"]))
    for o in data:
        del o["_comp"]

    # 近5個交易日只列「已確認分層曾改變」的個股；未變層檔數由前端依族群篩選即時計算。
    # states 保留策略 key，顯示名稱與顏色由 tiers 單一對照表提供。
    tier_flow_stocks = []
    for o in data:
        if o.get("trading"):
            continue
        by_date = {h["date"]: h["tier"] for h in score_hist.get(o["id"], [])}
        states = [by_date.get(d) for d in tier_dates]
        observed = [s for s in states if s is not None]
        if len(observed) < 2 or len(set(observed)) < 2:
            continue
        last_change = max((i for i in range(1, len(states))
                           if states[i] is not None and states[i - 1] is not None
                           and states[i] != states[i - 1]), default=0)
        tier_flow_stocks.append({"id": o["id"], "nm": o["nm"], "g": o["g"],
                                 "states": states, "lastChange": last_change})
    tier_pos = {t: i for i, t in enumerate(TIER_ORDER)}
    tier_flow_stocks.sort(key=lambda o: (-o["lastChange"], GROUP_ORDER.index(o["g"]),
                                         tier_pos.get(o["states"][-1], 99), o["id"]))
    tier_flow = {
        "dates": tier_dates,
        "tiers": [{"key": t, "label": TIER_UI_LABEL.get(t, t),
                   "col": TIER_COL.get(t, "var(--neutral)")} for t in TIER_ORDER],
        "stocks": tier_flow_stocks,
    }

    # ◇ 蓄勢候補獨立卡片:從中性池抽出、插在蓄勢旁(缺項少者排前)
    cands = sorted(((r["pending"].count("、"), -r["composite_s"], r["stock_id"], r["pending"])
                    for r in rows if r["stock_id"] not in trading_map
                    and r["pending"] and r["tier"] == "潛在/中性"))
    cand_ids = [c[2] for c in cands]
    cand_sub = {c[2]: c[3].replace("蓄勢候補·", "") for c in cands}

    tiers = []
    for t in TIER_ORDER:
        if t in tiers_map:
            ids = [sid for _, sid in sorted(tiers_map[t], reverse=True)]
            if t == "潛在/中性":
                ids = [i for i in ids if i not in cand_ids]
            tiers.append({"key": t, "t": TIER_UI_LABEL.get(t, t), "d": TIER_DESC.get(t, ""),
                          "col": TIER_COL.get(t, "var(--neutral)"), "ids": ids})
        if t == "蓄勢·外資佈局" and cand_ids:
            tiers.append({"key": "蓄勢候補", "t": "◇ 相對蓄勢候補",
                          "d": "籌碼相對位置靠前；補齊後先成為今日初判,連2日才更新已確認層",
                          "col": "var(--neutral)", "ids": cand_ids, "sub": cand_sub})

    y, mo, d = last.split("-")
    date_str = f"{y}/{int(mo)}/{int(d)}"
    grpmeta = {g: {"nm": GROUP_NM.get(g, g), "tag": GROUP_TAG.get(g, ""),
                   "short": GROUP_SHORT.get(g, GROUP_NM.get(g, g))} for g in GROUP_ORDER}
    html = open(TEMPLATE, encoding="utf-8").read()
    html = html.replace("__DATA_JSON__", json.dumps(data, ensure_ascii=False))
    html = html.replace("__TIERS_JSON__", json.dumps(tiers, ensure_ascii=False))
    html = html.replace("__GROUPS_JSON__", json.dumps(groups, ensure_ascii=False))
    html = html.replace("__TIER_FLOW_JSON__", json.dumps(tier_flow, ensure_ascii=False))
    html = html.replace("__OVERVIEW_JSON__", json.dumps(overview, ensure_ascii=False))
    html = html.replace("__GRPMETA_JSON__", json.dumps(grpmeta, ensure_ascii=False))
    html = html.replace("__GORDER_JSON__", json.dumps(GROUP_ORDER))
    html = html.replace("__WEIGHTS_JSON__", json.dumps(WEIGHTS))
    html = html.replace("__STRATEGY_JSON__", json.dumps(strategy, ensure_ascii=False))
    html = html.replace("__DIVERGE_JSON__", json.dumps(diverge, ensure_ascii=False))
    html = html.replace("__LENS_JSON__", json.dumps(lenses, ensure_ascii=False))
    html = html.replace("__RECENT_ARTICLES_JSON__",
                        json.dumps(recent_articles, ensure_ascii=False))
    # 量尺門檻(②量比/⑤融資水位)——單一事實來源 score.py,調旋鈕量尺刻度自動同步
    html = html.replace("__THRESH_JSON__", json.dumps({
        "volr_active": list(VOLR_ACTIVE), "volr_dry": VOLR_DRY, "volr_overheat": VOLR_OVERHEAT,
        "margin_mid": MARGIN_UTIL_MID, "margin_hot": MARGIN_UTIL_HOT}))
    html = html.replace("__PAGE_TITLE__", PAGE_TITLE)
    html = html.replace("__H1__", H1_TITLE)
    html = html.replace("__TITLE_TAIL_JSON__", json.dumps(TITLE_TAIL, ensure_ascii=False))
    scope = f"{len(GROUP_ORDER)} 族群 · 有效評分 {active_n}/{eligible_n} 檔"
    if status_rows:
        scope += f" · 暫停／未交易 {len(status_rows)} 檔（完整名單 {universe_n}）"
    html = html.replace("__SCOPE__", scope)
    html = html.replace("__MKT_TIP_JSON__", json.dumps(mtip, ensure_ascii=False))
    html = html.replace("__GROUP_HOW_JSON__", json.dumps({"how": GROUP_HOW, "src": GROUP_SRC},
                                                         ensure_ascii=False))
    html = html.replace("__DATE_ISO__", last)
    html = html.replace("__DATE__", date_str)
    # 快照日期清單(含本次):注入頁內當 fallback,另寫 manifest 供已凍結的舊頁抓最新清單
    os.makedirs(ARCHIVE, exist_ok=True)
    dates = sorted({f[:10] for f in os.listdir(ARCHIVE)
                    if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.html", f)} | {last})
    html = html.replace("__DATES_JSON__", json.dumps(dates))
    research_html = open(RESEARCH_TEMPLATE, encoding="utf-8").read()
    research_html = research_html.replace(
        "__RESEARCH_JSON__", _inline_script_json(research_library)
    )
    research_html = research_html.replace("__DATE_ISO__", last)
    research_html = research_html.replace("__DATE__", date_str)
    open(OUT, "w", encoding="utf-8").write(html)
    open(RESEARCH_OUT, "w", encoding="utf-8").write(research_html)
    archive_path = os.path.join(ARCHIVE, f"{last}.html")
    archive_created = not os.path.exists(archive_path)
    if archive_created:
        open(archive_path, "w", encoding="utf-8").write(html)
    open(os.path.join(ARCHIVE, "manifest.json"), "w", encoding="utf-8").write(json.dumps(dates))
    print(f"已重生 {OUT}、{RESEARCH_OUT} — 資料日 {date_str},{len(data)} 檔,"
          f"研究 {research_library['total']} 篇,{len(tiers)} 個 tier;"
          f"{'建立' if archive_created else '保留既有'}快照 archive/{last}.html,"
          f"manifest 共 {len(dates)} 日")
    # 可選區段算不出來時前端只會少一整塊、導覽還留著死連結,而 build 照印「已重生」。
    # CI 的 tests.yml 刻意不吃 index.html/data 的路徑(每日 3~4 個資料 commit),
    # 所以產出物契約測試不會在每日管線上跑 → 這行是每日唯一會出聲的地方,務必留著。
    dead = [n for n, v in (("策略狀態", strategy),
                           ("兩視角分歧", diverge), ("時間尺度", lenses)) if not v]
    if dead:
        print(f"⚠ 下列區段沒有 payload,頁面會少掉整塊(導覽連結仍在):{'、'.join(dead)}")


if __name__ == "__main__":
    main()
