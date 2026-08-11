# 800VDC 不是 SiC 或 GaN 二選一：價值取決於它位在電力鏈哪一段

<!-- research_topic
topic_id: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-07-14
last_reviewed_at: 2026-08-02
review_due: 2026-08-16
source_type: mixed
publisher: Infineon Technologies
publisher_domain: infineon.com
canonical_url: https://www.infineon.com/technology-news/2026/infpss202603-067
source_chain_id: 800v-functional-semiconductor-partition-20260802
stock_ids:
group_ids: power,powersupply
trigger_type: power_architecture_component_partition
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C5
base_confidence: medium
confidence_basis: NVIDIA 的 2027 架構錨點、Infineon 的 GaN IBC 與 SiC BBU 實體 reference design、onsemi 的高壓 SST 路徑及 ROHM 的產品規劃可交叉確認功能分工；但 reference design、planned adoption 與 full-scale deployment 仍未對齊，台灣財務曝險也未建立
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_source_800v_power_tree_scan
evidence: source_chain:800v-functional-semiconductor-partition-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_sic_gan_and_silicon_roles_from_reference_design_and_deployment_stage
evidence: sources:S1,S2,S3,S4,S5
-->

<!-- research_source
source_id: S1
role: company_release
source_kind: document
publisher: NVIDIA
title: NVIDIA 800 VDC Architecture Will Power the Next Generation of AI Factories
published_at: 2025-05-20
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
locator: opening summary、1 MW racks、starting in 2027 與 silicon provider ecosystem 段落
limitation: NVIDIA 架構路線圖與模型目標不證明 2026 已 full-scale 部署、個別元件通過客戶驗收或供應商取得收入
independence_group: nvidia
-->

<!-- research_source
source_id: S2
role: company_release
source_kind: document
publisher: Infineon Technologies
title: CoolGaN-based HV IBC reference designs for 800 VDC architectures
published_at: 2026-03-17
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.infineon.com/technology-news/2026/infpss202603-067
locator: 800V／±400V to 50V 與 12V reference design；650V CoolGaN、40V OptiMOS 與 availability 段落
limitation: Reference design 的效率、功率密度與 demo board 是供應商特定條件結果，不是客戶量產、跨廠比較或財務貢獻
independence_group: infineon
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Infineon Technologies
title: 24 kW SiC-based BBU reference design for high-voltage AI data centers
published_at: 2026-06-02
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.infineon.com/technology-news/2026/infpss202606-093
locator: battery stack to 800V DC bus；650V／1200V SiC；bidirectional buck-boost 與 hot-swap 段落
limitation: 供應商 reference design 與元件 qualification 不等於 hyperscaler 系統驗收、部署量、可靠度實績或收入
independence_group: infineon
-->

<!-- research_source
source_id: S4
role: competitor_primary
source_kind: document
publisher: onsemi
title: The Emerging Way to Conquer Power Challenges in AI Data Centers
published_at: 2026-07-14
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.onsemi.com/company/newsroom/featured-stories/data-center/the-emerging-way-to-conquer-power-challenges-in-ai-data-centers
locator: SST early commercialization；front-end／downstream SiC voltage classes；800V transition beginning later this decade
limitation: 公司技術文章與產品 positioning 不證明特定資料中心已採用 SST、實際效率、量產份額或財務貢獻
independence_group: onsemi
-->

<!-- research_source
source_id: S5
role: competitor_primary
source_kind: document
publisher: Infineon Technologies
title: Infineon power semiconductor portfolio partition for AI data centers
published_at: 2026-06-26
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.infineon.com/de/press-release/2026/infxx202606-117
locator: SiC and GaN: the right technology at every stage；SiC grid-to-rack、GaN intermediate stages、silicon processor level
limitation: 公司新聞稿援引第三方報告並描述自家策略；可支持公司所採功能分工，不能當成全產業唯一最優解或市占證據
independence_group: infineon
-->

<!-- research_source
source_id: S6
role: competitor_primary
source_kind: living_index
publisher: ROHM
title: Special Dialogue: HVDC for AI servers
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.rohm.com/ir/dialogue/ai-server
locator: 800V／±400V coexistence；Q2–Q3 2026 PSU plan；Si 與 SiC MOSFET planned adoption 段落
limitation: 管理層對 planned mass production 與 planned adoption 的敘述不等於截至本輪已出貨、客戶驗收、收入或 full-scale 800V rack deployment
independence_group: rohm
-->

