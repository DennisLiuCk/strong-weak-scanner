# 800VDC 從路線圖走到量產要跨七關：2026 已到設計與驗證，full-scale 仍待 2027

<!-- research_topic
topic_id: MI-2026-08-01-800VDC-EXECUTION-READINESS
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-01
source_published_at: 2025-05-20
last_reviewed_at: 2026-08-12
review_due: 2026-09-12
source_type: mixed
publisher_domain: nvidia.com
canonical_url: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
source_chain_id: nvidia-800v-ecosystem-update-20260731
stock_ids: 2301,2308,8255
group_ids: power,powersupply,thermal
trigger_type: architecture_update_and_validation
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C13
base_confidence: medium
confidence_basis: NVIDIA、OCP、UL、元件商與台灣供應商一手資料可把架構、設施、介面、安全、子系統資格與商業節點拆成七關；但 full-scale 客戶驗收、現場運行分母與可辨識財務貢獻仍未證實
cross_company_numbers: false
schema_migrated_at: 2026-08-02
-->

<!-- transition
date: 2026-08-01
from: initial
to: inbox
reason: primary_source_architecture_and_company_stage_scan
evidence: source_chain:nvidia-800v-ecosystem-update-20260731
-->
<!-- transition
date: 2026-08-01
from: inbox
to: triaged
reason: separated_800v_validation_from_50v_shipments_and_2027_full_scale_timing
evidence: sources:S1,S2,S3,S4,S5
-->

<!-- research_source
source_id: S1
role: company_release
publisher: NVIDIA
title: 800V HVDC architecture 技術文章
published_at: 2025-05-20
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
locator: 1MW racks、2027 Kyber 與 full-scale production 段落
limitation: 效率與 TCO 數字是架構目標，未提供客戶營運實績或量產數量
-->

<!-- research_source
source_id: S2
role: company_release
publisher: NVIDIA
title: GTC Taipei 800V power rack 與 hybrid bridge 更新
published_at: 2026-06-01
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/
locator: 800VDC power rack 與 hybrid AC bridge 段落
limitation: 參考設計與生態系列名不等於資料中心全面部署或供應商訂單
-->

<!-- research_source
source_id: S3
role: company_release
publisher: Delta Electronics
title: 台達電 GTC 800VDC 系統展示
published_at: 2026-03-16
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.delta-americas.com/en-US/news/40116
locator: 660kW power rack、480kW BBU 與 2.4MW CDU 展示規格
limitation: 展示規格與公司效能主張不證實客戶驗收、量產數量、收入或毛利
-->

<!-- research_source
source_id: S4
role: company_release
publisher: LITEON Technology
title: 光寶科 2026Q1 結果與電源產品時程
published_at: 2026-04-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.liteon.com/en/news/press-center/content/quarterly-first-eps-2026
locator: 50V power rack、110kW power shelf 與 800V validation 段落
limitation: 公司時程不等於驗證完成、量產出貨或客戶採購承諾
-->

<!-- research_source
source_id: S5
role: company_release
publisher: LITEON Technology
title: 光寶科 2026 年 6 月營收
published_at: 2026-07-09
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.liteon.com/en/news/press-center/content/liteon-monthly-sales-june-2026
locator: Cloud and AIoT 營收占比與成長段落
limitation: 月營收沒有拆出 800V 產品，不能把整體 Cloud and AIoT 成長歸因於 800V
-->

<!-- research_source
source_id: S6
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-01 以台灣電源供應商代號重查重大訊息、法說與季度財報的入口
limitation: 查詢入口會持續更新；入口本身不證明 800V 驗證、量產、訂單或財務貢獻
-->

<!-- research_source
source_id: S7
role: standard
source_kind: document
publisher: Open Compute Project
title: DCF Power Distribution LVDC White Paper Version 1.0
published_at: 2026-03-30
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/dcf-power-distribution-lvdc-white-paper-version-1-0-final-pdf-1
locator: pp.14–26 的 IT rack progression 與三階段 transition；pp.26、48 的 redundancy 與 interoperable voltage band；pp.134–147 的 standardization、commissioning 與 training
limitation: OCP 白皮書是共同架構方法與待完成工作，不是 800VDC 量產規格、通過報告、客戶部署清單或供應商財務證據
independence_group: open-compute-project
-->

<!-- research_source
source_id: S8
role: standard
source_kind: document
publisher: UL Solutions
title: UL Solutions and the Open Compute Project to Help Advance Safety and Scalability in New AI Data Center Innovations
published_at: 2026-01-13
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.ul.com/news/ul-solutions-and-open-compute-project-help-advance-safety-and-scalability-new-ai-data-center
locator: standards gap、codes and standards workstream、workforce training、commissioning practices 與 component／system scope 段落
limitation: 這是標準與安全工作啟動公告，不是新版標準已發布、監管核准完成、任何資料中心已通過 commissioning 或元件已取得認證
independence_group: ul-solutions
-->

<!-- research_source
source_id: S9
role: company_release
source_kind: document
publisher: NVIDIA
title: BESS Self-Qualification Guidelines v1.0
published_at: 2026-05-28
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.nvidia.com/dsx/facilities-infra/bess/overview
locator: Qualification Workflow、Submission Expectation 與 Qualification Boundary；明示 passing qualification does not imply site-level stability
limitation: 規範只涵蓋 BESS 在 AC terminals／PCS boundary 的自我資格流程，不是整套 800VDC 配電、power rack、BBU 或資料中心的驗收結果
independence_group: nvidia
-->

<!-- research_source
source_id: S10
role: competitor_primary
source_kind: document
publisher: onsemi
title: The Emerging Way to Conquer Power Challenges in AI Data Centers
published_at: 2026-07-14
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.onsemi.com/company/newsroom/featured-stories/data-center/the-emerging-way-to-conquer-power-challenges-in-ai-data-centers
locator: Key Takeaways 的 SST early commercialization、800V HVDC evaluation 與 later-this-decade timing
limitation: 供應商技術文章描述自家產品定位與產業方向，不是 hyperscaler 驗收、production rack deployment、跨廠市場份額或台灣公司財務證據
independence_group: onsemi
-->

<!-- research_source
source_id: S11
role: company_release
source_kind: document
publisher: Delta Electronics
title: Delta Electronics and X LABS Sign Technology Partnership MOU to Power Next-Gen AI Data Centers
published_at: 2026-07-14
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.delta-americas.com/en-us/news/delta-electronics-americas-and-x-labs-sign-technology-partnership-mou-to-power-next-gen-ai-data-centers
locator: MOU、expected deployment of 100MW of SST、800VDC grid-to-rack capability 與 moves from MOU to deployment 段落
limitation: 100MW 是公司公告中的 MOU 規劃量，不是已部署抽樣觀測、具約束力採購、客戶驗收、已出貨容量、收入或毛利；不適用抽樣 SE
independence_group: delta-electronics
-->

<!-- research_source
source_id: S12
role: standard
source_kind: living_index
publisher: Open Compute Project
title: Power Distribution Sub-Project
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/community/power-distribution
locator: 2026-08-12 顯示 LVDC、interoperability、safety、operation、protection、energy storage 與後續 work products 的持續更新入口
limitation: 專案頁只用來發現後續白皮書、specification 與 workstream 更新；頁面存在不代表工作已完成或產品已通過驗收
independence_group: open-compute-project
-->

<!-- research_source
source_id: S13
role: company_release
source_kind: living_index
publisher: NVIDIA
title: NVIDIA 800 VDC Architecture
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.nvidia.com/en-au/data-center/technologies/800-vdc-architecture/
locator: 2026-08-12 的 architecture overview、gradual AC-to-800VDC transition、partner list 與後續文件入口
limitation: 平台索引與夥伴名單只能用來發現新文件；不能證明合作深度、qualification、部署、供應份額或收入
independence_group: nvidia
-->

