import contextlib
import io
import json
import os
import re
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from unittest import mock


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import qual_notes  # noqa: E402
import qual_evidence  # noqa: E402


PRIMARY = (
    "- [S1] **一手**｜公司 2026 Q1 財務報告（2026-05-15）｜p.12 營業收入｜"
    "https://example.com/2026q1.pdf"
)
SECONDARY = (
    "- [S1] **二手**｜媒體法說摘要（2026-05-16）｜第 3 段｜"
    "https://example.com/article"
)
PRIMARY_2 = (
    "- [S2] **一手**｜交易所重大訊息（2026-05-16）｜說明第 5 項｜"
    "https://example.com/announcement"
)
FOCUSED_ANNUAL = (
    "- [S1] **一手**｜公司 2025 年報暨年度查核財報（2026-03-31）｜p.45 產品組合｜"
    "https://example.com/2025-annual-report.pdf"
)
FOCUSED_QUARTERLY = (
    "- [S2] **一手**｜公司 2026 Q1 財務報告（2026-05-15）｜p.12 營業收入｜"
    "https://example.com/2026q1.pdf"
)
FOCUSED_IR = (
    "- [S3] **一手**｜公司 2026 Q1 法說簡報（2026-05-20）｜p.8 營運展望｜"
    "https://example.com/2026q1-ir.pdf"
)


def sign(text):
    digest = qual_notes.content_digest(text)
    return text.replace(
        "reviewed_content_sha256:",
        f"reviewed_content_sha256: {digest}",
        1,
    )


def resign(text):
    meta_match = qual_notes._META_RE.search(text)
    if not meta_match:
        return text
    clean_meta = re.sub(
        r"^[ \t]*reviewed_content_sha256[ \t]*:.*$",
        "reviewed_content_sha256:",
        meta_match.group(0),
        flags=re.M,
    )
    return sign(text[:meta_match.start()] + clean_meta + text[meta_match.end():])


def independent_note(source=PRIMARY, table_citation="[S1]", reviewed_by="reviewer-b"):
    text = f"""# 1234 測試 — 質化研究筆記

<!-- meta
stock_id: 1234
template_version: 2
verification_status: independently_verified
drafted_by: researcher-a
last_updated: 2026-07-11
content_as_of: 2026-07-11
latest_financial_period: 2026 Q1
next_review: 2026-10-31
reviewed_by: {reviewed_by}
reviewed_at: 2026-07-11
review_scope: all_material_claims
reviewed_content_sha256:
-->

## 30 秒摘要

公司 2026 Q1 營收為 10 億元。[S1]

- 毛利率為 30%。[S1]

| 指標 | 數值 | 依據 |
|---|---|---|
| 營收 | 10 億元 | {table_citation} |

## 產業位置與競爭格局
產業競爭者共有三家。[S1]

## 業務與獲利模式
公司以銷售自有產品取得收入。[S1]

## 客戶、產品與地區結構
主要產品占營收六成。[S1]

## 財務品質與資本配置
公司維持淨現金部位。[S1]

## 優勢、弱點與護城河
認證週期形成轉換成本。[S1]

## 成長動能、催化劑與驗證 KPI
新產能預計下一季量產。[S1]

## 風險與預警指標
客戶集中度是主要風險。[S1]

## 管理層與治理
董事會每季檢查資本支出。[S1]

## 證據索引與資料來源

{source}

## 下次更新與事件觸發

- **固定複核**：下一季財報發布後更新。
- **事件觸發**：重大訊息公告或核心 KPI 偏離時提前更新。
"""
    return sign(text)


def analyse(text, filename="1234_測試.md"):
    return qual_notes._analyse_note(os.path.join(ROOT, filename), text)


