# 800VDC 不是 SiC 或 GaN 二選一：先看拓撲，再用六把尺選元件

<!-- research_topic
topic_id: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-07-14
last_reviewed_at: 2026-08-12
review_due: 2026-08-19
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
thesis_claim_id: C7
base_confidence: medium
confidence_basis: NVIDIA 的分階段架構、TI 與 ST 兩條獨立直降 reference architecture、OCP 現行 48V power shelf contract，以及 Infineon／onsemi／ROHM 的元件設計可交叉確認「拓撲先決定 stage、選材再發生於 stage 內」；但公開鏈仍未接到同一客戶的 qualification、production BOM、field reliability 或財務分母
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

<!-- research_source
source_id: S9
role: competitor_primary
source_kind: document
publisher: Texas Instruments
title: TI unveils complete 800-VDC power architecture for future-generation AI data centers with NVIDIA
published_at: 2026-03-16
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html
locator: 800V→6V isolated bus converter、6V→sub-1V multiphase、800V→12V、hot-swap、CBU 與 30kW AC-DC reference architecture 段落
limitation: TI 公開的是供應商 reference architecture 與元件組合；不證明 NVIDIA production rack 已固定此 topology、客戶 qualification、跨廠比較、出貨或收入
independence_group: texas-instruments
-->

<!-- research_source
source_id: S10
role: competitor_primary
source_kind: document
publisher: STMicroelectronics
title: STMicroelectronics unveils power architectures for 800VDC AI data centers
published_at: 2026-03-17
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://newsroom.st.com/media-center/press-item.html/t4766.html
locator: 800V→50V GaN LLC prototype、800V→12V 與 800V→6V architectures，以及 Si／SiC／GaN／controller 組合段落
limitation: ST 的 prototype 與 architecture 只支持可行轉換路徑及公司所採元件角色；不等於具名客戶 qualification、量產 BOM、可靠度或財務貢獻
independence_group: stmicroelectronics
-->

<!-- research_source
source_id: S11
role: company_release
source_kind: living_index
publisher: NVIDIA
title: 800 VDC Architecture for Next-Generation AI Factories
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.nvidia.com/en-au/data-center/technologies/800-vdc-architecture/
locator: 2026-08-12 活頁的 gradual evolution、support existing data centers、path to all-800V future 與 fewer conversion stages；並逐頁核對頁面所連官方 whitepaper 的 phased strategy、transitional side power rack、facility rectifier、direct conversion 及 certification 邊界
limitation: NVIDIA 的活頁與 whitepaper 是資訊性架構路徑，不是 rigid production specification、採購承諾、共同 pass report 或已部署場站清冊；文件亦明示客戶仍須自行測試
independence_group: nvidia
-->

<!-- research_source
source_id: S12
role: standard
source_kind: document
publisher: Open Compute Project
title: Open Rack V3 HPR V2 72kW Power Shelf Specification Version 1.0.0
published_at: 2026-06-12
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/open-rack-v3-hpr-v2-72kw-power-shelf-spec-v1-0-0-pdf
locator: PDF pp.6–11；72kW shelf、6×12kW PSU、60kW N+1、48V narrow-range architecture、PSU／BBU transition、peak-load 與 busbar temperature requirements
limitation: OCP specification 固定一套 48V power-shelf contract 與要求，不證明所有會員已部署、800V transition 延後、特定供應商通過 qualification 或取得收入
independence_group: open-compute-project
-->

<!-- research_source
source_id: S13
role: standard
source_kind: document
publisher: Open Compute Project
title: Diablo 400 Project Rack and Power Specification 0.7.0
published_at: 2026-03-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf
locator: PDF pp.10、14–18、31–32；800kW–1MW+ disaggregated power rack；+400V-to-COM 與 -400V-to-COM 的±400VDC output；±400V／800V busbar；50kW／63A、100kW／125A、400kW／500A、800kW／1000A cable options；average 與 RMS current thermal boundary
limitation: Diablo 400 是多家參與的 0.7.0 system specification，不指定唯一 topology、實作導體尺寸、完整效率與損耗分解、共同 qualification、客戶場站、production BOM、供應商或財務效果；文件中線纜 kW／A 是規格選項而不是本文 72kW 條件式算例的實測
independence_group: open-compute-project
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

