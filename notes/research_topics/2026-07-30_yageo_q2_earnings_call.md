# 國巨 2026Q2 法說：毛利率、AI 組合與被動元件需求更新

<!-- research_topic
topic_id: MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-07-30
source_published_at: 2026-07-29
last_reviewed_at: 2026-08-09
review_due: 2026-08-15
source_type: official_company
publisher: YAGEO Group
publisher_domain: yageogroup.com
canonical_url: https://yageogroup.com/SalesResources/ResourceLibrary/item/19061
source_chain_id: yageo-2q26-earnings-call-20260729
stock_ids: 2327
group_ids: passive
trigger_type: quarterly_results_and_earnings_call
evidence_role: candidate_source
route: formal_note_candidate
thesis_claim_id: C5
base_confidence: medium
confidence_basis: Q2 營收可由國巨簡報與 TWSE 個股報告兩條獨立官方鏈交叉重算；毛利、AI 組合與價格歸因仍主要來自公司簡報，完整核閱季報附註、價格範圍、交期與稼動率仍待補
cross_company_numbers: false
schema_migrated_at: 2026-08-02
-->

<!-- transition
date: 2026-07-30
from: initial
to: inbox
reason: caught_by_official_event_calendar_backfill_after_priority_scan_omission
evidence: source_chain:yageo-2q26-earnings-call-20260729
-->
<!-- transition
date: 2026-07-30
from: inbox
to: triaged
reason: official_q2_deck_directly_hits_registered_h1_h2_proof_points
evidence: sources:S1,S2
-->
<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: twse_stock_report_independently_reconciled_q2_revenue_without_overstating_full_filing_coverage
evidence: sources:S2,S4
-->
<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave8_learning_no_conclusion_change
evidence: editorial:plain_language_wave8
-->
<!-- transition
date: 2026-08-11
from: triaged
to: triaged
reason: editorial_plain_language_wave133_yageo_margin_bridge_no_conclusion_change
evidence: editorial:plain_language_wave133_yageo_margin_bridge
-->
<!-- transition
date: 2026-08-11
from: triaged
to: triaged
reason: editorial_plain_language_wave148_yageo_beginner_opening_no_conclusion_change
evidence: editorial:plain_language_wave148_yageo_beginner_opening
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: profit_free_cash_flow_cash_stock_and_working_capital_ledgers_added_from_existing_deck_without_refreshing_thesis_clock
evidence: sources:S2,S3
-->
## 新手先讀：這篇在講什麼

### 名詞小字典

- **毛利率**：營收扣掉直接銷售成本後占營收的比例；改善可能來自價格、產品組合、成本或稼動率，不能只靠一個原因解釋。
- **產品組合**：不同產品或應用在營收中的占比；高毛利產品占比提高，可能推升整體毛利率。
- **季增／年增**：分別與上一季、去年同一季相比；兩種增幅的比較基準不同，不能混成同一個成長速度。
- **每股盈餘（EPS）**：公司稅後盈餘按流通股數換算到每一股的結果；它是整家公司數字，不會自動指出哪個產品帶來獲利。
- **稼動率**：實際使用產能占可用產能的程度；稼動率提高可能改善固定成本分攤，但本文資料尚未揭露這個數字。
- **鉭質電容**：使用鉭材料、常見於高可靠度或高階電子應用的電容；銷售成長不等於所有被動元件同步漲價。
- **MLCC（積層陶瓷電容）**：以多層陶瓷與金屬電極堆疊的小型電容。不同尺寸、容量、電壓與可靠度等級的供需可能分化，不能把單一高階料號的變化寫成全產品線同步漲價。
- **TWSE（臺灣證券交易所）**：上市公司申報與市場資料的官方入口。本文使用其個股報告交叉核對月營收；該摘要頁不等同完整季度財報與會計師附註。
- **核閱財務報告**：包含會計師核閱報告與附註的季度正式文件；法說簡報中的已檢閱摘要不等同完整季報。
- **自由現金流（FCF）**：公司在法說簡報使用的現金流指標；若未同時揭露公式，就要先稱為「公司簡報所列自由現金流」，不能自行假定一定等於營業現金流減資本支出。
- **現金存量**：資產負債表在某一天的現金及約當現金餘額；它是時點數，不等於一整季產生的自由現金流。
- **營運資金**：應收、存貨、應付與其他營運項目占用或提供的資金。本文用應收帳款加存貨減應付帳款做窄版代理值，不把它冒充完整會計定義。
- **強度代理比率**：把期末應收、存貨或應付除以同季營收或銷貨成本的診斷比率；它不是用平均餘額計算的正式 DSO、DIO 或 DPO。
- **EBITDA**：利息、所得稅、折舊與攤銷前盈餘；它是另一種獲利口徑，不等於營業現金流或自由現金流。
- **Python**：本文用來執行第一條確定性算術重算的程式語言；執行結果本身不是新的公司證據。
- **Decimal**：Python 的十進位精確運算型別；本文用它避免二進位浮點顯示誤差，再以另一種工具獨立核對。

