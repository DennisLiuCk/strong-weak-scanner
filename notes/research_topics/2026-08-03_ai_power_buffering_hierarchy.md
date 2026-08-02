# AI 機櫃功率緩衝不是一顆大電池：CBU、BBU、BESS 必須按時間尺度分開看

<!-- research_topic
topic_id: MI-2026-08-03-AI-POWER-BUFFERING-HIERARCHY
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-03
source_published_at: 2025-10-13
last_reviewed_at: 2026-08-03
review_due: 2026-09-01
source_type: mixed
publisher: NVIDIA
publisher_domain: developer.nvidia.com
canonical_url: https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/
source_chain_id: ai-power-buffering-primary-scan-20260803
stock_ids:
group_ids: passive,powersupply,power
trigger_type: architecture_standard_and_reference_design
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C4
base_confidence: medium
confidence_basis: NVIDIA 直接定義毫秒至秒與秒至分鐘兩層儲能，OCP Diablo 400 把機架 BBU 與電容儲能選項分列，TI 又公開 EDLC CBU reference design；三份一手來源足以建立功能與位置邊界，但都不是量產 BOM、客戶採購或台灣供應商財務證據
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-03
from: initial
to: inbox
reason: captured_multi_timescale_storage_and_rack_options
evidence: source_chain:ai-power-buffering-primary-scan-20260803
-->
<!-- transition
date: 2026-08-03
from: inbox
to: triaged
reason: separated_cbu_bbu_bess_by_timescale_location_and_function
evidence: sources:S1,S2,S3
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **CBU（Capacitor Bank Unit）**：以電容或超級電容靠近機架吸收很快的功率尖峰與低谷，重點是高功率、快速反應，不是長時間供電。
- **BBU（Battery Backup Unit）**：以電池在機架或直流匯流排側提供短時 ride-through，目的通常是跨過電源切換或受控停機，不等於設施級儲能。
- **BESS（Battery Energy Storage System）**：位於設施或公用電網介面側的較大型電池儲能，用來處理較慢、影響範圍更大的負載變化與發電機切換。
- **時間尺度**：事件從發生到需要被補償的快慢。元件若在錯誤的時間尺度工作，即使都能儲能，也不代表可互相替代。

### 三句話抓重點

- NVIDIA 把 AI 負載波動拆成毫秒至秒的機架附近電容／超級電容，以及秒至分鐘的設施級 BESS；兩者處理的頻率、位置與任務不同。
- OCP Diablo 400 又把 BBU 與 capacitor bank 分成兩個機架選項，TI 則公開以 EDLC 超級電容實作的 800V CBU reference design，證明「電容緩衝」已不是只有概念圖。
- 這些證據能建立 CBU／BBU／BESS 的架構地圖，不能直接推導國巨等被動元件公司、電源供應商或功率元件廠已進入量產 BOM、取得訂單或認列收入。

### 為什麼重要

「AI 用電暴增」經常被簡化成所有儲能與被動元件一起受惠，但同步運算帶來的是不同速度、
不同位置的功率問題。機架旁的 CBU、機架／匯流排側的 BBU、設施端的 BESS 在能量、
功率、反應速度、維修與安全條件上各自受限。若不先拆層，市場研究會把架構必要性誤寫成
任一零件供應商的確定需求，也會把短暫功率緩衝與長時間備援重複計算。

### 接下來怎麼追

- 追 OCP Open Rack／Diablo 的 CBU、BBU、busbar、保護與連接器規格是否形成正式版本及互通測試。
- 追 NVIDIA 或平台客戶是否公布同一量產機架的 CBU／BBU／BESS 位置、額定任務、qualification 與 field deployment。
- 追台灣被動元件、電源供應與功率元件公司是否以具名產品、客戶驗收、量產數量及可辨識財務貢獻完成雙向核對。

### 想一想

