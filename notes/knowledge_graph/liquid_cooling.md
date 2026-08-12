# 液冷 CDU 知識圖譜

容量、操作包絡線、可靠度、平台驗證、供應狀態、客戶部署與財務認列是不同維度。本圖不以
kW 大小排序公司關聯強弱，也不把 OCP 通用方法、Marketplace 列名或 MOU 改寫成產品通過、
訂單或收入。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: liquid-cooling
root_node_id: concept:liquid-cooling
label: 液冷 CDU
summary: 把 CDU 額定能力拆成熱性能、TCS 壓頭、FWS 阻抗與具位置單位時間品質的量測上下文，再把平台資格、系統整合、場域驗證和可辨識財務貢獻分開。
article_ids: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER
status: active
-->

<!-- knowledge_edge
edge_id: KG-LC-C01
view: company
from_id: company:3017
to_id: concept:liquid-cooling
relation: platform_lists
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C1,MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C7,MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C8
note_refs: 3017#S1
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-16
status: active
boundary: AVC 與 3017 的實體映射、CDU 型號、1.2MW 與 Sample Ready 在 2026-08-09 捕捉仍可定位；這不證明客戶、訂單、收入、市占或毛利。
next_trigger: 3017 將具名 CDU 型號連到客戶驗收、量產數量、收入占比與毛利。
-->

<!-- financial_materiality
contract_version: 2
assessment_id: FM-LC-3017-01
edge_id: KG-LC-C01
financial_scope: product
metric: thermal_products_revenue
value_kind: reported
reported_value: 311.91
unit: TWD_100m
period_start: 2026-01-01
period_end: 2026-03-31
period_basis: quarter
denominator_metric: consolidated_revenue
denominator_value: 490.38
denominator_unit: TWD_100m
share_percent: 63.6
attribution_status: bounded_proxy
source_refs: QUAL-3017#S1
calculation:
as_of: 2026-08-09
review_due: 2026-08-20
status: active
metric_definition: 奇鋐 2026Q1 公司揭露的散熱產品收入，涵蓋範圍大於液冷與 CDU。
denominator_definition: 奇鋐 2026Q1 合併營收 490.38 億元，與散熱產品收入為同一期間及合併範圍。
boundary: 63.6% 是散熱產品占公司營收的有界代理，不是液冷、CDU 或特定客戶收入占比；公司未拆出各散熱產品毛利。
next_trigger: 奇鋐以同期間合併分母單獨揭露液冷／CDU 收入、出貨量乘單價或毛利。
-->

<!-- knowledge_edge
edge_id: KG-LC-C02
view: company
from_id: company:2308
to_id: concept:liquid-cooling
relation: platform_lists
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C1,MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C8
note_refs: 2308#S4
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-16
status: active
boundary: Delta 型號、1MW 與 MP Ready 在 2026-08-09 捕捉仍是 Marketplace 原始欄位；不等於具名客戶、大量訂單、收入、市占、毛利或現金流。
next_trigger: 2308 揭露具名 CDU 客戶驗收、量產數量與可辨識財務貢獻。
-->

<!-- financial_materiality
contract_version: 2
assessment_id: FM-LC-2308-01
edge_id: KG-LC-C02
financial_scope: segment
metric: power_and_components_revenue
value_kind: reported
reported_value: 856.23
unit: TWD_100m
period_start: 2026-01-01
period_end: 2026-03-31
period_basis: quarter
denominator_metric: consolidated_revenue
denominator_value: 1594.00
denominator_unit: TWD_100m
share_percent: 54.0
attribution_status: bounded_proxy
source_refs: QUAL-2308#S4
calculation:
as_of: 2026-08-09
review_due: 2026-08-31
status: active
metric_definition: 台達電 2026Q1 電源及零組件事業營收，包含電源、零組件與散熱等多種產品。
denominator_definition: 台達電 2026Q1 合併營收約 1,594 億元；簡報事業占比以整數百分比揭露。
boundary: 54% 是電源及零組件事業占公司營收的有界代理，不是液冷、CDU、AI 電源或資料中心收入占比；四捨五入口徑使金額重算約 53.72%。
next_trigger: 台達電以同期間合併分母單獨揭露液冷／CDU 或 AI 電源收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-LC-C03
view: company
from_id: company:2301
to_id: concept:liquid-cooling
relation: platform_lists
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C1,MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C8
note_refs: 2301#S3
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-16
status: active
boundary: LITEON 型號、380kW 與 Sample Ready 在 2026-08-09 捕捉仍可定位；不證明量產規模、訂單、收入或產品優劣。
next_trigger: 2301 將具名 CDU 型號連到客戶驗收、出貨、收入與毛利。
-->