<!-- research_source
source_id: S7
role: company_release
source_kind: living_index
publisher: Infineon Technologies
title: Data center power solutions from grid to core
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.infineon.com/applications/ai-data-center/data-center-power-solutions
locator: 2026-08-02 查得 HVDC、SST、IBC、hot-swap、BBU 與 point-of-load 更新入口
limitation: 產品索引只用來發現新 reference design 與產品階段；不能以頁面存在證明客戶採用
independence_group: infineon
-->

<!-- research_source
source_id: S8
role: competitor_primary
source_kind: living_index
publisher: onsemi
title: onsemi Data Center Solutions
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.onsemi.com/solutions/computing/data-center
locator: 2026-08-02 查得 Si／SiC／GaN、hot-swap、smart fuse 與 800V power tree 更新入口
limitation: 供應商產品頁不能代替量產客戶、實際部署、系統效率或財務揭露
independence_group: onsemi
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: NVIDIA 公開架構仍把支援 1 MW 以上 IT racks 的 800VDC transition 錨定為 starting in 2027
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-08-02
basis: S1 opening summary 與架構段落直接列出 1 MW racks、800VDC 與 2027
boundary: 這不排除 2026 有元件、PSU 或 reference design 先行，也不證明 2027 所有資料中心一次切換
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
claim: Infineon 已公開以 650V GaN 為核心的 800V／±400V 至 50V 或 12V HV IBC reference design，角色是靠近 compute tray 的高頻中間轉換
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-03-17
basis: S2 直接列出 input、output、topology 與 CoolGaN／OptiMOS 元件
boundary: Reference design 不等於 hyperscaler qualification、量產、所有 IBC 都必須使用 GaN，或公司效率數字可與別家直接排名
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
claim: Infineon 的另一份 reference design 使用 650V／1200V SiC，讓 BBU 在電池與 800V DC bus 之間雙向轉換，並把 SiC JFET 用在 ORing／hot-swap
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-06-02
basis: S3 直接列出 24 kW BBU、SiC voltage class、bidirectional stage 與 protection role
boundary: 只支持該設計中的 SiC 功能，不代表已被具名資料中心採用、長期可靠度已驗證或 SiC 獨占所有 800V stages
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C4
label: verified
status: active
claim: onsemi 把 SST 的高壓前端與下游 DC-DC 描述為不同電壓級的 SiC 應用，ROHM 則規劃在特定 AC-DC PSU 同時採用 Si 與 SiC MOSFET
supporting_source_ids: S4,S6
contrary_source_ids:
as_of: 2026-08-02
basis: S4 的 SST voltage-class 段落與 S6 的 planned PSU adoption 段落
boundary: 兩家公司談的是不同產品、拓撲與階段；不能比較效率、成本、份額，ROHM 的 planned adoption 也不是已出貨證據
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: inference
status: active
claim: 800VDC 的功率半導體較合理的研究框架是功能分區而非材料二選一：SiC 偏向高壓、高功率、雙向備援與保護，GaN 偏向高頻高密度中間轉換，Si 仍留在低壓功率、控制與成本敏感環節
supporting_source_ids: S2,S3,S4,S5,S6
contrary_source_ids:
as_of: 2026-08-02
basis: S2／S3 在同一家供應商的不同實體 reference design 顯示 GaN 與 SiC 分工，S4 提供 SST 高壓 SiC 路徑，S5 明示 grid-to-rack／intermediate／processor 分層，S6 顯示 Si 與 SiC 可共存於 PSU
boundary: 這是功能地圖，不是固定 BOM、材料市占、供應商勝負或台灣公司營收預測；實際選材會受 topology、成本、可靠度與客戶規格改變
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: 這些 reference design 已進入 NVIDIA 2027 full-scale rack、材料分工已定案，或 universe 內功率／電源公司已取得可辨識 800V SiC／GaN 訂單與獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有來源分別是架構路線圖、供應商設計、產品規劃與 early commercialization 描述，缺少同一客戶系統的 qualification、BOM、量產與公司財務雙向核對
boundary: 合作名單、reference board、展示規格與 planned adoption 都不能直接畫成台灣公司收入線
verification_needed: 需具名 hyperscaler／platform qualification、production BOM、rack deployment、供應商出貨與收入／毛利揭露，並區分 Si、SiC、GaN 所在 stage
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C2,C3,C4,C5,C6
metric: 各 power stage 的實際 topology、材料、qualification 與 production BOM
source_ids: S2,S3,S4,S5,S6
watch_source_ids: S7,S8
frequency: weekly
frequency_detail: 每週檢查新 reference design、product release 與 qualification；先標 stage 再記材料
next_check: 2026-08-16
trigger: 具名客戶或平台公布同一 800V rack 的 SST、PSU、BBU、hot-swap、IBC 與 POL production BOM
invalidation: 客戶延長 48／54V 過渡、取消某轉換層，或實際 topology 讓 SiC／GaN 的角色與目前分區不同
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C1,C5,C6
metric: 2027 full-scale 800V rack 部署與供應商財務認列
source_ids: S1,S2,S3,S4
watch_source_ids: S7,S8
frequency: monthly
frequency_detail: 每月檢查 platform、hyperscaler 與供應商法說的 qualification、shipment、deployment 與收入
next_check: 2026-09-02
trigger: 平台確認 production rack 與客戶部署，供應商同步揭露具名產品出貨、收入占比或毛利
invalidation: Full-scale 時程延後、只有 demo／sample，或出貨仍集中在 48／54V 過渡產品而非 800V
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
reason: editorial_plain_language_wave80_power_conversion_roles_no_conclusion_change
evidence: editorial:plain_language_wave80_power_conversion_roles
-->

