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
- **超級電源軌（Super Power Rail）**：台積電 A16 的背面供電實作名稱；名稱本身不公開完整流程、工具或供應商。
- **背面供電導通（PowerVia）**：Intel 18A 家族的背面供電實作名稱；不能因名稱相近就假設和台積電採相同結構。
- **A16／A12**：A16 是台積電規劃結合超級電源軌、並把量產排在 2026 下半年的具名製程；A12 是公司規劃於 2029 年把同一供電方向延伸到 A14 平台的後續節點，不代表 A16 已實際量產。
- **N2P**：台積電 N2 家族的延伸製程，也是公司公開 A16 速度、功耗與密度指標所用的比較基準；比較 A16 和 N2P 不能自動拆出背面電軌的單獨貢獻。
- **Intel 18A**：Intel 表示已於 2025 年進入生產的製程；本文不把這個里程碑與其他晶圓廠的量產用語直接排名。
- **Intel 18A-P**：Intel 18A 家族的延伸製程；Intel 於 2026 年 6 月表示它已進入風險生產。
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
- **設計技術共同最佳化（DTCO）**：設計與製程一起調整，讓電源、訊號、面積與製造限制能相互配合。
- **風險生產**：製程已進入早期製造驗證，但仍不是成熟大量生產、外部客戶採用或穩定良率的同義詞。
- **量產計畫**：公司對未來進入大量生產的時程安排；計畫不等於截至目前已完成量產。
- **客戶資格認證（Qualification）**：客戶依功能、可靠度與製造條件確認工具、材料或產品是否可採用。
- **良率**：投入製造後能成為合格品的比例；沒有共同產品與製程分母時，不能跨廠直接比較。
- **雙向核對**：同一具名製程、工具或材料同時能由晶圓廠端與供應商端文件互相對上。
- **財務足跡**：能在出貨、收入、毛利或現金流中辨識的結果；只看到技術需要或合作公告還不算。
- **電力完整性**：電力送到各處電晶體時，電壓與電流仍維持在設計可接受範圍的程度。
- **電壓降（IR drop）**：電流通過有電阻的路徑後造成的電壓損失；線路和接點都會影響它。
- **靜態 IR drop**：在近似固定電流下觀察供電路徑的直流壓降；核心關係是電流乘上電阻。
- **動態／瞬態電壓下陷**：大量電晶體短時間切換時，供電因電流驟變與路徑阻抗短暫下降；它和靜態 IR drop 不是同一種量測。
- **工作電壓（Vdd）**：供應給電晶體的正電源電壓；「相同 Vdd」表示比較時先把這個條件固定。
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
- 再查它量的是哪個失效位置：對準、接觸面積、接點電阻、電力完整性、應力、良率或可靠度。
- 遇到「提升幾％」時，先填完受測物、基準、固定條件與量測範圍；百分比沒有共同分母就不跨公司排名。
- 最後要求晶圓廠端與供應商端雙向核對同一產品與期間，並補上資格、出貨、份額、價格與財務結果。

### 想一想

- 晶圓確實需要變薄，為什麼仍不能直接推論某一家薄化設備商會增加獲利？
- 如果晶圓廠已進入生產，而外部供應商只推出具名量測產品但沒有節點資格，應上調哪一個時鐘？
- 同一道製程由不同晶圓廠以不同名稱實作時，哪些資料可以比較，哪些必須留在各自的成熟度時鐘？
- 「動態電壓下陷降低 10 倍」和「電壓下陷改善超過 30%」看似衝突；在知道受測物、基準與活動向量前，為什麼其實不能比較？

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

## 先用五個位置分開「送訊號」和「送電」

| 本文五個位置 | 它負責什麼 | 和下一位置怎麼接 | 主要工程問題 | 不能直接推成 |
|---|---|---|---|---|
| 1. 正面訊號佈線 | 在晶片正面傳送資料與控制指令 | 由前側金屬與接點接近電晶體 | 訊號線仍要守住延遲、干擾與佈線空間 | 正面空間增加，不等於整顆晶片效能一定提升 |
| 2. 背面金屬網路 | 從晶圓背面分配電力 | 把電力送到背面導通孔 | 要控制金屬電阻、熱、應力與整合一致性 | 有背面金屬需求，不等於具名材料已被採用 |
| 3. 奈米級背面導通孔 | 穿過薄化後的矽，連接背面與元件附近 | 向下接背面金屬，向上接埋置電源軌 | 孔徑、深度、疊對、圓角、接觸面積與填孔缺陷都要受控 | imec／Lam 的研究結構不等於所有量產流程採同一規格 |
| 4. 埋置電源軌 | 在電晶體下方接收並分配電力 | 讓背面導通結構更靠近電晶體 | 要和元件、材料、設計規則一起整合 | 電源軌是必要元件，不等於某家 IP 或材料商已有收入 |
| 5. 電晶體 | 接收電力並依訊號執行開關與運算 | 同時接上供電與訊號，但兩者來自不同路徑 | 最後仍要驗證電壓、速度、應力、良率與可靠度 | 單一結構成功，不等於完整產品可穩定量產 |

這五個位置不是一張完整晶片設計圖，而是閱讀背面供電的最短路徑：訊號主要留在正面，
電力則從背面金屬經導通孔與埋置電源軌接近電晶體。實際結構會因晶圓廠而異，不能用 imec
的一般流程替台積電或 Intel 補上未公開的尺寸、材料、工具與供應商。

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

本輪合計以十五份一手文件或官方頁面，分開建立技術機制、量測比較、設計取捨、製程控制、
晶圓廠路線圖與外部具名設備產品。它們沒有提供跨公司共同良率、同一客戶產品、設備台數、
供應商份額、價格或財務分母，也沒有一致預期、估值或即時部位資料，因此本文不判斷題材是否已反映。
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

- 同一 frontside／backside 產品版本公開八格比較護照，並同時提供靜態 IR drop、動態下陷、PPA、熱、可靠度與原始分布。
- 同一具名試驗晶片或客戶產品，同時公開設計取捨、接點電阻、電力完整性與可靠度結果。
- 台積電正式確認 A16 實際進入量產，並提供至少一個客戶產品、爬坡、良率或製造範圍。
- Intel 將 18A／18A-P 連到具名外部晶圓代工客戶產品與可定位出貨，而不只停在公司製程里程碑。
- 量測、蝕刻、薄化、接合或材料商揭露同一背面供電步驟的具名客戶資格與重複出貨，且由晶圓廠端交叉核對。
- 台灣公司只有在供應商產品、節點、資格、期間與財務分母都對上時才升級；一般能力、合作或題材熱度仍維持未證。
