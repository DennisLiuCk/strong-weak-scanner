# AI 製程控制強度：HBM 與 2.5D／3D 把良率學習推向先進封裝

<!-- research_topic
topic_id: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-07-28
last_reviewed_at: 2026-08-02
review_due: 2026-08-13
source_type: mixed
publisher: KLA Corporation
publisher_domain: ir.kla.com
canonical_url: https://ir.kla.com/news-events/press-releases/detail/518/kla-corporation-reports-fiscal-2026-fourth-quarter-and-full
source_chain_id: kla-fy26q4-process-control-20260728
stock_ids:
group_ids: semiequip,material,pcb,packtest
trigger_type: industry_results_and_product_qualification
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C4
base_confidence: medium
confidence_basis: KLA、Applied Materials 與 Onto Innovation 三個獨立公司一手來源共同支持複雜度、檢測需求與客戶資格節點，但都是設備供應商資料；尚無客戶端或全產業資料證明 wallet share、台灣公司訂單或 KLA 成長的來源分解
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_source_process_control_scan
evidence: source_chain:kla-fy26q4-process-control-20260728
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_engineering_need_and_qualification_from_industry_wallet_share_and_taiwan_orders
evidence: sources:S1,S2,S3
-->
<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave3_no_conclusion_change
evidence: editorial:plain_language_wave3
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **製程控制**：在製造途中用量測、檢查與缺陷分析找出偏差，再把結果回饋到製程調整；它不同於封裝完成後才判定成品良否的成品最終測試（ATE final test）。
- **HBM**：把多層記憶體垂直堆疊的高頻寬記憶體；堆疊越複雜，晚發現缺陷的代價越高。
- **2.5D／3D 封裝**：把多顆晶片並排連接或上下堆疊；技術名稱不代表已通過客戶驗證。
- **量測／檢查**：前者確認尺寸與材料是否合規，後者尋找顆粒、刮傷或接合不良。
- **良率學習**：把缺陷資料回饋製程、找出報廢原因；不同於成品階段的最終測試。
- **設備預算占比（wallet share）**：客戶全部設備支出中，分給某類工具的比例；工程更重要不等於預算占比已上升。
- **財政年度第 4 季（FY26Q4）**：公司依自己的會計年度命名季度；它不一定等於曆年的第四季，跨公司閱讀時要先對齊期間。
- **電子束檢測（eBeam）**：用電子束觀察極細微結構與缺陷的量測方法；能看得更細不等於每一道製程都需要新增一台工具。
- **公開資訊觀測站（MOPS）**：台灣上市櫃公司的正式申報入口；要用它找具名產品、客戶階段與財務揭露，不能只靠海外設備商說法推導台灣公司受惠。

### 三句話抓重點

- 三家設備商的一手文件，分別說明需求方向、缺陷為何更昂貴，以及設備已走到客戶驗證的哪一步。
- 真正要查的是：每一代產品是否需要更多量測、檢查與良率回饋，而不只是設備名稱變多。
- 現有資料還不能證明全產業設備預算占比上升，也沒有台灣公司訂單，因此目前只建立族群觀察路徑。

### 為什麼重要

先進封裝把多顆昂貴晶片連在一起。若其中一顆在最後才被發現有缺陷，先前投入的晶片、封裝
材料與製程時間可能一起損失，因此越早找到問題越有價值。

但「更需要檢查」和「設備市場一定變大」仍是兩個問題。新工具或客戶驗證只說明工程需求與
採用節點；產業的獲利池是否擴大，還要看實際新增的步驟、工具數、採購金額與收入組成。

### 接下來怎麼追

- 追設備商是否揭露有期間與定義的訂單、收入、工具數或量產採用。
- 追公開資訊觀測站是否出現台灣公司的具名產品、客戶階段與財務貢獻。

### 想一想

- 若成長主要來自市占、漲價、產品組合或服務，主命題應如何縮小？
- 一套工具通過一名客戶認證，還缺哪些證據才能推論成產業錢包占比上升？

## 用一條回饋迴路理解製程控制

### 第一步：先看見偏差

量測回答尺寸、厚度或材料是否落在規格內；檢查則尋找顆粒、刮傷、翹曲與接合不良。兩者都
發生在產品完成之前，目的不是替成品打分數，而是及早知道哪一道製程開始偏離。

