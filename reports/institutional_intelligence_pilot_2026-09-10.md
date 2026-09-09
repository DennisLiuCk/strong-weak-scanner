# 機構市場情報試作與來源檢查 — 2026-09-10

研究前選題 commit：`1eb8b05`；本輪起始基準：`57fec56aa2a451f92a5e0a98e7a5501d53b1c9f3`。
本輪是三個既有市場議題的定向抽樣，不是全universe、全部公司筆記或機構報告普查。
採用官方可讀文章、逐字稿、研究發布稿與公司原文，不宣稱取得付費完整模型。

## 第一段：場址供電與液冷取捨

- 對應：`MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER` 新S25–S27、C32–C34、T9。
- 核對GS官方9/1日期、分析師署名、physical environment、區域限制、表後發電橋接原說法。
  原始HTML：`tmp/institutional-pilot-20260910/gs_20260901.html`，SHA256
  `775fab4de50852a456300078c02afc90d2fcfb902d6e13c2321edb28d2ab24b1`。
- 核對Microsoft官方6/22日期與能源／用水原段。直接HTTP403；官方web正文可讀，保存的是
  `web-source-extracts.json`工具文字截取，非原始HTML；SHA256
  `c08725f54bb3e6651ce2759eb73d6ac27042aca9413be39ff6f0a7268517f361`。
  明示建設計畫、初次充填、穩態範圍；不推成已營運、園區零用水或台廠訂單。
- Microsoft公開信明示Texas頁為進度入口；當日索引可見Pecos公開信，未把其他Texas
  場址施工代填Pecos。`microsoft-watch-extract.json` SHA256
  `67710699d3c2f6c30a083cd68bd57bb7cc01d83bdfc9c01ade7977222a5130a3`。
- GS與Microsoft是兩條發布鏈，但前者宏觀分析、後者單場址計畫，不能說完成同母體的
  預測驗證。未計算電力、用水或投資收益估計，SE／t不適用。
- 上述payload mode為唯讀，SHA可重算；這是版本固定與基本內容核對，不是正式個股
  focused evidence pack簽核，也不代表來源內容一定為真。
- macOS26.6.2 arm64／預設Python3.11.11（UTF-8 mode 0，未設PYTHONUTF8）及Node22.14.0：
  684項既有測試、六項lint與隔離重建通過，prepublish雜湊確認正式DB與舊archive未改。
  headless Chrome實開1440、390與320px，無頁面JS錯誤或水平溢出；已檢視桌機與手機畫面。
  原液冷內容測試將來源／claim／monitor的固定總數改為保留歷史下限，允許合法追加；
  舊內容逐項斷言與append-only baseline檢查仍完整保留。

## 第二段：AI支出、融資義務與現金回收

- 對應：`MI-2026-08-01-AI-CAPEX-CASH-CONVERSION` 新S23/S24、C28–C31、T6；重讀既有S1。
- S&P8/27官方發布稿列出六家指定公司（包含SpaceX）；核對FOCF預測期限、2028一般模型
  假設及文末非rating action說明。原HTML `sp_ratings_20260827.html` SHA256
  `9a267232a275876dec107603cd57879ed1b6588eabe32662c061215721524fd4`。
- Microsoft7/29法說核對useful-life update、finance/operating leases、FY27 FCF指引；
  當日IR索引可回到同一S1，後續法說日期尚未公布。沒有把S&P年度自行改成相同CY，
  也沒有把公司FCF和機構FOCF當成同一公式。保留兩份展望及待對帳缺口。
- 本次官方web工具文字截取（非原始HTML）`finance-critical-extract.json` SHA256
  `3a851e73bd9e3f89e8bcc1b1daf0bcbb51b346baf9146e57dbbabc265b08d166`；
  `finance-web-extract.json` SHA256
  `5f66dc7629b0664c007477f169d58c67029cf0c47076329db66849cdb3ae6f93`，payload均mode唯讀。
- C28為機構情境推論，C29/C30只證實公司公開說法；未新增跨公司總額或抽樣估計，
  SE/t不適用，公開稿沒有預測誤差帶。T6的10/31是人工工作回查日。
- 液冷commit整合期間遠端新增閱讀UI變更，保留雙方後重跑prepublish及三視口QA通過。
  此時預設macOS26.6.2／Python3.11.11測試數為685；融資段同環境執行，內容測試同樣
  保留原來源/主張/監看/transition下限及逐項歷史斷言，允許追加，不減弱baseline閘門。
- 融資段`finance-check-fixed`：685項測試、六lint、隔離重建及保護檔雜湊通過；
  Chrome1440/390/320px無JS錯誤與水平溢出，已目視1440與390畫面。