<!-- research_claim
claim_id: C7
label: inference
status: active
claim: 800VDC 的元件研究應採兩層契約：系統 topology 先決定哪些轉換、隔離、備援與保護 stage 仍存在；在每個保留 stage 內，再依工作電壓／電流、切換頻率與 topology、隔離安全、瞬態保護、熱與封裝，以及 qualification／供應六軸選擇 Si、SiC、GaN 與控制元件
supporting_source_ids: S2,S3,S4,S5,S9,S10,S11,S12
contrary_source_ids:
as_of: 2026-08-12
basis: S9／S10 兩家獨立供應商各自公開 800V→6V／12V／50V 路徑，顯示中間 stage 可被移動或整合；S11 明示既有、過渡與 all-800V 架構會並存且轉換級數不同；S12 固定一套現行 48V power-shelf contract；S2–S5 再顯示同一 power tree 內不同 stage 可採不同材料
boundary: 兩層契約是整理設計變數與證據的研究框架，不是唯一最佳 topology、固定 material share、device count、供應商排名、客戶 production BOM 或財務預測；六軸也必須在相同輸入輸出與測試條件下才可比較
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
claim: TI 已公開一條 800V→6V isolated bus converter 再由 6V 降至 sub-1V 的 reference architecture，並另列 800V→12V、hot-swap、CBU 與 AC-DC building blocks
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-03-16
basis: S9 直接列出兩段 voltage path 與相鄰 reference designs／power stages
boundary: 只支持 TI 所公開的架構與 building blocks；不代表 NVIDIA 已選定此 production topology、所有中間級都會消失、客戶通過或量產出貨
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
claim: ST 已公開 800V→50V GaN LLC prototype，並提出 800V→12V 與 800V→6V architectures；同一套供電敘事仍同時包含 Si、SiC、GaN、analog 與 controller 角色
supporting_source_ids: S10
contrary_source_ids:
as_of: 2026-03-17
basis: S10 直接列出三種 output-voltage 路徑、prototype 狀態與不同半導體角色
boundary: Prototype／architecture 不等於具名客戶採用、共同 efficiency benchmark、production BOM、可靠度或營收；材料組合仍依各條 topology 改變
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: OCP 的 Open Rack V3 HPR V2 規格仍固定一套 72kW、6×12kW PSU、60kW N+1 的 48V narrow-range power shelf，並把 PSU／BBU transition、peak load 與 busbar temperature sensing 列為系統要求
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-06-12
basis: S12 pp.6–11 的 architecture、power budget、transition、peak-load 與 temperature requirements
boundary: 這證明現行 48V contract 仍具體存在，不證明所有平台採同一規格、800V 不會導入、任何產品已通過 OCP qualification 或特定公司取得訂單
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: unverified
status: active
claim: 任一公開的 800V device 或 reference architecture 已沿同一版本鏈完成 converter 原始測試、rack／site safety 與 fault qualification、多來源客戶驗收、production BOM、field deployment，並形成可雙向核對的供應商收入與毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S9／S10 只到供應商 architecture／prototype，S11 是資訊性 platform path，S12 是 48V specification；本輪沒有同一產品版本跨過全部工程、客戶、部署與財務節點
boundary: 生態系名單、datasheet、reference board、單點效率、規格發布、planned deployment 或事業群營收均不能單獨補齊這條鏈
verification_needed: 需固定同一 input／output／topology／cooling／revision，取得 device data、converter raw test、rack／site pass-fail、客戶 acceptance、production BOM、deployed denominator，以及買賣雙方同期間 shipment／revenue／cost／margin
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: OCP HPR V2 1.0.0 雖將系統命名為 Narrow Range 48V Architecture，但規格寫明 PSU output 是 50V adjustable；72kW capacity 的 shelf 以 60kW N+1 運作，並因 high-current output 採 bolted connection、引用 2000A DC output connector 且監測 busbar 溫度
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-06-12
basis: S12 pp.6–8、11、16 直接列出 capacity、N+1 output、50V setpoint、bolted high-current output、2000A connector 與溫度感測
boundary: `48V` 是架構名稱，不應自行把規格內 50V setpoint 改回 48.0V 重算；72kW capacity、60kW N+1 與 2000A connector rating 也是不同欄位，不代表實測電流、所有負載同時滿載、共同部署或供應商收入
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: verified
status: active
claim: OCP Diablo 400 0.7.0 將每極寫成 +400V-to-COM 與 -400V-to-COM，兩極間為 800V differential；其線纜選項列 50kW／63A、100kW／125A、400kW／500A 與 800kW／1000A，並要求線徑依應用的 average power 或 RMS current 決定
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-03-01
basis: S13 pp.14、18、31 直接定義±400VDC 端點、±400V／800V busbar、3-wire output 及各組 kW／A cable options，Appendix B 另分 average 與 RMS current 的熱影響
boundary: 電流值必須隨負載實際跨接 +400V、COM、-400V 的方式、正負極平衡、波形、降額與備援重算；規格線纜 rating 不是現場實測、銅用量、損耗、效率或安全驗收結果
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: inference
status: active
claim: 若只作量綱教材，固定同一 72kW 穩態負載並假設無轉換或配電損失，則從 HPR 規格內 50V 端點供電的條件式電流為 1440A，改以 +400V-to-(−400V) 的 800V differential 供電則為 90A，前者為後者 16 倍
supporting_source_ids: S12,S13
contrary_source_ids:
as_of: 2026-08-14
basis: 以 P=V×I 重算：72000／50=1440A，72000／800=90A，1440／90=16；Python Decimal 與 awk 兩條獨立算術路徑完全一致；S13 另列 100kW／125A 與 50kW／63A，可核對 full-differential 800V 下 100000／800=125A、50000／800=62.5A 的量綱關係
boundary: 這是 N=1 個人為固定的反事實工作點，沒有 sampling SE／t；不是 HPR 與 Diablo 的實驗比較、實際 output current、相同產品、相同 topology 或量產系統。若負載只跨單極 400V-to-COM，同一 72kW 條件式電流會是 180A，因此不寫清 reference plane 就不能除以 400 或 800
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C15
label: inference
status: active
claim: 將 C14 再加上「相同導體電阻 R」的反事實假設時，I²R 導體損耗比為 (90／1440)²=1／256=0.390625%；這不是真實系統降低 99.609375% 的證據，實際總效益必須重新固定 RMS 電流與波形、導體材料／長度／截面積與接點、轉換級效率、絕緣與電弧間距、保護斷開、散熱、備援與故障包絡線
supporting_source_ids: S1,S12,S13
contrary_source_ids:
as_of: 2026-08-14
basis: S13 Appendix B 明示導體熱影響要用 RMS current，並寫明 wire gauge 隨 average power 或 RMS current 及應用決定；S12 又以高電流螺栓連接、2000A connector 與溫度感測展示低壓電流的實體代價，S1 同時把 800V 轉換級、過流保護與 serviceability 列為系統問題；Python Decimal 與 awk 均得 0.00390625 比值
boundary: 1／256 只是 fixed-R sensitivity，沒有實驗樣本、sampling SE／t 或現場不確定度；升壓後若縮小導體截面、增加線路長度／接點或改變 topology，R 就不再相同。配電 I²R、converter loss、銅用量、系統效率、TCO 與供應商財務是不同指標，不得用單一算式互相代填
verification_needed: 需具名 production topology 與版本，在相同 delivered-load profile 下公開全電力路徑的 voltage／RMS-current waveforms、導體幾何與溫升、各 conversion stage input／output、冷卻與輔助負載、fault／redundancy state、原始數據、量測不確定度、pass-fail 與客戶驗收
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: retired
retired_at: 2026-08-12
retirement_reason: C5 的材料功能分區已被 C7 的 topology-first／six-axis 兩層契約擴展；舊 stage 與 production BOM 問題由 T3 以更新後來源與 claim 集合接續
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
status: retired
retired_at: 2026-08-12
retirement_reason: 2027 deployment 與財務問題需先分開 converter、rack／site、customer BOM 與 financial attribution；原 trigger 由 T4 依 C7／C11 的固定版本鏈接續
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

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C2,C3,C5,C7,C8,C9,C10,C11
metric: 具名 800V topology 中保留／移除的轉換與保護 stage，以及每個 stage 的六軸選材條件
source_ids: S2,S3,S4,S5,S9,S10,S11,S12
watch_source_ids: S7,S8,S11
frequency: weekly
frequency_detail: 每週先畫 input-to-output power path，再逐級記錄 voltage／current、switching／topology、isolation、transient、thermal／package 與 qualification；不只搜尋材料名
next_check: 2026-08-19
trigger: 平台或客戶固定 production topology 與 revision，公開各 stage 的 input／output、protection／thermal boundary、具名 device 及 converter pass-fail
invalidation: Production architecture 保留／取消的 stage、電壓路徑或材料角色與 C7 框架不相容，或相同條件下資料支持另一種 topology／material partition
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C1,C6,C7,C11
metric: 同一版本由 reference architecture 到 converter、rack／site、customer、production BOM 與財務的交接證據
source_ids: S1,S9,S10,S11,S12
watch_source_ids: S7,S8,S11
frequency: monthly
frequency_detail: 每月分開檢查原始測試、qualification／acceptance、deployment denominator、shipment，以及同產品收入／成本／毛利；缺任一層就停在上一層
next_check: 2026-09-12
trigger: 買方與供應商雙向固定同一 platform／product／revision／period，公開 pass-fail、production BOM、deployed volume 與財務分母
invalidation: Full-scale 時程或 topology 改變、只有 demo／sample／MOU，或出貨與財務仍無法對上同一 800V product／site
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