<!-- research_source
source_id: S14
role: standard
source_kind: document
publisher: Open Compute Project
title: Open Data center Spec Version 0.5.0
published_at: 2026-02-25
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.opencompute.org/documents/open-data-center-spec-version-0-5-0-pdf
locator: 官方 26 頁 PDF p.9 的 power architecture 表；同頁分列 4 feeds with independent UPS／3+1 與 2N connection，並分別列出 750kW／1MW minimum row-level power 及約 6MW／12MW minimum data-hall power；已由瀏覽器 PDF viewer 逐頁目視核對
limitation: 這是 OCP Next-Generation ML Infrastructure Design Principles 的特定設計表，不是 N+1、3+1、2N 或 critical IT capacity 的跨場站通用定義，也不是 as-built 單線圖、故障測試、實際負載、能源效率或客戶驗收結果；官方端點對命令列直取回應 403，故本輪不宣稱本地檔案 SHA
independence_group: open-compute-project
-->

<!-- research_source
source_id: S15
role: regulator_or_policy
source_kind: document
publisher: U.S. Department of Energy Federal Energy Management Program
title: Best Practices Guide for Energy-Efficient Data Center Design
published_at: 2024-07-26
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design.pdf
locator: 官方 48 頁 PDF，SHA-256 f4db5c015154933482e84f1946dcafc297d8ad526db90d2985df35232d8ab0c2；PDF p.38（印刷 p.29）§8.1 定義 PUE 為年度 total facility energy／IT equipment energy，說明單位為 annual kWh、只衡量 supporting infrastructure efficiency；實際引用頁及前後頁 PDF pp.37–39 已逐頁渲染核對
limitation: DOE 文件提供年度能源計量方法與邊界，不提供任一 800VDC 場站的 installed capacity、critical IT capacity、冗餘拓撲、瞬時 peak power、IT 工作產出、commissioning、成本或財務結果；本文教材的 PUE 1.25 不是 DOE 建議值
independence_group: us-doe-femp
-->

<!-- research_source
source_id: S16
role: company_release
source_kind: document
publisher: NVIDIA
title: Why Scaling AI Compute Performance Requires a New Power Architecture
published_at: 2026-08-11
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://blogs.nvidia.com/blog/800-vdc-power-architecture-ai-factory/
locator: Existing Facilities Don't Have to Wait 與 A Roadmap for Every Stage of Growth；分列 2026H2 hybrid power rack、2027 row power center 及較後期 facility-scale DC power block
limitation: arriving／expected availability 是 NVIDIA 供貨與架構路線圖，不是具名場站已安裝、commissioning、production volume、供應商收入或毛利；80+ 生態系公司也不提供個別供應深度
independence_group: nvidia
-->

<!-- research_source
source_id: S17
role: company_release
source_kind: document
publisher: NVIDIA
title: DSX Facilities Infrastructure Reference Design Overview
published_at: 2026-08-19
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://docs.nvidia.com/dsx/facilities-infra/reference-design-overview
locator: NVIDIA DSX Facilities Infrastructure Design Guide v2.0；Grid Substation、Dry Coolers、BESS & Backup Generation、Central Utility Building 與 250 MW / 96 SU Example Site Figures
limitation: 這是 250MW-class IT load 的 sizing reference 與 campus context，不是圖示場址或任何具名客戶的 as-built 配置；實際容量與布局逐案不同，也未提供 800V production BOM、驗收、部署量或財務歸因
independence_group: nvidia
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: NVIDIA 仍把 1MW 以上機櫃與 800VDC full-scale production 錨定於 2027 Kyber 世代
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-07-31
basis: NVIDIA 更新後的技術文章直接提供架構定位與量產時鐘
boundary: 這是平台商路線圖，不是已完成的客戶驗收、部署量或營收
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: 台達電已展示 800VDC power rack、BBU 與 CDU 系統規格
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-03-16
basis: 公司官方展示公告列出系統與功率規格
boundary: 證實的是展示內容，不代表客戶訂單、量產、利用率或財務貢獻
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: 光寶科表示 50V power rack 已量產、110kW power shelf 已出貨，而 800V power rack 預計在 2026 下半年進入驗證
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-04-29
basis: 公司季度結果直接區分量產、出貨與待驗證三個產品階段
boundary: 50V 出貨不可改寫成 800V 出貨，預計驗證也不等於驗證完成
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: superseded
claim: 2026 年較合理的基準情境是 800VDC 從參考設計與展示走向驗證的過渡期，而非全面商用年
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-07-31
basis: 平台量產時鐘仍在 2027，供應商證據分別停在展示、過渡產品量產與 800V 驗證
boundary: 沒有全產業客戶驗收、部署數、出貨占比或供應商收入資料可估計轉換速度
verification_needed:
resolution:
correction_kind:
corrects_claim_id:
corrected_by_claim_id: C13
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: 台達電、光寶科或其他台灣供應商已由 800VDC 取得可量化的大規模訂單與獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-01
basis: 現有來源是架構、展示、驗證時程與未拆分的 Cloud and AIoT 營收
boundary: 不建立 800V 客戶、出貨量、收入占比、市占、毛利或朋程供應關係
verification_needed: 需平台客戶驗收與台灣公司法說或財報雙向核對產品、數量及財務貢獻
resolution:
-->

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: 光寶科 2026 年 6 月 Cloud and AIoT 營收年增逾 80%、占營收 56%，成長驅動包含高階伺服器電源與 BBU
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-07-09
basis: S5 直接揭露事業占比、年增幅與高階資料中心伺服器電源及 BBU 需求背景
boundary: 公司沒有把 Cloud and AIoT 增量拆為 800V 產品收入，不能以此證明 800V 已出貨或貢獻獲利
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: OCP 將資料中心 LVDC 轉換拆為三個設施階段：先由 DC 供應 IT racks 與選配 cooling，再擴到完整 IT module，最後才是資料中心所有設備的 full DC distribution
supporting_source_ids: S7
contrary_source_ids:
as_of: 2026-03-30
basis: S7 pp.20–26 逐段定義 Stage 1、Stage 2 與 Stage 3 的供電邊界
boundary: 這是架構方法，不代表任一資料中心已走完三階段，也不規定所有業者必須選相同 isolation、SST 或 AC／DC 混合路徑
verification_needed:
resolution:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: OCP 指出 DC distribution 不能沿用 UPS maintenance bypass 的既有做法，需在 power block 或 distribution 層補 redundancy；長距離配電還要處理 line inductance 與 AI cyclic load 對介面的影響
supporting_source_ids: S7
contrary_source_ids:
as_of: 2026-03-30
basis: S7 p.26 的 redundancy 段落與 p.48 的 interoperable voltage band proposal 直接列出兩類系統約束
boundary: 白皮書沒有提供共同 production design、故障率、維修時間或已通過的跨廠 voltage band 實績
verification_needed:
resolution:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
-->

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: UL Solutions 與 OCP 已啟動高壓 DC 的 codes and standards gap analysis，範圍包含 switchgear、panelboards、busbars、cables 與 overcurrent protection，並把 standards revision、workforce training 與 commissioning practices 列為規模部署前置工作
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-01-13
basis: S8 直接說明 workstream、受影響 component／system 類別與待建立的實務能力
boundary: 啟動工作不等於缺口已關閉、標準已修訂、地方主管機關已核准或現場人員已完成訓練
verification_needed:
resolution:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: NVIDIA 的 BESS 指引要求 partner-run tests、submission evidence 與 owner review，且明示通過 BESS qualification 不代表 site-level stability
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-05-28
basis: S9 的 qualification workflow、submission expectation 與 boundary note 直接區分子系統資格和場站整合
boundary: BESS 是相鄰子系統範例；不能把其測試表直接冒充 800VDC power rack、BBU、配電或整座資料中心的共同驗收規格
verification_needed:
resolution:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: 台達電與 X LABS 於 2026-07-14 簽署 MOU，框架包含預期部署 100MW 台達 SST，並把 SST 與 800VDC 描述為 grid-to-rack 能力
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-07-14
basis: S11 的標題、MOU 條款描述與 expected deployment 段落直接支持合作階段與公司規劃量
boundary: MOU 與 expected deployment 不等於具約束力訂單、已完成 deployment、800VDC rack 驗收、100MW 已出貨或台達已認列收入／毛利；100MW 為單一公告目標，無抽樣 SE
verification_needed:
resolution:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: onsemi 於 2026-07-14 將 SST 定位為 early commercialization，並描述 hyperscaler 與 infrastructure providers 正在評估 later-this-decade 的 800V HVDC 轉換
supporting_source_ids: S10
contrary_source_ids:
as_of: 2026-07-14
basis: S10 Key Takeaways 直接使用 early commercialization、evaluate 與 later this decade 的階段語言
boundary: 這是供應商產業觀察與產品定位，不是全市場採用率、具名客戶 qualification、production deployment 或收入證據
verification_needed:
resolution:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
-->

