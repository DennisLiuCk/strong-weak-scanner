# 製程控制量測系統契約知識圖譜

本圖把「量測結果是否可信」與「產線如何抽樣、分類、警報、攔截及處置」分成前後兩層，
先用 base rate、四格與不對稱錯判成本固定門檻，再把 OCAP、實際圍堵、製造履歷與修正後放行
接成事件護照。通用方法可建立查核欄位，但不替任何 HBM 產線、設備商資格、良率改善或台灣公司財務貢獻背書。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: process-control-measurement-contract
root_node_id: concept:measurement-system-contract
label: 製程控制量測系統契約
summary: 先固定被測量 方法環境 參考校正 偏差變異與不確定度 再以base rate 四格 門檻 複判容量與漏失成本接抽樣 逃逸 偽警報 OCAP 圍堵履歷及放行事件 避免把accuracy 精細數字或警報速度直接當成可信決策 良率改善或設備收入。
article_ids: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY
status: active
-->

<!-- knowledge_edge
edge_id: KG-PCMC-C01
view: company
from_id: company:kla
to_id: concept:measurement-system-contract
relation: provides_tooling
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C13,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C17
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: limited_source
exclusivity_scope: KLA 公告列出自家 advanced packaging 工具與任務分工 本輪沒有第二家供應商對相同 measurement-system contract 的共同結果。
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: KLA 具名工具可支援部分 inline post-dicing screening metrology 任務 不等於完整六欄量測系統已被客戶公開驗證 也不證明部署量 收入或獨家。
next_trigger: KLA 與客戶共同公布同一產品的 measurand method calibration uncertainty control plan qualification 與量產結果。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-C02
view: company
from_id: company:nova
to_id: concept:measurement-system-contract
relation: reports_financials
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C21
note_refs:
evidence_state: verified
commercial_stage: financial
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-06
review_due: 2026-08-14
status: active
boundary: Nova 只表示 Sentronics advanced-packaging dimensional-metrology solutions 是創高產品線之一，沒有題材金額、占比、HBM 分解，也未公開被測量、校正、不確定度、control plan 或客戶製造結果。
next_trigger: Nova 與客戶對同一具名產品公開 AP 收入或訂單分子及公司分母，並把 measurement-system contract 接到量產 control-plan decision 與結果。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I01
view: industry
from_id: capability:process-control
to_id: concept:measurement-system-contract
relation: requires
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C17
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 量測系統六欄是研究中心依 NIST 方法整理的查核框架 不是共同半導體標準或客戶量產 recipe。
next_trigger: 客戶端對同一產品 layer 公開版本化量測系統紀錄並接到實際製程決策與結果。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I02
view: industry
from_id: concept:measurement-system-contract
to_id: metric:measurement-measurand-decision
relation: includes
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C16
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: NIST traceability 文件與 e-Handbook 都要求先界定量測對象與結果用途 但不限定半導體產品的決策門檻。
as_of: 2021-05-06
review_due: 2026-08-31
status: active
boundary: 被測量與用途是通用計量要件 不代表本文已知特定 HBM 結構 規格值或 pass fail rule。
next_trigger: 具名量產產品公開 measurand unit specification range 與放行隔離重工或調參用途。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I03
view: industry
from_id: concept:measurement-system-contract
to_id: capability:measurement-method-context
relation: includes
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C15,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C16
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: 兩份 NIST 方法鏈共同要求說明量測系統與工作條件 但未提供半導體共同 recipe。
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 通用方法要求不證明任何設備 recipe 演算法 組態或環境已被客戶固定並通過資格。
next_trigger: 客戶公開 method sample preparation recipe version configuration operator environment 與變更控制。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I04
view: industry
from_id: concept:measurement-system-contract
to_id: capability:measurement-reference-traceability
relation: requires
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C16
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: limited_source
exclusivity_scope: 本圖的直接定義來源是 NIST Technical Note 2156 不是多家半導體客戶的共同 qualification 文件。
as_of: 2021-05-06
review_due: 2026-08-31
status: active
boundary: 可追溯屬於特定量測結果 且不表示不確定度適合用途 也不是 NIST 對設備品牌的背書。
next_trigger: 具名量產量測結果公開 reference calibration chain uncertainty contribution 與 measurement assurance。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I05
view: industry
from_id: concept:measurement-system-contract
to_id: metric:measurement-bias-resolution-linearity
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C15
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: limited_source
exclusivity_scope: NIST SEMATECH e-Handbook 列出 bias resolution linearity 等通用誤差來源 未提供 HBM 門檻。
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 知道應量化的誤差來源不等於特定設備已達到產品需要的 accuracy range 或 resolution。
next_trigger: 同一產品量程公開 reference bias resolution linearity curve acceptance limit 與判定結果。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I06
view: industry
from_id: concept:measurement-system-contract
to_id: metric:measurement-repeatability-reproducibility-stability
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C15
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: limited_source
exclusivity_scope: NIST SEMATECH 手冊使用自身 repeatability reproducibility stability 定義 其他標準細部用語可能不同。
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 通用 Gauge R and R 欄位不指定客戶 study design 樣本 統計門檻或工作環境結果。
next_trigger: 具名客戶公開同機短期 跨機跨日及長期漂移研究的完整分母與允收規則。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I07
view: industry
from_id: concept:measurement-system-contract
to_id: metric:measurement-uncertainty-decision-rule
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C15,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C16
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: NIST 兩份方法來源都要求 uncertainty 但沒有替特定半導體規格設定 guard band 或 decision rule。
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 報告不確定度不自動代表 fit for purpose 仍需由結果使用者按決策風險設定判定方法。
next_trigger: 同一產品公開 uncertainty budget specification limit guard band disposition 及錯判後果。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I08
view: industry
from_id: concept:measurement-system-contract
to_id: concept:inspection-control-plan
relation: moves_to
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C17
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 兩層先後是研究查核順序 不代表所有工廠採同名文件 同一工具或固定流程。
next_trigger: 客戶版本文件把 qualified measurement system 明確接到 sampling alarm containment 與 disposition。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I09
view: industry
from_id: concept:measurement-system-contract
to_id: metric:inspection-sampling-coverage
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C14
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 抽樣單位與覆蓋是研究欄位 不是全產業共同 sampling rate 或全面檢查要求。
next_trigger: 同一量產產品公開 lot wafer die site package 分母與動態抽樣規則。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I10
view: industry
from_id: concept:measurement-system-contract
to_id: metric:defect-sensitivity-escape
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C14
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 解析度或供應商 sensitivity 敘述不能替代 killer defect definition escape rate 與後續產品失效。
next_trigger: 客戶公開 target defect truth set sensitivity escape downstream failure 與完整分母。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I11
view: industry
from_id: concept:measurement-system-contract
to_id: metric:nuisance-false-alarm
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C14
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 找到更多 defect candidates 不代表關鍵缺陷增加 AI 分類功能也不等於已知 false alarm denominator。
next_trigger: 同一 truth set 公開 true defect nuisance misclassification review capacity 與決策影響。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I12
view: industry
from_id: concept:measurement-system-contract
to_id: metric:inspection-cycle-time
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C14
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 單機 throughput 或 image time 不能替代量測複判分類決策與產線圍堵的完整 elapsed time。
next_trigger: 客戶公開從 sample 到 disposition 的 timestamp 分解 WIP 及受影響產品數。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I13
view: industry
from_id: concept:measurement-system-contract
to_id: capability:excursion-containment
relation: requires
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C14
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 看見異常不等於已停線隔離重工或找到根因 也不能直接改寫成良率改善。
next_trigger: 客戶公開 alarm threshold lot tool isolation disposition root cause recovery 與製造結果。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I14
view: industry
from_id: concept:measurement-system-contract
to_id: group:semiequip
relation: routes_to
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 量測與檢查方法只建立設備族群搜尋入口 沒有 universe 公司具名產品 客戶資格 訂單或財務貢獻。
next_trigger: 台灣設備公司與客戶雙向確認具名 measurement task qualification deployment 收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I15
view: industry
from_id: concept:measurement-system-contract
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 封測廠是方法使用端不代表增加檢查必然提高收入 毛利或採購台灣設備。
next_trigger: OSAT 與客戶公開同一產品量測契約 control plan 良率結果 資本支出及財務影響。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-C03
view: company
from_id: company:tsmc
to_id: concept:measurement-system-contract
relation: has_capability
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C36
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: limited_source
exclusivity_scope: 台積電現行頁面公開自家先進封裝 per-die identification process history tool logs material data yield impact-scope 與 root-cause 功能 本輪沒有第二家客戶以相同欄位公開量產結果。
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: 公司功能頁沒有 product recipe OCAP 九事件時間戳 受影響數 重工報廢 放行 良率成本或外部工具商財務 不能外推成產業共同部署。
next_trigger: 第二家客戶或台積電版本化量產文件公開同產品事件履歷 affected-object set disposition release 及結果。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I16
view: industry
from_id: concept:measurement-system-contract
to_id: process:out-of-control-action-plan
relation: requires
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C35
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: limited_source
exclusivity_scope: NIST SEMATECH 手冊直接把 process monitoring 後的 OCAP 與 automated intervention 分開 但未證明半導體客戶採用同一流程。
as_of: 2003-06-01
review_due: 2026-08-31
status: active
boundary: 通用 OCAP 定義不指定 advanced-packaging alarm threshold owner stop hold recovery latency 或製造結果。
next_trigger: 具名客戶公開同產品 process-specific OCAP version trigger action owner 與 execution record。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I17
view: industry
from_id: concept:measurement-system-contract
to_id: process:excursion-containment-event-passport
relation: includes
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C38
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: t0 至 t8 是研究中心查核框架 不是 NIST 台積電與 SEMI 共同標準 也不表示每座廠使用相同 event names 或 sequencing。
next_trigger: 客戶版本文件公開 signal validation command enforcement genealogy disposition correction verification release 的原始事件 schema。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I18
view: industry
from_id: concept:measurement-system-contract
to_id: metric:signal-validation-actuation-latency
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C38
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: signal to hold 只是 t6 減 t3 不涵蓋取樣前歷史 excursion onset 佇列 後站材料或修正後放行 不能改寫成完整 exposure 或 cycle time。
next_trigger: 同一量產產品公開 t2 至 t6 timestamp distribution queue review decision acknowledgement 與 affected-object count。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I19
view: industry
from_id: concept:measurement-system-contract
to_id: capability:manufacturing-genealogy
relation: requires
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C36,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C37,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C38
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: 台積電公開 per-die product resume 用途 SEMI 公開跨製造測試組裝 unique identification 方向 但兩者不是同一客戶實作或共同 event schema。
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: Unique ID 與 traceability 不自動證明根因 受影響範圍完整 圍堵成功 良率改善或工具收入。
next_trigger: 同一 production cohort 公開 object IDs route tool chamber recipe material time window candidate scope confirmed failures disposition 與 release。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I20
view: industry
from_id: concept:measurement-system-contract
to_id: process:defect-threshold-cost-passport
relation: includes
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C39,MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C40
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: limited_source
exclusivity_scope: NIST 的 wafer defect 與 misclassification 研究同屬一條中立方法鏈 本圖只據此建立可稽核欄位 不把 surrogate datasets 當成客戶量產結果。
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: 成本護照是研究中心比較契約 不是 NIST 共同標準 半導體客戶 recipe 固定門檻 錯判成本 工具需求或財務模型。
next_trigger: 同一 production product layer 公開 base rate truth method TP FP FN TN threshold version review capacity escape consequence cost ratio 與 change control。
-->

<!-- knowledge_edge
edge_id: KG-PCMC-I21
view: industry
from_id: concept:measurement-system-contract
to_id: metric:defect-miss-review-cost-crossover
relation: measured_by
claim_refs: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY#C40
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: 一百萬個假想單位與 90.91 crossover 只示範量綱 沒有量產樣本 sampling SE t 良率 產能 工具數 公司效果或投資結論。
next_trigger: 客戶以同一 truth set 公開至少兩個 threshold 的 confusion matrix review time escape consequence 與完整成本分母 並能重算實際決策交叉點。
-->