<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: expanded_functional_partition_to_topology_first_six_axis_and_five_gate_contract
evidence: sources:S9,S10,S11,S12
-->

<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_voltage_current_reference_plane_and_fixed_resistance_sensitivity_without_thesis_clock_refresh
evidence: sources:S1,S12,S13
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
- **Power stage（功率級）**：完成一次升壓、降壓、整流、隔離或保護任務的一段電路。若拓撲取消這一級，原本放在這裡的元件需求可能一起消失。
- **隔離（isolation）**：讓輸入與輸出沒有直接導電路徑，限制故障與觸電風險；隔離元件、爬電距離和安全驗證會占用空間與成本。
- **軟切換（soft switching）**：讓功率開關在電壓或電流接近零時切換，以降低切換損耗；能否做到取決於拓撲與工作範圍，不是材料名稱自動保證。
- **EMI（電磁干擾）**：快速切換產生的雜訊可能干擾其他電路或超過法規限制；效率高不代表 EMI、瞬態與可靠度也已過關。
- **HPR V2**：OCP 第二版高功率機架電力架規格；本文只用它說明一套現行 48V contract，不把它當成所有機架的共同設計。
- **Sub-1V**：低於 1 伏特的晶片核心供電；即使高壓匯流排改成 800V，靠近處理器的最後降壓仍然需要完成。
- **AC-DC**：把交流電轉成直流電的整流與轉換級；它可放在 rack、side power rack 或設施端。
- **All-800V**：NVIDIA 所述由設施到 IT 配電更全面採用 800VDC 的未來路徑，不代表今天所有設備都已切換。
- **LLC**：利用電感與電容共振達成軟切換的一類 DC-DC topology；效率與可用範圍仍取決於實際設計條件。
- **Reference plane（參考平面）**：數值所屬的量測端點與系統邊界。電壓必須寫明是哪兩個端點之間，功率與效率也必須寫明包含哪些轉換、線路與輔助負載。
- **Differential voltage（差動電壓）**：兩條帶電導體之間的電壓差。Diablo 的 +400V 與 -400V 相對 COM 各為 400V，但正負端之間是 800V。
- **COM／return（共同點／回流端）**：電路用來定義電壓與回流路徑的端點；它和機殼或保護接地的關係必須依具體 grounding topology 確認。
- **RMS current（均方根電流）**：用來反映電流波形造成熱效應的等效值。負載快速變動時，只看平均電流可能低估導體與接點溫升。
- **`P = V × I`**：在本文條件式 DC 教材中，功率等於電壓乘電流。公式本身不會告訴你實際電壓端點、波形、效率、備援或安全邊界。
- **`I²R` 導體損耗**：電流通過電阻後轉成熱的功率關係。只有在電阻、電流定義與時間邊界一致時，才能用電流平方比較。
- **Derating（降額）**：為溫度、海拔、壽命、安全或故障留餘裕，將元件或線纜可用上限設得低於型錄額定值。
- **Python Decimal／awk**：本文用兩個彼此獨立的算術工具重算同一公式，降低抄寫與顯示錯誤；兩路一致不會補上工程條件或實驗證據。
- **Fixed-R sensitivity**：刻意假設兩種系統的導體電阻 R 不變，只看電流改變會如何影響 `I²R`；這是敏感度，不是實測節能。
- **Sampling SE／t**：SE 是抽樣標準誤，t 常用來表示估計與零相對於標準誤的距離；確定性單一算例沒有抽樣分布，因此兩者不適用。
- **to-COM**：電壓是從某一帶電端量到共同點 COM；`+400V-to-COM` 與 `-400V-to-COM` 各是 400V，不是正負端間的 800V。