<!-- research_claim
claim_id: C13
label: inference
status: active
claim: 800VDC 的 execution readiness 應拆成架構時鐘、設施邊界、介面與冗餘、安全標準、子系統資格、場站驗收、量產與財務七關；2026 的證據已從展示前進到標準工作、資格框架與規劃部署，但仍不足以改寫成 full-scale 商用年
supporting_source_ids: S1,S2,S7,S8,S9,S10,S11
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C4；NVIDIA 提供 2027 平台時鐘，OCP／UL 拆出設施與標準缺口，NVIDIA BESS 顯示子系統與場站邊界，onsemi 與台達資料把商業階段分別停在 early commercialization 與 MOU planned deployment
boundary: 七關是研究端的證據分類，不是任何一家機構發布的單一認證流程；沒有完成場站 commissioning、客戶 acceptance、production volume、收入與毛利分母可估計轉換速度
verification_needed:
resolution:
correction_kind: supersedes
corrects_claim_id: C4
corrected_by_claim_id:
-->

<!-- research_claim
claim_id: C14
label: verified
status: active
claim: OCP Open Data center Spec v0.5.0 的同一 power-architecture 表把 4 路獨立 UPS 支援的 3+1 與另一欄 2N connection 分開，並分別列出每列最低 750kW／1MW 及資料廳最低約 6MW／12MW 的設計數值
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-02-25
basis: S14 PDF p.9 的表格逐欄直接列出 feed redundancy、row-level power、facility-to-load architecture 與 minimum data-hall power
boundary: 這只證實一份 OCP 設計文件中的兩欄條件與數值，不定義所有場站的 N、N+1、3+1 或 2N，也不能從 12MW headline 判定 installed、fault-tolerant critical、實際 IT 負載、能源或已部署容量
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C15
label: verified
status: active
claim: DOE FEMP 2024 指南把 PUE 定義為資料中心年度 total facility energy 除以年度 IT equipment energy，使用 annual kWh，並明示 PUE 只描述 supporting infrastructure efficiency、不是整座資料中心的 overall efficiency
supporting_source_ids: S15
contrary_source_ids:
as_of: 2024-07-26
basis: S15 PDF p.38（印刷 p.29）§8.1 直接給出公式、年度量測理由與適用邊界
boundary: 年度能源比不能單獨推出瞬時 facility input、peak demand、installed capacity、critical IT capacity、N+1／2N 拓撲、IT 工作效率或商業利用率；不同 meter boundary 與期間的 PUE 也不能直接比較
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C16
label: inference
status: active
claim: 場站容量判讀應把 installed／nameplate capacity、設計故障後仍可承載的 critical IT capacity、實際 IT load，以及期間 facility／IT energy 與 PUE 分成四本帳；本文固定 200kW 模組時，假想 5+1 N+1 的 installed／critical 為 1.2／1.0MW，假想雙完整路徑 2N 為 2.0／1.0MW，同為 0.8MW 期間平均 IT load 時 critical utilization 都是 80%，但 installed utilization 分別為 66.7%／40%；另以 365 天 IT energy 7,008MWh、facility energy 8,760MWh 得 PUE 1.25 與 supporting energy 1,752MWh，直接用 installed÷PUE 卻得到 0.96／1.60MW，兩者都不是 1.0MW critical capacity
supporting_source_ids: S7,S14,S15
contrary_source_ids:
as_of: 2026-08-14
basis: S7／S14 顯示 facility transition 與 redundancy 必須連同特定 topology／design basis 閱讀，S15 固定年度能源分子分母；Python Fraction 與獨立 awk 均重算容量、兩種 utilization、annual energy、PUE、supporting energy 及錯誤 installed÷PUE 結果
boundary: 這是 N=2 個假想冗餘設計加 N=1 個假想 365 天 meter case 的確定性教材，不是抽樣、OCP reference design、DOE benchmark 或 800VDC 場站測試；200kW、5+1、雙路 2N、0.8MW、1.25 與 8,760 小時均非標準預設，沒有 sampling SE／t、peak distribution、derating、維修併發、故障率、PUE 實測、IT work、rack、site、客戶、部署、收入或公司效果
verification_needed: 同一具名場站與版本的 single-line diagram、reference boundary、N 的負載定義、模組 rating／derating、設計故障與維修情境、installed／critical capacity、同步 IT／non-IT power trace、meter map、PUE 期間與原始能源讀數、commissioning pass／fail、可用工作量及財務共同鍵
resolution:
-->

