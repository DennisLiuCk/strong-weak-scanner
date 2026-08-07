# AI 機櫃信任根知識圖譜

本圖把「規格定義了什麼」與「誰能替採購方查證」分開。Caliptra、SPDM 與 SPDM Authorization
各自是已發布規格，OCP S.A.F.E. 是稽核制度；三者都不代表任何具體裝置已通過驗證，也不建立
台灣公司的供貨或受惠線。company:5274 的線只表示產品頁具名列出該功能，不含出貨與財務。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ai-rack-trust-root
root_node_id: concept:ai-rack-trust-root
label: AI 機櫃信任根
summary: 從晶片內量測信任根走到元件證明與動作授權，並把可獨立查證的第三方保證層與規格層分開，暴露兩者成熟度不同步的缺口。
article_ids: MI-2026-08-08-AI-RACK-TRUST-ROOT
status: active
-->

<!-- knowledge_edge
edge_id: KG-TRT-C01
view: company
from_id: company:5274
to_id: concept:ai-rack-trust-root
relation: uses_standard
claim_refs: MI-2026-08-08-AI-RACK-TRUST-ROOT#C5
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-08
review_due: 2026-11-14
status: active
boundary: 信驊產品頁具名列出 AST2700 採用 Caliptra SiRoT；不證明出貨量、客戶認證階段、稽核結果、收入或毛利，也不支持份額與競爭優勢推論。
next_trigger: 季報、法說或重大訊息首次分開揭露 AST2700 出貨、客戶認證階段與可辨識收入或毛利。
-->

<!-- knowledge_edge
edge_id: KG-TRT-C02
view: company
from_id: company:insyde
to_id: concept:ai-rack-trust-root
relation: integrates
claim_refs: MI-2026-08-08-AI-RACK-TRUST-ROOT#C6
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-08
review_due: 2026-11-14
status: active
boundary: Insyde 公告把 AST2700 信任根整合進其 OpenBMC 平台並以 Redfish 暴露 SerDes telemetry；該稿明示未主張量產部署、具名客戶或營收。
next_trigger: 出現具名客戶採用、場域部署或可辨識財務貢獻的一手文件。
-->

<!-- knowledge_edge
edge_id: KG-TRT-I01
view: industry
from_id: concept:ai-rack-trust-root
to_id: standard:caliptra
relation: requires
claim_refs: MI-2026-08-08-AI-RACK-TRUST-ROOT#C1,MI-2026-08-08-AI-RACK-TRUST-ROOT#C2
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-08
review_due: 2026-09-30
status: active
boundary: Caliptra 定義 SoC 內 RTM 區塊且範圍刻意最小化，並把 certification 列為 out of scope；不證明任何實作已完成規格以外的保證工作。
next_trigger: 新 revision 改變 RTM 範圍，或出現具名裝置的 Caliptra 實作稽核報告。
-->

<!-- knowledge_edge
edge_id: KG-TRT-I02
view: industry
from_id: concept:ai-rack-trust-root
to_id: standard:spdm
relation: requires
claim_refs: MI-2026-08-08-AI-RACK-TRUST-ROOT#C3,MI-2026-08-08-AI-RACK-TRUST-ROOT#C4
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-08
review_due: 2026-08-31
status: active
boundary: DSP0274 把身分認證、韌體與組態量測及加密工作階段分列為不同章節；章節存在不代表任何實作支援全部章節。
next_trigger: 出現裝置層級的 SPDM 一致性測試結果或營運方公布的驗收準則。
-->

<!-- knowledge_edge
edge_id: KG-TRT-I03
view: industry
from_id: concept:ai-rack-trust-root
to_id: standard:spdm-authorization
relation: requires
claim_refs: MI-2026-08-08-AI-RACK-TRUST-ROOT#C3
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-08
review_due: 2026-08-31
status: active
boundary: DSP0289 已於 2025-12-08 發布為 Standard，證明認證與授權在此體系中是分開的文件；其配套白皮書在本輪仍標示目標 2026Q3，尚未發布。
next_trigger: DSP2071 授權白皮書發布，或出現採用該授權規格的具名實作。
-->

