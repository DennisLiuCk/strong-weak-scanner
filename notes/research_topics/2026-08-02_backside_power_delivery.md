# 晶片把供電線移到背面，不只是換條路：先看電力路徑、製程接力與量產證據

<!-- research_topic
topic_id: MI-2026-08-02-BACKSIDE-POWER-DELIVERY
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-04-16
last_reviewed_at: 2026-08-12
review_due: 2026-08-16
source_type: mixed
publisher: Taiwan Semiconductor Manufacturing Company
publisher_domain: investor.tsmc.com
canonical_url: https://investor.tsmc.com/static/annualReports/2025/english/index.html
source_chain_id: backside-power-manufacturing-milestones-20260802
stock_ids:
group_ids: semiequip,material,ipdesign
trigger_type: process_manufacturing_milestone
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C6
base_confidence: medium
confidence_basis: 台積電、Intel、imec、Lam Research 與 Applied Materials 的一手資料可交叉確認設計、製程成形、製程控制、可靠度與具名製造產品是不同成熟度時鐘；但晶圓代工廠節點定義仍不可直接相比，A16 實際量產產品、台灣設備材料商資格及財務貢獻仍未證實
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_source_backside_power_scan
evidence: source_chain:backside-power-manufacturing-milestones-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_foundry_manufacturing_milestones_from_supplier_revenue_exposure
evidence: sources:S1,S2,S3
-->

<!-- research_source
source_id: S1
role: company_filing
source_kind: document
publisher: Taiwan Semiconductor Manufacturing Company
title: TSMC 2025 Annual Report
published_at: 2026-04-16
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investor.tsmc.com/static/annualReports/2025/english/index.html
locator: Business Overview；N2、N2P、A16 roadmap 段落，A16 Super Power Rail 與 2026 下半年量產時程
limitation: 公司自述製程路線圖；沒有客戶名稱、量產晶圓數、良率或個別供應商內容
independence_group: tsmc
-->

<!-- research_source
source_id: S2
role: competitor_primary
source_kind: document
publisher: Intel Foundry
title: Intel Foundry Details Process Milestones and Future Innovation at VLSI Symposium
published_at: 2026-06-16
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.intel.com/intel-foundry/intel-foundry-details-process-milestones-future-innovation-at-vlsi-symposium
locator: Intel 18A entered production in 2025；Intel 18A-P now in risk production 段落
limitation: Intel 的 production／risk production 定義、產品組合與節點基準不能直接套用到台積電 A16
independence_group: intel
-->

<!-- research_source
source_id: S3
role: other_primary
source_kind: document
publisher: imec
title: Backside power delivery
published_at: 2022-11-25
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.imec-int.com/en/articles/how-power-chips-backside
locator: Promises of a backside power delivery network；Buried power rail and nano-through-silicon-vias；overall process flow 段落
limitation: 研究機構的技術機制與試驗流程不是晶圓廠量產良率、客戶採用或設備商訂單證據
independence_group: imec
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: living_index
publisher: Taiwan Semiconductor Manufacturing Company
title: TSMC A16 Technology
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_A16
locator: 2026-08-02 查得 A16 integrates nanosheet transistors with backside power rail，並標示 2H26 production-ready
limitation: 產品技術頁會持續更新；頁面本身不證明實際量產、客戶採用、良率或供應商收入
independence_group: tsmc
-->

<!-- research_source
source_id: S5
role: competitor_primary
source_kind: living_index
publisher: Intel Foundry
title: Intel Foundry Newsroom
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.intel.com/intel-foundry
locator: 2026-08-02 查得 2026-06-16 Intel 18A-P risk production 更新及後續 Foundry 公告入口
limitation: 新聞索引只用來偵測新文件；任何新主張仍須回到具體公告或申報文件
independence_group: intel
-->

<!-- research_source
source_id: S6
role: other_primary
source_kind: document
publisher: Lam Research
title: Optimizing the Nano-TSV-to-BPR Connection in Backside Power Networks
published_at: 2026-06-29
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://newsroom.lamresearch.com/optimizing-the-nano-tsv-to-bpr-connection-in-backside-power-networks?blog=true
locator: Key Process Challenges、Modeling nTSV Resistance 與 Simulation Highlights 段落；特別是 overlay、corner rounding、contact area 與 nTSV-BPR connection resistance 的連結
limitation: Lam／imec 的虛擬製程與量測比對只針對該研究結構與幾何；本文不把模擬製程窗口改寫成 A16／18A 通用規格、量產良率、客戶資格或供應商收入
independence_group: lam-research
-->

<!-- research_source
source_id: S7
role: management_commentary
source_kind: document
publisher: Taiwan Semiconductor Manufacturing Company
title: TSMC 2Q26 Earnings Conference Transcript
published_at: 2026-07-16
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/547d1696765e05ce3adb81c108ce1c8c1682b80c/TSMC%202Q26%20Transcript.pdf
locator: PDF p.5，A14 development／capacity／volume-production lead-time 段落，以及 A12 will bring Super Power Rail to the A14 platform、2029 volume production 段落
limitation: 這是台積電官網託管的 edited transcript 與前瞻路線圖；A12 時程不證明 A16 已量產，也沒有 A16 客戶、良率、工具、材料或台灣供應商財務拆分
independence_group: tsmc
-->

<!-- research_source
source_id: S8
role: other_primary
source_kind: document
publisher: imec
title: Backside power delivery options: a DTCO study
published_at: 2023-08-28
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.imec-int.com/en/articles/backside-power-delivery-options-dtco-study
locator: BSPDN mechanism、standard-cell connectivity options、block-level evaluation 與 DTCO 段落
limitation: imec／Arm 的研究比較特定 BPR／nTSV 與替代連接方案；不是台積電或 Intel 的完整量產配方、共同效能基準、客戶採用或供應商收入證據
independence_group: imec
-->

<!-- research_source
source_id: S9
role: company_release
source_kind: document
publisher: Applied Materials
title: Applied Materials Unveils Next-Gen Chipmaking Products to Supercharge AI Performance
published_at: 2025-10-07
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unveils-next-gen-chipmaking-products/
locator: Introducing PROVision 10 eBeam Metrology System 段落；purpose-built for GAA／Backside Power Delivery、on-device overlay 與 multiple leading logic and memory chipmakers
limitation: 公司只說具名量測產品可服務背面供電架構且被多家未具名晶片廠使用；沒有把客戶、製程節點、背面供電資格、出貨量、產品收入或毛利逐一對上
independence_group: applied-materials
-->

<!-- research_source
source_id: S10
role: other_primary
source_kind: document
publisher: Lam Research
title: The Other Side of the Wafer: Transistor Channel Stress in Backside Power Delivery Networks
published_at: 2025-04-02
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://newsroom.lamresearch.com/transistor-channel-stress-backside-power-delivery-networks
locator: Challenges of Implementing BSPDN 與 Analyzing Differing Stress Levels in GAA 段落；薄化、背面金屬、TSV、熱機械應力與不同整合方案
limitation: Lam 的虛擬製程研究說明失效機制，不是晶圓廠量產良率、可靠度認證、具名客戶產品或任何台灣供應商財務證據
independence_group: lam-research
-->

<!-- research_source
source_id: S11
role: other_primary
source_kind: living_index
publisher: Lam Research
title: Lam Research Newsroom Technology Blog
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://newsroom.lamresearch.com/blog
locator: 2026-08-12 查得 2026-06-29 nTSV-BPR optimization 與 2025-04-02 backside-power stress 文件，作為後續製程控制、模擬與具名工具更新入口
limitation: 動態索引不證明任何新工具已通過客戶資格或形成財務貢獻；命中新文件後仍須另建 document source
independence_group: lam-research
-->

<!-- research_source
source_id: S12
role: company_release
source_kind: living_index
publisher: Applied Materials
title: Applied Materials Investor Relations News Releases
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://ir.appliedmaterials.com/news-releases
locator: 2026-08-12 查得 2025-10-07 PROVision 10 公告，作為後續背面供電量測產品、客戶採用與財務附件的重查入口
limitation: 新聞索引會持續變動且不證明背面供電客戶、資格、出貨或收入；命中後須回到具體公告、財報或產品文件
independence_group: applied-materials
-->

<!-- research_source
source_id: S13
role: company_release
source_kind: document
publisher: Taiwan Semiconductor Manufacturing Company
title: TSMC Celebrates 30th North America Technology Symposium with Innovations Powering AI with Silicon Leadership
published_at: 2024-04-24
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://pr.tsmc.com/english/news/3136
locator: A16 Technology 段落；相對 N2P 的 same-Vdd speed、same-speed power 與 chip-density 三組條件式指標
limitation: A16 同時結合 nanosheet transistor 與 Super Power Rail；公司 roadmap 指標不是 SPR 單一技術歸因、實際客戶產品、量產良率或跨廠共同 benchmark
independence_group: tsmc
-->

<!-- research_source
source_id: S14
role: competitor_primary
source_kind: document
publisher: Intel
title: PowerVia Test Shows Industry-Leading Performance
published_at: 2023-06-05
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://newsroom.intel.com/client-computing/powervia-test-shows-industry-leading-performance
locator: How It Works 與 test implementation 段落；internal trial node、product-like test chip、cell utilization、platform voltage droop、frequency、thermal 與 debug 邊界
limitation: 公司試驗晶片自述未提供完整測試向量、PVT、封裝／板級 PDN、原始分布或量產產品結果；不能直接和 A16 roadmap 或 Intel 18A 量產節點百分比相比
independence_group: intel
-->

<!-- research_source
source_id: S15
role: other_primary
source_kind: living_index
publisher: Synopsys
title: What is Voltage Drop?
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.synopsys.com/glossary/what-is-voltage-drop.html
locator: 2026-08-12 查得 Static IR Drop、Dynamic IR Drop 與 Managing Voltage Drop With Simulation 段落；DC I×R、L×dI/dt、vector-based、vectorless 與 transient analysis
limitation: EDA 供應商的持續更新工程說明可用來區分量測概念與方法，不是背面供電產品 benchmark、晶圓廠 signoff、客戶採用或量產良率證據
independence_group: synopsys
-->

<!-- research_source
source_id: S16
role: other_primary
source_kind: document
publisher: IBM Research
title: Methodology Development to Benchmark Power Delivery Designs in Advanced Technology Nodes
published_at: 2023-02-27
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://research.ibm.com/publications/methodology-development-to-benchmark-power-delivery-designs-in-advanced-technology-nodes
locator: Abstract；pre-PDK／post-PDK methodology、5nm／2nm BS-PDN simulation，以及 logic-area／minimum-pitch RC-delay 結果對 reference design 的依賴
limitation: IBM 的前 PDK／既有 PDK 模擬只支持指定架構與參考設計的條件關係；不是 A16／18A 實體晶圓、產品效能、量產良率或供應商財務結果
independence_group: ibm-research
-->

<!-- research_source
source_id: S17
role: other_primary
source_kind: document
publisher: IBM Research
title: Comprehensive BEOL Performance Assessment: Interconnects Optimized for Signal Routing and Power Delivery in Advanced CMOS Technology Nodes
published_at: 2020-10-05
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://research.ibm.com/publications/comprehensive-beol-performance-assessment-interconnects-optimized-for-signal-routing-and-power-delivery-in-advanced-cmos-technology-nodes-invited
locator: Abstract；固定 power-tap spacing 與固定 IR-drop 的兩種比較，以及 IR drop 對 power-tap frequency、inverter drive strength、activity factor 的依賴
limitation: beyond-7nm circuit-level simulation 的數值只屬該模型與條件；不能當成現行晶圓節點共同規格、矽驗證結果、跨廠排名或供應商收入證據
independence_group: ibm-research
-->

<!-- research_source
source_id: S18
role: standard
source_kind: document
publisher: National Institute of Standards and Technology
title: SI Units – Electric Current
published_at: 2025-07-29
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.nist.gov/pml/owm/si-units-electric-current
locator: Electric Current 段落；1 V＝1 W/A 與 1 Ω＝1 V/A 的 SI derived-unit 關係，以及頁面 2025-07-29 更新日
limitation: 這是通用 SI 量綱與單位關係，不是晶片 PDN 模型、背面供電設計規則、產品電壓／功率、量測方法、允收門檻或量產結果
independence_group: us-nist-si
-->

<!-- research_source
source_id: S19
role: other_primary
source_kind: document
publisher: IBM Research
title: Analysis and modeling of dc current crowding for TSV-based 3-D connections and power integrity
published_at: 2014-01-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://research.ibm.com/publications/analysis-and-modeling-of-dc-current-crowding-for-tsv-based-3-d-connections-and-power-integrity
locator: IEEE Transactions on Components Packaging and Manufacturing Technology paper abstract；TSV／global power-grid connection 的 current-density distribution、local current crowding、single-resistor model 與 hotspot 邊界
limitation: 公開頁只有摘要；研究對象是 3-D IC TSV 與其線路接點，不是 A16／PowerVia 的 nano-TSV、BPR 或具名產品，也沒有本輪可用的幾何、電流密度分布、溫度、樣本或量產可靠度數字
independence_group: ibm-research
-->

<!-- research_source
source_id: S20
role: other_primary
source_kind: document
publisher: IBM Research
title: Fast and Accurate Machine Learning Prediction of Back-End-of-Line Thermal Resistances in Backside Power Delivery and Chiplet Architectures
published_at: 2025-05-27
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://research.ibm.com/publications/fast-and-accurate-machine-learning-prediction-of-back-end-of-line-thermal-resistances-in-backside-power-delivery-and-chiplet-architectures
locator: ECTC 2025 paper abstract；BSPDN chip-package heat path、BEOL stack thermal resistance、multiscale model 與 maximum-hotspot-temperature sensitivity 段落
limitation: 公開頁只有摘要；模型誤差是作者特定 finite-element reference 與 dataset 的結果，沒有 package stack、raw prediction distribution、實體產品溫度、冷卻邊界、樣本、可靠度、良率或量產成本，本文不採其誤差百分比做跨方法 benchmark
independence_group: ibm-research
-->

<!-- research_source
source_id: S21
role: competitor_primary
source_kind: document
publisher: Intel Foundry
title: Intel Foundry Achieves Major Milestones
published_at: 2024-08-06
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://newsroom.intel.com/intel-foundry/intel-foundry-achieves-major-milestones
locator: What’s New、More on Intel 18A 與 How It Works 段落；Panther Lake／Clearwater Forest 流片後 powered-on／booted、PDK 1.0 與外部客戶預期流片的不同里程碑
limitation: 這是 Intel 在 2024-08-06 的時點公告；powered-on／booted 只證實具名內部產品的早期功能里程碑，外部客戶於 2025 上半年流片是當時前瞻預期，不是已發生的客戶採用、出貨、良率或營收
independence_group: intel
-->