<!-- research_claim
claim_id: C17
label: verified
status: active
claim: NVIDIA 2026-08-11 路線圖把 800VDC 部署分成三種 on-ramp：預定 2026H2 可裝入既有 AC 設施、在列內送 800V 到運算機櫃的 hybrid power rack；預期 2027 提供、以 overhead 800V busway 支援最高 2MW／row 的 row power center；以及未給明確供貨日、面向未來新設施的 facility-scale DC power block
supporting_source_ids: S16
contrary_source_ids:
as_of: 2026-08-23
basis: S16 的 Existing Facilities 與 Roadmap 兩節直接分開三種設施邊界與時間語言
boundary: 2026H2 與 2027 都是 NVIDIA 的 arriving／expected availability，不是已部署或穩定量產觀測；2MW／row 是 up to 設計能力、N＝1 條公司路線圖，沒有抽樣 SE／t、具名客戶、commissioning、出貨分母或財務貢獻
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C18
label: verified
status: active
claim: NVIDIA DSX Facilities Infrastructure Design Guide v2.0 的參考園區仍同時使用 100kV 以上 utility input、34.5kV campus backbone、4.16kV chiller bus 與 480V pumps／coolers／controls，並要求 BESS 適用性與容量逐案評估
supporting_source_ids: S17
contrary_source_ids:
as_of: 2026-08-23
basis: S17 的 Grid Substation、Dry Coolers、BESS 與 Central Utility Building 欄位直接列出各責任域及電壓
boundary: 這只證實一份 NVIDIA sizing reference 的多電壓設施樹，不是 as-built 場站、跨市場採用率或未來 native 800V 設施的唯一拓撲；100kV+、34.5kV、4.16kV、480V 是同一參考設計的確定性欄位，沒有抽樣 SE／t
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C19
label: inference
status: active
claim: 判讀「800V 已採用」時至少要同時記錄 conversion boundary 與 deployment boundary；現有證據只足以分開既有 AC 建築中的列內 800V、整列 800V busway 與更後期 facility-scale DC power block，不能用單一採用年份或單一 800V 標籤代表整座園區所有設備都已轉為 800V
supporting_source_ids: S7,S16,S17
contrary_source_ids:
as_of: 2026-08-23
basis: S16 把三種 on-ramp 分開，S17 顯示現行 DSX 參考園區仍是多電壓責任域，S7 又把 LVDC facility transition 拆成三種改動範圍
boundary: 這是研究端跨 NVIDIA 與 OCP 架構文件建立的分類，不是標準定義、採用率統計或場站驗收；S16／S17 同屬 NVIDIA 消息鏈，仍缺具名 as-built 場站、production volume、客戶 acceptance 與公司財務共同鍵
verification_needed: 同一具名場站版本的 grid-to-rack single-line、AC／DC conversion boundary、各電壓域、實際部署日、commissioning、運行分母及供應商出貨財務
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: retired
claim_ids: C1,C4
metric: 800VDC 客戶驗證、資料中心部署與 2027 full-scale production 時程
source_ids: S1,S2
watch_source_ids: S6
frequency: monthly
frequency_detail: 每月平台更新與重大產品發布
next_check: 2026-08-08
trigger: NVIDIA 或客戶首次揭露通過驗收、部署機櫃數、功率規模或正式量產日期
invalidation: 若 2027 時程延後或客戶持續只採 hybrid bridge，快速全面切換假說失效
retired_at: 2026-08-12
retirement_reason: 2026-08-08 no_new_evidence 回查已保留；C4 的展示到驗證粗階梯由 C13 七關框架取代，後續由 T3 以平台與 OCP living index 接續且不改寫原檢查結果
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C2,C3,C5,C6
metric: 台灣電源供應商 800V 產品的驗證、出貨、收入占比與毛利
source_ids: S3,S4,S5
watch_source_ids: S6
frequency: quarterly
frequency_detail: 每季法說、財報與月營收後複核
next_check: 2026-10-31
trigger: 公司首次明確區分 800V 客戶驗證、量產數量及財務貢獻
invalidation: 若成長只來自 50V 或其他 Cloud and AIoT 產品，800V 個股受惠映射維持未證
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C1,C7,C8,C9,C10,C11,C12,C13
metric: 800VDC 七關中的 architecture timing、facility boundary、interoperability／redundancy、standards、subsystem qualification、site acceptance 與 production deployment
source_ids: S1,S2,S7,S8,S9,S10,S11
watch_source_ids: S12,S13
frequency: monthly
frequency_detail: 每月回查 OCP Power Distribution 與 NVIDIA 800VDC 文件；出現新 specification、qualification packet、commissioning result 或 production deployment 時提前重審
next_check: 2026-09-12
trigger: 平台或場站公開同一版本的介面、冗餘、標準符合、子系統測試、commissioning、客戶驗收、部署容量與正式量產日期
invalidation: 2027 時程延後、標準與 commissioning 缺口未關閉、MOU 未轉部署，或 50／54V hybrid bridge 長期吸收需求，則全面切換假說下修
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
date: 2026-08-12
from: triaged
to: triaged
reason: superseded_demo_to_validation_thesis_with_seven_gate_execution_readiness_framework
evidence: sources:S7,S8,S9,S10,S11
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: separated_installed_critical_actual_load_and_annual_pue_ledgers_without_thesis_or_clock_refresh
evidence: sources:S7,S14,S15
-->
<!-- transition
date: 2026-08-23
from: triaged
to: triaged
reason: separated_hybrid_row_and_facility_scale_800v_onramps_without_thesis_or_clock_refresh
evidence: sources:S16,S17
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **800VDC**：以約 800 伏特直流電在資料中心傳送電力，目的是降低超高功率機櫃的電流、線材與轉換損耗。
- **Power rack**：集中把資料中心電力轉換、分配給多個運算機櫃的電源系統，不等於伺服器本身。
- **BBU**：電池備援單元，停電或負載突升時短暫供電，避免高功率 AI 機櫃中斷。
- **CDU（冷卻液分配單元）**：把冷卻液送往機櫃、帶走熱量的設備；展示功率不等於已有客戶大量部署。
- **GTC**：NVIDIA 舉辦的開發者與產業活動。展會公開的架構或展示規格，仍需客戶驗收與量產資料才能確認商業進度。
- **Kyber**：NVIDIA 公開路線圖中預計於 2027 導入的高功率機櫃世代；路線圖上有名稱，不等於目前已大量出貨。
- **驗證**：客戶測試產品是否符合規格與可靠度；開始驗證不等於驗證完成或已大量出貨。
- **Cloud and AIoT**：光寶科揭露的雲端運算與人工智慧物聯網營收分類；它包含多種產品，不能直接當成 800V 收入。
- **LVDC**：低壓直流配電。OCP 本文把它界定為不高於 1,500VDC 的系統範圍；名稱中的「低壓」是工程分類，不表示可以像低壓電子產品一樣徒手維修。
- **SST（固態變壓器）**：用功率半導體、磁性元件與數位控制轉換電壓的系統。它可能減少轉換級數，但仍要通過保護、冗餘、熱、控制與場站測試。
- **Interoperability（互通）**：不同供應商設備在同一電壓範圍、保護邏輯與控制契約下可共同運作；插頭接得上只是起點。
- **Redundancy（冗餘）**：某一路設備故障或維修時，其他路徑仍能維持服務。改成 DC 後，既有 UPS maintenance bypass 不一定能原樣沿用。
- **N／N+1／2N**：N 是承擔指定設計負載所需的設備或路徑；N+1 多一個指定單元，2N 則有兩套可各自承擔該負載的完整路徑。字母只在故障、維修與 reference boundary 都說清楚後才有容量意義。
- **Installed／nameplate capacity（裝置／銘牌容量）**：把已安裝設備在指定額定條件下的容量加總；它包含備援與待命路徑，不等於故障後仍可承載的 IT 負載。
- **Critical IT capacity（關鍵 IT 可承載容量）**：在明列的設計故障、維修、降額與環境條件下，場站仍承諾供給 IT 的容量；它不是把全部銘牌 MW 相加。
- **Actual IT load（實際 IT 負載）**：IT 設備在指定時刻或期間真正取用的功率。平均、峰值與百分位是不同時間口徑，不能只寫一個 MW。
- **kW／MW 與 kWh／MWh**：前者是某時刻或短窗口的功率，後者是功率隨時間累積的能源；容量比較不能把 MW 與年度 MWh 混成同一分母。
- **PUE（Power Usage Effectiveness）**：同一 meter boundary 與期間內，total facility energy 除以 IT equipment energy；年度 PUE 是能源比，不是 installed MW 的折減係數，也不是 IT 工作效率。
- **DOE FEMP**：美國能源部 Federal Energy Management Program；本文引用其資料中心節能設計指南來固定 PUE 的年度能源口徑，不把政府指南當成 800V 場站驗收。
- **Open Data center Spec v0.5.0**：OCP 的 Next-Generation ML Infrastructure Design Principles 文件版本；本文只引用 p.9 的特定設計表，版本號不表示所有資料中心都採同一拓撲。
- **Sampling SE／t**：用來表達抽樣點估計誤差與相對零值強度的統計量；本文是假想拓撲的確定性算術，沒有可估的抽樣 SE 或 t 值。
- **Commissioning（場站試運轉／驗收）**：設備安裝完成後，以實際接線、控制、保護、負載與異常情境確認整個場站可安全運作。
- **AHJ（主管機關）**：對當地電氣、消防與建築安全具有核准權的機關或人員；平台商的技術資格不能取代 AHJ 核准。
- **MOU（合作備忘錄）**：記錄合作方向與預期範圍，通常比產品展示更接近商業執行，但仍不等於具約束力訂單、完成部署或收入。
- **BESS（電池儲能系統）**：位在場站或電網端、由電池、雙向轉換、控制與保護組成的儲能資產；它與機櫃內 BBU 的位置、時間尺度和驗收邊界不同。
- **Stage（階段）**：OCP 用來區分資料中心哪些區域改採直流的架構範圍，不是產品認證分數。
- **HVDC（高壓直流）**：在本文指約 800V 的直流配電架構；不同機構的電壓分類語境可能不同，不能只看縮寫判定適用標準。
- **DSX**：NVIDIA 用來串接運算、電力、冷卻與場站設計的參考架構；它提供規劃共同語言，不等於圖中的場站已實際建成。
- **Facilities（設施）**：本文指建築與園區層的電力、冷卻、備援及控制，不是單一 power rack 或伺服器產品。
- **v1.0／v2.0（文件版本）**：表示文件已形成可引用的版本基線；版本變大不代表涵蓋所有子系統，也不代表任何產品或場站已通過要求。

