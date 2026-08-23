# AI CapEx 到供應商財務七關橋接知識圖譜

本圖先用承諾、資產、收入與現金四個時鐘拆開同一資料中心專案；遇到殘值保證時，先把揭露上限
放在第 0 層，再以六個或有現金檢查點分開可服務、起租生效、付款或違約、資產回收、補差額與補償；
遇到長期研究計畫時，另把 planned envelope、期間 R&D、PP&E／incentive、研究設施、技術轉移／產能與供應商財務分成六本帳。之後才把雲端買方的資本計畫、
付款、資產上線、容量使用與現金回收，和台灣供應商的產品／公司財務歸因分開。公司級財務結果
與單一交易條款已有公開資料；七關仍只是研究框架，不表示每一關都有資料，也不把族群搜尋路由
當成任何個股的訂單、收入或獲利。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ai-capex-cash-conversion
root_node_id: concept:ai-capex-cash-conversion
label: AI CapEx 到供應商財務七關橋接
summary: 先分開承諾 資產 收入 現金四個時鐘，殘值保證另拆生效 違約 回收 補差額與補償，長期研發另拆計畫 費用 PP&E／incentive 設施執行 技術轉移／產能及供應商財務，再從資本承諾追到供應商歸因，避免把 headline 直接換算成當期支出 產能 訂單與台灣公司受惠。
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
edge_id: KG-ACC-C04
view: company
from_id: company:nvidia
to_id: concept:ai-capex-cash-conversion
relation: reports_financials
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C16,MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C17
note_refs:
evidence_state: verified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-17
review_due: 2026-08-27
status: active
boundary: NVIDIA 8-K 只證明 PORTS-Pike 初始保證的附條件累計上限與違約後回收／補差額摘要；它不是當期 CapEx、已支付 1,050 億美元、預期損失或台灣供應商財務。
next_trigger: NVIDIA 在 10-Q 提交完整 Agreements form，或正式揭露逐租約起租 ready-for-service Trigger Event 回收 實際付款與 OpenAI 補償。
-->

<!-- knowledge_edge
edge_id: KG-ACC-C05
view: company
from_id: company:micron
to_id: concept:ai-capex-cash-conversion
relation: reports_financials
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C21
note_refs:
evidence_state: verified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-25
review_due: 2026-09-30
status: active
boundary: Micron 較早 10-Q 只證明公司級 R&D expense PP&E cash incentive 與全年 net CapEx estimate 分開揭露；它早於 Labs 公告，不能證明計畫已包含或排除於任一數字，也沒有 Labs 或供應商財務分子。
next_trigger: Micron 以同一 Labs program 或 facility key 公布年度 plan-to-actual R&D／PP&E／incentive 建置 研究產出 技術轉移 qualification capacity及vendor／financial attribution。
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

<!-- knowledge_edge
edge_id: KG-ACC-I13
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: process:residual-value-guarantee-cash-waterfall
relation: measured_by
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C18
note_refs:
evidence_state: inference
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-17
review_due: 2026-08-27
status: active
boundary: PORTS-Pike 三份官方文件只對應同一交易；1,050 億美元是初始保證的累計付款上限，不是當期 CapEx、已付款或預期損失，15 億美元股權投資與 IT-GW 容量另屬不同帳本。
next_trigger: NVIDIA 後續 10-Q 提交完整 Agreements form，或逐租約出現起租 ready-for-service Trigger Event 重租／出售回收 實際補差額與 OpenAI 補償。
-->

<!-- knowledge_edge
edge_id: KG-ACC-I14
view: industry
from_id: concept:ai-capex-cash-conversion
to_id: process:rd-plan-expense-capex-execution-capacity-order-passport
relation: measured_by
claim_refs: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION#C22
note_refs:
evidence_state: inference
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-23
review_due: 2026-09-30
status: active
boundary: 六本帳是研究中心的可追溯框架而非 Micron 會計政策；兩份文件屬同一公司鏈且 10-Q 早於 Labs 公告，沒有同一 project 的年度 actual 技術轉移 產能與 supplier order 共同鍵。
next_trigger: 同一研究 program 或 facility 首次把 planned envelope 接到期間費用與現金 建置啟用 研究成果 qualification 增量產能及 supplier PO／出貨／驗收／財務。
-->
