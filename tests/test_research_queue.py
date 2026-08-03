import sqlite3
import sys
import unittest
from datetime import date
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import research_queue as rq
import leading_hypotheses as lh


def topic_text(stock_id="1234", group_id="serverodm"):
    return f"""# 測試議題

<!-- research_topic
topic_id: MI-2026-07-27-TEST
schema_version: 1
status: triaged
priority: p1
captured_at: 2026-07-27
source_published_at: 2026-07-26
last_reviewed_at: 2026-07-27
review_due: 2026-08-03
source_type: official_company
publisher_domain: example.com
canonical_url: https://ir.example.com/news
source_chain_id: example-20260726
stock_ids: {stock_id}
group_ids: {group_id}
trigger_type: product_ramp
evidence_role: candidate_source
route: market_issue_watch
-->

<!-- transition
date: 2026-07-27
from: initial
to: inbox
reason: initial_capture
evidence: source_chain:example-20260726
-->
<!-- transition
date: 2026-07-27
from: inbox
to: triaged
reason: mapping_reviewed
evidence: source_chain:example-20260726
-->

<!-- impact
group_id: {group_id}
stock_ids: {stock_id}
direction: uncertain
hypothesis_refs: {stock_id}:H1
note_action: watch
action_due: 2026-08-03
rationale: 需要等公司正式揭露
evidence_boundary: 不構成訂單或營收事實
-->
"""


def topic_text_v2():
    return topic_text().replace("schema_version: 1", "schema_version: 2") + """

## 新手先讀：這篇在講什麼

### 名詞小字典

- **CPO**：把光學元件放到交換晶片旁邊，縮短高速電訊號要走的距離。
- **可插拔光模組**：可以從交換器面板拔換的光通訊模組，維修與升級比較直觀。
- **量產**：產品已進入持續製造，但不自動代表營收、毛利或市占已達特定水準。

### 三句話抓重點

- 這是第一句足以讓新手理解事件本身的完整重點摘要。
- 這是第二句用來說明證據邊界而不是把產業事件外推成訂單。
- 這是第三句提醒讀者等待公司正式文件與可觀察數字再做判斷。

### 為什麼重要

同一個產業事件可能同時帶來新需求與替代風險；先拆清楚技術位置、商業階段與公司曝險，讀者才不會把新聞標題直接當成營收結論。

### 接下來怎麼追

- 下一季公司文件是否首次揭露量產收入、客戶認證或毛利。
- 後續平台是否維持原時程，並出現可核對的出貨或部署節點。

### 想一想

- 哪個可觀察數字若沒有出現，會推翻目前的正面說法？
- 這是整體市場新增需求，還是把既有支出從另一種架構搬過來？

## 來源與證據邊界

- [官方來源](https://ir.example.com/news)

## 影響路由

只保留候選映射，不升格成公司事實。

## 下一個可證明／否定的節點

- 等待公司正式文件。
"""


def _contract_block(kind, fields):
    lines = [f"<!-- {kind}"]
    lines.extend(f"{key}: {value}" for key, value in fields)
    lines.append("-->")
    return "\n".join(lines)


def topic_text_v3():
    text = topic_text_v2().replace("schema_version: 2", "schema_version: 3", 1)
    text = "evidence: sources:S1,S2".join(
        text.rsplit("evidence: source_chain:example-20260726", 1))
    text = text.replace(
        "route: market_issue_watch\n-->",
        "route: market_issue_watch\n"
        "thesis_claim_id: C1\n"
        "base_confidence: high\n"
        "confidence_basis: 兩份來源直接支持事件、公司映射仍待驗證\n"
        "cross_company_numbers: false\n"
        "schema_migrated_at: 2026-07-27\n"
        "-->",
        1,
    )
    contract = "\n\n".join([
        _contract_block("research_source", [
            ("source_id", "S1"),
            ("role", "company_release"),
            ("publisher", "甲平台"),
            ("title", "甲平台產品公告"),
            ("published_at", "2026-07-26"),
            ("captured_at", "2026-07-27"),
            ("accepted_at", "2026-07-27"),
            ("status", "active"),
            ("url", "https://ir.example.com/news"),
            ("locator", "產品進度段落"),
            ("limitation", "未提供供應商收入與毛利"),
        ]),
        _contract_block("research_source", [
            ("source_id", "S2"),
            ("role", "competitor_primary"),
            ("publisher", "乙同業"),
            ("title", "乙同業產品公告"),
            ("published_at", "2026-07-25"),
            ("captured_at", "2026-07-27"),
            ("accepted_at", "2026-07-27"),
            ("status", "active"),
            ("url", "https://competitor.example.org/release"),
            ("locator", "量產與客戶段落"),
            ("limitation", "未揭露出貨數量"),
        ]),
        _contract_block("research_source", [
            ("source_id", "S9"),
            ("role", "exchange"),
            ("source_kind", "living_index"),
            ("publisher", "公開資訊站"),
            ("title", "公司申報查詢入口"),
            ("published_at", ""),
            ("captured_at", "2026-07-27"),
            ("accepted_at", "2026-07-27"),
            ("status", "active"),
            ("url", "https://exchange.example.net/search"),
            ("locator", "公司季報與重大訊息入口"),
            ("limitation", "入口本身不證明新訂單"),
        ]),
        _contract_block("research_claim", [
            ("claim_id", "C1"),
            ("label", "verified"),
            ("status", "active"),
            ("claim", "甲平台已正式公告產品進入量產階段"),
            ("supporting_source_ids", "S1"),
            ("contrary_source_ids", ""),
            ("as_of", "2026-07-27"),
            ("basis", "來源直接使用量產字樣"),
            ("boundary", "只證明公告內容，不證明台灣供應商收入"),
            ("verification_needed", "none"),
            ("resolution", ""),
            ("correction_kind", ""),
            ("corrects_claim_id", ""),
            ("corrected_by_claim_id", ""),
        ]),
        _contract_block("research_claim", [
            ("claim_id", "C2"),
            ("label", "unverified"),
            ("status", "active"),
            ("claim", "台灣供應商可能取得可量化新增訂單"),
            ("supporting_source_ids", ""),
            ("contrary_source_ids", "S2"),
            ("as_of", "2026-07-27"),
            ("basis", "平台事件只構成搜尋觸發"),
            ("boundary", "不可由產業事件直接建立個股訂單"),
            ("verification_needed", "公司法說、財報與客戶交叉文件"),
            ("resolution", ""),
            ("correction_kind", ""),
            ("corrects_claim_id", ""),
            ("corrected_by_claim_id", ""),
        ]),
        _contract_block("monitoring_item", [
            ("monitor_id", "T1"),
            ("status", "active"),
            ("claim_ids", "C1"),
            ("metric", "平台正式部署與出貨節點"),
            ("source_ids", "S1"),
            ("watch_source_ids", "S9"),
            ("frequency", "quarterly"),
            ("next_check", "2026-08-03"),
            ("trigger", "首次公布可核對的部署數量"),
            ("invalidation", "產品時程取消或量產措辭撤回"),
        ]),
        _contract_block("monitoring_item", [
            ("monitor_id", "T2"),
            ("status", "active"),
            ("claim_ids", "C2"),
            ("metric", "供應商收入、毛利與現金流"),
            ("source_ids", "S2"),
            ("watch_source_ids", "S9"),
            ("frequency", "quarterly"),
            ("next_check", "2026-08-10"),
            ("trigger", "公司文件首次量化相關收入"),
            ("invalidation", "公司否認參與或毛利現金流未改善"),
        ]),
    ])
    return text.replace(
        "\n## 新手先讀：這篇在講什麼",
        "\n\n" + contract + "\n\n## 新手先讀：這篇在講什麼",
        1,
    )