### 三句話抓重點

- NVIDIA 仍把 800VDC full-scale production 放在 2027；OCP 則把設施轉換拆成三階段，說明「支援 800V」不是一個單點開關。
- 2026 的證據已從展場往前走到標準工作、子系統資格框架與台達／X LABS 的規劃部署 MOU，但各來源停在不同關卡，不能合成「已全面商用」。
- 真正需要等待的是同一場站的介面、冗餘、安全、commissioning、客戶驗收與 production volume，再由供應商文件對上收入與毛利。

### 為什麼重要

800VDC 可能改變資料中心從配電、電源轉換到備援與散熱的價值分配，但它同時跨越設施端、機櫃端、地方法規與維修流程。若只看某顆元件或某次展示，會漏掉「設備各自可用、接在一起卻不穩」的系統風險，也容易把 2027 的架構方向提前當成 2026 的訂單與獲利。

### 接下來怎麼追

- 追 OCP 是否把白皮書推進成固定版本的 voltage band、interoperability、redundancy、protection 與 commissioning 契約。
- 追具名場站是否把 installed／critical／actual load 與年度 PUE 分成四本帳，公開 single-line、失效假設、同步功率序列與 meter boundary。
- 追平台或客戶是否公布同一場站的子系統資格、現場驗收、部署容量、故障／維修結果與正式量產日期。
- 追台達電的 MOU 是否轉為實際部署與出貨，並追光寶科是否揭露 800V 驗證結果；兩家公司都要再對上收入與毛利分母。

### 想一想

- 一個 BESS 或 power rack 通過自己的測試，為什麼仍不能證明整座資料中心穩定？
- 若 50V 過渡產品持續成長，但互通標準或地方 commissioning 延後，供應商短期收入與長期技術方向可能如何分化？
- MOU 從「規劃 100MW」走到「已交付 100MW」，中間至少還缺哪些可核對文件？

## 先用七關看懂：800VDC 何時才算真的走到量產

這七關是研究中心把多份一手文件合併後建立的證據分類，不是 NVIDIA、OCP 或 UL 發布的一套
單一認證。每關都回答不同問題，也不能用後一關的宣傳語倒推前一關已完成。

| 關卡 | 要回答的問題 | 目前可見證據 | 還缺什麼才前進 |
|---|---|---|---|
| 1. 架構與時鐘 | 為何要從 50／54V 走向高壓 DC，平台何時需要它？ | NVIDIA 把 1MW 以上 rack 與 2027 Kyber／full-scale production 連在一起 | 固定平台版本、production date 與實際部署分母 |
| 2. 設施轉換邊界 | 只改 IT rack、連 cooling 一起改，還是整座場站改 DC？ | OCP 定義 Stage 1、2、3；NVIDIA 提供 hybrid AC／800V bridge | 具名場站選定的 stage、isolation、SST／converter 與責任邊界 |
| 3. 介面、冗餘與維修 | 長距離配電、負載擺動、故障與維修時如何保持服務？ | OCP 指出 line inductance、cyclic AI load 與 maintenance bypass 替代問題 | 固定 voltage band、fault matrix、redundancy topology、維修程序及通過結果 |
| 4. 安全、標準與人員 | 設備如何符合地方電氣／消防要求，誰能安全施工與維修？ | UL／OCP 已啟動 codes and standards gap analysis、training 與 commissioning 工作 | 新版標準、AHJ 採納、訓練資格、現場安全測試與核准紀錄 |
| 5. 子系統資格 | BESS、power rack、BBU、保護與控制是否各自按固定邊界通過？ | NVIDIA BESS v1.0 示範 evidence packet、test、owner review 與明確排除範圍 | 800V 各子系統的固定版本、原始測試、pass／fail、變更控制與多來源重現 |
| 6. 場站 commissioning 與客戶驗收 | 子系統接在一起後，實際負載、保護、控制與公用電網是否仍穩定？ | 台達已有展示，台達／X LABS 又進入 MOU 規劃部署 | as-built 模型、現場全負載／故障測試、客戶 acceptance、運行時數與缺陷處置 |
| 7. 量產與財務歸因 | 規劃如何變成可重複交付、production volume 與供應商損益？ | 光寶 50V 已量產但 800V 原定 2026H2 驗證；台達 MOU 規劃量仍未交付 | 具名產品、出貨期間／數量、收入、成本、毛利與現金流的買賣雙向對帳 |

## 8 月新路線圖：同樣叫 800V，邊界其實分三層

先問「800V 從哪裡開始、到哪裡結束」，會比只問採用年份更接近真實工程。NVIDIA 8 月 11 日
把路徑拆成三個 on-ramp；8 月 19 日 DSX v2.0 的參考園區又顯示，AI 工廠上游電力與冷卻仍由
多個電壓域共同工作。兩份資料應這樣合讀，而不是把三個時間點壓成一次全場切換：

| 路徑／證據 | 800V 的實際邊界 | 時間語言 | 能證明什麼 | 仍不能證明什麼 |
|---|---|---|---|---|
| Hybrid 800V power rack | 既有建築維持 AC；在列內轉成 800V 送到運算機櫃 | 預定 2026H2 arriving | 既有機房有不改建築電力系統的升級入口 | 已安裝、通過 commissioning、穩定量產或供應商獲利 |
| Row power center | 以 overhead 800V busway 供應完整機櫃列，公告能力最高 2MW／row | 預期 2027 availability | 800V 邊界可由單一 power rack 擴到整列 | 整座園區、冷卻與所有輔助設備都改成 800V |
| Facility-scale DC power block | 從 grid 端直接轉成 800V，供新設施採更原生的 DC 架構 | 定位為 decade ahead，未給供貨日 | 平台商已畫出更後期的設施級方向 | 已有具名 as-built 場站、production volume 或客戶驗收 |
| DSX v2.0 參考園區 | utility input 100kV+、campus backbone 34.5kV、chiller 4.16kV、pumps／coolers／controls 480V | 2026-08-19 參考設計 | 一座 AI 工廠可以同時保留多個電壓與責任域 | 未來 native 800V 設施只能照此拓撲，或圖中容量已實際部署 |

因此，多方可以說 2026 的 hybrid 入口降低既有機房導入摩擦、2027 又有擴到整列的路徑；空方
也可以說分階段導入延長 AC 資產壽命，設施級 DC 仍沒有明確供貨日。兩方都不能跳到「整座 AI
工廠已全面 800V」或「台灣供應商已認列獲利」。下一份真正會改變判讀的證據，必須把同一具名
場站的 single-line、conversion boundary、各電壓域、commissioning、運行分母與供應商出貨財務
用同一版本鍵對起來。

