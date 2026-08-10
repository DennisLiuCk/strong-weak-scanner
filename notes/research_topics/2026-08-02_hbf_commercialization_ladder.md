# 新記憶體層不能只靠大容量：HBF 還要通過讀寫、耐久、系統整合與量產

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

<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave92_hbf_system_conditions_roles_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **新記憶體層**：在既有高速工作記憶體與長期儲存之間增加一個資料位置；只有容量還不夠，系統還要知道哪些資料適合放進去。
- **高頻寬快閃記憶體（HBF）**：嘗試把大量快閃記憶體平行化，再配上底部邏輯晶片，提高容量與讀取能力；目前仍在共同規則與樣品前階段。
- **高頻寬記憶體（HBM）**：把多層動態記憶體疊在一起並放在運算晶片附近；速度高，但容量、成本與封裝空間都有取捨。
- **快閃記憶體（NAND）**：固態硬碟常用、斷電後仍可保留資料的記憶體；密度高，但讀寫等待、更新與耐久特性不同於工作記憶體。
- **動態隨機存取記憶體（DRAM）**：需要持續供電、適合快速讀寫的工作記憶體；它與快閃記憶體的速度、成本與資料保留方式不同。
- **固態硬碟（SSD）**：以快閃記憶體保存大量資料的儲存裝置；容量大不代表能直接承擔工作記憶體的即時讀寫任務。
- **鍵值快取（KV cache）**：大型模型推論時保存先前上下文計算結果的資料；容量不足會增加搬移或重算，但實際讀寫模式仍依工作負載而異。
- **容量**：裝置能保存多少資料；容量變大不代表讀取、寫入、耐久、功耗與成本會同時達標。
- **頻寬**：一段時間內可搬移多少資料；總量高不代表每次取用的等待時間都短。
- **延遲**：從提出讀寫要求到取得結果所需的等待時間；平均值不能取代最慢情況與不同存取模式。
- **隨機讀取**：從分散位置取資料；它與連續搬移大區塊資料的難度不同，不能只用順序讀取數字代替。
- **順序讀取**：連續讀出相鄰資料；表現好不代表頻繁跳點、寫入或更新同樣適合。
- **寫入與更新**：新增資料或改寫既有內容；工作負載若頻繁更新，只有讀取速度不足以證明可用。
- **耐久**：記憶體可承受多少次寫入、溫度與使用時間；單次展示不能證明長期服務壽命。
- **功耗**：裝置運作所需電力；每次搬移資料的耗能與整體系統功率都會影響是否可部署。
- **熱管理**：把晶片與封裝產生的熱帶走；堆疊密度提高後，熱點可能限制速度、壽命與穩定度。
- **底部邏輯晶片（logic base die）**：位在記憶體堆疊底部、處理資料傳輸與控制功能的邏輯晶片；有此設計方向不等於產品已完成。
- **控制器**：安排資料讀寫、錯誤處理與裝置溝通的元件或邏輯；能控制一般固態硬碟不代表已支援 HBF。
- **堆疊**：把多層晶粒垂直整合，以增加容量或縮短連線；層數增加也會提高接合、測試與散熱難度。
- **記憶體分層**：依資料的速度、容量、持久性與成本需求，安排不同記憶體或儲存位置；不是越靠近運算晶片就一定越好。
- **軟體調度**：由系統軟體決定哪些資料何時搬移、放在哪一層；硬體存在不代表應用會自動使用。
- **標準化**：多方討論共同名稱、介面與測試規則；開始標準化不等於規格完成或產品互通。
- **工作組（workstream）**：由參與者共同推進特定議題的組織；工作組成立只證明有人開始協作。
- **公開規格（specification）**：可定位版本與內容的共同技術文件；新聞稿提到標準化不能替代正式規格。
- **介面**：裝置與系統交換資料、指令與狀態的規則；介面名稱存在不等於多家產品已互通。
- **合規計畫（compliance）**：用一致方法檢查產品是否符合規格；規劃測試不等於已有通過結果。
- **記憶體樣品（memory sample）**：可被量測的實體記憶體產品；公布目標日期不等於樣品已交付。
- **裝置樣品（device sample）**：把記憶體整合進可運作裝置或系統的樣品；單一展示板不等於客戶產品完成。
- **客戶資格認證（qualification）**：客戶依指定產品、工作負載與條件判定能否採用；開始測試不等於已通過。
- **製造良率**：投入製造後能成為合格產品的比例；少量成功樣品不能證明大量製造可穩定維持。
- **量產**：產品進入持續製造與交付；只有樣品、可量產聲明或設備就位仍不是實際量產。
- **重複訂單與收入**：客戶持續採購，且財務金額能對應同一產品與期間；公司總營收不能直接證明 HBF 貢獻。