### 三句話抓重點

- 國巨官方 Q2 簡報同時公布營收、毛利率、每股盈餘（EPS）、AI 終端占比與鉭質電容銷售變化。公司公布的營收，還能用 TWSE 的 4、5、6 月月營收重新加總核對。
- 公司表示，價格調整與 AI 產品組合改善，幫助毛利率上升；但投入成本上升與標準品需求增加，也抵銷了部分效果。
- 這些新資料足以啟動進一步查證，但還不能證明 MLCC 已全面漲價、交期拉長、產能滿載，或已有長約訂單。

### 為什麼重要

**先拆開看成長來源。** 營收和每股盈餘成長，不代表所有產品都同步變好。還要分清哪些改善
來自價格、哪些來自高毛利產品占比提高，以及哪些效果被成本或較弱的標準品需求抵銷。

**再看 AI 到底占多少。** 國巨這次公布 AI 終端占營收 16%，也說明價格調整與 AI 產品組合
如何影響毛利率。這讓「AI 需求強」可以拆成較具體的營收占比與獲利線索。

**最後確認文件能證明到哪裡。** 法說簡報已列公司定義自由現金流與資產負債表摘要，卻不是
完整季報。營業、投資、融資三張現金流與會計附註仍要等正式核閱財務報告，不能只靠摘要替
期末現金的大幅變動指定原因。

### 接下來怎麼追

- 取得完整 2026Q2 核閱財務報告，核對營業、投資、融資現金流、公司自由現金流公式、存貨、
  應收、借款與合併範圍變化。
- 追公司後續法說是否說明價格調整涵蓋的產品、交期、稼動率、通路庫存與客戶合約。
- 等正式筆記完成原始文件封存、逐頁核對與第二次獨立複核後，再判斷原本兩個可驗證假說是否需要改變。

### 想一想

- 毛利率上升時，如何分辨是售價、產品組合、成本下降還是稼動率改善？
- AI 終端占營收提高，是否足以證明每一類 MLCC 與電阻都同步受惠？
- 法說簡報已有財務摘要時，為什麼還要等完整核閱季報與附註？
- 淨利增加、自由現金流減少、期末現金大增，為什麼可以在同一季同時發生？

## 先把這一季的結果分成四組數字

**先看公司總額。** 國巨簡報列示 2026Q2 營收 444.56 億元；TWSE 個股報告的 4、5、6 月
營收加總為 444.56327 億元，兩者在四捨五入後一致。這一步只確認整季營收對得上。

**再看獲利結果。** 毛利率為 38.5%，季增 0.4 個百分點、年增 2.9 個百分點；簡報也列出
EPS。這些數字說明結果變好，但還沒有把售價、產品組合、成本與稼動率各自貢獻多少拆開。

**最後看產品與應用。** AI 終端占營收 16%，鉭質電容銷售季增 14.1%、年增 44%，MLCC 與
電阻的成長幅度高於整體。這些是不同範圍的數字，不能相加，也不能改寫成所有產品同步受惠。

| 本文四組數字 | 目前資料 | 先回答什麼 | 還不能回答什麼 |
|---|---|---|---|
| 公司營收 | Q2 444.56 億元；TWSE 月營收加總 444.56327 億元 | 整季營收是否能由第二條官方鏈對上 | 哪個產品、客戶或題材貢獻多少 |
| 整體毛利率 | 38.5%；季增 0.4 個百分點、年增 2.9 個百分點 | 公司整體銷售扣除直接成本後的結果是否改善 | 售價、組合、成本與稼動率各貢獻多少 |
| AI 終端占比 | 占營收 16% | 公司如何描述 AI 應用在整體營收中的位置 | 每一類 MLCC、電阻或電容的 AI 收入與毛利 |
| 產品銷售變化 | 鉭質電容季增 14.1%、年增 44%；MLCC 與電阻成長高於整體 | 哪些產品類別本季成長較快 | 全產品線漲價、滿載、長交期或長約訂單 |

