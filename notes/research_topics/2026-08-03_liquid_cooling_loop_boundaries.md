# 液冷不是買完設備就能運作：冷源、管路、伺服器與控制必須共同交接

<!-- research_topic
topic_id: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-03
source_published_at: 2022-10-18
last_reviewed_at: 2026-08-03
review_due: 2026-09-03
source_type: mixed
publisher: Open Compute Project
publisher_domain: opencompute.org
canonical_url: https://www.opencompute.org/documents/cold-plate-cooling-loop-requirements-rev-2-pdf
source_chain_id: liquid-cooling-loop-boundary-primary-scan-20260803
stock_ids:
group_ids: thermal,powersupply,serverodm
trigger_type: interface_requirement_and_operations_contract
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C5
base_confidence: high
confidence_basis: OCP requirement document直接劃出 TCS／FWS／ITE 範圍，OCP 現行專案頁又把 cold plate、manifold、quick disconnect、coolant 與 CDU 拆成工作流；Lenovo 的部署指引及 NVIDIA 的 BMS 資料契約分別從系統實作與可觀測控制補強，因此可高信心建立責任邊界，但高信心只適用於架構，不延伸到個別供應商訂單或財務
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-03
from: initial
to: inbox
reason: captured_formal_loop_scope_and_operational_interfaces
evidence: source_chain:liquid-cooling-loop-boundary-primary-scan-20260803
-->
<!-- transition
date: 2026-08-03
from: inbox
to: triaged
reason: rebuilt_fws_tcs_ite_control_and_maintenance_responsibility_map
evidence: sources:S1,S2,S3,S4,S5
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
reason: editorial_plain_language_wave7_power_cooling_learning_no_conclusion_change
evidence: editorial:plain_language_wave7
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave88_cooling_loop_handoffs_and_evidence_gates_no_conclusion_change
evidence: editorial:plain_language_wave88_cooling_loop_handoffs_and_evidence_gates
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_coolant_lifecycle_contract_and_commissioning_baseline
evidence: sources:S3,S7,S8
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **FWS（Facility Water System，設施水系統）**：資料中心設施端的水路，位於冷源與 CDU 之間；它負責把熱帶往冷卻塔、乾式冷卻器或冰水主機。OCP Cold Plate Rev 2 沒有把這一段納入 TCS 規格範圍。
- **TCS（Technology Cooling System，技術冷卻系統）**：從 CDU 出發，經機櫃管路、分流器與伺服器冷板再回到 CDU 的循環水路；冷卻液、管路、接頭、壓力、流量與維護都在這一圈互相影響。
- **ITE（Information Technology Equipment）**：伺服器、加速器與內部冷板等 IT 設備。規格若只管 TCS，不代表 ITE 端所有設計與責任都已被涵蓋。
- **CDU（Coolant Distribution Unit，冷卻液分配單元）**：透過泵浦、熱交換器與控制，把伺服器迴路的熱交給設施水路。它是一個重要節點，不等於整套液冷系統。
- **BMS（Building Management System）**：建築管理系統，收集溫度、流量、壓差、漏液與設備狀態，並在安全 guardrails 內執行控制或隔離。
- **DSX**：NVIDIA 用來描述 AI factory 基礎設施資料、控制契約與驗證生態的文件／平台名稱；列入 DSX 不等於場域已完成驗收。
- **QD／UQD（快速接頭／通用快速接頭）**：QD 是讓液冷管路能快速拆接的連接器；UQD 是 OCP 推動的通用介面方向。單一接頭通過測試，不代表混用不同管路、流體與 manifold 後整套系統仍可靠。
- **rackLocationId（機櫃位置識別碼）**：DSX 用來讓設施端與 IT 端指向同一座實體機櫃的穩定 ID。若兩邊映射不同，告警或隔離命令可能落到錯誤機櫃。
- **Requirement document／specification（要求文件／完整規格）**：要求文件先說明必須滿足哪些條件與範圍；完整規格還需把介面、數值、測試與責任寫到能重現。本文引用的 OCP Rev 2 明說自己是要求文件，不是完整規格。
- **一次側迴路／二次側迴路**：一次側是設施冷源到 CDU 的水路，二次側是 CDU 到機櫃與伺服器再回來的水路。兩側透過熱交換器傳熱，但水質、壓力與維護責任可以不同。
- **Heat exchanger（熱交換器）**：讓兩側流體交換熱量、但通常不直接混合的設備；它是設施水路與技術冷卻水路的交界之一。
- **Piping／tubing（管路）**：承載冷卻液的固定管線或軟管。管徑、材料、壓降、清潔度與接法都會影響流量和可靠度。
- **Manifold（分流器）**：把一條主水路分配到多個機櫃或伺服器支路，再把回水匯集回來；分配不均可能讓部分冷板流量不足。
- **Valve（閥件）**：控制、關閉或調節流體的元件。維修與漏液處置時，能否隔離正確區段取決於閥件位置和控制邏輯。
- **Cold plate（冷板）**：貼近 GPU、CPU 或其他發熱元件，把熱傳給冷卻液的金屬元件；它位於伺服器內，不等於 CDU 或機房冷源。
- **Setpoint（設定值）**：控制系統希望設備維持的目標，例如溫度、壓力或流量。設定值不合理或傳到錯誤設備，可能造成控制失效。
- **Sensor（感測器）**：量測溫度、流量、壓力、漏液或設備狀態的元件。讀數還要有正確位置、單位與品質標記，才能安全使用。
- **供回水溫／流量／壓差**：供水溫是液體進入設備前的溫度，回水溫是帶熱後的溫度；流量是單位時間通過的液體量，壓差是前後壓力差。三者要一起看，不能只看單一數字。
- **水質／腐蝕／污染**：冷卻液的化學成分、顆粒與微生物會影響金屬、密封件和流道。水質失控可能造成腐蝕、沉積或堵塞，即使設備額定容量沒有改變。
- **浸液材料（Wetted materials）**：在迴路內會直接接觸冷卻液的金屬、塑膠、彈性體、密封件、接著劑與塗層。只要新增或更換一種材料，就要重新核對它和流體及其他材料是否相容。
- **冷卻液基準（Coolant baseline）**：系統剛填充、條件合格時留下的流體配方、檢驗值與樣本。之後的讀值要和這個起點比較，才看得出趨勢，而不是只問有沒有超過單一警報值。
- **TSS／TDS**：TSS 是懸浮在液體裡、可形成顆粒污染的固體；TDS 是已溶解的離子與物質總量。兩者都可能影響水路，但不能用同一個數字互相替代。
- **導電度／pH／濁度**：導電度反映流體中離子導電的程度，pH 表示酸鹼性，濁度反映懸浮顆粒造成的混濁。它們是不同觀測窗，不是「水質」的一個總分。
- **腐蝕抑制劑／殺生劑**：前者用來降低金屬腐蝕，後者用來控制微生物。兩者都必須和流體、材料及操作條件相容，不能看到濃度不足就自行加藥。
- **結垢／污堵／腐蝕／微生物生長**：四種不同失效。結垢是礦物沉積，污堵是顆粒或殘留物堆積，腐蝕是材料被化學或電化學反應破壞，微生物生長則可能形成生物膜；四者的檢查與處置不能混為一談。
- **沖洗／鈍化（Flushing／passivation）**：沖洗把施工殘留、顆粒與不合格流體帶出迴路；鈍化是在適用材料表面建立較穩定的保護狀態。它們是試運轉程序，不等於設備出廠時已自動完成。
- **變更控制／行動門檻**：變更控制要求流體、材料、濾材或程序一有改動就重新評估；行動門檻則預先規定讀值偏離時由誰複驗、隔離、換液或停機，避免告警出現後才臨時決定。
- **漏液偵測／隔離**：偵測是發現哪裡有液體異常；隔離是關閉正確閥件或設備，限制影響範圍。看得到告警不代表系統一定能安全隔離。
- **備援**：主要泵浦、電源、感測或控制失效時，由另一組元件接手。備援要經過實際切換測試，不能只靠產品型錄判定。
- **IT／OT**：IT 是伺服器、叢集與資料處理系統；OT 是建築、機電與現場設備控制。液冷告警常需要兩邊對到同一機櫃與同一事件。
- **Guardrail／action ownership（安全限制／動作責任）**：安全限制規定控制動作不能超過哪些邊界；動作責任則回答誰有權下令、誰執行、誰確認結果。
- **Interface control（介面控制）**：把兩個系統交界的尺寸、材料、訊號、設定值、測試與責任寫清楚，避免雙方都以為對方會處理。
- **Commissioning／SAT（試運轉／場域驗收測試）**：試運轉是在現場確認整套系統按設計運作；SAT 是客戶或場域依約定條件完成的驗收測試。兩者比單件產品測試更接近實際部署。
- **L1–L5 commissioning levels（五級試運轉）**：ASHRAE 框架以 L1 表示出貨前的工廠驗收，L2 核對到貨與安裝，L3 做單件／子系統運轉前檢查，L4 測完整系統在不同條件下的功能，L5 再測多系統於真實與故障情境下能否協同。本文提到 L4／L5 基準，就是後兩級留下的整體運轉與整合測試起點。
- **Field reliability（場域可靠度）**：設備長期在真實環境運作後的故障、維修與可用情況；剛通過驗收還不能回答全生命週期表現。
- **Deployment denominator（部署分母）**：用來說明部署規模的基礎，例如多少座場域、機櫃或設備。沒有分母，就不能把少數案例外推成大規模採用。

