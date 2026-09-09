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