四組數字的分母不同：營收與毛利率是公司總額，AI 是應用占比，鉭質電容、MLCC 與電阻是
產品類別。先把分母分開，才不會把同一季的多個好消息重複算成同一筆成長。

## 毛利率上升，要依序追四種可能原因

**售價與產品組合，目前有公司說法。** 公司表示價格調整與 AI 產品組合優化是毛利率改善因素；
這能確認管理層如何解釋本季結果，還不能量化兩者各自貢獻。

**成本不是本輪的正向證據。** 公司同時把投入成本上升與標準品需求增加列為抵銷因素，因此不能
把毛利率改善改寫成「成本已下降」，也不能只保留有利因素而忽略抵銷項目。

**稼動率仍是缺口。** 簡報沒有揭露產線使用程度、交期、訂單覆蓋或客戶合約；沒有這些資料，
就無法判斷固定成本分攤是否改善，也不能證明需求已進入滿載或長約階段。

| 四個拆解問題 | 本篇目前能說 | 還要補什麼 | 不應直接推成 |
|---|---|---|---|
| 售價有沒有提高？ | 公司把價格調整列為毛利改善因素 | 哪些產品、哪些客戶、調整幅度與生效時間 | 所有 MLCC 已全面漲價 |
| 高毛利產品占比有沒有提高？ | 公司把 AI 產品組合優化列為改善因素，AI 終端占營收 16% | 各產品與應用的收入、毛利率及前後期占比 | AI 占比提高就代表所有被動元件同步受惠 |
| 成本有沒有下降？ | 公司反而表示投入成本上升抵銷部分效益 | 原料、人工、折舊與併購後成本橋接 | 毛利率提高就是成本下降 |
| 產能有沒有用得更滿？ | 本輪沒有稼動率、交期或訂單覆蓋資料 | 產能、出貨、交期、庫存與客戶合約 | 已滿載、供不應求或已有長約 |

因此，目前最安全的說法是「價格調整與 AI 產品組合對毛利率有幫助，但成本與標準品需求抵銷
部分效益」；至於四個原因各占多少，仍要等公司提供可重建的毛利橋接。

## 淨利變好，現金不一定同速進來：三本帳與一張營運資金橋

國巨簡報第 8、11、13 頁把三種看似衝突的數字放在同一季：Q2 合併淨利為 94.55 億元，較
Q1 的 80.38 億元增加 17.6%；公司簡報所列自由現金流卻由 77.52 億元降至 57.83 億元，季減
25.4%；期末現金及約當現金則由 1,052.04 億元升至 2,000.78 億元，增加 948.74 億元 [S2]。
三者沒有誰一定是錯的：淨利是權責發生制的期間成果，自由現金流是另一個期間指標，期末現金
則是某一天的資產負債表存量。先分帳，才不會把「有獲利」、「有現金流」與「帳上現金很多」
寫成同一句話。

| 三本帳 | 2026Q1 | 2026Q2 | 機械變化 | 正確問題 | 不能直接回答 |
| --- | ---: | ---: | ---: | --- | --- |
| 合併淨利 | 80.38 億元 | 94.55 億元 | +17.6% | 當季收入扣除費用與稅後的會計成果 | 客戶何時付款、資本支出多少、現金由哪裡來 |
| 公司簡報所列自由現金流 | 77.52 億元 | 57.83 億元 | −25.4% | 公司簡報所用現金流指標本季有多少 | 在沒有公式時，不能自行指定為哪幾個現金流量表科目 |
| 期末現金及約當現金 | 1,052.04 億元 | 2,000.78 億元 | +948.74 億元／+90.2% | 季末這一天帳上有多少現金存量 | 本季營運賺進多少，或增加額一定來自營運 |

### 第一帳：淨利與自由現金流要同期間、同公式對讀