<!-- financial_materiality
contract_version: 2
assessment_id: FM-LC-2301-01
edge_id: KG-LC-C03
financial_scope: segment
metric: cloud_and_iot_external_revenue
value_kind: reported
reported_value: 229.03
unit: TWD_100m
period_start: 2026-01-01
period_end: 2026-03-31
period_basis: quarter
denominator_metric: consolidated_revenue
denominator_value: 434.07
denominator_unit: TWD_100m
share_percent: 52.8
attribution_status: bounded_proxy
source_refs: QUAL-2301#S3
calculation:
as_of: 2026-08-09
review_due: 2026-08-31
status: active
metric_definition: 光寶科 2026Q1 雲端及物聯網部門外部營收，亦包含網通、AIoT、影像等非 AI 電源產品。
denominator_definition: 光寶科 2026Q1 合併營收 434.07 億元，與部門外部營收為同一期間及合併範圍。
boundary: 52.8% 是雲端及物聯網部門占公司營收的有界代理，不是 CDU、AI 電源或特定電源產品收入占比。
next_trigger: 光寶科以同期間合併分母單獨揭露 CDU／AI 電源收入、出貨量乘單價或毛利。
-->

<!-- knowledge_edge
edge_id: KG-LC-C04
view: company
from_id: company:lg-electronics
to_id: concept:liquid-cooling
relation: validated_for
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C2,MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C8
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-16
status: active
boundary: LGE 600kW／850LPM 與 validation type 已在 2026-08-09 Marketplace 捕捉可定位，但供應狀態欄空白；不能代填為 Sample Ready、MP Ready、客戶或訂單。
next_trigger: Marketplace 明示 LGE 原始供應狀態，或公司揭露客戶部署、採購與財務結果。
-->

<!-- knowledge_edge
edge_id: KG-LC-C05
view: company
from_id: company:daikin
to_id: concept:liquid-cooling
relation: integrates
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C3,MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-06
review_due: 2026-08-09
status: active
boundary: MOU portfolio 與 PoC 時鐘不等於產品完成、客戶採購、節電效果或收入。
next_trigger: PoC 公布可重算的節電、成本、可靠度結果或正式商用部署。
-->

<!-- knowledge_edge
edge_id: KG-LC-C06
view: company
from_id: company:ntt-data
to_id: concept:liquid-cooling
relation: runs_poc
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: poc
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-06
review_due: 2026-08-09
status: active
boundary: 2026-07 至 2027-03 的 PoC 與 FY2027 商用目標都是驗證時鐘，不是已完成節能或採購。
next_trigger: NTT DATA 或 Daikin 發布基線、結果、部署範圍與商用採購。
-->

<!-- knowledge_edge
edge_id: KG-LC-C07
view: company
from_id: company:nvidia
to_id: concept:liquid-cooling
relation: owns_platform
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C8
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-16
status: active
boundary: Marketplace 在 2026-08-09 提供四個具名列項、比較欄位與原始狀態；動態頁仍沒有完整跨廠測試協定、不可變歷史或公司財務資料。
next_trigger: Marketplace 更新 validation type、supply status、型號或 4°C ATD 定義。
-->