### 三句話抓重點

- 液冷可以先分成三段：機房把熱送走的設施水路、冷卻設備到機櫃的循環水路，以及伺服器內的冷板與管路。OCP 文件只規定其中一段的部分要求，沒有把三段都包進同一份完整規格。
- Lenovo 的部署指引說明兩條水路如何分開，也要求泵浦備援、溫度與壓力感測、閥件、漏液偵測、材料與水質維護；NVIDIA 文件則定義告警與控制資料如何交換。
- 所以一台冷卻設備通過平台驗證，只證明一個節點；完整部署還要讓冷源、管路、接頭、分流器、冷板、控制與維護一起通過驗收。

### 為什麼重要

第八站回答一台冷卻設備能帶走多少熱、平台把它列在哪個供應階段；這一站接著問整套系統如何
運作。液冷的風險常發生在交接點：設施水質會影響熱交換器，管路材料與冷卻液會影響腐蝕，
接頭與分流器會影響漏液和維修，伺服器內部阻力會影響流量分配，控制系統則決定告警能否指向
正確機櫃、隔離動作能否真的執行。只有把這些責任接起來，才知道問題發生時由誰處理。

### 接下來怎麼追

- 追蹤 OCP 是否把目前的要求文件補成可重現的冷板、冷卻液、快速接頭與整套迴路測試，並保存每次版本變化。
- 追蹤 NVIDIA 是否從設備列名，往現場試運轉、資料完整性、漏液隔離與長期可靠度增加公開欄位。
- 查台灣散熱、電源供應與伺服器代工公司是否說清楚責任範圍：只供元件、供機櫃水路、整合冷卻設備與控制，還是承擔場域驗收和維護；再核對部署規模與財務資料。