def topic_text_v3_with_comparisons(comparability="directly_comparable"):
    text = topic_text_v3().replace(
        "cross_company_numbers: false", "cross_company_numbers: true", 1)
    text = text.replace(
        "supporting_source_ids: S1\n", "supporting_source_ids: S1,S2\n", 1)
    common = [
        ("comparison_id", "M1"),
        ("claim_id", "C1"),
        ("metric", "自由現金流"),
        ("period_start", "2026-04-01"),
        ("period_end", "2026-06-30"),
        ("period_basis", "quarter"),
        ("unit", "USD_billion"),
        ("definition_key", "ocf_less_cash_ppe"),
        ("definition", "營業現金流減現金購置不動產廠房設備"),
        ("comparability", comparability),
        ("comparability_reason", "期間、單位與公式已逐項核對"),
    ]
    normalized = ([
        ("normalization_method", "換算為同期間與十億美元"),
        ("normalized_value", "19.6"),
        ("normalized_unit", "USD_billion"),
        ("normalized_period_start", "2026-04-01"),
        ("normalized_period_end", "2026-06-30"),
        ("normalized_definition_key", "normalized_free_cash_flow"),
    ] if comparability == "normalized_comparable" else [])
    first = _contract_block("metric_comparison", [
        common[0],
        ("observation_id", "M1-O1"),
        common[1],
        ("entity", "甲公司"),
        common[2],
        ("reported_value", "19.6"),
        *common[3:],
        ("evidence_ids", "S1"),
        *normalized,
    ])
    normalized_second = ([
        ("normalization_method", "換算為同期間與十億美元"),
        ("normalized_value", "18.2"),
        ("normalized_unit", "USD_billion"),
        ("normalized_period_start", "2026-04-01"),
        ("normalized_period_end", "2026-06-30"),
        ("normalized_definition_key", "normalized_free_cash_flow"),
    ] if comparability == "normalized_comparable" else [])
    second = _contract_block("metric_comparison", [
        common[0],
        ("observation_id", "M1-O2"),
        common[1],
        ("entity", "乙公司"),
        common[2],
        ("reported_value", "18.2"),
        *common[3:],
        ("evidence_ids", "S2"),
        *normalized_second,
    ])
    text = text.replace(
        "<!-- monitoring_item", first + "\n\n" + second + "\n\n<!-- monitoring_item", 1)
    return text.replace(
        "## 來源與證據邊界",
        "對應比較帳本 `M1`。\n\n## 來源與證據邊界",
        1,
    )


class ResearchTopicContractTest(unittest.TestCase):
    def setUp(self):
        self.universe = [
            {"stock_id": "1234", "name": "甲", "group": "serverodm", "biz": "x"},
            {"stock_id": "5678", "name": "乙", "group": "pcb", "biz": "y"},
        ]
        self.reports = {
            "1234": {"hypotheses": [{"id": "H1"}]},
            "5678": {"hypotheses": [{"id": "H1"}]},
        }

    def test_valid_topic_preserves_candidate_boundary_and_routes_to_known_stock(self):
        info = rq.analyse_topic(
            "topic.md", topic_text(), self.universe, {"serverodm", "pcb"}, self.reports)
        self.assertFalse(info["quality_invalid"], info["quality_errors"])
        self.assertEqual(info["stock_ids"], ["1234"])
        self.assertEqual(info["impacts"][0]["hypothesis_refs"], ["1234:H1"])
        self.assertEqual(info["status"], "triaged")

    def test_valid_schema_v2_requires_substantive_beginner_guide_and_builds_summary(self):
        info = rq.analyse_topic(
            "topic.md", topic_text_v2(), self.universe,
            {"serverodm", "pcb"}, self.reports)
        self.assertFalse(info["quality_invalid"], info["quality_errors"])
        self.assertIn("第一句", info["summary"])
        self.assertIn("第三句", info["summary"])

    def test_schema_v2_rejects_missing_or_underfilled_beginner_content(self):
        text = topic_text_v2().replace("### 想一想", "### 延伸思考")
        text = text.replace(
            "- 這是第三句提醒讀者等待公司正式文件與可觀察數字再做判斷。\n", "")
        info = rq.analyse_topic(
            "topic.md", text, self.universe, {"serverodm", "pcb"}, self.reports)
        self.assertTrue(any("想一想" in error for error in info["quality_errors"]))
        self.assertIn("三句話抓重點必須恰好有 3 個頂層 bullet", info["quality_errors"])

    def test_schema_v1_and_v2_are_grandfathered_but_cutover_requires_v3(self):
        legacy = rq.analyse_topic(
            "legacy.md", topic_text(), self.universe,
            {"serverodm", "pcb"}, self.reports)
        self.assertFalse(legacy["quality_invalid"], legacy["quality_errors"])

        legacy_v2 = rq.analyse_topic(
            "legacy-v2.md", topic_text_v2(), self.universe,
            {"serverodm", "pcb"}, self.reports)
        self.assertFalse(legacy_v2["quality_invalid"], legacy_v2["quality_errors"])

        for version, source in (("1", topic_text()), ("2", topic_text_v2())):
            with self.subTest(version=version):
                new_text = source.replace(
                    "captured_at: 2026-07-27", "captured_at: 2026-08-02")
                new_text = new_text.replace(
                    "last_reviewed_at: 2026-07-27", "last_reviewed_at: 2026-08-02")
                info = rq.analyse_topic(
                    "new.md", new_text, self.universe,
                    {"serverodm", "pcb"}, self.reports)
                self.assertTrue(any(
                    "schema_version: 3" in error for error in info["quality_errors"]))

    def test_stock_group_mismatch_is_rejected(self):
        info = rq.analyse_topic(
            "topic.md", topic_text(group_id="pcb"),
            self.universe, {"serverodm", "pcb"}, self.reports)
        self.assertTrue(any("實際屬 serverodm" in error for error in info["quality_errors"]))

    def test_meta_must_declare_every_impact_stock_and_group(self):
        text = topic_text().replace("stock_ids: 1234", "stock_ids:", 1)
        text = text.replace("group_ids: serverodm", "group_ids:", 1)
        info = rq.analyse_topic(
            "topic.md", text, self.universe, {"serverodm", "pcb"}, self.reports)
        self.assertIn(
            "meta stock_ids 必須等於所有 impact stock_ids 聯集",
            info["quality_errors"])
        self.assertIn(
            "meta group_ids 必須等於所有 impact group_id 聯集",
            info["quality_errors"])

    def test_broken_transition_chain_is_rejected(self):
        text = topic_text().replace("from: inbox", "from: initial", 1)
        info = rq.analyse_topic(
            "topic.md", text, self.universe, {"serverodm", "pcb"}, self.reports)
        self.assertTrue(any("未銜接上一狀態" in error for error in info["quality_errors"]))


