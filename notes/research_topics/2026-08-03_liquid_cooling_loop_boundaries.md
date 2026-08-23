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

<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_liquid_heat_flow_atd_pressure_and_pump_power_passport_without_thesis_clock_refresh
evidence: sources:S9,S10,S11,S12
-->

<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_dew_point_local_surface_and_economizer_passport_without_thesis_clock_refresh
evidence: sources:S13,S14,S15,S16
-->

<!-- transition
date: 2026-08-23
from: triaged
to: triaged
reason: added_liquid_leak_blast_radius_and_service_loss_denominator_without_thesis_clock_refresh
evidence: sources:S17,S18,S19
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **FWS（Facility Water System，設施水系統）**：資料中心設施端的水路，位於冷源與 CDU 之間；它負責把熱帶往冷卻塔、乾式冷卻器或冰水主機。OCP Cold Plate Rev 2 沒有把這一段納入 TCS 規格範圍。
- **TCS（Technology Cooling System，技術冷卻系統）**：從 CDU 出發，經機櫃管路、分流器與伺服器冷板再回到 CDU 的循環水路；冷卻液、管路、接頭、壓力、流量與維護都在這一圈互相影響。
- **ITE（Information Technology Equipment）**：伺服器、加速器與內部冷板等 IT 設備。規格若只管 TCS，不代表 ITE 端所有設計與責任都已被涵蓋。
- **CDU（Coolant Distribution Unit，冷卻液分配單元）**：透過泵浦、熱交換器與控制，把伺服器迴路的熱交給設施水路。它是一個重要節點，不等於整套液冷系統。
- **BMS（Building Management System）**：建築管理系統，收集溫度、流量、壓差、漏液與設備狀態，並在安全 guardrails 內執行控制或隔離。
- **BMC／BCM（基板管理控制器／Base Command Manager）**：BMC 位在伺服器或托盤內，處理本機感測與動作；本文 NVIDIA 文件中的 BCM 是較上層的機櫃與叢集管理軟體。兩者名稱相近，但角色不能互換。
- **MQTT／broker（訊息佇列遙測傳輸／訊息代理服務）**：MQTT 是 BMS 與管理軟體交換事件和狀態的發布／訂閱協定，broker 是轉送訊息的伺服器。固定 heartbeat 只表示通訊節拍，不等於動作完成時間。
- **DSX**：NVIDIA 用來描述 AI factory 基礎設施資料、控制契約與驗證生態的文件／平台名稱；列入 DSX 不等於場域已完成驗收。
- **QD／UQD（快速接頭／通用快速接頭）**：QD 是讓液冷管路能快速拆接的連接器；UQD 是 OCP 推動的通用介面方向。單一接頭通過測試，不代表混用不同管路、流體與 manifold 後整套系統仍可靠。
- **PBMC（Pivoting Blind Mate Coupling，旋轉式盲插接頭）**：一種允許一定偏移、可在模組插入時自動接合液路的快速接頭設計。接頭規格通過不代表整條迴路或場域已驗收。
- **PSIG（每平方英吋磅力的表壓）**：以當地大氣壓為零點的壓力單位；0 PSIG 不等於絕對真空。比較漏液或接頭測試時，要連同流體、溫度、方向與量測方法一起看。
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
- **液體捕熱率（liquid heat capture ratio）**：IT 用電轉成的熱有多少比例真正進入液體迴路；剩餘熱量仍可能由空氣或其他路徑帶走，所以 IT MW 不一定等於液體 MW。
- **迴路溫升（ΔTloop）**：同一側冷卻液的回水溫減供水溫；它和流體性質、流量共同決定液體帶走多少熱。
- **接近溫差（ATD）**：液對液 CDU 中，TCS 供水溫減 FWS 供水溫；它描述熱交換器兩側的接近程度，不是 TCS 回水減供水的迴路溫升。
- **比熱／密度**：比熱表示每單位質量升高一度能吸收多少熱，密度把質量流量連到體積流量；水與不同濃度的乙二醇／丙二醇不能共用同一換算常數。
- **泵浦揚程／流動阻抗**：泵浦揚程是泵能克服的壓力能力，流動阻抗是管路、接頭、冷板、閥件與濾網造成的壓力損失；兩條曲線交會才是實際工作點。
- **泵浦／馬達效率**：輸入電力有多少轉成流體的壓力與流量；效率會隨工作點改變，不能只用最高效率或銘牌功率估全年耗能。
- **LPM／LPM/kW**：LPM 是每分鐘公升的體積流量；LPM/kW 是每一千瓦液體熱負載配置多少流量。兩者都不是散熱功率，必須連同流體與溫差閱讀。
- **OAI／OAM 與 PG25**：OAI 是 OCP 的 Open Accelerator Infrastructure，OAM 是其中的加速器模組；PG25 是約 25% 體積濃度等級的丙二醇水溶液。本文引用的是這組特定邊界下的指引，不是所有液冷平台通則。
- **PQ 曲線／dP**：PQ 曲線把壓力與流量連在一起，dP 是兩點間壓差；泵浦曲線與整條流路阻抗的交點才是工作點，單一最大流量或零件壓差都不夠。
- **PUE／WUE**：PUE 比較資料中心總能源與 IT 能源，WUE 描述用水效率；泵浦或 TCS 的單點效率只是其中一小段，不能直接推成整座場域的 PUE／WUE。
- **DOE**：本文的 DOE 指美國能源部；引用它的一般泵浦生命週期成本指南來解釋流量、揚程、效率與時間剖面，不代表能源部替任何 CDU 或資料中心背書。
- **NBS／NIST**：NBS 是美國國家標準局的舊稱，後改組為 NIST。本文用 NBS 1970 論文的公式做露點教材，不表示 NIST 替任何液冷設計背書。
- **W1／W2／W3／W4／W5**：ASHRAE 液冷設備的供水溫度 classes；數字較高代表可接受更暖供水的不同設計邊界，不是設備品質或供應商排名。
- **Prineville**：OCP 文章記錄的一座美國資料中心及其 air-side economizer 控制事件；本文只引用局部表面結露機制，不把單一事件外推成液冷故障率。
- **CAP1／PCB**：CAP1 是 OCP 受控箱體案例中被追蹤表面溫度的一顆電容，PCB 是電路板；兩者同處一台電源內卻位於露點兩側。
- **Guideline／Guidelines／requirement**：guideline／guidelines 是設計指引，requirement 是必須滿足的要求；兩者都不等於產品已驗收、場域已量產或公司已認列收入。
- **乾球溫度（Dry-bulb temperature）**：一般溫度感測器讀到的空氣溫度；它要和同一位置、同一時間的相對濕度一起使用，才能換算該處露點。
- **相對濕度（RH）**：當下水蒸氣分壓相對於同溫度飽和水蒸氣分壓的比例。相同 RH 在不同乾球溫度下不代表相同含水狀態或相同露點。
- **露點（Dew point）**：在水蒸氣分壓不變下，空氣降溫至飽和時的溫度；表面若低於其周圍空氣的局部露點，就進入可能結露的熱力邊界。
- **最冷局部表面**：管路、接頭、分流器、冷板、電容、機殼或其他表面中溫度最低的位置。機房平均溫度、供液感測點與最冷表面通常不是同一參考面。
- **局部露點裕度**：最冷局部表面溫度減同位置、同時間露點。正值表示表面仍高於露點，零附近需納入感測與控制不確定度，負值表示表面已低於露點。
- **結露／non-condensing**：水蒸氣在較冷表面形成液態水；標示 non-condensing 是操作條件限制，不是只要室內 RH 低於某個百分比就自動成立。
- **水側 economizer**：在戶外條件合適時，以熱交換器和冷卻塔或乾式冷卻器先帶走熱、降低或繞過冰水主機負載的運轉模式；可用時數取決於氣候、供水設定、熱交換器與控制。
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
- **處置影響範圍（blast radius）**：一次告警或安全動作會讓多少托盤、機櫃、整列機櫃或冷卻設備失去電力或冷卻。範圍越大不一定越安全或越差，還要看定位可信度與硬體損害風險。
- **誤報／漏報**：誤報是沒有真正漏液卻觸發告警或停機；漏報是已漏液卻沒有及時被偵測。兩者代價不同，不能只用「告警有動作」判定系統可靠。
- **受影響機櫃小時（affected rack-hours）**：每次事件中，受影響的機櫃等價數乘上無法提供服務的時間，再對事件加總。它比只數告警次數更接近容量損失，但仍不能替代 accelerator-hours、job-hours、設備損害與復原成本。
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
- 所以一台冷卻設備通過平台驗證，只證明一個節點；完整部署還要讓冷源、管路、接頭、分流器、冷板、控制與維護一起通過驗收，並把液體帶走的熱、流量、壓差、泵功，以及局部露點裕度分帳。