### 想一想

- 如果客戶現場出現水質不合、流量不足或告警指向錯誤機櫃，應由設施端、冷卻系統整合者、伺服器供應商還是控制系統負責？現有文件能分清嗎？
- 快速接頭、分流器、冷板與冷卻液各自通過單件測試，是否足以證明混合多家供應商後仍能長期可靠運作？
- 同一家公司若同時賣電源、冷卻設備與控制，研究上要看到哪些合約、驗收與收入資料，才能證明它真的承接較多價值？

## 主張與證據帳本

本篇把「要求文件」「平台資料契約」「產品列名」「場域部署」「財務認列」分開。
證實的責任邊界不自動證明某一家供應商能提供完整方案，更不證明台灣公司已取得訂單。

<!-- research_source
source_id: S1
role: standard
source_kind: document
publisher: Open Compute Project
title: Cold Plate Cooling Loop Requirements Rev 2
published_at: 2022-10-18
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.opencompute.org/documents/cold-plate-cooling-loop-requirements-rev-2-pdf
locator: p.5 Introduction；文件自稱 requirement document and not a specification，並定義 TCS 為 CDU 至 rack、manifold、ITE 再回 CDU；FWS 與 ITE 本身不在範圍內
limitation: PDF 正文未標可定位的批准日，published_at 採 Rev 2 在 2022 OCP Global Summit 首次公開展示的 2022-10-18 作 public anchor；本文件是要求框架，不是單一產品、完整場域設計或客戶驗收證據
independence_group: open-compute-project
-->

<!-- research_source
source_id: S2
role: standard
source_kind: living_index
publisher: Open Compute Project
title: Cold Plate Sub-Project
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.opencompute.org/community/cold-plate
locator: 2026-08-03 Scope；TCS from cold plate to CDU，列出 cold plates、tubing、manifolds、QDs、CDUs，並連到現行 workstreams
limitation: 動態專案頁只證明捕捉日的專案範圍與工作流；不提供各文件固定版本、產品 qualification、客戶部署、供應商份額或財務貢獻
independence_group: open-compute-project
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Lenovo
title: Lenovo Neptune Direct Water-Cooling Standards
published_at: 2024-09-13
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://lenovopress.lenovo.com/lp2018-lenovo-neptune-direct-water-cooling-standards
locator: Solution tiers 的 FWS／TCS separate loops；Neptune compliant data center design 與 Cooling Distribution Units；另見 Direct Water-Cooling Quality、Water Treatment、Monitoring
limitation: Lenovo 文件是自家平台實作與建議，不是所有資料中心的唯一標準；產品案例、tier 與建議不能直接外推為跨供應商測試結果、採購量或財務貢獻
independence_group: lenovo
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: living_index
publisher: NVIDIA
title: DSX Exchange BMS Integration Companion Guide
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://docs.nvidia.com/dsx-exchange/bms-integration
locator: Object Types and Point Types；RackLiquidSupplyTemperature、ReturnTemperature、Flow、DifferentialPressure、LeakDetect、LiquidIsolationStatus／Request，以及 BMS guardrails 與 rackLocationId pre-deployment requirement
limitation: 動態技術文件是 NVIDIA DSX 的資料與控制契約，不證明特定 site 已完整實作、感測器精度、field reliability、設備供應商或財務結果
independence_group: nvidia
-->