class ResearchTopicSchemaV3ContractTest(unittest.TestCase):
    def setUp(self):
        self.universe = [
            {"stock_id": "1234", "name": "甲", "group": "serverodm", "biz": "x"},
            {"stock_id": "5678", "name": "乙", "group": "pcb", "biz": "y"},
        ]
        self.reports = {
            "1234": {"hypotheses": [{"id": "H1"}]},
            "5678": {"hypotheses": [{"id": "H1"}]},
        }

    def analyse(self, text, as_of=date(2026, 8, 3)):
        return rq.analyse_topic(
            "topic-v3.md", text, self.universe,
            {"serverodm", "pcb"}, self.reports, as_of=as_of)

    def assert_error_contains(self, info, fragment):
        self.assertTrue(
            any(fragment in error for error in info["quality_errors"]),
            f"找不到 {fragment!r}；實際 errors={info['quality_errors']}",
        )

    def test_valid_v3_inherits_beginner_contract_and_derives_ledger_state(self):
        info = self.analyse(topic_text_v3())
        self.assertFalse(info["quality_invalid"], info["quality_errors"])
        self.assertIn("第一句", info["summary"])
        self.assertEqual(
            {claim["label"] for claim in info["claims"]},
            {"verified", "unverified"},
        )
        self.assertEqual(info["last_evidence_at"], "2026-07-27")
        self.assertEqual(info["confidence"]["effective"], "high")
        self.assertEqual(len(info["monitoring"]), 2)

    def test_v3_strict_blocks_reject_unknown_duplicate_key_and_duplicate_id(self):
        cases = [
            (
                topic_text_v3().replace(
                    "role: company_release", "role: company_release\nunknown_role_note: x", 1),
                "含未知欄位:unknown_role_note",
            ),
            (
                topic_text_v3().replace(
                    "role: company_release", "role: company_release\nrole: media", 1),
                "欄位重複:role",
            ),
            (
                topic_text_v3().replace("source_id: S2", "source_id: S1", 1),
                "source_id 重複:S1",
            ),
        ]
        for text, expected in cases:
            with self.subTest(expected=expected):
                self.assert_error_contains(self.analyse(text), expected)

    def test_duplicate_schema_version_cannot_downgrade_v3_contract(self):
        text = topic_text_v3().replace(
            "schema_version: 3", "schema_version: 3\nschema_version: 2", 1)
        info = self.analyse(text)
        self.assert_error_contains(info, "schema_version 必須且只能出現一次")
        self.assertEqual(info["meta"]["schema_version"], "3")
        self.assertEqual(len(info["sources"]), 3)

    def test_live_loader_rejects_backdated_legacy_topic(self):
        with mock.patch.object(rq.glob, "glob", return_value=["legacy.md"]):
            with mock.patch.object(rq.os.path, "isdir", return_value=True):
                with mock.patch("builtins.open", mock.mock_open(read_data=topic_text())):
                    topics = rq.load_topics(
                        "topics", self.universe, {"serverodm", "pcb"}, self.reports,
                        as_of=date(2026, 8, 3),
                    )
        self.assert_error_contains(topics[0], "live research register 僅接受")

    def test_source_dates_status_and_references_are_enforced(self):
        cases = [
            (
                topic_text_v3().replace(
                    "title: 甲平台產品公告\npublished_at: 2026-07-26",
                    "title: 甲平台產品公告\npublished_at: 2026-07-28",
                    1,
                ),
                "日期必須符合 published_at <= captured_at",
            ),
            (
                topic_text_v3().replace("status: active", "status: rejected", 1),
                "引用非 active source:S1",
            ),
            (
                topic_text_v3().replace(
                    "supporting_source_ids: S1", "supporting_source_ids: S99", 1),
                "找不到 source id:S99",
            ),
            (
                topic_text_v3().replace(
                    "accepted_at: 2026-07-27", "accepted_at: 2026-07-28", 1),
                "衍生 last_evidence_at 不可晚於 last_reviewed_at",
            ),
        ]
        for text, expected in cases:
            with self.subTest(expected=expected):
                self.assert_error_contains(self.analyse(text), expected)

    def test_living_index_uses_capture_date_without_fake_publication_date(self):
        text = topic_text_v3().replace(
            "role: company_release\npublisher: 甲平台",
            "role: company_release\nsource_kind: living_index\npublisher: 甲平台",
            1,
        ).replace(
            "title: 甲平台產品公告\npublished_at: 2026-07-26",
            "title: 甲平台產品公告\npublished_at:",
            1,
        )
        info = self.analyse(text)
        self.assertFalse(info["quality_invalid"], info["quality_errors"])
        self.assertEqual(info["sources"][0]["source_kind"], "living_index")

        missing = topic_text_v3().replace(
            "title: 甲平台產品公告\npublished_at: 2026-07-26",
            "title: 甲平台產品公告\npublished_at:",
            1,
        )
        self.assert_error_contains(self.analyse(missing), "document 缺少必填欄位:published_at")

        dated_index = topic_text_v3().replace(
            "title: 公司申報查詢入口\npublished_at:",
            "title: 公司申報查詢入口\npublished_at: 2026-07-27",
            1,
        )
        self.assert_error_contains(
            self.analyse(dated_index), "living_index 的 published_at 必須留空")

    def test_historical_dates_cannot_be_in_the_future(self):
        cases = [
            topic_text_v3().replace(
                "accepted_at: 2026-07-27", "accepted_at: 2026-08-04", 1),
            topic_text_v3().replace(
                "as_of: 2026-07-27", "as_of: 2026-08-04", 1),
            topic_text_v3().replace(
                "schema_migrated_at: 2026-07-27", "schema_migrated_at: 2026-08-04", 1),
            topic_text_v3().replace(
                "date: 2026-07-27", "date: 2026-08-04", 1),
        ]
        for text in cases:
            with self.subTest(text=text[:80]):
                self.assert_error_contains(
                    self.analyse(text, as_of=date(2026, 8, 3)),
                    "晚於研究判定日",
                )

    def test_verified_and_inference_claims_require_active_support(self):
        verified = topic_text_v3().replace(
            "supporting_source_ids: S1", "supporting_source_ids:", 1)
        self.assert_error_contains(self.analyse(verified), "至少需要一個 evidence/source id")

        inference = _contract_block("research_claim", [
            ("claim_id", "C3"),
            ("label", "inference"),
            ("status", "active"),
            ("claim", "需求可能先傳到伺服器組裝環節"),
            ("supporting_source_ids", ""),
            ("contrary_source_ids", ""),
            ("as_of", "2026-07-27"),
            ("basis", "由平台量產事件推導"),
            ("boundary", "尚無公司訂單或收入"),
            ("verification_needed", "公司正式揭露"),
            ("resolution", ""),
        ])
        text = topic_text_v3().replace(
            "<!-- monitoring_item", inference + "\n\n<!-- monitoring_item", 1)
        self.assert_error_contains(self.analyse(text), "research_claim 3 至少需要一個")

    def test_unverified_claim_requires_verification_needed(self):
        text = topic_text_v3().replace(
            "verification_needed: 公司法說、財報與客戶交叉文件",
            "verification_needed:",
            1,
        )
        self.assert_error_contains(self.analyse(text), "待驗證 claim 必須填 verification_needed")

    def test_verified_claim_with_contrary_source_requires_resolution(self):
        text = topic_text_v3().replace(
            "contrary_source_ids:", "contrary_source_ids: S2", 1)
        self.assert_error_contains(self.analyse(text), "有 contrary source 時必須填 resolution")

    def test_thesis_must_be_active_and_cannot_be_unverified(self):
        unverified = topic_text_v3().replace("thesis_claim_id: C1", "thesis_claim_id: C2", 1)
        self.assert_error_contains(
            self.analyse(unverified), "thesis_claim_id 不可指向 unverified claim")

        historical = topic_text_v3().replace(
            "label: verified\nstatus: active",
            "label: verified\nstatus: superseded",
            1,
        ).replace("resolution:\n-->", "resolution: superseded_by:C2\n-->", 1)
        self.assert_error_contains(
            self.analyse(historical), "thesis_claim_id 必須指向 active claim")

    def test_peripheral_claim_evidence_does_not_refresh_thesis_clock(self):
        source = _contract_block("research_source", [
            ("source_id", "S3"),
            ("role", "competitor_primary"),
            ("publisher", "丙同業"),
            ("title", "丙同業反方公告"),
            ("published_at", "2026-07-28"),
            ("captured_at", "2026-07-29"),
            ("accepted_at", "2026-07-29"),
            ("status", "active"),
            ("url", "https://third.example.net/release"),
            ("locator", "反方證據段落"),
            ("limitation", "只更新周邊供應商映射"),
        ])
        text = topic_text_v3().replace(
            "last_reviewed_at: 2026-07-27", "last_reviewed_at: 2026-07-29", 1)
        text = text.replace("<!-- research_claim", source + "\n\n<!-- research_claim", 1)
        text = text.replace("contrary_source_ids: S2", "contrary_source_ids: S2,S3", 1)
        text = text.replace(
            "claim: 台灣供應商可能取得可量化新增訂單\n"
            "supporting_source_ids: \ncontrary_source_ids: S2,S3\nas_of: 2026-07-27",
            "claim: 台灣供應商可能取得可量化新增訂單\n"
            "supporting_source_ids: \ncontrary_source_ids: S2,S3\nas_of: 2026-07-29",
            1,
        )
        info = self.analyse(text, as_of=date(2026, 8, 3))
        self.assertFalse(info["quality_invalid"], info["quality_errors"])
        self.assertEqual(info["last_evidence_at"], "2026-07-27")
        self.assertEqual(info["ledger_last_evidence_at"], "2026-07-29")

    def test_append_only_correction_can_retire_claim_source_and_monitor(self):
        source = _contract_block("research_source", [
            ("source_id", "S3"),
            ("role", "company_release"),
            ("publisher", "甲平台"),
            ("title", "甲平台修正公告"),
            ("published_at", "2026-07-28"),
            ("captured_at", "2026-07-28"),
            ("accepted_at", "2026-07-28"),
            ("status", "active"),
            ("url", "https://ir.example.com/correction"),
            ("locator", "修正後產品進度段落"),
            ("limitation", "仍未提供供應商收入"),
        ])
        corrected_claim = _contract_block("research_claim", [
            ("claim_id", "C3"),
            ("label", "verified"),
            ("status", "active"),
            ("claim", "甲平台已撤回原量產時程並發布修正日期"),
            ("supporting_source_ids", "S2,S3"),
            ("contrary_source_ids", ""),
            ("as_of", "2026-07-28"),
            ("basis", "correction_of:C1；修正公告直接改寫舊時程"),
            ("boundary", "只證明公司修正，不推導供應商收入"),
            ("verification_needed", ""),
            ("resolution", ""),
            ("correction_kind", "supersedes"),
            ("corrects_claim_id", "C1"),
            ("corrected_by_claim_id", ""),
        ])
        new_monitor = _contract_block("monitoring_item", [
            ("monitor_id", "T3"),
            ("status", "active"),
            ("claim_ids", "C3"),
            ("metric", "修正後部署與出貨節點"),
            ("source_ids", "S2,S3"),
            ("watch_source_ids", "S9"),
            ("frequency", "event_driven"),
            ("next_check", "2026-08-03"),
            ("trigger", "發布修正後可核對部署數量"),
            ("invalidation", "再次撤回或取消產品"),
        ])
        transition = _contract_block("transition", [
            ("date", "2026-07-28"),
            ("from", "triaged"),
            ("to", "triaged"),
            ("reason", "source_correction_recorded"),
            ("evidence", "sources:S3"),
        ])
        text = topic_text_v3().replace("thesis_claim_id: C1", "thesis_claim_id: C3", 1)
        text = text.replace(
            "last_reviewed_at: 2026-07-27", "last_reviewed_at: 2026-07-28", 1)
        text = text.replace("status: active", "status: superseded", 1)
        text = text.replace(
            "label: verified\nstatus: active",
            "label: verified\nstatus: superseded",
            1,
        ).replace(
            "corrected_by_claim_id: \n-->",
            "corrected_by_claim_id: C3\n-->",
            1,
        )
        text = text.replace("<!-- research_source", transition + "\n\n<!-- research_source", 1)
        text = text.replace("<!-- research_claim", source + "\n\n<!-- research_claim", 1)
        text = text.replace(
            "<!-- monitoring_item", corrected_claim + "\n\n" + new_monitor
            + "\n\n<!-- monitoring_item", 1)
        text = text.replace(
            "monitor_id: T1\nstatus: active",
            "monitor_id: T1\nstatus: retired\nretired_at: 2026-07-28\n"
            "retirement_reason: 原時程已由 C3 取代",
            1,
        )
        info = self.analyse(text, as_of=date(2026, 8, 3))
        self.assertFalse(info["quality_invalid"], info["quality_errors"])
        self.assertEqual(info["last_evidence_at"], "2026-07-28")
        self.assertEqual(
            {item["monitor_id"] for item in info["monitoring"] if item["status"] == "active"},
            {"T2", "T3"},
        )

        broken = text.replace("corrects_claim_id: C1", "corrects_claim_id: C9", 1)
        self.assert_error_contains(self.analyse(broken), "corrects_claim_id 找不到:C9")

        broken_transition = text.replace("evidence: sources:S3", "evidence: sources:S99", 1)
        self.assert_error_contains(
            self.analyse(broken_transition), "evidence 找不到 source:S99")

        second_source = _contract_block("research_source", [
            ("source_id", "S4"),
            ("role", "company_release"),
            ("publisher", "甲平台"),
            ("title", "甲平台第二次修正公告"),
            ("published_at", "2026-07-29"),
            ("captured_at", "2026-07-29"),
            ("accepted_at", "2026-07-29"),
            ("status", "active"),
            ("url", "https://ir.example.com/second-correction"),
            ("locator", "第二次修正日期"),
            ("limitation", "仍未提供供應商收入"),
        ])
        second_claim = _contract_block("research_claim", [
            ("claim_id", "C4"),
            ("label", "verified"),
            ("status", "active"),
            ("claim", "甲平台再次修正部署日期"),
            ("supporting_source_ids", "S2,S4"),
            ("contrary_source_ids", ""),
            ("as_of", "2026-07-29"),
            ("basis", "correction_of:C3；第二次公告直接修正前版"),
            ("boundary", "只證明第二次修正"),
            ("verification_needed", ""),
            ("resolution", ""),
            ("correction_kind", "supersedes"),
            ("corrects_claim_id", "C3"),
            ("corrected_by_claim_id", ""),
        ])
        second_monitor = _contract_block("monitoring_item", [
            ("monitor_id", "T4"),
            ("status", "active"),
            ("claim_ids", "C4"),
            ("metric", "第二次修正後的部署節點"),
            ("source_ids", "S2,S4"),
            ("watch_source_ids", "S9"),
            ("frequency", "event_driven"),
            ("next_check", "2026-08-03"),
            ("trigger", "公布可核對部署數量"),
            ("invalidation", "再次撤回或取消產品"),
        ])
        second_transition = _contract_block("transition", [
            ("date", "2026-07-29"),
            ("from", "triaged"),
            ("to", "triaged"),
            ("reason", "second_source_correction_recorded"),
            ("evidence", "sources:S4"),
        ])
        twice = text.replace("thesis_claim_id: C3", "thesis_claim_id: C4", 1)
        twice = twice.replace(
            "last_reviewed_at: 2026-07-28", "last_reviewed_at: 2026-07-29", 1)
        twice = twice.replace(
            "claim_id: C3\nlabel: verified\nstatus: active",
            "claim_id: C3\nlabel: verified\nstatus: superseded",
            1,
        ).replace(
            "corrects_claim_id: C1\ncorrected_by_claim_id:",
            "corrects_claim_id: C1\ncorrected_by_claim_id: C4",
            1,
        )
        twice = twice.replace(
            "monitor_id: T3\nstatus: active",
            "monitor_id: T3\nstatus: retired\nretired_at: 2026-07-29\n"
            "retirement_reason: 第二次修正已取代節點",
            1,
        )
        twice = twice.replace(
            "<!-- research_source", second_transition + "\n\n<!-- research_source", 1)
        twice = twice.replace(
            "<!-- research_claim", second_source + "\n\n<!-- research_claim", 1)
        twice = twice.replace(
            "<!-- monitoring_item", second_claim + "\n\n" + second_monitor
            + "\n\n<!-- monitoring_item", 1)
        twice_info = self.analyse(twice, as_of=date(2026, 8, 3))
        self.assertFalse(twice_info["quality_invalid"], twice_info["quality_errors"])
        self.assertEqual(rq.audit_topic_history(text, twice), [])

    def test_source_identity_claim_cutoff_and_monitor_cadence_are_enforced(self):
        duplicate = topic_text_v3().replace(
            "https://competitor.example.org/release", "https://ir.example.com/news", 1)
        self.assert_error_contains(self.analyse(duplicate), "不可重複使用同一 URL")

        fragment_duplicate = topic_text_v3().replace(
            "https://competitor.example.org/release",
            "https://IR.EXAMPLE.com:443/news#copy",
            1,
        )
        self.assert_error_contains(
            self.analyse(fragment_duplicate), "不可重複使用同一 URL")

        media_only = topic_text_v3().replace(
            "role: company_release", "role: media", 1).replace(
                "role: competitor_primary", "role: media", 1)
        self.assert_error_contains(
            self.analyse(media_only),
            "verified 不可只由 media／market_estimate 支持",
        )

        early_claim = topic_text_v3().replace("as_of: 2026-07-27", "as_of: 2026-07-25", 1)
        self.assert_error_contains(early_claim_info := self.analyse(early_claim), "as_of 早於引用來源")
        self.assertTrue(early_claim_info["quality_invalid"])

        never = topic_text_v3().replace("frequency: quarterly", "frequency: never", 1)
        self.assert_error_contains(self.analyse(never), "frequency 不在值域:never")

    def test_transition_evidence_is_strict_source_bound_and_chronological(self):
        invalid_initial = topic_text_v3().replace(
            "evidence: source_chain:example-20260726",
            "evidence: source_chain:another-chain",
            1,
        )
        self.assert_error_contains(
            self.analyse(invalid_initial),
            "initial evidence 必須等於 source_chain:example-20260726",
        )

        for evidence in ("none", "source:S1", "source_chain:example-20260726"):
            with self.subTest(evidence=evidence):
                invalid_revision = topic_text_v3().replace(
                    "evidence: sources:S1,S2", f"evidence: {evidence}", 1)
                self.assert_error_contains(
                    self.analyse(invalid_revision),
                    "evidence 必須使用 sources:S1[,S2...]",
                )

        unknown = topic_text_v3().replace(
            "evidence: sources:S1,S2", "evidence: sources:S1,S99", 1)
        self.assert_error_contains(
            self.analyse(unknown), "evidence 找不到 source:S99")

        accepted_later = topic_text_v3().replace(
            "accepted_at: 2026-07-27", "accepted_at: 2026-07-28", 1)
        accepted_later = accepted_later.replace(
            "last_reviewed_at: 2026-07-27", "last_reviewed_at: 2026-07-28", 1)
        self.assert_error_contains(
            self.analyse(accepted_later),
            "日期早於 evidence S1 accepted_at",
        )

    def test_history_audit_allows_append_and_lifecycle_but_rejects_rewrites(self):
        old = topic_text_v3()
        self.assertEqual(rq.audit_topic_history(topic_text_v2(), old), [])

        appended = old.replace(
            "## 來源與證據邊界", "新增正文說明。\n\n## 來源與證據邊界", 1)
        self.assertEqual(rq.audit_topic_history(old, appended), [])

        added_impact = _contract_block("impact", [
            ("group_id", "serverodm"),
            ("stock_ids", "1234"),
            ("direction", "mixed"),
            ("hypothesis_refs", "1234:H1"),
            ("note_action", "none"),
            ("action_due", ""),
            ("rationale", "保留原路由並追加第二個觀察角度"),
            ("evidence_boundary", "新增路由不改寫既有判定"),
        ])
        appended_impact = old.replace(
            "<!-- research_source", added_impact + "\n\n<!-- research_source", 1)
        self.assertEqual(rq.audit_topic_history(old, appended_impact), [])

        prose_rewrite = old.replace(
            "這是第一句足以讓新手理解事件本身的完整重點摘要。",
            "完全不同且可能與帳本相反的新市場斷言，但格式仍可通過。",
            1,
        )
        self.assertTrue(any(
            "歷史可見正文不可靜默改寫" in error
            for error in rq.audit_topic_history(old, prose_rewrite)))

        signed_old = old.replace(
            "這是第一句足以讓新手理解事件本身的完整重點摘要。",
            "這是第一句，觀測值為 -44.66 億元。",
            1,
        )
        sign_rewrite = signed_old.replace("-44.66", "44.66", 1)
        self.assertTrue(any(
            "歷史可見正文不可靜默改寫" in error
            for error in rq.audit_topic_history(signed_old, sign_rewrite)))

        impact_rewrite = old.replace(
            "direction: uncertain", "direction: tailwind", 1).replace(
                "note_action: watch", "note_action: update_required", 1)
        self.assertTrue(any(
            "歷史 impact 不可靜默改寫" in error
            for error in rq.audit_topic_history(old, impact_rewrite)))

        revision = _contract_block("transition", [
            ("date", "2026-07-28"),
            ("from", "triaged"),
            ("to", "triaged"),
            ("reason", "visible_research_revised"),
            ("evidence", "sources:S1"),
        ])
        revised_with_evidence = prose_rewrite.replace(
            "<!-- research_source", revision + "\n\n<!-- research_source", 1)
        revised_info = self.analyse(revised_with_evidence)
        self.assertFalse(
            revised_info["quality_invalid"], revised_info["quality_errors"],
        )
        self.assertEqual(rq.audit_topic_history(old, revised_with_evidence), [])

        impact_with_evidence = impact_rewrite.replace(
            "<!-- research_source", revision + "\n\n<!-- research_source", 1)
        impact_info = self.analyse(impact_with_evidence)
        self.assertFalse(
            impact_info["quality_invalid"], impact_info["quality_errors"],
        )
        self.assertEqual(rq.audit_topic_history(old, impact_with_evidence), [])

        arbitrary_revision = _contract_block("transition", [
            ("date", "2026-07-28"),
            ("from", "triaged"),
            ("to", "triaged"),
            ("reason", "priority_revised"),
            ("evidence", "none"),
        ])
        arbitrary_meta = old.replace("priority: p1", "priority: p0", 1).replace(
            "<!-- research_source", arbitrary_revision + "\n\n<!-- research_source", 1)
        self.assert_error_contains(
            self.analyse(arbitrary_meta),
            "evidence 必須使用 sources:S1[,S2...]",
        )
        self.assertTrue(any(
            "meta 變更必須追加綁定 sources" in error
            for error in rq.audit_topic_history(old, arbitrary_meta)))

        rewritten = old.replace("accepted_at: 2026-07-27", "accepted_at: 2026-07-28", 1)
        self.assertTrue(any(
            "immutable 欄位被改寫:accepted_at" in error
            for error in rq.audit_topic_history(old, rewritten)))

        deleted = old.replace("<!-- research_claim", "<!-- removed_claim", 1)
        self.assertTrue(any(
            "歷史 claim ID 不可刪除:C1" in error
            for error in rq.audit_topic_history(old, deleted)))

        reordered = old.replace(
            "reason: initial_capture", "reason: rewritten_history", 1)
        self.assertIn(
            "既有 transition 不可刪除、重排或改寫；只能在尾端追加",
            rq.audit_topic_history(old, reordered),
        )

        identity_rewrite = old.replace(
            "topic_id: MI-2026-07-27-TEST",
            "topic_id: MI-2026-07-27-RENAMED",
            1,
        )
        self.assertTrue(any(
            "immutable 欄位被改寫:topic_id" in error
            for error in rq.audit_topic_history(old, identity_rewrite)))

        comparison_old = topic_text_v3_with_comparisons()
        comparison_rewrite = comparison_old.replace(
            "reported_value: 19.6", "reported_value: 999.9", 1)
        self.assertTrue(any(
            "歷史 comparison M1-O1 immutable 欄位被改寫:reported_value" in error
            for error in rq.audit_topic_history(comparison_old, comparison_rewrite)))

    def test_history_audit_rejects_deadline_rollover_without_new_thesis_evidence(self):
        old = topic_text_v3()
        rollover = old.replace(
            "last_reviewed_at: 2026-07-27", "last_reviewed_at: 2026-08-03", 1)
        rollover = rollover.replace("review_due: 2026-08-03", "review_due: 2026-09-03", 1)
        rollover = rollover.replace("next_check: 2026-08-03", "next_check: 2026-09-03", 1)
        rollover = rollover.replace("next_check: 2026-08-10", "next_check: 2026-09-10", 1)
        revision = _contract_block("transition", [
            ("date", "2026-08-03"),
            ("from", "triaged"),
            ("to", "triaged"),
            ("reason", "reviewed_without_new_evidence"),
            ("evidence", "sources:S1"),
        ])
        rollover = rollover.replace(
            "<!-- research_source", revision + "\n\n<!-- research_source", 1)
        errors = rq.audit_topic_history(old, rollover)
        self.assertTrue(any("不得刷新:last_reviewed_at,review_due" in error for error in errors))

    def test_history_audit_allows_same_day_thesis_correction_without_clock_refresh(self):
        old = topic_text_v3()
        source = _contract_block("research_source", [
            ("source_id", "S3"),
            ("role", "competitor_primary"),
            ("source_kind", "document"),
            ("publisher", "丙同業"),
            ("title", "同日發布的架構修正證據"),
            ("published_at", "2026-07-27"),
            ("captured_at", "2026-07-27"),
            ("accepted_at", "2026-07-27"),
            ("status", "active"),
            ("url", "https://third.example.com/correction"),
            ("locator", "架構分流段落"),
            ("limitation", "只修正技術分工，不支持收入"),
        ])
        claim = _contract_block("research_claim", [
            ("claim_id", "C3"),
            ("label", "verified"),
            ("status", "active"),
            ("claim", "新證據顯示原量產主張必須縮窄為特定產品"),
            ("supporting_source_ids", "S1,S3"),
            ("contrary_source_ids", ""),
            ("as_of", "2026-07-27"),
            ("basis", "correction_of:C1；同日新來源縮窄原主張"),
            ("boundary", "不延後期限、不提高信心，也不推導收入"),
            ("verification_needed", ""),
            ("resolution", ""),
            ("correction_kind", "supersedes"),
            ("corrects_claim_id", "C1"),
            ("corrected_by_claim_id", ""),
        ])
        transition = _contract_block("transition", [
            ("date", "2026-07-27"),
            ("from", "triaged"),
            ("to", "triaged"),
            ("reason", "same_day_thesis_correction"),
            ("evidence", "sources:S3"),
        ])
        revised = old.replace("thesis_claim_id: C1", "thesis_claim_id: C3", 1)
        revised = revised.replace(
            "claim_id: C1\nlabel: verified\nstatus: active",
            "claim_id: C1\nlabel: verified\nstatus: superseded",
            1,
        ).replace(
            "corrects_claim_id: \ncorrected_by_claim_id: \n-->",
            "corrects_claim_id: \ncorrected_by_claim_id: C3\n-->",
            1,
        )
        revised = revised.replace(
            "<!-- research_source", transition + "\n\n<!-- research_source", 1)
        revised = revised.replace(
            "<!-- research_claim", source + "\n\n<!-- research_claim", 1)
        revised = revised.replace(
            "<!-- monitoring_item", claim + "\n\n<!-- monitoring_item", 1)
        self.assertEqual(rq.audit_topic_history(old, revised), [])

    def test_scan_log_history_is_append_only(self):
        header = (
            "scan_id,window_start,window_end,scanned_at,scope,source_domains,"
            "result_topic_ids,next_scan_due,coverage_note\n")
        old = header + "SC-1,2026-07-01,2026-07-31,2026-08-01,full,a.com,,2026-08-08,none\n"
        appended = old + "SC-2,2026-08-01,2026-08-02,2026-08-02,partial,b.com,,2026-08-09,none\n"
        self.assertEqual(rq.audit_scan_log_history(old, appended), [])
        self.assertTrue(any(
            "歷史 scan_id 不可改寫:SC-1" in error
            for error in rq.audit_scan_log_history(
                old, old.replace("2026-08-08", "2026-09-08"))))

    def test_scan_log_same_day_latest_uses_append_order_not_scan_id_sort(self):
        text = (
            "scan_id,window_start,window_end,scanned_at,scope,source_domains,"
            "result_topic_ids,next_scan_due,coverage_note\n"
            "Z-FIRST,2026-08-01,2026-08-02,2026-08-02,partial,a.com,none,"
            "2026-08-08,第一輪\n"
            "A-LAST,2026-08-02,2026-08-02,2026-08-02,partial,b.com,none,"
            "2026-08-09,同日追加的第二輪\n"
        )
        with mock.patch.object(rq.os.path, "exists", return_value=True):
            with mock.patch("builtins.open", mock.mock_open(read_data=text)):
                scan = rq.load_scan_log("scan.csv", as_of=date(2026, 8, 2))
        self.assertFalse(scan["errors"])
        self.assertEqual(scan["latest"]["scan_id"], "A-LAST")

    def test_direct_comparison_requires_a_group_and_matching_dimensions(self):
        valid = self.analyse(topic_text_v3_with_comparisons())
        self.assertFalse(valid["quality_invalid"], valid["quality_errors"])
        self.assertEqual(len(valid["comparisons"]), 2)

        single = topic_text_v3_with_comparisons()
        second_start = single.index("<!-- metric_comparison", single.index("<!-- metric_comparison") + 1)
        second_end = single.index("-->", second_start) + len("-->")
        single = single[:second_start] + single[second_end:]
        self.assert_error_contains(self.analyse(single), "至少需要 2 個不同 entity")

        mismatched = topic_text_v3_with_comparisons().replace(
            "unit: USD_billion", "unit: USD_million", 1)
        self.assert_error_contains(self.analyse(mismatched), "標為可直接比較但 unit 不一致")

        detached = topic_text_v3_with_comparisons().replace(
            "claim_id: C1", "claim_id: C2")
        self.assert_error_contains(
            self.analyse(detached), "未納入關聯 claim 的證據鏈:S1")

    def test_comparison_periods_are_ordered_and_bounded_by_claim_and_research_date(self):
        inverted = topic_text_v3_with_comparisons().replace(
            "period_start: 2026-04-01", "period_start: 2026-07-01")
        self.assert_error_contains(
            self.analyse(inverted), "period_start 不可晚於 period_end")

        after_claim = topic_text_v3_with_comparisons().replace(
            "period_end: 2026-06-30", "period_end: 2026-07-28")
        self.assert_error_contains(
            self.analyse(after_claim),
            "period_end 不可晚於關聯 claim as_of:2026-07-27",
        )

        future = topic_text_v3_with_comparisons().replace(
            "period_end: 2026-06-30", "period_end: 2099-06-30")
        self.assert_error_contains(
            self.analyse(future), "period_end 晚於研究判定日 2026-08-03")

        normalized = topic_text_v3_with_comparisons("normalized_comparable")
        normalized_inverted = normalized.replace(
            "normalized_period_start: 2026-04-01",
            "normalized_period_start: 2026-07-01",
        )
        self.assert_error_contains(
            self.analyse(normalized_inverted),
            "normalized_period_start 不可晚於 normalized_period_end",
        )

        normalized_future = normalized.replace(
            "normalized_period_end: 2026-06-30",
            "normalized_period_end: 2099-06-30",
        )
        self.assert_error_contains(
            self.analyse(normalized_future),
            "normalized_period_end 晚於研究判定日 2026-08-03",
        )

    def test_normalized_comparison_requires_normalization_and_common_unit(self):
        valid_text = topic_text_v3_with_comparisons("normalized_comparable")
        valid = self.analyse(valid_text)
        self.assertFalse(valid["quality_invalid"], valid["quality_errors"])

        missing = valid_text.replace("normalization_method: 換算為同期間與十億美元", "", 1)
        self.assert_error_contains(self.analyse(missing), "缺少必填欄位:normalization_method")

        mismatched = valid_text.replace("normalized_unit: USD_billion", "normalized_unit: USD_million", 1)
        self.assert_error_contains(self.analyse(mismatched), "normalized_unit 必須一致")

    def test_not_comparable_observations_require_reason(self):
        valid_text = topic_text_v3_with_comparisons("not_comparable")
        valid = self.analyse(valid_text)
        self.assertFalse(valid["quality_invalid"], valid["quality_errors"])

        missing = valid_text.replace(
            "comparability_reason: 期間、單位與公式已逐項核對", "comparability_reason:", 1)
        self.assert_error_contains(self.analyse(missing), "缺少必填欄位:comparability_reason")

    def test_heterogeneous_evidence_requires_distinct_metrics_and_not_comparable(self):
        valid_text = topic_text_v3_with_comparisons("not_comparable")
        valid_text = valid_text.replace(
            "comparison_id: M1", "comparison_id: M1\ncomparison_kind: heterogeneous_evidence")
        first = valid_text.find("metric: 自由現金流")
        second = valid_text.find("metric: 自由現金流", first + 1)
        valid_text = (valid_text[:second]
                      + valid_text[second:].replace(
                          "metric: 自由現金流", "metric: 營業利益率", 1))
        valid = self.analyse(valid_text)
        self.assertFalse(valid["quality_invalid"], valid["quality_errors"])

        aligned = valid_text.replace(
            "comparison_kind: heterogeneous_evidence", "comparison_kind: aligned_metric")
        self.assert_error_contains(self.analyse(aligned), "aligned_metric 的 metric 必須一致")

        direct = valid_text.replace("comparability: not_comparable", "comparability: directly_comparable")
        self.assert_error_contains(
            self.analyse(direct), "heterogeneous_evidence 只能標為 not_comparable")

    def test_monitoring_contract_and_review_due_use_earliest_next_check(self):
        missing = topic_text_v3().replace("frequency: quarterly", "frequency:", 1)
        self.assert_error_contains(self.analyse(missing), "缺少必填欄位:frequency")

        wrong_due = topic_text_v3().replace("review_due: 2026-08-03", "review_due: 2026-08-04", 1)
        self.assert_error_contains(
            self.analyse(wrong_due),
            "review_due 必須等於所有 monitoring_item 最早的 next_check",
        )

    def test_confidence_is_current_on_due_date_decays_next_day_and_stops_when_closed(self):
        due = self.analyse(topic_text_v3(), as_of=date(2026, 8, 3))
        self.assertFalse(due["confidence"]["stale"])
        self.assertEqual(due["confidence"]["effective"], "high")
        self.assertEqual(due["confidence"]["last_evidence_at"], "2026-07-27")

        overdue = self.analyse(topic_text_v3(), as_of=date(2026, 8, 4))
        self.assertTrue(overdue["confidence"]["stale"])
        self.assertEqual(overdue["confidence"]["effective"], "medium")
        self.assertEqual(overdue["confidence"]["days_overdue"], 1)

        closed = topic_text_v3().replace("status: triaged", "status: resolved", 1)
        closed_transition = _contract_block("transition", [
            ("date", "2026-07-27"),
            ("from", "triaged"),
            ("to", "resolved"),
            ("reason", "evidence_chain_closed"),
            ("evidence", "sources:S1"),
        ])
        closed = closed.replace(
            "<!-- research_source", closed_transition + "\n\n<!-- research_source", 1)
        closing_claim = _contract_block("research_claim", [
            ("claim_id", "C3"),
            ("label", "verified"),
            ("status", "active"),
            ("claim", "公司文件未支持原先的供應商訂單假設"),
            ("supporting_source_ids", "S1,S2"),
            ("contrary_source_ids", ""),
            ("as_of", "2026-07-27"),
            ("basis", "correction_of:C2；結案時依正式文件裁決"),
            ("boundary", "不代表未來永遠不會出現新訂單"),
            ("verification_needed", ""),
            ("resolution", ""),
            ("correction_kind", "refutes"),
            ("corrects_claim_id", "C2"),
            ("corrected_by_claim_id", ""),
        ])
        closed = closed.replace(
            "claim_id: C2\nlabel: unverified\nstatus: active",
            "claim_id: C2\nlabel: unverified\nstatus: refuted",
            1,
        )
        c2_start = closed.index("claim_id: C2")
        c2_end = closed.index("-->", c2_start)
        c2_block = closed[c2_start:c2_end].replace(
            "corrected_by_claim_id:", "corrected_by_claim_id: C3")
        closed = closed[:c2_start] + c2_block + closed[c2_end:]
        closed = closed.replace(
            "<!-- monitoring_item", closing_claim + "\n\n<!-- monitoring_item", 1)
        closed = closed.replace(
            "status: active\nclaim_ids: C1",
            "status: retired\nretired_at: 2026-07-27\n"
            "retirement_reason: topic resolved\nclaim_ids: C1",
            1,
        ).replace(
            "status: active\nclaim_ids: C2",
            "status: retired\nretired_at: 2026-07-27\n"
            "retirement_reason: topic resolved\nclaim_ids: C2",
            1,
        )
        closed_info = self.analyse(closed, as_of=date(2026, 8, 4))
        self.assertFalse(closed_info["quality_invalid"], closed_info["quality_errors"])
        self.assertFalse(closed_info["confidence"]["stale"])
        self.assertEqual(closed_info["confidence"]["effective"], "high")

    def test_repo_topic_register_and_scan_log_lint(self):
        topics = rq.load_topics(reports=lh.load_reports())
        scan = rq.load_scan_log(topic_ids=[topic["topic_id"] for topic in topics])
        self.assertGreaterEqual(len(topics), 4)
        self.assertIn(
            "MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL",
            {topic["topic_id"] for topic in topics},
        )
        self.assertFalse(any(topic["quality_errors"] for topic in topics))
        self.assertFalse(scan["errors"])
        self.assertEqual(scan["latest"]["scope"], "full")

    def test_scan_log_rejects_empty_id_and_impossible_clock_order(self):
        text = (
            "scan_id,window_start,window_end,scanned_at,scope,source_domains,"
            "result_topic_ids,next_scan_due,coverage_note\n"
            ",2026-07-19,2026-07-27,2026-07-26,partial,example.com,none,"
            "2026-07-25,測試\n"
        )
        with mock.patch.object(rq.os.path, "exists", return_value=True):
            with mock.patch("builtins.open", mock.mock_open(read_data=text)):
                scan = rq.load_scan_log("scan.csv")

        self.assertTrue(any("scan_id 不可空白" in error for error in scan["errors"]))
        self.assertTrue(any("window_end 晚於 scanned_at" in error for error in scan["errors"]))
        self.assertTrue(any("scanned_at 晚於 next_scan_due" in error for error in scan["errors"]))
        self.assertIsNone(scan["latest"])

    def test_scan_log_rejects_future_scan_that_could_hide_due_work(self):
        text = (
            "scan_id,window_start,window_end,scanned_at,scope,source_domains,"
            "result_topic_ids,next_scan_due,coverage_note\n"
            "S1,2026-08-01,2026-08-04,2026-08-04,full,example.com,none,"
            "2026-08-10,未來掃描\n"
        )
        with mock.patch.object(rq.os.path, "exists", return_value=True):
            with mock.patch("builtins.open", mock.mock_open(read_data=text)):
                scan = rq.load_scan_log("scan.csv", as_of=date(2026, 8, 3))
        self.assertTrue(any("晚於研究判定日" in error for error in scan["errors"]))
        self.assertIsNone(scan["latest"])