### 為什麼重要

第八站回答一台冷卻設備能帶走多少熱、平台把它列在哪個供應階段；這一站接著問整套系統如何
運作。液冷的風險常發生在交接點：設施水質會影響熱交換器，管路材料與冷卻液會影響腐蝕，
接頭與分流器會影響漏液和維修，伺服器內部阻力會影響流量分配，控制系統則決定告警能否指向
正確機櫃、隔離動作能否真的執行。只有把這些責任接起來，才知道問題發生時由誰處理。

同樣地，「機房 60% RH」或「供液 20°C」都不是完整防結露證據：還要知道兩個讀值的時間與
位置、最冷表面在哪裡、露點裕度多少，以及 economizer／冰水主機切換時控制是否跟得上。

### 接下來怎麼追

- 追蹤 OCP 是否把目前的要求文件補成可重現的冷板、冷卻液、快速接頭與整套迴路測試，並保存每次版本變化。
- 追蹤 NVIDIA 是否從設備列名，往現場試運轉、資料完整性、漏液隔離與長期可靠度增加公開欄位。
- 查台灣散熱、電源供應與伺服器代工公司是否說清楚責任範圍：只供元件、供機櫃水路、整合冷卻設備與控制，還是承擔場域驗收和維護；再核對部署規模與財務資料。
- 追具名 CDU 是否在同一流體、FWS／TCS 溫度、流量、ATD、揚程、阻抗與備援條件下公布容量曲線，而不是只報一個最大 kW。
- 追具名量產場域是否以共同時間鍵公開乾球溫度、RH、露點、最冷表面、供回液溫、感測不確定度、控制模式與結露事件，而不是只報機房平均值。

### 想一想

- 如果客戶現場出現水質不合、流量不足或告警指向錯誤機櫃，應由設施端、冷卻系統整合者、伺服器供應商還是控制系統負責？現有文件能分清嗎？
- 快速接頭、分流器、冷板與冷卻液各自通過單件測試，是否足以證明混合多家供應商後仍能長期可靠運作？
- 同一家公司若同時賣電源、冷卻設備與控制，研究上要看到哪些合約、驗收與收入資料，才能證明它真的承接較多價值？
- 若兩台 CDU 都標示 1MW，但一台在較寬 ATD、較低流量或較容易的壓差條件下額定，兩個 1MW 還能直接相比嗎？
- 若室內一直顯示 60% RH，溫度突然升高或某個金屬零件仍很冷，單看牆上的濕度計能排除結露嗎？

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

<!-- research_source
source_id: S9
role: standard
source_kind: living_index
publisher: ASHRAE
title: ASHRAE Handbook — Hydronic Heating and Cooling, Chapter 13
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://handbook.ashrae.org/Handbooks/S20/SI/s20_ch13/s20_ch13_si.aspx
locator: 2.2 Thermal Components，Heat Transferred to or from Water；熱傳率由質量流量、比熱與跨設備溫升／溫降相乘，標準條件水的密度 1000kg/m³、比熱 4.18kJ/(kg·K)，並明示可用於單一設備或整段配管的 heat-carrying capacity
limitation: 這是 ASHRAE 現行線上 Handbook 的一般 hydronic 方法，頁面會更新且不是 AI data center TCS 規格；標準水常數不能套到 PG25、其他濃度／溫度或未量測流體，也不證明 CDU 額定、場域驗收或財務
independence_group: ashrae
-->

<!-- research_source
source_id: S10
role: standard
source_kind: document
publisher: Open Compute Project
title: OCP OAI System Liquid Cooling Guidelines
published_at: 2023-03-03
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.opencompute.org/documents/oai-system-liquid-cooling-guidelines-in-ocp-template-mar-3-2023-update-pdf
locator: PDF pp.6–8、11–13；p.7 把 PG25 的 7.5–12°C coolant rise 對應 1.25–2.0LPM/kW，10°C 典型目標對應 1.5LPM/kW；pp.12–13 說明 flow、pressure drop、流體性質、冷板與拓撲的取捨
limitation: PDF 正文未標日期，published_at 依官方 canonical URL 的 Mar-3-2023 update 正規化且不主張文件批准時刻；本文是 OAI／OAM guideline、明示不是共同 specification，數值與案例不能外推成所有 AI rack、流體、CDU 或客戶 pass line；官方端點對命令列回 403，僅以官方 PDF viewer 逐頁核對，無本地 SHA
independence_group: open-compute-project
-->

<!-- research_source
source_id: S11
role: standard
source_kind: document
publisher: Open Compute Project
title: Liquid to Liquid CDU Test Methodology and Performance Rating Revision 1.0
published_at: 2024-08-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.opencompute.org/documents/ocp-wp-l-lcdu-test-methodology-performance-rating-r1-pdf
locator: PDF pp.15–21；thermal performance 需綁 heat load、FWS／TCS flow 與 temperature、ATD，TCS head 與 FWS impedance 要用 pressure-versus-flow curve；額定建議另固定 fluid、FWS temperature、1.5LPM/kW、ATD 與 head／impedance
limitation: 頁尾只標 August 2024，published_at 以 2024-08-01 做月精度正規化且不主張日精度，version table 另有 11/01/2024 記載；這是 Rev 1.0 方法與建議，不是所有 CDU 的強制共同額定、實際場域曲線或財務證據；官方端點對命令列回 403，僅以官方 PDF viewer 逐頁核對，無本地 SHA
independence_group: open-compute-project
-->

<!-- research_source
source_id: S12
role: other_primary
source_kind: document
publisher: U.S. Department of Energy
title: Pump Life Cycle Costs — A Guide to LCC Analysis for Pumping Systems, Executive Summary
published_at: 2001-01-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www1.eere.energy.gov/manufacturing/tech_assistance/pdfs/pumplcc_1001.pdf
locator: PDF file pp.7–9，尤其 file p.8（印刷 p.6）Energy Costs；泵浦輸入功率由流量、揚程、比重、泵浦與馬達效率共同決定，變動輸出要按時間建立使用剖面，節流、洩壓或 bypass 會降低效率並增加耗能
limitation: 文件頁尾只標 January 2001，published_at 以 2001-01-01 做月精度正規化且不主張日精度；這是 DOE、Hydraulic Institute 與 Europump 的一般泵浦 LCC 指南，不是資料中心 CDU 測試、特定泵浦曲線、電價或場域年度耗能
independence_group: us-department-of-energy
-->

<!-- research_source
source_id: S13
role: standard
source_kind: document
publisher: National Bureau of Standards
title: The Use of Dew-Point Temperature in Humidity Calculations
published_at: 1970-08-21
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://nvlpubs.nist.gov/nistpubs/jres/74C/jresv74Cn3-4p117_A1b.pdf
locator: PDF 印刷 pp.117–120（file pp.1–4）；p.118 定義 RH 與 dew point，p.119 給 Celsius Antoine 常數 A＝8.10765、B＝1750.286、C＝235.0 及由 dry-bulb／RH 推露點的式 (3)
limitation: 本文使用的是標準大氣壓附近、0–60°C 水蒸氣的工程公式；不能替代現代場域校正、感測誤差、局部氣流、凝結成核或設備 qualification。官方 PDF SHA-256 a76d4d8fbb2fa4bd59336862fea8fbdb43bcf88cdbdbbac1c4b9b01bbcf6ba8e，共 6 頁
independence_group: nist
-->