<!-- research_source
source_id: S22
role: competitor_primary
source_kind: document
publisher: Intel
title: Intel Unveils Panther Lake Architecture: First AI PC Platform Built on 18A
published_at: 2025-10-09
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://newsroom.intel.com/client-computing/intel-unveils-panther-lake-architecture-first-ai-pc-platform-built-on-18a
locator: News Highlights、Panther Lake 與 Intel 18A 段落；first client SoC／first product、already in production、Fab 52 ramp、multi-chiplet architecture 與當時預計出貨／上市時程
limitation: 公司公告把 Panther Lake、18A、RibbonFET、PowerVia 與 Foveros 放在同一平台敘事；不能把整體產品效能歸因給 PowerVia，也不能把 Intel 內部產品、production 或預計上市改寫成外部晶圓代工客戶、實際出貨量、良率或市占
independence_group: intel
-->

<!-- research_source
source_id: S23
role: competitor_primary
source_kind: document
publisher: Intel
title: CES 2026: Intel Core Ultra Series 3 Debut as First Built on Intel 18A
published_at: 2026-01-05
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a
locator: News Highlights 與 Availability 段落；Series 3 launch、200-plus design company claim、2026-01-06 preorder、2026-01-27 global system availability 及 edge Q1 2026
limitation: 這是 Intel 的產品上市公告；design 數不是已售系統、處理器出貨、晶圓量、良率或 sell-through，預購與可供應日期也不證明所有地區、OEM、SKU 或通路都有相同庫存
independence_group: intel
-->

<!-- research_source
source_id: S24
role: competitor_primary
source_kind: document
publisher: Intel
title: Intel Technology Tour 2025 Summary - Panther Lake
published_at: 2025-10-16
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://cdrdv2-public.intel.com/866361/ITT_2025_Panther_Lake_Recap1.pdf
locator: PDF pp.26–29；p.26 列 compute／PCD／GPU 分工與 Foveros 2.5D，pp.27–29 三種配置皆把 Compute tile 標為 Intel 18A、PCD 標為 External；8-core 與 16-core／4Xe 的 GPU tile 標 Intel 3，16-core／12Xe 的 GPU tile 標 External；SHA-256 7ed40a155d887af40b65657efaafd3c22cdb290247c4c6643bd3e746bf160864
limitation: 文件沒有可見發布日，published_at 以官方端點 HTTP Last-Modified 2025-10-16 為固定版本錨點；簡報沒有列出 External 的晶圓廠／節點、各 tile 面積與成本、封裝良率、PowerVia 實際覆蓋、產品出貨或 unit mix，GPU 製程又依配置而變，不能以單一 SKU 概括整個家族
independence_group: intel
-->

<!-- research_source
source_id: S25
role: competitor_primary
source_kind: living_index
publisher: Intel
title: Products formerly Panther Lake
published_at:
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://www.intel.com/content/www/us/en/ark/products/codename/237132/products-formerly-panther-lake.html
locator: 2026-08-23 查得 17 Products；15 個產品列示 Q1'26、2 個產品列示 Q2'26，並逐列提供產品名稱、核心、頻率、快取與 GPU
limitation: ARK 是會更新的產品索引且頁面明示資料可能變更；17 是當日列示的 SKU census，不是 shipped units、可買到的 OEM systems、晶圓／封裝良率、退貨率、外部 foundry 客戶或 PowerVia 單獨貢獻
independence_group: intel
-->

<!-- research_source
source_id: S26
role: company_release
source_kind: document
publisher: 2026 IEEE Symposium on VLSI Technology and Circuits
title: A16 Angstrom-class CMOS Technology featuring Enhanced Nanosheet Transistors with Super-Power Rail
published_at: 2026-06-16
captured_at: 2026-08-24
accepted_at: 2026-08-24
status: active
url: https://vlsi26.mapyourshow.com/8_0/sessions/session-details.cfm?ScheduleID=246
locator: 2026-06-16 T1.5 session title、Abstract 與 speaker；TSMC 作者稱 A16 已完成 development／qualification、SPR 採 novel backside direct contact、相對 N2P 的三組平台結果，以及 mass production slated for Q4'26
limitation: published_at 以 2026-06-16 正式場次日期固定證據時點，不視為網頁發布 timestamp；會議頁轉述 TSMC 作者的 A16 平台主張，qualified 範圍未定義，Q4'26 是未來計畫，且沒有公開直接接觸的 landing target、材料、幾何、wafer／lot／die 樣本、良率、客戶、供應商或財務分母
independence_group: tsmc
-->

<!-- research_source
source_id: S27
role: company_release
source_kind: document
publisher: 2026 IEEE Symposium on VLSI Technology and Circuits
title: 2026 VLSI Technical Tipsheet - A16 Super Power Rail
published_at: 2026-04-30
captured_at: 2026-08-24
accepted_at: 2026-08-24
status: active
url: https://www.vlsisymposium.org/wp-content/uploads/2026/04/2026-VLSI-Technical-Tipsheet-REVISED-FINAL-4.25.26-1-1.pdf
locator: PDF reader p.4（網頁文字索引 P3），並渲染相鄰 pp.3、5；p.4 列 Device／F-BEoL→Bond→Flip→Si thinning→VB & B-BEoL 流程、A16 SPR 的 backside direct contact（VB）、ARM core benchmark、N2P 比較與 Q4'26 計畫；SHA-256 9e826bdf7bc4d195155796cf427bfafc306dc4d282297b0300c66b48e90c365c
limitation: published_at 以 PDF creation／modification metadata 2026-04-30 CST 固定版本，不把檔名 4.25.26 當已驗證發布日；這與 S26 同屬 TSMC 消息鏈，圖為高階流程且未公開 bonding 類型、薄化厚度、VB 落點與材料、overlay、分布、良率或 SPR 單獨 PPA 貢獻
independence_group: tsmc
-->

<!-- research_source
source_id: S28
role: other_primary
source_kind: document
publisher: imec
title: The path to high-density front- and backside wafer connectivity
published_at: 2025-08-19
captured_at: 2026-08-24
accepted_at: 2026-08-24
status: active
url: https://www.imec-int.com/en/articles/path-high-density-front-and-backside-wafer-connectivity
locator: Backside through-dielectric vias with 20nm bottom diameter 段落；via-first TDV 先形成於 frontside STI、薄化超過 STI floor 後從背面露出，並列 20nm bottom diameter、120nm pitch、55nm-wide backside metal line 與 15nm layout overlay margin 的 typical test structure
limitation: 這是 imec 研究載具與 typical test structure；TDV 名稱說明穿過 STI dielectric，不自動等於背面供電或直接接到電晶體，幾何與 layout margin 也不是 A16／18A 設計規則、across-wafer overlay 分布、量產良率、客戶資格或供應商財務
independence_group: imec
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: 台積電 2025 年報把 A16 定位為採用 Super Power Rail 的 N2 家族延伸，並把 A16 與 N2P 的量產排在 2026 下半年
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-04-16
basis: S1 的 A16 roadmap 段落直接列示技術定位與 volume production 時程
boundary: 這是公司量產計畫，不等於截至 2026-08-02 已完成量產、客戶採用、良率或收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: Intel 表示 18A 已於 2025 年進入生產，18A-P 則在 2026-06-16 進入風險生產
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-06-16
basis: S2 標題與製程里程碑段落直接區分 18A production 與 18A-P risk production
boundary: Intel 的里程碑不能改寫成外部晶圓代工客戶已大量採用，也不能與台積電 A16 的量產定義直接排名
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: imec 將背面供電的核心機制描述為把供電網路與前側訊號網路分離，並把埋置電源軌、晶圓薄化與 nano-TSV 列為關鍵製程步驟
supporting_source_ids: S3
contrary_source_ids:
as_of: 2022-11-25
basis: S3 的 BSPDN 原理、BPR／nTSV 與 overall process flow 段落直接列出機制及步驟
boundary: 技術必要步驟不等於每一家晶圓廠採用完全相同流程、工具、材料或供應商
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: superseded
claim: 背面供電已由研究概念跨入具名製程的生產與量產時鐘，但目前最可用的研究單位仍是各晶圓廠自己的成熟度階梯，而不是跨廠效能排名或台灣供應鏈受惠名單
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-08-02
basis: S3 建立技術機制，S1 與 S2 分別提供 A16、18A／18A-P 的製造里程碑；三份來源支持方向但沒有共同可比的節點定義與供應商財務資料
boundary: 不推估市占、量產晶圓數、設備內容量、供應商份額或獲利，也不把 Intel 的 production 等同台積電的 volume production
verification_needed:
corrected_by_claim_id: C6
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: 台灣半導體設備、材料或矽智財公司已因 A16／PowerVia 取得可辨識訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有一手來源只證實晶圓廠里程碑與一般製程步驟，未列出台灣供應商、料號、產線或財務貢獻
boundary: 不以「晶圓薄化、CMP、蝕刻、量測可能需要更多」直接建立公司受惠關係
verification_needed: 需晶圓廠與供應商文件雙向核對具名製程步驟、量產資格、出貨與可辨識財務貢獻
resolution:
-->

