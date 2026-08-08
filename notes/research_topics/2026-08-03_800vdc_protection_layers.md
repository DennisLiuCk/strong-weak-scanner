# 800VDC 保護不是一顆保險絲：人身、故障電流與 Hot-swap 必須分層

<!-- research_topic
topic_id: MI-2026-08-03-800VDC-PROTECTION-LAYERS
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-03
source_published_at: 2026-03-01
last_reviewed_at: 2026-08-03
review_due: 2026-09-01
source_type: mixed
publisher: Open Compute Project
publisher_domain: opencompute.org
canonical_url: https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf
source_chain_id: 800vdc-protection-primary-scan-20260803
stock_ids:
group_ids: power,powersupply,passive
trigger_type: safety_standard_and_reference_design
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C4
base_confidence: medium
confidence_basis: OCP Diablo 400 明列 accessibility／interlock、creepage／clearance、overcurrent、earthing、leakage 與 ground-fault requirements，TI 與 Infineon 兩條獨立供應商鏈再把 800V hot-swap／inrush 與轉換、儲能分開；足以建立保護責任層，但尚無共同 production topology、完整 fault matrix、台灣供應商 qualification 或財務證據
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-03
from: initial
to: inbox
reason: captured_safety_fault_and_hot_swap_protection_layers
evidence: source_chain:800vdc-protection-primary-scan-20260803
-->
<!-- transition
date: 2026-08-03
from: inbox
to: triaged
reason: separated_human_safety_fault_current_connection_and_energy_roles
evidence: sources:S1,S2,S3
-->

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:high_frequency_glossary
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **Interlock（安全連鎖）**：當人員要接近高壓帶電部位時，先強制斷電或阻止接近；它處理的是人身與維修安全，不是吸收功率尖峰。
- **Overcurrent／ground fault**：前者偵測或切斷超額電流，後者處理電流錯誤流向接地或機殼；兩者的偵測條件與故障路徑不同。
- **Hot-swap**：設備仍帶電時控制連接、預充與切離，避免插入大電容時的湧入電流或故障擴散；它不等於長時間備援電源。
- **SOA（Safe Operating Area）**：功率開關在電壓、電流與時間組合下可安全工作的範圍；預充軌跡若超出 SOA，開關可能在保護動作前受損。
- **Diablo 400**：OCP 的機架與電源規格專案，列出 400／800V 系統需求；它不是單一供應商的量產產品。
- **eFuse（電子保險絲）**：用功率開關、感測與控制快速限制或切斷異常電流；功能與一次性熔絲、hot-swap 或備援儲能不同。
- **CBU（Capacitor Bank Unit）**：靠近機架、以電容處理快速功率波動的儲能模組；它不負責取代故障隔離或人身安全保護。

### 三句話抓重點

- OCP Diablo 400 的 safety requirements 把 live-access interlock、creepage／clearance、overcurrent、protective earthing、leakage current 與 ground-fault detection 分別列出，顯示 800V rack 不是靠單一元件承擔全部風險。
- TI 把 800V hot-swap 定義為 input power protection 並與 DC/DC、末端轉換及 CBU 分列；Infineon 的 400／800V reference design 又把可程式化 inrush control、SiC JFET 與 12kW sampling board 具體化。
- 這些資料足以建立保護責任圖，不能直接證明台灣 power、powersupply 或 passive 公司已進入 production BOM、具有共同 telemetry schema、取得訂單或形成可辨識獲利。

### 為什麼重要

「800V 保護需求增加」若沒有故障模型，幾乎沒有公司研究價值。人員接近帶電部位、導體過流、
絕緣或接地故障、插拔時對大電容充電，以及停電時維持運作，是不同事件；它們可能分別由
機構／連鎖、被動斷路、感測與主動開關、hot-swap／eFuse、CBU／BBU 處理。把這些層混成
「保護元件」會重複計算 BOM，也會把 reference board 的技術能力誤寫成量產訂單。

### 接下來怎麼追

- 追 OCP／平台的 fault matrix 是否把每個 fault、偵測時間、斷電範圍、interlock、grounding 與 service procedure 對齊。
- 追 800V hot-swap／eFuse 從 reference design 推進到具名 platform qualification、production deployment、field fault log 與維修閉環。
- 追台灣相關族群是否由客戶與公司申報雙向確認具名 protection product、額定、測試、量產、收入及毛利。

### 想一想

- 保險絲能切斷大故障電流，是否也能安全控制設備插入時對 bulk capacitor 的預充軌跡？
- Hot-swap 能限制湧入電流，是否就能取代 interlock、protective earthing 或 ground-fault detection？
- 若 telemetry 只有控制器功能清單、沒有共同事件欄位與維修動作，它能否被當成獨立商業價值？

