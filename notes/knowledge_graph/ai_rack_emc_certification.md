# AI 機櫃 EMC 驗證知識圖譜

本圖把元件抑制、設備排放／量測程序與完整機櫃實驗室能力分開，再以 TL、AL、量測不確定度、
guard band 與事前判定規則固定邊界結果。公司線只停在具名產品能力；沒有 test plan、
qualification 與財務分母前，不把 EMI 元件、量測能力或系統整合能力畫成 AI 機櫃受惠。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ai-rack-emc-certification
root_node_id: concept:ai-rack-emc-certification
label: AI 機櫃 EMC 驗證
summary: 將局部雜訊抑制 設備合規程序 大型完整配置測試容量與TL AL 不確定度 guard band 判定規則拆成不同責任層，避免用元件規格或pass標籤替代整櫃資格與可重算風險配置。
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

<!-- knowledge_edge
edge_id: KG-EMC-I10
view: industry
from_id: concept:ai-rack-emc-certification
to_id: capability:large-eut-emc-test-site
relation: requires
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C9,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C10
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2023-03-14
review_due: 2026-08-31
status: active
boundary: FCC 的大型設備 alternative 與 NIST 場地等效要求證明尺寸 幾何與場地能力要被記錄；不判定特定 AI rack 適用程序 實驗室家數 時槽或產品 pass。
next_trigger: 具名 operator 或 lab 公布完整 rack 尺寸 測試體積 距離 場地等效與正式結果。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I11
view: industry
from_id: concept:ai-rack-emc-certification
to_id: process:emc-test-report-passport
relation: requires
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C13
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 九欄護照是研究中心整合 FCC 與 NIST 文件的可比性工具 不是官方聯合標準 完整法規報告模板或具名產品合格證。
next_trigger: 具名量產 AI rack 報告逐欄公開配置 方法 場地 結果 scope 與版本變更並可重複核對。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I12
view: industry
from_id: concept:ai-rack-emc-certification
to_id: metric:emc-compliance-margin
relation: measured_by
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C10,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C13
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 裕量只有在方法 偵測器 頻寬 限制與不確定度固定時才可解讀；本文不建立跨方法通用 guard band 或公司排行。
next_trigger: 完整 test report 同時揭露 measured value limit detector bandwidth margin uncertainty 與 decision rule。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I13
view: industry
from_id: concept:ai-rack-emc-certification
to_id: metric:measurement-uncertainty-decision-rule
relation: measured_by
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C10,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C13
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: NIST 支持 method-specific uncertainty budget 與校正證據 本線把它納入護照是研究整合；不替法規 客戶或 lab 指定單一判定規則。
next_trigger: 具名 rack 報告公開 uncertainty budget decision rule 近限制值處置與重複量測分布。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I14
view: industry
from_id: concept:ai-rack-emc-certification
to_id: capability:emc-accreditation-scope-check
relation: requires
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C11,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C12,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C13
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: scope 核對只確認指定地點 方法 產品與活動是否在認可範圍 不能把 NVLAP mark 讀成產品 certification approval endorsement 或大型設備 capacity。
next_trigger: 具名 lab scope 與 AI rack report 對上實際地點 方法 產品類別及 accredited unaccredited data 標示。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I15
view: industry
from_id: concept:ai-rack-emc-certification
to_id: process:emc-boundary-decision-passport
relation: includes
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C15,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C16,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C17
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: limited_source
exclusivity_scope: ILAC 認可指引與 NIST conformity-risk 研究是兩條獨立方法消息鏈 本圖據此整理七欄讀者契約 不是 AI rack 客戶規格 實驗室 SOP 或產品證書。
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: 七欄護照是研究中心把既有九欄報告護照聚焦到邊界決策的工具 不替任何法域 客戶或 lab 指定 guard band 風險門檻或處置。
next_trigger: 同一具名 rack 版本公開方法 TL y U coverage w AL decision category retest redesign schedule 與財務共同鍵。
-->

<!-- knowledge_edge
edge_id: KG-EMC-I16
view: industry
from_id: concept:ai-rack-emc-certification
to_id: metric:emc-guard-band-acceptance-limit
relation: measured_by
claim_refs: MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C15,MI-2026-08-09-AI-RACK-EMC-CERTIFICATION#C17
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-31
status: active
boundary: 40.0 dBµV/m 38.5 dBµV/m U=3.0 dB 與 AL=37.0 都是假想教材 N=4量測值與N=4設定 沒有sampling SE t 頻率偵測器rack實驗室容量公司效果或投資結論。
next_trigger: 具名 test report 與事前合約共同揭露 TL AL w U measured value binary或non-binary處置及重複結果 並能跨版本重算。
-->
