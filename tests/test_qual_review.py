#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""qual_review 機器輔助複核 triage 的純函式測試(不需 Poppler)。"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                "scripts"))

from qual_review import (build_report, classify_claims, extract_claim_numbers,
                         match_number, page_number_tokens, pairwise_match)


def _numbers(text):
    return {item["raw"] for item in extract_claim_numbers(text)}


class ExtractClaimNumbersTest(unittest.TestCase):
    def test_keeps_money_pct_and_comma_numbers(self):
        text = "2025 營收 7,516,293 仟元、年減 11.96%,毛利率 28.77%,約 54.34 億元"
        self.assertEqual(_numbers(text), {"7,516,293", "11.96", "28.77", "54.34"})

    def test_skips_years_dates_and_period_codes(self):
        self.assertEqual(_numbers("2026Q1 與 2025 年、2026-07-18 及 115 年度"), set())

    def test_skips_small_bare_integers(self):
        self.assertEqual(_numbers("前 3 大客戶、60 交易日"), set())

    def test_unit_detection(self):
        items = {item["raw"]: item for item in extract_claim_numbers("負 4.25 億元與 836 萬元")}
        self.assertEqual(items["4.25"]["unit"], "億")
        self.assertEqual(items["836"]["unit"], "萬")

    def test_pct_detection(self):
        item = extract_claim_numbers("成長 10%")[0]
        self.assertTrue(item["pct"])


class MatchNumberTest(unittest.TestCase):
    def _match(self, claim_text, page_text):
        number = extract_claim_numbers(claim_text)[0]
        return match_number(number, page_number_tokens(page_text))

    def test_exact_match(self):
        self.assertTrue(self._match("營收 7,516,293 仟元", "銷貨收入 $ 7,516,293 100"))

    def test_yi_to_thousand_scale_with_rounding(self):
        # 54.34 億元 = 5,433,973 仟元(容差為最後一位小數的半格 ×100000)。
        self.assertTrue(self._match("合計 54.34 億元", "小計 5,433,973 72.30"))

    def test_yi_rejects_non_conventional_scale(self):
        # 0.99 億元不可經 ×1,000,000 誤命中 988,547(那是 9.89 億)。
        self.assertFalse(self._match("匯損 0.99 億元", "存貨 988,547 13"))

    def test_pct_never_scaled(self):
        self.assertFalse(self._match("占比 0.07%", "金額 7,000,000 元"))

    def test_negative_matches_paren_absolute(self):
        # 財報以括號表示負數;比對取絕對值,正負號屬 reviewer 口徑判讀。
        self.assertTrue(self._match("營業現金流 -4.25 億元", "營業活動 ( 424,987 )"))

    def test_money_unit_ignores_bare_small_tokens(self):
        # 5.00 億元不可命中頁腳的裸「5」。
        self.assertFalse(self._match("契約價 5.00 億元", "- 5 -"))

    def test_rounding_of_integer_pct(self):
        self.assertTrue(self._match("約 23%", "占比 22.62 無"))


class PairwiseMatchTest(unittest.TestCase):
    def _pairs(self, claim_text, page_text):
        number = extract_claim_numbers(claim_text)[0]
        tokens = [dict(tok, page=1) for tok in page_number_tokens(page_text)]
        return pairwise_match(number, tokens)

    def test_sum_case_6451(self):
        # 訊芯-KY 案例:現金 5,572,071 + 定存 3,111,952 = 8,684,023 仟元 = 86.84 億。
        pairs = self._pairs("合計 86.84 億元", "現金 5,572,071 定存 3,111,952")
        self.assertEqual(len(pairs), 1)
        self.assertEqual(pairs[0][1], "+")

    def test_difference_case(self):
        pairs = self._pairs("差額 10.94 億元", "現金流 1,556,809 購置 462,716")
        self.assertTrue(any(op == "-" for _a, op, _b, _s in pairs))

    def test_pct_excluded(self):
        self.assertEqual(self._pairs("毛利率 30.51%", "毛利 475,203 營收 1,557,270"), [])

    def test_tiny_operand_excluded(self):
        # 運算元須達目標一成,排除「31 + 23,194」式湊數對。
        self.assertEqual(self._pairs("合計 232.25 億元", "附註 31 金額 23,194,969"), [])


class ClassifyClaimsTest(unittest.TestCase):
    def _units(self, text, refs):
        return [{"text": text, "raw": text, "refs": refs, "kind": "paragraph"}]

    def _docs(self, cited_text="", neighbor_text=""):
        return [{
            "id": "S1", "cited_pages": [4], "rendered_pages": [3, 4, 5],
            "page_text": {3: "", 4: cited_text, 5: neighbor_text},
        }]

    def test_hit_on_cited_page(self):
        findings = classify_claims(self._units("營收 1,557,270 仟元", ["S1"]),
                                   self._docs(cited_text="營業收入 1,557,270 100"))
        self.assertEqual(findings[0]["numbers"][0]["status"], "hit")

    def test_neighbor_only_is_flagged(self):
        findings = classify_claims(self._units("定存 3,111,952 仟元", ["S1"]),
                                   self._docs(neighbor_text="定期存款 3,111,952"))
        self.assertEqual(findings[0]["numbers"][0]["status"], "neighbor_only")

    def test_derived_beats_neighbor(self):
        # 運算元皆在 cited 頁時是合法推導主張,鄰頁字面值只是提示,不是 HARD。
        findings = classify_claims(
            self._units("租賃負債合計 4.55 億元", ["S1"]),
            self._docs(cited_text="流動 69,478 非流動 385,627",
                       neighbor_text="合計 455,105"))
        self.assertEqual(findings[0]["numbers"][0]["status"], "derived")

    def test_miss_and_risk_terms(self):
        findings = classify_claims(self._units("量產訂單 9,999,999 仟元", ["S1"]),
                                   self._docs(cited_text="無關文字"))
        self.assertEqual(findings[0]["numbers"][0]["status"], "miss")
        self.assertIn("量產", findings[0]["risk_terms"])

    def test_unknown_ref_reported(self):
        findings = classify_claims(self._units("營收 1,557,270 仟元", ["S9"]), self._docs())
        self.assertEqual(findings[0]["unknown_refs"], ["S9"])

    def test_duplicate_numbers_deduped(self):
        findings = classify_claims(self._units("上限 10% 與下限 10%", ["S1"]),
                                   self._docs(cited_text="10"))
        self.assertEqual(len(findings[0]["numbers"]), 1)


class BuildReportTest(unittest.TestCase):
    def test_hard_counts_neighbor_and_missing_render(self):
        units = [{"text": "定存 3,111,952 仟元", "raw": "", "refs": ["S1"], "kind": "paragraph"}]
        docs = [{"id": "S1", "cited_pages": [4], "rendered_pages": [4, 5],
                 "page_text": {4: "", 5: "定期存款 3,111,952"}}]
        findings = classify_claims(units, docs)
        manifest = {"pack_sha256": "f" * 64, "documents": []}
        report, hard_count, stats = build_report(
            "9999", "notes/qualitative/9999_test.md", manifest, findings,
            textless=[], render_issues=[{"sid": "S1", "page": 5, "kind": "missing"}])
        self.assertEqual(hard_count, 2)
        self.assertIn("只在鄰頁命中", report)
        self.assertIn("render 缺檔", report)
        self.assertEqual(stats["miss"], 0)


if __name__ == "__main__":
    unittest.main()