若只把簡報兩個相鄰季度放在一起，Q2 自由現金流除以合併淨利為
`5,783 ÷ 9,455 = 61.2%`，Q1 則為 `7,752 ÷ 8,038 = 96.4%`。這是研究中心為教學建立的
機械比率，不是國巨公布的 cash-conversion KPI，也不是營業現金流轉換率；簡報沒有給自由現金流
公式、營業現金流與資本支出橋接，因此不能由 61.2% 指定差額來自存貨、應收、設備、所得稅或
其他單一項目。

這組數字真正能做的，是提出一個查證問題：為什麼淨利季增 17.6% 時，公司定義自由現金流反而
季減 25.4%？答案必須回到完整現金流量表，把非現金損益、營運資金、稅息、資本支出、處分、
併購與其他投資逐項接回；沒有這張橋，就只能說兩支碼表方向不同，不能替差額編故事。

### 第二帳：期末現金大增，不等於營運現金同額流入

Q2 期末現金比 Q1 多 948.74 億元，遠高於同季簡報所列 57.83 億元自由現金流；兩個 headline
機械相減是 890.91 億元，但這個差額**不是**一條會計調節項。期末現金還會受到借款、發債、
償債、收購／處分、其他投資、匯率、受限現金分類與合併範圍影響，自由現金流定義也尚未揭露。
同頁摘要顯示，總資產季增 1,056.97 億元、總負債季增 960.59 億元、股東權益季增 96.39 億元；
依簡報顯示位數，負債與權益增加合計比資產增加多 0.01 億元，屬摘要四捨五入差，不應拿來製造
精確到百萬元的資金用途敘事 [S2]。

淨金融負債／過去 12 個月 EBITDA 同時由 32.8% 降至 22.4%，也提醒讀者：現金增加與負債變動
可能同時發生，不能只看現金餘額就判定「完全靠本業累積」，也不能只看總負債增加就判定
「財務彈性惡化」。還要取得現金、金融負債、非金融負債與 EBITDA 的完整分子及現金流方向。

### 第三帳：營運資金要同時看絕對額與相對強度

用簡報期末應收帳款、存貨與應付帳款建立窄版代理值：
`應收帳款 + 存貨 − 應付帳款`。Q1 為 `29,913 + 33,379 − 19,548 = 43,744` 百萬元，Q2 為
`33,619 + 35,597 − 20,942 = 48,274` 百萬元，絕對額增加 45.30 億元。若停在這裡，很容易寫成
「營運資金惡化」；但同期營收與銷貨成本也成長，代理值除以單季營收反而由 114.6% 降至
108.6%。這表示「占用金額增加」與「相對本季營收的強度下降」可以同時成立。

| 期末存量／單季流量代理 | 2026Q1 | 2026Q2 | 本輪能讀到的方向 | 仍不能升格成 |
| --- | ---: | ---: | --- | --- |
| 應收帳款／營收 | 78.4% | 75.6% | 應收增速低於單季營收增速 | 正式 DSO、收款改善原因或客戶付款品質 |
| 存貨／銷貨成本 | 139.9% | 130.2% | 期末存貨增加，但相對本季成本強度下降 | 正式 DIO、每個產品去庫存或不存在跌價風險 |
| 應付帳款／銷貨成本 | 82.0% | 76.6% | 應付提供的短期資金強度也下降 | 正式 DPO、供應商條件改善或惡化 |
| 應收＋存貨−應付／營收 | 114.6% | 108.6% | 窄版淨營運資金代理強度下降 | 完整營運資金、營業現金流或自由現金流原因 |

這四個比率都以期末存量除以單季流量，只是快速診斷，不是用期初期末平均餘額與日數計算的
正式周轉天數；外幣換算、合併範圍、收購價格分攤、其他應收／應付、預付款與合約負債也都未
納入。它們能阻止研究者只看存貨增加 6.6% 就下結論，卻不能代替完整附註與現金流量表。

### 多空小作文必須共用同一組現金裁決欄位

- **多方可以寫到哪裡**：Q2 營收、淨利與 EBITDA 成長，公司簡報所列自由現金流仍為正，
  淨金融負債／過去 12 個月 EBITDA 下降；三個期末營運資金強度代理中的應收、存貨與窄版
  淨營運資金均改善。若完整財報顯示營業現金穩健、自由現金流公式一致，後續季度又能重複，
  才能強化「成長有現金品質且槓桿可控」。
- **空方可以寫到哪裡**：淨利增加時自由現金流反向下降，教學比率由 96.4% 降至 61.2%；
  應付帳款／成本代理也下降，期末現金的大增尚無完整資金來源橋。若完整財報顯示營運資金持續
  吃現金、自由現金流依賴處分或公式調整，或後續季度轉負，才會強化「表面獲利沒有同步轉現」。
