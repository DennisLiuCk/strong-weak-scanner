# AI 機櫃儲能要接力：短暫尖峰、機櫃備援與設施儲能各有任務

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
reason: editorial_plain_language_wave83_storage_timescale_no_conclusion_change
evidence: editorial:plain_language_wave83_storage_timescale
-->

<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_power_energy_response_handoff_recharge_and_life_event_contract_without_refreshing_thesis_clock
evidence: sources:S2,S6,S7
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **CBU（Capacitor Bank Unit）**：以電容或超級電容靠近機架吸收很快的功率尖峰與低谷，重點是高功率、快速反應，不是長時間供電。
- **Rack（機架／機櫃）**：集中安裝運算、電源、儲能與冷卻設備的結構單位。「靠近機架」代表需更快回應局部功率波動。
- **DC（Direct Current，直流電）**：電流主要往固定方向流動。機架內的高壓直流匯流排，是 CBU 或 BBU 可能連接的電力節點。
- **PSU（Power Supply Unit，電源供應單元）**：把輸入電力轉成設備需要的電壓與電流；其內建保持能量可先撐過極短交接縫隙。
- **DOE（U.S. Department of Energy，美國能源部）**：本文引用其通用儲能定義與性能方法，用來拆解規格欄位，不代表 DOE 對 AI 機架架構背書。
- **BBU（Battery Backup Unit）**：以電池在機架或直流匯流排側提供短時 ride-through，目的通常是跨過電源切換或受控停機，不等於設施級儲能。
- **BESS（Battery Energy Storage System）**：位於設施或公用電網介面側的較大型電池儲能，用來處理較慢、影響範圍更大的負載變化與發電機切換。
- **時間尺度**：事件從發生到需要被補償的快慢。元件若在錯誤的時間尺度工作，即使都能儲能，也不代表可互相替代。
- **Diablo 400**：OCP 的機架與電源規格專案，分別列出 BBU 與 capacitor bank 選項；規格選項不等於所有平台都採用。
- **EDLC（電雙層電容）**：可快速反覆充放電的超級電容；TI 用它示範 CBU，但 reference design 不等於量產 BOM。
- **功率尖峰／低谷**：用電量在很短時間內突然升高或降低；緩衝設備要快速補上或吸收這段差額，避免供電系統失穩。
- **儲能**：先把能量存起來，再在需要時釋放；電容與電池都能儲能，但反應速度、可支撐時間、位置與維護條件不同。
- **高壓直流匯流排**：在機櫃或資料中心內集中傳送高壓直流電的共同電力路徑，儲能與轉換設備可能接在這裡。
- **備援**：主要電力短暫中斷時，由另一套設備接手，讓系統撐過切換或安全關機所需時間。
- **短暫供電不中斷（ride-through）**：在主電源波動或切換時，暫時維持設備供電；它不是長時間停電備援的同義詞。
- **電源切換**：供電從一個來源轉移到另一個來源的過程；切換期間若出現空檔，就需要儲能設備補上。
- **受控停機**：電力無法持續時，讓設備按安全順序降載、保存狀態並關閉，避免突然斷電造成損壞或資料問題。
- **公用電網接點**：資料中心設施與外部電網連接的位置；設施級儲能會在這一層協調整體負載與備用發電機。
- **互通測試**：確認不同供應商的設備能依共同接口、訊號與保護規則一起運作。
- **客戶資格驗證（qualification）**：客戶依自己的電氣、安全、可靠度與系統條件，確認產品是否可被採用的測試階段。
- **現場部署（field deployment）**：設備已在實際場域安裝運作；它比展示或參考設計更接近真實採用，但仍需確認部署數量與範圍。
- **充放電任務循環（duty cycle）**：設備在多長時間內、以多大功率、多久一次進行充放電；它會影響容量、壽命、散熱與維護需求。
- **功率容量（power capacity）**：儲能設備當下能以多快的速度輸出或吸收能量，通常以 W、kW 或 MW 表示；它回答「這一刻補得上多少差額」。
- **能量容量（energy capacity）**：設備能儲存的能量總量，通常以 Wh、kWh 或 MWh 表示；它回答「在指定輸出下能撐多久」。
- **可用能量（usable energy）**：扣除最低／最高電壓或荷電狀態、安全餘裕、轉換與輔助負載損失後，任務真正能取出的能量；不等於銘牌總容量。
- **反應時間（response time）**：從偵測事件到儲能輸出達到指定功率所需時間。只看能量夠不夠，仍可能因反應太慢而接不上。
- **交接時間（handoff time）**：主電源、內建保持能量、CBU／BBU 與後續電源之間切換的時間窗口；前一層必須撐到下一層穩定接手。
- **回充時間（recharge time）**：一次放電後恢復到可再次執行任務所需時間；事件來得比回充快，就可能出現「第一發有用、第二發沒電」。
- **荷電狀態（SOC）**：儲能剩餘能量相對於可用範圍的狀態指標。相同銘牌容量在不同 SOC 下，不代表當下有相同備援能力。
- **往返效率（round-trip efficiency）**：同一荷電狀態起訖下，放出的淨能量相對於充入能量的比率；充放電、轉換、熱管理與輔助設備都可能造成損失。
- **循環壽命／日曆壽命**：前者看反覆充放電與放電深度累積後能用幾次，後者看即使不頻繁使用也會隨時間、溫度與 SOC 老化多久。
- **參考設計（reference design）**：供應商公開的可行電路與元件組合，用來示範一種做法；不等於客戶已採用或量產。
- **量產材料清單（production BOM）**：客戶量產產品實際核准使用的元件與數量清單；進入清單仍不等於已取得固定份額或收入。