<!-- research_source
source_id: S5
role: other_primary
source_kind: living_index
publisher: NVIDIA Marketplace
title: DSX Infrastructure for AI Factory validated CDU list
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://marketplace.nvidia.com/en-us/enterprise/dsx-infrastructure/
locator: 2026-08-03 CDU 清單的 vendor、model、cooling capacity、validation type、wetted materials 與 supply chain status 欄位
limitation: 動態清單沒有不可變版本、完整跨廠測試協定、site commissioning、field reliability、訂單或財務資料；列名只是一個資格節點
independence_group: nvidia-marketplace
-->

<!-- research_source
source_id: S6
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-03 起追蹤 thermal、powersupply、serverodm 族群公司的法說、季報與重大訊息
limitation: 索引頁本身不證明液冷責任範圍、客戶、驗收、量產、收入或毛利；命中文件後須另建 document source 並雙向核對
independence_group: twse-mops
-->

<!-- research_source
source_id: S7
role: standard
source_kind: document
publisher: Open Compute Project
title: Guidelines for Using Water-Based Transfer Fluids in Single-Phase Cold Plate-Based Liquid-Cooled Racks
published_at: 2022-10-03
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/guidelines-for-using-water-based-transfer-fluids-in-single-phase-cold-plate-based-liquid-cooled-racks-final-pdf
locator: 文件頁碼 pp.5–10、14–17；fluid／wetted materials mutual compatibility、Table 1 baseline、startup sample 與 routine monitoring tables
limitation: 這是 2022 年 water-based、non-PG TCS 的指引，數值須按專案客製，不能外推為 FWS、PG、介電液或所有平台的通用門檻；PDF 本身未標批准日，published_at 採共同作者公開 OCP publication listing 的日期，現行 OCP 工作頁另有後續 draft
independence_group: open-compute-project
-->

