"""入口文件契約:CLAUDE.md 與 AGENTS.md 必須完全相同。

兩檔曾被不同 session 各自更新而分岔,導致後續 agent 讀到的入口文件缺關鍵規範。
規則本身寫在 CLAUDE.md「鐵律」,這裡把它變成 CI 會擋下的契約,不再只靠人工 diff。
(以文字模式讀取 → 換行符已正規化,Windows CRLF 與 Linux LF 檢出皆適用。)
"""
import difflib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class EntryDocsSyncTest(unittest.TestCase):
    def test_claude_md_and_agents_md_identical(self):
        claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8").splitlines()
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8").splitlines()
        self.assertTrue(any(claude), "CLAUDE.md 不應為空")
        diff = list(difflib.unified_diff(claude, agents, "CLAUDE.md", "AGENTS.md",
                                        lineterm="", n=1))
        self.assertTrue(not diff, "CLAUDE.md 與 AGENTS.md 必須完全相同——改任一檔要同步"
                                  "另一檔:\n" + "\n".join(diff))


if __name__ == "__main__":
    unittest.main()