### 三句話抓重點

- 「800V」只告訴你高壓匯流排的一個電壓，沒有告訴你電力中途會停在 50V、12V、6V，還是少掉某一層轉換。
- 正確順序是先畫 topology、確認哪些 power stage 存在，再用六把尺比較同一 stage 裡的 Si、SiC、GaN 與控制元件；材料名不能反過來決定整套系統。
- 2026 年已能看到 TI、ST、Infineon 等供應商的多條 reference architecture，但尚未有同一版本一路接到 rack／site qualification、production BOM、部署分母與財務歸因。

### 為什麼重要

**先找電力在哪裡改變。** 可以把供電想成一條有多個轉乘站的路線：800V 是幹線電壓，
50V、12V、6V 與晶片核心電壓是可能的轉乘站。拓撲若把一個轉乘站取消，原本放在那裡的
開關、磁性元件、控制器、連接器與散熱需求不一定「轉移」，也可能直接消失。

**再確認那一層是否真的會留在量產系統。** 一張展示板採用某種材料，只能證明這種做法可行；
還要看到客戶驗證、量產材料清單與出貨，才能判斷該轉換層是否存在，以及元件需求落在哪裡。

### 接下來怎麼追

- 先寫完整的「輸入電壓 → 中間電壓 → 輸出電壓」，再標出整流、隔離、備援、hot-swap 與 POL；不能只記「800V」。
- 比較兩個設計前，先對齊輸入輸出、功率、負載範圍、冷卻、開關頻率、隔離與測試方法；不同 reference plane 的效率不能直接排名。
- 分開記錄元件資料、converter 測試、rack／site qualification、客戶 acceptance、production BOM 與財務，不能用前一關代替後一關。