## 為何值得持續追

真正的研究問題不是「800V 比 54V 新」，而是架構、場站與公司三種時鐘何時對齊。NVIDIA
7 月 31 日更新技術文章後，仍把 1MW 以上機櫃與 full-scale production 錨定在 2027 Kyber；
OCP 3 月白皮書則顯示 voltage band、redundancy、standardization 與 commissioning 還在共同
建模。7 月的新證據把台達從純展示推到 MOU planned deployment，把 SST 描述為 early
commercialization，但都沒有穿過第 6、7 關。因此 2026 仍較像 execution readiness 過渡年，
不是已全面商用的證據。

## 證據現在落在哪一關

| 層級 | 一手來源明講的事實 | 不能外推的結論 |
|---|---|---|
| 架構路線圖 | NVIDIA 表示 800VDC 用來支援 1MW 以上機櫃，full-scale production 將與 2027 Kyber 同步；頁面於 2026-07-31 更新合作夥伴與命名 | 2026 已大規模建置、效率／TCO 目標已由客戶實績驗證 |
| 設施過渡 | NVIDIA 2026 GTC Taipei 說明 hybrid AC／800V bridge；OCP 又分成只供 IT rack、IT module 連 cooling、以及 full DC facility 三階段 | 所有資料中心會一次由 50／54V 切換為 800V，或三階段有固定唯一順序 |
| 介面與冗餘 | OCP 指出 DC maintenance bypass、power-block redundancy、長距離 line inductance 與 cyclic AI load 都要重新處理 | 已有共同 production voltage band、故障選擇性、維修程序或 field reliability |
| 安全與核准 | UL／OCP workstream 盤點 switchgear、panelboard、busbar、cable 與 overcurrent protection 的標準缺口，並要求 training／commissioning | 標準修訂完成、全球法規一致、AHJ 已核准任何具名場站 |
| 子系統資格 | NVIDIA BESS v1.0 要求 partner-run tests、submission evidence 與 owner review，並明示通過不等於 site stability | BESS 規範就是整套 800VDC rack／facility 的共同資格，或任一具名場站已通過 |
| 系統展示 | 台達電在 GTC 展示 660kW power rack、480kW BBU 與 2.4MW CDU；98% 等數字是公司展示規格 | 客戶訂單、量產數量、利用率、收入或毛利 |
| 規劃部署 | 台達與 X LABS 簽署 MOU，公告的框架包含預期部署 100MW SST，並把 SST／800VDC 連到 grid-to-rack | 100MW 已成為具約束力訂單、已交付、通過 800V rack 驗收或認列財務；100MW 是單一公司規劃值，無抽樣 SE |
| 公司產品節點 | 光寶科 4 月表示 50V power rack 已量產、110kW power shelf 已出貨；800V power rack 預計 2026H2 進入驗證 | 把 50V 出貨改寫成 800V 出貨，或把驗證改寫成量產 |
| 需求背景 | 光寶科 7 月公告 6 月 Cloud & AIoT 營收年增逾 80%、占營收 56%，驅動力包含高階伺服器電源與 BBU | 該增量由 800V 產品貢獻；公司未作此拆分 |

## OCP 的三階段不是「成熟度排名」，而是改動範圍

- **Stage 1：DC 先供 IT racks。** 其他設備仍可使用 AC，cooling 是否一起轉換也是選項；最接近現有設施的漸進式改法。
- **Stage 2：整個 IT module 使用 DC。** 除 IT racks 外，CDU 與網路等模組也納入，但建築基礎設施仍跑 AC。
- **Stage 3：資料中心全面 LVDC。** 從中壓端到全部設備都改用 DC，是改動最廣的終局架構。

這三段描述「哪裡改成 DC」，不是「產品已通過第幾級認證」。同一 Stage 1 仍可能因 isolation
位置、電壓範圍、保護、能量儲存或維修程序不同而需要重新驗收；Stage 3 也不天然比 hybrid
方案更適合每一座既有場站。

## 同樣寫 1MW，為什麼 installed、critical、actual 與 PUE 是四本帳

場站新聞常把「裝了多少 MW」、「故障後能供多少 MW」、「現在用了多少 MW」和「一年用了多少
MWh」塞進同一段。它們其實回答四個不同問題：installed／nameplate capacity 是設備加總，
critical IT capacity 是在指定失效情境下仍可承載的 IT 容量，actual IT load 是某時刻或期間真的
取用多少，PUE 則是同一期間兩顆能源表的比值。任何一項都不能只靠另一項換算。

OCP Open Data center Spec v0.5.0 提供一個很實用的反例：同一張表把 4 路獨立 UPS 的 3+1 與
另一欄 2N connection 分開，row-level minimum 分別寫 750kW 與 1MW，minimum data-hall power
又分別寫約 6MW 與 12MW。[S14] 這只能說明該設計表的兩欄條件不同；它不是「2N 一律等於
12MW」的定義，更不能告訴讀者 12MW 是設備銘牌加總、故障後承載量、實際負載或已部署容量。

### 先固定失效情境，再算 installed 與 critical

以下固定每個模組 200kW，不考慮降額、共因故障與同時維修，只用 N=2 個純假想拓撲教分母：

- **5+1 的 N+1：**承擔設計負載需要 5 個模組，另裝 1 個備援；假設任一模組不可用時，剩下 5 個仍可供電。
- **雙完整路徑的 2N：**A、B 各有 5 個模組，每一路都能獨立承擔設計負載；假設其中一整條路徑不可用。

| 四本帳中的容量項 | 假想 5+1 N+1 | 假想雙路 2N | 正確讀法 |
|---|---:|---:|---|
| Installed／nameplate | 6×200 = 1.20MW | 2×5×200 = 2.00MW | 實際裝了多少額定設備，含備援 |
| Critical IT capacity | 5×200 = 1.00MW | 1×5×200 = 1.00MW | 指定單元／整路失效後仍能承載多少 |
| 期間平均 actual IT load | 0.80MW | 0.80MW | 這一期間 IT 真正平均取用多少；不是 peak |
| Actual ÷ critical | 0.80÷1.00 = 80.0% | 0.80÷1.00 = 80.0% | 對可承載 IT 容量的平均使用比 |
| Actual ÷ installed | 0.80÷1.20 = 66.7% | 0.80÷2.00 = 40.0% | 對全部銘牌設備的平均使用比；分母含不同備援量 |

所以「2N 裝了 2MW」不表示它能在設計失效後額外承載 2MW IT；這個例子裡，它和 N+1 都只
承諾 1MW critical capacity。反過來，兩案都有 80% critical utilization，也不表示設備利用率
相同：若分母改成 installed，數字立刻變成 66.7% 與 40.0%。比較利用率前必須先問分母。

### PUE 是年度能源比，不是容量折扣

DOE FEMP 的 2024 指南把 PUE 定義為年度 total facility energy 除以年度 IT equipment energy，
並明說它只衡量 supporting infrastructure efficiency，不是整座資料中心的 overall efficiency；
年度量測能納入 cooling 條件與動態 IT load 的變化。[S15] 因此 PUE 需要 kWh／MWh 能源表與
共同期間，不能直接拿銘牌 MW 相除。

另設 N=1 個純假想 365 天 meter case：期間平均 IT load 為 0.80MW、平均 total facility
power 為 1.00MW，兩顆表完整涵蓋同一 8,760 小時：

```text
IT energy          = 0.80MW × 8,760h = 7,008MWh
Facility energy    = 1.00MW × 8,760h = 8,760MWh
Supporting energy  = 8,760 − 7,008   = 1,752MWh
PUE                = 8,760 ÷ 7,008   = 1.25
```