<!-- research_source
source_id: S8
role: standard
source_kind: living_index
publisher: ASHRAE
title: AI Data Center Energy Performance Framework - Commissioning & Performance Validation
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.ashrae.org/technical-resources/ai-data-center-framework/commissioning-performance-validation
locator: 2026-08-12 Discussion and Highlights；L1–L5 commissioning、construction／startup fouling、cleaning／flushing／passivation 與 L4／L5 baseline trending
limitation: 動態框架頁提供 commissioning 方法與風險邊界，沒有具名場域、冷卻液數值門檻、供應商結果、field failure rate 或財務貢獻
independence_group: ashrae
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: OCP Cold Plate Cooling Loop Requirements Rev 2 是 requirement document 而非完整 specification；其適用範圍是 CDU 經 rack、manifold 與 ITE 再回 CDU 的 TCS，FWS 與 ITE 本身不在文件範圍內
supporting_source_ids: S1
contrary_source_ids:
as_of: 2022-10-18
basis: S1 p.5 直接描述文件性質、TCS 流路及兩個排除範圍
boundary: 只證實該要求文件的 scope；不代表 FWS／ITE 不重要，也不表示任一設備符合要求、完成 specification 或已被客戶驗收
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
claim: OCP Cold Plate Sub-Project 的現行範圍從 cold plate 到 CDU，並把 tubing、manifold、quick disconnect、coolant 與 CDU 等介面列入不同文件或工作流
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-08-03
basis: S2 Scope 與 current workstreams 直接列出 TCS ingredients 與持續標準化項目
boundary: 專案範圍與工作流不等於所有項目已有 final specification、跨廠 qualification 或量產部署
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
claim: Lenovo 的部署指引把 facility primary loop 與 technology secondary loop 分開，並把 CDU 備援、可維修性、過濾、溫度／壓力／流量感測、閥件、漏液偵測以及 fluid chemistry 納入系統要求
supporting_source_ids: S3
contrary_source_ids:
as_of: 2024-09-13
basis: S3 separate loops、quality／water treatment／monitoring 與 Cooling Distribution Units 段落共同列出設計和營運條件
boundary: 這是 Lenovo reference practice，不是所有平台共同的最低規格，也不形成 CDU 供應商的跨公司排名或採購證據
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
claim: NVIDIA DSX BMS contract 為 rack 液冷定義 supply／return temperature、flow、differential pressure、leak detection 與 liquid isolation 等資料或控制點，並要求 BMS 對外部 setpoint／action request 套用安全 guardrails
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-08-03
basis: S4 Object Types and Point Types、Guardrails 與 Integration-Published Points 直接列出欄位、權責和控制原則
boundary: 資料契約只代表可被交換的語意，不證明每個 site 感測完整、數值正確、控制已 commissioned 或隔離動作在 field 成功
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
claim: 液冷可部署性是一份跨 FWS、TCS、ITE、控制與維護的介面契約；單一 CDU 的額定容量、平台列名或單件 qualification 是必要但不足的成熟度證據
supporting_source_ids: S1,S2,S3,S4,S5
contrary_source_ids:
as_of: 2026-08-03
basis: S1 劃出範圍缺口，S2 顯示多個介面仍各自標準化，S3 把設計延伸到水質與維護，S4 定義可觀測與隔離責任，S5 則只提供設備列名欄位；五者共同顯示 site readiness 超出單一設備
boundary: 這是系統工程推論，不宣稱每個專案採相同拓撲、每個介面同等重要、單一 integrator 必須承擔全部責任，亦不評估供應商市占或財務
verification_needed: 需具名客戶的 interface control document、site acceptance test、commissioning、field reliability 及責任矩陣驗證實際部署
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: 台灣 thermal、powersupply、serverodm 族群已有公司承擔可辨識的完整液冷迴路整合、site acceptance 與維護責任，並取得具財務重大性的量產收入
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-03
basis: 現有一手來源能證明架構與若干產品資格，不能由公司產品型錄或平台列名重建合約責任、部署分母、收入與毛利
boundary: 不把 CDU／cold plate／server 系統產品存在、MOU、PoC 或平台列名改寫成完整責任與財務事實
verification_needed: 需客戶驗收或合約範圍、公司法說／季報、具名部署數量與售後責任交叉核對
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: NVIDIA Marketplace 的 CDU 清單把 vendor、model、cooling capacity、validation type、wetted materials 與 supply chain status 作為設備層欄位，但沒有 site acceptance、commissioning 或 field reliability 欄位
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-08-03
basis: S5 捕捉日可定位清單欄位；未出現的 site-level 證據依頁面可見欄位邊界判讀
boundary: 動態頁面可能更新，本文不保存不可變外部快照；缺欄位不代表供應商沒有內部資料，只表示該公開清單不能支持 site-level 結論
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
claim: OCP 的 water-based TCS 指引要求冷卻液、完整浸液材料清單、接頭、溫度、壓力、過濾與安全條件彼此相容；若迴路加入新材料或元件，原相容性判定必須重新評估
supporting_source_ids: S7
contrary_source_ids:
as_of: 2022-10-03
basis: S7 pp.5–10 把 fluid、wetted materials、connectors 與 operating conditions 放在同一套 mutual-compatibility 要求，並明示 additions require reevaluation
boundary: 只證實該 OCP water-based TCS 方法；不表示一份材料清單已涵蓋所有流體、FWS、PG 或介電液，也不證明任一供應商已完成客戶 qualification
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
claim: OCP 指引要求啟動時在合格條件下保留代表性冷卻液樣本，並在運轉中監測導電度、pH、硬度、細菌、抑制劑、外觀與濾材負載，再以實驗室品質控制和趨勢比較判讀變化
supporting_source_ids: S7
contrary_source_ids:
as_of: 2022-10-03
basis: S7 pp.14–17 的 startup cleanliness、flushing、fill、retained sample 與 routine monitoring tables 直接列出採樣、檢測、QA 和 trending 要求
boundary: 文件沒有替每座場域給出同一採樣頻率、全套 action limit 或 root-cause 決策；保留樣本和監測也不等於已證實長期可靠
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
claim: Lenovo 的 Neptune 指引把 scaling、fouling、corrosion 與 microbiological growth 分成四類水質失效，並要求系統從設計、製造、運送、安裝到維護保持潔淨，持續監測 pH、導電度、細菌數與腐蝕抑制劑
supporting_source_ids: S3
contrary_source_ids:
as_of: 2024-09-13
basis: S3 Direct Water-Cooling Quality、Water Treatment 與 Monitoring 段落直接列出四類風險、全流程 cleanliness 和監測欄位
boundary: 這是 Lenovo 平台實作指引，不是所有流體與材料的共同 failure limit，也不提供跨場域故障率或供應商比較
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
claim: ASHRAE 的 AI data center commissioning 框架指出液冷設施會因施工與啟動潔淨度不良而產生 fouling 風險，因而把 cleaning、flushing、passivation 及 L4／L5 的效能基準與趨勢追蹤列為 commissioning 和營運交接重點
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-08-12
basis: S8 2026-08-12 捕捉頁面的 Discussion and Highlights 直接描述 fouling susceptibility、清潔／沖洗／鈍化與 L1–L5 commissioning baseline
boundary: 動態方法頁沒有提供具名專案的 pass／fail、冷卻液 action limit、長期可靠度或供應商責任結果
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: inference
status: active
claim: 一份可部署的冷卻液生命週期合約至少要固定操作包絡、化學基準、浸液材料與變更控制、潔淨度與污染預算、試運轉基準、長期監測與行動責任六欄；CDU 額定容量或一次壓測／漏測不能替代這六欄
supporting_source_ids: S3,S7,S8
contrary_source_ids:
as_of: 2026-08-12
basis: S7 把 fluid、materials、startup sample 與 monitoring 串成生命週期，S3 補足四類失效與全流程 cleanliness，S8 再把施工啟動及 L4／L5 baseline 接到 commissioning；六欄是對三份文件的系統工程整理
boundary: 六欄是研究檢查框架，不宣稱所有專案採相同流體、門檻、取樣頻率、責任分工或必須由單一供應商承擔，也不形成商業或財務判定
verification_needed: 需具名多供應商量產場域公開完整 fluid baseline、wetted-material list、cleaning／flushing／passivation、action limits、責任矩陣及長期趨勢驗證完整性
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 冷源到伺服器要交接五次

