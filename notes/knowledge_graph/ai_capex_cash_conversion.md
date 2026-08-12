# AI CapEx 到供應商財務七關橋接知識圖譜

本圖先用承諾、資產、收入與現金四個時鐘拆開同一資料中心專案，再把雲端買方的資本計畫、
付款、資產上線、容量使用與現金回收，和台灣供應商的產品／公司財務歸因分開。三家公司已
揭露各自公司級財務結果；七關是研究框架，並不表示每一關都已有資料，更不把族群搜尋路由
當成任何個股的訂單、收入或獲利。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ai-capex-cash-conversion
root_node_id: concept:ai-capex-cash-conversion
label: AI CapEx 到供應商財務七關橋接
summary: 先分開承諾 資產 收入 現金四個時鐘，再從資本承諾 現金與租賃支出 資產建置上線 可用容量 工作負載與收入 買方現金回收追到供應商財務歸因，避免把買方 CapEx 直接換算成台灣公司受惠。
article_ids: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION
status: active
-->

<!-- knowledge_edge
edge_id: KG-ACC-C01
view: company
from_id: company:microsoft
to_id: concept:ai-capex-cash-conversion
relation: reports_financials
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C1
note_refs:
evidence_state: verified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-29
review_due: 2026-08-15
status: active
boundary: Microsoft 公司級 headline CapEx cash paid for PP&E OCF 與 FCF 可按其公式回溯；這不是可與 Meta Amazon 直接排名的 AI ROI，也沒有台灣供應商分子。
next_trigger: Microsoft 提供同期間資產類別 租賃現金 上線容量 使用收入與供應商財務的完整橋接。
-->

<!-- knowledge_edge
edge_id: KG-ACC-C02
view: company
from_id: company:meta
to_id: concept:ai-capex-cash-conversion
relation: reports_financials
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C1
note_refs:
evidence_state: verified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-29
review_due: 2026-08-15
status: active
boundary: Meta 公司級 cash PP&E finance-lease principal OCF 與自訂 FCF 可按其公式回溯；沒有 AI 資產批次 利用率或台灣供應商財務分子。
next_trigger: Meta 提供同期間資產類別 租賃增加 上線容量 使用收入與供應商財務的完整橋接。
-->

<!-- knowledge_edge
edge_id: KG-ACC-C03
view: company
from_id: company:amazon
to_id: concept:ai-capex-cash-conversion
relation: reports_financials
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C1
note_refs:
evidence_state: verified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-30
review_due: 2026-08-15
status: active
boundary: Amazon TTM OCF PP&E purchases incentives 與自訂 FCF 可按其公式回溯；TTM 不能和兩家單季直接排名，也沒有台灣供應商財務分子。
next_trigger: Amazon 提供可對齊的單季資產類別 租賃 上線容量 使用收入與供應商財務橋接。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I01
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: stage:capital-commitment
relation: passes_through
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C6
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 全年指引 預算或租賃承諾只表示配置意圖，不表示當期已付款 設備已交付或供應商已認列收入。
next_trigger: 公司以固定資產類別與期間把承諾調節到實際現金購置及租賃增加。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I02
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: stage:cash-ppe-and-leases
relation: passes_through
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C6
note_refs:
evidence_state: inference
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 現金 PP&E 租賃增加與租賃本金是不同欄位；合計支出仍包含建物 電力 網路與其他非 AI 專屬資產。
next_trigger: 三家公司以同期間揭露 cash PP&E finance-lease additions principal 其他租賃付款與 AI 資產分類。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I03
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: stage:asset-construction-commissioning
relation: passes_through
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C6
note_refs:
evidence_state: inference
commercial_stage: deployment
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 本輪來源沒有逐批在建工程 安裝 通電 試運轉 驗收與 placed-in-service 日期，不能由付款推定資產已可使用。
next_trigger: 買方公布同一資產批次的 CIP 轉入 可用日期 地點與容量分母。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I04
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: stage:service-capacity-available
relation: passes_through
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C6
note_refs:
evidence_state: inference
commercial_stage: deployment
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 公司需求評論不提供同一新增資產批次的可用運算 儲存 網路或電力容量，資產上線也不代表容量已被使用。
next_trigger: 買方用固定服務 單位 地區與時間窗揭露新增可用容量及啟用日期。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I05
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: stage:workload-utilization-revenue
relation: passes_through
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C6
note_refs:
evidence_state: inference
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: Azure AWS 成長與需求訊號沒有把收入 毛利或利用率歸因到同一批新增資產，不能據此重算增量資產 ROI。
next_trigger: 買方把同一容量批次連到可重算使用量 定價 收入 毛利與時間窗。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I06
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: stage:buyer-cash-conversion
relation: passes_through
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C6
note_refs:
evidence_state: inference
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 三家公司期間與 FCF 公式不同，且折舊與租賃分類會移動報表呈現；本圖不提供跨公司回收效率排名。
next_trigger: 對齊單季 OCF cash PP&E 租賃現金 營運資金 稅與資產範圍後再比較回收。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I07
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: stage:supplier-financial-attribution
relation: passes_through
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C5
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 買方來源沒有台灣供應商 料號 份額 出貨期間 單價 毛利或現金，因此沒有任何個股題材財務歸因。
next_trigger: 買方與供應商以同一平台 料號 期間 數量 驗收 收入分母 毛利及現金完成雙向核對。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I08
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: group:serverodm
relation: routes_to
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C5
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 伺服器 ODM 只是一個需求查找入口；總 CapEx 沒有伺服器台數 ODM 份額 驗收條件 收入或毛利。
next_trigger: 具名平台的買方驗收與 ODM 公司文件對上同一批數量 期間 收入 毛利與 OCF。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I09
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C5
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: PCB 只是一個需求查找入口；總 CapEx 沒有板種 層數 材料 客戶資格 數量 單價 收入或毛利。
next_trigger: 具名平台與 PCB 公司文件對上同一板件 資格 出貨期間 數量 收入 毛利與 OCF。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I10
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C5
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 電源供應器只是一個需求查找入口；總 CapEx 沒有電力架構 功率規格 供應商資格 數量 單價 收入或毛利。
next_trigger: 具名平台與電源公司文件對上同一 PSU 或電力模組 資格 出貨期間 收入 毛利與 OCF。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I11
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: group:thermal
relation: routes_to
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C5
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 散熱只是一個需求查找入口；總 CapEx 沒有風冷液冷比例 CDU 冷板 供應商資格 數量 收入或毛利。
next_trigger: 具名平台與散熱公司文件對上同一冷卻方案 資格 出貨期間 數量 收入 毛利與 OCF。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I12
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: concept:capital-asset-revenue-cash-clocks
relation: measured_by
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C9
note_refs:
evidence_state: inference
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: Meta 與 Amazon 申報能證明四個時點可分離，但沒有同一具名 AI 資產批次的合約 上線 使用 收入 付款與供應商收款全鏈。
next_trigger: 買方與供應商用同一平台或資產批次公開合約生效 placed-in-service 客戶使用 收入 付款及收款日期。
-->
