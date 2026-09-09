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

## 第三段：記憶體買方的供應、定價及利潤率

- 對應：`MI-2026-08-02-AI-MEMORY-HIERARCHY` 新S24–S27、C31–C35、T8。
- 核對Morgan Stanley6/8 Shawn Kim逐字稿中的分層採購框架；舊文明示作背景，
  不採缺口與需求占比預測數字。`ms_memory_20260608.html`原HTML SHA256
  `d0d377f02a6b7c1fa6cc8b2c9e1c427147d8383b634d23d684b2fbb289929e7a`。
- S&P MI7/28 Chris Rogers原文的壓縮／架構替代屬未來風險，未當成當期採購下降。
  直接HTTP403但官方web正文可讀；與Ratings同集團，不增加獨立消息鏈。
- HP10-Q的SEC index明列filing date8/27、accepted8/26 19:04:12及period7/31；
  MD&A頁40/45核對成本、季度同比及管理層歸因。獨立複核將草稿「毛利」改為
  「毛利率」，補上「去年同期」；與8/26公司稿的供應改善並存，沒有抹去反方。
  HP兩份文件屬同一公司/季度，不是兩個獨立買方；沒有隔離記憶體成本因果。
- 官方web文字截取（非原HTML）`memory-critical-extract.json` SHA256
  `9d29cd90043f3f03041c489660983601eab3746050a32a29c7c560c19d260dab`；
  `memory-web-extract.json` SHA256
  `fdb82425153b11d64e5907e9692676b0bf7430c4081ffa0751a671b6c02edc4a`，payload mode唯讀。
- 未新增財務點估計或抽樣统计，SE/t不適用。T8按買方壓力與賣方格式需求分別裁決，
  不把供應改善一概推成所有記憶體公司不受惠；C8及舊時鐘未刷新。
- macOS26.6.2／預設Python3.11.11：685項測試、六lint、隔離build及保護檔雜湊通過。
  Chrome1440/390/320px無JS錯誤與水平溢出，已目視桌機與手機。內容測試允許追加，
  思考問題測試以該節真正邊界取文，保留原白話與歷史證據斷言。

## 本輪發布與總驗收

| 完成段落 | 獨立commit | 遠端結果 |
|---|---|---|
| 方法與研究前選題 | `1eb8b05` | 已push |
| 場址供電與液冷 | `639e81c` | 已push；tests、qualitative-quality及Pages成功 |
| AI融資與現金回收 | `1492451` | 已push；tests、qualitative-quality及Pages成功 |
| 記憶體成本與買方 | `74b24b4` | 已push；tests、qualitative-quality及Pages成功 |

- 新active radar為`RADAR-2026-09-10-01`；三題以`expand_existing`連回文章，原8月雷達
  退役保存。研究前排名、第一拒絕及下一份證據逐字保留，沒有用研究結果重排。
- 修正原分類將`advance → expand_existing`誤算成研究後拒絕的問題；本輪為三題擴充，
  零題新文章/圖譜升格、零題拒絕。這是工作結果分類，非研究命中或投資勝率。
  watch/defer後的實際轉向另列；舊帳本與方法snapshot未改寫，新建`2026-09-10_04.json`。
- 網站從雷達或族群矩陣進入增量文章時，文案如實說明新資料補進既有文章。
  方法及维护文件接入機構取材流程，後續查核日期只是人工待辦，本輪未建立自動排程。
- 最終`final-check`以起始baseline執行：macOS26.6.2 arm64、預設Python3.11.11
  （UTF-8 mode0、未設PYTHONUTF8）、Node22.14.0，692項測試、六lint與隔離重建通過；
  正式DB及46份既有archive受保護檔雜湊均不變。
- `radar-final.json`：Chrome在1440、390與320px分別實開三張候選卡、對應新段落，
  並使用桌機或手機的實際返回控制回同一雷達；無JS錯誤或水平溢出。
  已目視桌機/手機雷達及三篇新段落；頁面閱讀分鐘屬整篇既有文章，本輪可先讀
  各篇大綱中的「9月10日機構情報」段。
- 來源報告列入的全部payload重算SHA吻合，mode皆無寫入位元；tmp存檔未入版控。
  這輪完成基本來源驗證與內容複核，沒有宣稱重新簽核全站正式公司筆記。
