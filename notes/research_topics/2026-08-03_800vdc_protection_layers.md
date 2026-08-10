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

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave5_power_system_learning_no_conclusion_change
evidence: editorial:plain_language_wave5
-->

<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave81_protection_roles_no_conclusion_change
evidence: editorial:plain_language_wave81_protection_roles
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **Interlock（安全連鎖）**：當人員要接近高壓帶電部位時，先強制斷電或阻止接近；它處理的是人身與維修安全，不是吸收功率尖峰。
- **Overcurrent／ground fault**：前者偵測或切斷超額電流，後者處理電流錯誤流向接地或機殼；兩者的偵測條件與故障路徑不同。
- **Hot-swap**：設備仍帶電時控制連接、預充與切離，避免插入大電容時的湧入電流或故障擴散；它不等於長時間備援電源。
- **DC（Direct Current，直流電）**：電流主要往固定方向流動。800VDC 代表約 800 伏的直流供電架構。
- **BBU（電池備援單元）**：斷電或電源切換時短暫供電，它處理的是維持運作，不是取代故障隔離與人身安全保護。
- **SiC（碳化矽）**：可處理較高電壓與功率的半導體材料；參考設計使用 SiC，不等於所有量產系統都會採用。
- **JFET（接面場效電晶體）**：一種電子開關。本文引用的 SiC JFET 用於控制高壓接入時的電流，不代表已完成客戶量產驗收。
- **SOA（Safe Operating Area）**：功率開關在電壓、電流與時間組合下可安全工作的範圍；預充軌跡若超出 SOA，開關可能在保護動作前受損。
- **Diablo 400**：OCP 的機架與電源規格專案，列出 400／800V 系統需求；它不是單一供應商的量產產品。
- **eFuse（電子保險絲）**：用功率開關、感測與控制快速限制或切斷異常電流；功能與一次性熔絲、hot-swap 或備援儲能不同。
- **CBU（Capacitor Bank Unit）**：靠近機架、以電容處理快速功率波動的儲能模組；它不負責取代故障隔離或人身安全保護。
- **絕緣距離（creepage／clearance）**：帶電零件之間沿表面與穿過空氣必須保留的安全距離，用來降低電弧、漏電或擊穿風險。
- **保護接地與漏電（protective earthing／leakage current）**：前者替異常電流提供安全流向，後者檢查不該流出的電流；兩者都不是只靠切斷大電流就能處理。
- **湧入電流／預充（inrush／pre-charge）**：設備剛接上電源時，大電容會瞬間吸收很大的電流；預充會先限制這股電流，再讓設備正式接通。
- **參考設計（reference design）**：供應商公開的可行電路與元件組合，用來示範一種做法；不等於客戶已採用或量產。
- **樣品板（sampling board）**：供測試與評估的早期電路板；可運作不等於已通過客戶驗證或進入量產。
- **量產材料清單（production BOM）**：量產產品實際採用的零件與材料清單；比規格、展示板或規劃更接近真實採購。
- **客戶資格驗證（qualification）**：客戶依自己的安全、可靠度與系統條件測試產品是否可用；通過後仍不等於已大量出貨。
- **監測資料（telemetry）**：設備持續回報的電壓、電流、溫度、故障與狀態資料；只有數值而沒有後續動作，還不能形成完整的保護流程。
- **故障與處置對照表（fault matrix）**：把每種故障、偵測方式、處置裝置、反應時間與隔離範圍對在一起的表格。

### 三句話抓重點

- OCP Diablo 400 規格把人員接近高壓、絕緣與接地、過大電流及漏電等風險分開規定，表示 800V 機櫃不能只靠一種保護方式。
- TI 與 Infineon 的公開設計顯示，帶電插入設備時還要先限制湧入電流，再安全接通或隔離；這和長時間備援、接地或人員防護是不同責任。
- 目前證據只足以畫出誰負責什麼，尚不能證明台灣功率元件、電源供應或被動元件公司已進入量產材料清單、取得訂單或形成可辨識獲利。

### 為什麼重要

**先問要保護的是誰、遇到什麼事。** 人員接近帶電部位、導體過流、絕緣或接地故障、設備帶電
插入時替大電容充電，以及停電時維持運作，是五種不同事件。

**再把每個事件交給不同保護責任。** 安全連鎖先保護人員，斷路與主動開關處理異常電流，
不停機更換與電子保險絲控制接通，電容與電池備援則維持短暫供電；它們可以合作，但不能互相取代。

**最後才談公司與元件價值。** 把所有責任混成「保護元件」，會重複計算量產材料清單，也會把
供應商參考設計的技術能力誤寫成客戶量產訂單。

### 接下來怎麼追

