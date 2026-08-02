# HBF 已進入 OCP 標準化，但樣品、裝置整合與量產仍是三道不同門檻

<!-- research_topic
topic_id: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-02-25
last_reviewed_at: 2026-08-02
review_due: 2026-08-17
source_type: mixed
publisher: Sandisk and SK hynix
publisher_domain: sandisk.com
canonical_url: https://www.sandisk.com/company/newsroom/press-releases/2026/2026-02-25-sandisk-and-sk-hynix-begin-global-standardization-of-next-generation-memory-solution-high-bandwidth-flash-hbf
source_chain_id: hbf-standardization-sampling-20260802
stock_ids:
group_ids: memory,packtest
trigger_type: memory_standardization_and_sampling_ladder
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C4
base_confidence: medium
confidence_basis: Sandisk、SK hynix 與 OCP 一手資料可交叉確認標準化工作組、NAND／logic base die 架構與樣品目標；但實體樣品、介面規格、客戶資格、裝置整合、量產及財務貢獻尚未被證實
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_source_hbf_scan
evidence: source_chain:hbf-standardization-sampling-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_standardization_memory_sample_device_sample_qualification_and_production
evidence: sources:S1,S2,S3,S4
-->

<!-- research_source
source_id: S1
role: company_release
source_kind: document
publisher: Sandisk and SK hynix
title: Sandisk and SK hynix Begin Global Standardization of Next-Generation Memory Solution High Bandwidth Flash
published_at: 2026-02-25
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.sandisk.com/company/newsroom/press-releases/2026/2026-02-25-sandisk-and-sk-hynix-begin-global-standardization-of-next-generation-memory-solution-high-bandwidth-flash-hbf
locator: 標題下方 workstream 摘要與正文第 1 至 5 段；兩家公司將在 OCP 建立 HBF 專屬 workstream
limitation: 聯合公告證實合作與設計方向，不證明規格已完成、樣品已交付、客戶採用或量產
independence_group: sandisk-sk-hynix-joint
-->

<!-- research_source
source_id: S2
role: standard
source_kind: living_index
publisher: Open Compute Project
title: OCP Semi-Private Workstreams
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.opencompute.org/community/semi-private-workstreams
locator: 2026-08-02 的 Storage 分類列出 High Bandwidth Flash workstream
limitation: 動態工作組索引只能確認 OCP 目前列有 HBF；不提供公開規格內容、版本、合規結果或產品成熟度
independence_group: open-compute-project
-->

<!-- research_source
source_id: S3
role: competitor_primary
source_kind: document
publisher: SK hynix
title: SK hynix Presents Vision at TSMC Symposium 2026
published_at: 2026-04-23
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://news.skhynix.com/en/tsmc-technology-symposium-2026/
locator: The Way Forward in the AI Era 段落；HBF 註解將其定義為 NAND solution、KV cache 應用並使用 logic process base die
limitation: 技術願景與展示不等於最終產品規格、實測結果、客戶樣品、qualification 或出貨
independence_group: sk-hynix
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: document
publisher: Sandisk
title: Memory-Centric AI Sandisk High Bandwidth Flash Will Redefine AI Infrastructure
published_at: 2025-08-11
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.sandisk.com/company/newsroom/blogs/2025/memory-centric-ai
locator: NAND reimagined、Finding allies 與 Looking forward；目標於 2026 下半年交付首批 HBF memory samples、2027 年初送出首批 HBF inference device samples
limitation: 時程與效能敘述是公司目標及內部模擬；截至本輪不是已完成的樣品、獨立 benchmark、客戶資格或商業出貨
independence_group: sandisk
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: living_index
publisher: Sandisk
title: Sandisk Newsroom
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.sandisk.com/company/newsroom
locator: 2026-08-02 查得 Sandisk 新聞、部落格與 HBF 後續附件入口
limitation: 新聞索引只供未來重查；新標題不能替代文件內容、樣品交付或客戶證據
independence_group: sandisk
-->