1,752MWh 相當於 IT energy 的 25.0%，卻只占 total facility energy 的 20.0%；連「支援耗能
占比」都要先說分母。更重要的是，若誤把 PUE 當容量折扣，前述 N+1 的 1.20÷1.25 會得到
0.96MW，2N 的 2.00÷1.25 會得到 1.60MW；兩個答案都不是已由拓撲與失效假設算出的
1.00MW critical capacity。這個反例直接證明 installed MW ÷ PUE 沒有 critical-capacity 語意。

年度 PUE 也不提供瞬時 peak facility input、哪一條備援路徑在線、IT 做了多少有效工作，或
同一小時的 cooling 與 compute 關係。要回答那些問題，還要同步功率序列、meter map、工作量、
環境與故障狀態；不能把一個年度 ratio 當成全場站數位分身。

Python Fraction 與獨立 awk 浮點路徑均重算出 N+1／2N 的 installed utilization
66.666667%／40.000000%、critical utilization 均為 80.000000%，年度 IT／facility／supporting
energy 為 7,008／8,760／1,752MWh、PUE 1.250000，以及錯誤的 installed÷PUE
0.960000／1.600000MW。這是固定整數與有理數的確定性展開，不是兩座場站實驗或抽樣估計，
沒有 sampling SE／t、peak distribution、derating、maintenance overlap、failure rate、IT work、
commissioning、成本或財務效果。

### 多空小作文要共用十欄設施容量—能源護照

| 十欄設施容量—能源護照 | 至少保存什麼 | 少了最容易被誤寫成 |
|---|---|---|
| 1. 場站、版本與 reference boundary | site／data hall／row／rack、single-line revision、容量從哪個輸入端算到哪個 IT 端 | 不同邊界的 MW 可以相加 |
| 2. 單位與時間口徑 | kW／MW、kWh／MWh、瞬時／平均／peak／percentile、期間起訖與時區 | 年度 MWh 就是可承載 MW |
| 3. Topology 與 N 定義 | N+1／3+1／2N、N 代表模組／feed／UPS／generator／path，正常如何分攤負載 | 寫了 2N 就知道容量 |
| 4. 失效與維修假設 | 單模組、整路、共因、同時維修、切換時間、允許中斷與 safe state | 冗餘銘牌自動等於可用容量 |
| 5. Rating 與 derating | 每模組額定、溫度／海拔／功率因數／老化降額、可用數量與變更控制 | Datasheet maximum 可全時加總 |
| 6. Installed／nameplate capacity | 逐設備加總、在役／待命／未啟用狀態及計算式 | 公告 MW 已可供客戶使用 |
| 7. Critical IT capacity | 指定失效與維修情境後仍能送到 IT reference point 的容量及 pass／fail | Installed、contracted 與 critical 是同一數 |
| 8. Actual IT load | 同步原始功率序列、平均／peak／percentile、負載品質、IT 工作量與可用性 | 一次 peak 或平均值就是利用率全貌 |
| 9. Facility energy 與 PUE | facility／IT meter IDs、涵蓋設備、校正、缺值、同一期間能源分子分母及不確定度 | PUE 可把 MW 換成 critical capacity |
| 10. 驗收與商業交接 | fault／maintenance commissioning、客戶 acceptance、運行時數、可服務工作量、計費、收入與成本共同鍵 | 工程設計容量已等於部署與獲利 |

**多方小作文可以寫到哪裡：** 若同一 as-built 版本在設計故障與維修情境下反覆維持明列的
critical IT capacity，實際 load distribution 有合理餘量，年度 meter data 又顯示 PUE 與 supporting
energy 改善，且 commissioning、可服務工作量、客戶 acceptance 與供應商出貨財務都能用共同鍵
對上，才可說容量、效率與商業交付正在同時成熟。

**空方小作文可以寫到哪裡：** 若新聞只給「12MW、2N、PUE 1.2」三個 headline，沒有 reference
boundary、N 定義、installed／critical bridge、實際 load trace、meter map 與 fault test，數字可能
分別來自設備銘牌、設計上限與另一期間的能源比；即使每個數字各自正確，拼在一起仍可能是錯的。

兩方必須共用同一份護照。正的容量裕量與低 PUE 仍只回答場站工程的一部分；沒有 IT 工作分母、
deployment、availability、計費、收入與毛利共同鍵，不能把 MW 或 PUE 改寫成台達、光寶、朋程
或任何台灣公司的可辨識財務受惠。

## 為什麼子系統通過，還不等於場站穩定

NVIDIA BESS 指引是一個很好的邊界教材：它要求供應商交測試與模型資料，但明確把 site
transformer、switchgear、relay、generator 與 campus control 排除在 BESS qualification 之外，
也直接說通過資格不代表 site-level stability。這不是拿 BESS 規範替 800V rack 背書，而是提醒
讀者：每份 pass report 都要先問「測試邊界畫在哪裡、誰負責邊界外整合」。

套回 800VDC，power rack、BBU、CBU、SST、CDU、保護器與控制器可以各自有漂亮數字，卻仍可能
在長距離線路、負載突升、故障清除或維修切換時互相影響。只有 as-built 場站在共同版本與實際
負載下完成 commissioning，才能跨過第 6 關。

## 公司公告要放回正確抽屜

| 公告用語 | 能證明什麼 | 仍不能證明什麼 |
|---|---|---|
| 生態系列名 | 公司被平台列入合作範圍 | 供應品項、份額、資格、訂單與獲利 |
| Reference design／展示 | 指定 topology 或設備在供應商條件下可以運作 | 客戶接受、跨廠互通、field reliability 或 production volume |
| Validation scheduled／in validation | 有預定或進行中的測試節點 | 已通過、何時量產、合格率與收入 |
| MOU／expected deployment | 合作方向、角色與規劃量更具體 | 具約束力採購、施工完成、customer acceptance、交付與收入 |
| Mass production／shipment | 指定產品開始量產或交付 | 一定是 800V、客戶已上線、收入占比或毛利改善 |
| 營收分類成長 | 公司某事業群需求正在變化 | 增量由單一 800V 產品造成，或可直接套上市占 |

## 來源與證據邊界