沿著冷卻液前進的方向讀這張表：先從機房設施把熱交給冷卻設備，再經循環水路、機櫃分流與
伺服器冷板；最後還要讓建築控制和 IT 控制指向同一座機櫃。每一列都是一個雙方必須共同確認
的交接點，不代表左邊或右邊必然由某一類供應商獨占。

| 交接點 | 這一段由誰或什麼負責 | 雙方要說清楚什麼 | 沒說清楚會怎樣 | 本輪依據 |
|---|---|---|---|---|
| 1. 機房設施 ↔ 冷卻設備 | 設施冷源、熱交換器與一次側管路 | 供回水溫、壓力、流量、水質、可用性與維修責任 | 冷源不足、污染、壓差不合，雙方都以為對方會處理 | OCP 排除範圍＋Lenovo 實作指引 |
| 2. 冷卻設備 ↔ 循環水路 | 泵浦、熱交換器、二次側管路與控制 | 目標溫度、流量、壓差、過濾、備援與告警 | 泵浦故障、過濾器堵塞或控制不穩 | Lenovo 指引＋NVIDIA 控制資料點 |
| 3. 循環水路 ↔ 機櫃分流 | 管路、快速接頭、分流器與閥件 | 介面尺寸、材料、壓降、漏液偵測與隔離方法 | 接頭漏液、流量失衡或維修時無法隔離正確區段 | OCP 工作項目＋NVIDIA 隔離控制點 |
| 4. 機櫃分流 ↔ 伺服器冷板 | 伺服器托盤、冷板與內部管路 | 熱負載、流動阻力、流量、材料與污染控制 | 局部過熱、腐蝕、堵塞或冷板失效 | OCP 責任邊界＋Lenovo 水質與材料指引 |
| 5. 建築控制 ↔ IT 控制 | 感測器、事件傳遞、叢集管理與操作人員 | 機櫃身分、讀值品質、安全限制、下令與確認責任 | 隔離錯誤機櫃、送出無效設定值或告警無人負責 | NVIDIA DSX 資料契約 |

這張表刻意不指定「誰一定是贏家」。同一專案可以由 ODM、冷卻設備商、機電承包商、
設施營運方與平台商分別負責不同列；真正的商業價值要看合約責任、驗收、維護與收入分母，
不是產品型錄涵蓋的方框數。

## 水質不是一個數字：先寫六欄流體生命週期合約

額定散熱能力回答「設備在指定條件下能帶走多少熱」；流體生命週期合約回答「這些條件能否
在施工、填充、運轉、維修與換件之後仍然成立」。兩者都重要，但不能互相代替。研究一座
液冷場域時，至少要把下列六欄寫到能由不同團隊重複核對。

| 合約欄位 | 必須固定什麼 | 怎麼驗 | 失敗訊號 | 不能被什麼替代 |
|---|---|---|---|---|
| 1. 操作包絡 | 流體類型、供回水溫、壓力、流量、熱負載與過濾條件 | 最差條件測試與趨勢資料 | 流量、壓差或換熱能力偏離設計區間 | CDU 名牌容量或單一穩態測點 |
| 2. 化學基準 | 初始配方、pH、導電度、硬度、TSS、抑制劑／殺生劑與合格範圍 | 填充前檢驗、啟動樣本與實驗室 QA | 讀值持續漂移、顆粒或外觀異常 | 「使用純水」這種沒有數值與樣本的描述 |
| 3. 浸液材料與變更控制 | 所有金屬、塑膠、密封、接著劑、塗層及替代料 | 材料清單、流體相容性評估與每次變更重審 | 新材料後出現腐蝕、膨潤、脆化或沉積 | 單一元件材質聲明或供應商列名 |
| 4. 潔淨度與污染預算 | 製造、運送、現場管路、接管與維修可容許的顆粒／殘留 | 清潔封存、濾材檢查、沖洗終點與樣本 | 濁度、TSS、濾材負載或壓差上升 | 只在設備出廠時做一次清潔 |
| 5. 試運轉基準 | 清洗、沖洗、必要時鈍化、填充、排氣、取樣與留樣順序 | 有簽核的程序、代表性基準樣本與 L4／L5 測試 | 啟動後很快污染，卻無法分辨原始或新增問題 | 壓測、漏測或單件 FAT |
| 6. 監測與行動責任 | 取樣點、頻率、趨勢、行動門檻、複驗、隔離、換液與復原責任 | 儀表／實驗室交叉核對、趨勢圖與演練紀錄 | 告警存在但沒有人能判斷或執行下一步 | BMS 上有一個「水質正常」燈號 |