- 如果 CBU 能吸收毫秒級尖峰，但不能支撐數十秒停電，它能取代 BBU 嗎？
- 如果設施 BESS 能平滑分鐘級負載，配電與線路延遲是否允許它取代靠近機架的快速緩衝？
- 一家公司被列在 800V 生態系，和它的某顆電容、控制器或電源模組進入 production BOM，中間還缺哪些資格節點？

## 主張與證據帳本

本文的「證實」只表示官方文件支持精確的架構敘述；reference design、規格選項與生態系列名
都不自動證明量產採用。涉及台灣族群的 BOM、供應商份額、訂單及財務貢獻一律留在待驗證層。

<!-- research_source
source_id: S1
role: company_release
source_kind: document
publisher: NVIDIA
title: Building the 800 VDC Ecosystem for Efficient, Scalable AI Factories
published_at: 2025-10-13
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/
locator: Reducing the swings with multi-timescale energy storage 段落；短時儲能為 milliseconds to seconds 且靠近 compute racks，長時儲能為 seconds to minutes 且位於 utility interconnection
limitation: NVIDIA 描述目標架構與合作生態系，不提供同一量產機架的完整 BOM、元件數量、qualification、部署分母、供應商份額或財務貢獻
independence_group: nvidia
-->

<!-- research_source
source_id: S2
role: standard
source_kind: document
publisher: Open Compute Project
title: Diablo 400 Project Rack and Power Specification 0.7.0
published_at: 2026-03-01
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf
locator: 7.2.1 Battery Backup Unit Option 與 7.2.2 Capacitor Bank Option CBU；前者要求 45 至 90 秒 backup range，後者要求 rack 支援 application-specific capacitive bank energy storage
limitation: 0.7.0 是 OCP 專案規格版本，不是所有 NVIDIA／AI 機架的統一量產 BOM；CBU 容量與 power 仍由應用決定，也沒有台灣供應商名單、採購量或財務資料
independence_group: open-compute-project
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Texas Instruments
title: TI unveils complete 800 VDC power architecture for future generation AI data centers with NVIDIA
published_at: 2026-03-16
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html
locator: Complete power solution；TI 展示 800V capacitor bank units using EDLC super capacitor cells，並列出 hot-swap、800V 至 6V bus converter、末端 buck 與其他 power reference designs
limitation: 公司展示與 reference design 支持技術可行性，不等於指定 hyperscaler 已 qualification、量產部署、採用固定 BOM，亦不證明任何台灣公司供貨
independence_group: texas-instruments
-->

<!-- research_source
source_id: S4
role: standard
source_kind: living_index
publisher: Open Compute Project
title: Open Rack Specifications and Designs
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.opencompute.org/wiki/Open_Rack/SpecsAndDesigns
locator: 2026-08-03 的 Open Rack specifications and designs 索引；持續追蹤 rack power、busbar、BBU／CBU 與後續正式版本
limitation: 動態索引只提供文件入口，不能用索引本身證明某版內容、量產採用、供應商資格、訂單或收入；命中新文件後須另建 document source
independence_group: open-compute-project
-->

