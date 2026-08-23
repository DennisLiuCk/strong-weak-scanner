# AI 硬體 SDC 生命週期責任鏈知識圖譜

本圖把硬體錯誤分類、製造篩檢、整機診斷、機群與應用偵測、裝置隔離、FRU 換件、供應商
RMA 處置及矯正措施分開。公開證據已支持多個單站能力，尚未支持共同誤報漏報、跨框架格式、
同一序號完整閉環或台灣公司收入。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ai-hardware-sdc-lifecycle
root_node_id: concept:ai-hardware-sdc-lifecycle
label: AI 硬體 SDC 生命週期責任鏈
summary: 從 benign corrected DUE 與 SDC 分類追到製造篩檢 系統診斷 機群與應用偵測 零事件暴露與錯判上限 隔離 FRU換件 RMA處置 矯正措施 part history 及共同測試格式 避免把單站 pass fail 當成完整生命週期與公司收入。
article_ids: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE
status: active
-->

<!-- knowledge_edge
edge_id: KG-SDC-C01
view: company
from_id: company:meta
to_id: concept:ai-hardware-sdc-lifecycle
relation: has_capability
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C4
note_refs:
evidence_state: verified
commercial_stage: deployment
materiality: named_product
exclusivity: limited_source
exclusivity_scope: Meta 公開 Fleetscanner Ripple Hardware Sentinel 與自有機群隔離流程；本輪沒有其他 operator 用相同分母的直接比較。
as_of: 2025-07-22
review_due: 2026-08-31
status: active
boundary: Meta 場域方法不建立業界共同 cadence coverage 誤報漏報 quarantine 門檻 或供應商財務價值。
next_trigger: Meta 公開固定版本 hardware pool 分母 confusion matrix isolation outcome 與 factory feedback。
-->

<!-- knowledge_edge
edge_id: KG-SDC-C02
view: company
from_id: company:nvidia
to_id: concept:ai-hardware-sdc-lifecycle
relation: has_capability
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C5
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: limited_source
exclusivity_scope: DCGM 是 NVIDIA GPU 管理與診斷工具；公開頁面沒有跨供應商相同 plugin 與 threshold 的共同結果。
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: DCGM 可測指定運算與 framebuffer data path 但不修復 不取代 offline field diagnostics 不決定 RMA 也不保證長期無 SDC。
next_trigger: NVIDIA 公布 DCGM 對固定 known-good known-bad suspect pool 的 coverage false positive negative FRU 與 RMA handoff。
-->

<!-- knowledge_edge
edge_id: KG-SDC-C03
view: company
from_id: company:google
to_id: concept:ai-hardware-sdc-lifecycle
relation: has_capability
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C6
note_refs:
evidence_state: verified
commercial_stage: deployment
materiality: named_product
exclusivity: limited_source
exclusivity_scope: Google Research 的 Spanner 案例支持應用層 SDC detection prevention 與移除故障機器；不是所有 Google AI 平台或工作負載的共同實作。
as_of: 2022-01-01
review_due: 2026-08-31
status: active
boundary: 應用層發現資料不一致不能單獨定位 CPU GPU 軟體或核心根因 也不替製造與整機測試背書。
next_trigger: Google 公布可重現 workload check device mapping isolation threshold 與 supplier root-cause feedback。
-->