<!-- research_source
source_id: S14
role: standard
source_kind: living_index
publisher: ASHRAE
title: ASHRAE Handbook — Data Centers and Telecommunication Facilities, Chapter 19
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://handbook.ashrae.org/Handbooks/A15/SI/a15_ch19/a15_ch19_si.aspx
locator: Internal Liquid-Cooling Loop 段落指出 rack 內循環液通常維持高於露點；Environmental Guidelines for Liquid-Cooled Equipment 的 W1–W5、Table 2 與其後文字說明供水溫、基礎設施、condensation prevention 及 configuration-specific flow／pressure
limitation: 這是會更新的 ASHRAE Handbook 一般架構，表內 classes 與原則不是任何具名 AI rack、CDU、場域控制設定、感測精度、可用時數或節能實績
independence_group: ashrae
-->

<!-- research_source
source_id: S15
role: other_primary
source_kind: document
publisher: Open Compute Project
title: Learning Lessons at the Prineville Data Center
published_at: 2013-08-07
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.opencompute.org/blog/learning-lessons-at-the-prineville-data-center
locator: Issue Analysis；控制箱把 RH 拉到 97%、10 分鐘內由 15°C 升至 30°C，CAP1 表面約第 6 分鐘低於露點並再結露約 9 分鐘，而 PCB 全程高於露點且無結露；Corrective Actions 另列控制與監測修正
limitation: 這是 air-side economizer／蒸發冷卻事件及受控箱體重現，不是液冷管路測試、現代 AI rack、跨場域故障率或供應商比較；本文只用它證明局部表面與時間動態，不能外推發生率、根因分布或財務
independence_group: open-compute-project
-->

<!-- research_source
source_id: S16
role: other_primary
source_kind: document
publisher: U.S. Department of Energy
title: Cooling Water Efficiency Opportunities for Federal Data Centers
published_at: 2019-01-09
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.energy.gov/cmei/femp/cooling-water-efficiency-opportunities-federal-data-centers
locator: Space Temperature and Humidity Control 與 Use of Water-Side Economizing Strategies；說明過窄設定會增加負荷，water-side economizer 可用串聯熱交換器先冷卻或在適合戶外條件下繞過 chiller
limitation: 這是以 cooling tower、chilled-water 與 air-cooled IT rack 為主的一般 FEMP 指引；可用時數與節能取決於氣候、設定、控制及系統配置，不能外推特定液冷場域、產品、PUE／WUE、收入或毛利
independence_group: us-department-of-energy
-->

<!-- research_source
source_id: S17
role: standard
source_kind: document
publisher: Open Compute Project
title: Rope Leak Sensor Base Specification Revision 1.0.0
published_at: 2026-02-02
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://www.opencompute.org/documents/rope-leak-sensor-base-specification-r1-0-0-final-pdf
locator: PDF 印刷 pp.10–12；Table 5 分開 normal、leak、open-circuit fault 與 power-cable presence，pp.11–12 說明接觸液體即輸出不分量的二元訊號、使用者自定 timer／shutdown／rack-CDU 動作及 false-alarm reduction
limitation: 這是 16 頁、effective 2026-02-02 的 leak-sensor-rope base specification；只規定感測器特徵、介面與範例處置，不量測漏液量、位置、端到端隔離延遲、場域故障率或停機。官方 PDF 端點可由瀏覽器逐頁核對，但命令列下載回 403，因此本輪無本地 SHA
independence_group: open-compute-project
-->

<!-- research_source
source_id: S18
role: company_release
source_kind: document
publisher: NVIDIA
title: NVIDIA Mission Control Integration with Building Management System, Software Installation Guide 2.1.0
published_at: 2026-07-16
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://docs.nvidia.com/mission-control/docs/nmc-software-installation-guide/2.1.0/integration-of-bms-with-bcm.html
locator: Introduction、Prerequisites、Heartbeat、Fault Type and Handling Recommendations 與頁尾 last updated；分列 tray、rack、row、sensor fault 的 BMC／Mission Control／BMS 建議動作，以及 customer-provided BMS／MQTT 與 license 前置條件
limitation: 這是 NVIDIA GB200／GB300 NVL72 的功能、設定與建議責任矩陣，不是事故紀錄、動作成功率或 SLA；5 秒是 expected heartbeat interval，不是 leak-to-safe-state 上限，row-level 動作也不能外推為整座資料中心停機
independence_group: nvidia
-->

<!-- research_source
source_id: S19
role: standard
source_kind: document
publisher: Open Compute Project
title: Pivoting Blind Mate Coupling Specification Revision 1.0
published_at: 2026-04-15
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://www.opencompute.org/documents/pbmc-design-specification1-0-final-pdf
locator: PDF viewer indices 24、40（頁面標示 pp.25、41）的 Table 6.0 與 Table 7.1 tests 7.1-1～7.1-3；spillage 要求在 0／75 PSIG 為 ≤0.06／≤0.12cm³，實測條件則用 water、垂直方向、0／80 PSIG，並分列 pressure-drop、air-inclusion 與 same-supplier／interoperability 最低樣本
limitation: 這是 PBMC connector conformance specification，不是整條 loop、production site、field leak rate、維修時間或可用率證據；Table 6.0 的 75 PSIG requirement 與 7.1-3 的 80 PSIG test condition 必須原樣分列，重複 mate cycles 也不能當成獨立 fleet samples。官方端點可逐頁核對但命令列下載回 403，本輪無本地 SHA
independence_group: open-compute-project
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