def focused_manifest():
    urls = {
        "S1": "https://example.com/2025-annual-report.pdf",
        "S2": "https://example.com/2026q1.pdf",
        "S3": "https://example.com/2026q1-ir.pdf",
    }
    documents = []
    for index, source_id in enumerate(("S1", "S2", "S3"), 1):
        documents.append({
            "id": source_id,
            "roles": (
                ["annual_report", "annual_financials"] if source_id == "S1"
                else ["latest_quarterly_report"] if source_id == "S2"
                else ["latest_investor_conference"]
            ),
            "url": urls[source_id],
            "file": f"documents/{source_id}.pdf",
            "sha256": str(index) * 64,
            "size_bytes": 100 + index,
            "page_count": 20,
            "cited_pages": [10],
            "rendered_pages": [9, 10, 11],
        })
    manifest = {
        "schema": qual_evidence.SCHEMA,
        "schema_version": qual_evidence.SCHEMA_VERSION,
        "research_profile": qual_evidence.RESEARCH_PROFILE,
        "stock_id": "1234",
        "content_as_of": "2026-07-11",
        "source_search_timeout_minutes": qual_evidence.SOURCE_SEARCH_TIMEOUT_MINUTES,
        "unverified_claims_removed": True,
        "documents": documents,
    }
    manifest["pack_sha256"] = qual_evidence.manifest_digest(manifest)
    return manifest


def focused_note(pack_sha):
    text = independent_note()
    text = text.replace(
        "template_version: 2",
        "template_version: 2\n"
        "research_profile: focused_v1\n"
        "core_source_ids: S1,S2,S3\n"
        "evidence_pack_manifest: notes/qualitative/evidence/1234/test-pack.json\n"
        f"evidence_pack_sha256: {pack_sha}\n"
        "review_method: offline_evidence_pack_independent_recalculation",
    )
    text = text.replace(PRIMARY, "{{FOCUSED_SOURCES}}")
    text = text.replace("[S1]", "[S1][S2][S3]")
    text = text.replace(
        "{{FOCUSED_SOURCES}}",
        "\n".join((FOCUSED_ANNUAL, FOCUSED_QUARTERLY, FOCUSED_IR)),
    )
    return resign(text)


def analyse_focused(text, manifest=None):
    with tempfile.TemporaryDirectory() as directory:
        manifest_path = os.path.join(
            directory, "notes", "qualitative", "evidence", "1234", "test-pack.json"
        )
        os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
        if manifest is not None:
            with open(manifest_path, "w", encoding="utf-8", newline="\n") as handle:
                json.dump(manifest, handle, ensure_ascii=False, sort_keys=True)
        note_path = os.path.join(directory, "1234_測試.md")
        with mock.patch.object(qual_notes, "ROOT", directory):
            return qual_notes._analyse_note(note_path, text)


