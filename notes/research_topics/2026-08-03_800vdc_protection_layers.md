# 800VDC 保護不是一顆保險絲：人身、故障電流與 Hot-swap 必須分層

<!-- research_topic
topic_id: MI-2026-08-03-800VDC-PROTECTION-LAYERS
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-03
source_published_at: 2026-03-01
last_reviewed_at: 2026-08-13
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
confidence_basis: OCP Diablo 400 明列 accessibility／interlock、creepage／clearance、overcurrent、earthing、leakage 與 ground-fault requirements，IEC 60947-10 公開摘要再把半導體斷路器的電流切斷與串聯機械隔離分開，TI 與 Infineon 則補上 800V hot-swap／inrush、故障清除與殘餘電荷放電；足以建立保護及維修安全責任層，但尚無共同 production topology、完整 safe-state fault matrix、台灣供應商 qualification 或財務證據
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

<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_precharge_and_fault_clearing_time_scale_evidence_without_refreshing_thesis_clock
evidence: sources:S8
-->

<!-- transition
date: 2026-08-13
from: triaged
to: triaged
reason: added_interruption_isolation_discharge_and_safe_access_sequence_with_six_field_service_passport
evidence: sources:S9
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
- **故障清除時間（fault-clearing time）**：從異常被偵測，到電力路徑被限制或切斷所需的時間；必須連同故障型態、電壓、電流、溫度與開關安全工作區判讀。
- **電流切斷與隔離（interruption／isolation）**：前者停止故障電流，後者建立可確認的機械斷開邊界；電子開關關閉不必然等於已具備維修隔離。
- **殘餘電荷放電（stored-energy discharge）**：主開關關閉後，電容仍可能保有能量；需有明確放電路徑，並以指定時間後的殘餘電壓確認結果。
- **可安全維修狀態（service-safe state）**：不是單一訊號，而是切斷、隔離、放電與獨立確認都達到規定條件後，才允許人員接近的狀態。
- **IEC 60947-10**：2026 年發布、涵蓋最高 1,500VDC 半導體斷路器的國際標準；本文只使用 IEC 公開摘要，不把未取得的完整條文或測試細節自行補齊。
- **STDA029**：TI 於 2026 年 3 月發布的 800V／±400V floating-ground hot-swap 技術白皮書代號；它是一組指定實驗架構，不是產業共同標準。
- **OFF（關閉命令）**：控制器要求電子開關停止導通的狀態；它需要用實際電流、隔離接點與殘餘電壓再確認，不能單獨充當安全證明。

### 三句話抓重點

- OCP Diablo 400 規格把人員接近高壓、絕緣與接地、過大電流及漏電等風險分開規定，表示 800V 機櫃不能只靠一種保護方式。
- IEC、TI 與 Infineon 的公開資料顯示，帶電插入時要慢慢限制湧入、故障時要快速切斷，但切斷後仍要建立機械隔離並排掉殘餘電荷；這些時鐘和長時間備援、接地或人員防護又是不同責任。
- 目前證據只足以畫出誰負責什麼，尚不能證明台灣功率元件、電源供應或被動元件公司已進入量產材料清單、取得訂單或形成可辨識獲利。

### 為什麼重要

**先問要保護的是誰、遇到什麼事。** 人員接近帶電部位、導體過流、絕緣或接地故障、設備帶電
插入時替大電容充電，以及停電時維持運作，是五種不同事件。

**再把每個事件交給不同保護責任。** 安全連鎖先保護人員，斷路與主動開關處理異常電流，
不停機更換與電子保險絲控制接通，電容與電池備援則維持短暫供電。即使都在同一條電力路徑，
預充也要給大電容時間慢慢充電，短路或過流卻要盡快限制故障能量；它們可以合作，但不能互相取代。

**最後才談公司與元件價值。** 把所有責任混成「保護元件」，會重複計算量產材料清單，也會把
供應商參考設計的技術能力誤寫成客戶量產訂單。

### 接下來怎麼追