<!-- research_claim
claim_id: C6
label: inference
status: active
claim: 背面供電不能只用「製程已生產」一個標籤判斷成熟度；截至 2026-08-12，一手證據支持把它拆成五個相接但不可互相替代的時鐘：設計與電力完整性、背面製程成形、製程控制與可靠度、晶圓節點與客戶產品量產、供應商資格與財務轉換
supporting_source_ids: S1,S2,S3,S6,S7,S8,S9,S10
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C4；S3／S8 顯示連接方案需由設計與製程共同最佳化，S6／S10 顯示對準、形貌、接點電阻與機械應力另有製程控制時鐘，S1／S2／S7 提供不同晶圓節點路線與量產語言，S9 則只前進到具名量測產品與未具名晶片廠使用；五組證據不能被單一 production 標籤取代
boundary: 這是證據分層框架，不是跨晶圓廠效能、良率或速度排名；不證明 A16 已完成量產、任一外部客戶產品已採用，也不證明台灣設備、材料或 IP 公司取得訂單、收入、毛利或現金流
verification_needed: 同一具名客戶產品同時公開設計規則或試驗晶片、量產製程窗口與良率、客戶資格、供應商產品出貨，以及可辨識財務結果
correction_kind: supersedes
corrects_claim_id: C4
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: Lam Research 與 imec 的研究顯示，nano-TSV 對埋置電源軌的疊對偏差與圖形圓角會改變實際接觸面積及連接電阻，因此背面導通不能只驗孔有沒有做出來
supporting_source_ids: S6
contrary_source_ids:
as_of: 2026-06-29
basis: S6 的 process challenges、realistic-profile simulation 與 resistance results 直接連結 overlay、corner rounding、contact area 與 nTSV-BPR connection resistance
boundary: 只證實該研究結構與模擬／量測比對的工程關係；不把文中的幾何範圍外推成 A16／18A 通用製程規格、量產良率或設備商訂單
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
claim: 台積電在 2026Q2 法說表示，先進節點從技術與產品開發、準備產能到大量生產需多年接力，並把 Super Power Rail 延伸到規劃 2029 年量產的 A12 平台
supporting_source_ids: S7
contrary_source_ids:
as_of: 2026-07-16
basis: S7 p.5 直接說明新技術、產品、產能與大量生產的長交期，並列示 A12 將把 Super Power Rail 帶到 A14 platform、A12／A13 預計 2029 年量產
boundary: 這證實台積電的路線圖延伸與公司時程說法，不證明 A16 截至 2026-08-12 已量產、A12 一定如期，或任何具名客戶與供應商已完成資格
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
claim: Applied Materials 將 PROVision 10 描述為可服務 GAA 與背面供電架構的具名電子束量測產品，並表示該產品已由多家未具名的先進邏輯與記憶體晶片製造商使用
supporting_source_ids: S9
contrary_source_ids:
as_of: 2025-10-07
basis: S9 的 PROVision 10 段落直接列出 purpose-built application、on-device overlay／critical-dimension metrology 與 multiple leading logic and memory chipmakers
boundary: 這只建立外部設備商的具名產品與廣義使用階段；沒有客戶名稱、A16／18A 對應、背面供電 qualification、台數、收入或毛利，不能改寫成台灣設備商受惠
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
claim: Lam Research 的虛擬製程研究顯示，晶圓薄化、背面金屬與導通結構等整合步驟會改變奈米片電晶體的機械應力與位移分布，可靠度與電性必須另外驗收
supporting_source_ids: S10
contrary_source_ids:
as_of: 2025-04-02
basis: S10 的 integration challenges 與 stress-evolution analysis 直接比較前側與不同背面連接方案，並把薄化、背面金屬、導通結構與應力變化連在同一製程序列
boundary: 這是研究模型與機制證據，不是量產晶圓統計、共同可靠度標準、客戶失效資料或任一供應商財務貢獻
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: imec 與 Arm 以設計技術共同最佳化比較了 BPR／nano-TSV 與其他背面連接方案，並在標準單元與區塊層級評估電力完整性與面積取捨
supporting_source_ids: S8
contrary_source_ids:
as_of: 2023-08-28
basis: S8 直接列出一種 BPR／nTSV 實作、替代 backside connectivity options，以及 standard-cell／block-level DTCO evaluation
boundary: 這證實背面供電需要設計與製程共同選擇，不表示所有晶圓廠採同一結構，也不是量產良率、客戶採用、PPA 跨廠排名或供應商收入證據
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: 台積電對 A16 公開的速度、功耗與密度數字是三個不同控制條件的比較：相對 N2P，在相同 Vdd 下速度提升 8–10%、相同速度下功耗降低 15–20%，以及資料中心產品晶片密度最高 1.10 倍
supporting_source_ids: S13
contrary_source_ids:
as_of: 2024-04-24
basis: S13 的 A16 段落直接列出比較基準 N2P，並分別固定 Vdd、速度與密度分母
boundary: 三組指標不能相加或視為同一顆產品可同時取得；A16 同時結合 nanosheet transistor 與 Super Power Rail，文件沒有把改善拆成 SPR 單一貢獻，也不是實際量產客戶產品結果
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
claim: Intel 2023 年在內部試驗節點的 product-like test chip 上報告 PowerVia 達到超過 90% standard-cell utilization、超過 30% platform voltage-droop improvement 與 6% frequency benefit
supporting_source_ids: S14
contrary_source_ids:
as_of: 2023-06-05
basis: S14 直接說明 PowerVia 與 RibbonFET 分開開發、受測物為 internal trial node 的 silicon test chip，並列出三組結果
boundary: 這是公司試驗晶片結果，不是 Intel 20A／18A 客戶量產產品；文件沒有完整公開共同 baseline、活動向量、PVT、封裝／板級 PDN 與原始分布，不能和 A16 指標直接排名
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: verified
status: active
claim: Intel 2026 年 VLSI 更新把一組背面供電結果明確綁在可比的前側互連技術基準：routed area 減少 11%、dynamic voltage droop 降低 10 倍，並對應「最高 6% frequency uplift 或超過 15% dynamic power reduction」兩種取捨
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-06-16
basis: S2 Additional updates at VLSI 段落直接列出 comparable frontside interconnect baseline、area、dynamic droop，以及 frequency 或 dynamic-power 的條件式結果
boundary: up to 與 or 不可改寫成同時保證；公告沒有完整公開工作負載、PVT、封裝／板級 PDN、樣本分布或客戶產品，亦不能把另一項約 0.5V 的 CPU-core 結果混進同一分母
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C15
label: verified
status: active
claim: 靜態 IR drop 與動態 voltage droop 不是同一量測：前者以直流 I×R 為核心，後者還受快速電流變化與路徑電感影響，且 vector-based、vectorless 與完整 transient analysis 的覆蓋與保守程度不同
supporting_source_ids: S15
contrary_source_ids:
as_of: 2026-08-12
basis: S15 分開定義 static 與 dynamic IR drop，列出 I×R 加 L×dI/dt 的關係，並說明三種活動與時間域分析方法的差異
boundary: 這是工程量測概念與方法，不代表所有公司公告採相同定義，也不證明任何背面供電架構已完成晶片、封裝與系統共同 signoff
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C16
label: verified
status: active
claim: IBM 的電力網路模擬顯示，背面供電改善幅度會隨比較問題改變：固定電源接點間距與固定 IR drop 得到不同答案，IR drop 又受接點頻率、反相器驅動強度與活動因子影響；另一研究的面積與互連延遲結果也明示依 reference design 而變
supporting_source_ids: S16,S17
contrary_source_ids:
as_of: 2023-02-27
basis: S17 對固定 tap spacing／固定 IR drop 分別報告 delay 與 spacing，並列出 activity 等依賴；S16 以 pre／post-PDK 方法說明 area／RC-delay 結果 depends on reference design
boundary: 兩份資料都是特定架構與模型的模擬研究，不能把數字外推到 A16、18A、量產產品、良率、成本或跨廠效能排名
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C17
label: inference
status: active
claim: 閱讀背面供電效能百分比時，至少要把受測物與成熟度、比較基準、固定條件、輸出指標、工作負載／活動向量、空間與時間視窗、PDN 與環境邊界、共同取捨八格對齊；缺一格時只能保留成該文件內的條件式結果，不能跨廠排序或直接歸因到背面供電單一結構
supporting_source_ids: S2,S13,S14,S15,S16,S17
contrary_source_ids:
as_of: 2026-08-12
basis: S13 將 A16 三組 PPA 數字鎖在不同固定條件，S14 與 S2 的 Intel 結果屬不同受測物與 baseline，S15 區分靜態／動態及活動方法，S16／S17 又顯示 reference design、固定量與 activity 會改變結果；交集支持八格比較護照
boundary: 八格是證據閱讀與重驗框架，不是晶圓廠共同 benchmark 標準；現有公開文件仍不足以建立 A16、PowerVia 或其他 BSPDN 的同產品、同工作負載、同 PVT 與同 PDN 範圍排名
verification_needed: 同一版本的 frontside 與 backside 設計公開受測物、baseline、iso-condition、metric definition、activity vector、spatial／temporal window、chip-package-board PDN、PVT／thermal 及完整 PPA／reliability trade-off
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C18
label: verified
status: active
claim: NIST 的 SI 關係固定 1 V＝1 W/A 與 1 Ω＝1 V/A；在明示直流、等效集中路徑與負載端功率的條件下，可由量綱一致地重算 P＝V×I、ΔV＝I×R 與路徑焦耳損耗 P_loss＝I²R
supporting_source_ids: S18
contrary_source_ids:
as_of: 2025-07-29
basis: S18 直接固定 volt、watt、ampere 與 ohm 的 SI derived-unit 關係，三式是同一組單位關係的代數重排
boundary: 只證實通用確定性換算；等效 R 不含未列出的 frequency-dependent impedance，固定 load power 不代表 CMOS 真實 P-V-f 關係，也不提供任何 A16／PowerVia rail、via、產品或 signoff 數值
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C19
label: verified
status: active
claim: IBM 的 3-D IC TSV 研究指出，TSV 與全晶片電源網路的接點可發生 current crowding，局部電流密度可能高於預期平均值，而把 TSV 與線段只簡化成單一電阻會漏掉這類局部 hotspot
supporting_source_ids: S19
contrary_source_ids:
as_of: 2014-01-01
basis: S19 abstract 直接區分 average current density、connection-local current crowding、single-resistor approximation 與 finite-element-checked distribution model
boundary: 這是較大尺度 3-D TSV 的機制與模型證據，不是 A16／PowerVia nano-TSV 或 BPR 的直接量測；不能外推 peak-to-average 倍數、電遷移壽命、產品可靠度或任何供應商規格
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C20
label: verified
status: active
claim: IBM 的 ECTC 2025 BSPDN 研究把 powered transistors 到 heat sink 的熱路徑連到高熱阻的前側後段金屬堆疊，並顯示 BEOL thermal-resistance model 的選擇會實質改變預測的 maximum chip hotspot temperature
supporting_source_ids: S20
contrary_source_ids:
as_of: 2025-05-27
basis: S20 abstract 直接固定 BSPDN chip package、transistor-to-heat-sink path、BEOL stack thermal resistance、multiscale model 與 maximum-hotspot-temperature sensitivity
boundary: 只證實模型與熱路徑需被明示；公開摘要沒有 package stack、冷卻面、實體溫度、樣本或產品資料，不能量化 A16／18A 溫升、冷卻需求、良率、可靠度或成本
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C21
label: inference
status: active
claim: 背面供電的電力完整性應把 rail／reference voltage、負載功率、總電流、等效路徑、壓降、導體與局部電流密度、焦耳損耗、熱路徑與 hotspot、PVT／工作負載及產品資格財務綁成同一份十欄電力—熱護照；只報 mV、百分比、平均電流或較寬金屬都不足以判斷產品裕量與公司價值
supporting_source_ids: S3,S14,S15,S18,S19,S20
contrary_source_ids:
as_of: 2026-08-14
basis: S18 固定電壓電流電阻功率量綱，S3／S14 明示 BSPDN 的 IR-drop 與 thermal 邊界，S15 區分靜態／動態，S19 顯示平均值可漏局部 current crowding，S20 顯示 BEOL thermal model 會改變 hotspot prediction；十欄是跨來源研究整合
boundary: 護照與本文算例不是晶圓廠、NIST 或 IBM 共同標準，也不是電路／熱 signoff；沒有把抽象等效路徑、TSV 模型或 BSPDN 摘要外推成製程規格、產品效能、設備內容量、需求、收入、毛利或投資排序
verification_needed: 同一具名 frontside／backside 產品版本公開 rail reference、load／activity、chip-package-board current path、distributed RLC、local current-density／thermal distribution、PVT、cooling boundary、reliability、good-product yield、成本與供應商財務共同鍵
resolution:
-->

<!-- research_claim
claim_id: C22
label: verified
status: active
claim: Intel 在 2024-08-06 表示 Panther Lake 與 Clearwater Forest 已於流片後 powered-on 並啟動作業系統，且 18A PDK 1.0 已提供；同篇所稱首位外部客戶預計於 2025 上半年流片，當時仍是前瞻里程碑
supporting_source_ids: S21
contrary_source_ids:
as_of: 2024-08-06
basis: S21 What’s New 直接把兩個內部產品的流片、powered-on／booted 與預計 2025 生產分列，More on Intel 18A 則另列 PDK 1.0；外部客戶使用 expected 語氣
boundary: 開機證明該批早期矽可執行作業系統，不等於產品生產、上市、出貨、穩定良率或 field reliability；外部客戶預期不能回填成已完成 tape-out 或採用
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C23
label: verified
status: active
claim: Intel 於 2025-10-09 將 Panther Lake／Core Ultra Series 3 定位為第一個採用 18A 的 client 產品與 SoC，並表示它已進入生產；同篇把首批 SKU 出貨與 2026 年 1 月廣泛上市仍列為後續時程
supporting_source_ids: S22
contrary_source_ids:
as_of: 2025-10-09
basis: S22 News Highlights 與 Panther Lake 段落直接分列 first client SoC／first product、already in production、first SKU slated to ship 與 broad market availability starting January 2026
boundary: 這證實具名 Intel 內部產品已由開機走到生產，但當時的 slated／starting 仍是前瞻文字；production 不提供 wafer start、good die、yield、shipment 或外部 foundry customer 分母
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C24
label: verified
status: active
claim: Intel 於 2026-01-05 正式推出 Core Ultra Series 3，公告首批消費型筆電 2026-01-06 開放預購、2026-01-27 起全球供應，並稱該平台將驅動超過 200 個設計
supporting_source_ids: S23
contrary_source_ids:
as_of: 2026-01-05
basis: S23 News Highlights 直接標示 launched 與 over 200 designs，Availability 段落列出 preorder、global systems available 與 edge Q1 2026 日期
boundary: 上市與系統可供應讓產品時鐘再前進，但 200-plus designs 是公司所報設計數，不是已出貨／已售系統、處理器顆數、良率、退貨率或 field reliability；也不是外部 foundry 客戶數
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C25
label: verified
status: active
claim: Intel 的 Panther Lake 架構簡報把三種配置的 compute tile 都標為 Intel 18A、PCD 都標為 External；GPU tile 則依配置標 Intel 3 或 External。截至 2026-08-23，ARK 在同一代號下列出 17 個產品，其中 15 個列 Q1'26、2 個列 Q2'26
supporting_source_ids: S24,S25
contrary_source_ids:
as_of: 2026-08-23
basis: S24 pp.27–29 對 8-core、16-core／4Xe、16-core／12Xe 逐 tile 標示製造來源，S25 當日索引列出 17 Products 及逐項 Launch Date；15／2 是對完整可見列的確定性計數
boundary: 17 是可變動索引的 SKU census，不是隨機樣本、出貨量或供應狀態；External 沒有公開晶圓廠與節點，GPU 來源又隨配置改變，不能由品牌產品反推整顆封裝每一 tile 都採 18A／PowerVia，或把平台效能歸因給 PowerVia
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C26
label: inference
status: active
claim: 背面供電的具名產品時鐘至少要把 PDK、內部設計流片、首次開機、生產／量產爬坡、處理器 SKU 上市、終端系統可供應、重複出貨與良率／field quality、外部 foundry 客戶採用、供應商財務九道門分開，並逐一固定 node、tile、package、SKU、OEM system 與 unit／wafer／lot 分母
supporting_source_ids: S21,S22,S23,S24,S25
contrary_source_ids:
as_of: 2026-08-23
basis: S21 把 PDK、流片、開機與外部客戶預期分列，S22 讓同一內部產品前進至 production，S23 再提供 launch、preorder 與 system availability，S24／S25 顯示同一產品名下仍有 tile 與 SKU 分母；交集支持九門而非單一 production 標籤
boundary: 九道門與產品證據護照是研究中心的閱讀框架，不是 Intel 或晶圓代工業共同認證；同一 Intel 產品時間序列不能替代獨立客戶、良率、field reliability、外部 foundry 採用、供應商資格或財務證據
verification_needed: 同一具名產品以可重建共同鍵公開每個 tile／node、內外部客戶身分、tape-out／production／availability、wafer／lot／good-die yield、unit shipment／returns、field reliability、供應商 qualification／出貨與收入
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C27
label: verified
status: active
claim: 2026 VLSI 官方資料把台積電 A16 的 Super Power Rail 描述為 novel backside direct contact，並以 Device／F-BEoL、Bond、Flip、Si thinning、VB & B-BEoL 顯示高階流程；TSMC 作者稱平台已完成 development／qualification，量產排定 2026Q4
supporting_source_ids: S26,S27
contrary_source_ids:
as_of: 2026-06-16
basis: S26 session title／Abstract 直接寫 developed and qualified、backside direct contact 與 mass production slated for Q4'26；S27 p.4 的流程圖與截面示意以 VB 標示直接接觸，兩者屬同一 TSMC 消息鏈
boundary: qualified 的範圍未公開，不能改寫成客戶認證、量產良率或已量產；Q4'26 在 2026-08-24 仍是未來計畫，公開圖也不足以判定 VB 最後落在 source／drain、特定 contact metal、BPR 或其他端點，更沒有材料、幾何、工具與供應商
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C28
label: verified
status: active
claim: imec 的公開研究顯示，BPR／nTSV、TSV-middle 與直接 backside connectivity 的差異首先在導通落點；另一路 via-first TDV 則先在 frontside STI 內形成，薄化後因穿過 STI dielectric 而得名，TDV 名稱本身不表示一定直接接到電晶體或只用來送電
supporting_source_ids: S3,S8,S28
contrary_source_ids:
as_of: 2025-08-19
basis: S3 把 BPR／nTSV 明列為一種 specific implementation，S8 分列 BPR、TSVM、BSC-E／BSC-M／BSC-M* 的不同連接終點，S28 則直接解釋 via-first TDV 在 STI 中形成及穿越 dielectric 的命名
boundary: 三份 imec 文件涵蓋不同研究載具與年份，不能拼成任何晶圓廠的單一量產流程；S28 的 20nm bottom、120nm pitch、55nm-wide backside metal line 與 15nm layout margin 只屬 typical test structure，不是 A16／18A 規格、across-wafer overlay、良率或供應商資格
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C29
label: inference
status: active
claim: 閱讀背面供電連接時，應至少分開記錄三個可能彼此耦合的面向：最後落點、垂直結構穿過的材料區域、導通結構在正面／接合／薄化流程中的形成時序；direct contact、BPR／nTSV 與 TDV 因而不是三個可直接排序或互斥的世代名稱
supporting_source_ids: S3,S8,S26,S27,S28
contrary_source_ids:
as_of: 2026-08-24
basis: S3／S8 顯示 BPR、TSVM、BSC 的落點與中繼不同；S28 顯示 TDV 名稱來自穿越 STI dielectric，而該份特定示範另採 via-first 時序；S26／S27 又只把 A16 公開到 backside direct contact 與高階流程。交集支持三面向護照，而不是用一個 via 名稱補完全部結構
boundary: 三面向護照是研究中心的閱讀框架，不是 TSMC、imec 或產業標準；公開案例只證明部分組態，不表示三個面向可以任意組合、均可製造或具有相同成本與可靠度。不能把 imec test-structure 幾何搬到 A16，也不能把 A16 完整平台相對 N2P 的速度、功耗與密度主張拆成 SPR 單一貢獻或跨廠排名
verification_needed: 晶圓廠以具名節點公開可追溯剖面、landing target、穿越材料、via-first／middle／last 時序、幾何分布、接點電阻、wafer／lot 良率與客戶產品，並由供應商端核對資格及財務共同鍵
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: retired
claim_ids: C1,C2,C4
metric: A16、18A 與 18A-P 的實際量產、客戶產品與製造成熟度里程碑
source_ids: S1,S2
watch_source_ids: S4,S5
frequency: weekly
frequency_detail: 每週檢查晶圓廠技術頁、新聞稿與法說；重大製程更新即重審
next_check: 2026-08-09
trigger: 台積電確認 A16 實際進入量產或具名客戶產品，或 Intel 更新 18A／18A-P 出貨與外部客戶狀態
invalidation: A16 時程延後、18A 量產問題或客戶改採不含背面供電的替代節點，均下修近期商業成熟度
retired_at: 2026-08-12
retirement_reason: C4 已由 C6 的五時鐘框架取代；T1 的 2026-08-09 產品里程碑檢查已留下 no_new_evidence review，後續由 T3 分開追設計、製程控制與客戶產品量產
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C3,C5
metric: BPR、晶圓薄化、bonding、nTSV、背面金屬與量測步驟的具名供應商資格及財務轉換
source_ids: S3
watch_source_ids: S4,S5
frequency: event_driven
frequency_detail: 晶圓廠或供應商發布具名 A16／18A 製程工具、材料、資格或量產結果時檢查
next_check: 2026-08-16
trigger: 至少一組晶圓廠與供應商文件可雙向核對同一製程步驟、量產狀態與收入邊界
invalidation: 若製程整合由晶圓廠自有方案完成、供應商無具名資格或只有研發合作，台灣公司映射維持未證
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C1,C2,C6,C7,C8,C10,C11
metric: 背面供電從設計驗證、接點與應力製程窗口，走到具名晶圓節點、客戶產品及穩定量產的五時鐘證據
source_ids: S1,S2,S6,S7,S8,S10
watch_source_ids: S4,S5,S11
frequency: monthly
frequency_detail: 每月檢查晶圓廠技術／法說、Lam 製程研究與具名客戶產品；重大量產或可靠度更新即重審
next_check: 2026-08-26
trigger: 同一具名產品公開設計或試驗晶片結果、可重現製程窗口／良率、客戶資格與實際量產，或 A16／18A 外部客戶產品提供可定位出貨證據
invalidation: 晶圓廠延後節點、產品取消背面供電，或接點電阻、應力、良率與可靠度無法跨過量產門檻，均下修相應時鐘而非只看 roadmap 名稱
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C5,C6,C7,C9,C10
metric: 具名背面供電設備／材料由能力與產品，進入晶圓廠 qualification、重複出貨、台灣公司映射與財務轉換
source_ids: S6,S9,S10
watch_source_ids: S11,S12
frequency: event_driven
frequency_detail: 設備材料商或晶圓廠公布具名工具、節點、客戶資格、量產出貨及財務附件時重審
next_check: 2026-09-12
trigger: 至少一組晶圓廠、設備／材料商與財務文件能對上同一產品、製程步驟、量產資格、出貨期間及收入邊界
invalidation: 產品只維持通用 GAA／BSPDN 能力、客戶與節點持續匿名，或台灣公司沒有雙向資格及財務證據，個股映射維持未證
-->

