# AI 機櫃 EMC 驗證知識圖譜

本圖把元件抑制、設備排放／量測程序與完整機櫃實驗室能力分開。公司線只停在具名產品能力；
沒有 test plan、qualification 與財務分母前，不把 EMI 元件或系統整合能力畫成 AI 機櫃受惠。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ai-rack-emc-certification
root_node_id: concept:ai-rack-emc-certification
label: AI 機櫃 EMC 驗證
summary: 將局部雜訊抑制 設備合規程序與大型完整配置的可用測試容量拆成不同責任層，避免用元件規格替代整櫃資格。
article_ids: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION
status: active
-->

<!-- knowledge_edge
edge_id: KG-EMC-C01
view: company
from_id: company:2327
to_id: concept:ai-rack-emc-certification
relation: has_capability
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C4,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C6
note_refs: 2327#S1,2327#S2
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-15
status: active
boundary: 國巨集團產品公告證實具名柔性 EMI 吸波材能力 公司筆記證實被動元件與廣義 AI 應用位置；兩側沒有共同 AI rack part placement qualification 客戶 出貨或財務證據。
next_trigger: 公司或買方雙向揭露具名 EMI part 目標頻帶 rack placement qualification production shipment 及財務分母。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I01
view: industry
from_id: concept:ai-rack-emc-certification
to_id: component:emi-absorber
relation: uses_component
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C4,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C5
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2021-02-26
review_due: 2026-08-31
status: active
boundary: FLEX SUPPRESSOR 證明吸波材是元件級 EMI 抑制的一種；不表示它處理所有傳導與輻射路徑或已用於 AI rack。
next_trigger: 具名 rack test report 公開元件位置 目標頻帶 attenuation 與 system-level 前後差異。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I02
view: industry
from_id: concept:ai-rack-emc-certification
to_id: capability:component-emi-suppression
relation: requires
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C4,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C5
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-31
status: active
boundary: 將局部抑制列為整體責任層是研究推論；元件能力不能替代 equipment configuration 量測或正式 qualification。
next_trigger: Hyperscaler 或 ODM test plan 把元件路徑 pre-scan 與 final configuration 的 pass fail 串接。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I03
view: industry
from_id: concept:ai-rack-emc-certification
to_id: standard:cispr-32
relation: requires
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C2,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C5
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-31
status: active
boundary: CISPR 32 publication scope 可定位 multimedia equipment 排放與量測目標；本線不判定特定 AI rack equipment configuration 電壓邊界或法域適用性。
next_trigger: 正式 test plan 或主管機關意見明確界定解耦式 AI rack 的被測配置與適用條款。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I04
view: industry
from_id: concept:ai-rack-emc-certification
to_id: standard:fcc-part-15-emissions
relation: requires
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C3,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C5
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-31
status: active
boundary: FCC KDB 提供一般 Part 15 measurement 入口與其他方法詢問邊界；不表示所有 AI rack 走同一 authorization procedure。
next_trigger: FCC Laboratory 或具名 test plan 說明大型解耦配置的程序 被測模式與認可範圍。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I05
view: industry
from_id: concept:ai-rack-emc-certification
to_id: capability:full-rack-emc-testing
relation: requires
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C1,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C5
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-31
status: active
boundary: OCP practitioner 指出重型高功率解耦式 rack 的完整配置測試問題；本線不主張每個平台都必須整櫃重驗或既有模組證書無法沿用。
next_trigger: Operator 或認可實驗室公布正式 equipment configuration 模組證書沿用規則與 full-rack pass fail 結果。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I06
view: industry
from_id: concept:ai-rack-emc-certification
to_id: capability:accredited-emc-lab-capacity
relation: requires
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C1,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C3,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C5
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-31
status: active
boundary: 大型完整配置需要匹配空間 承重 供電 冷卻程序與認可 scope；全球家數 可用時槽 lead time 與部署延遲仍未驗證。
next_trigger: 至少兩個獨立 operator 或 lab 公布可測配置 chamber weight power accredited scope 利用率與 lead time。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I07
view: industry
from_id: concept:ai-rack-emc-certification
to_id: group:passive
relation: routes_to
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C6,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-15
status: active
boundary: 被動元件與吸波材只形成 component-level 搜尋路由；不證明 AI rack qualification design win 訂單或財務貢獻。
next_trigger: 買方與公司雙向對齊具名 part placement attenuation qualification shipment 及毛利。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I08
view: industry
from_id: concept:ai-rack-emc-certification
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-31
status: active
boundary: PSU 與高功率供電可能位於 conducted-emission 及被測配置責任鏈 目前沒有具名 universe 公司 test plan qualification 訂單或財務證據。
next_trigger: 平台與電源公司雙向確認具名 PSU 測試責任 configuration qualification shipment 及財務分母。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I09
view: industry
from_id: concept:ai-rack-emc-certification
to_id: group:serverodm
relation: routes_to
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-31
status: active
boundary: ODM 可能負責整櫃 configuration 與重設計只形成搜尋路由；沒有具名 test ownership pass fail deployment 或財務證據。
next_trigger: 客戶與 ODM 雙向公布 test plan configuration ownership qualification retest 部署量及毛利。
-->
