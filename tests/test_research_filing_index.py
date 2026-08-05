# -*- coding: utf-8 -*-
"""MOPS direct filing-index parser and input contract."""
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import research_filing_index as filing_index


SAMPLE_HTML = """
<table>
<tr><th>證券代號</th><th>資料年度</th><th>資料類型</th><th>結案類型</th>
<th>性質</th><th>資料細節說明</th><th>備註</th><th>電子檔案</th>
<th>檔案大小</th><th>上傳日期</th><th>財務報告更(補)正</th></tr>
<tr><td>8261</td><td>115 年 第二季</td><td>財務報告書</td><td>&nbsp;</td>
<td>&nbsp;</td><td>IFRSs合併財報</td><td>&nbsp;</td>
<td><a>202602_8261_AI1.pdf</a></td><td>1,410,794</td>
<td>115/08/05 15:04:16</td><td>無</td></tr>
<tr><td>8261</td><td>115 年 第二季</td><td>財務報告書</td><td>&nbsp;</td>
<td>&nbsp;</td><td>IFRSs英文版-合併財報</td><td>&nbsp;</td>
<td><a>202602_8261_AIA.pdf</a></td><td>874,379</td>
<td>115/08/05 15:06:59</td><td>無</td></tr>
</table>
"""


class ResearchFilingIndexTest(unittest.TestCase):
    def test_parser_preserves_filename_size_time_and_download_locator(self):
        filings = filing_index.parse_filing_index_html(
            SAMPLE_HTML, stock_id="8261", year=115, season=2,
        )
        self.assertEqual(len(filings), 2)
        self.assertEqual(filings[0]["filename"], "202602_8261_AI1.pdf")
        self.assertEqual(filings[0]["sizeBytes"], 1_410_794)
        self.assertEqual(filings[0]["uploadedAtRoc"], "115/08/05 15:04:16")
        self.assertIn("step=9", filings[0]["downloadUrl"])
        self.assertIn("filename=202602_8261_AI1.pdf", filings[0]["downloadUrl"])

    def test_parser_accepts_explicit_no_data_page_as_empty_index_result(self):
        filings = filing_index.parse_filing_index_html(
            "<h4>查無所需資料</h4>", stock_id="6488", year=115, season=2,
        )
        self.assertEqual(filings, [])

    def test_parser_rejects_unexpected_page_instead_of_calling_it_no_filing(self):
        with self.assertRaises(filing_index.FilingIndexError):
            filing_index.parse_filing_index_html(
                "<html><title>maintenance</title></html>",
                stock_id="6488", year=115, season=2,
            )

    def test_parser_rejects_unparseable_size_in_a_filing_row(self):
        broken = SAMPLE_HTML.replace("1,410,794", "unknown", 1)
        with self.assertRaises(filing_index.FilingIndexError):
            filing_index.parse_filing_index_html(
                broken, stock_id="8261", year=115, season=2,
            )

    def test_stock_ids_must_be_unique_and_in_universe(self):
        universe = {"8261": "富鼎", "6488": "環球晶"}
        self.assertEqual(
            filing_index.parse_stock_ids("8261,6488", universe),
            ["8261", "6488"],
        )
        with self.assertRaises(filing_index.FilingIndexError):
            filing_index.parse_stock_ids("8261,8261", universe)
        with self.assertRaises(filing_index.FilingIndexError):
            filing_index.parse_stock_ids("9999", universe)

    def test_index_url_keeps_period_and_company_explicit(self):
        url = filing_index.build_index_url("8261", 115, 2)
        self.assertIn("co_id=8261", url)
        self.assertIn("year=115", url)
        self.assertIn("seamon=2", url)
        self.assertIn("mtype=A", url)

    def test_runbooks_route_direct_mops_checks_through_the_tool(self):
        for name in ("RESEARCH_MAINTENANCE.md", "MARKET_RESEARCH_METHOD.md"):
            content = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("research_filing_index.py", content)
            self.assertIn("索引", content)


if __name__ == "__main__":
    unittest.main()