<!-- transition
date: 2026-08-11
from: triaged
to: triaged
reason: editorial_plain_language_wave112_system_table_evidence_steps_no_conclusion_change
evidence: editorial:plain_language_wave112_power_evidence_cards
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **Si／SiC／GaN**：矽、碳化矽與氮化鎵三種功率元件材料；耐壓、切換速度、成本與成熟度各不相同。
- **交流電／直流電（AC／DC）**：交流電會週期性改變方向，直流電則維持固定方向；資料中心會在不同環節轉換兩者與電壓高低。
- **SST**：固態變壓器，用功率電子元件處理中壓 AC 到 DC，可減少傳統轉換層級。
- **IBC**：中間匯流排轉換器，把 800V 高壓 DC 降成 50V、12V 等較低電壓供伺服器板使用。
- **HV（High Voltage）**：高壓。本文用來標示數百伏的輸入或轉換節點，不是特定公司或單一產品名。
- **POL（Point of Load，負載點轉換）**：靠近 CPU、GPU 或其他晶片的最後一段電壓轉換，把較低電壓變成晶片直接使用的電壓。
- **BBU**：電池備援單元，在電網切換、斷電或負載突增時維持運算設備供電。
- **Hot-swap**：設備不停機時安全接入或移除模組，需限制湧入電流並隔離故障。
- **PSU（Power Supply Unit）**：把輸入電力轉成伺服器可用電壓的電源供應器；它只是整條 800V 電力鏈的一個節點。
- **參考設計（reference design）**：供應商公開的可行電路與元件組合，用來示範一種做法；不等於客戶已採用或量產。
- **客戶資格驗證（qualification）**：客戶依自己的規格、可靠度與系統條件測試產品是否可用；通過後仍不等於已大量出貨。
- **量產材料清單（production BOM）**：量產產品實際採用的零件與材料清單；比展示板或規劃更接近真實採購。
- **電路架構（topology）**：元件如何連接、在哪些位置升降壓或提供保護的設計方式。
- **量產（HVM）**：高量產階段，表示製程與供應已進入大量生產；不能只由樣品或參考設計推定。
- **實際部署（deployment）**：設備已進入客戶現場並投入使用；與展示、送樣或測試中的狀態不同。

### 三句話抓重點

- 800V 是一整條電力鏈，不是一顆「800V 晶片」，每個轉換與保護節點需要的材料不同。
- 目前一手設計顯示 SiC、GaN 與 Si 可以同時存在：高壓備援、快速中間轉換與低壓控制各有位置。
- 2026 年已有供應商公開參考設計與產品規劃，但 NVIDIA 仍把整櫃規模的 800V 架構放在 2027；目前還沒有同時對上具名量產客戶與可辨識財務貢獻。

### 為什麼重要

**先找電力在哪裡改變。** 電從電網送到 GPU 的途中，會經過固態變壓器、電源供應器、
電池備援、保護、中間匯流排與負載點轉換。每一段處理的電壓、功率與責任不同，因此不能只問
「SiC 還是 GaN 受惠」。

**再確認那一層是否真的會留在量產系統。** 一張展示板採用某種材料，只能證明這種做法可行；
還要看到客戶驗證、量產材料清單與出貨，才能判斷該轉換層是否存在，以及元件需求落在哪裡。

### 接下來怎麼追

- 對每則新聞先標出它談的是電網端、固態變壓器、電源供應器、電池備援、保護、中間匯流排或負載點轉換，不能只記「800V」。
- 分開記錄參考設計、樣品、客戶資格驗證、量產與實際部署，不用效率宣稱取代客戶階段。
- 台灣公司要等具名料號、客戶驗證、出貨與財務揭露，不能只從材料能力或 NVIDIA 生態系名單推定。