- **共同裁決資料**：完整 2026Q2 現金流量表與附註、公司自由現金流公式、營業現金流、現金
  CapEx、投資／併購與處分、借款／發債／償債、匯率與合併範圍、受限現金、應收帳齡、存貨
  品類與備抵、應付條件，以及至少下一季同口徑重算。沒有共同期間與公式，就不裁決多空。

本段是 `N=1` 家發行人、`N=2` 個相鄰季度的定向個案，不是被動元件公司、景氣循環或投資報酬
樣本，沒有 sampling SE／t。官方 PDF SHA-256 為
`4ace6c4735abd1edfe2b015062bf5b125f741217aac3e9142185f34cbddbcc2c`；已逐頁目視核對實際引用的
第 8、11、13 頁及相鄰頁。Python `Decimal` 與 `awk` 兩條獨立路徑均重算出淨利 +17.6%、自由
現金流 −25.4%、兩個教學比率 61.2%／96.4%、窄版營運資金 482.74／437.44 億元及 45.30 億元
增量。算術一致只能證明顯示值計算可重現，不消除自由現金流公式、四捨五入、合併範圍與附註
尚未取得的不確定性，因此不進跨公司 comparison ledger。

## 最後把公司總額、AI 題材與個股結論分開

**公司總額已經能對帳。** Q2 營收可由公司簡報與 TWSE 月營收交叉核對；這是本文最完整的
第二條官方驗證，但它只涵蓋營收，不會順帶驗證毛利率、EPS 或產品歸因。

**AI 題材仍停在公司層級。** 簡報提供 AI 終端占比與產品組合說法，卻沒有揭露單一產品、客戶、
認證、出貨量、價格與毛利分母，所以不能從 16% 直接算出某類元件的收入或獲利。

**個股結論還要等完整文件。** 完整核閱季報仍要核對現金流、存貨、應收、借款與併購後
資產負債；後續法說也要補價格範圍、交期、稼動率、通路庫存與客戶合約。

| 判讀層次 | 現在能說 | 尚未知道 | 下一份關鍵證據 |
|---|---|---|---|
| 公司總額 | Q2 營收 444.56 億元可由 TWSE 月營收重算 | 完整現金流、資產負債與附註是否支持表面改善 | 含會計師核閱報告與完整附註的 2026Q2 財務報告 |
| AI 與產品歸因 | 公司揭露 AI 終端占比、產品成長與價格／組合說法 | 哪個料號、客戶與產品線實際貢獻收入及毛利 | 可重建的產品、價格、產能與毛利橋接 |
| 個股判斷 | 新資料足以觸發正式筆記與既有假說複核 | 全面漲價、滿載、長交期、長約與可持續高毛利是否成立 | 正式筆記 evidence pack 與第二次獨立複核 |

這三層不能跳級：公司總額對得上，不等於 AI 題材已能精確歸因；題材占比提高，也不等於
訂單、毛利與投資結論已被證明。

## 為何值得進佇列

國巨在 7 月 29 日法說發布的官方簡報顯示，2026Q2 營收 444.56 億元，季增 16.5%、
年增 35.7%；毛利率 38.5%，季增 0.4 個百分點、年增 2.9 個百分點。公司並揭露 AI
終端占營收 16%，鉭質電容銷售額季增 14.1%、年增 44%，MLCC 與電阻的成長幅度高於
整體。這些資料直接命中 `2327:H1`、`2327:H2` 與既有多空小作文預先登錄的 Q2
毛利率、產品組合、AI 占比和價格效果驗證點，因此應列為 P1 更新，而非等到原訂
8 月 15 日或 8 月 31 日才處理。

## 來源與證據邊界

<!-- research_source
source_id: S1
role: company_release
publisher: YAGEO Group
title: YAGEO 2026Q2 Earnings Conference Resource Page
published_at: 2026-07-29
captured_at: 2026-07-30
accepted_at: 2026-07-30
status: active
url: https://yageogroup.com/SalesResources/ResourceLibrary/item/19061
locator: 2026Q2 法說事件頁與官方簡報下載入口
limitation: 事件頁只證實公司發布本次法說資料，不能單獨承擔財務數字或產品主張
-->