### 想一想

- 如果 800V 架構取消某一層電壓轉換，原本放在那一層的元件需求會轉移到別處，還是直接消失？
- 同一家公司同時賣 Si、SiC 與 GaN，材料市占的變化是否一定等於公司整體毛利改善？

## 先用四個位置看：拓撲會把元件工作移到哪裡

| 本文四個位置 | 電力怎麼走 | 哪些工作被保留、移動或整合 | 本輪一手證據 | 不能直接推成 |
|---|---|---|---|---|
| 1. 現行機架入口 | 設施交流電進入 rack PSU，再送到 48V／54V 匯流排 | 整流與主要降壓仍在機架 power shelf，板端再繼續降壓 | OCP HPR V2 固定 48V、6×12kW PSU 與 60kW N+1 contract | 所有 AI rack 都採同一規格，或 48V 永遠不會被替換 |
| 2. 過渡 side power rack | 既有設施交流架構先保留，由側邊電力櫃整流成 800V 再送入 compute rack | 高壓整流移到 sidecar；rack 內低壓轉換、保護與備援仍要重新分工 | NVIDIA whitepaper 把它列為過渡路徑 | 已是 rigid production spec、客戶場站已部署或 2027 時程保證 |
| 3. 設施級 800V 匯流排 | 設施端集中整流，長距離以 800VDC 配電至機架 | 部分 AC-DC stage 移出 rack，銅線與配電介面改變；但隔離、fault protection、BBU 與 rack conversion 仍存在 | NVIDIA 公開 gradual evolution 與 facility-level rectifier 路徑 | SST 必然取代所有傳統設備，或任何一家供應商已取得份額 |
| 4. 靠近運算的直降 | 800V 可先到 50V，也可直接到 12V／6V，再降到晶片 sub-1V | 50V 或其他 intermediate stage 可能保留、縮小或被整合；最後 POL 不會因 800V 標籤自動消失 | Infineon 有 50V／12V IBC；TI 與 ST 分別公開 6V／12V／50V 路徑 | 某一路徑已被 NVIDIA 客戶定案、材料內容量或 device count 已知 |

這四個位置不是四個互斥產品，而是「電力責任可能放在哪裡」的閱讀地圖。先畫出實際路徑，
才能知道要研究幾個 power stage；只看「800V adoption」無法算出需要幾顆 SiC 或 GaN。

## 為什麼 48V 與 800V 會共存一段時間

OCP 在 2026 年 6 月發布的 HPR V2 規格，仍把 72kW power shelf 寫成六顆 12kW PSU，
並以 60kW N+1 運作；它還要求處理 PSU／BBU 切換、尖峰負載與匯流排溫度。這是一份很具體的
48V 系統契約。另一邊，NVIDIA 把 800V 描述成由現有資料中心逐步走向 all-800V 的路徑，
而不是一夜切換。

兩者並不矛盾：規格告訴你「現行系統今天必須怎麼交付」，路線圖告訴你「未來責任可能怎麼搬」。
因此研究時要同時追兩個母體：新建 800V 架構走到哪一關，以及 48V／54V 過渡產品還有多少實際
部署。只追其中一邊，容易把未來設計誤當今天 BOM，或把今天規格誤當永遠不變。

## 48V 不一定是 48.0V，±400V 也不能只除以 400

先別急著套 `P = V × I`。第一個問題應該是：**V 是哪兩個端點之間的電壓？**
OCP HPR V2 把架構叫做 `Narrow Range 48V`，但規格內 PSU output setpoint 寫的是
`50V adjustable`。Diablo 400 則把端點寫成 +400V、COM 與 -400V：單極對 COM 是
400V，正負兩極之間才是 800V。只看架構名稱就把除數寫成 48、400 或 800，
可能在第一行就差一倍。

| 文件欄位 | 端點／運作條件 | 可做的量綱核對 | 不能當成 |
|---|---|---|---|
| HPR V2 72kW capacity | PSU output 對 50V return；規格以 60kW N+1 運作 | `72,000／50 = 1,440A`；N+1 output 為 `60,000／50 = 1,200A` | 1,440A 已在某櫃實測，或 2,000A connector 平時就流 2,000A |
| Diablo 全差動路徑 | +400V 到 -400V，跨 800V | 文件的 `100kW／125A` 符合 `100,000／800=125A`；`50kW／63A` 對應算式 62.5A 與線纜額定整數 | 所有負載都跨全差動、正負極完全平衡，或 rating 是實測平均值 |
| Diablo 單極路徑 | +400V-to-COM 或 COM-to-(−400V)，跨 400V | 同一 72kW 若真的全由單極承擔，條件式電流是 `72,000／400=180A` | 把 180A 與全差動的 90A 互換，或忽略 midpoint grounding 與負載分配 |