<!-- research_source
source_id: S5
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-03 起追蹤 passive、powersupply、power 族群公司的法說、季報與重大訊息
limitation: 索引頁本身不證明 CBU／BBU／BESS 產品、客戶、資格、訂單、收入或獲利；命中文件後須另建 document source 並核對口徑
independence_group: twse-mops
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: NVIDIA 把 AI power buffering 分為靠近 compute racks 的毫秒至秒高功率電容／超級電容，以及位於 utility interconnection 的秒至分鐘設施級 BESS
supporting_source_ids: S1
contrary_source_ids:
as_of: 2025-10-13
basis: S1 的 multi-timescale energy storage 段落直接列出兩層的時間範圍、儲能技術、位置與任務
boundary: 只證實 NVIDIA 公開架構；不代表每個 AI data center 都採相同配置、時間切點或供應商，也不證明量產部署
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
claim: OCP Diablo 400 0.7.0 把 BBU 與 capacitor bank CBU 分成兩個機架選項；BBU 要求支援 45 至 90 秒備援範圍，而 CBU 的 power 與 capacity 由應用決定
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-03-01
basis: S2 7.2.1 與 7.2.2 分別定義 BBU option 和 CBU option，並給出不同的任務邊界
boundary: 這是單一 OCP 專案規格，不是全產業共同 BOM；時間與容量不可外推至其他平台，也不形成供應商或財務排行
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
claim: TI 在 2026-03-16 公開的 NVIDIA 800V reference architecture 中展示以 EDLC super capacitor cells 實作的 800V CBU，並把它與 hot-swap、DC/DC bus conversion 及末端供電分列
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-03-16
basis: S3 Complete power solution 直接列出各 reference design 與 800V capacitor bank unit 的儲能技術
boundary: 展示與 reference design 只支持技術角色，不證明客戶 qualification、production BOM、部署量或台灣供應商參與
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
claim: AI 功率緩衝應按時間尺度、系統位置與失效任務拆成 CBU、BBU、BESS 三層；三者可協同但不可只因都能儲能就視為同一需求或互相替代，平台架構也不能直接換算成被動元件族群需求
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-08-03
basis: S1 提供短時與長時層級，S2 在 rack 層再分開 BBU 與 CBU，S3 證實 CBU 與電力轉換／保護是不同模組；三個獨立來源共同支持功能分層
boundary: 這是系統架構推論，不指定唯一時間切點、能量容量、拓撲、材料、供應商、採用率或財務受惠；不同平台可能合併或重分配功能
verification_needed: 需同一 production rack 與 facility 的完整 power architecture、qualification、operating data 和採購文件驗證實際分工
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: 台灣 passive、powersupply、power 族群已有公司以具名量產元件或模組進入 AI CBU／BBU／BESS BOM，並取得可辨識的訂單、收入與獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-03
basis: 現有來源只到 NVIDIA 架構、OCP 規格與 TI reference design；沒有客戶與台灣供應商雙向核對的 production BOM、數量、價格或財務分母
boundary: 不把 NVIDIA ecosystem 列名、規格上的元件必要性或外部 reference design 改寫成 universe 公司供貨事實
verification_needed: 需客戶 qualification 或採購文件，並與台灣公司法說、季報或重大訊息交叉核對具名產品、量產、收入及獲利
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 架構地圖：先問「哪一種波動」，再問「哪一顆元件」

| 層級 | 主要位置 | 要處理的事件 | 本輪一手證據 | 現在不能推論 |
|---|---|---|---|---|
| CBU | 靠近 rack／DC bus | 毫秒至秒的快速尖峰與低谷 | NVIDIA 的短時電容層、OCP CBU option、TI EDLC CBU | 固定電容量、電容材料、供應商、單機價值量、量產份額 |
| BBU | rack 或高壓直流匯流排 | 較長的 ride-through、切換或受控停機 | OCP Diablo 400 的獨立 BBU option | 所有平台都採同一秒數、化學體系、模組供應商或採購量 |
| BESS | facility／utility interconnection | 秒至分鐘的整體負載平滑與發電機切換 | NVIDIA 的 facility-level BESS 層 | 能取代 rack 緩衝、所有專案都採 800VDC、台灣族群收入 |

這張表不是產品排行榜。它的知識價值是把「容量」與「反應速度」分開：CBU 的核心可能是
短時間輸出很大功率，BESS 的核心可能是支撐更久的能量，BBU 則在機架可靠度與切換邏輯中
承擔另一個任務。只有在同一平台揭露 duty cycle、電壓、功率、能量、溫度、安全與壽命條件後，
才有資格把架構翻譯成元件規格與用量。

## 和既有 800V 研究的分工