### 第二步：找出原因並調整製程

看到缺陷之後，工程師要把位置、形狀與發生條件連回設備參數、材料批次或製程步驟。若資料
只停在「發現一個壞點」，就還沒有形成良率學習；能找到根因並回頭調整，才是完整的回饋迴路。

### 第三步：再判斷商業價值落在哪裡

同一個工程問題可能由新增工具、既有設備升級、更聰明的抽樣，或設計規則改善來解決。因此
研究者要追的是每代新增多少步驟、哪些工具進入重複採購，以及收入來自工具數、價格、服務
還是市占變動。只有把這些來源拆開，才能判斷需求是否真的擴大。

對台灣族群也要走完同一條路：公司先具名產品，再說明客戶驗證或量產階段，最後才看得到
訂單、收入或毛利。海外設備商說「先進封裝更需要製程控制」，只能建立搜尋方向，不能替本地
公司完成後面三步。

## 主張與證據帳本

`證實` 只表示指定文件直接支持該句精確措辭；它不代表設備商的產業預測必然實現，
也不代表研究端已證明全產業支出、台灣公司訂單或獲利。

<!-- research_source
source_id: S1
role: company_release
source_kind: document
publisher: KLA Corporation
title: KLA Corporation Reports Fiscal 2026 Fourth Quarter and Full Year Results
published_at: 2026-07-28
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.kla.com/news-events/press-releases/detail/518/kla-corporation-reports-fiscal-2026-fourth-quarter-and-full
locator: FY26Q4（截至 2026-06-30）結果頁的 CEO 評論段，起句為 KLA remains uniquely positioned；另見 First Quarter Fiscal 2027 Guidance 與 Segment Information
limitation: 管理層把 memory complexity 與 advanced packaging 連到 process-control demand，但未分解產業錢包占比、單位工具量、客戶採購，也未區分成長來自市占、ASP、產品組合或服務
independence_group: kla
-->

<!-- research_source
source_id: S2
role: competitor_primary
source_kind: document
publisher: Applied Materials
title: Applied Materials Introduces New Systems to Accelerate DRAM and Advanced Packaging for AI Chips
published_at: 2026-06-25
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-new-systems-accelerate-dram-and/
locator: New eBeam Systems Bring Wafer-Fab Process Control to Advanced Packaging 小節；另見 HBM die warpage、VeritySEM 7AP 與 SEMVision G7AP 段落
limitation: 來源直接描述缺陷、量測與高量產使用情境，但仍是產品供應商公告，沒有全產業支出、第三方良率實績或台灣供應商訂單
independence_group: applied-materials
-->

<!-- research_source
source_id: S3
role: competitor_primary
source_kind: document
publisher: Onto Innovation
title: Onto Innovation Reports 2026 First Quarter Results
published_at: 2026-05-05
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Reports-2026-First-Quarter-Results/default.aspx
locator: First Quarter Business and Financial Highlights 的 Dragonfly G5 qualification bullet，以及 CEO 評論的 Dragonfly G5 inspection 與 Atlas G6 OCD adoption 段落
limitation: 只證實特定工具在一名 2.5D logic 客戶與一名 HBM 客戶的資格節點，以及公司對採用進度的描述；不提供訂單規模、產業滲透率或台灣映射
independence_group: onto-innovation
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: living_index
publisher: KLA Corporation
title: KLA Financial Results
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.kla.com/financial-information/financial-results
locator: 2026-08-02 觀察到 2026 → FY 2026 下列 Earnings Release、Letter to Shareholders、Earnings Slide Presentation 與 Earnings Infographic
limitation: 持續更新的索引只供重查新附件，不能替代特定季度文件，也不能單獨證明需求或財務貢獻
independence_group: kla
-->

<!-- research_source
source_id: S5
role: competitor_primary
source_kind: living_index
publisher: Applied Materials
title: Applied Materials News Releases
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.appliedmaterials.com/news-releases/
locator: 2026-08-02 觀察到 2026 年公告清單，包含 2026-06-25 DRAM and Advanced Packaging for AI Chips 公告
limitation: 持續更新的新聞索引只供未來重查；索引與產品標題本身不證明客戶採購、產業錢包占比或財務貢獻
independence_group: applied-materials
-->

