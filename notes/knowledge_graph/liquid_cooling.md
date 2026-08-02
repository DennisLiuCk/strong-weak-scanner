# 液冷 CDU 知識圖譜

容量、平台驗證、供應狀態、客戶部署與財務認列是不同維度。本圖不以 kW 大小排序
公司關聯強弱，也不把 Marketplace 列名或 MOU 改寫成訂單。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: liquid-cooling
root_node_id: concept:liquid-cooling
label: 液冷 CDU
summary: 把 CDU 額定能力、平台資格、系統整合與場域驗證拆開，並區分台廠列名和可辨識財務貢獻。
article_ids: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER
status: active
-->

<!-- knowledge_edge
edge_id: KG-LC-C01
view: company
from_id: company:3017
to_id: concept:liquid-cooling
relation: platform_lists
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C1,MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C7
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-09
status: active
boundary: AVC 與 3017 的實體映射、CDU 型號、1.2MW 與 Sample Ready 只到捕捉日，不證明客戶、訂單、收入、市占或毛利。
next_trigger: 3017 將具名 CDU 型號連到客戶驗收、量產數量、收入占比與毛利。
-->

<!-- knowledge_edge
edge_id: KG-LC-C02
view: company
from_id: company:2308
to_id: concept:liquid-cooling
relation: platform_lists
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-09
status: active
boundary: Delta 型號、1MW 與 MP Ready 是 Marketplace 原始欄位，不等於具名客戶、大量訂單、收入、市占、毛利或現金流。
next_trigger: 2308 揭露具名 CDU 客戶驗收、量產數量與可辨識財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-LC-C03
view: company
from_id: company:2301
to_id: concept:liquid-cooling
relation: platform_lists
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-09
status: active
boundary: LITEON 型號、380kW 與 Sample Ready 不證明量產規模、訂單、收入或產品優劣。
next_trigger: 2301 將具名 CDU 型號連到客戶驗收、出貨、收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-LC-C04
view: company
from_id: company:lg-electronics
to_id: concept:liquid-cooling
relation: validated_for
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-27
review_due: 2026-08-09
status: active
boundary: 公司稱 600kW CDU 通過超過 100 項評估，但沒有 Marketplace 同欄定義、供應狀態、客戶或訂單。
next_trigger: LGE 產品出現在可重現清單，或公司揭露客戶部署、採購與財務結果。
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
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-09
status: active
boundary: Marketplace 提供比較欄位與原始狀態，但頁面沒有完整跨廠測試協定或公司財務資料。
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
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C1,MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C5
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-09
status: active
boundary: 同欄容量可正規化比較，但 MW／kW 不是效率、產品優劣、成熟度或財務排名。
next_trigger: 平台公布完整測試協定、工況、流量、壓差、備援與效率定義。
-->

<!-- knowledge_edge
edge_id: KG-LC-I03
view: industry
from_id: concept:liquid-cooling
to_id: stage:platform-validation
relation: passes_through
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C1,MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-09
status: active
boundary: 平台驗證降低部分技術採購風險，但不等於客戶下單、完成部署或供應商認列收入。
next_trigger: 驗證條件與供應商狀態可用相同定義重現，並出現客戶驗收。
-->

<!-- knowledge_edge
edge_id: KG-LC-I04
view: industry
from_id: concept:liquid-cooling
to_id: stage:supply-status
relation: passes_through
claim_refs: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-09
status: active
boundary: Sample Ready 與 MP Ready 是平台原文類別，不能自行換算成產能、良率、訂單或收入。
next_trigger: 型號狀態換階段，或平台正式定義各狀態的供應與量產門檻。
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
