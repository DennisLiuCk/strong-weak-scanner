"""Expiry review must preserve evidence freshness and source-date boundaries."""
import csv
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEWS = ROOT / 'notes/research_method_reviews'


def records(path, kind):
    text = (ROOT / path).read_text(encoding='utf8')
    return [dict((k.strip(), v.strip()) for k, v in
                 (line.split(':', 1) for line in body.splitlines() if ':' in line))
            for body in re.findall(r'<!-- ' + kind + r'\s*\n(.*?)-->', text, re.S)]


class EveningExpiryReviewTest(unittest.TestCase):
    def test_work_reviews_do_not_clear_evidence_expiry(self):
        before = json.loads((REVIEWS / '2026-10-08_01.json').read_text(encoding='utf8'))
        after = json.loads((REVIEWS / '2026-10-08_02.json').read_text(encoding='utf8'))
        self.assertEqual(before['monitors']['dueOrOverdue'], 63)
        self.assertEqual(after['monitors']['dueOrOverdue'], 0)
        self.assertEqual(after['freshness'], before['freshness'])
        self.assertEqual(after['freshness']['staleTopics'], 39)
        self.assertEqual(after['corrections']['monitorReviewEvents'] -
                         before['corrections']['monitorReviewEvents'], 63)
        self.assertEqual(after['claims']['active'] - before['claims']['active'], 3)
        with (REVIEWS / 'monitor_reviews.csv').open(encoding='utf8', newline='') as f:
            rows = [r for r in csv.DictReader(f)
                    if r['review_id'].startswith('MR-2026-10-08-EVENING-')]
        self.assertEqual(len(rows), 63)
        self.assertEqual(len({(r['topic_id'], r['monitor_id']) for r in rows}), 63)
        self.assertEqual(Counter(r['result'] for r in rows),
                         {'new_support': 2, 'no_new_evidence': 3, 'not_yet_testable': 58})
        for row in rows:
            self.assertIn('原工作期限：', row['notes'])
            self.assertIn('待補：', row['notes'])
            self.assertIn('查核入口：', row['notes'])
            self.assertGreater(row['next_check'], row['checked_at'])
            if row['result'] != 'new_support':
                self.assertEqual(row['claim_action'], 'none')
                self.assertEqual(row['evidence_source_ids'], '')

    def test_novara_update_is_partial_restart_not_a_q2_thesis_refresh(self):
        path = 'notes/research_topics/2026-07-31_missed_priority_q2_disclosures.md'
        meta = records(path, 'research_topic')[0]
        self.assertEqual((meta['thesis_claim_id'], meta['last_reviewed_at'],
                          meta['review_due'], meta['base_confidence']),
                         ('C19', '2026-08-14', '2026-08-19', 'medium'))
        sources = {r['source_id']: r for r in records(path, 'research_source')}
        self.assertEqual(sources['S31']['published_at'], '2026-09-14')
        self.assertEqual(sources['S32']['published_at'], '2026-10-07')
        self.assertEqual(sources['S31']['independence_group'], sources['S32']['independence_group'])
        claim = next(r for r in records(path, 'research_claim') if r['claim_id'] == 'C36')
        self.assertEqual(set(claim['supporting_source_ids'].split(',')), {'S31', 'S32'})
        self.assertIn('部分復工', claim['claim'])
        self.assertTrue(claim['boundary'])

    def test_old_bmc_report_is_not_a_new_deployment_or_complete_assurance(self):
        path = 'notes/research_topics/2026-08-08_ai_rack_trust_root.md'
        meta = records(path, 'research_topic')[0]
        self.assertEqual((meta['thesis_claim_id'], meta['last_reviewed_at'],
                          meta['review_due'], meta['base_confidence']),
                         ('C7', '2026-08-08', '2026-08-31', 'medium'))
        sources = {r['source_id']: r for r in records(path, 'research_source')}
        self.assertEqual(sources['S13']['published_at'], '2025-10-10')
        self.assertEqual(sources['S13']['accepted_at'], '2026-10-08')
        self.assertEqual(sources['S14']['published_at'], '')
        self.assertEqual(sources['S13']['independence_group'], sources['S14']['independence_group'])
        claims = {r['claim_id']: r for r in records(path, 'research_claim')}
        self.assertIn('2025-10-09', claims['C19']['claim'])
        self.assertIn('未讀長式報告', claims['C19']['boundary'])
        self.assertIn('未來要求', claims['C20']['claim'])
        self.assertIn('並非本輪查得的發布日', claims['C20']['boundary'])

    def test_single_day_census_keeps_missing_dates_and_prior_scan(self):
        with (ROOT / 'notes/research_topics/scan_log.csv').open(encoding='utf8', newline='') as f:
            scans = {r['scan_id']: r for r in csv.DictReader(f)}
        old = scans['scan-2026-10-08-version-and-paired-evidence']
        new = scans['scan-2026-10-08-evening-expiry-review']
        self.assertIn('63個原到期項未查仍逾期', old['coverage_note'])
        self.assertEqual(new['scope'], 'partial')
        self.assertIn('各缺10/4、5、6、8', new['coverage_note'])
        self.assertIn('19筆公告涉及15公司', new['coverage_note'])
        self.assertIn('其餘16篇只盤點時鐘與待辦', new['coverage_note'])


if __name__ == '__main__':
    unittest.main()