### 同一個 72kW 教材為何從 1,440A 變 90A

現在才做一個刻意簡化的條件式比較：固定同一 72kW 穩態 delivered load，先忽略
轉換與配電損失，再把一邊定義為 50V-to-return，另一邊定義為 +400V-to-(−400V)
的 800V differential。這時 `I = P／V`：

1. 50V 路徑：`72,000W ÷ 50V = 1,440A`。
2. 800V 路徑：`72,000W ÷ 800V = 90A`。
3. 電流比：`1,440 ÷ 90 = 16`；在這個教材條件下，高壓路徑的電流是低壓路徑的 `1／16`。

Python Decimal 與 awk 兩條獨立算術路徑完全一致。這不是實驗樣本，而是 N=1 個人為工作點；
沒有 sampling SE 或 t 值。S12 與 S13 也不是同一產品的 A／B test：本文只用兩份規格提供
低壓與高壓的實體端點定義，不把 90A 寫成 Diablo 公布的 72kW 測量。

### `1／256` 是 fixed-R 敏感度，不是系統節電成績

導體的發熱關係常寫成 `P_loss = I_rms² × R`。若在上述人為工作點之外，再加上一個
現實中不會自動成立的假設——兩邊導體電阻 R 完全一樣——那麼損耗比是：

`(90／1,440)² = (1／16)² = 1／256 = 0.390625%`。

反過來寫是 99.609375% 下降，但這只是 **fixed-R sensitivity**，不是任何具名資料中心、
rack 或 power shelf 的節電測量。升壓後設計者可能縮小導體截面，R 會上升；線路長度、
接點數、降額、備援與 RMS 電流波形也會改變溫升。更重要的是，少掉或新增的
AC-DC／DC-DC stage、風扇與控制電力屬於 converter 與 end-to-end loss，不是同一個 `I²R`
分子。

因此，真正可比的「電壓—電流—損耗護照」至少要固定：**源端與負載端 reference plane、
voltage endpoints、delivered-load waveform、average／RMS／peak current、導體材料與幾何、接點與溫升、
每一轉換級的 input／output、輔助負載與冷卻、備援／fault state、絕緣／電弧／斷開邊界、
原始數據、量測不確定度與 pass-fail**。沒有這些欄位，可以教電學，不能排效率或算銅用量。

### 多空小作文：升壓是價值搬家，不是所有元件一起增加

**偏多路徑**是：同功率下的電流大幅下降，可解開低壓母排、接頭、配電空間與溫升的物理限制；
同時，高壓轉換、SiC／GaN、斷路與 hot-swap、絕緣材料、高壓連接器、感測與安全驗證可能獲得更高的
系統責任與價值。只有這些節點出現具名資格、量產 BOM、出貨及收入／毛利時，才能從工程路線進到個股。

**偏空路徑**是：高壓配電可能減少 rack-level AC-DC PSU、低壓 power shelf、粗銅母排與某些中間轉換級；
新增的高壓內容也可能被整合到少數模組，或被絕緣、電弧、保護、commissioning 與 field service 成本抵銷。
若最終 topology 取消某一 stage，那一層的元件需求可能不是轉移，而是直接消失。多空兩邊都要用同一份
production power tree、同一負載與故障波形、同一 BOM 及同期財務分母裁決，不能把 16 倍電流比直接畫成銅箔、被動元件或功率元件的營收線。

## 再用六把尺：同一個 power stage 也不能只看材料

| 本文六把尺 | 先問什麼 | 為何會改變 Si／SiC／GaN 的角色 | 比較時必須固定 | 不能直接推成 |
|---|---|---|---|---|
| 1. 工作電壓與電流 | 正常、尖峰與故障時各承受多少電壓／電流？需要多少安全餘裕？ | 高耐壓與高功率可能增加 SiC 的可行性；較低電壓仍可能由成熟 Si 處理 | input／output、功率、derating、fault envelope | 耐壓較高就一定效率、成本或可靠度最好 |
| 2. 切換頻率與 topology | 是硬切換、LLC 等軟切換，還是雙向 buck-boost？全負載範圍都能維持嗎？ | 高頻可縮小磁性元件並提高 GaN 吸引力；但 switching condition 改變後損耗排序也會改 | topology、frequency、load range、control mode | 單一峰值效率可跨 topology 排名 |
| 3. 隔離與安全 | 哪裡需要 galvanic isolation、爬電距離、維修斷電與人員保護？ | 隔離會加入變壓器、driver、sensor 與安全間距，影響密度與封裝 | insulation class、voltage band、標準與 service boundary | 功率開關可用就等於整機安全合格 |
| 4. 瞬態與保護 | 如何處理 inrush、short circuit、load step、ORing、hot-swap 與 BBU 切換？ | 開關的安全工作區、偵測速度與控制責任可能比穩態效率更重要 | transient waveform、duration、fault energy、pass／fail | datasheet 額定值等於 rack fault 已驗證 |
| 5. 熱、封裝與整合 | 熱從 junction 經封裝、PCB／busbar 到冷卻系統怎麼走？driver 與 sensor 是否整合？ | 高頻與高密度會把損耗、寄生參數與散熱問題綁在一起，材料優勢可能被封裝限制吃掉 | ambient／coolant、thermal path、package、layout | 晶片效率提升會等比例變成 rack 節能 |
| 6. Qualification 與供應 | 誰測、依哪個版本、樣本多少、有哪些替代來源、客戶是否接受？ | 工程可行的材料若無可靠度資料、產能、second source 或客戶 pass，仍不能進 production BOM | revision、test matrix、sample／hours、change control、source count | 生態系列名、reference board 或 planned adoption 等於訂單 |