<!-- knowledge_edge
edge_id: KG-LC-I01
view: industry
from_id: concept:liquid-cooling
to_id: component:cdu
relation: contains
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C5
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-09
status: active
boundary: CDU 是液冷系統中的設備，不等於 GPU 冷板、chiller 或完整機房冷卻方案。
next_trigger: 系統商以相同架構揭露 CDU、冷板、chiller 與控制的責任邊界。
-->

<!-- knowledge_edge
edge_id: KG-LC-I02
view: industry
from_id: concept:liquid-cooling
to_id: metric:cooling-capacity-4c-atd
relation: measured_by
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C8,MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C11,MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C14
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 4°C ATD 同欄容量可正規化比較標示值，但仍缺同型號三張性能曲線、量測位置與校正；MW／kW 不是效率、成熟度或財務排名。
next_trigger: 平台對具名型號公布熱性能、TCS 壓頭、FWS 阻抗、量測品質、備援與 pass／fail。
-->

<!-- knowledge_edge
edge_id: KG-LC-I03
view: industry
from_id: concept:liquid-cooling
to_id: stage:platform-validation
relation: passes_through
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C2,MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C8
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-16
status: active
boundary: 平台驗證與 2026-08-09 列名降低部分技術採購風險，但不等於共同測試條件、客戶下單、完成部署或供應商認列收入。
next_trigger: 驗證條件與供應狀態以相同定義重現，並出現具名客戶驗收。
-->

<!-- knowledge_edge
edge_id: KG-LC-I04
view: industry
from_id: concept:liquid-cooling
to_id: stage:supply-status
relation: passes_through
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C8
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-16
status: active
boundary: Sample Ready、MP Ready 與空白欄都是 2026-08-09 平台原始狀態；不能自行換算成產能、良率、訂單或收入，也不能替空白補階段。
next_trigger: 型號狀態換階段，或平台正式定義各狀態與空白欄位的供應及量產門檻。
-->

<!-- knowledge_edge
edge_id: KG-LC-I05
view: industry
from_id: concept:liquid-cooling
to_id: process:system-integration
relation: requires
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-11
review_due: 2026-08-09
status: active
boundary: 100 至 3000kW 是 MOU portfolio scope，不是單一產品額定值、完成部署或未來收入。
next_trigger: 合作方案完成產品化、客戶驗收並揭露部署範圍。
-->

<!-- knowledge_edge
edge_id: KG-LC-I06
view: industry
from_id: concept:liquid-cooling
to_id: process:field-poc
relation: moves_to
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: poc
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-06
review_due: 2026-08-09
status: active
boundary: PoC 只代表規劃驗證，不證明節能、成本、可用率或商業接受度已改善。
next_trigger: 2027-03 前公布可重算結果，或正式商用部署與採購。
-->

<!-- knowledge_edge
edge_id: KG-LC-I07
view: industry
from_id: concept:liquid-cooling
to_id: component:chiller-hvac
relation: includes
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-06
review_due: 2026-08-09
status: active
boundary: 設施端 HVAC／chiller 與控制可能承接價值，但現有 PoC 尚未分解價值、節電或收入歸屬。
next_trigger: PoC 分解 CDU、chiller、HVAC 與控制軟體對結果的貢獻。
-->

<!-- knowledge_edge
edge_id: KG-LC-I08
view: industry
from_id: concept:liquid-cooling
to_id: group:thermal
relation: routes_to
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C5
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-09
status: active
boundary: 散熱族群是產品與認證搜尋路由，不代表族群內公司都具 CDU、客戶或財務貢獻。
next_trigger: 公司文件具名 CDU 型號、資格、量產與財務結果。
-->

<!-- knowledge_edge
edge_id: KG-LC-I09
view: industry
from_id: concept:liquid-cooling
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C5
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-09
status: active
boundary: 電源供應族群只因具名公司兼營資料中心基礎設施而成為搜尋路由，不代表電源本業與 CDU 財務可合併。
next_trigger: 公司以產品與分部資料拆出液冷客戶、出貨、收入及毛利。
-->