<!-- research_source
source_id: S6
role: competitor_primary
source_kind: living_index
publisher: SK hynix
title: SK hynix Press Center
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://news.skhynix.com/press-center/press-release/
locator: 2026-08-02 查得 SK hynix HBF、AI NAND、樣品與量產更新入口
limitation: 動態新聞索引不能證明 HBF 有新規格、客戶樣品、量產或收入；須另登錄實際附件
independence_group: sk-hynix
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: Sandisk 與 SK hynix 於 2026-02-25 公告共同推進 HBF 標準化，並表示會在 Open Compute Project 建立專屬 workstream；OCP 的工作組索引截至 2026-08-02 也列有 High Bandwidth Flash
supporting_source_ids: S1,S2
contrary_source_ids:
as_of: 2026-08-02
basis: S1 的聯合公告直接說明合作與 OCP workstream，S2 由 OCP 自身索引交叉確認工作組存在
boundary: 工作組成立不等於規格 ratified、介面穩定、合規計畫完成或多廠產品已互通
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
claim: SK hynix 將 HBF 描述為面向 KV cache 等大量運算資料的下一代 NAND solution，並表示其像 HBM 一樣在 base die 使用 logic process 以提高資料傳輸能力
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-04-23
basis: S3 的 HBF 註解直接定義 NAND、KV cache 與 logic base die
boundary: 技術定位不證明所有推論工作負載都適用，也不證明延遲、寫入、耐久、熱與軟體調度已達客戶要求
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
claim: Sandisk 的公開目標是於 2026 年下半年交付首批 HBF memory samples，並預期首批整合 HBF 的 AI inference device samples 在 2027 年初出現
supporting_source_ids: S4
contrary_source_ids:
as_of: 2025-08-11
basis: S4 Looking forward 直接列出兩個目標時點
boundary: 這是前瞻目標，不是截至 2026-08-02 已交付樣品、已通過客戶測試或已量產
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
claim: HBF 目前最合理的成熟度定位，是一個已由單一公司概念前進到跨公司與 OCP 標準化、但仍位於實體 memory sample 之前的 NAND 型 AI 記憶體候選層；能否進入正式 AI memory hierarchy，要依序通過介面公開、樣品、裝置整合、客戶 qualification 與量產
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-08-02
basis: S1 與 S2 證實標準化工作組，S3 補上 NAND／base die／KV cache 的技術位置，S4 明示樣品仍是未來目標
boundary: 不把標準化、公司模擬或樣品目標改寫成產品效能勝過 HBM、客戶採用、市占、收入或台灣供應商訂單
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
claim: 截至 2026-08-02，HBF 最終公開介面規格已完成、首批 memory samples 已實際交付、整合裝置已送樣，或已有具名客戶完成 qualification
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有來源只有工作組、技術定位與未來時程，沒有規格版本、shipment 文件、客戶名稱、測試條件或 qualification 結果
boundary: 找不到完成證據不是反證；但在新文件出現前，圖譜成熟度不能越過 planned sample
verification_needed: OCP 公開規格或合規文件、Sandisk／SK hynix 樣品交付公告，以及客戶或裝置端可交叉核對的 qualification 結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: universe 內記憶體或封測公司已因 HBF 取得可辨識訂單、收入、毛利或資本支出貢獻
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: Sandisk、SK hynix 與 OCP 文件沒有具名台灣供應商，也沒有雙向核對的產品、客戶與財務資料
boundary: NAND、controller、bonding、TSV 或封測能力只形成搜尋路由，不構成公司受惠事實
verification_needed: HBF 平台端與台灣公司端同時揭露具名產品、qualification、出貨及可辨識財務貢獻
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C3,C4,C5
metric: HBF 規格版本、memory sample、device sample 與客戶 qualification
source_ids: S1,S2,S3,S4
watch_source_ids: S2,S5,S6
frequency: event_driven
frequency_detail: 週一三五自動研究循環檢查 OCP、Sandisk 與 SK hynix；出現規格、樣品或客戶文件即重審
next_check: 2026-08-17
trigger: OCP 發布可定位的 HBF 規格／合規資料，或 Sandisk、SK hynix、客戶公告實體樣品、測試條件與 qualification
invalidation: 2026 下半年沒有 sample evidence、工作組不再列示、時程延後，或實測顯示延遲、寫入、耐久與熱邊界無法支援目標工作負載
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C2,C5,C6
metric: HBF 在 AI memory hierarchy 的實際工作負載與台灣供應鏈財務足跡
source_ids: S2,S3,S4
watch_source_ids: S5,S6
frequency: quarterly
frequency_detail: 每季檢查 HBF inference device、軟體調度、量產與供應商法說；只有雙向證據才升級公司線
next_check: 2026-10-15
trigger: 具名裝置公布 HBF／HBM／DRAM 分層、工作負載與測試結果，且供應商揭露產品、出貨、收入或毛利
invalidation: HBF 長期只停留在模擬與標準化，或實際系統仍以 HBM、DRAM、CXL memory、SSD／context storage 完成需求
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **HBF（High Bandwidth Flash）**：把大量 NAND 平行化並配上邏輯 base die，試圖做出容量大、讀取頻寬高的記憶體；目前仍在標準化與樣品前階段。
- **HBM**：把多層 DRAM 疊在一起、放在加速器附近的高頻寬記憶體；速度高，但容量、成本與封裝空間都是系統設計限制。
- **NAND**：SSD 常用的非揮發記憶體，斷電後資料仍保留；密度高，但延遲、寫入與耐久特性和 DRAM 不同。
- **KV cache**：大型模型推論時保存先前上下文計算結果的資料；容量不足會增加搬移或重算，但它的讀寫模式不等於所有模型權重與訓練資料。
- **標準化／樣品／qualification**：先定共同介面，再交付可測的實體產品，最後由客戶驗證；三者不能互相代替。

### 三句話抓重點

- Sandisk 與 SK hynix 已把 HBF 放進 OCP 工作組，代表它不再只是單一公司的投影片概念。
- SK hynix 把 HBF 定位在 NAND、logic base die 與 KV cache，但 Sandisk 公開時程仍是 2026 下半年 memory sample、2027 年初 device sample 的目標。
- 因此目前最重要的不是先猜誰受惠，而是依序等規格、實體樣品、裝置整合、客戶 qualification 與量產；任何一步沒過都會改寫商業價值。