### 三句話抓重點

- 新的記憶體層不能只提供更大容量；它還要在目標工作負載下證明讀取速度、寫入與更新、耐久、功耗和熱管理都能成立。
- 高頻寬快閃記憶體想用快閃記憶體搭配底部邏輯晶片，放在高速工作記憶體與長期儲存之間，但本輪公開資料仍只有共同標準化與未來樣品目標。
- 因此目前只能說兩家公司和開放運算計畫正討論共同規則；還不能說公開規格已完成、實體樣品已交付、裝置已整合、客戶已通過或產品已量產。

### 為什麼重要

人工智慧系統裡，有些資料正在被運算，有些要快速重複取用，有些則適合長期保存。新增一層記憶體
只有在容量、等待時間、讀寫模式、耐久、功耗與成本共同成立，而且系統軟體知道何時搬移資料時，
才可能真正分擔既有記憶體與儲存裝置的工作。

因此「工作組成立」、「公司畫出架構」與「樣品目標」只能證明研發方向正在推進，不能自動創造
可交付產品。把系統條件、角色交接與商用關卡分開，才能避免把新名詞直接寫成量產市場或台灣
供應商訂單。

### 接下來怎麼追

- 先找開放運算計畫公開的規格版本、介面與合規計畫，而不只看工作組名稱。
- 再找 2026 年下半年實體記憶體樣品的交付日、規格、測試條件與接收方。
- 2027 年初若出現裝置樣品，要確認它真的完成裝置整合、軟體調度與目標工作負載測試，而非單一展示板。
- 公司層級必須同時看到平台端具名、客戶資格認證、穩定製造、出貨、重複訂單與可辨識財務資料。

### 想一想

- 如果一種裝置容量很大、連續讀取很快，卻無法承受應用所需的頻繁寫入與更新，它應被當成新的工作記憶體層，還是特殊儲存裝置？
- 公司宣布加入工作組、公開規格完成、中立測試通過與多家產品互通，分別代表哪些不同證據？
- 即使裝置樣品能運作，還要看到哪些客戶與製造證據，才能稱為量產市場？

## 先判斷它能不能成為新的記憶體層

以下五項只是本文整理本輪公開資料的閱讀問題，不是完整產品規格，也不是對任何記憶體技術的
效能排名。只有把目標工作負載與共同測試條件說清楚，才能判斷新裝置究竟是工作記憶體、快取，
還是特殊儲存設備。

| 本文五項系統條件 | 讀者先問 | 沒通過會怎樣 | 主要接力角色 | 本輪可確認到哪裡 |
|---|---|---|---|---|
| 1. 容量與資料保留 | 能否保存目標資料量，斷電後是否要保留 | 容量不足會頻繁搬移；保留方式不符則放錯資料層 | 快閃記憶體、堆疊與控制器 | 公司把 HBF 定位為快閃記憶體方案；尚無實體產品規格 |
| 2. 讀取與等待時間 | 連續與分散讀取能否在工作負載要求內完成 | 總頻寬看似很高，單次取用仍可能等太久 | 底部邏輯晶片、控制器與介面 | 只有公司技術定位；沒有共同條件下可重現的第三方結果 |
| 3. 寫入、更新與耐久 | 能否承受應用需要的改寫頻率與服務壽命 | 只能大量讀取時，可能仍較像特殊儲存裝置 | 記憶體元件、控制器與韌體 | 現有來源未證明寫入、更新與耐久已達目標工作負載要求 |
| 4. 功耗、熱與封裝 | 堆疊與底部邏輯晶片能否在系統功率與溫度範圍內穩定運作 | 熱點、功耗或接合問題可能限制速度、壽命與良率 | 封裝、測試、供電與散熱角色 | 公開方向包含底部邏輯晶片；尚無實體樣品的熱與功耗結果 |
| 5. 系統整合與軟體調度 | 裝置、控制器與軟體是否知道哪些資料何時搬移 | 硬體即使可用，也可能沒有應用願意或能夠使用 | 裝置商、系統軟體、應用與客戶 | 2027 年初裝置樣品仍是公司目標；尚無具名系統運行結果 |