- 追 OCP 或平台規格是否把每種故障、偵測時間、斷電範圍、安全連鎖、接地與維修程序對齊。
- 追具名平台是否把電流切斷、機械隔離、儲能放電、殘餘電壓確認、維修放行與復歸測試串成同一個可稽核狀態機。
- 追 800V 不停機更換與電子保險絲，是否從參考設計推進到具名平台的預充軌跡、故障清除時間、客戶資格驗證、實際量產、現場故障紀錄與維修閉環。
- 追台灣相關公司是否由客戶文件與公司申報雙向確認具名保護產品、額定規格、測試、量產、收入及毛利。

### 想一想

- 保險絲可以切斷過大的故障電流，但設備帶電插入時，大電容也會瞬間吸收電流；預充要慢、短路清除要快，為什麼同一條電力路徑需要兩支不同速度的時鐘？
- 不停機更換功能能限制湧入電流，是否就能取代安全連鎖、保護接地或接地故障偵測？
- 如果監測資料只有數值與故障清單，沒有規定發生事件後要隔離哪裡、怎麼維修，能否成為獨立產品價值？
- 如果控制器顯示 FET 已關閉，但隔離接點沒有位置回饋、下游電容也沒有殘壓量測，能否允許人員接近？

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

<!-- research_source
source_id: S8
role: other_primary
source_kind: document
publisher: Texas Instruments
title: Floating Ground Hot-Swap Architecture to Enable Robust Protection on 800V or ±400V DC Power Distribution
published_at: 2026-03-01
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.ti.com/lit/wp/stda029/stda029.pdf
locator: PDF 第 1 頁摘要；第 4–5 頁的 800V、100µF、200mA startup 設計算例與 440ms 計算值；第 6 頁 Test Results 的 22A gradual-overcurrent 10µs 關斷與 steady-state output short 數微秒關斷
limitation: 文件只標示 March 2026，published_at 以月份首日作公開月份錨點而非精確發布日；數字只屬 TI 指定元件、800V、100µF、17kW、60°C 最大環境溫度等條件下的實驗架構，不是跨廠標準、所有故障、量產平台、客戶資格、現場可靠度、production BOM 或台灣公司財務證據
independence_group: texas-instruments
-->