### 三句話抓重點

- 事件持續時間只是第一道篩選：還要同時寫清功率缺口、可用能量、反應與交接、重複頻率、回充、損耗、散熱及壽命，才知道設備能不能連續完成任務。
- 機櫃旁的電容儲能模組（CBU）重視反應速度，機櫃電池備援單元（BBU）負責短暫供電不中斷與受控停機，設施級電池儲能系統（BESS）則協調整體負載與發電機切換；時間可能重疊，但位置與任務仍不同。
- NVIDIA、OCP 與 TI 的公開資料足以建立這三種角色，還不能證明台灣被動元件、電源供應或功率元件公司已進入量產材料清單、取得訂單或認列收入。

### 為什麼重要

**先看事件持續多久。** 毫秒至秒的功率尖峰，需要靠近機櫃的設備快速反應；數十秒的供電
空檔，需要電池讓設備撐過切換或完成受控停機；秒至分鐘的整體負載變化，則由設施級儲能協調。

**再把功率和能量分開。** 功率是「當下補多少」，能量是「可以補多久」；同樣能撐一段時間的
兩套設備，若反應速度、可用 SOC 窗口或回充節奏不同，就不一定能處理同一種事件。

**接著看設備離誰最近。** 電容儲能模組與電池備援多半靠近機櫃或高壓直流匯流排，設施級儲能
則位在資料中心設施或公用電網接點。距離不同，反應速度、配電延遲、維修與安全條件也不同。

**最後才談公司與元件需求。** 架構需要某一層儲能，不代表任何零件供應商已經取得訂單；要先
確認具名產品、客戶資格驗證、現場部署與量產材料清單，才能把系統角色翻譯成數量與財務貢獻。

### 接下來怎麼追

- 追 OCP Open Rack／Diablo 是否把電容儲能、電池備援、高壓直流匯流排、保護與連接器寫成正式規格，並完成互通測試。
- 追同一平台是否公開事件波形、可用能量窗口、反應／交接時間、回充時間、重複頻率、溫度、效率與壽命，避免只拿一個「備援秒數」比較設備。
- 追 NVIDIA 或平台客戶是否公布同一量產機櫃中，三種儲能設備的位置、額定任務、客戶資格驗證與現場部署資料。
- 追台灣被動元件、電源供應與功率元件公司是否以具名產品、客戶驗收、量產數量及可辨識財務貢獻完成雙向核對。

### 想一想

- 機櫃旁的電容儲能模組只能處理毫秒到秒的尖峰，為什麼不能取代能支撐數十秒的電池備援單元？
- 兩套設備的銘牌能量若一樣，但一套能快速輸出、另一套只能慢慢放電，為什麼不能視為相同備援能力？
- 一套儲能第一次尖峰能接住，卻來不及在下一次尖峰前回充，這算不算符合任務？還缺哪個規格欄位？
- 設施級電池儲能能平滑秒至分鐘的整體負載，為什麼仍不能取代靠近機櫃的快速緩衝？
- 一家公司被列在 800V 生態系，和它的具名電容、控制器或電源模組進入量產材料清單，中間還缺哪些驗證？

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

