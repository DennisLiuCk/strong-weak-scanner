from pathlib import Path
import unittest


class WeeklyLabWorkflowTest(unittest.TestCase):
    def test_lab_failure_publishes_formal_reports_before_failing_job(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / '.github/workflows/weekly-validate.yml').read_text(encoding='utf-8')
        lab_at = workflow.index('- name: 更新短週期實驗比較與固定檢視')
        audit_at = workflow.index('- name: 獨立核對短週期實驗數值')
        dashboard_at = workflow.index('- name: 同步首頁')
        commit_at = workflow.index('- name: commit 報告')
        lab = workflow[lab_at:audit_at]
        self.assertIn('id: experiment_lab', lab)
        self.assertIn('continue-on-error: true', lab)
        audit = workflow[audit_at:dashboard_at]
        self.assertIn("if: steps.experiment_lab.outcome == 'success'", audit)
        self.assertIn('id: audit_experiment_lab', audit)
        self.assertIn('continue-on-error: true', audit)
        gate_at = workflow.index('- name: 實驗失敗標紅')
        self.assertLess(dashboard_at, commit_at)
        self.assertLess(commit_at, gate_at)
        commit = workflow[commit_at:gate_at]
        stage_at = commit.index('git add reports/ index.html research.html')
        failure_at = commit.index('if [ "${{ steps.experiment_lab.outcome }}" != "success" ] || [ "${{ steps.audit_experiment_lab.outcome }}" != "success" ]; then')
        self.assertLess(stage_at, failure_at)
        failure = commit[failure_at:].split('fi', 1)[0]
        self.assertIn('git reset -q -- reports/experiment_lab.json reports/experiment_lab.html reports/experiment_reviews/ reports/experiment_lab_acceptance.json', failure)
        self.assertIn('git push', commit)
        gate = workflow[gate_at:]
        self.assertIn("if: steps.experiment_lab.outcome == 'failure' || steps.audit_experiment_lab.outcome == 'failure'", gate)
        self.assertIn('::error::experiment_lab 更新失敗', gate)
        self.assertIn('::error::audit_experiment_lab 核對失敗', gate)
        self.assertIn('[ "${{ steps.experiment_lab.outcome }}" = "failure" ]', gate)
        self.assertIn('[ "${{ steps.audit_experiment_lab.outcome }}" = "failure" ]', gate)
        self.assertIn('exit 1', gate)