<!-- research_source
source_id: S2
role: company_release
publisher: YAGEO Group
title: YAGEO 2Q26 Earnings Conference Presentation Chinese
published_at: 2026-07-29
captured_at: 2026-07-30
accepted_at: 2026-07-30
status: active
url: https://www.yageogroup.com/content/Resource%20Library/Financial/YAGEO%202Q26_Earnings%20Conference%20Presentation_CH.pdf
locator: pp.4、6、11–14 的營運結果、產品組合與已檢閱摘要
limitation: 法說簡報不是含會計師核閱報告與完整附註的季度財務報告，也未揭露交期、稼動率、訂單覆蓋或客戶合約
-->

<!-- research_source
source_id: S3
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-07-30
accepted_at: 2026-07-30
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-07-30 以 2327 查詢季度財報與法說重大訊息的入口
limitation: 查詢入口會持續更新；入口本身不證明完整 Q2 財報已發布，也不能支持任何財務數字
-->

<!-- research_source
source_id: S4
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: TWSE 個股資訊－國巨股份有限公司（2327）
published_at:
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://www.twse.com.tw/pdf/ch/2327_ch.pdf
locator: 2026-08-09 產製版 p.4 的 2026/04、05、06 月營收與 p.5 的 2026-07-29 Q2 合併財務報告提報董事會公告列
limitation: 個股報告可獨立重算季度營收並確認公告存在，但不是含會計師核閱報告與完整附註的季度財報，也不交叉驗證毛利率、AI 組合、價格範圍、交期或稼動率
independence_group: twse-stock-profile
-->