<!-- knowledge_edge
edge_id: KG-LC-I10
view: industry
from_id: concept:liquid-cooling
to_id: metric:cdu-operating-envelope
relation: measured_by
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C10
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: OCP 建議把容量連同冷卻液 ATD FWS／TCS 流量與壓力閱讀；這不是 NVIDIA 各型號已採相同 protocol 或現場可達相同工作點的證明。
next_trigger: 平台公開具名型號、版本、完整熱／水力條件、原始資料與 pass／fail，使跨產品工作點可重現。
-->

<!-- knowledge_edge
edge_id: KG-LC-I11
view: industry
from_id: concept:liquid-cooling
to_id: stage:cdu-assembly-qualification
relation: passes_through
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C10
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 元件層與完整系統層是 OCP 方法中的不同 qualification 範圍；通用方法不證明任何 Marketplace 型號已完成兩層驗證或取得客戶驗收。
next_trigger: 具名產品的版本化 evidence packet 同時列出元件與整機範圍、條件、原始資料、結果及限制。
-->

<!-- knowledge_edge
edge_id: KG-LC-I12
view: industry
from_id: concept:liquid-cooling
to_id: capability:cdu-reliability-validation
relation: requires
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C10
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 材料相容性、水壓、衝擊／振動、熱循環與法規文件是不同證據類別；通過單項不等於完整產品、場域、訂單或財務驗證。
next_trigger: 平台或客戶公開具名型號的完整 reliability matrix、測試版本、pass／fail、失效處置及變更控制。
-->

<!-- knowledge_edge
edge_id: KG-LC-I13
view: industry
from_id: concept:liquid-cooling
to_id: metric:cdu-thermal-performance-curve
relation: measured_by
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2024-11-01
review_due: 2026-08-31
status: active
boundary: OCP 把 ATD 與指定流量下的熱負載接成性能曲線；通用示例不證明 Marketplace 具名型號採相同條件、已通過或現場可達。
next_trigger: 具名型號公開版本化 ATD 熱負載曲線、流體、兩側流量、進水溫度、原始資料與 pass／fail。
-->

<!-- knowledge_edge
edge_id: KG-LC-I14
view: industry
from_id: concept:liquid-cooling
to_id: metric:cdu-tcs-pressure-head-curve
relation: measured_by
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2024-11-01
review_due: 2026-08-31
status: active
boundary: TCS 壓頭曲線只描述 CDU 二次側泵浦在流量下的能力；不證明具名伺服器迴路阻力、支路平衡、備援切換或長期可靠。
next_trigger: 具名型號與目標 rack loop 公開同流量下的 CDU 壓頭、系統阻力、最差支路及泵浦失效工作點。
-->

<!-- knowledge_edge
edge_id: KG-LC-I15
view: industry
from_id: concept:liquid-cooling
to_id: metric:cdu-fws-impedance-curve
relation: measured_by
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2024-11-01
review_due: 2026-08-31
status: active
boundary: FWS 阻抗曲線只描述設施水流過 CDU 一次側的壓差需求；不證明具名機房已供足水溫、流量、壓力或完成全年調試。
next_trigger: 具名場域把 CDU FWS 阻抗曲線對回設施泵浦曲線、季節條件、commissioning 原始資料與驗收結果。
-->

<!-- knowledge_edge
edge_id: KG-LC-I16
view: industry
from_id: concept:liquid-cooling
to_id: capability:typed-event-context
relation: requires
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C13
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: DSX 讓 CDU 值帶設備與位置、單位、時間及 quality，並分開感測與控制請求；資料可解讀不等於感測器已校正、曲線已重現或場域已驗收。
next_trigger: 具名部署公開點位清單、位置、校正／不確定度、時間同步、quality 規則、穩態資料與控制 guardrail 驗收。
-->