<!-- knowledge_edge
edge_id: KG-TRT-I04
view: industry
from_id: concept:ai-rack-trust-root
to_id: capability:silicon-rtm
relation: requires
claim_refs: MI-2026-08-08-AI-RACK-TRUST-ROOT#C1,MI-2026-08-08-AI-RACK-TRUST-ROOT#C2
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-08
review_due: 2026-09-30
status: active
boundary: 規格定義晶片內身分、measured boot 與量測輸出；不證明任何晶片已啟用該功能或量測值被下游正確使用。
next_trigger: 具名裝置公布 measured boot 流程、量測涵蓋範圍與驗證失敗處置。
-->

<!-- knowledge_edge
edge_id: KG-TRT-I05
view: industry
from_id: concept:ai-rack-trust-root
to_id: capability:device-attestation
relation: requires
claim_refs: MI-2026-08-08-AI-RACK-TRUST-ROOT#C4,MI-2026-08-08-AI-RACK-TRUST-ROOT#C2
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-08
review_due: 2026-08-31
status: active
boundary: 協定定義如何提供憑證與量測報告；簽章只保證來源與內容未被竄改，不保證所載韌體版本本身安全。
next_trigger: 出現可重現的多供應商 attestation 交換測試結果。
-->

<!-- knowledge_edge
edge_id: KG-TRT-I06
view: industry
from_id: concept:ai-rack-trust-root
to_id: capability:action-authorization
relation: requires
claim_refs: MI-2026-08-08-AI-RACK-TRUST-ROOT#C3,MI-2026-08-08-AI-RACK-TRUST-ROOT#C7,MI-2026-08-08-AI-RACK-TRUST-ROOT#C8
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-08
review_due: 2026-08-31
status: active
boundary: 把授權視為信任鏈的必要獨立層是研究判讀；沒有任何文件說明 production 機櫃在 attestation 失敗時的實際授權後果。
next_trigger: 平台或場域文件說明 attestation 結果如何進入隔離請求的裁決邏輯與 fail-safe。
-->

<!-- knowledge_edge
edge_id: KG-TRT-I07
view: industry
from_id: concept:ai-rack-trust-root
to_id: capability:security-conformance-assurance
relation: requires
claim_refs: MI-2026-08-08-AI-RACK-TRUST-ROOT#C7,MI-2026-08-08-AI-RACK-TRUST-ROOT#C1
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-08
review_due: 2026-08-31
status: active
boundary: Caliptra 側有稽核報告與第三方稽核機構制度、SPDM 側一致性測試指引仍為 WIP，是本輪觀察到的狀態；不評價任何產品實際安全性，也不預測標準組織時程。
next_trigger: 一致性測試指引正式發布並出現可查的裝置測試結果，或營運方公布獨立驗收準則。
-->

<!-- knowledge_edge
edge_id: KG-TRT-I08
view: industry
from_id: concept:ai-rack-trust-root
to_id: concept:ai-rack-action-contract
relation: integrated_with
claim_refs: MI-2026-08-08-AI-RACK-TRUST-ROOT#C8
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-08
review_due: 2026-08-31
status: active
boundary: 信任根是動作契約中「請求者身分可信」的上游前提，這是概念層相接；不代表任何平台已把 attestation 結果接進 isolation request 的授權判斷。
next_trigger: 同一平台文件同時公布身分驗證結果與 isolation request 的 accept／reject 依據。
-->

<!-- knowledge_edge
edge_id: KG-TRT-I09
view: industry
from_id: concept:ai-rack-trust-root
to_id: group:ipdesign
relation: routes_to
claim_refs: MI-2026-08-08-AI-RACK-TRUST-ROOT#C10
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-08
review_due: 2026-11-14
status: active
boundary: BMC 與管理 IC 是信任根落地位置，只形成搜尋路由；沒有出貨、客戶認證或財務分母，不建立受惠排行。
next_trigger: 族群內公司首次分開揭露安全功能對應的出貨、認證階段與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-TRT-I10
view: industry
from_id: concept:ai-rack-trust-root
to_id: group:serverodm
relation: routes_to
claim_refs: MI-2026-08-08-AI-RACK-TRUST-ROOT#C10
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-08
review_due: 2026-11-14
status: active
boundary: 系統與機櫃整合商位於平台韌體與客戶驗收條款交界，只形成搜尋路由；沒有具名承擔 attestation 或授權鏈責任的文件與財務分母。
next_trigger: 客戶驗收條款或公司申報首次具名要求 attestation、授權鏈或第三方稽核。
-->