OCP 2022 指引的 Table 1 提供一組 **water-based、non-PG TCS 的典型起點**：TSS 小於
5 ppm、25°C 導電度小於 1,500 μS/cm、pH 8.0–10.5、運轉中細菌小於 100 CFU/mL。
這些數字有助於理解規格必須帶單位、溫度與流體範圍，卻不是跨專案的通用答案；PG 配方、
介電液、FWS 水質、不同材料與客戶條件都必須另行評估。研究上應先問「這是哪一段迴路、哪種
流體、哪份材料清單、哪個版本」，再判斷數值能否比較。

## 四種品質失效不是同一種髒

「水髒了」無法指向可執行的處置。Lenovo 把水質風險拆成四類；OCP 與 ASHRAE 的啟動樣本、
沖洗及長期趨勢，則提供區分「一開始就帶入」與「運轉後才生成」的時間軸。

| 失效類型 | 常見可能成因 | 應一起看的觀測 | 可能造成的系統結果 | 要補的處置證據 |
|---|---|---|---|---|
| 結垢（scaling） | 礦物濃度、溫度或化學條件讓固體析出 | 硬度、pH、導電度、溫度與換熱趨勢 | 流道或換熱面沉積，熱阻與壓降增加 | 水處理紀錄、沉積物分析、清洗前後效能 |
| 污堵（fouling） | 施工殘留、顆粒、密封碎屑或不合格流體進入 | TSS、濁度、濾材負載、流量與壓差 | 濾材或細流道堵塞，支路流量失衡 | 污染來源、沖洗終點、濾材與樣本紀錄 |
| 腐蝕（corrosion） | 流體與浸液材料不相容，或抑制劑與化學條件失控 | pH、導電度、抑制劑、材料變更與外觀 | 材料劣化、產生顆粒，甚至形成漏液風險 | 完整材料清單、相容性重審與原因分析 |
| 微生物生長 | 細菌進入並在適合條件下繁殖 | 細菌數、外觀、濾材負載、殺生程序與趨勢 | 生物膜、堵塞、腐蝕或水質持續惡化 | 取樣品質、處理紀錄、復驗與再發監測 |

單次超標只能說「某個觀測點異常」，不能單獨證明根因。若沒有啟動基準、代表性取樣、材料
與維修變更紀錄，就很難分辨問題來自原始填充、現場施工、某次換件，還是長期化學漂移；
也無法把責任公平地交給設施端、整合商、設備商或營運方。

## 從文件要求到長期營運要過五關

這張表回答「看到哪一種證據，研究判定才可以往前一格」。產品出現在平台清單只是第三關；
前面仍要有清楚範圍與單件測試，後面還要有具名場域驗收、長期運作與公司財務資料。

| 先過哪一關 | 看到什麼才算往前 | 還不能因此判定 |
|---|---|---|
| 1. 責任與範圍寫清楚 | OCP 定義技術冷卻水路的介面與排除範圍 | 某一項產品是否合格、某座場域會如何實作 |
| 2. 零件與設備通過測試 | 冷板、快速接頭、分流器與冷卻設備有可重現測試 | 混合多家產品後能否通過整套系統驗收 |
| 3. 平台列出具名產品 | NVIDIA Marketplace 出現可定位的型號與原始狀態 | 現場水質、控制整合、場域驗收、客戶採購與收入 |
| 4. 具名場域完成驗收 | 場域有介面控制文件、驗收測試、漏液隔離與備援切換結果 | 長期可靠度與全生命週期維護成本 |
| 5. 長期運作與財務出現 | 有部署規模、故障率、維護紀錄與供應商財報 | 未揭露的專案仍不能靠市場敘事反向猜測 |

## 研究判定

- **目前可以確定**：液冷是跨設施水路、技術冷卻水路、伺服器、控制與維護的介面系統；單一冷卻設備被平台列出，不足以代表整座場域已能穩定部署。
- **仍不能推到公司**：目前高信心只涵蓋架構與證據階梯；公司供貨、訂單、收入、市占、毛利及完整方案責任仍未驗證。
- **相對第八站新增了什麼**：研究從容量與供應狀態，前進到責任交接、感測、隔離與維護，不是再做另一張設備排名。
- **何時才能升為公司研究**：客戶與供應商要能雙向確認責任範圍、場域驗收、部署規模與可辨識財務結果。

