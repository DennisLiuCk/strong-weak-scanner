# -*- coding: utf-8 -*-
"""研究方法快照、到期 review event 與 dashboard 契約。"""
import datetime as dt
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import research_method_audit as audit


class ResearchMethodAuditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 以最新 immutable snapshot 日期重算 registry，避免測試日期落後於合法新資料。
        cls.latest = audit.load_method_audit(strict=True)
        cls.as_of = dt.date.fromisoformat(cls.latest["asOf"])
        cls.topics, cls.graph, cls.radar, cls.scan = audit._load_context(cls.as_of)
        cls.reviews = audit.load_monitor_reviews(cls.topics, cls.as_of, strict=True)
        cls.current = audit.compute_method_audit(
            cls.topics, cls.graph, cls.radar, cls.reviews, cls.scan, cls.as_of,
        )

    def test_baseline_snapshot_matches_current_registry(self):
        self.assertRegex(self.latest["snapshotId"], r"^RMA-\d{4}-\d{2}-\d{2}-\d+$")
        self.assertEqual(self.latest["asOf"], self.current["asOf"])
        self.assertEqual(self.latest["methodologyVersion"], "1.6")
        self.assertEqual(
            self.latest["registryFingerprint"], self.current["registryFingerprint"],
        )
        self.assertGreater(len(self.latest["history"]), 0)
        self.assertEqual(
            self.latest["history"][-1]["snapshotId"], self.latest["snapshotId"],
        )
        self.assertEqual(
            len({item["snapshotId"] for item in self.latest["history"]}),
            len(self.latest["history"]),
        )

    def test_audit_exposes_counts_without_fake_accuracy_score(self):
        active_claims = sum(
            claim.get("status", "active") == "active"
            for topic in self.topics
            for claim in topic["claims"]
        )
        self.assertEqual(self.current["scope"]["topics"], len(self.topics))
        self.assertEqual(self.current["scope"]["graphs"], self.graph["stats"]["graphs"])
        self.assertEqual(self.current["scope"]["scanEvents"], len(self.scan["rows"]))
        self.assertEqual(self.current["claims"]["active"], active_claims)
        self.assertEqual(
            self.current["graphs"]["activeEdges"], self.graph["stats"]["edges"]
        )
        self.assertEqual(
            self.current["graphs"]["traceableEdges"],
            self.current["graphs"]["activeEdges"],
        )
        self.assertGreaterEqual(self.current["monitors"]["reviewedMature"], 0)
        self.assertEqual(
            self.current["monitors"]["reviewedMature"],
            self.latest["monitors"]["reviewedMature"],
        )
        self.assertEqual(
            self.current["corrections"]["monitorReviewEvents"], len(self.reviews),
        )
        expected_results = {
            result: sum(row["result"] == result for row in self.reviews)
            for result in audit.REVIEW_RESULTS
        }
        self.assertEqual(self.current["corrections"]["resultCounts"], expected_results)
        # 修正數量以 claim lifecycle 重算，不能靠手動維護的固定值冒充學習紀錄。
        expected_corrections = sum(
            claim.get("status") in {"superseded", "refuted"}
            for topic in self.topics
            for claim in topic["claims"]
        )
        self.assertEqual(
            self.current["corrections"]["supersededOrRefutedClaims"],
            expected_corrections,
        )
        self.assertEqual(
            self.current["scans"]["latestId"], self.scan["latest"]["scan_id"]
        )
        self.assertEqual(
            self.current["scans"]["latestScope"], self.scan["latest"]["scope"]
        )
        self.assertEqual(self.current["scans"]["overdue"], 0)
        # 校準狀態同時受待回顧 monitor、成熟回查與最低結果筆數約束。
        evidence_outcomes = sum(
            row["result"] in audit.EVIDENCE_RESULTS for row in self.reviews
        )
        expected_ready = (
            self.current["monitors"]["dueOrOverdue"] == 0
            and self.current["monitors"]["reviewedMature"] > 0
            and evidence_outcomes >= audit.MIN_DESCRIPTIVE_OUTCOMES
        )
        self.assertEqual(
            self.current["calibration"]["descriptiveBreakdownReady"], expected_ready,
        )
        self.assertEqual(
            self.current["calibration"]["evidenceBearingOutcomes"], evidence_outcomes,
        )
        self.assertEqual(
            self.current["calibration"]["outcomeCounts"],
            {
                "new_support": expected_results["new_support"],
                "new_contrary": expected_results["new_contrary"],
            },
        )
        self.assertNotIn("supportRate", self.current["calibration"])
        self.assertNotIn("score", self.current)
        self.assertEqual(self.current["scope"]["financialAssessments"], 4)
        self.assertEqual(self.current["graphs"]["financialAssessments"], 4)
        self.assertEqual(self.current["graphs"]["financialContractComplete"], 4)
        self.assertEqual(self.current["graphs"]["directFinancialAttribution"], 0)
        self.assertEqual(self.current["graphs"]["boundedFinancialProxies"], 3)
        self.assertEqual(self.current["graphs"]["financialDenominatorsNotDisclosed"], 1)
        selection = self.current["selection"]
        self.assertEqual(selection["cycleId"], self.radar["selectionCycleId"])
        self.assertEqual(selection["candidates"], len(self.radar["candidates"]))
        self.assertEqual(selection["frozenBeforeResearch"], len(self.radar["selectionLog"]))
        self.assertEqual(selection["advanceDecisions"], self.radar["stats"]["selectedAdvance"])
        self.assertEqual(selection["promotedAfterResearch"], sum(
            row["selectionOutcome"] == "promoted_after_research"
            for row in self.radar["candidates"]
        ))
        self.assertEqual(selection["rejectedAfterResearch"], sum(
            row["selectionOutcome"] == "rejected_after_research"
            for row in self.radar["candidates"]
        ))
        self.assertEqual(selection["cycles"], self.radar["historyStats"]["schema2Cycles"])
        self.assertEqual(
            selection["accountableCycles"], selection["cycles"],
        )
        self.assertEqual(selection["requiredEarlyReselections"], 1)
        self.assertEqual(selection["documentedEarlyTriggers"], 1)
        self.assertEqual(selection["grandfatheredEarlyReselections"], 3)
        self.assertTrue(selection["accountable"])
        self.assertIn("不是選題正確率或投資命中率", selection["boundary"])

    def test_every_gate_keeps_its_own_status_and_boundary(self):
        gates = {item["id"]: item for item in self.current["gates"]}
        snapshot_gates = {item["id"]: item for item in self.latest["gates"]}
        self.assertEqual(
            set(gates),
            {
                "selection_accountability", "traceability", "cross_check_depth", "falsifiability",
                "freshness", "correction_learning", "scan_accountability",
                "calibration", "financial_materiality_contract",
            },
        )
        self.assertEqual(gates["selection_accountability"]["status"], "pass")
        self.assertEqual(gates["cross_check_depth"]["status"], "pass")
        self.assertEqual(gates["financial_materiality_contract"]["status"], "pass")
        self.assertEqual(
            gates["freshness"]["status"], snapshot_gates["freshness"]["status"],
        )
        self.assertEqual(
            gates["correction_learning"]["status"],
            snapshot_gates["correction_learning"]["status"],
        )
        self.assertEqual(gates["scan_accountability"]["status"], "pass")
        self.assertEqual(
            gates["calibration"]["status"], snapshot_gates["calibration"]["status"],
        )
        for gate in gates.values():
            self.assertTrue(gate["observed"])
            self.assertTrue(gate["boundary"])

    def test_cross_check_gate_names_every_topic_missing_a_second_chain(self):
        missing = self.current["sources"]["thesesNeedingSecondIndependentGroup"]
        self.assertEqual(missing, [])
        self.assertEqual(
            self.current["sources"]["thesesWithTwoIndependentGroups"],
            self.current["sources"]["activeTheses"] - len(missing),
        )
        gate = next(item for item in self.current["gates"]
                    if item["id"] == "cross_check_depth")
        for topic_id in missing:
            self.assertIn(topic_id, gate["observed"])

    def test_method_audit_uses_same_corporate_domain_grouping_as_topic_lint(self):
        investor = {"url": "https://investor.nvidia.com/news/example"}
        newsroom = {"url": "https://www.nvidia.com/en-us/news/example"}
        self.assertEqual(audit._source_group(investor), audit._source_group(newsroom))

    def test_no_new_evidence_reviews_do_not_claim_sources_or_actions(self):
        # not_yet_testable 與 no_new_evidence 同樣不帶新證據：前者是觸發條件的觀測窗
        # 尚未開啟，後者是查過但沒有新資料。原本把「非 no_new_evidence」一律當成帶證據，
        # 在第一筆 not_yet_testable 出現時就會誤要求它附 source 與 new_claim。
        # 只有 new_support／new_contrary 才是 audit 計入 calibration 的帶證據結果。
        non_evidence = [row for row in self.reviews
                        if row["result"] in {"no_new_evidence", "not_yet_testable"}]
        evidence_bearing = [row for row in self.reviews
                            if row["result"] in {"new_support", "new_contrary"}]
        self.assertEqual(len(non_evidence) + len(evidence_bearing), len(self.reviews))
        self.assertEqual(len(evidence_bearing),
                         self.current["calibration"]["evidenceBearingOutcomes"])
        for row in non_evidence:
            self.assertEqual(row["evidence_source_ids"], [])
            self.assertEqual(row["claim_action"], "none")
        for row in evidence_bearing:
            self.assertTrue(row["evidence_source_ids"])
            self.assertIn(row["claim_action"], audit.CLAIM_ACTIONS)
        self.assertEqual(
            self.current["monitors"]["dueOrOverdue"],
            self.latest["monitors"]["dueOrOverdue"],
        )
        self.assertEqual(
            self.current["freshness"]["staleTopics"],
            self.latest["freshness"]["staleTopics"],
        )

    def test_snapshot_baseline_treats_windows_crlf_as_git_lf(self):
        self.assertTrue(audit._same_content_ignoring_crlf(
            b'{\r\n  "schemaVersion": 1\r\n}\r\n',
            b'{\n  "schemaVersion": 1\n}\n',
        ))
        self.assertFalse(audit._same_content_ignoring_crlf(
            b'{\r\n  "schemaVersion": 1\r\n}\r\n',
            b'{\n  "schemaVersion": 2\n}\n',
        ))

    def test_evidence_result_requires_registered_source(self):
        text = (
            ",".join(audit.REVIEW_HEADER) + "\n"
            "MR-2026-08-02-TEST,2026-08-02,"
            "MI-2026-07-23-US-SECTION301-TAIWAN,T1,new_support,,none,"
            "2026-08-09,missing source\n"
        )
        _, errors = audit._read_review_text(text, self.topics, self.as_of)
        self.assertTrue(any("必須引用已登錄 source" in error for error in errors))

    def test_dashboard_and_runbooks_publish_method_audit(self):
        builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        method = (ROOT / "MARKET_RESEARCH_METHOD.md").read_text(encoding="utf-8")
        maintenance = (ROOT / "RESEARCH_MAINTENANCE.md").read_text(encoding="utf-8")
        workflow = (ROOT / ".github" / "workflows" / "qualitative-quality.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn('research_library["methodAudit"] = load_method_audit(', builder)
        for token in (
            'id="methodAudit"', "const AUDIT=LIB.methodAudit", "function renderMethodAudit()",
            "方法健康度（不合成分數）", "逐項顯示歷史選題承諾、提前重選觸發",
            "掃描覆蓋問責", "scope.scanEvents",
        ):
            self.assertIn(token, template)
        self.assertIn("monitor_reviews.csv", method)
        self.assertIn("獨立交叉驗證", method)
        self.assertIn("每月方法回顧", maintenance)
        self.assertIn("掃描覆蓋問責", method)
        self.assertIn("selection_log.csv", method)
        self.assertIn("early_trigger", method)
        self.assertIn("research_event_scan.py", maintenance)
        self.assertIn("不計算支持率", method)
        self.assertIn("選題前承諾", maintenance)
        self.assertIn("python scripts/research_method_audit.py --lint", workflow)


if __name__ == "__main__":
    unittest.main()
