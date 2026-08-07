# 2026-08-07 AI 機櫃控制與責任鏈研究雷達

本輪由前一輪 telemetry 的明示反證門檻觸發：DSX 新資料已從感測欄位推進到隔離 request、
publisher ownership 與 BMS guardrail。排名在深研前凍結；升格只代表 article＋graph 的
證據契約通過，不代表 production deployment、台灣供應商受惠或投資建議。

<!-- research_radar
schema_version: 2
radar_id: RADAR-2026-08-07-01
as_of: 2026-08-07
next_review: 2026-08-14
status: retired
method: 先做全 universe 官方事件端點快掃並明示 8 月 7 日資料尚未出現在來源端點，因此 scope 維持 partial；再依上一輪明示 next evidence、族群圖譜缺口、可證偽性、至少兩條一手來源鏈、台灣公司映射風險與維護成本排序。候選先寫入 append-only selection log 並獨立 commit；深研後只更新 evidence posture、route 與結果，不改凍結排名、第一拒絕與下一份證據
selection_cycle_id: RS-2026-08-07-01
-->

<!-- research_candidate
candidate_id: RC-AI-POWER-TELEMETRY
rank: 1
title: AI 機櫃 telemetry 的事件、隔離與維修 action contract
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: NVIDIA DSX BMS Event Bus 1.0.0 與 companion guide 已把 rack identity、Value／Metadata、integration publisher、liquid／electrical isolation request、BMS authority 與 safe default 串成具體契約；這是 8 月 3 日雷達等待的直接 early trigger
knowledge_gain: 把「監測點越多越有價值」改寫成 identity→typed value／metadata→request owner→guardrail→isolation state→service outcome 的可反證階梯，並把 DSX、OpenRMC／Redfish、場域結果與公司財務分成不同成熟度
first_rejection: 若 DSX 只是一家平台的欄位清單，無法與 OpenRMC／Redfish 的管理介面對齊，也沒有可驗證的 request→isolation→service 狀態轉移，就不建立獨立文章或商業價值主張。
next_evidence: 逐欄核對 DSX Event Bus／BMS Integration、OCP OpenRMC 與 Redfish 的 identity、telemetry、request、action ownership、acknowledgement 與 fail-safe 邊界；另查 production deployment 與台灣公司曝險。
next_check: 2026-08-31
route: article_and_graph
article_topic_id: MI-2026-08-07-AI-RACK-ACTION-CONTRACT
graph_id: ai-rack-action-contract
sources: NVIDIA DSX BMS Event Bus 1.0.0 => https://docs.nvidia.com/dsx-exchange/schema/bms-event-bus/overview | NVIDIA BMS Integration Companion Guide => https://docs.nvidia.com/dsx-exchange/bms-integration | OCP OpenRMC Design Specification => https://www.opencompute.org/documents/openrmc-design-specification-v1-0-1-pdf | DMTF Redfish standards => https://www.dmtf.org/standards/redfish
-->

<!-- research_candidate
candidate_id: RC-AI-THERMAL-RESISTANCE-CHAIN
rank: 2
title: AI package／TIM／cold plate 熱阻與機械公差鏈
priority: p1
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: OCP cold-plate qualification 已把 TIM2、case-to-liquid thermal resistance、flow 與 pressure drop 放進同一測試，NVIDIA partner-cooled SuperNIC 文件又揭露 force、torque 與 thermal-pad 邊界；但兩條來源尚未構成完整 package-to-coolant 責任與可靠度鏈
knowledge_gain: 若能補齊，可把 thermal／material 研究從材料導熱係數推進到接觸壓力、翹曲、TIM 老化、冷板流阻與失效定位；現階段保留 watch，避免把一份 qualification 流程外推成供應商價值
first_rejection: 若來源無法把 die／package、TTP／lid、TIM、cold plate 與 coolant 的熱阻、機械公差及可靠度分開，或只剩材料商導熱係數宣傳，就不建立材料排行或台廠受惠映射。
next_evidence: 核對 OCP cold-plate development、NVIDIA partner-cooled hardware 與獨立 package／TIM 文件的量測定義、接觸壓力、翹曲、老化與失效條件。
next_check: 2026-08-31
route: watch_only
sources: OCP Cold Plate Development and Qualification => https://www.opencompute.org/documents/ocp-cold-plate-development-and-qualification-with-integrated-comments-pdf | NVIDIA ConnectX-8 partner-cooled recommendations => https://networking-docs.nvidia.com/connectx8ocphw/general-cooling-recommendations-for-partner-cooled-supernics
-->

