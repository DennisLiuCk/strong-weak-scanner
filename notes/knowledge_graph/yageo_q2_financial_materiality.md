# 國巨 2026Q2 公司財務分母知識圖譜

本圖只回答「研究中心是否已把一個具名 universe 公司連到可重算的財務結果」。它不把
國巨整體季度營收拆成 AI、MLCC、鉭質電容或其他產品貢獻，也不把營收、淨利、公司定義
自由現金流與期末現金存量畫成同一筆錢。
依財務材料性契約 v2，這是 `company_total`／`not_disclosed` 分母錨點，不是題材財務材料性。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: yageo-q2-financial-materiality
root_node_id: concept:yageo-q2-financial-materiality
label: 國巨 Q2 公司財務分母
summary: 以國巨公司簡報與 TWSE 逐月營收交叉重算季度公司總額，再把淨利 公司定義自由現金流 期末現金與營運資金代理分帳，示範 v2 如何保留題材與現金歸因缺口。
article_ids: MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL
status: active
-->

<!-- knowledge_edge
edge_id: KG-YQ2-C01
view: company
from_id: company:2327
to_id: concept:yageo-q2-financial-materiality
relation: reports_financials
claim_refs: MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL#C5
note_refs:
evidence_state: verified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-23
status: active
boundary: 兩條獨立官方來源只交叉驗證國巨 2026Q2 合併營收 444.56327 億元；這不是 AI、MLCC 或鉭質電容收入，也不支持毛利率、EPS、現金流、訂單、交期或長約的獨立交叉驗證。
next_trigger: 完整 2026Q2 核閱報告與附註可重算現金流、存貨、應收及借款，且公司文件把產品／AI 組合連到收入與毛利分母。
-->

<!-- financial_materiality
contract_version: 2
assessment_id: FM-YQ2-2327-01
edge_id: KG-YQ2-C01
financial_scope: company_total
metric: consolidated_revenue
value_kind: reported
reported_value: 444.56327
unit: TWD_100m
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: quarter
denominator_metric: consolidated_revenue
denominator_value: 444.56327
denominator_unit: TWD_100m
share_percent:
attribution_status: not_disclosed
source_refs: MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL#S2,MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL#S4
calculation:
as_of: 2026-08-09
review_due: 2026-08-23
status: active
metric_definition: 國巨 2026Q2 合併營收公司總額；公司簡報數字由 TWSE 2026 年 4 至 6 月逐月營收交叉重算。
denominator_definition: 同期間、同合併範圍的國巨合併營收；此處只建立公司財務分母。
boundary: 題材或產品分子未揭露，因此沒有題材占比；444.56327 億元不得改寫成 AI、MLCC、鉭質電容或任一產品收入。
next_trigger: 公司以相同期間與合併分母揭露產品／AI 收入或毛利，並能由一手文件重算占比。
-->

<!-- knowledge_edge
edge_id: KG-YQ2-I01
view: industry
from_id: concept:yageo-q2-financial-materiality
to_id: group:passive
relation: routes_to
claim_refs: MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL#C5
note_refs:
evidence_state: inference
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-23
status: active
boundary: 國巨是 passive universe 公司，因此公司級財務結果可作族群研究入口；總營收不能代表被動元件全族群、任一產品線或其他公司同步成長。
next_trigger: 以相同期間與一致分母建立產品別財務橋接，再與其他 passive 公司逐一比較，而不是用單一公司總營收代替族群結論。
-->

<!-- knowledge_edge
edge_id: KG-YQ2-I02
view: industry
from_id: concept:yageo-q2-financial-materiality
to_id: concept:profit-fcf-cash-stock-ledgers
relation: includes
claim_refs: MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL#C6,MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL#C7
note_refs:
evidence_state: inference
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-15
status: active
boundary: 國巨簡報可定位相鄰兩季淨利 公司定義自由現金流與期末現金，但沒有完整自由現金流公式與現金流量表；三本帳是研究中心的對讀框架，不是國巨公布的現金轉換模型。
next_trigger: 取得完整 Q2 核閱財報與公司自由現金流公式，把營業 投資 融資 匯率 合併範圍 受限現金與金融負債接成可重算橋。
-->

<!-- knowledge_edge
edge_id: KG-YQ2-I03
view: industry
from_id: concept:yageo-q2-financial-materiality
to_id: metric:working-capital-intensity-proxy
relation: measured_by
claim_refs: MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL#C8
note_refs:
evidence_state: inference
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-15
status: active
boundary: 期末應收 存貨 應付除以單季營收或成本只是同公司相鄰季度診斷；未用平均餘額 未納入其他營運項目與合併範圍 不得稱為正式 DSO DIO DPO 或現金流原因。
next_trigger: 完整季報提供營運資金現金流調節 帳齡 品類 備抵 合併範圍與平均餘額後，再計算正式周轉日並與後續季度同口徑重算。
-->