<!-- research_source
source_id: S6
role: regulator_or_policy
source_kind: document
publisher: U.S. Department of Energy
title: Solar Integration: Solar Energy and Storage Basics
published_at: 2025-03-31
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.energy.gov/cmei/systems/solar-integration-solar-energy-and-storage-basics
locator: What Is Energy Storage 段落；energy capacity 是可儲存總能量，power capacity 是特定時點可釋放速率，不同組合對應不同任務，且儲能轉換與取回不可能零損失
limitation: DOE 的太陽能與電網入門頁提供跨技術定義，不是 AI rack、CBU、BBU 或 BESS 的產品規格、qualification、控制序列、供應商 BOM 或財務證據
independence_group: us-doe
-->

<!-- research_source
source_id: S7
role: regulator_or_policy
source_kind: document
publisher: U.S. Department of Energy
title: Energy Storage Valuation: A Review of Use Cases and Modeling Tools
published_at: 2022-06-01
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.energy.gov/sites/default/files/2022-06/MSP_Report_2022June_Final_508_v3.pdf
locator: PDF pp.14–15（報告頁碼 9–10），Figure 2、Operating Costs 與 Performance Metrics；分列 power equipment、controls、round-trip efficiency、response time、cycle life 與 calendar life，並定義各自量測邊界
limitation: 這是以定置型 ESS 估值與方法為主的政府技術報告，不是 AI 機架實測；其指標可當規格拆解方法，但不能把 grid-scale 數值、成本或壽命直接套到 CBU／BBU
independence_group: us-doe
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

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: DOE 把儲能的 energy capacity 與 power capacity 分成兩個尺度；前者描述可儲存總能量，後者描述特定時點可釋放的速率，而不同組合會對應不同任務
supporting_source_ids: S6
contrary_source_ids:
as_of: 2025-03-31
basis: S6 的 What Is Energy Storage 段落直接定義 energy capacity、power capacity 與任務差異
boundary: 只支持通用儲能概念；不指定 AI rack 的額定功率、持續時間、元件技術、控制拓撲或供應商
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: DOE 的 ESS 方法把往返效率、反應時間、循環壽命與日曆壽命分開量測；反應時間是從零到額定功率，循環壽命受放電深度影響，電池日曆壽命則與環境溫度及 SOC 有關
supporting_source_ids: S7
contrary_source_ids:
as_of: 2022-06-01
basis: S7 PDF p.15（報告頁碼 10）的 Performance Metrics 逐項定義 RTE、response time、cycle life 與 calendar life
boundary: 這些是跨技術 ESS 方法欄位，不代表 CBU、BBU、BESS 具有相同測試法、數值或退化機理，也不支持任何 AI 平台商業判定
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: OCP Diablo 400 要求 PSU／shelf 的保持能量涵蓋 AC dropout 到儲能 ramp-up 的平順交接，並明列 BBU 不應由 peak 或 dynamic loading 觸發；動態負載測試另分 load step、frequency、duty cycle、pulse duration 與 slew rate
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-03-01
basis: S2 7.1.3.2 說明 transition，7.3.2–7.3.3 把短峰值／動態負載與 BBU backup 分開，Tables 5–8 列出事件波形欄位
boundary: 只證實 Diablo 400 0.7.0 的系統責任與測試欄位；不代表所有 AI rack 使用相同 profile、控制閾值或 BBU／CBU 分工
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: inference
status: active
claim: 判讀 AI 功率緩衝不能只看「能撐幾秒」；至少要把任務與觸發、功率波形、持續時間與可用能量、反應與交接、重複與回充、損耗與散熱、壽命與安全寫成同一事件合約，才能比較 CBU、BBU 與 BESS 是否可接力或替代
supporting_source_ids: S2,S6,S7
contrary_source_ids:
as_of: 2026-08-12
basis: S6 分開 power 與 energy，S7 分開 efficiency、response、cycle／calendar life，S2 又把 transition、backup trigger 與動態波形分開；合併後形成七欄規格閱讀框架
boundary: 七欄是本文的證據整理方法，不是 OCP 或 DOE 頒布的單一標準，也不替任何平台設定數值、優先技術、供應商或商業結論
verification_needed: 需同一 production platform 公布完整事件波形、控制邏輯、可用能量窗口、回充、熱安全、壽命與 field pass／fail 資料，才能驗證實際接力邊界
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 三種儲能怎麼接力：先看事件持續多久