<!-- research_claim
claim_id: C13
label: verified
status: active
claim: ASHRAE 的 hydronic 方法把水側熱傳率寫成質量流量、比熱與跨設備溫升／溫降的乘積，並指出同一方法可核對單一設備或整段配管的 heat-carrying capacity
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-08-14
basis: S9 Chapter 13 的 Heat Transferred to or from Water 直接定義 q、mass flow、specific heat、temperature difference 與標準水條件
boundary: 只證實一般穩態熱平衡方法；流體性質、感測位置、熱損、未進液體的熱、動態負載與量測不確定度都要另列，不能用標準水常數替 PG25 或直接宣布場域通過
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
claim: OCP OAI 液冷指引在 PG25 與其指定邊界下，把 7.5–12°C 冷卻液溫升對應到 1.25–2.0LPM/kW，並把 10°C、1.5LPM/kW 當典型設計目標；同頁明示較高溫升有利 PUE、但會犧牲 cooling performance，反之亦然
supporting_source_ids: S10
contrary_source_ids:
as_of: 2023-03-03
basis: S10 PDF p.7 的 Coolant Flow Rate 直接列出 coolant、溫升、LPM/kW 與 PUE／cooling performance 取捨
boundary: 這是 OAI／OAM guideline、不是共同規格；PG25、heat-exchanger allowance、平台拓撲與工作點都限定適用範圍，不可外推成純水常數、所有 rack 流量、PUE 實測或固定需求倍數
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
claim: OCP 的液對液 CDU Rev 1.0 方法要求把 cooling capacity 綁到流體、FWS 溫度、FWS／TCS 流量、TCS 揚程、FWS 阻抗與 ATD；TCS head 與 FWS impedance 又必須用 pressure-versus-flow curve 評估
supporting_source_ids: S11
contrary_source_ids:
as_of: 2024-08-01
basis: S11 PDF pp.15–20 的 thermal performance、TCS pressure head、FWS flow impedance 與 performance reporting 段落逐一列出額定條件及曲線
boundary: Rev 1.0 提供方法與建議，不表示所有供應商已採共同額定；單一最大 kW、單點 flow 或單點 dP 都不能替代完整 capacity／PQ curve、part-load、備援與場域驗收
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
claim: DOE／Hydraulic Institute／Europump 的泵浦 LCC 指南把輸入功率連到流量、揚程、流體比重、泵浦效率與馬達效率，並要求變動負載用時間剖面計算能耗；節流、洩壓與 bypass 不能被視為免費控制
supporting_source_ids: S12
contrary_source_ids:
as_of: 2001-01-01
basis: S12 file p.8（印刷 p.6）的 Energy Costs 直接給出公式、變動 output profile 與三種控制對效率／耗能的影響
boundary: 這是一般泵浦方法，不提供 CDU 專用效率、壓差、運轉時數、備援狀態或電價；本文的 Δp×體積流量÷綜合效率是同一功率關係的 SI 換寫，不是來源的 AI 場域實測
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
claim: 液冷容量研究應把 IT 用電、進入液體的熱、流體熱運能力、熱交換器 ATD、流路壓差與泵浦輸入功率分帳，再用同一份十欄熱工—水力護照連到備援、全年 duty profile、場域驗收與商業責任；只有最大 kW 或 LPM 不能推導部署價值與公司受惠
supporting_source_ids: S1,S3,S4,S9,S10,S11,S12
contrary_source_ids:
as_of: 2026-08-14
basis: S9 建立 heat-flow-temperature balance，S10 建立 coolant／ΔT／flow trade-off，S11 固定 CDU capacity、ATD 與 PQ curves，S12 補上泵功與時間剖面；S1／S3／S4 把算式放回 FWS／TCS／ITE 與控制責任
boundary: 六本帳與十欄護照是研究框架，不是唯一設計流程、跨 CDU 排名、PUE 或 WUE 計算、客戶 qualification、需求預測或財務歸因；不支持台灣公司訂單、收入、毛利或股價尚未反映
verification_needed: 同一 production site 的 IT load／liquid heat capture、fluid properties、FWS／TCS temperatures、flow／dP curves、pump efficiency／duty、heat rejection、raw telemetry、commissioning、BOM、合約及財務共同鍵
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C18
label: verified
status: active
claim: NBS／NIST 的 Antoine 關係把同位置乾球溫度與相對濕度轉成露點；因此相同 RH 在不同乾球溫度下可以對應不同露點，RH 本身不是可跨溫度比較的固定含水量
supporting_source_ids: S13
contrary_source_ids:
as_of: 1970-08-21
basis: S13 印刷 pp.118–119 先定義 RH 與 dew point，再以 Celsius 常數 B＝1750.286、C＝235.0 給出 (DP＋C)⁻¹＝(T＋C)⁻¹＋B⁻¹log₁₀(RH⁻¹)
boundary: 只證實標準大氣壓附近、0–60°C 水蒸氣的工程換算；公式不量測局部表面、感測誤差、氣流、熱慣性、凝結成核、滴水遷移或設備可靠度
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C19
label: verified
status: active
claim: ASHRAE 的資料中心章指出 rack 內循環液通常維持在露點之上以消除結露疑慮，W1／W2 的設計必須防止結露；較高供水溫可降低設施冷卻成本，但設備端要以增強熱設計守住元件溫度
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-08-14
basis: S14 Internal Liquid-Cooling Loop 與 Environmental Guidelines for Liquid-Cooled Equipment 直接連接 dew point、W classes、supply water temperature、condensation prevention 與 thermal design
boundary: 這是一般設計邊界，不提供任何具名場域的最冷表面、控制死帶、感測精度、economizer 可用時數、可靠度或成本；higher supply temperature 也不是無條件較佳
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C20
label: verified
status: active
claim: OCP 的 Prineville 受控箱體重現中，CAP1 表面約在溫度 ramp 第 6 分鐘低於露點並再結露約 9 分鐘，PCB 則全程高於露點且沒有結露，顯示同一設備內結露取決於局部表面溫度與時間
supporting_source_ids: S15
contrary_source_ids:
as_of: 2013-08-07
basis: S15 Issue Analysis 對 Figure 6 的文字說明逐一對應 CAP1、dew point、約 6 分鐘 crossing、後續約 9 分鐘 condensation，以及 PCB 無結露
boundary: 這是高溫高濕 air-side economizer 事件的受控箱體重現，不是液冷量產場域；不能外推現代 AI rack、冷板／QD 的結露率、故障率、材料效果或任何供應商財務
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C21
label: inference
status: active
claim: 液冷防結露與 economizer 研究應以同一時間、位置與運轉模式，把乾球溫度、RH、露點、最冷局部表面、供回液溫、感測與控制不確定度、告警／隔離、可用時數及財務分母綁成一份護照；單一機房 RH 或供液溫不能證明整套系統 non-condensing 或節能
supporting_source_ids: S3,S4,S13,S14,S15,S16
contrary_source_ids:
as_of: 2026-08-14
basis: S13 建立 dry-bulb／RH／dew-point 關係，S14 把 rack liquid、dew point、W classes 與設施成本連接，S15 顯示局部表面和控制動態，S16 補上 economizer 系統與氣候依賴；S3／S4 把量測與動作放回液冷責任邊界
boundary: 十欄護照是跨來源研究框架，不是 ASHRAE／NIST／OCP／DOE 的共同標準，不指定唯一裕度或控制算法，也不證明場域可用性、PUE／WUE、故障率、供應商訂單、收入、毛利或估值
verification_needed: 需具名 production site 以共同時間鍵公開 zone-level dry-bulb／RH、measured or derived dew point、surface map、FWS／TCS temperatures、sensor uncertainty、control transitions、condensation events、economizer hours、energy／water 及財務責任
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C22
label: verified
status: active
claim: OCP Rope Leak Sensor Base Specification 把正常、漏液、感測器 open-circuit fault 與電源線狀態分開，且明示感測繩接觸液體便輸出不分漏液量的 leak／no-leak 二元訊號；timer、停機及 rack manifold／CDU 中斷則是後續使用者與系統責任
supporting_source_ids: S17
contrary_source_ids:
as_of: 2026-02-02
basis: S17 Table 5 逐一列出四類訊號狀態，印刷 p.11 又明示 regardless of amount、discrete signal，並把 mitigation plan、timer／immediate shutdown 與超出 ITE 的 rack manifold／CDU 動作分開
boundary: 只證實規格所定義的訊號與責任層；二元告警不能量出漏液量、精確來源、嚴重度、誤報率、漏報率、隔離成功或服務損失
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
claim: NVIDIA Mission Control 2.1.0 的建議矩陣讓 tray、rack 與 row leak 對應不同 power／fluid 動作範圍，sensor fault 則要求現場檢查；整合前置條件包括 Mission Control license、客戶 BMS／MQTT broker 與網路連線
supporting_source_ids: S18
contrary_source_ids:
as_of: 2026-07-16
basis: S18 Introduction／Prerequisites 與 Fault Type and Handling Recommendations 逐列分配 BMC、BCM、BMS 的 tray、rack、row、sensor-fault 動作，並明示 license、customer-provided BMS、MQTT broker 和 TCP/IP
boundary: 這是具名平台的功能與建議責任矩陣，不證明客戶已部署、每個命令執行成功、5 秒內完成隔離、零誤報、避免停機或產生供應商財務；datacenter-level 感測位置也不能被改寫成整座 datacenter shutdown
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
claim: OCP PBMC Revision 1.0 把快速接頭的 spillage requirement 與 test condition 分開：Table 6.0 在 0／75 PSIG 要求 ≤0.06／≤0.12cm³，而 test 7.1-3 用 water、垂直方向與 0／80 PSIG，same-supplier 及 interoperability 每種組合至少三個樣本
supporting_source_ids: S19
contrary_source_ids:
as_of: 2026-04-15
basis: S19 印刷 p.25 Table 6.0 直接列出兩個壓力與 spillage 上限，印刷 p.41 test 7.1-3 列出 0／80 PSIG、water、vertical graduated-cylinder method、兩壓力結果及 minimum 3 per combination
boundary: Connector conformance pass 不能外推成零 field leaks、整條 loop 相容、場域可用率或修復時間；75 PSIG requirement 與 80 PSIG test condition 不互相替換，樣本也不是隨機場域或 fleet 分母
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C25
label: inference
status: active
claim: 漏液研究應把二元偵測、決策與已確認安全狀態分帳，並以同一事件護照保存漏液與流體、sensor fault／debounce、四段時間戳、tray／rack／row／CDU 處置範圍、殘餘冷卻、受影響 rack／node／job、復原再驗收及責任 owner；商業損失至少另算 affected rack-hours，而非只數告警或 connector pass
supporting_source_ids: S17,S18,S19
contrary_source_ids:
as_of: 2026-08-23
basis: S17 證明 signal 與 mitigation 分層且存在 false-alarm／fault 分支，S18 讓不同偵測層對應不同 power／fluid blast radius，S19 則把 connector requirement、test condition、interoperability 與樣本分母固定；九欄與 rack-hours 是把三者接到 service loss 的研究重組
boundary: 九欄護照與 affected rack-hours 不是 OCP／NVIDIA 共同標準，也不指定唯一 timer、隔離策略或安全優先序；它們不證明 field incident rate、MTTR、availability、設備損害、價格、部署、收入、毛利或估值
verification_needed: 需具名 production site 或代表性 fault injection 提供逐事件 raw signal、true／false／fault label、四段 timestamp、confirmed power／valve／CDU state、受影響 rack／node／job、復原再驗收及合約與財務共同鍵
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