<!-- research_source
source_id: S9
role: standard
source_kind: document
publisher: International Electrotechnical Commission
title: IEC 60947-10:2026 Low-voltage switchgear and controlgear — Part 10: Semiconductor circuit-breakers
published_at: 2026-05-12
captured_at: 2026-08-13
accepted_at: 2026-08-13
status: active
url: https://webstore.iec.ch/en/publication/67514
locator: IEC 公開摘要的適用範圍與 covered types；最高 1,000VAC／1,500VDC，SCCB 與 semiconductor hybrid circuit-breaker 都另列為 isolation function 串聯的 mechanical isolation contacts
limitation: 公開頁只提供標準範圍、斷路器類型與目標摘要，未提供付費標準 121 頁的完整定義、性能門檻、測試方法或 conformity 結果；不能由摘要外推特定 rack 拓撲、殘餘電壓門檻、量產採用或供應商財務
independence_group: iec-60947-10
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
supporting_source_ids: S1,S2,S3,S9
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

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: TI 的 STDA029 實驗架構在指定 800V、100µF 負載條件下，以 200mA startup target 算得約 440ms 預充時間；其第 6 頁測試另顯示 gradual overcurrent alert 約 22A 時在 10µs 內關斷 FET，steady-state output short 則在數微秒內關斷
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-03-01
basis: S8 第 4–5 頁列出 system specification、startup target 與計算時間，第 6 頁 Test Results 分別列出 gradual-overcurrent 與 output-short 的實測關斷結果
boundary: 只證實 TI 這組實驗架構與指定條件的設計算例及測試結果；不外推為所有電容量、負載、溫度、故障型態、元件、平台或量產系統的共同時間門檻
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: inference
status: active
claim: 800V hot-swap／power-path protection 至少要分開檢查受控接通的預充時間與異常發生後的故障清除時間；前者避免匯流排壓降與開關超出安全工作區，後者限制故障能量，因此不能用單一「反應速度」評價整個保護設計
supporting_source_ids: S3,S8
contrary_source_ids:
as_of: 2026-03-01
basis: S3 以 SOA 控制 inrush，S8 又在同一 hot-swap 架構中分別給出 startup 設計時間與過流／短路關斷時間；兩條獨立公司來源鏈共同支持雙時間尺度的工程判讀
boundary: 這是研究端對保護時序責任的推論，不建立通用的預充或清除時間、比較供應商性能，也不指定 fault matrix、元件數、production topology、客戶資格或財務受惠
verification_needed: 需具名 production platform 在一致電壓、電流、電容量、溫度、SOA 與 fault-type 條件下，公布完整 pre-charge trajectory、fault-clearing matrix、qualification 與 field log
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: IEC 60947-10:2026 的公開摘要適用最高 1,500VDC 半導體斷路器，並分別描述 semiconductor circuit-breaker 與 hybrid circuit-breaker；兩類都另以串聯 mechanical isolation contacts 執行 isolation function
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-05-12
basis: S9 公開摘要逐項列出額定範圍與兩類 breaker 架構，且兩類的 isolation function 都明列 series mechanical isolation contacts
boundary: 只證實 IEC 公開摘要中的適用範圍與類型分工；未取得的完整條文、性能門檻、測試方法、特定 800V rack 實作與 conformity 結果都不自行推論
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: TI STDA029 的指定 hot-swap 實驗架構在 FET 關閉或輸入斷開時啟用 output discharge circuit，並以 2kΩ、10W 電阻把 100µF 輸出電容設計為 1.5 秒內放電；文件的整體解法摘要只承諾小於 2 秒
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-03-01
basis: S8 第 5 頁 Output Discharge Circuit 直接列出啟動條件、2kΩ／10W、100µF 與 1.5 秒設計值，摘要則列 output discharge time <2 seconds
boundary: 這是 TI 指定電容量、電阻、功率與實驗架構的設計例，不是 IEC 或 OCP 的通用殘餘電壓門檻，也不能外推所有 800V 平台的放電時間、觸電風險或維修程序
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: inference
status: active
claim: 800V 維修安全至少要把故障電流切斷、機械隔離、儲能放電與可安全接近確認分成四道狀態；研究文件還應固定事件與工況、偵測門檻與計時、切斷裝置與清除時間、隔離邊界與接點狀態、儲能／放電路徑與殘餘電壓時間，以及安全接近與復歸責任六個欄位
supporting_source_ids: S1,S8,S9
contrary_source_ids:
as_of: 2026-08-13
basis: S9 把 semiconductor interruption 與 series mechanical isolation 分開，S8 顯示主 FET 關閉後仍另需 output discharge，S1 又要求高壓部位帶電時不可接近並以 interlock／power-off 先去能；三條獨立來源共同支持四道狀態，六欄則是研究中心把可追溯條件整合成的查核護照
boundary: 四道狀態與六欄護照是研究端綜合方法，不是 IEC、OCP 與 TI 共同發布的標準、完整 LOTO 程序或通用 pass-fail 門檻；不指定唯一拓撲、殘餘電壓、時間、元件、供應商或財務受惠
verification_needed: 需具名 production platform 的 one-line diagram、fault／service state machine、隔離接點回饋、放電軌跡、殘餘電壓門檻、獨立驗證、維修許可、復歸測試與 field record
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: unverified
status: active
claim: 具名 800V production rack 已以同一固定版本公開完整六欄維修安全護照、逐項 pass-fail、故障注入、隔離回饋、放電曲線、殘餘電壓、現場維修紀錄與復歸結果
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-13
basis: 現有來源分別只到 OCP 系統 requirement、IEC 公開標準摘要、TI 實驗架構與 Infineon sampling reference design，尚未找到同一具名量產平台把六欄及現場結果完整公開
boundary: 不把規格存在、breaker 類型、FET OFF、單一放電設計例、interlock 訊號或 reference board 改寫成整機已完成 service-safe qualification
verification_needed: 平台商或買方以固定版本公開完整六欄、測試條件、pass-fail、原始軌跡、維修與復歸紀錄，並能由第二條獨立來源鏈核對
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

## 同一條電力路徑有兩支時鐘

設備剛接上高壓匯流排時，負載端的大電容像空水桶：如果一次灌滿，瞬間電流可能拉低匯流排電壓，
也可能讓功率開關超出安全工作區。因此，預充刻意把接通拉長。可是設備已接通後若發生短路或過流，
時間拖得越久，故障能量就可能越大，此時反而要盡快限制或切斷。這不是設計互相矛盾，而是同一條
電力路徑在不同事件下有不同任務。

