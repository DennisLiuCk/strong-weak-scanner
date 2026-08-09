# 知識圖譜主題模板

知識圖譜是既有研究的證據投影，不是用關鍵字共現自動產生的事實庫。每條線都必須引用
active topic claim 或 independently verified 正式筆記的確切 source；找不到證據時不要建線。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: example-topic
root_node_id: concept:example
label: 顯示名稱
summary: 用一句話說明此圖能回答什麼，以及不能回答什麼。
article_ids: MI-YYYY-MM-DD-EXAMPLE
status: active
-->

<!-- knowledge_edge
edge_id: KG-EXAMPLE-C01
view: company
from_id: company:1234
to_id: concept:example
relation: has_capability
claim_refs: MI-YYYY-MM-DD-EXAMPLE#C1
note_refs: 1234#S1
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: YYYY-MM-DD
review_due: YYYY-MM-DD
status: active
boundary: 這條線直接支持到哪裡，以及不能外推成哪些訂單、收入、市占或獨家結論。
next_trigger: 哪一份文件、客戶節點或財務欄位會使這條線升級、縮窄或失效。
-->

欄位契約：

- `view`：`company` 或 `industry`。前者至少一端是 company；後者不得直接放 company。
- `relation`：受控詞彙，由 `scripts/knowledge_graph.py` 的 `RELATION_LABELS` 定義。
- `evidence_state`：`verified`、`inference`、`unverified`；不得強於引用 claim。
- `commercial_stage`：技術／商業成熟度，與證據強度分開。
- `materiality`：`unknown`、`adjacent`、`named_product`、`financial`；只有 verified 且
  `commercial_stage: financial`，並有 active `financial_materiality` v2 `direct` assessment
  才能使用 `financial`。
- `exclusivity`：`unknown`、`multi_source`、`limited_source`、`sole_source`。非 unknown
  必須填 `exclusivity_scope`，待驗證線不得宣稱供應集中度。
- `claim_refs`／`note_refs`：至少填一種；多筆以逗號分隔。
- MVP 每條 active edge 都必須直接連到 `root_node_id`，避免一開始變成不可讀的毛線球。

財務材料性契約 v2：

<!-- financial_materiality
contract_version: 2
assessment_id: FM-EXAMPLE-01
edge_id: KG-EXAMPLE-C01
financial_scope: product
metric: example_product_revenue
value_kind: reported
reported_value: 12.34
unit: TWD_100m
period_start: YYYY-MM-DD
period_end: YYYY-MM-DD
period_basis: quarter
denominator_metric: consolidated_revenue
denominator_value: 100.00
denominator_unit: TWD_100m
share_percent: 12.34
attribution_status: bounded_proxy
source_refs: QUAL-1234#S1
calculation:
as_of: YYYY-MM-DD
review_due: YYYY-MM-DD
status: active
metric_definition: 分子涵蓋哪些產品、地區、會計科目與合併範圍。
denominator_definition: 分母的公司、期間、會計科目與合併範圍。
boundary: 代理範圍比題材更廣；不能把 12.34% 改寫成題材收入占比。
next_trigger: 公司首次以相同期間與分母揭露題材收入或毛利。
-->

- `financial_scope`：`company_total`、`segment`、`product`、`unit_economics`。
- `attribution_status`：`direct`、`bounded_proxy`、`not_disclosed`。公司總額只能是
  `not_disclosed`，且不得填題材占比；`direct`／`bounded_proxy` 不得使用公司總額，
  必須填可重算的 `share_percent`。
- `source_refs` 必須是 linked edge 已解析出的 exact source ref；不得只貼文章首頁。
- `value_kind: derived` 必須填 `calculation`；所有 assessment 都必須有期間、分母定義、
  證據邊界與下一個升降級節點。
- 只有 `direct` 能把 edge 升為 `materiality: financial`；`bounded_proxy` 表示已量出較寬
  產品／事業部範圍，但仍不能歸因到圖譜題材。

新增節點前，先查 `config/knowledge_concepts.csv`、`config/external_entities.csv` 與
`config/universe.csv`，避免同義詞重複建點。發布前執行：

```powershell
python scripts/research_queue.py --lint
python scripts/knowledge_graph.py --lint
```