## 漏液告警不是停機答案：先算會停哪裡、停多久

漏液繩比較像煙霧警報器，不是漏水流量計。OCP Rope Leak Sensor Base Specification 把
normal、leak、open-circuit fault 與電源線狀態分開；它又明說感測繩只要接觸液體，就輸出
不分漏液量的 leak／no-leak 二元訊號。這個訊號沒有自動回答液體從哪裡來、漏了多少、該停哪一段，
也沒有證明閥件或電源真的完成動作。因此要先拆開三層：

| 層次 | 它真正回答什麼 | 至少要留下什麼 | 不能被什麼替代 |
|---|---|---|---|
| 1. 偵測 | 感測器看到 leak、normal 或 fault 嗎 | 原始狀態、sensor／zone ID、時間、閾值、fault 與 debounce | 一個總告警燈 |
| 2. 決策 | 哪個控制器依哪條規則要求動作 | BMC／BCM／BMS owner、timer、告警可信度、requested action | 「系統會自動處理」 |
| 3. 執行與確認 | 電源、閥件或 CDU 是否真的到達安全狀態 | 命令、acknowledgement、實際 breaker／valve／flow／power state 與時間 | 已送出命令或 5 秒 heartbeat |

OCP 把 timer、立即停機、BMC／CPLD 動作列為依使用者安全要求而變的後續處置；rack manifold 或
CDU 中斷更明確在該感測器規格範圍外。規格也另外提醒 condensation、溫度漂移與感測器 fault
可能造成 false alarm。換句話說，感測器能「喊有水」，控制契約才決定誰相信、誰下令，現場狀態
又要獨立確認有沒有真的安全。

### 同一個 leak，托盤、機櫃與整列的影響範圍不同

NVIDIA Mission Control 2.1.0 提供一個具體但平台限定的責任矩陣。它不是場域成效，卻很適合
看懂為什麼「有自動隔離」仍少了一個分母。

| 文件中的偵測層級 | 建議路徑 | 可能失去服務的範圍 | 判讀界線 |
|---|---|---|---|
| Tray | compute tray 的 BMC 啟動 shutdown timer、所有 tray 通知 BCM；只有 switch tray 明寫由 BCM 用 OOB Redfish 關閉漏液 tray，另開現場檢查 ticket | 單一托盤或節點 | 不能把 switch-tray 動作外推到所有 compute tray |
| Rack，由 BCM 偵測 | BCM 建議立即關 power shelf DC output 並通知 BMS；BMS 再關該 rack breakers 與 supply／return valves | 單一機櫃 | 「立即」是建議文字，不是量過的端到端上限 |
| Rack，由 BMS 偵測 | BMS 關該 rack breakers 與供回液閥，再通知 BCM；Mission Control 欄為 N/A | 單一機櫃 | 執行者與事件來源不同，不能假設都經過同一控制路徑 |
| Row | BMS 關該 row 全部 rack breakers 與 row CDU，再通知 BCM | 一整列機櫃 | 這不是整座 data center shutdown，也沒有寫 row valves |
| Sensor fault／misreading | Mission Control 與 BMS 路徑都要求現場檢查 | 視人工處置而定 | 文件沒有說系統已自動辨識或消除誤報 |

這項整合還要求 Mission Control license、客戶提供的 BMS／MQTT broker 與 TCP/IP。頁面所寫的
default heartbeat「預期為 5 秒」，只說雙方多久交換心跳；它沒有定義 heartbeat timeout，也沒有
量出 leak detection、決策、命令、breaker／valve 動作與復原各花多久。把 5 秒寫成「五秒完成隔離」
會把通訊節拍冒充安全 SLA。

### 接頭少漏幾滴，仍不是場域少停幾小時

OCP PBMC Revision 1.0 又示範另一個常見跳躍。Table 6.0 的 connector spillage requirement 是
0 PSIG 不超過 0.06cm³、75 PSIG 不超過 0.12cm³；test 7.1-3 實際指定的卻是 water、垂直方向、
0 與 80 PSIG，same-supplier 及 interoperability 每種組合至少三個樣本。75 PSIG 是 requirement
列，80 PSIG 是 test condition，兩個數字要原樣保存，不能選一個改寫另一個。

| PBMC conformance 項目 | 文件固定的最小分母 | 它能證明什麼 | 它仍不能證明什麼 |
|---|---:|---|---|
| Pressure drop | 每個 same-supplier／interop 組合至少 3 個樣本 | 特定 PG25、溫度、mate distance 與 flow points 的壓降要求 | 整條 loop 壓差、流量平衡或場域效率 |
| Air inclusion | 每個組合至少 2 個樣本 | 特定 fluid 與大氣壓條件的接頭測試 | field leak rate、液體污染或停機 |
| Spillage | 每個 same-supplier／interop 組合至少 3 個樣本 | 特定壓力、water、方向與量測方法的拆接 spill 上限 | 真實漏液事件、偵測延遲、隔離成功或修復時間 |

這些 N＝2 或 N＝3 是**每種 conformance combination 的零件樣本**，不是資料中心、機櫃或事故樣本。
同一 serialized valve pair 可被排進多項測試；同一對接頭的 1,256 次 mate cycles 也是 repeated
cycles，不是 1,256 個獨立接頭。Connector pass 是重要的第一道門，但不能被翻譯成「零 field leak」
或「不會停機」。

### 多空小作文共用的九欄漏液事件護照

| 護照欄位 | 必須固定什麼 | 少了最容易誤讀成什麼 |
|---|---|---|
| 1. 事件與版本 | site、rack／tray、平台、BMS／BMC、韌體、閥件與 connector 版本 | 不同拓撲的事件可以直接合併 |
| 2. 液體與漏點 | fluid、估計或量測量、來源、位置、pressure／temperature | 二元 leak signal 等於嚴重度 |
| 3. 感測品質 | sensor／zone、raw state、fault、閾值、debounce、true／false／miss label | 所有告警都是真漏液 |
| 4. 四段時間戳 | detected、decision、request sent、safe state confirmed | 命令送出時間等於隔離完成時間 |
| 5. 處置影響範圍 | tray／rack／row／CDU、power 與 fluid 各停哪裡 | 「自動隔離」代表影響很小 |
| 6. 殘餘冷卻 | 隔離後仍可用的 flow、thermal hold-up、備援與安全倒數 | 關閥後所有設備立刻安全 |
| 7. 服務分母 | affected racks／nodes／accelerators／jobs 與未完成工作 | 一次告警等於一次相同嚴重度停機 |
| 8. 復原與再驗收 | dry／repair、flush／refill、restart、recommission 與恢復服務時間 | alarm cleared 等於產能恢復 |
| 9. 動作責任 | 誰偵測、判定、下令、執行、確認、簽核及承擔成本 | 元件供應商自動承擔整體 SLA |