<!-- monitoring_item
monitor_id: T5
status: active
claim_ids: C12,C13,C14,C15,C16,C17
metric: 背面供電效能主張是否公開可重現的八格比較護照，而非只剩單一改善百分比
source_ids: S2,S13,S14,S15,S16,S17
watch_source_ids: S4,S5
frequency: monthly
frequency_detail: 每月檢查晶圓廠、試驗晶片與客戶產品文件；新效能數字出現時逐格核對受測物、baseline、iso-condition、metric、activity、window、PDN／PVT 與 trade-off
next_check: 2026-09-12
trigger: 同一 frontside／backside 產品版本公開共同工作負載與 PVT，並同時提供 static IR drop、dynamic droop、area、frequency／power、thermal、reliability 及原始分布或可重現方法
invalidation: 若後續數字持續來自不同節點、試驗晶片、baseline 或只給 up to／or 的宣傳百分比，跨廠比較與單一技術歸因維持不可判定
-->

<!-- monitoring_item
monitor_id: T6
status: active
claim_ids: C22,C23,C24,C25,C26
metric: 具名背面供電產品是否由內部開機、production、SKU／system availability 進一步走到可核對的重複出貨、良率、field quality、外部 foundry 客戶與供應商財務
source_ids: S21,S22,S23,S24,S25
watch_source_ids: S5,S25
frequency: monthly
frequency_detail: 每月核對 Intel Foundry 公告與 Panther Lake ARK；具名外部客戶 tape-out、產品、出貨、良率／可靠度或供應商財務出現時立即重審
next_check: 2026-09-30
trigger: 同一具名外部 foundry 客戶產品公開 tape-out、production、SKU／system availability、wafer／lot yield、unit shipment／field quality，並能接到供應商 qualification 與財務共同鍵
invalidation: 若 18A 只由 Intel 內部產品承接、外部客戶持續不具名或取消，或上市 SKU／OEM designs 無法轉成穩定出貨、良率與 field quality，外部商業成熟度維持未證或下修
-->

<!-- monitoring_item
monitor_id: T7
status: active
claim_ids: C27,C28,C29
metric: A16 direct contact 與 BPR／nTSV、TSVM、BSC、TDV 是否以落點、穿越材料、整合時序及研究／量產分母完整公開，而非只靠同一個 backside-via 名稱互相補值
source_ids: S3,S8,S26,S27,S28
watch_source_ids: S4
frequency: monthly
frequency_detail: 每月核對 TSMC A16 技術頁、VLSI 正式文件與 imec 連接研究；晶圓廠公開剖面、尺寸、量產或客戶資料時立即重審三軸護照
next_check: 2026-09-30
trigger: A16 或其他具名量產節點公開 landing target、穿越材料、via 形成時序、幾何與接點電阻分布、wafer／lot 良率及客戶產品，且供應商 qualification 能雙向核對
invalidation: 若後續正式剖面顯示本文分類漏掉關鍵中繼、同一名詞在不同流程有不同終點，或 TSMC 公開資料否定本文對 A16 未揭露欄位的判斷，就修正相應軸與邊界；未公開前不以 imec 尺寸替 A16 補值
-->

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:high_frequency_glossary
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave98_backside_power_path_process_roles_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: superseded_single_manufacturing_clock_after_design_process_control_reliability_and_roadmap_evidence
evidence: sources:S6,S7,S8,S9,S10
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_conditioned_measurement_passport_for_static_dynamic_and_ppa_claims
evidence: sources:S2,S13,S14,S15,S16,S17
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_voltage_current_resistance_loss_and_hotspot_passport_without_thesis_clock_refresh
evidence: sources:S18,S19,S20
-->
<!-- transition
date: 2026-08-23
from: triaged
to: triaged
reason: added_named_product_boot_production_availability_and_package_denominator_without_thesis_clock_refresh
evidence: sources:S21,S22,S23,S24,S25
-->
<!-- transition
date: 2026-08-24
from: triaged
to: triaged
reason: added_a16_direct_contact_and_three_axis_connection_architecture_without_thesis_clock_refresh
evidence: sources:S26,S27,S28
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **訊號線**：在晶片內傳送資料與控制指令的金屬連線；本文把它和送電的路徑分開理解。
- **供電線**：把電力送到電晶體附近的金屬網路；背面供電改變的是它所在的位置與接近元件的方式。
- **晶圓背面**：和電晶體、接點及前側金屬相反的一面；背面供電要把這一面加工成新的送電入口。
- **晶圓正面**：製作電晶體、接點與多層訊號金屬的一面；傳統電源與訊號會在前側佈線資源中彼此競爭。
- **電晶體**：晶片中執行開關與運算的基本元件；電力與訊號最後都要接近它，但扮演的功能不同。
- **背面供電（BSPDN）**：把供電網路移到晶圓背面，與前側訊號網路分開的架構方向。
- **電源軌**：在晶片內分配電力的金屬線；越接近電晶體，越需要控制阻抗、壓降與製程一致性。
- **埋置電源軌（BPR）**：位在電晶體下方的金屬電源軌，讓背面送入的電力能靠近元件。
- **奈米級背面導通孔（nTSV／nano-TSV）**：穿過薄化矽層、把背面金屬接到埋置電源軌附近的微小導通結構；本文引用的是 imec 的一般流程。
- **背面金屬**：做在晶圓背面的供電金屬網路；它仍要透過導通結構與前側元件連接。
- **前側後段金屬（BEOL）**：電晶體完成後疊在晶圓正面的多層金屬與介電層，負責訊號與傳統供電佈線；它也是部分背面供電封裝的散熱路徑。
- **超級電源軌（Super Power Rail）**：台積電 A16 的背面供電實作名稱；名稱本身不公開完整流程、工具或供應商。
- **背面直接接觸（Direct backside contact）**：從背面建立較直接接觸的架構方向；「直接」仍要說明最後落點，名稱本身不公開 A16 是否含其他中繼、端點、材料或尺寸。
- **VB**：台積電 2026 VLSI Technical Tipsheet／技術摘要在 A16 SPR 圖中使用的背面直接接觸標籤；公開圖沒有替 VB 展開通用全名，也沒有揭露最後落點。
- **導通落點**：一條背面垂直連接最後碰到的結構，可能是埋置電源軌、前側金屬、源／汲極外延區或接觸金屬；它比孔的名稱更能說明電力怎麼接近元件。
- **TSV-middle（TSVM）**：imec 研究中的替代連接路徑，以較高的垂直導通結構接到前側金屬側邊，不使用 BPR 中繼；它不是 A16 已公開的結構名稱。
- **背面直接連接（BSC）**：imec 研究中把背面連接直接接到源／汲極外延區或其接觸金屬的方案家族；BSC-E、BSC-M 等研究變體不能自動套成台積電 SPR。
- **穿介電層導通孔（TDV）**：穿過介電材料的垂直連接；imec 的 via-first 研究把它做在淺溝槽隔離區，名稱只告訴讀者穿過什麼，不保證終點或用途。
- **淺溝槽隔離（STI）**：用介電材料隔開相鄰元件的區域；TDV 可在這個區域形成，和穿過剩餘矽層的 nTSV 是不同命名軸。
- **Via-first／middle／last**：垂直連接相對元件、前側金屬、接合與薄化流程的形成時序；時序不同，不表示落點或用途必然不同。
- **背面供電導通（PowerVia）**：Intel 18A 家族的背面供電實作名稱；不能因名稱相近就假設和台積電採相同結構。
- **A16／A12**：A16 是台積電規劃結合超級電源軌、並把量產排在 2026 下半年的具名製程；A12 是公司規劃於 2029 年把同一供電方向延伸到 A14 平台的後續節點，不代表 A16 已實際量產。
- **N2P**：台積電 N2 家族的延伸製程，也是公司公開 A16 速度、功耗與密度指標所用的比較基準；比較 A16 和 N2P 不能自動拆出背面電軌的單獨貢獻。
- **Intel 18A**：Intel 表示已於 2025 年進入生產的製程；本文不把這個里程碑與其他晶圓廠的量產用語直接排名。
- **Intel 18A-P**：Intel 18A 家族的延伸製程；Intel 於 2026 年 6 月表示它已進入風險生產。
- **Panther Lake／Core Ultra Series 3**：Panther Lake 是 Intel 客戶端處理器平台代號，上市名稱包含 Core Ultra Series 3；本文把它當成一個具名產品家族，不把平台名當成單一晶粒。
- **Intel ARK**：Intel 的公開產品規格與型號索引；可用來核對當下列示的 SKU，但頁面會更新，listing 也不等於庫存、出貨或銷量。
- **PCD／External**：PCD 是 Panther Lake 的 platform-controller tile；官方簡報把它標為 External，表示不是 Intel 18A compute tile，但沒有在該文件公布外部晶圓廠與節點。
- **RibbonFET**：Intel 18A 的環繞閘極電晶體架構名稱；Panther Lake 同時使用 RibbonFET、PowerVia、Foveros 與多個 tile，不能把平台結果只歸因給其中一項。
- **晶圓接合**：把製程晶圓固定到支撐載體，讓原本朝下的背面可以安全加工。
- **支撐載體**：在晶圓變薄後提供機械支撐的暫時載體；有載體不等於整條製程已可量產。
- **晶圓薄化**：從背面移除大量矽，使後續導通孔能在更短距離內接近前側電源軌。
- **研磨**：先以機械方式快速去除背面材料的步驟；後續仍要用其他製程控制表面與剩餘厚度。
- **化學機械平坦化（CMP）**：同時利用化學反應與機械拋光控制表面平坦度的製程。
- **蝕刻**：用化學或電漿選擇性移除材料；背面流程會用它控制剩餘厚度、開孔與露出目標結構。
- **蝕刻停止層**：用來提示或限制蝕刻深度的材料層；它涉及材料與整合能力，不等於具名供應商已取得訂單。
- **背面對準**：晶圓接合、薄化甚至變形後，仍要從背面找到前側目標位置的製程能力。
- **製程整合**：把元件、接合、薄化、對準、開孔、金屬與檢查串成可重複製造的完整流程。
- **製程設計套件（PDK）**：晶圓廠提供給設計端的規則、模型與驗證資料；有新套件需求不等於本地 IP 公司已有授權收入。
- **流片（Tape-out）**：設計資料完成並交給晶圓廠進入製造的里程碑；流片不表示晶片已做完、可開機、良率穩定或上市。
- **Powered-on／booted（上電／開機）**：首次矽能通電，甚至啟動作業系統；它比流片多一層功能證據，但仍不是量產、出貨或長期可靠度。
- **大量生產爬坡（High-volume production ramp）**：產線把產量逐步拉高的過程；公司說已開始爬坡，不等於公開了 wafer starts、良率或 good units。
- **SKU（庫存單位）**：用型號區分可銷售產品的單位；同一架構可有多個 SKU，列出 17 個 SKU 不等於賣出 17 顆，也不代表 17 個獨立客戶。
- **OEM design（品牌整機設計）**：筆電或系統品牌規劃採用某處理器的機種設計；design 數可能包含尚未上市或不同配置，不能直接當成已售系統。
- **終端系統可供應**：消費者或企業可透過通路取得搭載該處理器的完整系統；公告供應日期仍要和地區、SKU、庫存及實際出貨分開。
- **多晶粒產品（Multi-chiplet product）**：把運算、繪圖、I/O 等不同 tile 放進同一封裝；產品使用某先進節點，不表示封裝內每個 tile 都用同一節點或同一背面供電。
- **內部產品／外部晶圓代工客戶**：內部產品由同一家公司設計並使用自己的製程；外部客戶則把第三方設計交給晶圓廠製造。前者成功不能自動證明後者已採用。
- **設計技術共同最佳化（DTCO）**：設計與製程一起調整，讓電源、訊號、面積與製造限制能相互配合。
- **風險生產**：製程已進入早期製造驗證，但仍不是成熟大量生產、外部客戶採用或穩定良率的同義詞。
- **量產計畫**：公司對未來進入大量生產的時程安排；計畫不等於截至目前已完成量產。
- **客戶資格認證（Qualification）**：客戶依功能、可靠度與製造條件確認工具、材料或產品是否可採用。
- **良率**：投入製造後能成為合格品的比例；沒有共同產品與製程分母時，不能跨廠直接比較。
- **雙向核對**：同一具名製程、工具或材料同時能由晶圓廠端與供應商端文件互相對上。
- **財務足跡**：能在出貨、收入、毛利或現金流中辨識的結果；只看到技術需要或合作公告還不算。
- **電力完整性**：電力送到各處電晶體時，電壓與電流仍維持在設計可接受範圍的程度。
- **電壓降（IR drop）**：電流通過有電阻的路徑後造成的電壓損失；線路和接點都會影響它。
- **毫伏（mV）**：一伏特的千分之一；mV 是絕對壓降，還要除以同一參考點的工作電壓才得到相對百分比。
- **靜態 IR drop**：在近似固定電流下觀察供電路徑的直流壓降；核心關係是電流乘上電阻。
- **動態／瞬態電壓下陷**：大量電晶體短時間切換時，供電因電流驟變與路徑阻抗短暫下降；它和靜態 IR drop 不是同一種量測。
- **工作電壓（Vdd）**：供應給電晶體的正電源電壓；「相同 Vdd」表示比較時先把這個條件固定。
- **供電參考點**：說清楚電壓是在調壓器、封裝入口、晶片電源軌或電晶體端量到；同一條路不同位置的電壓不能混成一個數字。
- **等效供電路徑**：把指定參考點之間分散的金屬、接點與導通孔暫時合成一個電阻或阻抗，方便量綱核對；它不是實際只有一條線。
- **分散式 RLC 路徑**：把金屬網路各處的電阻、電感與電容保留在空間位置與連接關係中；比單一等效電阻更能描述動態下陷與局部差異。
- **電流密度**：電流除以通過的導體截面積；總電流相同時，截面、分流與局部幾何不同，密度也會不同。
- **電流擁擠（Current crowding）**：電流在轉角、接點或截面改變處集中，使局部電流密度高於整體平均；平均值過關不代表局部沒有熱點。
- **焦耳損耗**：電流通過電阻時轉成熱的功率；在本文的直流等效算例中用 I²R 表示，不代表完整晶片只有這一種功耗。
- **熱阻**：指定兩個熱參考面之間，溫差相對通過熱功率的阻力；必須固定堆疊、面積、邊界與穩態／瞬態方法才能比較。
- **熱點（Hotspot）**：晶片或封裝局部溫度較高的位置；它受功率分布與多條散熱路徑共同影響，不能由全晶片平均溫度代替。
- **NIST**：美國國家標準暨技術研究院；本文只引用它的 SI 單位關係，不把通用量綱當成晶片產品標準。
- **相同速度（iso-speed）**：先讓兩個設計達到同一速度，再比較誰需要較少功耗；不能和相同電壓下的速度增益相加。
- **標準單元**：用來拼成數位邏輯的基本設計積木；單元高度、供電與訊號佈線會一起影響面積和速度。
- **單元利用率（cell utilization）**：指定版圖區域中可放入標準單元的比例；不是整顆晶片的電晶體密度、良率或成本同義詞。
- **已佈線面積（routed area）**：完成電源與訊號實際佈線後，設計占用的區域；不能直接替換成晶片密度或可售晶粒數。
- **試驗晶片（test chip）**：為驗證特定結構、規則或失效模式製作的矽載具；比純模擬多一層證據，但仍不是客戶量產產品。
- **參考設計（reference design）**：拿來做前後比較的固定電路或版圖；換了設計，面積、壓降與延遲結果也可能改變。
- **活動向量**：描述哪些電晶體在什麼時間切換的測試輸入；它會改變瞬時電流和最壞電壓下陷位置。
- **製程、電壓、溫度條件（PVT）**：電晶體製造差異、工作電壓與溫度的組合；只報典型條件不能替代最壞角落驗證。
- **效能、功耗、面積（PPA）**：晶片設計常一起取捨的三個結果；必須說明固定哪一項，才能比較另外兩項。
- **超大型積體電路研討會（VLSI Symposium）**：發表半導體元件與電路研究的技術會議；公司新聞摘要可定位結果，但不能替未公開的完整測試方法補值。
- **接點電阻**：兩個導電結構相接處對電流形成的阻力；孔做出來不代表接點一定夠低阻。
- **疊對誤差**：不同製程圖形沒有完全對準的偏差；背面導通孔和前側電源軌錯位會縮小接觸面積。
- **邊緣位置誤差**：實際圖形邊緣相對設計位置的偏差；它會和疊對誤差、圓角一起改變接點形貌。
- **製程窗口**：一組製程參數仍能穩定做出合格結果的容許範圍；單次成功不等於窗口已足夠量產。
- **機械應力**：材料受拉、壓或熱變化後承受的內部力量；薄化和背面金屬可能改變電晶體附近的應力。
- **熱預算**：後續製程允許晶圓承受的溫度與時間總量；超出限制可能改變既有材料或元件特性。
- **電子束量測**：以電子束觀察微小圖形尺寸、位置或缺陷的方法；具名量測產品不等於已通過某節點資格。
- **虛擬製程模擬**：先在電腦中重建製程形貌、應力或電性，縮小實驗範圍；模型結果仍要由實體晶圓驗證。
- **產品化設備（例如 PROVision 10）**：供應商已把能力做成具名、可交付的工具；它比概念能力多一步，卻仍不等於客戶資格、重複出貨或收入。