<!-- research_source
source_id: S6
role: competitor_primary
source_kind: living_index
publisher: Onto Innovation
title: Onto Innovation News
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investors.ontoinnovation.com/news/default.aspx
locator: 2026-08-02 以 2026 年公司新聞與季度結果作為 Dragonfly、Atlas、HBM 與 advanced packaging 後續資格及量產更新入口
limitation: 動態索引不等於新的資格、訂單或收入證據；出現新公告時須另建 document source
independence_group: onto-innovation
-->

<!-- research_source
source_id: S7
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-02 建立 semiequip、material、pcb、packtest 族群重大訊息、法說與季度財報的後續查詢入口
limitation: 查詢入口會持續更新；入口本身不證明任何台灣公司取得 HBM／先進封裝量測檢查訂單或財務貢獻
independence_group: twse-mops
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: KLA 在 FY26Q4 發布中表示，leading-edge foundry／logic 設計增加、記憶體效能規格複雜化與先進封裝機會正在帶動更高的 process-control 需求
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-07-28
basis: S1 的 CEO 評論直接把上述三項技術向量與 process-control demand 連結
boundary: 這是 KLA 管理層對需求驅動的陳述，不證明全產業支出比例、KLA 成長來源分解、客戶投資報酬或台灣公司訂單
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: Applied Materials 表示，先進封裝已面臨過去只在晶圓廠出現的缺陷與量測問題，較小特徵與 HBM 堆疊的缺陷代價使製程控制成為關鍵，並稱其 SEMVision G7AP eBeam defect-analysis 系統已用於記憶體與邏輯廠商的高量產先進封裝
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-06-25
basis: S2 的 New eBeam Systems 小節直接描述 optical inspection 限制、HBM stack 報廢風險、CD metrology、defect review 與 high-volume production 使用狀態
boundary: 證實的是 Applied 的工程機制與自家產品部署陳述，不代表第三方驗證的全產業良率效果、市占或收入
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: Onto Innovation 在 2026Q1 結果中表示，Dragonfly G5 已在一名 leading 2.5D logic 客戶與一名 HBM 客戶完成資格認證，且 Atlas G6 用於下一代邏輯與記憶體元件的 OCD metrology
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-05-05
basis: S3 的 Business Highlights 與 CEO 評論直接列出客戶類型、qualification 與產品用途
boundary: 資格認證是採用節點，不等於量產採購規模、收入、產業滲透率或台灣公司參與
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: active
claim: 三個獨立設備供應商的一手文件共同支持一個縮窄後的研究判讀：HBM、2.5D 與 3D 整合提高幾何、材料、翹曲與缺陷代價，使量測、檢查及良率學習在工程上的重要性上升
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-07-28
basis: S1 提供 memory／advanced-packaging process-control 需求方向，S2 提供缺陷與量測機制及高量產使用敘述，S3 提供 2.5D logic 與 HBM 客戶資格節點
boundary: 交叉證據只支持需求機制與資格節點，不證明全產業 wallet share、工具數量、供應商排名、價格、毛利或台灣公司訂單
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: 全產業配置給 metrology、inspection 與 yield-learning 的設備 wallet share 已隨 HBM／先進封裝世代結構性上升
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有來源來自三家設備供應商，沒有共同口徑的客戶資本支出、工具數、製程步驟或全市場資料
boundary: 不以三家公司產品公告、資格節點或單一發行人營收成長替代全產業 wallet-share 證據
verification_needed: 需要客戶端資本支出與製程控制步驟、兩期以上同口徑工具需求，或可信產業資料交叉驗證支出比例與定義
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: 台灣 semiequip、material、pcb 或 packtest 族群中的特定公司已因這波製程控制需求取得新增訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: S1 至 S3 未點名 universe 內公司、產品、客戶或財務貢獻
boundary: 目前只建立族群搜尋路由，stock_ids 保持空白，不把同族群或相鄰製程自動改寫成受惠者
verification_needed: 台灣公司公告、財報或法說須明確連結量測／檢查產品、HBM／先進封裝客戶階段，以及可辨識的訂單或財務貢獻
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: unverified
status: active
claim: KLA 的 FY26Q4 成長主要反映全產業製程控制強度提高，而不是 KLA 自身市占、ASP、產品組合或服務收入變化
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: S1 提供管理層需求解釋與發行人分部揭露，但沒有可重建的 growth bridge 將上述驅動逐一分解
boundary: 不用 KLA 單一公司的結果反推全產業支出比例，也不把未分解成長當成台灣供應鏈需求
verification_needed: 需要 KLA 單位出貨、ASP、服務與產品組合分解，並以同期間客戶支出及獨立同業資料交叉核對
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 為何值得進佇列