| 時鐘 | 發生什麼事 | TI STDA029 的指定條件例子 | 這個數字不能怎麼用 |
|---|---|---|---|
| 接通／預充時鐘 | 受控替負載電容充電，避免匯流排壓降與開關超出安全工作區 | 800V、100µF 的設計算例以 200mA 為 startup target，計算約 440ms | 不能當成不同電容量、負載、溫度或元件都應採用的固定預充時間 |
| 故障清除時鐘 | 偵測過流或短路後限制故障能量，並切離電力路徑 | 第 6 頁測試中，約 22A gradual overcurrent 在 10µs 內關斷；steady-state output short 在數微秒內關斷 | 不能當成所有故障型態、配線、保護層或量產平台的共同清除時間 |

這兩列不是在比較「440ms 比 10µs 慢多少」，而是在提醒讀者先辨認事件。真正的設計判讀仍要把
電壓、電流、電容量、溫度、功率開關安全工作區、故障路徑與隔離範圍放在同一張故障與處置對照表；
若只看到一個漂亮的反應時間，卻不知道測的是接通還是故障，就無法判斷保護是否完整。

## 關掉不等於沒電：四道維修安全閘門

**先停止電流，還不代表人可以伸手進去。** 電子開關可能已把故障電流切斷，但上游、下游或電容
仍可能帶電；控制器顯示 `OFF` 也不等於已經形成可目視或可回饋確認的機械隔離。IEC 60947-10
的公開摘要正好把這兩件事拆開：半導體元件負責 breaker 的切換，隔離功能另有串聯機械隔離接點。

**隔離完成，還要處理儲存的能量。** TI 的 STDA029 在主 FET 關閉或輸入斷開後，仍另外啟動
output discharge circuit；指定設計用 2kΩ、10W 電阻替 100µF 輸出電容放電，目標 1.5 秒內完成，
而解法摘要只寫小於 2 秒。這是一個參考設計例，不是所有 800V 系統共同的安全秒數；真正的
pass-fail 必須同時寫出初始電壓、電容量、放電路徑、時間點與可接受殘餘電壓。

| 四道閘門 | 這一步回答什麼 | 只看到什麼還不夠 |
|---|---|---|
| 1. 故障電流切斷 | 異常電流是否已停止，清除時間與隔離範圍是什麼？ | 只看到 controller 報警、FET command OFF 或單一反應時間 |
| 2. 機械隔離 | 哪一對接點建立維修斷開邊界，實際位置是否有回饋？ | 只由軟體狀態推定接點真的斷開 |
| 3. 儲能放電 | 哪些電容或其他儲能仍帶電，由哪條路徑在多久內降到什麼電壓？ | 只寫「有 bleeder」或移植別份設計的秒數 |
| 4. 安全接近確認 | 誰、用哪個獨立量測與程序放行維修，失敗時如何保持禁止接近？ | 只把 interlock 訊號、門鎖或斷路器標示當成量測結果 |

OCP Diablo 400 要求高壓帶電部位不可讓人員接近，並以 interlock／power-off 在接近前去能；但本文
引用的條文沒有替所有實作指定同一個殘餘電壓或等待時間。因此，研究時不能把「已切斷」「已隔離」
「已放電」與「已確認可接近」合成一個綠燈，也不能把 TI 的 1.5 秒設計例升格為 OCP 或 IEC 門檻。

### 六欄維修安全護照

| 欄位 | 最少要記什麼 | 為什麼不能省略 |
|---|---|---|
| 1. 事件與工況 | 正常停機、過流、短路、接地故障或輸入拔除；電壓、負載、溫度與版本 | 不同事件的能量路徑與安全狀態不同 |
| 2. 偵測與計時 | 感測器、門檻、去彈跳／延遲、計時起點與失效處理 | 不知道計時從哪裡開始，就不能比較反應時間 |
| 3. 切斷結果 | 執行元件、峰值電流、清除時間、選擇性與受影響範圍 | command OFF 不等於電流已停止 |
| 4. 隔離邊界 | 機械接點位置、回饋狀態、可見斷開或等效確認與失效安全狀態 | 電子開關不自動提供維修隔離證據 |
| 5. 儲能與殘壓 | 電容／其他儲能、初始條件、放電路徑、殘餘電壓、量測位置與時間 | 關掉來源後，下游仍可能保留危險能量 |
| 6. 放行與復歸 | 獨立驗證工具、放行者、維修許可、重新上電前檢查與變更紀錄 | 安全狀態必須能被證明，也要能安全退出 |