### 三句話抓重點

- 晶片正面原本要同時安排訊號線與供電線；這種做法把供電網路移到晶圓背面，讓電力與訊號改走不同方向。
- 要做到這件事，晶圓要依序完成靠近元件的電源軌、接合、薄化、背面對準、開孔、填金屬與檢查；少一道都不能只靠概念圖量產。
- 對公司而言，看到某道製程變重要只代表值得研究；還要核對具名工具或材料、客戶認證、量產出貨、份額、價格與財務結果，才能談受惠。

### 為什麼重要

**先分清為什麼要改供電路徑。** 正面仍要讓訊號抵達電晶體，供電則改從背面金屬、導通孔
與電源軌接近元件。這是在解決電力和訊號爭用前側空間、供電路徑過長等問題；架構方向成立，
不代表每家晶圓廠都採相同的連接方式、材料或工具。

**再看能不能穩定做出來。** 晶圓做完正面結構後，還要接到支撐載體、從背面變薄、重新
找準前側位置、開出導通結構、形成背面金屬，並控制接點電阻、機械應力與可靠度。孔做出來
只是幾何完成；電力能否穩定通過、整片晶圓能否重複生產，才是另外兩層驗收。

**最後才問誰能賺到錢。** 晶圓廠公布節點路線圖，外部設備商推出具名產品，都只推進各自
的成熟度時鐘。設備、材料與設計服務公司仍要證明客戶資格、重複出貨、份額與價格，最後再
接回收入、毛利和現金流；缺一段就不能把技術需要寫成公司受惠。

### 接下來怎麼追

- 先問新消息推進哪一個時鐘：設計、製程成形、製程控制、客戶產品量產，還是供應商財務。
- 再把背面連接拆成三問：最後接到哪裡、穿過什麼材料、在製程哪個時間點形成；孔名相同也不能省略。
- 再查它量的是哪個失效位置：對準、接觸面積、接點電阻、電力完整性、應力、良率或可靠度。
- 遇到「提升幾％」時，先填完受測物、基準、固定條件與量測範圍；百分比沒有共同分母就不跨公司排名。
- 遇到毫伏、安培或瓦特時，再固定供電參考點、負載功率、等效路徑、總電流／局部電流密度及完整散熱邊界。
- 最後要求晶圓廠端與供應商端雙向核對同一產品與期間，並補上資格、出貨、份額、價格與財務結果。

### 想一想

- 晶圓確實需要變薄，為什麼仍不能直接推論某一家薄化設備商會增加獲利？
- 如果晶圓廠已進入生產，而外部供應商只推出具名量測產品但沒有節點資格，應上調哪一個時鐘？
- 同一道製程由不同晶圓廠以不同名稱實作時，哪些資料可以比較，哪些必須留在各自的成熟度時鐘？
- 「動態電壓下陷降低 10 倍」和「電壓下陷改善超過 30%」看似衝突；在知道受測物、基準與活動向量前，為什麼其實不能比較？
- 同樣少掉 30 毫伏，若原本供電是 0.75 伏或 0.50 伏，留給電晶體的相對裕量為什麼不同？
- 公司說平台有 200 多個 design、產品索引有 17 個 SKU 時，為什麼仍不能推出處理器出貨量、良率或外部晶圓代工客戶數？
- 兩份文件都寫「從背面接上」，若一個先到地下電源軌、另一個直接到元件接點，為什麼不能共用孔徑與製程難度？

## 先用五個時鐘判斷成熟度

背面供電不是從「研究中」突然跳到「已量產」。比較穩妥的讀法，是把同一條技術路徑拆成
五個會互相接力、卻不能互相代替的時鐘：

| 本文五個時鐘 | 核心問題 | 可以升級的證據 | 本輪位置 | 仍然缺什麼 |
|---|---|---|---|---|
| 1. 設計與電力完整性 | 電力從背面進入後，電壓降、瞬態下陷、訊號佈線與晶片面積能否一起改善 | 設計規則、模型、試驗晶片及同一產品的電力完整性結果 | imec／Arm 已比較多種連接方案與設計取捨 | 晶圓廠和具名客戶產品的完整設計規則與實測 |
| 2. 背面製程成形 | 接合、薄化、對準、開孔、填金屬與背面配線能否做出完整結構 | 實體晶圓流程、截面、材料與可重複的整合步驟 | imec 說明一般流程；晶圓廠公布各自架構名稱 | A16／18A 完整配方、工具、材料與共同分母 |
| 3. 製程控制與可靠度 | 疊對、圓角、接觸面積、電阻、應力與熱變化能否留在製程窗口 | 實體量測、模型對照、失效分布、可靠度與良率資料 | Lam 說明接點與應力機制；Applied 有具名量測設備 | 具名節點的量產窗口、長期可靠度與良率統計 |
| 4. 晶圓節點與客戶產品 | 製程能否從計畫、風險生產走到具名產品的穩定大量生產 | 客戶產品、出貨期間、產能爬坡、良率與製造範圍 | 台積電與 Intel 各有自己的路線圖和製造用語 | A16 實際量產產品，以及可比較的客戶與產出資料 |
| 5. 供應商資格與財務轉換 | 哪個工具、材料或 IP 通過哪個客戶、哪個步驟，並形成多少生意 | 雙向資格、重複出貨、份額、價格、收入、毛利與現金流 | 外部設備商已有具名產品；台灣公司映射仍未證 | 客戶與節點對應、出貨分母及可辨識財務結果 |

五個時鐘不是五個分數。設計研究可能領先，製程控制仍在收斂；晶圓廠可能公布量產計畫，
供應商財務卻還沒有足夠證據。閱讀時只升級被新文件直接支持的那一格，其他格維持原狀。

## 從成功開機到買得到產品：把第 4 個時鐘再拆九道門

產品時鐘很像新餐廳開幕：廚房圖紙完成、第一次試菜、開始備料、正式開門、每天穩定出餐，
是五件不同的事。半導體新聞裡的 PDK、tape-out、powered-on、production、launch 與
availability 也不能壓成一句「已量產」。Panther Lake 正好提供一條具名、可按日期回查的例子：

| 公告日期 | 文件直接支持的里程碑 | 當時仍不能推出 |
|---|---|---|
| 2024-08-06 | Intel 18A PDK 1.0 已釋出；Panther Lake 與 Clearwater Forest 已在流片後上電並啟動作業系統 | 2025 生產與首位外部客戶流片仍是預期，不是已發生結果 |
| 2025-10-09 | Intel 把 Panther Lake／Core Ultra Series 3 稱為首個 18A client 產品，並表示已在 production | 首批 SKU 出貨與 2026 年 1 月廣泛上市在該公告仍是後續時程，沒有 wafer、yield 或 unit 分母 |
| 2026-01-05 | Intel 正式 launch Series 3，列出 1 月 6 日預購、1 月 27 日起全球系統供應，並稱有 200-plus designs | design 是品牌整機規劃，不是已售系統、處理器出貨或外部 foundry 客戶數 |
| 2026-08-23 查得 | Intel ARK 在 Panther Lake 代號下列 17 個產品：15 個標 Q1'26、2 個標 Q2'26 | 這是當日 SKU 索引，不是 17 個獨立客戶、17 顆銷量或通路庫存 |

這條時間線證明的進步很具體：同一具名內部產品已從早期矽開機，走到 production、處理器上市
與終端系統可供應。它沒有證明的也同樣重要：2024 年文件只說首位外部客戶「預計」流片；後三份
產品資料都在談 Intel 自己的產品。因此，**Intel 內部產品跨過產品門，不等於外部晶圓代工客戶已跨過
採用門**。

### 九道門逐一蓋章，缺的不要替公司補