KLA 提供需求方向，Applied Materials 說明缺陷機制，Onto Innovation 提供 2.5D logic 與
HBM 客戶資格節點。三條獨立消息鏈讓工程需求比單一廠商說法更可信。本題也不同於 ATE
tester TAM：它研究製程中的量測、缺陷定位與良率回饋。尚待證明的是這些需求有沒有變成
更多工具步驟與較高支出占比；未分解市占、ASP、產品組合與服務前，不能用 KLA 結果代表
全產業，更不能外推台灣公司受惠。

## 已驗證的證據階梯

| 層級 | 一手來源目前支持 | 仍不能外推 |
|---|---|---|
| 需求方向 | KLA 把 memory complexity、advanced packaging 連到 process control | 全產業 wallet share 或工具數 |
| 工程機制 | Applied 描述細小特徵、翹曲與高缺陷代價 | 第三方良率、總市場或排名 |
| 採用節點 | Onto 披露 2.5D logic 與 HBM 客戶資格認證 | 大量採購、收入或台灣參與 |

## 跨公司數字與可比性

本篇 `cross_company_numbers: false`：三家公司提供不同類型的證據，本文不比較營收、訂單、
工具數或市占。KLA 分部屬發行人自身定義，本文不列其數字，也不與同業排名。

## 來源與證據邊界