<!-- knowledge_edge
edge_id: KG-SDC-C04
view: company
from_id: company:google
to_id: concept:ai-hardware-sdc-lifecycle
relation: has_capability
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C6
note_refs:
evidence_state: verified
commercial_stage: deployment
materiality: named_product
exclusivity: limited_source
exclusivity_scope: Google Cloud 公開介面可用 SILENT_DATA_CORRUPTION reason 回報 faulty host 並進入停止與修復流程；處置依產品模式且屬 best effort。
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 回報可疑 SDC 不證明硬體根因 FRU 定位 永久修復 供應商 RMA 或跨平台 quarantine threshold。
next_trigger: Google Cloud 公布 fault confirmation host device mapping repair outcome repeat-failure 與 supplier disposition。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I01
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: concept:sdc-outcome-taxonomy
relation: includes
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: OCP v1.1 彙整 NVIDIA Meta Google AMD Intel Arm Microsoft 作者的共同 taxonomy；實作 error code 與 threshold 仍可不同。
as_of: 2025-12-16
review_due: 2026-08-31
status: active
boundary: benign corrected DUE SDC 的定義對齊不代表工具格式 故障嚴重度 隔離或 RMA 已對齊。
next_trigger: 各主要平台公布 taxonomy-to-error-code mapping 與一致測試案例。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I02
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: capability:factory-sdc-screening
relation: requires
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C2,MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C3
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-30
status: active
boundary: 結構 功能與 burn-in 測試可攔截部分 test escapes 但沒有公開 universe tester socket 測項 test-time 或增量 coverage。
next_trigger: 製造與供應商共同公布新增 SDC screen 的 fault model test condition escape reduction 與 production insertion。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I03
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: capability:system-level-sdc-diagnostics
relation: requires
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C3,MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C5
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: OCP 規格支援 CPU GPU accelerator 共通研究範圍且 DCGM 提供一套 GPU 實作；非單一供應商才能完成所有系統診斷。
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 已知答案與 data-path 測試只涵蓋指定 tool version plugin input environment 與時間 不保證全系統生命週期。
next_trigger: 第二套獨立平台用共同 input output schema 重現相同 hardware pool 結果。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I04
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: capability:in-fleet-sdc-detection
relation: requires
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C2,MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C4
note_refs:
evidence_state: verified
commercial_stage: deployment
materiality: adjacent
exclusivity: limited_source
exclusivity_scope: Meta 公開 deployed periodic colocated 與 analytical methods；OCP 白皮書提供跨公司研究背景但沒有共同 field outcome。
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 需要生命週期偵測不等於每個 operator 使用同一方法 cadence coverage 或成本。
next_trigger: 至少兩個 operator 公布相同定義與完整分母的 fleet test outcome。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I05
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: capability:workload-correctness-check
relation: requires
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C6,MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C7
note_refs:
evidence_state: inference
commercial_stage: deployment
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: Google Spanner 與 OCP AI 白皮書分別支持應用層資料完整性及 AI correctness 需要 但 workload-specific 方法不同。
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 應用異常與硬體 SDC 不是一對一 mapping 需要 deterministic replay device identity 與環境排除軟體原因。
next_trigger: 具名 AI workload 公布 deterministic check device attribution false positive negative 與 isolation result。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I06
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: capability:sdc-device-quarantine
relation: requires
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C6,MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C7
note_refs:
evidence_state: inference
commercial_stage: deployment
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: Meta 與 Google 公開來源都包含移出可疑 node host 的實際流程 但沒有相同 threshold 與 disposition。
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: quarantine 是保護正式工作與後續分析的中間狀態 不等於已知根因 永久修復或 RMA acceptance。
next_trigger: 公開 suspect confirmation release repair scrap criteria 與 repeat-failure outcome。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I07
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: process:sdc-part-history-feedback
relation: passes_through
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C3,MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C7,MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C9
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-30
status: active
boundary: OCP 已定義 part history 欄位 但尚未證實 factory SLT fleet supplier FA RMA corrective action 的公開跨公司閉環。
next_trigger: 同一 serial part identity 的全生命週期紀錄與改善前後 coverage 被製造 整機 operator 供應商共同公布。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I08
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: stage:sdc-common-test-format
relation: passes_through
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C8
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: OCP v1.0 明示列出的 DCGM OpenDCDiag OFHC 當時尚未符合共同 input output format 且沒有 cross-framework result。
next_trigger: 兩套以上獨立 framework 公布共同 schema version test pool input output 與一致 verdict。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I09
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: stage:sdc-commercial-attribution
relation: passes_through
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C10
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-30
status: active
boundary: 沒有 universe 公司具名 SDC product qualification contract deployment test denominator revenue 或 margin。
next_trigger: 買方與公司雙向確認具名產品責任 qualification 數量 單價 收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I10
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C10
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-30
status: active
boundary: manufacturing burn-in SLT 與 part history 只形成封測搜尋路由 不證明具名 test item tester socket 時間 coverage qualification 或收入。
next_trigger: 封測方與客戶公布具名 SDC test plan equipment time escape reduction production qualification 與財務分母。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I11
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: group:semiequip
relation: routes_to
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C10
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-30
status: active
boundary: 新 fault model diagnosis 與測試實驗只形成設備搜尋路由 不證明具名 tool bottleneck order shipment revenue 或 margin。
next_trigger: 測試計畫將 fault coverage 與具名設備工時 產能 客戶資格 出貨及財務對齊。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I12
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: group:serverodm
relation: routes_to
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C10
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-30
status: active
boundary: SLT BMC diagnostic integration node isolation repair handoff 只形成 ODM 搜尋路由 不證明平台責任 qualification deployment 或財務貢獻。
next_trigger: ODM 與客戶共同公布具名 platform SDC acceptance BMC mapping quarantine RMA outcome 部署數與財務分母。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I13
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: process:sdc-zero-event-isolation-evidence-passport
relation: measured_by
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C14
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: 十欄護照把 OCP 的 lifecycle test contract 與 NIST 零事件方法對齊成研究工具；不是共同 SDC compliance standard 產品 reliability acceptance RMA 規則或供應鏈訂單。
next_trigger: 至少兩套 framework 對同一具名 hardware pool 公開完整事件 暴露 分層 detector ground truth confusion matrix confidence quarantine RMA 成本及 field outcome。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I14
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: metric:sdc-exposure-confidence-confusion-boundary
relation: measured_by
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C11,MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C12,MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C13,MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C14
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: Binomial 與 HPP confidence bound 只在各自獨立或固定率假設下限制事件機率或速率；混淆矩陣也依 ground-truth pool 組成，不能把零命中 95% 上限或 validation precision 外推產品機群。
next_trigger: 具名產品公開可審計 raw verdict 與 device test time workload denominators 獨立性分層 detector sensitivity confusion matrix及模型適配檢查。
-->

<!-- knowledge_edge
edge_id: KG-SDC-I15
view: industry
from_id: concept:ai-hardware-sdc-lifecycle
to_id: process:sdc-five-decision-service-ledger
relation: includes
claim_refs: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C15,MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE#C16
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: NVIDIA Google Cloud 與 OCP 分別公開工具 operator 與 RAS／service 邊界；五本帳是本文跨來源整理，不是三方共同流程。
as_of: 2026-08-24
review_due: 2026-08-31
status: active
boundary: 診斷隔離換件RMA與矯正措施可跳站但不可互相替代；本輪三份文件的same-serial五章閉環復發共同觀測為N=0，也沒有universe公司合約與財務證據。
next_trigger: 同一incident host device FRU serial公開完整診斷隔離放行換件前後測RMA disposition根因措施生效日及改善前後recurrence denominator。
-->