- 追 OCP 或平台規格是否把每種故障、偵測時間、斷電範圍、安全連鎖、接地與維修程序對齊。
- 追 800V 不停機更換與電子保險絲，是否從參考設計推進到具名平台的客戶資格驗證、實際量產、現場故障紀錄與維修閉環。
- 追台灣相關公司是否由客戶文件與公司申報雙向確認具名保護產品、額定規格、測試、量產、收入及毛利。

### 想一想

- 保險絲可以切斷過大的故障電流，但設備帶電插入時，大電容也會瞬間吸收電流；為什麼還要先限流再接通？
- 不停機更換功能能限制湧入電流，是否就能取代安全連鎖、保護接地或接地故障偵測？
- 如果監測資料只有數值與故障清單，沒有規定發生事件後要隔離哪裡、怎麼維修，能否成為獨立產品價值？

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

## 先分清楚：保護誰、發生什麼事、誰來處理

| 保護責任 | 主要事件 | 目前證據說了什麼 | 仍需要其他保護處理 |
|---|---|---|---|
| 人員與維修安全（安全連鎖） | 人員接近帶電高壓部位或維修開蓋 | OCP 要求高風險帶電部位不可直接接近，必要時先由安全連鎖斷電 | 過大電流、接地故障、插入限流與停電備援仍須分開處理 |
| 絕緣、接地與漏電 | 帶電零件距離不足、電流流向機殼或保護地，以及不正常漏電 | OCP 分別規定絕緣距離、接地連接與漏電上限 | 不停機更換功能或單一主動開關不能取代這些責任 |
| 過大電流／接地故障 | 導體過流、短路，或電流錯誤流向地面與機殼 | OCP 要求輸出過流保護與接地故障偵測 | 人員安全連鎖、預先限流與備援儲能仍須另外處理 |
| 帶電插拔／湧入電流 | 設備帶電插入時替大電容預充，並在異常時快速隔離電力路徑 | TI 把它列為輸入電力保護；Infineon 參考設計依開關的安全工作範圍控制湧入電流 | 絕緣、接地、完整故障處理或長時間備援不能被它取代 |
| 電容／電池備援 | 快速功率波動、短暫停電或受控停機 | TI 把電容備援與帶電插拔保護分開；既有 OCP 功率緩衝研究再依持續時間區分 | 故障隔離、人員安全連鎖與接地保護仍須另外處理 |

這張表先分「誰被保護、發生什麼事、要多快動作」，再看需要哪些元件。同一個控制器或模組
可能整合多項功能，但整合不代表責任消失；反過來，一項安全要求也可能由多顆元件與機構共同完成。
因此，元件價值仍要由量產電路架構與客戶資格驗證重建，不能把規格要求的項目數直接當成材料清單顆數。

## 為什麼監測資料暫時仍屬於保護功能

Infineon 的 48V 電子保險絲資料已列出電壓、電流、能量、功率、故障與異常等即時監測值，
800V 產品頁也把監測列為功能方向。然而本輪尚未找到跨平台共用的事件格式、時間戳記、故障後
動作、資料保存、現場紀錄與維修決策契約。因此，監測資料目前只視為保護流程的一部分，不另建
「AI 電源監控」商業題材；等 OCP 或買方把欄位與後續動作固定後，再評估是否具有獨立價值。

## 怎麼用這張表判讀公司新聞

1. **先列出故障與處置對照表**：寫下每種故障、偵測器、清除裝置、反應時間、隔離範圍與安全失效狀態。
2. **分清規格與產品階段**：OCP 規格、供應商參考設計、樣品、客戶資格驗證與實際量產不能混成同一級。
3. **再對回量產材料清單與公司**：只有同一平台的電路架構、料號、客戶驗證與供應商申報對齊後，才能討論份額與財務。
4. **把監測資料綁到實際動作**：量測值與事件欄位還要連到隔離或維修決策，形成閉環後才有獨立知識價值。

## 研究判定

- **目前可保留的結論**：800V 保護至少包含人身與維修、絕緣與接地、故障電流，以及帶電插拔與湧入電流等不同責任；三條一手來源鏈足以重建基本的故障與處置對照表。
- **可信度為中而不是高**：OCP 提供系統規格，TI 與 Infineon 提供供應商架構、樣品與參考設計；目前仍缺共用的量產故障處置表與現場資料。
- **目前不能發布的結論**：保護元件顆數倍增、指定 SiC／Si／被動元件或台灣公司勝出、監測資料已形成獨立商業價值，以及已取得訂單、收入或毛利。
- **需要看到什麼才能前進**：具名量產平台公布完整保護電路架構、客戶資格驗證、故障紀錄、維修動作與材料清單，再由台灣公司申報交叉確認財務分母。

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