## 主張與證據帳本

本文把 requirement、公司 reference design 與 production evidence 分開。「證實」只到指定
文件明列的安全責任或產品階段；不把 sampling、展示或平台相容描述外推成量產採用與財務受惠。

<!-- research_source
source_id: S1
role: standard
source_kind: document
publisher: Open Compute Project
title: Diablo 400 Project Rack and Power Specification 0.7.0
published_at: 2026-03-01
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf
locator: PDF p.27（文件標示 Page 26），11.1 Safety Requirements；分列 accessibility／interlock、creepage and clearance、overcurrent protection、protective earthing and bonding、leakage current、ground fault detection 與 ESS safety
limitation: 這是 Diablo 400 0.7.0 的系統 requirement，不指定唯一 circuit topology、元件材料、反應時間、供應商、production BOM 或台灣公司財務曝險
independence_group: open-compute-project
-->

<!-- research_source
source_id: S2
role: company_release
source_kind: document
publisher: Texas Instruments
title: TI unveils complete 800 VDC power architecture for future generation AI data centers with NVIDIA
published_at: 2026-03-16
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html
locator: Complete power solution；800V hot-swap controller 明列為 800V rail 的 input power protection，並與 800V-to-6V、6V-to-<1V、PSU 與 CBU reference designs 分列
limitation: 這是 TI 公司發布與 GTC 展示，不是完整 safety standard、客戶 qualification、production fault data、固定 BOM 或台灣供應商證據
independence_group: texas-instruments
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Infineon Technologies
title: Infineon expands power path protection portfolio for 48 V and future AI data center architectures operating at 400 V and 800 V
published_at: 2025-10-09
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.infineon.com/technology-news/2025/INFPSS202510-002
locator: Hot-swap controller reference design for 400 V and 800 V 與 Availability；REF_XDP701_4800 使用 XDP controller 與 1200V CoolSiC JFET、依 SOA 控制 inrush、nominal TDP 12kW，當時狀態為 sampling
limitation: 供應商發布支持 reference design、規格與 sampling 階段，不證明任何客戶 qualification、量產部署、field reliability、供應份額或財務貢獻
independence_group: infineon
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
locator: 2026-08-03 的 Open Rack 規格索引；持續回查 Diablo／rack power safety、interconnect、management 與後續附件
limitation: 動態索引不能替代已發布規格或證明採用；命中新版本時須另建 document source 並比較 requirement 變化
independence_group: open-compute-project
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: living_index
publisher: Texas Instruments
title: TI Data Center Design Resources
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.ti.com/applications/data-center/overview.html
locator: 2026-08-03 的 data center resource index；回查 800V protection、hot-swap、isolation、sensing 與 reference design 文件
limitation: 公司資源索引只供未來重查；不能替代具日期文件，也不證明 production adoption、份額或財務貢獻
independence_group: texas-instruments
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: living_index
publisher: Infineon Technologies
title: Infineon Protection and Monitoring ICs
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.infineon.com/products/power/protection-and-monitoring-ics
locator: 2026-08-03 的 protection／monitoring portfolio 與 board index；回查 REF_XDP701_4800、eFuse、hot-swap、fault detection 與 telemetry
limitation: 動態產品頁會變動，只供重查入口；不能把功能清單當成共同平台規格、量產客戶或財務證據
independence_group: infineon
-->