六把尺的重點不是替材料打總分，而是防止跨條件比較。只有當兩個方案處理相同的輸入、輸出、
功率、負載範圍、冷卻與安全責任時，效率、功率密度、成本與可靠度才有可比性。

## 把公開設計放回正確的 power stage

| 公開來源 | 它實際展示什麼 | 可支持的材料／元件角色 | 證據停在哪裡 |
|---|---|---|---|
| TI | 800V→6V isolated bus，再由 6V→sub-1V；另有 800V→12V、hot-swap 與 CBU building blocks | GaN power stage、低壓 multiphase、控制與保護需共同工作 | Reference architecture；未固定 NVIDIA production topology |
| ST | 800V→50V GaN LLC prototype，以及 800V→12V／6V architectures | Si、SiC、GaN、analog 與 controller 在不同位置共存 | Prototype／architecture；未到具名客戶 qualification |
| Infineon | GaN 800V／±400V→50V／12V IBC；SiC 800V BBU 與 hot-swap design | GaN 偏高頻 IBC，SiC 偏高壓雙向備援／保護，低壓 Si 仍存在 | 兩套 reference design；不是同一 production rack 的完整 BOM |
| onsemi／ROHM | SST 不同電壓級的 SiC 路徑；特定 PSU 規劃同時採 Si 與 SiC | 高壓前端與成本／控制敏感位置可採不同材料 | 技術文章與 planned adoption；未到客戶部署與財務 |

這些資料共同反駁「800V 只會有一種材料」的簡化說法，但仍不能回答哪一家會拿到多少份額。
供應商可以同時賣多種材料；topology 改變也可能讓某個 stage 的元件數量下降，即使整體 800V
部署上升。

## 最後用五關：不要用元件資料替整套系統背書

| 本文五關 | 這一關要交付什麼 | 本輪可確認到哪裡 | 下一份關鍵證據 | 不能跳成 |
|---|---|---|---|---|
| 1. Topology contract | 固定 input／output、保留的 stage、隔離／保護／備援責任與版本 | NVIDIA 提供分階段路徑，TI／ST／Infineon 提供多種可行轉換鏈 | 平台或客戶的 production schematic／interface specification | Reference architecture 就是最終 BOM |
| 2. Device characterization | 在指定電壓、電流、溫度與 switching condition 下的損耗、SOA、短路與可靠度資料 | 供應商列出具名材料與元件系列，但本篇未取得同版完整 qualification pack | Datasheet、原始波形、sample／duration、失效與變更紀錄 | 元件額定值等於 converter 已通過 |
| 3. Converter validation | 固定 topology、控制、layout、磁性元件、冷卻後測效率曲線、EMI、transient、thermal 與 fault | 已有 prototype／reference design | 同版硬體全負載 raw data、pass／fail、第三方或客戶重測 | 峰值效率等於 rack 節能或可靠度 |
| 4. Rack／site／customer qualification | 把 power rack、BBU、busbar、protection、cooling 與負載放在一起驗收，包含 fault injection 與 serviceability | OCP 48V 規格提供要求；800V 尚無本輪可定位的同一產品 pass chain | 具名 rack／site、as-built revision、客戶 acceptance 與 operating hours | 規格發布或 partner list 等於部署 |
| 5. Production BOM／財務 | 買方與供應商對上同一產品、期間、出貨量、收入、成本、毛利與現金 | 尚未取得 | Production BOM、shipment、deployed denominator 與同產品財務分子 | 題材能力、MOU 或事業群營收等於 800V 受惠 |

這五關回答不同問題。元件測試是在問「這顆開關在指定條件下能否工作」；converter 測試是在問
「整段電路是否可重現」；rack／site 驗收是在問「故障、維修與長時間運行時整套系統是否可用」；
最後一關才有資格討論公司財務。任何前一關都不能替後一關簽名。

## 來源與證據邊界