class QualitativeNoteQualityTests(unittest.TestCase):
    def test_legacy_v1_never_auto_upgrades_from_date_or_citations(self):
        text = f"""# 1234 測試
<!-- meta
stock_id: 1234
template_version: 1
last_updated: 2026-07-11
next_review: 2026-10-01
-->
## 業務概況
公司營收 10 億元。[S1]
## 資料來源
{PRIMARY}
"""
        note = analyse(text)
        self.assertEqual("ai_draft", note["verification"])
        self.assertFalse(note["quality_invalid"])

    def test_valid_independent_note_requires_every_claim_block_primary(self):
        note = analyse(independent_note())
        self.assertEqual("independently_verified", note["verification"])
        self.assertEqual(11, note["claim_count"])
        self.assertEqual(11, note["cited_claim_count"])
        self.assertEqual(11, note["primary_cited_claim_count"])
        self.assertEqual([], note["quality_errors"])

    def test_focused_profile_binds_note_to_tracked_evidence_manifest(self):
        manifest = focused_manifest()
        note = analyse_focused(focused_note(manifest["pack_sha256"]), manifest)
        self.assertEqual("independently_verified", note["verification"])
        self.assertEqual([], note["quality_errors"])
        self.assertTrue(any("目標約 25–35" in item for item in note["quality_warnings"]))
        self.assertEqual("focused_v1", note["research_profile"])
        self.assertEqual(manifest["pack_sha256"], note["evidence_pack_sha256"])

    def test_focused_claim_target_is_warning_not_false_quality_failure(self):
        manifest = focused_manifest()
        extra_claims = "\n".join(
            f"- 額外的重要觀察 {index}。[S1]" for index in range(1, 15)
        )
        text = focused_note(manifest["pack_sha256"]).replace(
            "- 毛利率為 30%。[S1]",
            "- 毛利率為 30%。[S1]\n" + extra_claims,
        )
        note = analyse_focused(resign(text), manifest)
        self.assertEqual(25, note["claim_count"])
        self.assertEqual("independently_verified", note["verification"])
        self.assertFalse(any("目標約 25–35" in item for item in note["quality_warnings"]))

        too_many = "\n".join(
            f"- 次要觀察 {index}。[S1]" for index in range(1, 26)
        )
        text = focused_note(manifest["pack_sha256"]).replace(
            "- 毛利率為 30%。[S1][S2][S3]",
            "- 毛利率為 30%。[S1][S2][S3]\n" + too_many,
        )
        note = analyse_focused(resign(text), manifest)
        self.assertEqual(36, note["claim_count"])
        self.assertEqual("independently_verified", note["verification"])
        self.assertTrue(any("目標約 25–35" in item for item in note["quality_warnings"]))

    def test_focused_profile_rejects_missing_or_mismatched_pack(self):
        manifest = focused_manifest()
        wrong_sha = "f" * 64
        note = analyse_focused(focused_note(wrong_sha), manifest)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("evidence_pack_sha256 與 manifest 不一致" in error
                            for error in note["quality_errors"]))

        missing = analyse_focused(focused_note(manifest["pack_sha256"]), None)
        self.assertEqual("ai_draft", missing["verification"])
        self.assertTrue(any("找不到可提交的 evidence manifest" in error
                            for error in missing["quality_errors"]))

        no_recalculation = focused_note(manifest["pack_sha256"]).replace(
            "review_method: offline_evidence_pack_independent_recalculation",
            "review_method:",
        )
        note = analyse_focused(resign(no_recalculation), manifest)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("review_method" in error for error in note["quality_errors"]))

    def test_focused_profile_rejects_source_set_and_url_drift(self):
        manifest = focused_manifest()
        missing_core = focused_note(manifest["pack_sha256"]).replace(
            "core_source_ids: S1,S2,S3", "core_source_ids: S1,S2"
        )
        note = analyse_focused(resign(missing_core), manifest)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("3–5 份核心文件" in error for error in note["quality_errors"]))

        drifted = focused_note(manifest["pack_sha256"]).replace(
            "https://example.com/2026q1-ir.pdf",
            "https://example.com/changed-2026q1-ir.pdf",
        )
        note = analyse_focused(resign(drifted), manifest)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("S3 的筆記 URL" in error for error in note["quality_errors"]))

    def test_legacy_v2_is_not_retroactively_forced_into_focused_limits(self):
        note = analyse(independent_note())
        self.assertEqual("independently_verified", note["verification"])
        self.assertEqual([], note["quality_errors"])
        self.assertFalse(any("25–35" in item for item in note["quality_warnings"]))

    def test_table_caption_citation_does_not_cover_uncited_row(self):
        note = analyse(independent_note(table_citation=""))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("claim block 沒有 [S#]" in error for error in note["quality_errors"]))

    def test_short_material_claim_cannot_bypass_coverage(self):
        text = independent_note().replace(
            "- 毛利率為 30%。[S1]",
            "- 毛利率為 30%。[S1]\n- 市占第一",
        )
        # 重新簽署，確保失敗原因是 coverage 而非 hash。
        digest_line = next(
            line for line in text.splitlines() if line.startswith("reviewed_content_sha256:")
        )
        note = analyse(sign(text.replace(digest_line, "reviewed_content_sha256:")))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("claim block 沒有 [S#]" in error for error in note["quality_errors"]))

    def test_mixed_placeholder_language_cannot_hide_real_claim(self):
        text = independent_note().replace(
            "- 毛利率為 30%。[S1]",
            "- 毛利率為 30%。[S1]\n- 此案尚待核准，但公司已投入 10 億元。",
        )
        note = analyse(resign(text))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("claim block 沒有 [S#]" in error for error in note["quality_errors"]))

    def test_ordered_list_items_are_independent_claim_blocks(self):
        text = independent_note().replace(
            "- 毛利率為 30%。[S1]",
            "1. 公司是全球市占第一。\n2. 毛利率為 30%。[S1]",
        )
        note = analyse(resign(text))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("claim block 沒有 [S#]" in error for error in note["quality_errors"]))

    def test_adversarial_heading_cannot_bypass_claim_coverage(self):
        text = independent_note().replace(
            "## 證據索引與資料來源",
            "## 下次更新與重要風險\n公司可能破產。\n\n## 證據索引與資料來源",
        )
        note = analyse(resign(text))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("claim block 沒有 [S#]" in error for error in note["quality_errors"]))

    def test_secondhand_only_cannot_be_independently_verified(self):
        note = analyse(independent_note(source=SECONDARY))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("沒有一手來源" in error for error in note["quality_errors"]))

    def test_same_drafter_and_reviewer_is_rejected(self):
        note = analyse(independent_note(reviewed_by="researcher-a"))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("必須與 drafted_by 不同" in error for error in note["quality_errors"]))

    def test_edit_after_signoff_invalidates_digest(self):
        text = independent_note().replace("10 億元。[S1]", "11 億元。[S1]", 1)
        note = analyse(text)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("sha256 不一致" in error for error in note["quality_errors"]))

    def test_body_line_named_like_hash_field_is_still_hashed(self):
        text = independent_note().replace(
            "產業競爭者共有三家。[S1]",
            "產業競爭者共有三家。[S1]\n\nreviewed_content_sha256: 管理層宣稱訂單 10 億元。[S1]",
        )
        signed = resign(text)
        mutated = signed.replace("管理層宣稱訂單 10 億元", "管理層宣稱訂單 99 億元")
        note = analyse(mutated)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("sha256 不一致" in error for error in note["quality_errors"]))

    def test_independent_requires_complete_nonplaceholder_v2_structure(self):
        missing = resign(independent_note().replace("## 管理層與治理", "## 其他治理筆記"))
        note = analyse(missing)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("缺少 v2 章節：管理層與治理" in error for error in note["quality_errors"]))

        placeholder = resign(independent_note().replace(
            "董事會每季檢查資本支出。[S1]", "（待填：管理層與治理）"
        ))
        note = analyse(placeholder)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("模板占位：管理層與治理" in error for error in note["quality_errors"]))

    def test_verified_note_requires_review_schedule_and_real_actor_ids(self):
        no_schedule = resign(independent_note().replace("next_review: 2026-10-31", "next_review:"))
        note = analyse(no_schedule)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("缺少合法 next_review" in error for error in note["quality_errors"]))
        self.assertEqual("unscheduled", qual_notes.note_status(note, "2027-01-01"))

        placeholders = resign(independent_note()
                              .replace("reviewed_by: reviewer-b", "reviewed_by: TBD reviewer")
                              .replace("latest_financial_period: 2026 Q1",
                                       "latest_financial_period: TBD period"))
        note = analyse(placeholders)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("reviewed_by" in error for error in note["quality_errors"]))
        self.assertTrue(any("latest_financial_period" in error for error in note["quality_errors"]))

    def test_verification_dates_cannot_claim_future_knowledge(self):
        future = independent_note()
        future = future.replace("last_updated: 2026-07-11", "last_updated: 2099-01-01")
        future = future.replace("content_as_of: 2026-07-11", "content_as_of: 2099-01-01")
        future = future.replace("reviewed_at: 2026-07-11", "reviewed_at: 2099-01-01")
        note = analyse(resign(future))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("不可晚於今天" in error for error in note["quality_errors"]))

        after_review = resign(independent_note().replace(
            "content_as_of: 2026-07-11", "content_as_of: 2026-07-12"
        ))
        note = analyse(after_review)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("content_as_of 晚於 reviewed_at" in error for error in note["quality_errors"]))

    def test_research_today_uses_taiwan_date_across_utc_midnight(self):
        instant = datetime(2026, 7, 10, 16, 30, tzinfo=timezone.utc)

        class FakeDateTime:
            @classmethod
            def now(cls, tz):
                return instant.astimezone(tz)

        with mock.patch.object(qual_notes, "datetime", FakeDateTime):
            self.assertEqual("2026-07-11", qual_notes._today().isoformat())
        self.assertEqual(timedelta(hours=8), qual_notes._TAIPEI_TZ.utcoffset(None))

    def test_verified_source_must_be_direct_and_live_in_evidence_index(self):
        generic = resign(independent_note().replace(
            "https://example.com/2026q1.pdf", "https://mops.twse.com.tw/mops/"
        ))
        note = analyse(generic)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("不可使用 MOPS 查詢入口" in error for error in note["quality_errors"]))

        exact_url = (
            "https://mopsov.twse.com.tw/mops/web/ajax_t05st01?"
            "TYPEK=otc&firstin=true&step=2&year=115&month=all&e_month=all&"
            "co_id=3324&spoke_date=20260530&spoke_time=2944&seq_no=1"
        )
        exact = resign(independent_note().replace(
            "https://example.com/2026q1.pdf", exact_url
        ))
        note = analyse(exact)
        self.assertEqual("independently_verified", note["verification"])
        self.assertFalse(any("MOPS 查詢入口" in error for error in note["quality_errors"]))

        incomplete = resign(independent_note().replace(
            "https://example.com/2026q1.pdf", exact_url.replace("&seq_no=1", "")
        ))
        note = analyse(incomplete)
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("不可使用 MOPS 查詢入口" in error for error in note["quality_errors"]))

        source_elsewhere = independent_note().replace(PRIMARY, "")
        source_elsewhere = source_elsewhere.replace(
            "產業競爭者共有三家。[S1]", f"產業競爭者共有三家。[S1]\n\n{PRIMARY}"
        )
        note = analyse(resign(source_elsewhere))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("證據索引與資料來源章節沒有" in error for error in note["quality_errors"]))

    def test_excluded_evidence_and_update_sections_cannot_hide_company_claims(self):
        for hidden in ("公司是全球市占第一。", "### 公司是全球市占第一", "| 公司是全球市占第一 |"):
            with self.subTest(hidden=hidden):
                hidden_evidence = independent_note().replace(PRIMARY, PRIMARY + "\n\n" + hidden)
                note = analyse(resign(hidden_evidence))
                self.assertEqual("ai_draft", note["verification"])
                self.assertTrue(any("證據索引只能放" in error for error in note["quality_errors"]))

        hidden_update = independent_note().replace(
            "- **事件觸發**：重大訊息公告或核心 KPI 偏離時提前更新。",
            "- 公司可能破產。",
        )
        note = analyse(resign(hidden_update))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("事件觸發" in error for error in note["quality_errors"]))

    def test_review_cannot_predate_latest_edit(self):
        text = independent_note().replace(
            "reviewed_at: 2026-07-11", "reviewed_at: 2026-07-10"
        )
        # 先以新的 meta 重簽，隔離 reviewed_at 規則，不讓 hash mismatch 掩蓋它。
        text = text.replace(
            next(line for line in text.splitlines() if line.startswith("reviewed_content_sha256:")),
            "reviewed_content_sha256:",
        )
        note = analyse(sign(text))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("早於 last_updated" in error for error in note["quality_errors"]))

    def test_partial_requires_scope_reviewer_and_primary_reference(self):
        text = f"""# 1234 測試
<!-- meta
stock_id: 1234
template_version: 1
verification_status: partially_verified
drafted_by: writer-a
last_updated: 2026-07-11
next_review: 2026-10-01
reviewed_by: reviewer-b
reviewed_at: 2026-07-11
review_scope:
reviewed_content_sha256:
-->
## 財務亮點
2026 Q1 營收為 10 億元。[S1]
## 資料來源
{PRIMARY}
"""
        note = analyse(sign(text))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("review_scope" in error for error in note["quality_errors"]))

    def test_partial_cannot_hide_unused_primary_behind_secondary_citation(self):
        text = f"""# 1234 測試
<!-- meta
stock_id: 1234
template_version: 1
verification_status: partially_verified
drafted_by: writer-a
last_updated: 2026-07-11
next_review: 2026-10-01
reviewed_by: reviewer-b
reviewed_at: 2026-07-11
review_scope: confirmed_corrections_only
reviewed_content_sha256:
-->
## 財務亮點
2026 Q1 營收為 10 億元。[S1]
## 資料來源
{SECONDARY}
{PRIMARY_2}
"""
        note = analyse(sign(text))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("沒有實際指向一手來源" in error for error in note["quality_errors"]))

    def test_partial_citation_in_excluded_update_section_does_not_count(self):
        text = f"""# 1234 測試
<!-- meta
stock_id: 1234
template_version: 1
verification_status: partially_verified
drafted_by: writer-a
last_updated: 2026-07-11
next_review: 2026-10-01
reviewed_by: reviewer-b
reviewed_at: 2026-07-11
review_scope: confirmed_corrections_only
reviewed_content_sha256:
-->
## 財務亮點
2026 Q1 營收為 10 億元。
## 資料來源
{PRIMARY}
## 下次更新建議時機
下一季財報後更新。[S1]
"""
        note = analyse(sign(text))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("沒有任何可稽核 claim block" in error for error in note["quality_errors"]))

    def test_deletion_only_partial_signoff_needs_no_surviving_citation(self):
        text = """# 1234 測試
<!-- meta
stock_id: 1234
template_version: 1
verification_status: partially_verified
drafted_by: writer-a
last_updated: 2026-07-11
next_review: 2026-10-01
reviewed_by: reviewer-b
reviewed_at: 2026-07-11
review_scope: confirmed_correction_deletion_only
reviewed_content_sha256:
-->
## 業務概況
這一節仍是尚未完成全文查核的舊內容。
"""
        note = analyse(sign(text))
        self.assertEqual("partially_verified", note["verification"])
        self.assertEqual([], note["quality_errors"])

    def test_unknown_and_duplicate_source_ids_are_errors(self):
        text = f"""# 1234 測試
<!-- meta
stock_id: 1234
template_version: 1
last_updated: 2026-07-11
-->
## 業務概況
公司營收 10 億元。[S2]
## 資料來源
{PRIMARY}
{PRIMARY}
"""
        note = analyse(text)
        self.assertTrue(any("未定義來源：S2" in error for error in note["quality_errors"]))
        self.assertTrue(any("重複定義：S1" in error for error in note["quality_errors"]))

    def test_primary_source_requires_document_date_and_precise_locator(self):
        bad_source = (
            "- [S1] **一手**｜公司財務報告｜首頁｜https://example.com/report.pdf"
        )
        text = f"""# 1234 測試
<!-- meta
stock_id: 1234
template_version: 1
last_updated: 2026-07-11
-->
## 業務概況
公司營收 10 億元。[S1]
## 資料來源
{bad_source}
"""
        note = analyse(text)
        self.assertTrue(any("必須含發布、資料或擷取年份" in error for error in note["quality_errors"]))
        self.assertTrue(any("缺頁碼、表格或章節定位" in error for error in note["quality_errors"]))

    def test_invalid_real_date_is_rejected(self):
        text = """# 1234 測試
<!-- meta
stock_id: 1234
template_version: 1
last_updated: 2026-99-99
-->
## 業務概況
測試公司從事產品銷售。
"""
        note = analyse(text)
        self.assertTrue(any("不是合法" in error for error in note["quality_errors"]))
        self.assertEqual("draft", qual_notes.note_status(note, "2026-07-11"))

    def test_conflicted_requires_two_sources_and_explicit_conflict(self):
        text = f"""# 1234 測試
<!-- meta
stock_id: 1234
template_version: 2
verification_status: conflicted
drafted_by: writer-a
last_updated: 2026-07-11
next_review: 2026-07-20
reviewed_by: reviewer-b
reviewed_at: 2026-07-11
review_scope: conflicting_revenue_period
reviewed_content_sha256:
conflict_summary: 公司與交易所對營收期間標示不同
-->
## 未決衝突
公司文件將數字標為第一季。[S1] 交易所公告將同一數字標為前四月。[S2]
## 證據索引與資料來源
{PRIMARY}
{PRIMARY_2}
"""
        note = analyse(sign(text))
        self.assertEqual("conflicted", note["verification"])
        self.assertEqual([], note["quality_errors"])

        broken = text.replace("conflict_summary: 公司與交易所對營收期間標示不同", "conflict_summary:")
        note = analyse(sign(broken))
        self.assertEqual("conflicted", note["verification"])
        self.assertTrue(note["quality_invalid"])
        self.assertTrue(any("conflict_summary" in error for error in note["quality_errors"]))

        hidden_refs = text.replace(
            "公司文件將數字標為第一季。[S1] 交易所公告將同一數字標為前四月。[S2]",
            "公司文件與交易所公告的期間標示不同。<!-- hidden [S1][S2] -->",
        )
        note = analyse(sign(hidden_refs))
        self.assertEqual("conflicted", note["verification"])
        self.assertTrue(note["quality_invalid"])
        self.assertTrue(any("至少必須並列兩個來源" in error for error in note["quality_errors"]))

    def test_duplicate_meta_key_is_error(self):
        text = """# 1234 測試
<!-- meta
stock_id: 1234
stock_id: 1234
template_version: 1
last_updated: 2026-07-11
-->
## 業務概況
測試公司從事產品銷售。
"""
        note = analyse(text)
        self.assertTrue(any("meta key 重複" in error for error in note["quality_errors"]))

        second_meta = text + "\n<!-- meta\nstock_id: 1234\ntemplate_version: 1\n-->\n"
        note = analyse(second_meta)
        self.assertTrue(any("只能有一個 meta 區塊" in error for error in note["quality_errors"]))

    def test_unknown_future_template_version_is_rejected(self):
        text = independent_note().replace("template_version: 2", "template_version: 99")
        note = analyse(resign(text))
        self.assertEqual("ai_draft", note["verification"])
        self.assertTrue(any("高於目前可理解" in error for error in note["quality_errors"]))

    def test_freshness_does_not_change_verification(self):
        note = analyse(independent_note())
        note["next_review"] = "2026-07-10"
        self.assertEqual("due", qual_notes.note_status(note, "2026-07-11"))
        self.assertEqual("independently_verified", qual_notes.note_review_status(note))
        note["next_review"] = "2026-07-11"
        self.assertEqual("due", qual_notes.note_status(note, "2026-07-11"))

    def test_preamble_is_preserved_in_dashboard_sections(self):
        text = """# 1234 測試
<!-- meta
stock_id: 1234
template_version: 1
last_updated: 2026-07-11
-->
> Universe 歸屬有重要例外，讀者不可忽略。
## 業務概況
測試公司從事產品銷售。
"""
        note = analyse(text)
        self.assertEqual("研究定位與重要註記", note["sections"][0]["h"])

    def test_dashboard_parser_preserves_subheadings_and_ordered_lists(self):
        text = """# 1234 測試
<!-- meta
stock_id: 1234
template_version: 1
last_updated: 2026-07-11
next_review: 2026-10-01
-->
## 業務概況
### 驗證順序
1. 先核對財報。
2. 再核對法說。
"""
        note = analyse(text)
        blocks = note["sections"][0]["blocks"]
        self.assertEqual(["h3", "ol"], [block["t"] for block in blocks])
        self.assertEqual(2, len(blocks[1]["items"]))

    def test_windows_invalid_name_is_sanitized(self):
        self.assertEqual("愛普", qual_notes._safe_filename("愛普*"))

    def test_v2_scaffold_starts_as_clean_ai_draft(self):
        with open(qual_notes.TEMPLATE_MD, encoding="utf-8") as handle:
            text = handle.read()
        text = (text.replace("{{STOCK_ID}}", "1234")
                .replace("{{NAME}}", "測試")
                .replace("{{GROUP}}", "test")
                .replace("{{BIZ}}", "測試業務")
                .replace("{{TEMPLATE_VERSION}}", "2")
                .replace("{{TODAY}}", "2026-07-11"))
        note = analyse(text)
        self.assertEqual("ai_draft", note["verification"])
        self.assertEqual([], note["quality_errors"])
        self.assertEqual(0, note["claim_count"])

    def test_quality_ci_is_independent_from_daily_market_pipeline(self):
        with open(os.path.join(ROOT, "scripts", "run_daily.py"), encoding="utf-8") as handle:
            local_pipeline = handle.read()
        self.assertNotIn('run("qual_notes.py", "--lint")', local_pipeline)
        with open(os.path.join(ROOT, ".github", "workflows", "daily-fetch.yml"),
                  encoding="utf-8") as handle:
            daily_action = handle.read()
        self.assertNotIn("python scripts/qual_notes.py --lint", daily_action)
        with open(os.path.join(ROOT, ".github", "workflows", "qualitative-quality.yml"),
                  encoding="utf-8") as handle:
            quality_action = handle.read()
        self.assertIn("python scripts/qual_notes.py --lint", quality_action)
        self.assertIn("python -m unittest tests.test_qual_notes_quality", quality_action)
        self.assertGreaterEqual(quality_action.count('"config/universe.csv"'), 2)
        self.assertGreaterEqual(quality_action.count('"tests/test_dashboard_ux_contract.py"'), 2)

    def test_duplicate_stock_id_is_not_silently_overwritten(self):
        base = """# 測試
<!-- meta
stock_id: 1234
template_version: 1
last_updated: 2026-07-11
-->
## 業務概況
測試公司從事產品銷售。
"""
        with tempfile.TemporaryDirectory() as directory:
            for filename in ("1234_甲.md", "9999_乙.md"):
                with open(os.path.join(directory, filename), "w", encoding="utf-8") as handle:
                    handle.write(base)
            notes = qual_notes.load_notes(directory)
        self.assertEqual(1, len(notes))
        self.assertTrue(any("stock_id 1234 重複" in error for error in notes["1234"]["quality_errors"]))

    def test_lint_fails_when_universe_member_has_no_note(self):
        with mock.patch.object(qual_notes, "_load_universe", return_value=[{"stock_id": "1234"}]):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(1, qual_notes._lint({}))
            self.assertIn("universe 成員缺少質化研究筆記", output.getvalue())

    def test_missing_note_is_not_double_counted_as_ai_draft(self):
        universe = [{"stock_id": "1234", "name": "測試", "group": "test"}]
        with (mock.patch.object(qual_notes, "_load_universe", return_value=universe),
              mock.patch.object(qual_notes, "load_notes", return_value={})):
            rows = qual_notes._status_rows("2026-07-11")
        self.assertEqual("missing", rows[0]["status"])
        self.assertIsNone(rows[0]["verification"])


if __name__ == "__main__":
    unittest.main()