<!-- research_source
source_id: S7
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-03 起追蹤 power、powersupply、passive 族群公司的法說、季報、重大訊息與產品資料
limitation: 索引頁本身不證明任何公司具有 800V protection BOM、qualification、訂單、收入或毛利；命中文件後須另建 document source
independence_group: twse-mops
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: OCP Diablo 400 0.7.0 的 safety requirements 分別要求帶電部位 accessibility／必要時 interlock 或斷電、creepage／clearance、output overcurrent protection、protective earthing／bonding、leakage-current limits 與 ground-fault detection
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-03-01
basis: S1 11.1 Safety Requirements 逐項列出上述責任與適用標準
boundary: 只證實 Diablo 400 的系統要求；不指定每項功能的唯一元件、拓撲、反應時間、供應商或量產實作
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
claim: TI 在 2026-03-16 的 800V architecture 中把 hot-swap controller 定義為 800V rail 的 input power protection，並與 DC/DC bus conversion、processor buck、PSU 與 CBU reference designs 分列
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-03-16
basis: S2 Complete power solution 直接列出 hot-swap 的 input-protection 任務與其他 conversion／storage designs
boundary: 只支持 TI reference architecture 的功能分工；不證明完整 safety coverage、客戶採用、production topology、部署量或台灣公司參與
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
claim: Infineon 在 2025-10-09 發布 400／800V REF_XDP701_4800 hot-swap reference design，揭露以 1200V CoolSiC JFET 與 XDP controller 依 SOA 控制 inrush、nominal TDP 12kW，且當時產品階段為 sampling
supporting_source_ids: S3
contrary_source_ids:
as_of: 2025-10-09
basis: S3 的 400 V and 800 V reference-design 段落與 Availability 可直接定位架構、額定與 sampling 階段
boundary: Reference design 與 sampling 只證明公司能力及產品階段，不等於 customer qualification、production deployment、field reliability、份額或收入
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
claim: 800VDC protection 應按人身／維修安全、絕緣與接地、故障電流、帶電連接／inrush 及 energy ride-through 分成不同責任層；interlock、earthing、overcurrent／ground-fault、hot-swap／eFuse 與 CBU／BBU 可以協同，但不能視為同一功能或互相替代
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-08-03
basis: S1 把 safety responsibilities 分列，S2 把 hot-swap 與 conversion／CBU 分開，S3 具體化 inrush／SOA 與 reference-design stage；三條獨立來源鏈共同支持責任分層
boundary: 這是研究端 fault-model 推論，不指定唯一 circuit、清除時間、材料、供應商、元件數、共同 telemetry schema、deployment 或財務受惠
verification_needed: 需 production platform 的完整 one-line diagram、fault matrix、timing、qualification、field log、service procedure 與 production BOM 驗證實際分工
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: 台灣 power、powersupply 或 passive 族群已有公司以具名元件或模組進入 800VDC protection production BOM，並取得可辨識 qualification、份額、訂單、收入與毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-03
basis: 現有一手來源只到 OCP requirement、TI reference architecture 與 Infineon sampling reference design；沒有 universe 公司與客戶雙向核對的 production BOM、測試、數量、價格及財務分母
boundary: 不把 protection requirement、外部 reference design、ecosystem 列名、產品關鍵字或同族群營收成長改寫成台灣公司供貨事實
verification_needed: 客戶 qualification／採購或 production BOM，並與台灣公司法說、季報或重大訊息交叉核對具名產品、額定、測試、量產、收入及毛利
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## Fault map：先問誰或什麼要被保護

| 責任層 | 主要事件 | 本輪證據 | 不能被它取代 |
|---|---|---|---|
| Accessibility／interlock | 人員接近帶電高壓部位或維修開蓋 | OCP 要求帶電 PS2 以上部位不可接近，必要時先 interlock／斷電 | overcurrent、ground-fault、inrush control、ride-through |
| Creepage／clearance、earthing、leakage | 絕緣距離、機殼／保護地故障路徑與漏電 | OCP 分列 spacing、bonding、leakage limits | hot-swap 或單一主動開關 |
| Overcurrent／ground-fault | 導體過流、短路或電流錯誤流向地／機殼 | OCP 要求 output overcurrent 與 ground-fault detection | 人員 interlock、controlled pre-charge、backup energy |
| Hot-swap／inrush | 帶電插拔、bulk capacitance 預充、快速隔離 power path | TI 定義 input protection；Infineon reference design 依 SOA 控制 inrush | creepage、earthing、完整 fault coverage 或長時備援 |
| CBU／BBU ride-through | 快速功率波動、停電跨越或受控停機 | TI 把 CBU 與 hot-swap 分列；既有 OCP power-buffering 研究另有時間尺度 | fault isolation、interlock 與接地保護 |

這張表把「誰被保護、哪一種故障、要多快動作」放在元件名稱之前。同一個 controller 或
module 可能整合多項功能，但整合不代表責任消失；反過來，一項 requirement 也可能由多顆
元件與機構共同完成。因此，元件價值量必須由 production topology 與 qualification 重建，
不能把 requirement 數量直接當成 BOM 顆數。

## Telemetry 為什麼先併入保護層

Infineon 的 48V eFuse 發布已列出 voltage、current、energy、power、faults 與 anomalies 等
real-time telemetry；800V 產品頁也把 monitoring 列為功能方向。然而本輪沒有找到跨平台共同
event schema、timestamp、fault action、retention、site log 與維修決策契約。因此 telemetry
目前只作 protection monitor 的一部分，不另建「AI 電源監控」商業題材；待 OCP／買方把
欄位與 action contract 固定後再評估是否獨立升格。

## 分析師如何使用這張圖