### 想一想

- 如果 800V 架構取消某一層電壓轉換，原本放在那一層的元件需求會轉移到別處，還是直接消失？
- 同一家公司同時賣 Si、SiC 與 GaN，材料市占的變化是否一定等於公司整體毛利改善？

## 從電網到晶片：每一段電力怎麼轉換

| 電力鏈位置 | 目前看到什麼做法 | 證據走到哪一步 |
|---|---|---|
| 中壓交流電（AC）→ 直流電（DC）／固態變壓器（SST） | onsemi 把這一段列為高電壓 SiC 元件的應用位置 | 仍在早期開發與商用階段；尚未看到具名 AI 系統採用並量產的證據 |
| 800V 電池備援（BBU）／保護 | Infineon 公開一套 SiC 參考設計，示範雙向電池備援、保護與不停機更換模組 | 元件與參考設計已公開；尚未看到客戶完成資格驗證的證據 |
| 800V → 50V／12V 中間匯流排（IBC） | Infineon 的參考設計以 GaN 為主，搭配低壓 Si MOSFET、驅動器和控制器 | 目前只是供應商的參考設計與展示板；還不是量產產品的材料清單 |
| 交流轉直流電源供應器（AC-DC PSU） | ROHM 規劃在特定電源供應器中同時使用 Si 與 SiC | 目前只到規劃採用；截至本輪，尚未看到量產出貨證據 |
| 處理器端 | Infineon 的策略說明中，低壓末端仍保留 Si | 這是公司提出的一種功能分工；不代表所有客戶都會採用同一套電路架構 |

同一種材料可能出現在不同位置，同一個位置也可能有不只一種材料或電路架構。這張表只告訴你：
「在哪個環節，公開資料出現了哪種做法。」它不能回答哪種材料一定勝出，也不能把不同公司、
不同測試條件下的效率、功率密度或成本直接排在一起。

## 來源與證據邊界

- [NVIDIA 800VDC architecture](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)（2027 架構錨點）。
- [Infineon GaN HV IBC designs](https://www.infineon.com/technology-news/2026/infpss202603-067)（800V 到 50V／12V）。
- [Infineon SiC HV BBU design](https://www.infineon.com/technology-news/2026/infpss202606-093)（電池到 800V bus 的雙向轉換）。
- [onsemi SST and high-voltage SiC path](https://www.onsemi.com/company/newsroom/featured-stories/data-center/the-emerging-way-to-conquer-power-challenges-in-ai-data-centers)（SST 與高壓 stage）。
- [Infineon grid-to-core material partition](https://www.infineon.com/de/press-release/2026/infxx202606-117)（SiC／GaN／Si 功能定位）。
- [ROHM HVDC dialogue](https://www.rohm.com/ir/dialogue/ai-server)（Si＋SiC planned PSU adoption）。
- [Infineon data-center living index](https://www.infineon.com/applications/ai-data-center/data-center-power-solutions) 與 [onsemi data-center living index](https://www.onsemi.com/solutions/computing/data-center)（後續產品與驗證入口）。

本文刻意不比較不同 reference design 的效率、功率密度或電壓級，因為 topology、輸入輸出、
冷卻與測試條件不同。ROHM 的 Q2–Q3 2026 敘述是 planned PSU adoption；NVIDIA 的 2027 是
full-scale 架構錨點，兩者不是互相矛盾的同一個量產定義。

## 影響路由

<!-- impact
group_id: power
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-02
rationale: SiC／GaN／Si、driver、controller、hot-swap 與 protection 形成多個功率元件搜尋節點
evidence_boundary: 本批一手來源沒有點名 universe 功率公司；技術能力或相同材料不證明客戶 qualification、份額或收入
-->

<!-- impact
group_id: powersupply
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-02
rationale: PSU、power rack、BBU 與 IBC 的 topology 決定元件組合與系統內容量，值得從電源公司法說追蹤
evidence_boundary: 外部 reference design 與 planned adoption 不證明台灣電源廠採用相同 BOM、已量產 800V 或改善毛利
-->

## 下一個可證明／否定的節點

- 平台或 hyperscaler 公布 production-level 800V power tree，清楚列出 SST、PSU、BBU、protection、IBC 與 POL。
- 供應商將 reference design 推進到客戶 qualification、具名量產產品、出貨與現場可靠度。
- 實際 topology 若減少轉換層，重新評估哪一種材料內容量增加、哪一段反而被整合掉。
- 台灣公司只有在具名料號、客戶、量產與財務資料能雙向核對時才建立公司線；否則維持族群 watch。