- [國巨官方 2026Q2 法說頁](https://yageogroup.com/SalesResources/ResourceLibrary/item/19061)
- [國巨官方中文法說簡報](https://www.yageogroup.com/content/Resource%20Library/Financial/YAGEO%202Q26_Earnings%20Conference%20Presentation_CH.pdf)
- [TWSE 2327 個股資訊](https://www.twse.com.tw/pdf/ch/2327_ch.pdf)（2026-08-09 產製版）列示 4、5、6 月營收分別為 140.39098、150.58220、153.59009 億元；全數加總為 444.56327 億元，與公司簡報 444.56 億元的差異只來自億元顯示位數四捨五入。
- 簡報第 4 頁表示，毛利率改善主要受惠於價格調整與 AI 產品組合優化，但投入成本
  上升及標準品需求增加抵銷部分效益；這能更新獲利品質判讀，不能直接推成特定 MLCC
  料號已全面漲價。
- 簡報第 6 頁確認 AI 相關需求帶動多個產品類別，卻沒有揭露交期、稼動率、訂單覆蓋率、
  客戶合約或單一料號收入；因此尚不能把 `2327:H1` 的產業交期敘事升格為公司事實。
- 第 8 頁列公司定義自由現金流，第 11 至 13 頁標示為「國巨合併（已檢閱）」摘要；官方 PDF
  於 2026-08-14 下載後的 SHA-256 為 `4ace6c4735abd1edfe2b015062bf5b125f741217aac3e9142185f34cbddbcc2c`，
  已目視核對第 8、11、13 頁及相鄰頁。但 14 頁法說簡報仍不等同含會計師
  核閱報告及附註的完整 2026Q2 財務報告；正式筆記的 `latest_quarterly_report`
  仍須取得完整一手文件並走同一 evidence pack 的離線獨立重算。
- 現有正式筆記仍以 2024 年報與 2026Q1 為基準；這次重展開時須納入已發布的 2025
  年報，不能只在舊筆記補兩行 Q2 數字。

## Claim–evidence ledger

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: 國巨官方簡報列示 2026Q2 營收 444.56 億元、季增 16.5%、年增 35.7%，毛利率 38.5%，並列示 EPS、AI 終端占比與鉭質電容銷售變化
supporting_source_ids: S1,S2
contrary_source_ids:
as_of: 2026-07-30
basis: S1 提供官方文件入口，S2 的 Q2 營運與產品組合頁可直接定位上述數字
boundary: verified 表示公司簡報直接支持精確數字，不表示完整 Q2 財務報告已取得，也不證明後續季度會延續
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: 公司簡報表示毛利率改善主要受惠價格調整與 AI 產品組合優化，同時受到投入成本上升及標準品需求增加的部分抵銷
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-07-30
basis: S2 p.4 的管理層說明直接包含改善因素與抵銷因素
boundary: 這證實公司做出該歸因，不證明特定 MLCC 料號全面漲價，也未量化各因素的橋接貢獻
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: inference
status: active
claim: 這批 Q2 資料已足以提前觸發 2327 正式筆記與 H1／H2 複核，但尚不能直接完成正式簽核或假說終態轉移
supporting_source_ids: S1,S2
contrary_source_ids:
as_of: 2026-07-30
basis: 新數字直接命中預先登錄的毛利率、AI 占比與產品組合節點，但完整季度財報、現金流及部分商業化證據仍缺
boundary: 這是研究工作優先級與證據成熟度判斷，不是對股價、估值或未來獲利的結論
verification_needed: 完整 2026Q2 核閱財報、focused evidence pack 與獨立 reviewer 重算
resolution:
-->

<!-- research_claim
claim_id: C4
label: unverified
status: active
claim: 國巨已對所有 MLCC 全面漲價，且 AI 需求已轉成滿載、長交期、長期合約與可持續高毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-07-30
basis: S2 僅提供整體價格調整、產品組合與當季結果，沒有上述產品範圍及商業條件
boundary: 不得把此敘事寫成正式公司事實或用來裁決 H1／H2
verification_needed: 公司須揭露價格調整範圍、交期、稼動率、訂單覆蓋、客戶合約及後續毛利橋接
resolution:
-->

<!-- research_claim
claim_id: C5
label: verified
status: active
claim: TWSE 2026-08-09 個股報告列示國巨 2026 年 4、5、6 月營收合計 444.56327 億元，與公司 Q2 簡報的 444.56 億元在四捨五入後一致
supporting_source_ids: S2,S4
contrary_source_ids:
as_of: 2026-08-09
basis: S4 三個月的原始元數字相加為 44,456,327,000 元；換算億元後為 444.56327 億元，與 S2 顯示至小數點後兩位的 444.56 億元一致
boundary: 這只獨立交叉驗證合併營收；不代表 TWSE 個股報告已提供完整核閱附註，也不交叉驗證毛利率、EPS、AI 終端占比、價格、交期、稼動率或長約
verification_needed: 取得完整 2026Q2 核閱財務報告與附註，另以公司後續文件驗證產品與價格主張
resolution:
-->

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: 國巨官方簡報列示 Q2 合併淨利 94.55 億元、公司定義自由現金流 57.83 億元與期末現金 2,000.78 億元；相較 Q1，三者分別為增加 17.6%、減少 25.4%與增加 948.74 億元
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-07-29
basis: S2 pp.8、11、13 直接列示 Q1／Q2 自由現金流、損益與資產負債表摘要；2026-08-14 下載官方 PDF 後以引用頁及相鄰頁目視核對
boundary: verified 只代表公司簡報的三組顯示值與方向可定位；自由現金流公式、營業／投資／融資現金流及期末現金增加原因仍未由完整 Q2 財報驗證
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C7
label: inference
status: active
claim: 依簡報顯示值重算，公司定義自由現金流除以合併淨利的教學比率由 Q1 96.4%降至 Q2 61.2%，期末現金增加額與 Q2 自由現金流的機械差額為 890.91 億元
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-08-14
basis: Python Decimal 與 awk 兩條獨立路徑重算 7752／8038、5783／9455 及 200078−105204−5783，結果一致
boundary: 這是研究中心的確定性教學比率與機械差額，不是公司 KPI、GAAP 現金轉換率或會計調節；不得據此指定差額來源
verification_needed: 完整 Q2 現金流量表、自由現金流公式、投資／融資／匯率／合併範圍與受限現金附註
resolution:
-->

<!-- research_claim
claim_id: C8
label: inference
status: active
claim: 依期末應收加存貨減應付的窄版代理，營運資金由 Q1 437.44 億元增至 Q2 482.74 億元，但除以單季營收的代理強度由 114.6%降至 108.6%
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-08-14
basis: S2 pp.11、13 的營收、銷貨成本與期末應收／存貨／應付顯示值，經 Python Decimal 與 awk 兩條路徑重算
boundary: 期末存量除以單季流量不是正式 DSO／DIO／DPO，也未納入平均餘額、其他營運項目、外幣換算、合併範圍與收購價格分攤；只供同一發行人相鄰季度診斷
verification_needed: 完整季報的營運資金科目、帳齡／品類／備抵、現金流調節與合併範圍附註
resolution:
-->

<!-- research_claim
claim_id: C9
label: unverified
status: active
claim: 國巨 Q2 期末現金大增主要由本業自由現金流形成，且當季自由現金流下降只是短期時點差、後續會自動回升
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-14
basis: S2 的摘要同時出現自由現金流下降、現金與總負債大增，但沒有完整現金流與附註可指定來源或持續性
boundary: 不得把期末現金存量、正自由現金流與可持續現金轉換畫上等號，也不得在缺少後續同口徑資料時預測自動回升
verification_needed: 完整 2026Q2 現金流與附註、公司自由現金流公式，以及至少下一季同口徑的營業現金、CapEx、營運資金與融資變化
resolution:
-->

## 影響路由

<!-- impact
group_id: passive
stock_ids: 2327
direction: mixed
hypothesis_refs: 2327:H1,2327:H2
note_action: update_required
action_due: 2026-07-31
rationale: Q2 毛利率、AI 營收占比、MLCC 與特殊品成長及價格效果已直接命中既有 H1/H2 與多空小作文的預先登錄勝負手
evidence_boundary: 官方簡報支持 Q2 結果與管理層產品組合說法，但未提供交期、稼動率、訂單覆蓋率、客戶合約或特定 MLCC 全面漲價證據
-->

## 持續驗證帳本

<!-- monitoring_item
monitor_id: T1
status: retired
retired_at: 2026-08-09
retirement_reason: TWSE 個股報告已提供獨立季度營收對帳與 Q2 報告提報董事會公告，但完整核閱報告及附註仍待可下載版本，後續由 T3 接續
claim_ids: C1,C3
metric: 完整 Q2 核閱財報的現金流、存貨、應收、借款與併購後資產負債
source_ids: S1,S2
watch_source_ids: S3
frequency: event_driven
next_check: 2026-07-31
trigger: 公司或交易所發布含會計師核閱報告及完整附註的 2026Q2 財務報告
invalidation: 完整財報與法說摘要出現重大差異，或現金流與資產負債不支持表面獲利改善
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C2,C3,C4
metric: 價格調整產品範圍、AI 組合、交期、稼動率、通路庫存與毛利橋接
source_ids: S1,S2
watch_source_ids: S3
frequency: quarterly
next_check: 2026-08-15
trigger: 公司法說或正式文件提供可重建的產品、價格、產能與毛利資料
invalidation: 後續毛利回落、標準品需求抵銷擴大，或公司仍未證實全面漲價與長約主張
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C5
metric: 完整 Q2 核閱財報的現金流、存貨、應收、借款與併購後資產負債
source_ids: S2,S4
watch_source_ids: S3
frequency: event_driven
next_check: 2026-08-15
trigger: 公司或交易所提供可下載、含會計師核閱報告及完整附註的 2026Q2 財務報告
invalidation: 完整財報與已交叉驗證的季度營收出現重大差異，或現金流與資產負債不支持表面獲利改善
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C6,C7,C8,C9
metric: 2026Q2 營業／投資／融資現金流、公司自由現金流公式、現金與金融負債橋接、完整營運資金與後續季度現金轉換
source_ids: S2
watch_source_ids: S3
frequency: event_driven
next_check: 2026-08-15
trigger: 公司或交易所發布完整 2026Q2 核閱財報，或下一季文件提供同口徑自由現金流與資產負債橋接
invalidation: 完整文件顯示公司自由現金流公式、合併範圍或摘要科目不足以支持本文教學對讀，或後續現金流與暫時性回升敘事相反
-->

## 下一個可證明／否定的節點

- 取得完整 2026Q2 核閱財務報告，核對會計師核閱範圍、附註、現金流與併購後資產負債
  變化，並把公司自由現金流公式、期末現金、金融負債與營運資金接成可重算橋，再建立 focused
  evidence pack。
- 複核法說問答或公司後續正式說明，確認價格調整的產品範圍、交期、稼動率與通路庫存；
  若沒有一手揭露，保留為未驗證，不把簡報用語擴寫成 MLCC 全面漲價。
- 更新 2327 多空小作文的量化背景與 Q2 證據；正式筆記完成獨立 reviewer 簽核後，再決定
  `H1`、`H2` 的生命週期是否轉移。
