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
- **Commissioning（場站試運轉／驗收）**：設備安裝完成後，以實際接線、控制、保護、負載與異常情境確認整個場站可安全運作。
- **AHJ（主管機關）**：對當地電氣、消防與建築安全具有核准權的機關或人員；平台商的技術資格不能取代 AHJ 核准。
- **MOU（合作備忘錄）**：記錄合作方向與預期範圍，通常比產品展示更接近商業執行，但仍不等於具約束力訂單、完成部署或收入。
- **BESS（電池儲能系統）**：位在場站或電網端、由電池、雙向轉換、控制與保護組成的儲能資產；它與機櫃內 BBU 的位置、時間尺度和驗收邊界不同。
- **Stage（階段）**：OCP 用來區分資料中心哪些區域改採直流的架構範圍，不是產品認證分數。
- **HVDC（高壓直流）**：在本文指約 800V 的直流配電架構；不同機構的電壓分類語境可能不同，不能只看縮寫判定適用標準。
- **v1.0（第一個正式版本）**：表示文件已形成可引用的版本基線，不代表涵蓋所有子系統，也不代表任何產品已通過該文件要求。

### 三句話抓重點

- NVIDIA 仍把 800VDC full-scale production 放在 2027；OCP 則把設施轉換拆成三階段，說明「支援 800V」不是一個單點開關。
- 2026 的證據已從展場往前走到標準工作、子系統資格框架與台達／X LABS 的規劃部署 MOU，但各來源停在不同關卡，不能合成「已全面商用」。
- 真正需要等待的是同一場站的介面、冗餘、安全、commissioning、客戶驗收與 production volume，再由供應商文件對上收入與毛利。

### 為什麼重要

800VDC 可能改變資料中心從配電、電源轉換到備援與散熱的價值分配，但它同時跨越設施端、機櫃端、地方法規與維修流程。若只看某顆元件或某次展示，會漏掉「設備各自可用、接在一起卻不穩」的系統風險，也容易把 2027 的架構方向提前當成 2026 的訂單與獲利。

### 接下來怎麼追

- 追 OCP 是否把白皮書推進成固定版本的 voltage band、interoperability、redundancy、protection 與 commissioning 契約。
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

NVIDIA 列名 Delta、LITEON 只證實生態系參與。對 2301 而言，800V 仍停在公司預定的驗證節點；
對 2308 而言，證據已由展示增加到 MOU planned deployment，但仍沒有完成部署與財務分母；
對 8255 而言，本輪來源仍未點名。NVIDIA 的效率、減銅、維護與 TCO 數字屬架構模型／目標，
並非第三方場站實績。OCP、UL 與 BESS 文件也各有不同邊界，不能多數決成「已驗收」。本輪沒有
一致預期、估值或即時持倉資料，因此不宣稱市場尚未反映、已充分定價或應採取任何股票動作。

## 新手最常混淆的七件事

1. **800V 是電壓名稱，不是完成狀態。** 同樣標示 800V 的元件、rack 與 facility 可能處在完全不同的資格階段。
2. **OCP Stage 1–3 是改動範圍，不是認證等級。** Stage 1 也要完成自己的安全、介面與場站驗收。
3. **通過子系統 qualification 不等於 site stability。** 先畫測試邊界，再看誰負責邊界外設備。
4. **MOU 比 logo 具體，但仍不是出貨。** 規劃容量要再對上合約、施工、驗收與交付。
5. **50V 量產不能搬到 800V。** 同一家公司、同一客戶或同一事業群也不能跨產品偷換階段。
6. **標準工作啟動不等於標準缺口關閉。** 還要看 revision、地方採納、訓練與 commissioning。
7. **產業方向不能直接分配給台股。** 必須以買方與供應商文件對上具名產品、期間、數量、收入與毛利。

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
- **工程 KPI**：redundancy topology、fault matrix、子系統 pass／fail、跨廠互通、as-built commissioning 與運行時數。
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
- 若只有合作名單、展場規格或股價反應而沒有公司級收入／毛利證據，維持 `watch`，不得升格。