<!-- research_candidate
candidate_id: RC-AI-TEST-INSERTION-LADDER
rank: 3
title: Chiplet／HBM 的 test insertion 與 known-good-die 責任階梯
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: Teradyne 已把 CoW／CoP、known-good die、unpackaged module access 與 SLT 拆成新增 insertion；但目前主要是一家設備商敘事，尚未由封裝流程與客戶 qualification 獨立核對各測試節點
knowledge_gain: 若通過，可補既有 tester TAM 文章缺少的 wafer／pre-singulation／post-singulation／package／system-level 責任圖；現在不把 insertion 數量換成設備營收
first_rejection: 若只有測試設備商敘事，無法由封裝流程、客戶 qualification 或多家工具文件辨認 wafer／pre-singulation／post-singulation／package／system-level test 的邊界，就不把 insertion 數量外推成設備或介面營收。
next_evidence: 以 Teradyne HBM／chiplet test flow、Advantest 最新 tester 展望及封裝／標準一手文件對齊 test access、溫控、功率、良率損失與量產節點。
next_check: 2026-09-15
route: watch_only
sources: Teradyne AI chiplet test insertions => https://www.teradyne.com/2026/07/27/ai-chiplet-architectures-redefining-test-insertions/ | Teradyne Magnum 7H => https://www.teradyne.com/products/magnum-7h/ | Advantest IR library => https://www.advantest.com/investors/ir-library/
-->

<!-- research_candidate
candidate_id: RC-AI-RACK-MECHANICAL-QUALIFICATION
rank: 4
title: AI rack 機構、rail／tray 與 blind-mate qualification
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: OCP 2026 Open Rack Wide 與 MGX rack documents 可定位 rack form factor、rail／tray、busbar 與 liquid interface，但目前未找到同一責任鏈的 load case、運輸／seismic、循環壽命與場域驗收
knowledge_gain: 若完整，可補 serverodm／機構族群圖譜最薄的機械責任與 serviceability 路徑；現在只保留接口與測試缺口，不建立價值量或供應商份額
first_rejection: 若只能取得標準尺寸或產品頁，沒有 static／dynamic load、transport／seismic、rail cycle、blind-mate tolerance、serviceability 與 deployment acceptance 的可重現測試，就不建立機構價值量或台廠份額。
next_evidence: 取得 OCP ORW／MGX 正式規格、rail／tray 與 rack qualification 文件，逐項對齊 load case、接口、公差、循環壽命、維修動作與實際部署。
next_check: 2026-09-15
route: watch_only
sources: OCP Open Rack specifications => https://www.opencompute.org/wiki/Open_Rack/SpecsAndDesigns | OCP MGX rack and trays specification => https://www.opencompute.org/documents/mgx-accelerated-computing-rack-and-trays-specification-101024-pdf | NVIDIA MGX platform => https://www.nvidia.com/en-us/data-center/products/mgx/
-->

<!-- research_candidate
candidate_id: RC-AI-POWER-DISTRIBUTION-INTERFACES
rank: 5
title: Facility 800V、rack-side 400V 與 IT-gear 48V 配電接口
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: OCP HPR 72kW power shelf、ORW 與 Diablo 400 分別出現 48V 高電流 busbar、可液冷 interface 與 ±400V power rack，可直接暴露市場把不同 voltage domain 混成單一連接器需求的風險
knowledge_gain: 若能由 topology 與 qualification 對齊，可建立 voltage domain×current×mating×cooling×serviceability 矩陣；目前不同規格仍不是同一 production architecture
first_rejection: 若不同規格的 voltage domain、current、touch safety、mating／bolted interface、cooling 與 conversion boundary 無法對齊，或沒有 production topology，就不做連接器／busbar 用量與材料勝負推論。
next_evidence: 逐頁核對 OCP HPR 72kW、ORW、Diablo 400 與至少一份獨立 connector／busbar qualification，建立 voltage-domain×current×interface×cooling×serviceability 矩陣。
next_check: 2026-09-15
route: watch_only
sources: OCP HPR 72kW Power Shelf => https://www.opencompute.org/documents/open-rack-v3-hpr-v2-72kw-power-shelf-spec-v1-0-0-pdf | OCP Open Rack Wide => https://www.opencompute.org/documents/open-rack-wide-orw-base-specification-v1-0-0-final-pdf | OCP Diablo 400 => https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf
-->

## 本輪方法結果

- 研究前凍結五題；只有第一名通過 research-grade article＋graph，第二至第五名維持 watch，沒有為了固定產出數量而升格。
- 第一名是 early reselection：凍結 selection reason 留下新來源、日期與 URL，直接對應上一輪 `next_evidence`，不是未到期重排。
- 升格的是 action-contract 驗證階梯；production interoperability、field outcome 與台灣公司財務曝險仍是 active unverified claims。
- 研究後回顧將把「前兩名必須升格」從測試移除，並讓歷史雷達與 early trigger 納入方法稽核。