1. **先建立 fault matrix**：列出 fault、偵測器、清除裝置、反應時間、隔離範圍與 fail-safe 狀態。
2. **分清 requirement 與產品階段**：OCP requirement、reference design、sampling、qualification、production deployment 不能混成一級。
3. **再做 BOM 與公司映射**：只有同一 platform 的 topology、part number、客戶驗證與供應商申報對齊後，才談份額與財務。
4. **把 telemetry 綁到動作**：只有量測值、事件欄位與隔離／維修決策形成閉環，才有獨立知識價值。

## 研究判定

- **可保留的結論**：800V protection 至少包含人身／維修、絕緣接地、故障電流與 hot-swap／inrush 等不同責任；三條一手來源鏈能重建基本 fault map。
- **可信度為中而不是高**：OCP 是 requirement，TI／Infineon 是供應商架構與 sampling reference design；仍缺共同 production fault matrix 與 field data。
- **不得發布的結論**：保護元件顆數倍增、指定 SiC／Si／被動元件或台廠勝出、共同 telemetry 商業價值、訂單／收入／毛利及市場是否已反映。
- **升格條件**：具名 production platform 公布完整 protection topology、qualification、fault log、service action 與 BOM，並由台灣公司申報交叉確認財務分母。

## 來源

- [OCP：Diablo 400 Rack and Power Specification 0.7.0](https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf)
- [Texas Instruments：800V hot-swap input protection reference architecture](https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html)
- [Infineon：400／800V power-path protection 與 REF_XDP701_4800](https://www.infineon.com/technology-news/2025/INFPSS202510-002)
- [OCP Open Rack 規格索引](https://www.opencompute.org/wiki/Open_Rack/SpecsAndDesigns)
- [TI Data Center Design Resources](https://www.ti.com/applications/data-center/overview.html)
- [Infineon Protection and Monitoring ICs](https://www.infineon.com/products/power/protection-and-monitoring-ics)
- [公開資訊觀測站](https://mops.twse.com.tw/mops/web/index)

## 族群影響

<!-- impact
group_id: power
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: 主動隔離、hot-swap／eFuse、感測與驅動使 power 族群成為必要搜尋路由，但材料、topology 與供應份額仍未固定
evidence_boundary: 不由外部 reference design 推導 SiC／GaN／Si 份額，也不建立 universe 公司訂單、財務或受惠排行
-->

<!-- impact
group_id: powersupply
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: 電源模組與 rack／tray 整合者需把 interlock、fault clearing、hot-swap、CBU／BBU 與 service procedure 組成可驗證系統
evidence_boundary: 系統責任只形成搜尋路由，不證明台灣電源公司採用特定 topology、已 qualification、量產或形成可辨識獲利
-->

<!-- impact
group_id: passive
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: pre-charge bulk capacitance、overcurrent／temperature protection 與濾波讓 passive 族群具相鄰查核價值，但現有 requirement 沒有具名台灣元件
evidence_boundary: 不把保護層數量直接換成電容、熱敏或保險元件顆數，也不推導供應商、ASP、份額或收入
-->

## 監測器

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C4
metric: OCP／平台與供應商是否把 protection requirements 推進到共同 fault matrix、timing、qualification 與 production topology
source_ids: S1,S2,S3
watch_source_ids: S4,S5,S6
frequency: monthly
next_check: 2026-09-01
trigger: 新規格或 production 文件同時公布 fault、偵測、反應時間、清除裝置、隔離範圍、service action 與具名實作
invalidation: 新平台顯示本文責任分層不適用，或 field data／規格修訂實質否定 hot-swap、ground-fault、interlock 等邊界
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C5
metric: 台灣三個相關族群是否出現客戶與公司雙向核對的 protection product、qualification、production BOM 與財務分母
source_ids: S1,S2,S3
watch_source_ids: S7
frequency: quarterly
next_check: 2026-09-30
trigger: 公司申報與客戶文件同時指向具名產品、額定、fault test、qualification、量產出貨、收入及毛利
invalidation: 公司明確否認參與，或產品長期停在 reference design／sampling 而沒有 qualification 與 production evidence
-->

## 什麼會推翻這篇

- Production architecture 證明單一裝置在相同安全完整性與維修條件下可完整取代 interlock、earthing、overcurrent／ground-fault、hot-swap 與 ride-through 各層責任。
- OCP 或平台後續 requirement 移除本文關鍵責任，或 field evidence 顯示分層會造成錯誤的故障判讀。
- 若台灣公司只有「800V、保護、SiC、電源」字樣而始終沒有具名產品、資格、production 與財務分母，族群 route 應維持待驗證而非升格。