- [NVIDIA 800VDC architecture](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)（2027 架構錨點）。
- [Infineon GaN HV IBC designs](https://www.infineon.com/technology-news/2026/infpss202603-067)（800V 到 50V／12V）。
- [Infineon SiC HV BBU design](https://www.infineon.com/technology-news/2026/infpss202606-093)（電池到 800V bus 的雙向轉換）。
- [onsemi SST and high-voltage SiC path](https://www.onsemi.com/company/newsroom/featured-stories/data-center/the-emerging-way-to-conquer-power-challenges-in-ai-data-centers)（SST 與高壓 stage）。
- [Infineon grid-to-core material partition](https://www.infineon.com/de/press-release/2026/infxx202606-117)（SiC／GaN／Si 功能定位）。
- [ROHM HVDC dialogue](https://www.rohm.com/ir/dialogue/ai-server)（Si＋SiC planned PSU adoption）。
- [TI 800VDC power architecture](https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html)（800V→6V→sub-1V 與相鄰 building blocks）。
- [ST 800VDC power architectures](https://newsroom.st.com/media-center/press-item.html/t4766.html)（800V→50V／12V／6V paths）。
- [NVIDIA 800VDC architecture hub](https://www.nvidia.com/en-au/data-center/technologies/800-vdc-architecture/)（分階段過渡、既有資料中心與 all-800V 路徑；含官方 whitepaper 入口）。
- [OCP Open Rack V3 HPR V2 72kW power shelf specification](https://www.opencompute.org/documents/open-rack-v3-hpr-v2-72kw-power-shelf-spec-v1-0-0-pdf)（現行 48V power-shelf contract）。
- [OCP Diablo 400 Project Rack and Power Specification 0.7.0](https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf)（±400VDC 端點、差動 800V、線纜 kW／A 選項與 average／RMS current 熱邊界）。
- [Infineon data-center living index](https://www.infineon.com/applications/ai-data-center/data-center-power-solutions) 與 [onsemi data-center living index](https://www.onsemi.com/solutions/computing/data-center)（後續產品與驗證入口）。

本文刻意不把各供應商的峰值效率、功率密度或面積宣稱排成排行榜，因為 topology、輸入輸出、
負載範圍、隔離、冷卻與 reference plane 不同。OCP 的 48V contract、ROHM 的 planned PSU
adoption、供應商 reference architecture 與 NVIDIA 的 2027 full-scale 架構錨點，各自描述不同
系統與證據階段，不能互相替代。

## 8 月 14 日方法補強：先定義電壓端點，再討論升壓受惠

- S12 與 S13 均來自 OCP，保守算一條規格消息鏈；S1 的 NVIDIA platform architecture 是第二條獨立鏈。N=2 條消息鏈不是兩個 rack、產品、客戶、台灣 121 檔或全產業樣本。
- C14 的 1,440A、90A 與 16 倍只是同一 72kW 人為 reference plane 下的確定性算術；C15 的 1／256 又加上 fixed-R 假設。兩者沒有 sampling SE／t，Python Decimal 與 awk 一致只排除算錯，不消除 topology、RMS 波形、導體、轉換、保護與量測邊界的不確定性。
- 本輪提前核對 T3，補上 voltage endpoints、average／RMS current、導體與轉換損耗的讀法；但仍無具名 production topology 在同版本公開全路徑波形、導體溫升、converter raw data、fault／redundancy matrix、customer pass 與 BOM。T3 未完整命中 trigger，保持 active，immutable fields 與 2026-08-19 `next_check` 不變。
- 新證據沒有證明任一材料已勝出、具名台灣供應商取得訂單或改變 C7 的 topology-first 主命題；因此保留 `last_reviewed_at: 2026-08-12`、`review_due: 2026-08-19` 與 `base_confidence: medium`，不用方法教材刷新 thesis evidence clock。

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

- 平台或 hyperscaler 固定 production-level 800V power tree 與 revision，清楚列出每一級的 input／output、隔離、SST／PSU／BBU／protection／IBC／POL 責任。
- 同版 converter 公開全負載效率、EMI、thermal、transient、fault 與 change-control 原始資料，再由客戶或第三方重測；不能只補一個峰值數字。
- 具名 rack／site 公開 as-built configuration、commissioning、fault injection、customer acceptance、operating hours 與 deployment denominator。
- 實際 topology 若保留或取消不同轉換層，重畫六軸選材包絡線，檢查元件需求是轉移、增加還是直接消失。
- 同一 production power path 公開清楚的 voltage endpoints、average／RMS／peak-current waveforms、導體幾何與溫升、逐級轉換效率、fault／redundancy state 與量測不確定度，才比較實際銅用量與 end-to-end loss。
- 台灣公司只有在具名料號、客戶、production BOM、出貨與同產品財務資料能雙向核對時才建立公司線；否則維持族群 watch。