服務損失至少另算 **affected rack-hours＝Σ（受影響機櫃等價數×無法服務時數）**。在一個假想的
一小時事件中，若只隔離一座 rack，和關掉整列十座 rack，不應都記成「一件告警」。但 rack-hours 仍要與
accelerator-hours、job-hours、設備損害、清理成本及 false alarms 分帳：一座 rack 可能只停部分節點，
工作也可能已被排程器搬走；反過來，短暫告警可能留下較長的 drain、drying 與 recommissioning 尾巴。

**較強的多方版本**是更多、更精準的 sensor zone、閥件與控制能在代表性 fault injection 及真實事件中，
縮短 detected→confirmed-safe、縮小 tray／rack／row blast radius，並降低 rack-hours、job-hours、設備
損害與 recommissioning 時間；之後還要有合約責任、單價、部署分母與供應商收入，才可談商業受惠。

**較強的空方版本**是漏點不確定或硬體尾部風險很高時，粗粒度、立即關整列反而更安全；更多感測器、
閥件、MQTT、BMS 與控制軟體也會增加誤報、通訊、維修與整合失效點。PBMC 等介面標準化還可能讓
接頭更容易多來源替代。若細粒度自動化沒有降低 rack-hours、損害或復原時間，功能增加不等於價值增加。

本輪有 N＝3 份來源紀錄、N＝2 條組織來源鏈（OCP 與 NVIDIA）；其中 OCP 兩份文件屬同一標準生態，
不是兩個獨立場域。PBMC 的 N＝2／3 是每個 conformance combination 的最低零件樣本，repeated cycles
不獨立；具名 production leak event、true／false／fault 分母、端到端隔離延遲、affected rack-hours、
job-hours、設備損害、復原再驗收與財務共同觀測皆 N＝0。因此本文不估 leak rate、false-positive rate、
MTTR、availability、收入或毛利，也沒有可報的 sampling SE／t。

## 同樣 1MW，為什麼還要分熱量、流量、ATD、壓差與泵功

「1MW CDU」看似是一個容易比較的容量，實際上至少藏著六本帳：IT 用電、真正進入液體的熱、
流體熱運能力、熱交換器兩側的 ATD、整條流路的壓差，以及泵浦輸入功率。OCP 的液對液 CDU
方法因此要求把流體、FWS／TCS 溫度與流量、ATD、TCS 揚程、FWS 阻抗一起報告；只留下最大
kW，就無法知道兩台設備是否在同一難度下額定。

### 第一本帳：IT MW 不一定全進液體

先固定量測邊界。假想某機櫃實際 IT 用電 1,000kW，其中 80% 的熱進入 TCS，液體熱負載是
800kW，另有 200kW 仍由空氣、電源損耗或其他路徑帶走。這個 80% 只是教材輸入，不是任何
平台的 liquid heat capture ratio。若把 1,000kW 直接當成液體熱負載，後面的流量、CDU 數量、
FWS 容量與泵功都會從錯的分子出發。

### 第二本帳：帶走相同熱量，溫升越小通常要越多流量

ASHRAE 的穩態水側熱平衡是 qliquid＝質量流量×比熱×ΔTloop。以下固定液體熱負載 800kW，
先使用 ASHRAE 標準條件的水密度 1,000kg/m³、比熱 4.18kJ/(kg·K)，只改 TCS 回水減供水的
迴路溫升。

| 假想標準水案例 | 液體熱負載 | ΔTloop | 所需體積流量 | 能回答什麼 | 還不能回答什麼 |
|---|---:|---:|---:|---|---|
| W1 | 800kW | 5K | 2,296.651 LPM | 固定水性質與穩態熱量下的流量 | 冷板溫度、壓差、泵功、ATD、動態負載 |
| W2 | 800kW | 10K | 1,148.325 LPM | 同上 | 同上 |
| W3 | 800kW | 15K | 765.550 LPM | 同上 | 同上 |

把 ΔTloop 從 5K 放寬到 10K，理想流量減半；放寬到 15K，流量是 5K 案例的三分之一。
但較高回水溫可能壓縮晶片、冷板與熱交換器的溫度裕量，不能只看泵浦比較省就宣布整體較好。

OCP OAI 指引又提供另一個不能混用的口徑：在其 PG25、熱交換器與 OAI／OAM 邊界下，建議
7.5–12°C 溫升對應 1.25–2.0LPM/kW，典型 10°C 目標是 1.5LPM/kW。若只做確定性乘法，
800kW×1.5LPM/kW＝1,200LPM，比 W2 的標準水換算高 4.5%。兩者不是互相推翻，而是在提醒
讀者：流體性質與工程 allowance 不同，不能把純水公式、PG25 指引與供應商額定混成一條線。

### 第三本帳：迴路溫升與 ATD 是兩個不同溫差

ΔTloop 是 TCS 回水減 TCS 供水，用來核對液體帶熱；OCP CDU 方法定義的 ATD 則是 TCS 供水
減 FWS 供水，用來描述熱交換器兩側接近程度。下面固定 TCS 30→40°C，只改 FWS 供水：

| 假想溫度案例 | FWS 供水 | TCS 供水 | TCS 回水 | ATD | ΔTloop | 判讀 |
|---|---:|---:|---:|---:|---:|---|
| T1 | 25°C | 30°C | 40°C | 5K | 10K | 熱交換器兩側有 5K 接近溫差 |
| T2 | 27°C | 30°C | 40°C | 3K | 10K | 液體迴路溫升不變，但熱交換器條件更緊 |

若只報「TCS 溫差 10K」，T1 與 T2 會看起來相同；若只報「ATD 5K」，又看不出液體究竟帶走
多少熱。CDU capacity curve 必須把兩個溫差、兩側流量與流體放在同一工作點。

### 第四本帳：流量不等於泵功，還差壓差與效率

DOE 的泵浦指南把輸入功率連到流量、揚程、比重、泵浦效率與馬達效率。換成一致 SI 單位後，
可寫成 Pin＝壓差×體積流量÷綜合效率。下面固定 1,200LPM，也就是 0.02m³/s；綜合效率是
泵浦效率乘馬達效率的假想合併值。

| 假想泵浦案例 | 流量 | 壓差 | 綜合效率 | 輸入功率 | 假想全年滿載 8,760h |
|---|---:|---:|---:|---:|---:|
| P1 | 1,200LPM | 200kPa | 70% | 5.714kW | 50.057MWh |
| P2 | 1,200LPM | 400kPa | 70% | 11.429kW | 100.114MWh |
| P3 | 1,200LPM | 200kPa | 50% | 8.000kW | 70.080MWh |

P2 與 P1 流量相同，壓差加倍後泵功也加倍；P3 的壓差相同，效率較低仍多用電。真實壓差會
隨流量、管徑、QD、manifold、冷板、閥件、濾網堵塞與並聯路徑改變，效率也要看 pump curve、
馬達、VFD、N＋1 切換及 part-load duty。表中的全年 MWh 只是「假設全年都停在同一工作點」的
上課換算，DOE 明確要求變動負載用時間剖面計算，不能拿來當任何場域實績或 PUE。

以上共有 N＝1 個假想 IT／液體熱量拆分、N＝3 個標準水溫升案例、N＝1 個 PG25 指引乘法、
N＝2 個 ATD／ΔTloop 案例與 N＝3 個泵浦案例。Python Fraction 與獨立 awk 在顯示精度內完全
一致；這些都是固定輸入的確定性換算，不是抽樣、CFD、設備試驗或場域量測，因此沒有 sampling
SE／t，也沒有機櫃、CDU、客戶、部署、需求、價格、收入、毛利或公司效果。