- [S1：KLA FY26Q4 結果](https://ir.kla.com/news-events/press-releases/detail/518/kla-corporation-reports-fiscal-2026-fourth-quarter-and-full)。
- [S2：Applied Materials DRAM／先進封裝與 eBeam 系統](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-new-systems-accelerate-dram-and/)。
- [S3：Onto Innovation 2026Q1 結果與 qualification](https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Reports-2026-First-Quarter-Results/default.aspx)。
- 後續入口：[KLA](https://ir.kla.com/financial-information/financial-results)、[Applied](https://ir.appliedmaterials.com/news-releases/)、[Onto](https://investors.ontoinnovation.com/news/default.aspx)、[MOPS](https://mops.twse.com.tw/mops/web/index)。

三家設備商彼此獨立但都有商業動機，不能替代客戶端或全產業資本支出證據。本輪也沒有
一致預期、估值、即時持倉或台灣公司客戶資料，因此不談市場是否反映或個股方向。

## 反方與替代路徑

- **供應商特有效果**：KLA 成長可能來自市占、ASP、產品組合或服務，而非類別支出增加。
- **資格不等於規模**：Onto 的 qualification 可能停在單一工具或客戶，未形成跨客戶量產。
- **替代解法**：設計規則、抽樣或既有光學工具升級，可能降低新增工具需求。
- **價值沒有外溢**：支出即使增加，也可能集中於海外平台；台灣族群不必然受惠。

## 台灣族群觀察邊界

<!-- impact
group_id: semiequip
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-14
rationale: 製程量測、缺陷檢查、分析與封裝設備最接近本題，但需逐家公司核對產品、客戶資格與收入
evidence_boundary: 三份海外設備商文件未點名 universe 公司；族群相近不等於本地工具取得訂單或能取代國際設備
-->

<!-- impact
group_id: material
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-14
rationale: 更細結構、翹曲與異質整合可能提高材料控制要求，後續需查材料規格與認證節點
evidence_boundary: 現有來源只描述設備與製程問題，沒有點名台灣材料、用量、價格或毛利
-->

<!-- impact
group_id: pcb
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-14
rationale: chiplet 與先進封裝涉及有機或其他封裝基板的缺陷管理，但須先確認本 universe PCB 公司實際產品層級
evidence_boundary: 來源不支持把一般 PCB 營收、載板題材或海外檢查工具需求直接改寫成台灣公司受惠
-->

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-14
rationale: OSAT 與先進封裝產線是製程控制使用端，需追資本支出、工具導入、良率與客戶量產階段
evidence_boundary: 使用端增加檢測不必然改善封測商收入或毛利，也不證明其採購台灣設備
-->

`stock_ids` 刻意留空；公司文件把具名產品、客戶階段與財務貢獻接起來前，四個族群都不是
受惠名單。

## 持續驗證清單

`review_due` 為 2026-08-13，等於所有 active monitoring item 中最早的 `next_check`。

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C4,C5
metric: HBM／advanced-packaging 每一產品世代或單位產能所需的製程控制步驟、工具內容與客戶支出占比
source_ids: S1,S2,S3
watch_source_ids: S4,S5,S6
frequency: quarterly
frequency_detail: KLA、Applied Materials 與 Onto Innovation 季報、法說及投資人材料
next_check: 2026-08-13
trigger: 至少兩條獨立來源或一份客戶端文件，以相同期間與清楚定義顯示每一產品世代或單位產能的製程控制步驟、工具量或支出占比增加
invalidation: 客戶端同口徑資料顯示連續兩個產品世代的製程控制步驟、工具量或單位產能支出持平／下降，或明確指出既有光學、抽樣或設計規則已吸收新增複雜度
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C5
metric: inspection／metrology 從資格認證到高量產的客戶廣度、缺陷攔截與良率學習結果
source_ids: S2,S3
watch_source_ids: S5,S6
frequency: event_driven
frequency_detail: 新產品 qualification、production adoption、客戶技術論文或量產公告出現時重查
next_check: 2026-08-31
trigger: 不同客戶或供應商揭露由 qualification 進入高量產，並提供缺陷攔截、良率改善、重複採購或部署範圍
invalidation: 客戶或供應商明確揭露 qualification 撤回、量產未採用，或既有光學／抽樣方案已足以處理新增複雜度；只有未見第二客戶時維持 C5 待驗證，不視為反證
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C6
metric: 台灣 semiequip／material／pcb／packtest 的具名產品、客戶資格、訂單與財務貢獻
source_ids: S1,S2,S3
watch_source_ids: S7
frequency: quarterly
frequency_detail: 公開資訊觀測站重大訊息、法說簡報與季度財報發布後逐公司核對
next_check: 2026-08-14
trigger: 公司一手文件首次把量測、檢查或良率學習產品連到 HBM／2.5D／3D 客戶階段，並提供可辨識訂單、收入或毛利資訊
invalidation: 公司明確否認相關產品／客戶曝險、退出該市場，或可定位的採購與供應商資料直接顯示相關資本支出由非 universe 公司取得；到期未見揭露只維持 C6 待驗證
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C7
metric: KLA FY26Q4 同期間成長中，單位出貨、ASP、市占、產品組合、服務與產業類別支出的可重建貢獻
source_ids: S1
watch_source_ids: S4
frequency: quarterly
frequency_detail: KLA 季報、法說、股東信與分部附註發布後重做 growth bridge
next_check: 2026-08-13
trigger: 公司或可定位的獨立資料分解至少 80% 的同期間成長，且顯示超過 50% 來自同口徑工具量或客戶類別支出增加
invalidation: 可重建分解顯示超過 50% 的同期間成長來自市占、ASP、產品組合或服務，而非同口徑工具量或客戶類別支出增加
-->

## 下一個可證明／否定的節點

- 設備商是否首次提供 advanced-packaging process control 的收入、訂單、工具量或部署口徑。
- KLA 能否分解單位出貨、ASP、產品組合、服務與市占；否則 C7 維持待驗證。
- Onto qualification 是否推進到重複採購或更廣泛高量產。
- 台灣公司若沒有產品、客戶階段與財務貢獻，C6 不升級，`stock_ids` 留空。

到期時若沒有被 active thesis claim 引用的新證據，只在 append-only scan log 記錄重查結果，
不更新 `last_reviewed_at`、不延後 `review_due`，也不提高 `base_confidence`。