## 來源

- [OCP：Cold Plate Cooling Loop Requirements Rev 2](https://www.opencompute.org/documents/cold-plate-cooling-loop-requirements-rev-2-pdf)
- [OCP：Cold Plate Sub-Project](https://www.opencompute.org/community/cold-plate)
- [OCP：Water-Based Transfer Fluids Guidelines](https://www.opencompute.org/documents/guidelines-for-using-water-based-transfer-fluids-in-single-phase-cold-plate-based-liquid-cooled-racks-final-pdf)
- [Lenovo：Neptune Direct Water-Cooling Standards](https://lenovopress.lenovo.com/lp2018-lenovo-neptune-direct-water-cooling-standards)
- [ASHRAE：AI Data Center Commissioning & Performance Validation](https://www.ashrae.org/technical-resources/ai-data-center-framework/commissioning-performance-validation)
- [NVIDIA：DSX Exchange BMS Integration](https://docs.nvidia.com/dsx-exchange/bms-integration)
- [NVIDIA Marketplace：DSX Infrastructure validated CDU list](https://marketplace.nvidia.com/en-us/enterprise/dsx-infrastructure/)
- [公開資訊觀測站](https://mops.twse.com.tw/mops/web/index)

## 族群影響

<!-- impact
group_id: thermal
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: cold plate、QD、manifold、CDU、流體與 leak isolation 都是散熱族群的可驗證搜尋路由，且責任邊界比單一容量更能區分商業成熟度
evidence_boundary: 不把產品存在、平台列名或規格必要性改寫成具名客戶、site acceptance、訂單、收入或毛利
-->

<!-- impact
group_id: powersupply
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: CDU 泵浦、控制、冗餘電源、BMS 與 rack 電液隔離形成電源供應族群的相鄰整合路由
evidence_boundary: 產品組合較寬不等於承擔完整 liquid loop 合約或取得較高財務價值，需合約與分部資料驗證
-->

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: ODM 位於 ITE、rack manifold、BMC／cluster manager 與 site integrator 的交界，可能承擔介面整合與驗收責任
evidence_boundary: 平台生態系列名、伺服器產品或 MOU 不證明 ODM 承包 site-level FWS／TCS、維護或財務貢獻
-->

## 監測器

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C4,C5,C7
metric: OCP 與 NVIDIA 是否發布新版 requirement、qualification、BMS contract 或 site-level validation，改變 FWS／TCS／ITE／control 責任邊界
source_ids: S1,S3
watch_source_ids: S2,S4,S5
frequency: monthly
next_check: 2026-09-03
trigger: 新文件提供可重現 interface test、site commissioning、leak isolation、field reliability 或責任矩陣
invalidation: 新版標準或 field evidence 顯示單一設備 qualification 已足以覆蓋本文所列介面與場域風險
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C6
metric: 台灣 thermal、powersupply、serverodm 公司是否公開可雙向核對的液冷合約責任、site acceptance、部署分母與財務貢獻
source_ids: S1,S3,S4
watch_source_ids: S6
frequency: quarterly
next_check: 2026-09-30
trigger: 客戶與公司文件共同指向具名場域、責任範圍、驗收、量產部署及收入／毛利分母
invalidation: 公司明確只供單件且不承擔整合，或專案長期停在 MOU／PoC／sample 而未進場域驗收
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C8,C9,C10,C11,C12
metric: 多供應商 TCS 是否公開完整的操作包絡、流體基準、浸液材料與變更控制、污染預算、試運轉樣本、監測門檻及動作責任
source_ids: S3,S7,S8
watch_source_ids: S2,S8
frequency: monthly
next_check: 2026-09-03
trigger: 具名多供應商量產場域發布 fluid COA／baseline、wetted-material list、cleaning／flushing／passivation、sampling／action limits 與 field trend
invalidation: 標準化密閉迴路以跨更新週期的長期 field evidence 證明設備 qualification 已固定全部六欄，新增材料或維修變更也不需重新評估
-->

## 什麼會推翻這篇

- 具名量產場域的文件若證明單一冷卻設備測試已同時完成設施水路、循環水路、伺服器、控制、流體、維護與長期可靠度的共同驗收，而且沒有額外交接缺口，就會推翻本文的主要判定。
- OCP 或平台商若刪除多數介面工作項目，並以可重現的場域資料證明模組化混搭不再需要逐一驗證材料、流體、快速接頭、分流器與控制，也會削弱本文。
- 若台灣公司的公開文件始終無法說明責任範圍與部署規模，族群圖譜就只應保留為搜尋路線，不應升格為公司商業曝險。