既有 800VDC 功率半導體文章回答「SST、保護、IBC、末端轉換中 SiC／GaN／Si 各在哪裡」；
本文回答「負載波動由哪一層儲能在什麼時間尺度處理」。兩者在 800V bus 相交，但不能把
轉換級數與儲能元件數量相乘，也不能把 TI reference design 當成所有平台的 production BOM。

## 研究判定

- **可保留的結論**：CBU、BBU、BESS 是三個不同任務層；至少 NVIDIA、OCP 與 TI 的公開文件已能重建功能邊界。
- **可信度為中而不是高**：三份一手來源相互補強，但架構仍在演進，且缺同一量產場域的完整設計與運轉資料。
- **不得發布的結論**：被動元件用量倍增、指定台廠供貨、訂單／收入／毛利、受惠排名，以及市場是否已反映。
- **升格條件**：同一 production rack 公布 CBU／BBU qualification、field data 與 BOM，或買方和供應商雙向確認量產與財務分母。

## 來源

- [NVIDIA：800 VDC 與 multi-timescale energy storage](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/)
- [OCP：Diablo 400 Rack and Power Specification 0.7.0](https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf)
- [Texas Instruments：800 VDC architecture 與 EDLC CBU reference design](https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html)
- [OCP Open Rack 規格與設計索引](https://www.opencompute.org/wiki/Open_Rack/SpecsAndDesigns)
- [公開資訊觀測站](https://mops.twse.com.tw/mops/web/index)

## 族群影響

<!-- impact
group_id: passive
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: CBU 的電容／超級電容角色讓被動元件成為必要搜尋路由，但現有證據沒有台灣廠具名 BOM、材料規格、qualification 或財務分母
evidence_boundary: 只追元件規格與量產資格，不把架構必要性、NVIDIA ecosystem 或 TI reference design 當成族群訂單
-->

<!-- impact
group_id: powersupply
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: CBU、BBU、bus conversion、hot-swap 與控制需要系統整合，適合追蹤電源供應族群的具名模組與資格節點
evidence_boundary: 不把外部架構或合作列名改寫成台灣電源供應商已量產、取得訂單或認列收入
-->

<!-- impact
group_id: power
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: 高壓 bus、保護、雙向充放電與轉換使功率元件成為搜尋路由，但材料與 topology 仍未固定
evidence_boundary: 不由 reference design 推導 SiC／GaN／Si 固定份額，也不建立 universe 公司受惠排行
-->

## 監測器

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C4
metric: OCP／NVIDIA 新版 rack power 文件是否固定 CBU、BBU、BESS 的位置、任務、qualification 與互通邊界
source_ids: S1,S2,S3
watch_source_ids: S4
frequency: monthly
next_check: 2026-09-01
trigger: 新規格、reference design 或 production platform 公布可定位的 CBU／BBU／BESS 介面、測試與部署資料
invalidation: 新版平台把功能合併、移除，或 field data 顯示本文三層分法無法描述實際 power buffering
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C5
metric: 台灣三個相關族群是否出現可由客戶與公司雙向核對的具名產品、qualification、量產與財務分母
source_ids: S1,S2,S3
watch_source_ids: S5
frequency: quarterly
next_check: 2026-09-30
trigger: 公司法說／季報與客戶文件同時指向 CBU、BBU 或 BESS 的具名產品、量產出貨及可辨識財務貢獻
invalidation: 公司明確否認參與，或具名產品長期停在展示／樣品而未進 qualification 與量產
-->

## 什麼會推翻這篇

- Production architecture 顯示 CBU、BBU、BESS 的任務可由單一層在相同位置與可靠度條件下完全取代。
- OCP／NVIDIA 後續版本移除 capacitor bank，或實際運轉資料顯示靠近 rack 的短時儲能沒有穩定系統價值。
- 台灣公司證據若只重複「AI、800V、儲能」關鍵字，卻始終無具名產品、資格、部署與財務分母，族群路由應維持待驗證而非升格。