| 事件持續多久 | 誰來處理 | 設備在哪裡 | 目前一手證據 | 還不能因此判定 |
|---|---|---|---|---|
| 毫秒至秒的快速尖峰與低谷 | 機櫃旁的電容儲能模組（CBU） | 靠近機櫃或高壓直流匯流排 | NVIDIA 的短時電容層、OCP 電容儲能選項、TI 超級電容模組 | 固定電容量、電容材料、供應商、單機價值或量產份額 |
| 約 45 至 90 秒的短暫供電中斷、電源切換或受控停機 | 機櫃電池備援單元（BBU） | 機櫃或高壓直流匯流排側 | OCP Diablo 400 的獨立電池備援選項 | 所有平台都採相同秒數、電池化學體系、模組供應商或採購量 |
| 秒至分鐘的整體負載變化與發電機切換 | 設施級電池儲能系統（BESS） | 資料中心設施或公用電網接點 | NVIDIA 的設施級電池儲能層 | 能取代機櫃緩衝、所有專案都採 800V 直流電或台灣族群已有收入 |

先用事件持續時間排第一遍，再用設備位置與失效任務校正。電容儲能模組重點是很快輸出大功率，
機櫃電池備援要跨過短暫供電空檔，設施級電池儲能則支撐更久、影響範圍更大的負載變化。時間區間
可能重疊，但不代表三者可以互換。只有同一平台揭露充放電任務循環、電壓、功率、能量、溫度、
安全與壽命條件後，才有資格把架構翻譯成元件規格與用量。

## 「能撐多久」不是完整規格：先寫七欄事件合約

把儲能想成接力賽，比只看電池或電容更容易理解。主電源掉下來時，PSU 內建的保持能量先撐住；
下一層儲能必須在前一層耗盡前升到所需功率；如果事件是正常的短尖峰，控制器又不該誤把它當停電
而啟動 BBU。OCP Diablo 400 正是把「平順交接」「峰值負載」與「備援啟動」分開寫。

| 事件合約欄位 | 新手要問的問題 | 漏掉時最常見的誤判 |
|---|---|---|
| 1. 任務與觸發 | 是吸收正常尖峰、跨過電源切換、撐到發電機接手，還是讓設備受控停機？什麼訊號才啟動？ | 把正常動態負載當成停電，或把備援設備當成每次尖峰都要放電 |
| 2. 功率缺口與波形 | 差額有多大？上升多快？是單一脈衝、週期振盪，還是持續平台？ | 只看平均功率，忽略瞬間輸出、slew rate 與轉換器電流限制 |
| 3. 持續時間與可用能量 | 缺口維持多久？在最低／最高電壓、SOC、安全餘裕與損耗後，實際能取出多少？ | 把銘牌能量全部當成可用能量，或只看秒數卻沒核對負載大小 |
| 4. 反應與交接 | 從偵測到額定輸出要多久？前一層保持能量能否撐到下一層穩定接手？ | 能量總量夠，卻因反應太慢在交接縫隙先掉電 |
| 5. 重複、回充與可用率 | 事件多久再來一次？一次放電後多久恢復？充電會不會擠壓正常供電或散熱？ | 第一個事件接得住，第二個事件到來時仍未恢復 |
| 6. 損耗、輔助負載與散熱 | 充放電、DC/DC、控制與冷卻各損失多少？在哪個溫度與負載條件量測？ | 用理想能量估算續航，忽略實際可交付功率與熱限制 |
| 7. 壽命、安全與維護 | 指定放電深度、SOC、溫度與循環後能工作多久？故障時如何隔離、告警與更換？ | 把一次展示成功當成可長期反覆運行，或忽略安全與維修邊界 |

最簡化的關係是「所需能量約等於功率缺口乘以持續時間」，但這只是起點。工程上還要把輸出端
reference plane、可用電壓／SOC 窗口、轉換與輔助損失、最差溫度、老化後容量及安全餘裕寫進去。
因此，同樣標示一段備援時間的兩套設備，若負載、起始 SOC、回充與壽命條件不同，仍不能直接比較。

### 一次事件如何接力：偵測、響應、交接、恢復