| 產品時鐘的九道門 | 它回答什麼 | Panther Lake 本輪位置 | 下一份能升級的證據 |
|---|---|---|---|
| 1. PDK 可用 | 設計端是否拿得到規則、模型與流程 | PDK 1.0 已公布 | 外部設計完成 signoff 的版本與日期 |
| 2. 設計流片 | 設計資料是否已送入製造 | 兩個 Intel 內部 lead products 已流片 | 具名外部客戶與產品 tape-out |
| 3. 首次上電／開機 | 首批矽能否通電並執行基本功能 | 2024 年已 powered-on／booted | 多顆、跨 lot 的功能與 qualification 分布 |
| 4. Production／爬坡 | 產線是否開始製造並提高產量 | Intel 2025 年稱 Panther Lake 已在 production | wafer starts、good die、yield 與爬坡曲線 |
| 5. 處理器 SKU 上市 | 是否有具名可銷售處理器 | 2026 年正式 launch；ARK 有具名 SKU | 持續供貨、產品組合與實際 unit shipment |
| 6. 終端系統可供應 | OEM 整機是否能讓客戶取得 | 公告 1 月 27 日起全球供應 | 地區／通路庫存、sell-through 與重複訂單 |
| 7. 穩定量與品質 | 重複生產是否維持良率與 field quality | 公開資料不足 | wafer／lot／unit、returns、failure-rate 與 reliability |
| 8. 外部 foundry 客戶 | 第三方設計是否真的採用同一製程 | 2024 年只有未具名、前瞻的 tape-out 預期 | 具名客戶、產品、production 與出貨共同鍵 |
| 9. 供應商與財務 | 哪個工具／材料通過資格並形成多少生意 | 台灣公司仍未證 | 雙向 qualification、出貨、價格、收入與毛利 |

這九道門不是規定每家公司只能依固定順序公告；它們是防止讀者把不同動詞混用的查核表。
例如 production 可以早於公開 SKU，OEM design 也可能在處理器上市前啟動；但後一格的新聞不能
回頭替前一格補出沒公布的 yield、units 或客戶身分。

### 同一個 Panther Lake，還要分 tile、SKU 與 OEM system

Intel 的架構簡報把三種 Panther Lake 配置的 compute tile 都標為 Intel 18A，PCD 都標為 External；
GPU tile 則分成兩條路：8-core 與 16-core／4Xe 版本標 Intel 3，16-core／12Xe 版本標 External。
這代表「一款 18A 產品」是封裝／平台層描述，不是「封裝內每片矽都由 18A 製造」；文件也沒有說
External tile 的晶圓廠與節點。再往市場走，ARK 的 17 個 SKU 是處理器型號，Intel 所稱
200-plus designs 是品牌整機設計，最後消費者買到的才是筆電或 edge system。三個分母不能互換：

| 物件分母 | 最少要記什麼 | 最常見的錯譯 |
|---|---|---|
| Tile／製程 | compute、GPU、controller 各用什麼節點與供電架構 | 一個產品用 18A＝每個 tile 都用 PowerVia |
| Package／處理器 SKU | 哪些 tile 組合、封裝、型號與 launch date | 17 個 SKU＝17 個客戶或 17 顆出貨 |
| OEM system design | 品牌、機種、地區、上市／取消狀態 | 200-plus designs＝200 多台已售系統 |
| Unit／wafer／lot | 生產、出貨、銷售、退貨與良率的數量及期間 | available／production＝高良率且大量 sell-through |

因此讀具名產品時，至少保存八欄產品證據護照：**node 與版本、tile 身分、package／SKU、內部或
外部客戶、里程碑動詞與日期、availability／地區、unit／wafer／lot 與品質分母、技術歸因及供應商
財務共同鍵**。最後一欄要把 RibbonFET、PowerVia、Foveros、其他 tile、軟體與系統設計分開；
平台效能再好，也不能在沒有共同對照時全算給 PowerVia。

**較強的多方版本**是 Intel 內部產品之後，至少一個具名外部 foundry 客戶也能從 tape-out 走到
production、SKU／system availability，並公開跨 wafer／lot 的 good-die yield、unit shipment、
returns／field quality；同一期間又能由設備或材料商雙向核對 qualification、出貨與財務分母。

**較強的空方版本**是 18A 主要由 Intel 內部產品承接，外部客戶長期停在未具名或 tape-out 階段；
同時 SKU 與 OEM design 很多，卻沒有穩定 units、yield、sell-through 或 field-quality 證據。多晶粒
產品還會讓 platform 成果混合 18A compute tile、外部 tiles、封裝與系統設計，削弱 PowerVia 單一歸因。

本輪有 N＝5 份 Intel 官方來源紀錄，但全屬 N＝1 條公司消息鏈與 N＝1 個具名 client 產品家族，
不是五個獨立客戶或五次獨立量產實驗。17 是 2026-08-23 當日 ARK 完整列示的 SKU census，
200-plus 是 Intel 公告的 design 數；兩者都不是抽樣，也不是出貨。具名外部 foundry 客戶產品、
wafer／lot／good-die yield、unit shipment、sell-through、returns／field quality、PowerVia 增量貢獻與
供應商財務共同觀測皆 N＝0，因此沒有可報的 sampling SE／t，也不判斷估值、價格或市場是否反映。

## 看到百分比，先填八格比較護照

背面供電常以「壓降少幾倍、速度快幾％、面積省幾％」登上標題。這些數字不是不能用，
而是每個數字都要連著它的比較條件一起讀。最短做法是先填八格；公開文件少一格，就把
結論留在該文件的受測範圍，不替它補成跨廠排名。

| 八格比較護照 | 要記下什麼 | 少了會讀錯什麼 |
|---|---|---|
| 1. 受測物與成熟度 | 模擬、測試結構、試驗晶片、CPU core，還是客戶量產產品 | 把研究結果當成量產產品表現 |
| 2. 比較基準 | N2P、前側供電版本、內部試驗節點，或另一個參考設計 | 把不同世代與不同電晶體一起算成背面供電貢獻 |
| 3. 固定條件 | 相同 Vdd、相同速度、相同功耗，還是固定電源接點間距 | 把本來互斥的 PPA 選項相加 |
| 4. 輸出指標 | 靜態 IR drop、動態下陷、頻率、功耗、單元利用率、已佈線面積或晶片密度 | 把不同單位都叫做「效能」 |
| 5. 工作負載與活動 | 實際工作負載、活動向量、統計最壞情境，或沒有公開 | 以一組切換狀態代表所有 AI／HPC 負載 |
| 6. 空間與時間視窗 | 單一熱點、區塊、全晶片；平均、峰值、最壞值或哪段瞬態 | 把局部峰值改善當成整顆晶片平均改善 |
| 7. PDN 與環境邊界 | 只算晶片，還是含封裝、板級、電容；使用哪組 PVT 與熱條件 | 把 on-die 結果當成整個平台供電結果 |
| 8. 共同取捨與歸因 | 面積、速度、功耗、溫度、debug、可靠度是否同時量；改善能否拆給單一結構 | 把「最高」選項當成零代價且全由背面供電造成 |

### 四組官方數字，應該怎麼讀

| 文件中的結果 | 護照中已知的關鍵條件 | 仍不能推出 |
|---|---|---|
| 台積電 A16：相對 N2P，同 Vdd 下速度增 8–10%；同速度下功耗降 15–20%；晶片密度最高 1.10 倍 | 比較基準與三個不同控制條件有公開；受測技術同時包含 nanosheet transistor 與 Super Power Rail | 三項同時全拿、全部改善都由背面電軌造成，或 A16 已是具名客戶量產結果 |
| Intel 2023 PowerVia：單元利用率超過 90%、platform voltage droop 改善超過 30%、頻率增益 6% | 受測物是內部試驗節點上的 product-like test chip，且 PowerVia 與 RibbonFET 分開驗證 | 等同 18A 客戶量產產品，或可直接和 A16 roadmap 百分比相比 |
| Intel 2026 VLSI 更新：已佈線面積少 11%、動態下陷降低 10 倍，對應最高 6% 頻率提升「或」超過 15% 動態功耗降低 | 公開基準為可比的前側互連技術，也明示頻率與功耗是兩個取捨方向 | 6% 與 15% 同時保證、適用所有工作負載，或證明跨晶圓廠領先幅度 |
| IBM 模擬研究：固定接點間距和固定 IR drop 會得到不同答案；面積、延遲與壓降又依參考設計及活動條件改變 | 方法明示固定量、模型與 reference-design dependence | 把模擬中的最高改善值當成 A16／18A 實體晶片規格 |

這四組資料沒有互相否定，因為它們回答的問題不同。尤其「10 倍降低」不能拿來除以
「30% 改善」後宣稱新結果好幾十倍；兩者的受測物、基準、量測定義與活動條件沒有被
公開對齊。百分比只是答案，八格才是問題本身。

### 靜態 IR drop 和動態下陷，差在時間

靜態 IR drop 可以先用 `電壓降 ≈ 電流 × 電阻` 理解：金屬或接點越窄、越長、電阻越高，
同一電流走過去就損失更多電壓。降低 nTSV 到電源軌的接點電阻，確實能改善這條局部路徑，
但還沒有回答整顆晶片哪裡在何時切換。

動態下陷則發生在大量元件短時間切換時。除了 `I×R`，還要面對電流變化速度與路徑電感的
`L×dI/dt`；完整時間域分析還會追蹤電阻、電感、電容與每個時間點的狀態。因此工作負載、
活動向量、封裝和板級路徑、去耦電容、時間視窗都會改變答案。只看到「IR drop 改善」時，
第一個問題應是它量靜態還是動態，第二個才是改善多少。

最後還要把電壓結果接回速度、功耗與可靠度。同一供電改善可以拿來提高頻率，也可以留作
電壓裕量或降低功耗；文件若寫「或」，讀者就不能改成「且」。這也是為什麼降低接點電阻、
降低動態下陷與提升產品頻率是三個相接但不可互換的證據節點。

## 同樣少掉 30mV，不同 Vdd 不是同一個風險

壓降一定要有起點與終點。NIST 的 SI 關係給出 1V＝1W/A、1Ω＝1V/A；在直流等效路徑中，
可把它重排為功率 P＝V×I、壓降 ΔV＝I×R、路徑焦耳損耗 P_loss＝I²R。這些只是量綱一致的
算術，不會替晶片設計者補出真實工作負載、分散金屬網路或允收門檻。

先只固定相同的 30mV 絕對壓降，分母不同就得到不同相對裕量：

| 假想負載端工作電壓 | 相同絕對壓降 | 壓降÷工作電壓 | 這一列還沒回答什麼 |
|---:|---:|---:|---|
| 0.75V | 30mV | 4.000% | 沒有電流、路徑、時間、工作負載與允收門檻 |
| 0.50V | 30mV | 6.000% | 不能因百分比較高就推產品一定失效 |

所以 mV 與百分比不是兩筆可相加的成績：前者是分子，後者還需要同一參考點的供電電壓。
若一份文件從調壓器量、另一份從晶片電源軌量，即使都寫 30mV，也不是同一條路。

### 再固定負載功率與路徑，電流才會浮出來

下面再做一個刻意簡化的直流教材：假設負載端都真正收到 100W，指定參考點之間的等效路徑
電阻固定 0.2mΩ，並把負載端電壓分別設成 0.75V 與 0.50V。先用 I＝P_load÷V_load 求總電流，
再算路徑壓降與損耗。

| 假想負載端電壓 | 負載端功率 | 等效總電流 | 路徑壓降 | 壓降占負載端電壓 | 路徑焦耳損耗 | 假想來源端電壓 |
|---:|---:|---:|---:|---:|---:|---:|
| 0.75V | 100W | 133.333A | 26.667mV | 3.556% | 3.556W | 0.776667V |
| 0.50V | 100W | 200.000A | 40.000mV | 8.000% | 8.000W | 0.540000V |

在這組固定條件下，電壓由 0.75V 降到 0.50V，總電流與絕對壓降都變成 1.5 倍，I²R 損耗則
變成 2.25 倍。它不是「低電壓一定更熱」的產品結論：真實 CMOS 的動態功耗、頻率、活動、
漏電與電容都會隨工作點改變，100W 與 0.2mΩ 也都只是為了看懂量綱而設定的假想輸入。

本節有 N＝2 個固定 30mV 的電壓分母案例，另有 N＝2 個固定負載功率／等效電阻案例。
Python Fraction 與獨立 awk 在顯示精度內完全一致。這是確定性換算，不是抽樣、電路模擬、
晶片量測或跨公司 benchmark，因此沒有 sampling SE／t，也沒有 rail、via、die、wafer、lot、
產品、客戶、可靠度、冷卻、良率、成本、收入、毛利或公司效果。

### 平均電流過關，局部熱點仍可能失敗

等效總電阻適合做第一層核對，卻會抹平空間。IBM 的 3-D IC 研究指出，較大尺度 TSV 與全晶片
電源網路的接點會出現 current crowding，局部電流密度可能高於預期平均；只把 TSV 與線段當成
單一電阻，可能漏掉接點附近的 hotspot。這項機制提醒讀者要看分布，但研究對象不是 A16 或
PowerVia 的 nano-TSV，不能把任何倍數或壽命搬過來。

另一份 IBM ECTC 2025 摘要才直接研究 BSPDN chip package。它把 powered transistors 到 heat
sink 的路徑連到高熱阻的前側後段金屬堆疊，並指出採用不同 BEOL thermal-resistance model 時，
預測的 maximum hotspot temperature 會實質不同。兩篇同屬 IBM 研究鏈，回答的是電流分布與熱路徑
兩個不同問題，不是兩個獨立產品或量產 run。

| 要分開的帳 | 最少要保存什麼 | 只看平均值會漏掉什麼 |
|---|---|---|
| 負載與總電流 | 產品版本、rail、電壓、功率定義、頻率、活動與電流波形 | 同一平均功率下的瞬時電流峰值 |
| 分流與導體 | 金屬層、via／rail 數量、截面、材料、溫度與實際 current path | 少數窄路徑承擔較多電流 |
| 局部電流密度 | 平均、percentile、peak、位置與量測／模型解析度 | 轉角、接點和截面變化處的 current crowding |
| 電損地圖 | 各段 R／Z、I²R、動態損耗、空間與時間視窗 | 總損耗相同但熱源位置不同 |
| 熱路徑與熱點 | 晶片—封裝堆疊、熱參考面、散熱介面、冷卻邊界、熱阻模型與溫度分布 | 平均溫度正常但局部最高溫失敗 |