class ResearchScheduleTest(unittest.TestCase):
    def test_four_cohorts_cover_universe_once_and_are_balanced(self):
        universe = rq._load_universe()
        cohorts = rq.cohort_map(universe)
        flat = [row["stock_id"] for rows in cohorts.values() for row in rows]
        self.assertEqual(len(flat), 121)
        self.assertEqual(len(flat), len(set(flat)))
        self.assertEqual(sorted(map(len, cohorts.values())), [30, 30, 30, 31])
        for group_id in rq._load_groups():
            self.assertTrue(all(
                any(row["group"] == group_id for row in cohorts[label])
                for label in "ABCD"))

    def test_rotation_anchor_starts_with_a(self):
        self.assertEqual(rq.active_cohort(date(2026, 7, 27))[0], "A")
        self.assertEqual(rq.active_cohort(date(2026, 8, 3))[0], "B")

    def test_expected_month_respects_tenth_day_reporting_boundary(self):
        self.assertEqual(rq.expected_revenue_period(date(2026, 7, 10)), (2026, 5))
        self.assertEqual(rq.expected_revenue_period(date(2026, 7, 11)), (2026, 6))

    def test_expected_quarter_follows_filing_deadlines(self):
        self.assertEqual(rq.expected_quarter_date(date(2026, 3, 31)), date(2025, 9, 30))
        self.assertEqual(rq.expected_quarter_date(date(2026, 4, 1)), date(2025, 12, 31))
        self.assertEqual(rq.expected_quarter_date(date(2026, 5, 15)), date(2025, 12, 31))
        self.assertEqual(rq.expected_quarter_date(date(2026, 5, 16)), date(2026, 3, 31))
        self.assertEqual(rq.expected_quarter_date(date(2026, 8, 15)), date(2026, 6, 30))
        self.assertEqual(rq.expected_quarter_date(date(2026, 11, 15)), date(2026, 9, 30))

    def test_topic_priority_is_not_discarded_before_due_date(self):
        as_of = date(2026, 7, 27)
        due = date(2026, 8, 3)
        self.assertEqual(rq._topic_queue_priority("p0", due, as_of), "P0")
        self.assertEqual(rq._topic_queue_priority("p1", due, as_of), "P1")
        self.assertEqual(rq._topic_queue_priority("p2", due, as_of), "P2")
        self.assertEqual(
            rq._topic_queue_priority("p2", date(2026, 7, 26), as_of), "P1")

    def test_research_watch_is_read_only_and_runs_after_financial_fetch(self):
        text = (ROOT / ".github" / "workflows" / "research-watch.yml").read_text(
            encoding="utf-8")
        self.assertIn('cron: "0 1 * * 1"', text)
        self.assertIn('workflows: ["fetch-financials"]', text)
        self.assertIn("python scripts/research_queue.py --attention", text)
        self.assertIn("contents: read", text)
        self.assertNotIn("repo-main-writer", text)
        self.assertNotIn("git add", text)

        quality = (
            ROOT / ".github" / "workflows" / "qualitative-quality.yml"
        ).read_text(encoding="utf-8")
        self.assertIn("python scripts/research_queue.py --lint", quality)
        self.assertIn("fetch-depth: 0", quality)
        self.assertIn("PUSH_BEFORE: ${{ github.event.before }}", quality)
        self.assertIn("PR_BASE: ${{ github.event.pull_request.base.sha }}", quality)
        self.assertIn('--baseline-ref "$baseline"', quality)
        self.assertGreaterEqual(quality.count('"notes/research_topics/**"'), 2)
        self.assertGreaterEqual(quality.count('"tests/test_research_queue.py"'), 2)


