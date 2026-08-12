# 液冷迴路責任邊界知識圖譜

本圖把 FWS、TCS、CDU、manifold、cold plate、流體與 BMS 連成同一份介面責任圖。
平台列名只是其中一個成熟度節點；族群線仍不代表具名公司已承擔場域驗收或認列收入。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: liquid-cooling-loop-boundaries
root_node_id: concept:liquid-cooling-loop-boundary
label: 液冷迴路責任邊界
summary: 從 FWS／TCS 邊界、液冷元件、材料相容性到 BMS 觀測與隔離，拆解單一 CDU 資格與完整場域部署的差距。
article_ids: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES
status: active
-->

<!-- knowledge_edge
edge_id: KG-LCB-C01
view: company
from_id: company:lenovo
to_id: concept:liquid-cooling-loop-boundary
relation: integrates
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C3
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2024-09-13
review_due: 2026-09-03
status: active
boundary: Lenovo 公開的是 Neptune reference practice 與平台案例，不是所有資料中心共同規格、排他供應或台灣公司財務證據。
next_trigger: 具名客戶公布 interface scope、site acceptance、field reliability 與 Lenovo 合約責任。
-->

<!-- knowledge_edge
edge_id: KG-LCB-C02
view: company
from_id: company:nvidia
to_id: concept:liquid-cooling-loop-boundary
relation: owns_platform
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C4,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C7
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: NVIDIA 定義 DSX BMS contract 與 Marketplace 欄位，但液冷設備、site integrator 與控制實作仍由多家供應商共同完成。
as_of: 2026-08-03
review_due: 2026-09-03
status: active
boundary: 資料契約與設備列名不證明特定 site 已 commissioned、隔離成功、長期可靠或產生供應商收入。
next_trigger: DSX 公布具名 production site 的 commissioning、telemetry completeness、isolation test 與 field results。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I01
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: concept:liquid-cooling
relation: generation_of
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C5
note_refs:
evidence_state: inference
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-03
status: active
boundary: 責任邊界圖是既有液冷主題的系統工程視圖，不取代各設備性能、資格與公司財務研究。
next_trigger: 新版標準或場域證據改變 FWS／TCS／ITE／control 的責任切分。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I02
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: concept:facility-water-system
relation: contains
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C1,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C3
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-03
status: active
boundary: OCP Rev 2 將 FWS 排除於 TCS 文件範圍外，Lenovo 則說明 primary loop；這表示責任交接而非 FWS 不重要。
next_trigger: Site interface control document 公布 FWS 水質、溫度、壓力、流量與 availability 的驗收責任。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I03
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: concept:technology-cooling-system
relation: contains
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C1,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C2,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C3
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: OCP 與 Lenovo 都描述二次 technology loop，但實際元件與 integrator 可採多家供應。
as_of: 2026-08-03
review_due: 2026-09-03
status: active
boundary: TCS 範圍可重建，不代表每個專案採相同流體、拓撲、溫度、責任或供應商。
next_trigger: 具名 production site 公布完整 TCS specification、qualification 與 operating envelope。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I04
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: component:cdu
relation: contains
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C1,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C3,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C7
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: multi_source
exclusivity_scope: NVIDIA Marketplace 列出多家 CDU；CDU 只是 FWS 與 TCS 間的設備節點，不是單一供應商的完整場域方案。
as_of: 2026-08-03
review_due: 2026-09-03
status: active
boundary: 額定容量、validation type 與 supply status 不等於 site acceptance、field reliability、訂單或收入。
next_trigger: 具名 CDU 型號完成 site commissioning、field operation 並有客戶和供應商雙向證據。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I05
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: component:rack-manifold
relation: contains
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C1,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C2,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-03
status: active
boundary: Manifold 是 TCS 分配節點；現有證據不指定台灣供應商、量產份額、壓降表現或財務貢獻。
next_trigger: Production rack 公布 manifold interface、qualification、flow balance 與 field failure data。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I06
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: component:cold-plate
relation: contains
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C2,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: OCP 以開放工作流處理 cold plate；平台內仍可能有多種設計與供應商。
as_of: 2026-08-03
review_due: 2026-09-03
status: active
boundary: Cold plate 是熱交換元件，不等於整套 TCS、CDU、site integrator 或可辨識公司收入。
next_trigger: Cold plate base specification、qualification 與具名 production platform deployment。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I07
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: component:quick-disconnect
relation: contains
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: OCP 同時推進 hand-mate 與 blind-mate UQD 路徑，不是單一 connector 或供應商排他。
as_of: 2026-08-03
review_due: 2026-09-03
status: active
boundary: 工作流支持介面重要性，不證明 final spec、跨廠 qualification、採購量或台灣供應商份額。
next_trigger: UQD／BMQC final specification、multi-vendor test 與 production rack adoption。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I08
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: capability:coolant-compatibility
relation: requires
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C2,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-03
status: active
boundary: 流體、材料與維護相容性是系統要求，不指定唯一配方、材料、服務商或財務價值。
next_trigger: 同一多供應商 loop 公布長期相容性、腐蝕、污染與維護結果。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I09
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: capability:liquid-cooling-telemetry
relation: measured_by
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C4
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-03
status: active
boundary: DSX 定義資料語意不等於 site 感測完整、值可信、BMS 已 commissioned 或控制效果已驗證。
next_trigger: Production site 公布 telemetry completeness、data quality、alarm response 與 operating results。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I10
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: capability:leak-isolation
relation: requires
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C3,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C4
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-03
status: active
boundary: LeakDetect 與 LiquidIsolation points 支持控制責任存在，不證明任一 site 動作延遲、成功率或 fail-safe 結果。
next_trigger: 具名場域發布漏液注入測試、隔離動作、復原程序與 field incident data。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I11
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: stage:platform-validation
relation: passes_through
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C7
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-03
status: active
boundary: 平台列名降低部分設備採購風險，仍不包含完整 site acceptance、commissioning、field reliability 或財務。
next_trigger: 平台把設備 qualification 與 site-level validation 以可重現條件連接。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I12
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: group:thermal
relation: routes_to
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-30
status: active
boundary: 散熱族群是 cold plate、QD、manifold、CDU 與整合搜尋路由；沒有完整責任、site acceptance 或財務證據。
next_trigger: 客戶與公司雙向確認具名產品、責任範圍、驗收、部署及財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I13
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-30
status: active
boundary: CDU 電源、控制、BMS 與電液隔離形成相鄰路由，不證明電源本業與液冷財務能合併或已有訂單。
next_trigger: 具名液冷控制／電源產品完成 site acceptance 並有可辨識收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I14
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: group:serverodm
relation: routes_to
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-30
status: active
boundary: ODM 位於 ITE、rack 與 site integration 交界，但沒有合約責任、驗收分母、收入或毛利的雙向證據。
next_trigger: 客戶與 ODM 公布具名 site、interface scope、commissioning、部署量與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I15
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: metric:cdu-operating-envelope
relation: measured_by
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C8
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2022-10-03
review_due: 2026-09-03
status: active
boundary: OCP water-based TCS 方法要求固定溫度、壓力、過濾及安全條件，但不提供每一 CDU、流體或場域的通用工作點與 pass／fail。
next_trigger: 具名多供應商量產場域公開 fluid-specific 溫度、壓力、流量、熱負載及最差條件測試。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I16
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: metric:coolant-chemistry-baseline
relation: measured_by
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C8,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C9
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2022-10-03
review_due: 2026-09-03
status: active
boundary: 啟動基準與代表性樣本是可追蹤方法，不表示 OCP Table 1 數值可跨 PG、介電液、FWS 或不同材料直接套用。
next_trigger: 具名場域發布 fluid COA、填充後代表樣本、實驗室 QA 及跨季趨勢。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I17
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: capability:wetted-material-change-control
relation: requires
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C8
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2022-10-03
review_due: 2026-09-03
status: active
boundary: 完整浸液材料清單與變更重審是方法要求，不證明任一供應商已取得客戶資格、排他料號或收入。
next_trigger: 具名多供應商場域公布完整材料清單、替代料／維修變更及相容性重驗結果。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I18
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: metric:coolant-contamination-budget
relation: measured_by
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C9,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C10,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C11
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-03
status: active
boundary: 一手文件共同證明潔淨度要跨設計、施工、填充與運轉管理，但沒有形成所有平台共用的顆粒或微生物單一門檻。
next_trigger: 具名量產場域按製造、運送、施工、填充與維修階段公布 contamination budget、沖洗終點及 field trend。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I19
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: stage:tcs-fluid-commissioning
relation: passes_through
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C9,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C11
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-03
status: active
boundary: 清洗、沖洗、必要鈍化、填充與基準取樣構成 commissioning gate，不代表具名 site 已通過、長期可靠或完成商業認列。
next_trigger: 具名多供應商 production site 發布簽核程序、L4／L5 測試、代表樣本與驗收結果。
-->

<!-- knowledge_edge
edge_id: KG-LCB-I20
view: industry
from_id: concept:liquid-cooling-loop-boundary
to_id: metric:coolant-monitoring-action-limits
relation: measured_by
claim_refs: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C9,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C10,MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES#C11
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-03
status: active
boundary: 文件列出監測、QA 與 trending 方法，沒有替每座場域指定相同採樣頻率、action limit、隔離權限或維修責任。
next_trigger: 具名場域公開 sampling plan、lab／sensor cross-check、action limits、責任矩陣與異常處置結果。
-->