### 多空小作文共用的電力—熱十欄護照

| 護照欄位 | 必須固定什麼 | 少了最容易誤讀成什麼 |
|---|---|---|
| 1. 產品與 rail | 試驗晶片／具名產品、版本、Vdd／Vss rail 與調壓器—封裝—晶片—電晶體參考點 | 不同位置的電壓可以直接比較 |
| 2. 工作點 | 製程角落、電壓、頻率、溫度、工作負載、活動向量與時間視窗 | 一個典型點代表所有 PVT 與 AI／HPC 負載 |
| 3. 功率分子 | 負載收到、來源輸入、路徑損耗、dynamic、leakage 或整顆產品功率 | 把 100W 負載和 100W 來源當成同一件事 |
| 4. 電流分母 | total／rail／branch、平均／RMS／peak、waveform 與量測帶寬 | 平均安培數替瞬時與局部峰值背書 |
| 5. 路徑模型 | on-die／package／board 邊界、distributed RLC、contact 與去耦電容 | 一個等效 R 代表所有頻率與空間位置 |
| 6. 導體身分 | 金屬／via／rail 的材料、幾何、截面、長度、溫度與製程分布 | 金屬較寬就自動得到完整產品改善 |
| 7. 電流密度 | 分流、mean／percentile／peak、current crowding、解析度與位置 | 總電流合格就代表每個接點都安全 |
| 8. 壓降與電損 | mV 與 rail 百分比、static／dynamic、I²R／其他損耗及最壞位置 | 只報一個百分比就能解釋速度和熱 |
| 9. 熱與可靠度 | 功率地圖、BEOL／package 熱阻、hotspot、冷卻邊界、時間、電遷移與失效分布 | 平均溫度或模型通過等於產品壽命通過 |
| 10. 量產與商業 | die／wafer／lot、重複性、good-product yield、throughput、成本、qualification、供應商與財務 | 電力—熱機制直接跳成設備材料訂單與毛利 |

**較強的多方版本**不是「背面金屬較寬，所以功耗和熱一定一起下降」，而是同一具名產品在相同
工作量下，從來源端到電晶體端都能重建電流、壓降、局部電流密度、損耗與溫度分布，並在重複
wafer／lot、可靠度與成本下守住較好的產品裕量；供應商還要能對上實際解決的步驟與財務分子。

**較強的空方版本**也不是「IBM 提到 hotspot，所以背面供電不可量產」，而是低阻與釋放正面佈線的
收益，被局部 current crowding、熱路徑、薄化／接合／量測成本、debug 或可靠度 guard band 吃掉；
若完整產品只把技術裕量換成更高頻率而未降低每顆合格成本，供應鏈價值量就可能低於題材敘事。

## 先用五個位置看 BPR＋nTSV 的「送訊號」和「送電」範例

以下只示範 imec 公開的 BPR＋nTSV 路徑，方便先看懂一條電力接力；它不是所有背面供電的共同剖面。

| BPR＋nTSV 範例五個位置 | 它負責什麼 | 和下一位置怎麼接 | 主要工程問題 | 不能直接推成 |
|---|---|---|---|---|
| 1. 正面訊號佈線 | 在晶片正面傳送資料與控制指令 | 由前側金屬與接點接近電晶體 | 訊號線仍要守住延遲、干擾與佈線空間 | 正面空間增加，不等於整顆晶片效能一定提升 |
| 2. 背面金屬網路 | 從晶圓背面分配電力 | 把電力送到背面導通孔 | 要控制金屬電阻、熱、應力與整合一致性 | 有背面金屬需求，不等於具名材料已被採用 |
| 3. imec 範例的 nTSV | 穿過薄化後的矽，連接背面與元件附近 | 向下接背面金屬，向上接埋置電源軌 | 孔徑、深度、疊對、圓角、接觸面積與填孔缺陷都要受控 | imec／Lam 的研究結構不等於所有量產流程採同一規格 |
| 4. 此範例的 BPR | 在電晶體下方接收並分配電力 | 讓背面導通結構更靠近電晶體 | 要和元件、材料、設計規則一起整合 | 只在此路徑中是必要中繼，不等於每一種背面供電都需要 BPR，也不等於某家 IP 或材料商已有收入 |
| 5. 電晶體 | 接收電力並依訊號執行開關與運算 | 同時接上供電與訊號，但兩者來自不同路徑 | 最後仍要驗證電壓、速度、應力、良率與可靠度 | 單一結構成功，不等於完整產品可穩定量產 |

這五個位置不是一張完整晶片設計圖，而是 BPR＋nTSV 範例的最短路徑：訊號主要留在正面，
電力則從背面金屬經導通孔與埋置電源軌接近電晶體。實際結構會因晶圓廠而異，不能用 imec
的一般流程替台積電或 Intel 補上未公開的尺寸、材料、工具與供應商。

## 都叫背面供電，孔卻不一定接到同一站

上表畫的是容易入門的 **BPR＋nTSV 路徑**，不是所有背面供電的共同剖面。可以把晶片想成一棟
地下室進電的大樓：有一種電梯先停在地下總電源軌，再由短支線送進房間；另一種拉長電梯到
前側金屬；還有一種直接停在元件端子。它們都從背面進來，卻不是同一個孔、同一個終點或
同一套施工順序。

最安全的做法，是先分開記錄三個在實際流程中可能彼此耦合的面向，而不是把縮寫排成
「舊世代→新世代」。公開案例只證明部分組態，不代表三個面向能任意組合、都做得出來，
或具有相同的成本與可靠度：

| 三軸連接護照 | 先問什麼 | 公開研究中的例子 | 少了最容易誤讀成什麼 |
|---|---|---|---|
| 1. 最後落點 | 垂直連接最後碰到 BPR、前側金屬、源／汲極外延區，還是接觸金屬？ | BPR＋nTSV、TSVM、BSC-E、BSC-M 的終點不同 | 都叫 backside via，所以電阻、面積與失效模式相同 |
| 2. 穿過什麼 | 孔主要穿過薄化後的剩餘矽，還是 STI 介電材料？ | nTSV 以穿矽命名；TDV 以穿介電層命名 | TDV 一定直接接到電晶體，或 nTSV／TDV 必然互相取代 |
| 3. 何時形成 | via 在元件、前側金屬、接合與薄化流程的哪個時間點做？BPR 是否先從正面形成？ | 公開案例各自呈現特定時序與落點，兩欄都要記 | 看過少數案例，就以為任意時序與落點搭配都可製造 |

### 五種公開寫法，哪一格其實還是空白

| 公開寫法 | 文件直接支持的連接方式 | 可以帶走的知識 | 仍不能替它補什麼 |
|---|---|---|---|
| imec BPR＋nTSV | 背面金屬經穿過剩餘矽的 nTSV 落到先做好的埋置電源軌 | BPR 是靠近元件的中繼電力幹線 | 試驗載具尺寸不能變成 A16／18A 規格 |
| imec TSVM | 較高的垂直連接接到前側 M0A 金屬側邊，不用 BPR 中繼 | 沒有 BPR 仍可形成背面連接研究路徑 | 研究比較不是任何晶圓廠已採用的量產配方 |
| imec BSC | BSC-E 直接接源／汲極外延區；BSC-M 接其接觸金屬 | 「直接」必須再寫清楚接到元件哪一層 | BSC-E／M／M* 不能因字面相近就改名成 SPR |
| imec via-first TDV | 先在正面 STI 內形成 via，薄化超過 STI floor 後從背面露出 | 此示範同時公開 TDV 的穿越介質與 via-first 形成時序 | TDV 名稱只說穿過介電層，不保證時序、只送電、直接接電晶體或取代 nTSV／BPR |
| 台積電 A16 SPR | 官方稱 novel backside direct contact，圖中標 VB；高階流程為 Device／F-BEoL→Bond→Flip→Si thinning→VB & B-BEoL | A16 已公開到「直接接觸」與製程接力層級 | VB 最後落點、BSC 變體、材料、孔徑、節距、電阻與量產窗口都未公開 |

這張表也修正一個常見直覺：**TDV、BPR 和 direct contact 不是三個互斥盒子。** TDV 主要描述
垂直結構穿過介電層，BPR 描述其中一個中繼落點，direct contact 描述接觸關係或是否省略
某些中繼節點；實際流程也可能同時含多種垂直連接。但現有公開案例只證明部分組態，沒有
完整剖面前，不能假設任意組合都可製造，也不能只靠名詞判定誰比較先進。

### A16 的官方資料，把哪個時鐘往前推了一格

2026 VLSI 官方場次摘要中，TSMC 作者表示 A16 平台技術已完成 development 與 qualification；
Technical Tipsheet／技術摘要則畫出上述接合、翻面、薄化與形成 VB／背面金屬的高階順序。這讓公開證據比「只有
roadmap 名稱」多了一層，卻仍是公司的平台資格主張：qualification 範圍沒有公開，不能改寫成
客戶認證、跨 wafer／lot 的量產良率，或截至 2026-08-24 已開始大量生產。兩份資料都使用
`slated for Q4'26`，所以正確動詞仍是「量產排定於 2026 年第四季」，不是「已量產」。

同一組資料把 A16 相對 N2P 的平台結果寫成：相同功耗下速度提高 8%–10%、功耗改善
15%–20%，以及額外 8%–10% 晶片密度，圖說把最高約 10% 的密度與速度改善連到某 ARM core
benchmark；公開資料未揭露該實作或樣本數。這三組百分比的主詞是同時包含 enhanced nanosheet、SPR 與設計共同最佳化的
**完整 A16 平台**；它們不能相加，也不能拆成「直接接觸單獨帶來多少」。公開資料沒有揭露
wafer、lot、die、實作數、工作負載明細、PVT、原始分布或量測／模擬分界，因而沒有可報的
sampling SE／t。

### 20 奈米看起來很具體，卻最容易被搬錯地方

imec 的 2025 via-first TDV 研究列出 20nm bottom diameter、120nm pitch；其 typical test
structure 又以 55nm 線寬的背面金屬配 20nm TDV bottom，留下 15nm **layout overlay margin**。最後一個
數字是版圖容許量，不是跨晶圓量到的 3σ 疊對分布。較早的 imec BPR／nTSV 路徑另有約
320nm 深、200nm pitch 的研究實作；這些數字回答各自 test structure 怎麼做，不回答 A16 的 VB
多大、落在哪裡或能否穩定量產。看到精確尺寸時，至少把「機構、載具、落點、穿越材料、
時序、量測定義」一起帶走；少一欄就不搬家。

**較強的多方版本**不是「A16 有 direct contact，所以所有背面設備材料都會受惠」，而是 Q4
計畫後真的出現具名客戶產品，並能以同一剖面對上落點、材料、幾何與接點電阻分布，再跨
wafer／lot 公開 good-die yield、可靠度與重複出貨；供應商端還要把同一步驟的 qualification、
交付與財務分子雙向核對。

**較強的空方版本**也不是「研究尺寸不同，所以 A16 做不出來」，而是市場把 imec 的 BPR／nTSV
或 TDV 尺寸直接貼到未公開的 A16 VB，並把完整平台 PPA 全歸因給 SPR；之後 Q4 計畫沒有轉成
可定位的產品、良率與出貨，或供應商只停在廣義能力。第一個反證因此是正式剖面與量產分母，
不是另一個更漂亮的縮寫。

本輪新增 N＝3 份官方來源紀錄：N＝2 份 VLSI／TSMC 文件屬同一家公司消息鏈，N＝1 份 imec
研究頁屬另一條研究機構鏈；再回查既有 N＝2 份 imec 機制／DTCO 文件。它們不是五個獨立
產品或量產實驗。目前尚無一份公開資料同時提供 A16 的落點、幾何、wafer／lot／die 分布、
良率、客戶與供應商財務共同鍵；本文只建立架構邊界，不做跨廠效能排名、公司受惠推估或投資動作。

## 再把背面加工排成六個製程步驟

| 本文六個步驟 | 在做什麼 | 主要接力角色 | 要驗收什麼 | 本輪可確認到哪裡 |
|---|---|---|---|---|
| 1. 完成前側元件與電源軌 | 先製作電晶體、前側連線與靠近元件的埋置電源軌 | 晶圓廠製程整合、設計規則與 IP | 元件、電源軌與後續背面連接位置能共同工作 | imec 說明一般機制；沒有 A16／18A 完整配方 |
| 2. 接到支撐載體 | 把製程晶圓固定，讓背面能在不破裂下繼續加工 | 晶圓接合設備、載體與接合材料 | 接合強度、翹曲、顆粒、應力與後續可加工性 | 一般流程可確認；沒有具名台灣供應商資格 |
| 3. 從背面把晶圓變薄 | 依序用研磨、平坦化與蝕刻移除背面矽 | 薄化、CMP、蝕刻設備與相關材料 | 剩餘厚度、平坦度、損傷、應力與蝕刻停止位置 | imec 與 Lam 說明薄化及應力機制；工具、規格與份額未證 |
| 4. 從背面重新找準位置 | 在接合、薄化甚至變形後，仍要對準前側電源軌並開出連接位置 | 對準、電子束量測、蝕刻與虛擬製程模擬 | 疊對誤差、邊緣位置、孔形、深度與缺陷 | Lam 顯示這些形貌會影響接點；Applied 有具名量測產品，A16／18A 實際工具未公開 |
| 5. 形成導通孔與背面金屬 | 在開孔中形成導電結構，再建立背面供電網路 | 沉積、填孔、金屬、清洗與材料整合 | 接觸面積、接點電阻、空洞、污染、熱預算與金屬一致性 | imec／Lam 提供研究路徑；量產材料與供應商未證 |
| 6. 驗證完整流程能重複生產 | 把電力完整性、良率、可靠度與產能一起驗收 | 晶圓廠、檢測量測、可靠度與客戶產品團隊 | 同一產品的電壓下陷、良率、失效分布、產出與長期可靠度 | 晶圓廠有各自里程碑，沒有共同量尺或供應商財務分母 |

六個步驟是製程接力，不是六家公司的固定分工。晶圓廠負責把整條流程整合起來，研究機構
提供一般機制與試驗路徑；設備、材料與設計服務商只有在具名產品、步驟與資格被雙向核對後，
才能從「研究入口」升級為「已證實角色」。

## 看懂一個失敗怎麼沿鏈條放大

```text
布局與幾何 → 微影／蝕刻形貌 → 對準與接觸面積 → 接點電阻 → 供電穩定性 → 電路速度、良率與可靠度
```

