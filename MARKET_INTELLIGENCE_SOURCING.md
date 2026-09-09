# 機構市場情報：人工選題與基本驗證

用途是把可靠機構的新觀點，轉成可回查、可追蹤、與本 universe 有關的研究問題。
讀者產物仍放在既有 `notes/research_topics/`，經 builder 發布到研究中心；個股正式
筆記與 H# 仍依各自 runbook 簽核。本文件補充 `MARKET_RESEARCH_METHOD.md`，不取代它。

## 先選文件，再看機構招牌

| 來源層 | 本輪已讀的官方公開範例 | 可承擔的工作 | 必須保留的限制 |
|---|---|---|---|
| 全球投行研究 | [Goldman Sachs Exchanges，2026-09-01](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/the-outlook-for-data-center-power-demand-as-ai-token-use-grows)；[Morgan Stanley，2026-06-08](https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/high-cost-of-AI-memory-shawn-kim) | 找需求、成本與瓶頸的機制，以及研究者的分歧 | 官方逐字稿證明研究者說了什麼；預測不等於實績。公開稿通常不足以重算完整模型 |
| 評級機構的產業分析 | [S&P Global Ratings，2026-08-27 研究發布稿](https://press.spglobal.com/2026-08-27-AI-Infrastructure-Investment-To-Exceed-1-3-Trillion-By-2027,-S-P-Global-Ratings-Says) | 找現金流、契約義務、資本支出與融資風險 | 發布稿不是完整報告；信用風險觀點不能當成股票估值或買賣結論 |
| 供應鏈研究 | [S&P Global Market Intelligence，2026-07-28](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/behind-ai-boom-electronics-supply-side-constraints) | 找跨產品供需、材料成本與替代技術的反方 | Market Intelligence 與 Ratings 分開標示；同集團觀點不算兩條獨立消息鏈 |
| 公司、客戶與電網原始文件 | 公司 IR／監管申報／電網正式公告，依每篇主張另查 | 核對產品、支出、合約、時程及實際營運指標 | 管理層計畫仍是計畫；產品能力不能直接當成具名訂單或題材獲利 |

機構可靠度與主張證據力分開看。沒有作者、正式日期、可讀正文或清楚口徑的內容，
即使掛著知名機構名稱也只留搜尋線索。付費牆、403 或只有搜尋摘要時記錄取得限制，
不拼湊出「已讀報告」。新找到的舊文章標為背景，不能用捕捉日偽裝最新研究。

## 一次研究循環

1. **限定問題與範圍。** 預設找最近一至三個月；較舊來源只有在補機制、反方或原始基準時
   才採用。記錄實際搜尋日期窗與來源範圍；主題抽樣一律標 `partial`。
2. **尋找資訊增量。** 優先挑估計修訂、供應鏈瓶頸轉移、已知假說的反證、或可核對的
   公司新揭露。若只重複「AI 很強」而沒有新條件、新數據或下一份證據，暫不成文。
3. **研究前固定取捨。** 在 selection log 留研究順序、第一拒絕與下一份證據並獨立 commit。
   此順序只安排本輪工作，不是全市場優先序，更不是股票排名。
4. **逐文件基本驗證。** 打開官方正文，核對發布者／作者、正式日期、文件版本、引用位置、
   期間、幣別、單位、母體與預測期限。來源欄分開填 published／captured／accepted。
   保存原始 HTML 或取得方式明示的文字截取及 SHA 到 `tmp/`；雜湊固定取得版本，不證明內容為真。
5. **沿主張找獨立對照。** 至少一條機構研究鏈加一條公司、客戶、監管或其他原始鏈。
   同一聯合新聞稿、集團互引與媒體轉載不增加獨立性。主動找反方；查不到只是缺口。
6. **寫成短更新。** 先說新資料改變了什麼，再寫傳導機制、相關族群要查什麼、反例與下一個
   可觀察節點。數字無誤差範圍時標明來源未提供，不自行編造；來源模型估計不得套成統計檢定。
7. **對應既有類庫。** 優先補既有 topic；需要新問題才新建 v3。公司曝險不足就維持族群觀察。
   新增支線 claim 不刷新原主命題時鐘；原來源、修正鏈與到期警示完整保留。
8. **發布一段，驗收一段。** 每個完整主題更新含來源、claim、monitor、scan 與方法快照，
   重建首頁及研究中心，跑本轮起始 baseline 的 prepublish 閘門，檢查桌機／手機閱讀後
   中文 commit + push。確認 CI 與 Pages 對到已推送版本。

## 讀者應得到的內容

每段至少回答：來源何時說了什麼；它改變哪個判斷；哪些環節可能承壓或得到機會；
哪些公司證據仍缺；什麼結果會推翻判讀；下次要打開哪個官方入口。
「記憶體漲價」不能省略下游客戶成本，「資料中心需求成長」不能省略接電與驗收，
「資本支出增加」不能省略現金支出、租賃與收入回收之間的差別。

## 本輪試作與後續判斷

2026-09-10 的選題凍結為 `RS-2026-09-10-01`：依序補液冷／場址限制、AI 支出／融資、
記憶體／上下游成本三篇既有研究。這是定向抽樣；不代表重查了全站公司筆記或全部舊候選。
本輪先人工執行，不新增排程。

review 時看資訊是否有增量、原文是否能定位、事實與預測是否分清，以及下一步是否真的
能执行。後續若要自動化，可先自動發現官方新文件與做去重，保留人工作主張裁決；
是否值得採用，由這輪網站內容的實際品質決定。

## 已發布的試讀入口

從[研究雷達](https://dennisliuck.github.io/strong-weak-scanner/research.html#radar)可依凍結順序
進入三篇既有文章；各篇新增「9月10日機構情報」段。下次日期是人工查核待辦，不是排程。

| 問題與文章 | 本輪查核重點 | 後續文件／人工回查日 |
|---|---|---|
| [場址與液冷](https://dennisliuck.github.io/strong-weak-scanner/research.html#topic-MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER) | 高盛框架對照Microsoft場址計畫，分清計畫與實績 | Microsoft Texas／Pecos營運更新；10/10 |
| [AI支出與融資](https://dennisliuck.github.io/strong-weak-scanner/research.html#topic-MI-2026-08-01-AI-CAPEX-CASH-CONVERSION) | S&P預測與公司指引的期間、定義及版本分歧 | Microsoft IR新法說與財報；10/31 |
| [記憶體成本](https://dennisliuck.github.io/strong-weak-scanner/research.html#topic-MI-2026-08-02-AI-MEMORY-HIERARCHY) | 機構供需框架對照HP買方申報，保留供應改善反方 | 買方及記憶體公司新財報；10/1 |

來源取得方式、SHA、期間核對、失敗記錄及網站驗收見
[`reports/institutional_intelligence_pilot_2026-09-10.md`](reports/institutional_intelligence_pilot_2026-09-10.md)。