## 再把商用化拆成六關

後一關需要新的證據，不能因為公司合作、目標日期接近或產品名稱含有「高頻寬」，就把後面的
樣品、客戶結果與量產一起補滿。這是本文的閱讀順序，不是產業共同標準或公司快慢排名。

| 本文六關 | 這一關要證明 | 本輪已有證據 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 技術位置與工作負載說清楚 | 想處理哪類資料，為何不能由既有記憶體或儲存裝置完成 | SK hynix 描述快閃記憶體、底部邏輯晶片與鍵值快取位置 | 共同工作負載、延遲、寫入、耐久、熱與功耗結果 | 效能已勝過高頻寬記憶體，或所有推論工作負載都適用 |
| 2. 共同規則公開 | 多家產品要如何交換資料、測試與互通 | 兩家公司公告開放運算計畫工作組；官方索引列出 HBF | 公開規格、版本、介面與合規計畫 | 規格已完成、多家產品已互通或已有合規結果 |
| 3. 交出可測記憶體樣品 | 實體記憶體是否按規格做出並交給接收方測試 | Sandisk 以 2026 年下半年為首批樣品目標 | 實際交付日、規格、測試條件與接收方 | 樣品已交付、測試已通過或已有客戶訂單 |
| 4. 完成裝置整合 | 記憶體是否被放入具名裝置，並由軟體安排目標工作負載 | Sandisk 以 2027 年初為首批裝置樣品目標 | 具名裝置、軟體調度、工作負載與運行結果 | 裝置樣品已完成、可大規模部署或已被客戶採用 |
| 5. 通過客戶資格認證 | 客戶是否依指定產品與條件完成驗證 | 本輪沒有完成證據 | 客戶名稱、測試條件、通過結果與採購節點 | 開始測試就等於通過，或單一客戶可代表整個市場 |
| 6. 穩定量產與形成收入 | 能否維持良率、出貨與重複採購，並在財務上辨認同一產品 | 本輪沒有完成證據 | 穩定良率、量產出貨、重複訂單及可辨識收入 | 台灣供應商已受惠、已有毛利貢獻或整個族群同步成長 |

## 再把五組角色接力放回正確位置

HBF 若真的成為新記憶體層，不會只由一顆記憶體晶片完成。下表只說明各角色要交付什麼，以及
本輪證據停在哪裡；「形成搜尋路由」不等於已具名供應商、訂單或收入。

| 接力角色 | 要交付什麼 | 要和下一角色說清楚 | 本輪證據 | 不能外推 |
|---|---|---|---|---|
| 快閃記憶體與堆疊 | 提供容量、資料保留與可製造的記憶體結構 | 晶粒、堆疊、讀寫、耐久與測試規格 | 公開方向使用快閃記憶體；尚無最終晶粒、堆疊或樣品規格 | 一般固態硬碟用快閃記憶體可直接替代，或所有記憶體廠都能生產 HBF |
| 底部邏輯晶片與控制器 | 安排平行資料傳輸、命令與錯誤處理 | 介面、控制協定、製程、功耗與熱邊界 | SK hynix 公開底部邏輯晶片方向；沒有最終製程、供應商或實測 | 已完成設計、已選定晶圓代工或控制器供應商 |
| 封裝、測試與熱管理 | 把堆疊與邏輯晶片整合成可測、可散熱的產品 | 接合、互連、測試覆蓋、良率與散熱條件 | 只形成封裝與測試搜尋入口；沒有具名供應商或產品 | 服務高頻寬記憶體的公司必然取得 HBF 訂單 |
| 裝置、系統與軟體 | 把記憶體放進具名裝置，安排資料搬移與工作負載 | 裝置介面、驅動、軟體調度與端到端結果 | 裝置樣品仍是未來目標；沒有具名系統或軟體結果 | 單一展示板等於可部署產品，或應用會自動採用新硬體 |
| 客戶、製造與財務 | 完成資格認證、穩定製造、持續採購與財務揭露 | 通過條件、良率、出貨、重複訂單與同期間收入 | 本輪沒有客戶通過、量產、訂單或可辨識財務證據 | 工作組、樣品目標或公司總營收等於 HBF 商業化成功 |

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
