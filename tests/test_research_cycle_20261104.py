"""November 4: narrow new evidence does not upgrade deployment or funding scope."""
import copy
import unittest

from test_research_cycle_20261012 import ROOT, bd, records
from test_research_cycle_20261019 import keyed
from research_queue import analyse_topic, load_notes, load_reports


HELIOS = "notes/research_topics/2026-08-02_amd_helios_deployment_ladder.md"
AMKOR = "notes/research_topics/2026-08-01_us_advanced_packaging_regionalization.md"
HEL_GRAPH = "notes/knowledge_graph/amd_helios.md"
AMKOR_GRAPH = "notes/knowledge_graph/us_advanced_packaging_regionalization.md"
AS_OF = "2026-11-04"


class ResearchCycleNovember4Test(unittest.TestCase):
    def test_side_evidence_keeps_both_original_thesis_clocks(self):
        for path, expected in [
            (HELIOS, ("C11", "2026-08-12", "2026-08-15")),
            (AMKOR, ("C18", "2026-10-04", "2026-10-31")),
        ]:
            with self.subTest(path=path):
                meta = records(path, "research_topic")[0]
                self.assertEqual(tuple(meta[key] for key in
                                       ("thesis_claim_id", "last_reviewed_at", "review_due")),
                                 expected)
                self.assertEqual(meta["base_confidence"], "medium")

    def test_filing_and_release_dates_are_not_customer_event_dates(self):
        sources = keyed(HELIOS, "research_source", "source_id")
        self.assertEqual(sources["S28"]["published_at"], "2026-11-03")
        self.assertEqual(sources["S29"]["published_at"], AS_OF)
        for sid in ("S28", "S29"):
            self.assertEqual(sources[sid]["accepted_at"], AS_OF)
            self.assertEqual(sources[sid]["independence_group"], "amd")
            self.assertEqual(sources[sid]["source_kind"], "document")
        self.assertIn("公告日不可倒填", sources["S28"]["limitation"])
        amkor = keyed(AMKOR, "research_source", "source_id")["S15"]
        self.assertEqual(amkor["published_at"], "2026-10-27")
        self.assertEqual(amkor["accepted_at"], AS_OF)
        self.assertEqual(amkor["independence_group"], "amkor.com")

    def test_named_workloads_are_one_issuer_statement_not_five_acceptances(self):
        claim = keyed(HELIOS, "research_claim", "claim_id")["C31"]
        self.assertEqual(claim["label"], "verified")
        self.assertEqual(claim["supporting_source_ids"], "S26,S28")
        for name in ("Anthropic", "Meta", "Microsoft", "OpenAI", "OCI"):
            self.assertIn(name, claim["claim"])
        self.assertIn("本次新列 Anthropic", claim["claim"])
        self.assertIn("不把名稱數當獨立驗收樣本", claim["basis"])
        for boundary in ("原首個 GW", "五家全數驗收完成", "GA", "公告日期替代事件發生日"):
            self.assertIn(boundary, claim["boundary"])

    def test_helios_responsibilities_are_not_actual_shortages(self):
        claim = keyed(HELIOS, "research_claim", "claim_id")["C32"]
        self.assertEqual((claim["label"], claim["supporting_source_ids"]), ("verified", "S29"))
        for role in ("開發並授權", "供應部分產品", "不製造或出售完整 Helios 機櫃", "部分網路"):
            self.assertIn(role, claim["claim"])
        self.assertIn("不是已發生短缺或延誤", claim["boundary"])
        self.assertIn("不代表 AMD 不供應任何網路產品", claim["boundary"])

    def test_data_center_quarter_is_not_helios_financial_denominator(self):
        claim = keyed(HELIOS, "research_claim", "claim_id")["C33"]
        for value in ("2026-09-26", "三個月", "8546 百萬美元", "伺服器 CPU", "並非 Helios 專屬收入"):
            self.assertIn(value, claim["claim"])
        self.assertIn("three months 與 nine months", claim["basis"])
        self.assertIn("不把整個分部", claim["boundary"])
        self.assertIn("台灣供應商", claim["boundary"])
        self.assertIn("不作跨公司排名", claim["boundary"])

    def test_amkor_construction_cost_is_cumulative_and_not_cash_or_progress_rate(self):
        claim = keyed(AMKOR, "research_claim", "claim_id")["C19"]
        self.assertEqual((claim["label"], claim["supporting_source_ids"]), ("verified", "S15"))
        for value in ("2026-09-30", "5.533億美元", "850萬美元"):
            self.assertIn(value, claim["claim"])
        self.assertIn("非單季支出", claim["basis"])
        for boundary in ("不是同額現金已付", "利息已包含", "未分Phase1／2", "工程完成率"):
            self.assertIn(boundary, claim["boundary"])

    def test_korean_fdi_receipt_does_not_become_arizona_chips_or_profit(self):
        claims = keyed(AMKOR, "research_claim", "claim_id")
        self.assertIn("最高4.07億美元", claims["C20"]["claim"])
        self.assertIn("尚未收到這筆資金", claims["C20"]["claim"])
        self.assertIn("不等補助取消", claims["C20"]["boundary"])
        for value in ("1,500億韓元", "150億韓元", "1,100萬美元", "受限制現金及其他非流動負債"):
            self.assertIn(value, claims["C21"]["claim"])
        for boundary in ("不是Arizona CHIPS", "美元值沿用公司約數", "收入或可自由分配現金", "不與C19工程成本相減"):
            self.assertIn(boundary, claims["C21"]["boundary"])

    def test_new_monitors_are_separate_and_preserve_prior_contract_dates(self):
        hel = keyed(HELIOS, "monitoring_item", "monitor_id")
        amkor = keyed(AMKOR, "monitoring_item", "monitor_id")
        self.assertEqual((hel["T15"]["frequency"], hel["T15"]["next_check"]),
                         ("weekly", "2026-11-11"))
        self.assertEqual(hel["T15"]["claim_ids"], "C31,C32,C33")
        self.assertIn("同一對象", hel["T15"]["trigger"])
        self.assertIn("只有未公開細節不視為反證", hel["T15"]["invalidation"])
        self.assertEqual(hel["T14"]["next_check"], "2026-10-23")
        self.assertEqual((amkor["T9"]["frequency"], amkor["T9"]["next_check"]),
                         ("monthly", "2026-11-30"))
        self.assertEqual(amkor["T9"]["claim_ids"], "C19,C20,C21")
        self.assertIn("按國家、協議、期別與會計欄位分開", amkor["T9"]["frequency_detail"])
        self.assertIn("限制解除", amkor["T9"]["trigger"])
        self.assertIn("同案同期間核對", amkor["T9"]["invalidation"])
        self.assertEqual(amkor["T7"]["next_check"], "2026-10-31")
        self.assertEqual(amkor["T8"]["next_check"], "2026-11-14")

    def test_helios_graph_has_validation_and_role_edges_not_gw_upgrade(self):
        edges = keyed(HEL_GRAPH, "knowledge_edge", "edge_id")
        current = edges["KG-HEL-C16"]
        self.assertTrue(current["claim_refs"].endswith("#C31"))
        self.assertEqual((current["relation"], current["commercial_stage"]), ("tests", "validation"))
        self.assertEqual((current["materiality"], current["exclusivity"]), ("named_product", "unknown"))
        role = edges["KG-HEL-I22"]
        self.assertTrue(role["claim_refs"].endswith("#C32"))
        self.assertEqual(role["commercial_stage"], "integration")
        self.assertIn("不代表已發生短缺延誤", role["boundary"])
        original = edges["KG-HEL-C05"]
        self.assertEqual((original["commercial_stage"], original["as_of"], original["review_due"]),
                         ("planned", "2026-07-21", "2026-08-09"))
        self.assertIn("首個 GW 仍預計 2027H1", original["boundary"])

    def test_amkor_graph_keeps_each_grant_scope_and_adjacent_materiality(self):
        edge = keyed(AMKOR_GRAPH, "knowledge_edge", "edge_id")["KG-UAP-I02"]
        self.assertEqual({ref.rsplit("#", 1)[1] for ref in edge["claim_refs"].split(",")},
                         {"C20", "C21"})
        self.assertEqual((edge["evidence_state"], edge["commercial_stage"], edge["materiality"]),
                         ("verified", "planned", "adjacent"))
        self.assertEqual((edge["as_of"], edge["review_due"]), (AS_OF, "2026-11-30"))
        for boundary in ("不是award取消", "不是Arizona撥款", "公司利潤"):
            self.assertIn(boundary, edge["boundary"])

    def test_beginner_opening_shows_latest_and_preserves_october_comparison(self):
        text = (ROOT / HELIOS).read_text(encoding="utf8")
        opening = text.split("## 新手先讀：這篇在講什麼", 1)[1].split("### 名詞小字典", 1)[0]
        for term in ("11 月的新進度", "11/3", "Anthropic", "相較 10/12", "不是五份獨立客戶驗收"):
            self.assertIn(term, opening)
        self.assertIn("\n\n11/4 季報", opening)
        self.assertIn("11 月新手補充 誰在跑工作 誰在賣整櫃", text)
        self.assertIn("新增 T14 的下一節點是 2026-10-23", text)
        self.assertIn("T15 在 11/11 按週頻回查", text)

    def test_both_evidence_revisions_reach_homepage_without_clock_refresh(self):
        topics = []
        for path in (HELIOS, AMKOR):
            meta = records(path, "research_topic")[0]
            transitions = [row for row in records(path, "transition") if row["date"] <= AS_OF]
            current = [row for row in transitions if row["date"] == AS_OF]
            self.assertEqual(len(current), 1)
            self.assertTrue(current[0]["evidence"].startswith("sources:"))
            topics.append(dict(topic_id=meta["topic_id"], title=meta["topic_id"],
                               relpath=path, meta=meta, transitions=transitions))
        recent = bd.build_recent_articles(AS_OF, {}, {}, topics=topics)
        self.assertEqual({row["researchId"] for row in recent["items"]},
                         {"topic-" + topic["topic_id"] for topic in topics})
        self.assertTrue(all(row["date"] == AS_OF for row in recent["items"]))

    def test_current_trace_replays_work_fixture_but_not_evidence_clock(self):
        # A bounded schedule fixture exercises the renderer without loading live DB,
        # network, ignored capture files, or a future cycle's review ledger.
        reports = load_reports(notes=load_notes())
        for path, earliest in ((HELIOS, "2026-11-06"), (AMKOR, "2026-11-14")):
            with self.subTest(path=path):
                topic = analyse_topic(str(ROOT / path), (ROOT / path).read_text(encoding="utf8"),
                                      reports=reports, as_of=AS_OF)
                self.assertFalse(topic["quality_invalid"], topic["quality_errors"])
                before = copy.deepcopy(topic)
                reviews = []
                for monitor in topic["monitoring"]:
                    if monitor["status"] != "active" or monitor["next_check"] > AS_OF:
                        continue
                    next_check = "2026-11-11" if path == HELIOS else "2026-11-30"
                    if path == HELIOS and monitor["monitor_id"] == "T7":
                        next_check = "2026-11-06"
                    reviews.append(dict(topic_id=topic["topic_id"], monitor_id=monitor["monitor_id"],
                                        checked_at=AS_OF, next_check=next_check,
                                        result="not_yet_testable", claim_action="none",
                                        evidence_source_ids=[]))
                library = bd.build_research_library({}, {}, topics=[topic], as_of=AS_OF,
                                                     monitor_reviews=reviews)
                article = library["articles"][0]
                next_step = article["sections"][0]["blocks"][1]["items"][-1][1]["s"]
                self.assertIn("下次工作回查 " + earliest, next_step)
                self.assertIn("工作日期不代表證據已更新", next_step)
                self.assertEqual(article["confidence"]["last_evidence_at"], topic["last_evidence_at"])
                self.assertLess(article["confidence"]["last_evidence_at"], AS_OF)
                self.assertEqual(article["meta"]["reviewDue"], topic["meta"]["review_due"])
                self.assertEqual(topic, before)


if __name__ == "__main__":
    unittest.main()