- [NVIDIA 800VDC 技術文章](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)（2025-05-20；2026-07-31 更新）。
- [NVIDIA GTC Taipei／COMPUTEX 2026 更新](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/)（800V 段落為 2026-06-01）。
- [台達電 GTC 系統展示](https://www.delta-americas.com/en-US/news/40116)（2026-03-16）。
- [光寶科 2026Q1 結果與產品時程](https://www.liteon.com/en/news/press-center/content/quarterly-first-eps-2026)（2026-04-29）。
- [光寶科 2026 年 6 月營收](https://www.liteon.com/en/news/press-center/content/liteon-monthly-sales-june-2026)（2026-07-09）。
- [OCP DCF Power Distribution LVDC White Paper v1.0](https://www.opencompute.org/documents/dcf-power-distribution-lvdc-white-paper-version-1-0-final-pdf-1)（2026-03-30；架構、介面、冗餘、標準與 commissioning）。
- [UL Solutions／OCP 高壓 DC 安全與標準工作](https://www.ul.com/news/ul-solutions-and-open-compute-project-help-advance-safety-and-scalability-new-ai-data-center)（2026-01-13）。
- [NVIDIA BESS Self-Qualification Guidelines v1.0](https://docs.nvidia.com/dsx/facilities-infra/bess/overview)（2026-05-28；只作子系統與場站邊界教材）。
- [onsemi：SST early commercialization 與 800V evaluation](https://www.onsemi.com/company/newsroom/featured-stories/data-center/the-emerging-way-to-conquer-power-challenges-in-ai-data-centers)（2026-07-14）。
- [台達電／X LABS SST 與 800VDC MOU](https://www.delta-americas.com/en-us/news/delta-electronics-americas-and-x-labs-sign-technology-partnership-mou-to-power-next-gen-ai-data-centers)（2026-07-14）。
- [OCP Power Distribution 持續更新入口](https://www.opencompute.org/community/power-distribution)與 [NVIDIA 800VDC architecture 持續更新入口](https://www.nvidia.com/en-au/data-center/technologies/800-vdc-architecture/)（2026-08-12 捕捉，只供後續重查）。
- [OCP Open Data center Spec v0.5.0](https://www.opencompute.org/documents/open-data-center-spec-version-0-5-0-pdf)（2026-02-25；PDF p.9 的 3+1／2N、row-level 與 data-hall power 特定設計表，不是通用容量換算式）。
- [DOE FEMP：Best Practices Guide for Energy-Efficient Data Center Design](https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design.pdf)（2024-07-26；PDF p.38／印刷 p.29 的年度 PUE 定義與適用邊界）。
- [NVIDIA：Why Scaling AI Compute Performance Requires a New Power Architecture](https://blogs.nvidia.com/blog/800-vdc-power-architecture-ai-factory/)（2026-08-11；分開 2026H2 hybrid power rack、2027 row power center 與較後期 DC power block）。
- [NVIDIA DSX Facilities Infrastructure Reference Design Overview v2.0](https://docs.nvidia.com/dsx/facilities-infra/reference-design-overview)（2026-08-19；100kV+／34.5kV／4.16kV／480V 多電壓參考園區與 sizing boundary）。

NVIDIA 列名 Delta、LITEON 只證實生態系參與。對 2301 而言，800V 仍停在公司預定的驗證節點；
對 2308 而言，證據已由展示增加到 MOU planned deployment，但仍沒有完成部署與財務分母；
對 8255 而言，本輪來源仍未點名。NVIDIA 的效率、減銅、維護與 TCO 數字屬架構模型／目標，
並非第三方場站實績。OCP、UL 與 BESS 文件也各有不同邊界，不能多數決成「已驗收」；OCP 的
3+1／2N 設計表與 DOE 的年度 PUE 方法更不能拼成 installed-to-critical 容量公式。本輪沒有
一致預期、估值或即時持倉資料，因此不宣稱市場尚未反映、已充分定價或應採取任何股票動作。

## 新手最常混淆的九件事

1. **800V 是電壓名稱，不是完成狀態。** 同樣標示 800V 的元件、rack 與 facility 可能處在完全不同的資格階段。
2. **OCP Stage 1–3 是改動範圍，不是認證等級。** Stage 1 也要完成自己的安全、介面與場站驗收。
3. **通過子系統 qualification 不等於 site stability。** 先畫測試邊界，再看誰負責邊界外設備。
4. **MOU 比 logo 具體，但仍不是出貨。** 規劃容量要再對上合約、施工、驗收與交付。
5. **50V 量產不能搬到 800V。** 同一家公司、同一客戶或同一事業群也不能跨產品偷換階段。
6. **標準工作啟動不等於標準缺口關閉。** 還要看 revision、地方採納、訓練與 commissioning。
7. **產業方向不能直接分配給台股。** 必須以買方與供應商文件對上具名產品、期間、數量、收入與毛利。
8. **Installed MW 不等於 critical IT MW。** 前者含備援與待命容量，後者必須先固定 design fault、maintenance、derating 與 reference boundary。
9. **PUE 不是容量折扣。** 年度 kWh／kWh 不能把 nameplate MW 換成 fault-tolerant MW，也不能代替 peak power 或 IT work efficiency。

## 在研究中心接著怎麼學

1. **先讀本文的七關。** 建立從架構到財務的共同尺，之後遇到任何 800V 新聞都先定位關卡。
2. **再讀「800VDC 功率半導體鏈」。** 把 SST、BBU、IBC、hot-swap 與末端供電放回電力鏈，理解 Si、SiC、GaN 並非二選一。
3. **接著讀「800VDC 保護責任層」。** 追 interlock、接地、fault clearing 與 hot-swap 為何不能由一顆保險絲包辦。
4. **再看「AI 功率緩衝」與「SiC 到 AI BBU／PSU 七關資格鏈」。** 分清時間尺度、子系統測試與元件到整機的證據交接。
5. **最後進入機櫃控制、EMC 與液冷。** 這些文章處理設備接在一起後的 action contract、電磁干擾與 cooling responsibility。

這是學習順序，不是供應鏈受惠排序，也不表示各站已由同一客戶、同一平台或同一 production
BOM 串起。任何公司結論仍需回到各自正式筆記、買方文件與財務分母。

## 投資判讀框架

- **架構 KPI**：2027 平台時鐘、具名 facility stage、isolation／SST 路徑與固定 voltage band。
- **工程 KPI**：reference boundary、installed-to-critical capacity bridge、actual load distribution、年度 meter／PUE contract、redundancy topology、fault matrix、子系統 pass／fail、跨廠互通、as-built commissioning 與運行時數。
- **商業 KPI**：MOU 轉合約、施工與 acceptance，接著才是 production volume、出貨、收入、毛利與現金。
- **常見假訊號**：合作夥伴 logo、展場 demo、效率目標、MOU 規劃量，或把 50V 過渡產品出貨當成 800V 出貨。
- **最關鍵分歧**：價值是否由單顆 PSU 擴大到 power rack、保護、備援、控制與 cooling 的可重複交付；若只增加研發與資本投入，卻沒有通過第 6、7 關，題材不能升格成公司獲利。

## 影響路由

<!-- impact
group_id: powersupply
stock_ids: 2301,2308
direction: mixed
hypothesis_refs: 2301:H1,2308:H1
note_action: review_due
action_due: 2026-08-08
rationale: 2301 已有 50V 量產與 800V 驗證時程，2308 有 800V 系統級展示，下一步需用公司 IR 區分驗證、量產、收入與毛利
evidence_boundary: NVIDIA 生態系名單與公司展示不證實新增訂單、出貨占比、市占或獲利
-->

<!-- impact
group_id: power
stock_ids: 8255
direction: uncertain
hypothesis_refs: 8255:H1,8255:H2
note_action: review_due
action_due: 2026-08-08
rationale: 既有 H1 與 H2 直接主張切入 800V HVDC 與 TOLT／QDPAK 量產，應用下一份公司文件核對客戶驗證與量產節點
evidence_boundary: 本批 NVIDIA、台達電與光寶科來源均未點名朋程，不構成朋程供應關係或營收證據
-->

<!-- impact
group_id: thermal
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-08
rationale: 台達電把 800V power rack、BBU 與 MW 級 CDU 整合展示，顯示電源與液冷可能成為共同系統設計問題
evidence_boundary: 來源未點名 universe 內其他散熱廠，也未證實 800V 對散熱內容量或毛利的淨增量
-->

## 下一個可證明／否定的節點

- 光寶科 2026H2 是否正式揭露 800V 驗證結果、客戶採用、量產日與收入占比；驗證延後即為最直接反證。
- 台達電是否把展示規格推進到客戶量產、實際交付與可辨識的電源／散熱財務貢獻。
- 朋程是否以一手文件證實 800V HVDC 客戶、封裝料號、驗證完成與量產，而不是只保留研究假說。
- 安全、介面與維修標準若延誤，或客戶延長 50／54V 過渡期，2027 full-scale 時程需下修。
- 具名場站是否公開同版 single-line、N 定義、installed／critical capacity、實際 load trace、facility／IT meter map、PUE 期間與 fault／maintenance commissioning；只有 MW 與 PUE headline 不算填滿。
- 若只有合作名單、展場規格或股價反應而沒有公司級收入／毛利證據，維持 `watch`，不得升格。
