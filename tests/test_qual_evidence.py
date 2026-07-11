import base64
import copy
import json
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import qual_evidence  # noqa: E402


REAL_PDF_PAGE_COUNT = qual_evidence._pdf_page_count
ONE_PIXEL_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
)


class QualitativeEvidenceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.temp = Path(temporary.name)
        page_counter = mock.patch.object(qual_evidence, "_pdf_page_count", return_value=5)
        page_counter.start()
        self.addCleanup(page_counter.stop)

    def _inputs(self, count=3):
        sources = {}
        urls = {}
        pages = {}
        page_counts = {}
        roles = {}
        page_specs = ("1,3", "2-4", "5")
        for index in range(1, count + 1):
            source_id = f"S{index}"
            source = self.temp / f"{source_id}.pdf"
            source.write_bytes(
                b"%PDF-1.4\n"
                + f"fake evidence {source_id}\n".encode("ascii")
                + b"%%EOF\n"
            )
            sources[source_id] = str(source)
            urls[source_id] = f"https://example.test/{source_id}.pdf"
            pages[source_id] = page_specs[index - 1] if index <= 3 else "1"
            page_counts[source_id] = "5"
        if count == 3:
            roles = {
                "S1": "annual_report,annual_financials",
                "S2": "latest_quarterly_report",
                "S3": "latest_investor_conference",
            }
        else:
            role_values = (
                "annual_report",
                "annual_financials",
                "latest_quarterly_report",
                "latest_investor_conference",
                "shareholder_meeting",
            )
            roles = {
                f"S{index}": role_values[min(index - 1, len(role_values) - 1)]
                for index in range(1, count + 1)
            }
        return sources, urls, pages, page_counts, roles

    def _build(self, count=3, case="default"):
        sources, urls, pages, page_counts, roles = self._inputs(count)
        return qual_evidence.build_pack(
            "1234",
            "2026-07-11",
            sources,
            urls,
            pages,
            page_counts,
            roles,
            pack_root=self.temp / case / "packs",
            manifest_out=self.temp / case / "manifest.json",
        )

    def test_build_and_verify_three_fake_pdfs(self):
        manifest, pack_dir, manifest_path = self._build()

        self.assertEqual(qual_evidence.SCHEMA, manifest["schema"])
        self.assertEqual(qual_evidence.RESEARCH_PROFILE, manifest["research_profile"])
        self.assertEqual(qual_evidence.manifest_digest(manifest), manifest["pack_sha256"])
        self.assertEqual(manifest["pack_sha256"], pack_dir.name)
        self.assertEqual(["S1", "S2", "S3"], [item["id"] for item in manifest["documents"]])
        self.assertEqual(
            ["annual_report", "annual_financials"], manifest["documents"][0]["roles"]
        )
        self.assertEqual([1, 3], manifest["documents"][0]["cited_pages"])
        self.assertEqual([1, 2, 3, 4], manifest["documents"][0]["rendered_pages"])
        self.assertEqual([2, 3, 4], manifest["documents"][1]["cited_pages"])
        self.assertEqual([1, 2, 3, 4, 5], manifest["documents"][1]["rendered_pages"])
        self.assertEqual([5], manifest["documents"][2]["cited_pages"])
        self.assertEqual([4, 5], manifest["documents"][2]["rendered_pages"])

        loaded, errors = qual_evidence.verify_pack(pack_dir)
        self.assertEqual([], errors)
        self.assertEqual(manifest["pack_sha256"], loaded["pack_sha256"])
        self.assertEqual(manifest, qual_evidence.load_manifest(manifest_path))
        for document in manifest["documents"]:
            copied = pack_dir / document["file"]
            self.assertTrue(copied.is_file())
            self.assertEqual(0, stat.S_IMODE(copied.stat().st_mode) & 0o222)
            self.assertEqual(document["sha256"], qual_evidence._sha256_file(copied))
            self.assertEqual(document["size_bytes"], copied.stat().st_size)

    def test_verify_detects_document_and_manifest_tampering(self):
        manifest, pack_dir, _ = self._build(case="document-tamper")
        target = pack_dir / "documents" / "S2.pdf"
        os.chmod(target, stat.S_IRUSR | stat.S_IWUSR)
        target.write_bytes(target.read_bytes() + b"tampered")

        _, errors = qual_evidence.verify_pack(pack_dir)
        self.assertTrue(any("S2 文件大小不一致" in error for error in errors))
        self.assertTrue(any("S2 文件 SHA-256 不一致" in error for error in errors))

        manifest, pack_dir, _ = self._build(case="manifest-tamper")
        manifest["documents"][0]["url"] = "https://example.test/replaced.pdf"
        os.chmod(pack_dir / "manifest.json", stat.S_IRUSR | stat.S_IWUSR)
        (pack_dir / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )

        _, errors = qual_evidence.verify_pack(pack_dir)
        self.assertTrue(any("pack_sha256 不一致" in error for error in errors))

    def test_focused_profile_accepts_three_to_five_sources_only(self):
        for count in (2, 6):
            with self.subTest(count=count):
                with self.assertRaisesRegex(qual_evidence.EvidenceError, "3-5"):
                    self._build(count=count, case=f"invalid-{count}")

        manifest, pack_dir, _ = self._build(count=5, case="five-sources")
        self.assertEqual(5, len(manifest["documents"]))
        _, errors = qual_evidence.verify_pack(pack_dir)
        self.assertEqual([], errors)

    def test_roles_are_required_and_same_pack_rebuild_is_idempotent(self):
        sources, urls, pages, page_counts, roles = self._inputs(3)
        roles["S3"] = "shareholder_meeting"
        with self.assertRaisesRegex(qual_evidence.EvidenceError, "latest_investor_conference"):
            qual_evidence.build_pack(
                "1234", "2026-07-11", sources, urls, pages, page_counts, roles,
                pack_root=self.temp / "bad-role" / "packs",
                manifest_out=self.temp / "bad-role" / "manifest.json",
            )

        first, first_pack, first_manifest = self._build(case="idempotent")
        second, second_pack, second_manifest = self._build(case="idempotent")
        self.assertEqual(first, second)
        self.assertEqual(first_pack, second_pack)
        self.assertEqual(first_manifest, second_manifest)

        malformed = copy.deepcopy(first)
        del malformed["documents"][0]["size_bytes"]
        errors = qual_evidence.validate_manifest(malformed)
        self.assertTrue(any("size_bytes" in error for error in errors))

        sources, urls, pages, page_counts, roles = self._inputs(3)
        sources["S3"] = sources["S1"]
        urls["S3"] = urls["S1"]
        with self.assertRaisesRegex(qual_evidence.EvidenceError, "重複"):
            qual_evidence.build_pack(
                "1234", "2026-07-11", sources, urls, pages, page_counts, roles,
                pack_root=self.temp / "duplicate" / "packs",
                manifest_out=self.temp / "duplicate" / "manifest.json",
            )

    def test_cited_pages_expand_by_one_and_collapse_to_ranges(self):
        self.assertEqual([1, 3, 4, 5, 7], qual_evidence.parse_pages("7,3-5,1,4"))
        expanded = qual_evidence.expanded_render_pages([1, 4, 8], page_count=8)
        self.assertEqual([1, 2, 3, 4, 5, 7, 8], expanded)
        self.assertEqual(
            [{"first": 1, "last": 5}, {"first": 7, "last": 8}],
            qual_evidence.collapse_ranges(expanded),
        )
        self.assertEqual([], qual_evidence.collapse_ranges([]))

        for value in ("", "0", "4-2", "x", "2-x"):
            with self.subTest(value=value):
                with self.assertRaises(qual_evidence.EvidenceError):
                    qual_evidence.parse_pages(value)

        manifest, _, _ = self._build(case="rendered-page-contract")
        broken = copy.deepcopy(manifest)
        broken["documents"][0]["rendered_pages"] = [1, 3]
        errors = qual_evidence.validate_manifest(broken)
        self.assertTrue(any("引用頁及前後一頁" in error for error in errors))

    def test_verify_rejects_extra_payload_and_wrong_content_address(self):
        _, pack_dir, _ = self._build(case="extra-payload")
        documents_dir = pack_dir / "documents"
        os.chmod(documents_dir, 0o755)
        extra = documents_dir / "extra"
        extra.mkdir()
        os.chmod(extra, 0o555)
        os.chmod(documents_dir, 0o555)
        _, errors = qual_evidence.verify_pack(pack_dir)
        self.assertTrue(any("未列項目" in error for error in errors))

        _, pack_dir, _ = self._build(case="wrong-address")
        renamed = pack_dir.with_name("wrong-address")
        pack_dir.rename(renamed)
        _, errors = qual_evidence.verify_pack(renamed)
        self.assertTrue(any("完整 pack_sha256" in error for error in errors))

    def test_pdfinfo_parser_and_claimed_page_count_are_checked(self):
        executable = self.temp / "pdfinfo.exe"
        executable.write_bytes(b"fake executable")
        completed = subprocess.CompletedProcess(
            [str(executable)], 0, stdout="Pages:          5\n", stderr=""
        )
        with (
            mock.patch.object(qual_evidence.shutil, "which", return_value=str(executable)),
            mock.patch.object(qual_evidence.subprocess, "run", return_value=completed) as run,
        ):
            self.assertEqual(5, REAL_PDF_PAGE_COUNT(self.temp / "S1.pdf", pdfinfo=executable))
        self.assertFalse(run.call_args.kwargs["shell"])
        self.assertTrue(run.call_args.kwargs["check"])

        with mock.patch.object(qual_evidence, "_pdf_page_count", return_value=4):
            with self.assertRaisesRegex(qual_evidence.EvidenceError, "實際 4"):
                self._build(case="wrong-page-count")

    def test_render_pack_mocks_poppler_and_creates_only_planned_pages(self):
        manifest, pack_dir, _ = self._build(case="render")
        executable = self.temp / "pdftoppm.exe"
        executable.write_bytes(b"fake executable")

        def create_png(command, **_kwargs):
            Path(str(command[-1]) + ".png").write_bytes(ONE_PIXEL_PNG)
            return subprocess.CompletedProcess(command, 0)

        with (
            mock.patch.object(qual_evidence.shutil, "which", return_value=str(executable)),
            mock.patch.object(
                qual_evidence.subprocess,
                "run",
                autospec=True,
                side_effect=create_png,
            ) as run,
        ):
            plan = qual_evidence.render_pack(
                pack_dir,
                pdftoppm=str(executable),
                dpi=123,
                timeout_seconds=9,
            )

        expected_calls = sum(len(item["rendered_pages"]) for item in manifest["documents"])
        self.assertEqual(expected_calls, run.call_count)
        self.assertEqual(manifest["pack_sha256"], plan["pack_sha256"])
        self.assertEqual(
            [{"first": 1, "last": 4}],
            plan["documents"][0]["ranges"],
        )
        for call in run.call_args_list:
            command = call.args[0]
            self.assertEqual(str(executable), command[0])
            self.assertIn("-singlefile", command)
            self.assertEqual("123", command[command.index("-r") + 1])
            self.assertEqual(
                command[command.index("-f") + 1],
                command[command.index("-l") + 1],
            )
            self.assertFalse(call.kwargs["shell"])
            self.assertTrue(call.kwargs["check"])
            self.assertEqual(9, call.kwargs["timeout"])

        _, errors = qual_evidence.verify_pack(pack_dir, require_renders=True)
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