Lam 與 imec 的 nTSV／BPR 研究讓這條診斷鏈變得具體：如果孔和電源軌的疊對偏移，或蝕刻後
的圓角改變，實際接觸面積就可能變小；接點電阻隨之改變，電力送到電晶體的狀態也要重新
驗證。Lam 的另一份研究則提醒，薄化、背面金屬和導通結構還會改變電晶體附近的機械應力。

這條箭頭是找問題的順序，不是宣稱每次失效都由左向右單一發生，也不是各家晶圓廠的共同
量產配方。本文沒有同產品、同節點、同量測條件下的跨廠樣本，因此不能用它比較 A16、18A
或其他實作的速度、良率與可靠度高低。

## 把晶圓廠、製程控制與供應商時鐘分開

**晶圓廠時鐘回答「哪個節點走到哪裡」。** 台積電 2025 年報把 A16 描述為結合超級電源軌
的 N2 家族延伸，並規劃在 2026 下半年量產；截至本輪證據截止日，本文仍沒有 A16 已實際
量產或具名客戶產品的直接證據。Intel 則以自己的口徑表示 18A 已於 2025 年進入生產、
18A-P 在 2026 年 6 月進入風險生產。這些名詞都應留在各公司的時鐘，不能拿來排跨廠速度、
良率或商業勝負。

台積電 2026 年第二季法說又補上一個重要觀念：先進節點從技術與產品開發、準備產能到大量
生產，要經過多年的接力；公司也規劃在 2029 年把超級電源軌延伸到後續平台。這能證明背面
供電不是單一節點的一次性概念，卻不能反向證明 A16 已完成量產，也不能保證後續時程一定
照表發生。

**製程控制時鐘回答「結構能否穩定工作」。** imec／Arm 的設計技術共同最佳化研究比較了
不同背面連接方案；Lam／imec 則把疊對、圓角、接觸面積與接點電阻連在一起，並另外研究
薄化、背面金屬和導通結構帶來的機械應力。這些證據把問題從「有沒有孔」推進到「孔能否
在合理製程窗口內導電並維持可靠度」，但仍是研究結構與模型，不是 A16 或 18A 的公開量產
良率資料。

**供應商時鐘回答「哪個產品通過哪個客戶」。** Applied Materials 已把能力做成 PROVision 10
這項具名電子束量測產品，並表示有多家未具名的先進邏輯與記憶體晶片製造商使用。這比只說
「量測需求會增加」多了一層產品證據；可是文件沒有把客戶、節點、背面供電資格、台數與
收入逐一對上，因而不能建立台灣設備商映射，也不能把外部設備產品存在寫成 universe 公司
已取得訂單。

## 最後用七關把製程需要接回公司

| 本文七關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 架構問題成立 | 前側佈線壓力、電壓降等問題值得改變供電路徑 | imec 說明背面送電、前側送訊號的目的與一般機制 | 同產品的基準設計與背面供電設計比較 | 架構目的不能直接當成整顆產品效能提升 |
| 2. 設計與試驗晶片可行 | 設計規則、電力完整性與連接選擇能在晶片層級一起工作 | imec／Arm 比較多種連接方案與標準單元、區塊取捨 | 具名晶圓廠與客戶產品的試驗晶片實測 | 研究設計不能直接當成量產產品 |
| 3. 完整流程與接點導通成立 | 接合、薄化、對準、開孔、金屬與接點能串成可導通流程 | imec 的一般流程與 Lam 的接點研究支持工程鏈條 | 實體晶圓的截面、電阻分布與重複結果 | 模擬或單一研究結構不能替代量產配方 |
| 4. 製程窗口與可靠度通過 | 疊對、形貌、電阻、應力、良率與可靠度能穩定受控 | Lam 說明接點和應力機制；Applied 有具名量測產品 | 同一節點的製程窗口、失效分布、長期可靠度與良率 | 工具可量測不等於節點已通過資格 |
| 5. 具名節點與客戶產品量產 | 晶圓廠把架構放進具名節點，客戶產品穩定大量生產 | 台積電有 A16 計畫；Intel 公布 18A 家族各自里程碑 | A16 實際量產、具名客戶產品、爬坡與製造範圍 | 公司自定的 production 用語不能跨廠排名 |
| 6. 供應商資格與重複出貨 | 同一工具、材料或 IP 通過同一客戶與步驟，並持續交付 | Applied 有具名產品，但客戶、節點與資格未對上；台灣公司未證 | 晶圓廠與供應商雙向文件、合格清單、台數／用量與期間 | 具名產品、試驗或一次出貨不等於量產份額 |
| 7. 財務結果可以歸因 | 出貨能接回份額、價格、收入、成本、毛利與現金流 | 沒有任何台灣公司可辨識的背面供電財務貢獻 | 同期間的訂單、收入、毛利與收款分母 | 題材熱度、股價或廣義先進製程營收不能代替財務證據 |

本輪可把技術機制推到第三關，並為第四關建立明確量測項目；晶圓廠端在第五關各有不同口徑，
外部設備商在第六關之前已有具名產品，台灣公司映射則仍停在待驗證。七關是證據排序，不是
公司成熟度分數、供應商名單、營收預測或投資排名。

## 這篇對公司判斷的用處與界線

設備研究可以沿著接合、薄化、CMP、蝕刻、對準、量測、沉積與金屬流程尋找具名資格；材料
研究可以追埋置電源軌、蝕刻停止層、導通孔填充與背面金屬；IP 與設計服務則要追新 PDK、
共同最佳化、客戶採用與授權收入。這些都是「去哪裡找證據」，不是「已經找到受惠公司」。

如果新公告只說公司具備薄化、蝕刻或量測能力，最多只能建立能力節點；推出具名產品，也仍要
在第六關補上客戶與製程資格。真正能升級公司信心的資料，必須把同一製程、具名產品、客戶
認證、量產出貨與財務結果串在一起；在此之前，本文不支持個股排序、營收推估或投資動作。

## 來源與證據邊界

- [TSMC 2025 Annual Report](https://investor.tsmc.com/static/annualReports/2025/english/index.html)（A16 roadmap 與量產時程）。
- [Intel Foundry 2026 VLSI update](https://newsroom.intel.com/intel-foundry/intel-foundry-details-process-milestones-future-innovation-at-vlsi-symposium)（18A 與 18A-P 製造里程碑）。
- [imec backside power delivery](https://www.imec-int.com/en/articles/how-power-chips-backside)（BPR、晶圓薄化、nTSV 與整合流程）。
- [TSMC A16 Technology](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_A16)（持續更新的 A16 技術頁，只作路線圖追蹤入口）。
- [Intel Foundry Newsroom](https://newsroom.intel.com/intel-foundry)（持續更新的 Intel 製程公告入口）。
- [Lam Research：Optimizing the Nano-TSV-to-BPR Connection](https://newsroom.lamresearch.com/optimizing-the-nano-tsv-to-bpr-connection-in-backside-power-networks?blog=true)（疊對、圓角、接觸面積與接點電阻）。
- [TSMC 2Q26 Earnings Conference Transcript](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/547d1696765e05ce3adb81c108ce1c8c1682b80c/TSMC%202Q26%20Transcript.pdf)（節點開發至量產的長交期，以及後續超級電源軌路線圖）。
- [imec：Backside power delivery options—A DTCO study](https://www.imec-int.com/en/articles/backside-power-delivery-options-dtco-study)（多種連接方案與設計、製程共同最佳化）。
- [Applied Materials：PROVision 10](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unveils-next-gen-chipmaking-products/)（具名電子束量測產品與未具名晶片製造商使用範圍）。
- [Lam Research：Transistor Channel Stress in Backside Power Delivery Networks](https://newsroom.lamresearch.com/transistor-channel-stress-backside-power-delivery-networks)（薄化、背面金屬、導通結構與機械應力）。
- [TSMC 2024 North America Technology Symposium](https://pr.tsmc.com/english/news/3136)（A16 相對 N2P 的同 Vdd、同速度與密度三組條件式指標）。
- [Intel：PowerVia Test Shows Industry-Leading Performance](https://newsroom.intel.com/client-computing/powervia-test-shows-industry-leading-performance)（內部試驗節點、product-like test chip 與三組結果的成熟度邊界）。
- [Synopsys：What is Voltage Drop?](https://www.synopsys.com/glossary/what-is-voltage-drop.html)（靜態與動態壓降、活動向量及時間域分析方法）。
- [IBM Research：Methodology Development to Benchmark Power Delivery Designs](https://research.ibm.com/publications/methodology-development-to-benchmark-power-delivery-designs-in-advanced-technology-nodes)（pre／post-PDK 與 reference-design dependence）。
- [IBM Research：Comprehensive BEOL Performance Assessment](https://research.ibm.com/publications/comprehensive-beol-performance-assessment-interconnects-optimized-for-signal-routing-and-power-delivery-in-advanced-cmos-technology-nodes-invited)（固定接點間距、固定 IR drop、驅動與活動條件的差異）。
- [NIST：SI Units—Electric Current](https://www.nist.gov/pml/owm/si-units-electric-current)（volt、watt、ampere 與 ohm 的量綱關係）。
- [IBM Research：DC current crowding in TSV-based 3-D connections](https://research.ibm.com/publications/analysis-and-modeling-of-dc-current-crowding-for-tsv-based-3-d-connections-and-power-integrity)（平均與局部電流密度、單電阻模型及 hotspot 邊界）。
- [IBM Research：BSPDN 與 chiplet 的 BEOL thermal resistance](https://research.ibm.com/publications/fast-and-accurate-machine-learning-prediction-of-back-end-of-line-thermal-resistances-in-backside-power-delivery-and-chiplet-architectures)（BSPDN chip-package 熱路徑與 maximum-hotspot model sensitivity）。
- [Intel Foundry：Intel Foundry Achieves Major Milestones](https://newsroom.intel.com/intel-foundry/intel-foundry-achieves-major-milestones)（PDK 1.0、內部產品流片後開機與當時仍屬前瞻的外部客戶里程碑）。
- [Intel：First AI PC Platform Built on 18A](https://newsroom.intel.com/client-computing/intel-unveils-panther-lake-architecture-first-ai-pc-platform-built-on-18a)（Panther Lake 由開機走到 production，以及當時尚待發生的 SKU 出貨／上市時程）。
- [Intel：Core Ultra Series 3 Debut](https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a)（launch、預購、終端系統可供應與 200-plus OEM-design 公司主張）。
- [Intel：Panther Lake Architecture Recap](https://cdrdv2-public.intel.com/866361/ITT_2025_Panther_Lake_Recap1.pdf)（pp.27–29 的 compute／PCD／GPU tile 製程配置差異）。
- [Intel ARK：Products formerly Panther Lake](https://www.intel.com/content/www/us/en/ark/products/codename/237132/products-formerly-panther-lake.html)（2026-08-23 查得的 17 個 SKU 與 launch-quarter 索引）。
- [2026 VLSI Symposium：TSMC A16 session](https://vlsi26.mapyourshow.com/8_0/sessions/session-details.cfm?ScheduleID=246)（backside direct contact、平台 development／qualification、N2P 比較與 Q4'26 計畫）。
- [2026 VLSI Technical Tipsheet](https://www.vlsisymposium.org/wp-content/uploads/2026/04/2026-VLSI-Technical-Tipsheet-REVISED-FINAL-4.25.26-1-1.pdf)（p.4 的 A16 SPR／VB 高階流程、截面示意與 ARM core benchmark）。
- [imec：The path to high-density front- and backside wafer connectivity](https://www.imec-int.com/en/articles/path-high-density-front-and-backside-wafer-connectivity)（via-first TDV、STI 介電層、typical test structure 幾何與 layout-margin 邊界）。

本篇明列二十六份一手文件或官方頁面，分開建立技術機制、連接架構、量測比較、設計取捨、電力—熱邊界、
製程控制、晶圓廠路線圖、外部具名設備產品與 Intel 具名內部產品時鐘。它們沒有提供跨公司共同
良率、具名外部 foundry 客戶、處理器出貨、設備台數、供應商份額、價格或財務分母，也沒有一致
預期、估值或即時部位資料，因此本文不判斷題材是否已反映。
台積電是觀察層公司；Applied Materials 與 Lam Research 只作外部能力和產品錨點。不能因
它們出現在技術鏈，就把 universe 內設備、材料或 IP 公司自動連成供應鏈。

## 影響路由

<!-- impact
group_id: semiequip
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-16
rationale: 晶圓薄化、接合、背面對準、蝕刻、金屬與製程控制形成設備研究路由，但仍缺具名供應商資格與財務證據
evidence_boundary: 技術流程的必要性不證明任一 universe 公司已供貨、取得份額或增加獲利
-->

<!-- impact
group_id: material
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-16
rationale: BPR、nTSV、蝕刻停止層與背面金屬涉及材料整合問題，值得追蹤晶圓廠與材料商的具名 qualification
evidence_boundary: imec 研究流程不是台積電或 Intel 的完整量產配方，也沒有列名台灣材料供應商
-->

<!-- impact
group_id: ipdesign
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-16
rationale: 背面供電需要設計技術共同最佳化與新 PDK，但目前沒有 universe 公司具名 IP、客戶採用或授權收入證據
evidence_boundary: PDK 與 DTCO 需求不等於本地 IP／ASIC 設計服務商已有可辨識財務曝險
-->

## 下一個可證明／否定的節點

- 台積電正式公開 A16 SPR／VB 剖面，逐欄說明落點、穿越材料、via 形成時序、幾何分布與接點電阻，而不是由 imec BSC／TDV 替它補值。
- 同一 frontside／backside 產品版本公開八格比較護照，並同時提供靜態 IR drop、動態下陷、PPA、熱、可靠度與原始分布。
- 同一產品從調壓器、封裝、晶片 rail 到電晶體端公開電壓／電流參考點、distributed RLC、局部 current-density、loss map、thermal stack 與 hotspot distribution。
- 同一具名試驗晶片或客戶產品，同時公開設計取捨、接點電阻、電力完整性與可靠度結果。
- 台積電正式確認 A16 實際進入量產，並提供至少一個客戶產品、爬坡、良率或製造範圍。
- Intel 將 18A／18A-P 連到具名外部晶圓代工客戶產品與可定位出貨，而不只停在公司製程里程碑。
- 量測、蝕刻、薄化、接合或材料商揭露同一背面供電步驟的具名客戶資格與重複出貨，且由晶圓廠端交叉核對。
- 台灣公司只有在供應商產品、節點、資格、期間與財務分母都對上時才升級；一般能力、合作或題材熱度仍維持未證。
