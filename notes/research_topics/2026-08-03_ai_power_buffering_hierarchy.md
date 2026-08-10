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

## 新手先讀：這篇在講什麼

### 名詞小字典

- **CBU（Capacitor Bank Unit）**：以電容或超級電容靠近機架吸收很快的功率尖峰與低谷，重點是高功率、快速反應，不是長時間供電。
- **Rack（機架／機櫃）**：集中安裝運算、電源、儲能與冷卻設備的結構單位。「靠近機架」代表需更快回應局部功率波動。
- **DC（Direct Current，直流電）**：電流主要往固定方向流動。機架內的高壓直流匯流排，是 CBU 或 BBU 可能連接的電力節點。
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
- **參考設計（reference design）**：供應商公開的可行電路與元件組合，用來示範一種做法；不等於客戶已採用或量產。
- **量產材料清單（production BOM）**：客戶量產產品實際核准使用的元件與數量清單；進入清單仍不等於已取得固定份額或收入。

### 三句話抓重點

- 先按事件持續時間分層：毫秒至秒的快速尖峰、約 45 至 90 秒的機櫃備援，以及秒至分鐘的設施級負載變化，不能只因都叫儲能就合併計算。
- 機櫃旁的電容儲能模組（CBU）重視反應速度，機櫃電池備援單元（BBU）負責短暫供電不中斷與受控停機，設施級電池儲能系統（BESS）則協調整體負載與發電機切換；時間可能重疊，但位置與任務仍不同。
- NVIDIA、OCP 與 TI 的公開資料足以建立這三種角色，還不能證明台灣被動元件、電源供應或功率元件公司已進入量產材料清單、取得訂單或認列收入。

### 為什麼重要

**先看事件持續多久。** 毫秒至秒的功率尖峰，需要靠近機櫃的設備快速反應；數十秒的供電
空檔，需要電池讓設備撐過切換或完成受控停機；秒至分鐘的整體負載變化，則由設施級儲能協調。

**再看設備離誰最近。** 電容儲能模組與電池備援多半靠近機櫃或高壓直流匯流排，設施級儲能
則位在資料中心設施或公用電網接點。距離不同，反應速度、配電延遲、維修與安全條件也不同。

**最後才談公司與元件需求。** 架構需要某一層儲能，不代表任何零件供應商已經取得訂單；要先
確認具名產品、客戶資格驗證、現場部署與量產材料清單，才能把系統角色翻譯成數量與財務貢獻。

### 接下來怎麼追

- 追 OCP Open Rack／Diablo 是否把電容儲能、電池備援、高壓直流匯流排、保護與連接器寫成正式規格，並完成互通測試。
- 追 NVIDIA 或平台客戶是否公布同一量產機櫃中，三種儲能設備的位置、額定任務、客戶資格驗證與現場部署資料。
- 追台灣被動元件、電源供應與功率元件公司是否以具名產品、客戶驗收、量產數量及可辨識財務貢獻完成雙向核對。

### 想一想

- 機櫃旁的電容儲能模組只能處理毫秒到秒的尖峰，為什麼不能取代能支撐數十秒的電池備援單元？
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

## 這篇和 800V 電力轉換文章各回答什麼

800V 電力轉換文章回答「電力經過哪些轉換與保護環節，以及不同功率半導體各放在哪裡」；本文
回答「不同長度的負載波動，該由哪一層儲能處理」。兩者會在高壓直流匯流排相交，但不能把
轉換環節數量與儲能元件數量相乘，也不能把 TI 的參考設計當成所有平台的量產材料清單。

## 研究判定

- **目前可保留的結論**：機櫃旁的電容儲能、機櫃電池備援與設施級電池儲能是三個不同任務層；NVIDIA、OCP 與 TI 的公開文件已足以重建角色邊界。
- **可信度為中而不是高**：三份一手來源相互補強，但架構仍在演進，且缺同一量產場域的完整設計與實際運轉資料。
- **目前不能發布的結論**：被動元件用量倍增、指定台灣公司供貨、訂單、收入、毛利、受惠排名，以及市場是否已反映。
- **需要看到什麼才能前進**：同一量產機櫃公布電容儲能與電池備援的客戶資格驗證、現場資料及量產材料清單，或買方和供應商雙向確認量產與財務分母。

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

- 同一量產架構證明三種儲能任務能由單一設備在相同位置與可靠度條件下完全取代。
- OCP 或 NVIDIA 後續版本移除電容儲能，或實際運轉資料顯示靠近機櫃的短時儲能沒有穩定系統價值。
- 台灣公司若長期只有「AI、800V、儲能」敘事，卻沒有具名產品、客戶資格驗證、部署與財務分母，相關族群就應維持待驗證而不是升格。
