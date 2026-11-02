"""Work-date advancement cannot masquerade as resolved evidence."""
import datetime as dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from research_method_audit import monitor_review_progress

class ReviewProgressTest(unittest.TestCase):
    def topic(self, status='triaged'):
        return {'topic_id':'topic', 'status':status, 'monitoring':[
            {'monitor_id':'T1','status':'active'},
            {'monitor_id':'T2','status':'active'},
            {'monitor_id':'T3','status':'retired'}]}

    def row(self, day, result='not_yet_testable', monitor='T1', suffix=''):
        return dict(topic_id='topic',monitor_id=monitor,checked_at=day,
                    result=result,review_id=day+suffix)

    def test_no_reviews_is_not_no_evidence(self):
        got=monitor_review_progress([self.topic()],[],dt.date(2026,11,2))
        self.assertEqual(got['latestOutcomeCounts']['never_reviewed'],2)
        self.assertEqual(got['latestOutcomeCounts']['no_new_evidence'],0)
        self.assertEqual(got['notYetTestableRuns'],[])

    def test_same_day_does_not_inflate_run_and_future_excluded(self):
        rows=[self.row('2026-10-28'),self.row('2026-10-28',suffix='B'),
              self.row('2026-10-31'),self.row('2026-11-05','new_support')]
        got=monitor_review_progress([self.topic()],rows,dt.date(2026,11,2))
        self.assertEqual(got['notYetTestableRuns'][0]['consecutiveCheckDates'],2)
        self.assertEqual(got['notYetTestableRuns'][0]['lastCheckedAt'],'2026-10-31')

    def test_no_new_evidence_breaks_run_but_is_not_support(self):
        rows=[self.row('2026-10-20'),self.row('2026-10-22','no_new_evidence'),self.row('2026-10-28')]
        got=monitor_review_progress([self.topic()],rows,dt.date(2026,11,2))
        self.assertEqual(got['notYetTestableRuns'][0]['consecutiveCheckDates'],1)
        self.assertEqual(got['latestOutcomeCounts']['new_support'],0)

    def test_retired_and_closed_excluded_and_inputs_unchanged(self):
        topic=self.topic()
        before=repr(topic)
        rows=[self.row('2026-10-20',monitor='T3')]
        got=monitor_review_progress([topic],rows,dt.date(2026,11,2))
        self.assertEqual(sum(got['latestOutcomeCounts'].values()),2)
        self.assertEqual(repr(topic),before)
        self.assertEqual(sum(monitor_review_progress([self.topic('resolved')],rows,dt.date(2026,11,2))['latestOutcomeCounts'].values()),0)

    def test_latest_support_is_work_outcome_not_thesis_success(self):
        rows=[self.row('2026-10-20'),self.row('2026-10-28','new_support')]
        got=monitor_review_progress([self.topic()],rows,dt.date(2026,11,2))
        self.assertEqual(got['latestOutcomeCounts']['new_support'],1)
        self.assertEqual(got['notYetTestableRuns'],[])
        self.assertIn('不代表主命題真假',got['boundary'])

if __name__=='__main__':
    unittest.main()