### 為什麼重要

AI 記憶體需求不只有「HBM 越多越好」。不同資料有不同的容量、延遲、持久性與讀寫需求；如果
HBF 能在 HBM 與 SSD／context storage 之間形成新層，價值可能重新分配到 NAND、logic base die、
堆疊、控制器與軟體調度。但工作組與架構圖不會自動創造產品，先把成熟度拆開才能避免把
「新名詞」直接當成下一個量產市場。

### 接下來怎麼追

- 先找 OCP 的公開 specification、版本號、介面與 compliance 計畫，而不只看工作組名稱。
- 再找 2026 下半年實體 memory sample 的交付日、容量／功耗／延遲／耐久測試條件與客戶回饋。
- 2027 年初若出現 device sample，要確認它真的把 HBF 放入可運行的記憶體分層，而非單一展示板。
- 公司層級必須同時看到平台端具名與供應商端產品、qualification、出貨及財務資料。

### 想一想

- 如果 HBF 只能處理大量順序讀取，卻無法承受目標 KV cache 的寫入、更新與耐久需求，它還會是新記憶體層，還是只是一種特殊儲存裝置？
- OCP 工作組能降低介面分裂，但沒有公開規格與多方實作時，兩家公司合作和真正可替換的生態系之間還缺什麼？
- HBF 若成功，是新增總需求，還是把原本落在 HBM、DRAM、CXL memory 或 SSD 的價值重新分配？

## 商用化階梯：目前只到標準化

| 階段 | 目前證據 | 尚缺的畢業條件 |
|---|---|---|
| 架構概念 | Sandisk 與 SK hynix 描述 NAND、logic base die 與 inference／KV cache 位置 | 可重現的第三方工作負載、延遲、耐久、熱與功耗結果 |
| 標準化 | 兩家公司公告 OCP workstream，OCP 索引列出 HBF | 公開 specification、版本、介面、測試與 compliance 計畫 |
| Memory sample | Sandisk 目標為 2026 下半年 | 實際交付、規格、測試條件與接收方 |
| Device sample | Sandisk 預期 2027 年初 | 具名裝置、軟體調度、工作負載與運行結果 |
| Qualification／量產 | 本輪沒有完成證據 | 客戶資格、穩定良率、量產出貨、重複訂單與財務認列 |

這張表的關鍵是「目標」仍留在 planned 欄。日後若樣品真的出現，只升級對應的一格；不能因為
一個 memory sample 就把 device、qualification、production 與 revenue 一起標成完成。

## 來源與證據邊界

- [Sandisk／SK hynix HBF 標準化公告](https://www.sandisk.com/company/newsroom/press-releases/2026/2026-02-25-sandisk-and-sk-hynix-begin-global-standardization-of-next-generation-memory-solution-high-bandwidth-flash-hbf)（合作與 OCP workstream）。
- [OCP Semi-Private Workstreams](https://www.opencompute.org/community/semi-private-workstreams)（HBF 工作組的獨立索引）。
- [SK hynix TSMC Symposium 2026](https://news.skhynix.com/en/tsmc-technology-symposium-2026/)（NAND、KV cache 與 logic base die 技術位置）。
- [Sandisk Memory-Centric AI](https://www.sandisk.com/company/newsroom/blogs/2025/memory-centric-ai)（樣品目標與公司模擬邊界）。

本篇不採用 Sandisk 的模擬結果來宣稱 HBF 與 HBM 效能相等，也不比較不同公司的頻寬、容量、
成本或良率。因為沒有共同測試條件與外部實體產品，這些數字不能用來做跨產品勝負或公司估值。

## 影響路由

<!-- impact
group_id: memory
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-17
rationale: HBF 若形成新層，會連到 NAND、controller、logic base die 與記憶體分層；但本輪沒有 universe 公司被平台端具名，也沒有產品與財務雙向核對
evidence_boundary: 記憶體或控制器能力不等於 HBF specification、sample、qualification、訂單或收入
-->

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-17
rationale: HBF 概念使用堆疊與 logic base die，形成 bonding、TSV、測試與熱管理搜尋入口；但目前仍只有外部架構與樣品目標
evidence_boundary: 具備先進封裝能力或服務 HBM 客戶，不等於取得 HBF 客戶 qualification、量產或財務貢獻
-->

## 下一個可證明／否定的節點

- OCP 公開 HBF specification、介面、版本與 compliance 路線，而不是只有 workstream 名稱。
- Sandisk 或 SK hynix 公告實際 memory sample，並提供可核對的規格、測試條件與接收方。
- 客戶或裝置端獨立確認 HBF device sample、工作負載、軟體調度與 qualification 結果。
- 若 2026 下半年沒有樣品證據、時程延後或工作組停滯，C4 的成熟度與信心必須下修。
- 台灣公司只有在平台端與公司端完成具名產品、資格、出貨與財務雙向核對後，才能從搜尋路由升級為公司曝險線。