class ResearchFinancialCoverageTest(unittest.TestCase):
    def test_financial_snapshot_reports_exact_missing_stock_read_only(self):
        con = sqlite3.connect(":memory:")
        con.row_factory = sqlite3.Row
        con.executescript("""
            CREATE TABLE month_revenue(
              date TEXT, stock_id TEXT, revenue INTEGER,
              revenue_month INTEGER, revenue_year INTEGER);
            CREATE TABLE financials(
              date TEXT, stock_id TEXT, type TEXT, value REAL, origin_name TEXT);
            CREATE TABLE balance_sheet(
              date TEXT, stock_id TEXT, type TEXT, value REAL, origin_name TEXT);
            CREATE TABLE cash_flow(
              date TEXT, stock_id TEXT, type TEXT, value REAL, origin_name TEXT);
        """)
        con.execute(
            "INSERT INTO month_revenue VALUES(?,?,?,?,?)",
            ("2026-07-01", "1234", 1, 6, 2026))
        con.execute(
            "INSERT INTO month_revenue VALUES(?,?,?,?,?)",
            ("2026-07-01", "5678", None, 6, 2026))
        for table in ("financials", "balance_sheet", "cash_flow"):
            con.executemany(
                f"INSERT INTO {table} VALUES(?,?,?,?,?)",
                [
                    ("2026-03-31", "1234", "Revenue", 1.0, "x"),
                    ("2026-03-31", "5678", "Revenue", 1.0, "x"),
                    # 單一早報者不可把其餘 universe 推成新季缺口。
                    ("2026-06-30", "1234", "Revenue", 1.0, "x"),
                ],
            )
        con.commit()
        con.execute("PRAGMA query_only = 1")
        self.assertEqual(con.execute("PRAGMA query_only").fetchone()[0], 1)
        result = rq.financial_snapshot(
            con,
            [
                {"stock_id": "1234", "name": "甲", "group": "serverodm"},
                {"stock_id": "5678", "name": "乙", "group": "pcb"},
            ],
            date(2026, 7, 27),
        )
        con.close()

        self.assertEqual(result["expected_revenue_period"], "2026-06")
        self.assertEqual(result["revenue_missing"], ["5678"])
        self.assertEqual(result["expected_quarter_period"], "2026Q1")
        self.assertEqual(result["common_latest_period"], "2026Q1")
        self.assertTrue(all(
            item["covered"] == 2 for item in result["quarter_tables"].values()))

    def test_whole_batch_lag_cannot_self_report_as_complete(self):
        con = sqlite3.connect(":memory:")
        con.row_factory = sqlite3.Row
        con.executescript("""
            CREATE TABLE month_revenue(
              date TEXT, stock_id TEXT, revenue INTEGER,
              revenue_month INTEGER, revenue_year INTEGER);
            CREATE TABLE financials(
              date TEXT, stock_id TEXT, type TEXT, value REAL, origin_name TEXT);
            CREATE TABLE balance_sheet(
              date TEXT, stock_id TEXT, type TEXT, value REAL, origin_name TEXT);
            CREATE TABLE cash_flow(
              date TEXT, stock_id TEXT, type TEXT, value REAL, origin_name TEXT);
        """)
        for table in ("financials", "balance_sheet", "cash_flow"):
            con.executemany(
                f"INSERT INTO {table} VALUES(?,?,?,?,?)",
                [
                    ("2026-03-31", "1234", "Revenue", 1.0, "x"),
                    ("2026-03-31", "5678", "Revenue", 1.0, "x"),
                ],
            )
        con.commit()
        con.execute("PRAGMA query_only = 1")
        result = rq.financial_snapshot(
            con,
            [
                {"stock_id": "1234", "name": "甲", "group": "serverodm"},
                {"stock_id": "5678", "name": "乙", "group": "pcb"},
            ],
            date(2026, 8, 15),
        )
        con.close()

        self.assertEqual(result["expected_quarter_period"], "2026Q2")
        self.assertIsNone(result["common_latest_period"])
        self.assertTrue(all(
            item["covered"] == 0
            and item["missing"] == ["1234", "5678"]
            for item in result["quarter_tables"].values()))


if __name__ == "__main__":
    unittest.main()