這六欄是研究中心把 IEC、OCP 與 TI 文件拼成的查核方法，不是三方共同發布的表單，也不是完整的
lockout／tagout 作業程序。它的用途是攔下最常見的跨級推論：breaker 有動作，不等於隔離接點已
確認；接點已斷開，不等於電容已放完；電壓下降，也不等於現場已依程序允許接近。

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

- **目前可保留的結論**：800V 保護至少包含人身與維修、絕緣與接地、故障電流，以及帶電插拔與湧入電流等不同責任；hot-swap 還要把受控預充與故障清除兩支時鐘分開，維修安全則要再確認電流切斷、機械隔離、儲能放電與安全接近四道狀態。
- **可信度為中而不是高**：OCP 提供系統規格，TI 與 Infineon 提供供應商架構、樣品與參考設計；TI 實驗架構補上了指定條件的時間尺度，但目前仍缺共用的量產故障處置表與現場資料。
- **目前不能發布的結論**：保護元件顆數倍增、指定 SiC／Si／被動元件或台灣公司勝出、監測資料已形成獨立商業價值，以及已取得訂單、收入或毛利。
- **需要看到什麼才能前進**：具名量產平台公布完整保護電路架構、客戶資格驗證、故障紀錄、維修動作與材料清單，再由台灣公司申報交叉確認財務分母。

## 來源

- [OCP：Diablo 400 Rack and Power Specification 0.7.0](https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf)
- [Texas Instruments：800V hot-swap input protection reference architecture](https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html)
- [Texas Instruments：800V／±400V floating-ground hot-swap technical white paper](https://www.ti.com/lit/wp/stda029/stda029.pdf)
- [Infineon：400／800V power-path protection 與 REF_XDP701_4800](https://www.infineon.com/technology-news/2025/INFPSS202510-002)
- [IEC：IEC 60947-10:2026 半導體斷路器公開摘要](https://webstore.iec.ch/en/publication/67514)
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

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C6,C7
metric: 具名 800V production platform 是否分別公開預充與各類故障清除的完整時間軌跡、SOA 與 pass-fail matrix
source_ids: S3,S8
watch_source_ids: S4,S5,S6
frequency: monthly
next_check: 2026-09-01
trigger: 平台、規格或客戶文件以固定電壓、電流、電容量、溫度及 fault type 公布 pre-charge trajectory、clearing time、隔離範圍與 qualification 結果
invalidation: Production data 顯示預充與故障清除不需分開建模，或本文雙時間尺度無法預測安全接通與限制故障能量
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C8,C9,C10,C11
metric: 具名 800V production platform 是否公開從電流切斷、機械隔離、儲能放電到安全接近與復歸的完整六欄維修安全護照
source_ids: S1,S8,S9
watch_source_ids: S4,S5,S6
frequency: monthly
next_check: 2026-09-01
trigger: 平台或買方文件以固定版本公布事件／工況、偵測與計時、切斷結果、隔離接點回饋、放電與殘壓軌跡、獨立安全確認、維修放行及復歸測試
invalidation: Production architecture 或 field evidence 顯示切斷、隔離、放電與安全確認不需分開，或六欄護照無法辨識實際 service-safe failure
-->

## 什麼會推翻這篇

- Production architecture 證明單一裝置在相同安全完整性與維修條件下可完整取代 interlock、earthing、overcurrent／ground-fault、hot-swap 與 ride-through 各層責任。
- OCP 或平台後續 requirement 移除本文關鍵責任，或 field evidence 顯示分層會造成錯誤的故障判讀。
- 若台灣公司只有「800V、保護、SiC、電源」字樣而始終沒有具名產品、資格、production 與財務分母，族群 route 應維持待驗證而非升格。