### 多空小作文共用的液冷熱工—水力十欄護照

| 護照欄位 | 必須固定什麼 | 少了最容易誤讀成什麼 |
|---|---|---|
| 1. 系統邊界 | IT nameplate／實際 load、哪些元件進液體、liquid capture ratio、時間窗 | 把 IT MW 全當液體熱負載 |
| 2. 流體身分 | 配方、濃度、溫度、密度、比熱、黏度與老化狀態 | 把水與 PG25 共用同一 LPM/kW |
| 3. TCS 溫度 | 供水、回水、ΔTloop、感測位置與不確定度 | 只報一個進水溫就推散熱能力 |
| 4. FWS 與 ATD | FWS 供回水、TCS 供水、ATD、露點與 heat-exchanger curve | 把迴路溫升冒充熱交換器接近溫差 |
| 5. 熱量帳 | 液體／空氣熱量、穩態或動態、計算／量測方法與 energy balance | 把 TDP、IT load、CDU capacity 當同一 MW |
| 6. 流量與分配 | FWS／TCS 總流量、支路流量、串並聯、turndown 與 imbalance | 總 LPM 足夠就推每顆冷板都足夠 |
| 7. 壓差與阻抗 | pump head、FWS impedance、TCS dP、各元件 PQ curve、濾網狀態 | 用零件單點 dP 推整條迴路 |
| 8. 泵浦與備援 | 泵／馬達／VFD 型號、效率曲線、N／N＋1、切換與 duty profile | 用銘牌 kW 或最高效率推全年耗能 |
| 9. 熱排與環境 | CDU HX、facility heat rejection、chiller／dry cooler、露點、水與季節 | 從 TCS 效率直接推整座 PUE／WUE |
| 10. 驗收與商業 | raw telemetry、重複／不確定度、L4／L5、故障演練、BOM、責任與財務分母 | 從更高 rack density 直接跳到公司訂單 |

**較強的多方版本**不是「AI 功率變大，所以所有液冷零件同比增加」，而是同一 production site
的液體捕熱率、熱密度或可用性門檻提高後，CDU、冷板、QD、manifold、泵浦、感測與控制在共同
ATD／PQ／part-load／備援條件下仍通過，且合約、部署、維護與財務資料證明每站價值真的增加。

**較強的空方版本**也不是「溫差放大就不需要液冷」，而是平台以較高可接受 ΔTloop、較暖供水、
較低阻抗冷板、更少接頭、較佳泵效率或更高 liquid capture，降低每 kW 流量、泵功、CDU 台數或
剩餘空冷設施；若更高規格同時減少數量、整合供應商或把價值移到設施端，族群收入不必同步放大。

## 同樣 60% RH，露點可差 7.5°C：防結露要看最冷表面

「機房相對濕度 60%」不是固定含水量，也不是 non-condensing 證明；「供液 20°C」同樣不是
最冷表面實測。防結露真正要守的是同一位置、同一時間的局部露點裕度：

**局部露點裕度＝最冷局部表面溫度－同位置露點。**

裕度為正，只表示該表面在當下仍高於露點；接近零時還要扣除感測準確度、校正漂移、控制死帶、
位置差與暫態誤差；裕度為負，表示表面已低於周圍空氣的露點，進入可能結露的熱力條件。是否
真的形成水滴、多久形成、流到哪裡，仍要看表面、氣流、時間與材料，不能從一個負值直接推故障率。

### 第一本帳：RH 不帶乾球溫度，就不能固定露點

NBS／NIST 的 Celsius Antoine 關係在 0–60°C 水蒸氣範圍可寫成：

**露點＝1 ÷〔1 ÷（乾球溫度＋235.0）＋log₁₀（1 ÷ RH）÷ 1750.286〕－235.0**

其中 RH 用 0 至 1 的比例。以下三列都把最冷表面固定為 20°C，只改乾球溫度與 RH；這是公式
教材，不是任何機房設定或 pass line。

| 假想露點案例 | 乾球溫度 | RH | 換算露點 | 最冷表面 | 局部露點裕度 | 只可怎麼讀 |
|---|---:|---:|---:|---:|---:|---|
| D1 | 27°C | 60% | 18.579°C | 20°C | ＋1.421K | 表面高於公式露點，但未扣感測與控制不確定度 |
| D2 | 35°C | 60% | 26.066°C | 20°C | −6.066K | 同一表面低於公式露點，已進入結露風險邊界 |
| D3 | 27°C | 40% | 12.271°C | 20°C | ＋7.729K | 降低 RH 擴大此固定案例的公式裕度 |

D1 與 D2 都是 60% RH，露點卻相差 7.4867°C，標題四捨五入為 7.5°C。這不是說室溫升高會在
封閉空間自動增加水量；它只說「固定 RH」代表水蒸氣分壓隨乾球溫度改變，所以 RH 必須和同時、
同地的乾球溫度成對保存。若溫度改變但水蒸氣沒有同步增減，RH 本身也會跟著變，不能只固定一欄。

### 第二本帳：供液感測點不是最冷表面

同一個「20°C」可能指 CDU 出口液體、機櫃入口液體、管內流體或金屬表面；四者在穩態與暫態都
不必相同。研究與驗收至少要分開下列參考面。

| 參考面 | 要保存什麼 | 為什麼不能被供液設定值替代 |
|---|---|---|
| 機房／冷通道空氣 | 乾球溫度、RH、露點、位置與時間 | 中央感測器看不到每座機櫃局部混氣與濕氣 |
| 機櫃入口與內部空氣 | 同步乾球、RH、氣流與區域 ID | 同一房間仍可能有局部溫濕度梯度 |
| CDU 與機櫃供回液 | 實測溫度、流量、模式與時間戳 | 流體讀值不是外表面溫度，也看不到每條支路 |
| 管路、QD、manifold 與閥件表面 | 材料、保溫、位置、表面溫度與熱影像最低點 | 金屬、接頭與保溫缺口可能形成不同冷點 |
| 伺服器與電源內部表面 | 冷板鄰近件、機殼、PCB 與非發熱元件溫度 | 發熱 PCB 與高熱容量或非發熱元件可跨在露點兩側 |
| 感測與控制邊界 | 準確度、校正、取樣率、延遲、死帶與 alarm margin | 顯示裕度不等於扣除量測與動態不確定度後仍安全 |

OCP 2013 年 Prineville 案例提供一個很具體、但範圍有限的反例：受控箱體把 RH 拉到 97%，並在
10 分鐘內由 15°C 升至 30°C；CAP1 表面約第 6 分鐘落到露點以下，之後再觀察到約 9 分鐘結露，
但 PCB 全程高於露點且沒有結露。它證明的不是「液冷一定會結露」，而是**同一設備、同一空間，
不同表面仍可位於露點兩側**。該案例來自 air-side economizer／蒸發冷卻控制事件，不能當成現代
AI 液冷 rack 的故障率、冷板測試或供應商排名。

### 第三本帳：暖水與 economizer 是一組交換，不是免費效率

ASHRAE 指出機架內循環液通常維持高於露點，W1／W2 又明確要求防止結露；同一章也指出較高的
facility supply water temperature 通常可降低設施冷卻成本，但設備端需要更強的熱設計，才能把
液冷元件維持在目標溫度內。DOE FEMP 則說明水側 economizer 可在戶外條件合適時，透過串聯
熱交換器先冷卻冰水迴路、降低冰水主機負載，甚至在適當條件下繞過 chiller。

這裡有三個不能省略的交換：

- **結露裕度**：提高供液溫通常讓冷表面更容易高於露點，但仍須量最冷表面與暫態，不能用設定值代替。
- **晶片熱裕度**：較暖供液可能增加 economizer 可用條件，卻也可能壓縮冷板、晶片與 ATD 的熱設計空間。
- **財務分母**：economizer 可用時數要按地點氣候、負載、設定、熱交換器、控制與備援逐時重建；節電還要接到實測 chiller／pump kW、能源價格、水、維護與資本支出，不能從「可 bypass」直接推毛利。

