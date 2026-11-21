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
        self.assertIn("if: steps.experiment_lab.outcome == 'success'", workflow[audit_at:dashboard_at])
        gate_at = workflow.index('- name: 實驗失敗標紅')
        self.assertLess(dashboard_at, commit_at)
        self.assertLess(commit_at, gate_at)
        commit = workflow[commit_at:gate_at]
        self.assertIn("if [ \"${{ steps.experiment_lab.outcome }}\" = \"success\" ]; then", commit)
        success, failure = commit.split('else', 1)
        failure = failure.split('fi', 1)[0]
        self.assertIn('git add reports/ index.html research.html', success)
        self.assertIn('git add reports/validate_*.md reports/validation_progress.json index.html research.html', failure)
        self.assertNotIn('experiment', failure)
        gate = workflow[gate_at:]
        self.assertIn("if: steps.experiment_lab.outcome == 'failure'", gate)
        self.assertIn('::error::', gate)
        self.assertIn('exit 1', gate)