1. **辨識事件**：控制器先區分正常負載尖峰、輸入電壓暫降、主電源中斷與設備故障，避免錯誤觸發。
2. **先撐住交接縫隙**：PSU 內建保持能量或最近端電容先維持匯流排，讓 CBU／BBU 有時間升功率。
3. **由指定層承擔任務**：CBU 處理快速功率差額，BBU 跨過切換或受控停機，BESS 協調設施級負載與較長事件；實際邊界依平台而定。
4. **交給下一來源或結束事件**：主電源恢復、發電機接手，或運算系統完成降載／停機後，儲能退出而不造成新的電壓突變。
5. **回充並重新武裝**：控制器限制回充電流、處理熱與 SOC，確認設備已恢復到可承接下一事件的狀態；只驗第一個脈衝不算完成任務驗證。

這份流程也解釋為什麼「CBU 很快」不能自動推出「不需要 BBU」，以及「BESS 很大」不能推出
「機櫃旁不必緩衝」：接力的每一棒都有自己的反應、位置、能量與控制責任。

## 這篇和 800V 電力轉換文章各回答什麼

800V 電力轉換文章回答「電力經過哪些轉換與保護環節，以及不同功率半導體各放在哪裡」；本文
回答「不同長度的負載波動，該由哪一層儲能處理」。兩者會在高壓直流匯流排相交，但不能把
轉換環節數量與儲能元件數量相乘，也不能把 TI 的參考設計當成所有平台的量產材料清單。

## 研究判定

- **目前可保留的結論**：機櫃旁的電容儲能、機櫃電池備援與設施級電池儲能是三個不同任務層；NVIDIA、OCP 與 TI 的公開文件已足以重建角色邊界。
- **新增的閱讀方法**：先用七欄事件合約固定任務、功率波形、可用能量、交接、回充、損耗與壽命，再比較 CBU／BBU／BESS；這是方法框架，不是新的平台採用證據。
- **可信度為中而不是高**：三份一手來源相互補強，但架構仍在演進，且缺同一量產場域的完整設計與實際運轉資料。
- **目前不能發布的結論**：被動元件用量倍增、指定台灣公司供貨、訂單、收入、毛利、受惠排名，以及市場是否已反映。
- **需要看到什麼才能前進**：同一量產機櫃公布電容儲能與電池備援的客戶資格驗證、現場資料及量產材料清單，或買方和供應商雙向確認量產與財務分母。

## 來源

- [NVIDIA：800 VDC 與 multi-timescale energy storage](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/)
- [OCP：Diablo 400 Rack and Power Specification 0.7.0](https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf)
- [Texas Instruments：800 VDC architecture 與 EDLC CBU reference design](https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html)
- [OCP Open Rack 規格與設計索引](https://www.opencompute.org/wiki/Open_Rack/SpecsAndDesigns)
- [公開資訊觀測站](https://mops.twse.com.tw/mops/web/index)
- [美國能源部：Solar Energy and Storage Basics](https://www.energy.gov/cmei/systems/solar-integration-solar-energy-and-storage-basics)
- [美國能源部：Energy Storage Valuation 方法報告](https://www.energy.gov/sites/default/files/2022-06/MSP_Report_2022June_Final_508_v3.pdf)

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

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C8,C9
metric: 同一 AI production platform 是否以共同 reference plane 公開七欄事件合約及連續事件／回充後的 pass-fail 資料
source_ids: S2,S6,S7
watch_source_ids: S4
frequency: monthly
next_check: 2026-09-01
trigger: OCP、平台商或客戶文件同時固定 trigger、power waveform、usable energy、response／handoff、repetition／recharge、efficiency／thermal、life／safety 並提供 qualification 或 field data
invalidation: 實際平台資料證明本文七欄無法區分設備任務，或單一較簡單指標能在相同可靠度條件下完整預測接力與替代
-->

## 什麼會推翻這篇

- 同一量產架構證明三種儲能任務能由單一設備在相同位置與可靠度條件下完全取代。
- OCP 或 NVIDIA 後續版本移除電容儲能，或實際運轉資料顯示靠近機櫃的短時儲能沒有穩定系統價值。
- 台灣公司若長期只有「AI、800V、儲能」敘事，卻沒有具名產品、客戶資格驗證、部署與財務分母，相關族群就應維持待驗證而不是升格。
