# -*- coding: utf-8 -*-
"""產出的 index.html 沒有整塊消失(2026-07-26)。

`build_dashboard.py` 的可選區段(策略狀態、台積電專區、兩視角分歧、時間尺度)
都用 `except sqlite3.Error: return None` 包住。這個窄捕捉本身是對的——程式錯誤
還是會炸出來——但**資料層真的出事時,結果是頁面少掉一整塊、導覽留下死連結,
而 build 照印「已重生」、Actions 全綠、Pages 照常部署**。

CI 的 `tests.yml` 刻意不吃 `index.html`/`data/` 路徑(每交易日 3~4 個資料
commit,那些不改程式),所以既有的產出物斷言不會在每日管線上跑。這個檔就是要
被 `daily-fetch.yml` 直接點名執行的那一個:唯讀 index.html、純 stdlib、約 2 秒,
任何一塊掉了就讓 Actions 變紅。

對應鐵律:「push/rebase 衝突必須標紅,不得 exit 0」——同一個道理,
發布出去的東西壞了就不能靜悄悄。
"""
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
RESEARCH = ROOT / "research.html"

# (payload 變數名, section id, 導覽是否有連結, 人看得懂的名字)
SECTIONS = [
    ("STRATEGY", "strategy-status", False, "策略狀態"),
    ("RECENT", "recent", False, "研究中心入口"),
    ("TSMC", "tsmc", True, "台積電專區"),
    ("DIVERGE", "diverge", True, "兩視角分歧"),
    ("LENS", "lens", True, "時間尺度"),
]


class DashboardSectionsPresentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not INDEX.exists():
            raise unittest.SkipTest("index.html 尚未產生")
        cls.html = INDEX.read_text(encoding="utf-8")

    def test_no_placeholder_survived_the_build(self):
        """`__X_JSON__` 留在檔案裡代表 replace 沒對上,前端會直接語法錯誤。"""
        left = re.findall(r"__[A-Z_]+__", self.html)
        self.assertEqual(left, [], f"未被替換的 placeholder:{sorted(set(left))}")

    def test_every_optional_section_has_a_payload(self):
        dec = json.JSONDecoder()
        dead = []
        for var, _sid, _nav, name in SECTIONS:
            m = re.search(r"\b%s=" % var, self.html)
            self.assertIsNotNone(m, f"{name} 的 payload 變數 {var} 不在檔案裡")
            if dec.raw_decode(self.html, m.end())[0] is None:
                dead.append(name)
        self.assertEqual(dead, [], f"這些區段沒有 payload,頁面會少掉整塊:{dead}")

    def test_nav_links_point_at_sections_that_exist(self):
        """區段消失時導覽會留下點了沒反應的死連結。"""
        # 錨點不一定是靜態 <section>:策略狀態卡是 JS 在 render 時
        # `h('div',{id:'strategy-status'})` 建出來的,靜態檔裡只有 JS 字面值。
        # 兩種形式都接受;失敗訊息不要把整份 html 帶出來——它有好幾 MB。
        for href in sorted(set(re.findall(r'<a href="#([a-z-]+)"', self.html))):
            static = re.search(r'id="%s"' % re.escape(href), self.html)
            runtime = re.search(r"id:'%s'" % re.escape(href), self.html)
            self.assertTrue(static or runtime,
                            f"導覽指向 #{href},但頁面裡沒有任何地方建立這個 id")
        for _var, sid, nav, name in SECTIONS:
            if nav:
                self.assertIn(f'href="#{sid}"', self.html, f"{name} 的導覽連結不見了")

    def test_core_content_is_not_empty(self):
        """整份 payload 都在但個股是空的,同樣是壞頁面。"""
        dec = json.JSONDecoder()
        i = self.html.index("const DATA=")
        data = dec.raw_decode(self.html, i + len("const DATA="))[0]
        self.assertGreater(len(data), 50, f"只有 {len(data)} 檔,遠少於 universe 規模")
        groups = dec.raw_decode(self.html, self.html.index("GROUPS=", i) + len("GROUPS="))[0]
        self.assertGreater(len(groups), 5)

    def test_research_center_was_built_with_full_catalog(self):
        self.assertTrue(RESEARCH.exists(), "research.html 未產生，研究中心會是死連結")
        html = RESEARCH.read_text(encoding="utf-8")
        self.assertEqual(re.findall(r"__[A-Z_]+__", html), [], "研究中心仍有未替換 placeholder")
        dec = json.JSONDecoder()
        marker = "const LIB="
        start = html.index(marker) + len(marker)
        library = dec.raw_decode(html, start)[0]
        self.assertGreater(library.get("total", 0), 50)
        self.assertEqual(set(library.get("counts", {})), {"formal_note", "narrative", "topic"})
        self.assertTrue(all(article.get("sections") for article in library.get("articles", [])))


if __name__ == "__main__":
    unittest.main()