### 多空小作文共用的防結露—economizer 十欄護照

| 護照欄位 | 必須固定什麼 | 少了最容易誤讀成什麼 |
|---|---|---|
| 1. 場域與區域 | site、氣候、房間、冷通道、機櫃與局部位置 ID | 一個機房平均值代表所有冷點 |
| 2. 時間與運轉模式 | 時間戳、steady／ramp、chiller／economizer、切換事件 | 穩態讀值代表控制切換暫態 |
| 3. 空氣狀態 | 同位置 dry-bulb、RH、壓力與 measured／derived dew point | 單一 RH 等於固定含水量或固定露點 |
| 4. 最冷表面地圖 | 管路、QD、manifold、閥、機殼與內部元件最低溫 | CDU supply sensor 就是整套最低表面 |
| 5. 液體參考面 | FWS／TCS 供回液溫、流量、ATD、支路與 mixing | 一個供液設定能描述所有液體和表面 |
| 6. 裕度與不確定度 | 每點表面減露點、感測準確度、校正、位置差與 guard band | 顯示正 0.5K 就必然 non-condensing |
| 7. 控制與保護 | setpoint、deadband、ramp rate、alarm、隔離、fallback 與責任 | BMS 有讀值就等於動作經過驗證 |
| 8. 驗收與事件 | 最差氣候、切換、冷啟動、失效注入、結露／滴水與復原 | 一次正常穩態 SAT 等於全年可靠 |
| 9. 能源與水 | economizer hours、chiller／pump kW、heat rejection、PUE／WUE 邊界 | 可用暖水直接等於固定節能比例 |
| 10. 商業共同鍵 | BOM、供應商、合約責任、site／rack 分母、收入、毛利與維護 | 技術必要性直接等於公司訂單與獲利 |

**較強的多方版本**是具名量產場域在不同季節與切換情境下，以最冷表面扣除量測不確定度後仍
維持正裕度，同時增加 economizer 可用時數、降低可重建的 chiller／water 成本，而且合約與財務
共同鍵顯示控制、保溫、感測、QD、CDU 或整合價值確實由特定供應商承接。

**較強的空方版本**是 headline 只給室內 RH、供液設定或 W-class，最冷表面、控制暫態、感測
誤差、結露事件與能源基準都缺；或者更暖供水雖降低設施成本，卻減少 CDU／chiller 數量、壓縮
設備單價、把價值移到別的系統，讓技術採用與台灣公司收入不同步。

本節共有 N＝3 個固定輸入露點案例與 N＝1 個 OCP 受控箱體案例。三個公式案例以 Python
Decimal 與獨立 awk 重算，露點、裕度及同 RH 的 7.486658697367°C 差異在小數點後 12 位一致；
它們不是抽樣、場域量測、CFD、可靠度試驗或供應商樣本，因此沒有 sampling SE／t。OCP 案例
只是一條 air-side 事件／箱體消息鏈，也不能估結露發生率。NIST、ASHRAE、OCP 與 DOE 四份
官方來源提供方法與邊界，不是四座場域或四家供應商；production site 的同步表面圖、事件率、
economizer 時數、能源／水成本、BOM、訂單、收入與毛利共同觀測仍是 N＝0。

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
- **容量也必須同條件比較**：IT 用電、液體捕熱、流體性質、TCS 溫升、ATD、兩側流量、流路壓差、泵效率與備援 duty 少一項，就不能把相同最大 kW 視為相同熱工—水力能力。
- **防結露必須看局部與時間**：同一 RH 可因乾球溫度不同而有不同露點，同一設備內的表面也可跨在露點兩側；供液設定、房間平均 RH 或 W-class 都不能替代最冷表面裕度與控制暫態。
- **仍不能推到公司**：目前高信心只涵蓋架構與證據階梯；公司供貨、訂單、收入、市占、毛利及完整方案責任仍未驗證。
- **相對第八站新增了什麼**：研究從容量與供應狀態，前進到責任交接、感測、隔離、維護，以及熱量—流量—壓差—泵功的可重建護照，不是再做另一張設備排名。
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
- [ASHRAE Handbook：Hydronic Heating and Cooling](https://handbook.ashrae.org/Handbooks/S20/SI/s20_ch13/s20_ch13_si.aspx)
- [OCP：OAI System Liquid Cooling Guidelines](https://www.opencompute.org/documents/oai-system-liquid-cooling-guidelines-in-ocp-template-mar-3-2023-update-pdf)
- [OCP：Liquid to Liquid CDU Test Methodology and Performance Rating](https://www.opencompute.org/documents/ocp-wp-l-lcdu-test-methodology-performance-rating-r1-pdf)
- [DOE：Pump Life Cycle Costs](https://www1.eere.energy.gov/manufacturing/tech_assistance/pdfs/pumplcc_1001.pdf)
- [NIST／NBS：The Use of Dew-Point Temperature in Humidity Calculations](https://nvlpubs.nist.gov/nistpubs/jres/74C/jresv74Cn3-4p117_A1b.pdf)
- [ASHRAE Handbook：Data Centers and Telecommunication Facilities](https://handbook.ashrae.org/Handbooks/A15/SI/a15_ch19/a15_ch19_si.aspx)
- [OCP：Learning Lessons at the Prineville Data Center](https://www.opencompute.org/blog/learning-lessons-at-the-prineville-data-center)
- [DOE FEMP：Cooling Water Efficiency Opportunities for Federal Data Centers](https://www.energy.gov/cmei/femp/cooling-water-efficiency-opportunities-federal-data-centers)

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

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C18,C19,C20,C21
metric: 具名量產液冷場域是否以共同時間與位置鍵公開 dry-bulb、RH、dew point、最冷表面、FWS／TCS 供回液溫、感測不確定度、控制模式、結露事件、economizer 時數及能源／水結果
source_ids: S13,S14,S15,S16
watch_source_ids: S2,S4,S6,S8
frequency: monthly
next_check: 2026-09-03
trigger: production site 公開跨季 raw telemetry、surface map、control transition／failure injection、condensation incident denominator、economizer duty、energy／water baseline 與責任矩陣
invalidation: 跨氣候、拓撲與控制模式的量產證據證明單一房間 RH 或單一供液溫在扣除感測誤差後已能完整代表所有局部表面、結露事件與 economizer 成效
-->

<!-- monitoring_item
monitor_id: T5
status: active
claim_ids: C22,C23,C24,C25
metric: 具名 production leak event 是否逐事件公開漏液量與位置、true／false／fault、四段 timestamp、tray／rack／row／CDU 動作與 confirmed state、受影響 rack／node／job、rack-hours／job-hours、損害及復原再驗收
source_ids: S17,S18,S19
watch_source_ids: S2,S4
frequency: monthly
next_check: 2026-09-30
trigger: 量產場域或代表性 fault injection 提供可重建事件 log、端到端狀態時間、服務損失分母與偵測／決策／執行責任矩陣
invalidation: 在按事件嚴重度與拓撲調整後，細粒度或自動隔離沒有降低、甚至因誤報或控制失敗增加 affected rack-hours、job-hours、設備損害或復原時間
-->

## 什麼會推翻這篇

- 具名量產場域的文件若證明單一冷卻設備測試已同時完成設施水路、循環水路、伺服器、控制、流體、維護與長期可靠度的共同驗收，而且沒有額外交接缺口，就會推翻本文的主要判定。
- OCP 或平台商若刪除多數介面工作項目，並以可重現的場域資料證明模組化混搭不再需要逐一驗證材料、流體、快速接頭、分流器與控制，也會削弱本文。
- 若台灣公司的公開文件始終無法說明責任範圍與部署規模，族群圖譜就只應保留為搜尋路線，不應升格為公司商業曝險。
