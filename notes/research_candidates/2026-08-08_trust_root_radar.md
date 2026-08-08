# 2026-08-08 AI 機櫃信任根與保證層研究雷達

本輪四個候選皆為全新研究問題，未出現於任何前輪雷達，因此不需 early trigger。排名在深研前
凍結於 RS-2026-08-08-01；升格只代表 article＋graph 的證據契約通過，不代表任何產品安全性、
production 部署、台灣供應商受惠或投資建議。

<!-- research_radar
schema_version: 2
radar_id: RADAR-2026-08-08-01
as_of: 2026-08-08
next_review: 2026-08-15
status: retired
method: 先執行前一輪承諾的官方事件端點重查並如實記錄仍為 partial，再回查三個到期 monitor；由回查結果與既有圖譜缺口找出「上一輪動作契約未處理的身分前提」這個明確空白，按可證偽性、至少兩條獨立一手來源鏈、universe 個股是否有直接對應、以及能否把規格層與保證層分開檢驗來排序。候選先寫入 append-only selection log 並獨立 commit；深研後只更新 evidence posture、route 與結果，不改凍結排名、第一拒絕與下一份證據
selection_cycle_id: RS-2026-08-08-01
-->

<!-- research_candidate
candidate_id: RC-AI-RACK-TRUST-ROOT
rank: 1
title: AI 機櫃信任根、attestation 與動作授權責任鏈
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: 上一輪 MI-2026-08-07-AI-RACK-ACTION-CONTRACT 已把 rack identity→telemetry→request owner→guardrail→isolation state 串成動作契約，但整條鏈最上游「identity 與 request 授權憑什麼可信」仍是空白。OCP Caliptra 定義 SoC 內 RTM、DICE identity 與 signed attestation；DMTF DSP0274 SPDM 另由不同標準組織定義跨元件 authentication、firmware measurement 與 session；ASPEED AST2700 產品文件已明示採用 Caliptra 作為 silicon RoT，把這條標準鏈直接接到 universe 個股 5274
knowledge_gain: 把「有沒有安全功能」改寫成 silicon RTM→device attestation→action authorization→third-party assurance 的可反證階梯，並把規格層與可獨立查證的保證層分開，使「支援某標準」不再等同「已被驗證」
first_rejection: 若 Caliptra 與 SPDM 無法對齊成同一條可驗證的 identity→measurement→attestation→authorization 鏈，或找不到 BMC／機櫃層一手文件說明 attestation 結果如何實際改變授權與 fail-safe 行為，就只是兩份互不相干的規格，不建立信任根責任階梯，也不做任何台廠受惠或份額映射。
next_evidence: 逐節對齊 Caliptra 的 RTM／DICE／measurement 邊界、SPDM DSP0274 的 measurement 與 authentication 訊息、AST2700 的 vendor／owner 信任鏈欄位；再找 OCP 或平台商機櫃層文件說明 attestation 失敗時的授權後果與 safe default；另查是否有可辨識的量產、客戶認證或財務足跡。
next_check: 2026-08-31
route: article_and_graph
article_topic_id: MI-2026-08-08-AI-RACK-TRUST-ROOT
graph_id: ai-rack-trust-root
sources: OCP Caliptra R1 => https://www.opencompute.org/products/575/caliptra | Caliptra specification => https://chipsalliance.github.io/Caliptra/doc/Caliptra.html | DMTF SPDM standards => https://www.dmtf.org/standards/spdm | DSP0274 SPDM Specification 1.4.0 => https://www.dmtf.org/sites/default/files/standards/documents/DSP0274_1.4.0.pdf | ASPEED AST2700 => https://www.aspeedtech.com/server_ast2700/
-->

<!-- research_candidate
candidate_id: RC-AI-BBU-SAFETY-CERTIFICATION
rank: 2
title: AI 機櫃 BBU 的安全認證、熱失控測試與運輸法規責任鏈
priority: p1
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: OCP ORV3 已把 BBU 定義成機櫃內建備援模組，UL 1973 與 UL 9540A 又分別規範靜置電池組保護與熱失控傳播測試；但目前尚未取得把 cell→module→BBU→rack→installation 各層測試責任、運輸法規與現場驗收串起來的同一條文件鏈
knowledge_gain: 若能補齊，可把既有 AI 電力緩衝研究從電性規格推進到安全認證與責任分層；現階段保留 watch，避免把「有認證」換算成供應商份額
first_rejection: 若無法由一手標準與 OCP 規格分辨 cell、module、BBU、rack 與 installation 各層的測試對象、通過準則與責任方，或只剩電池廠行銷型認證宣稱，就不建立安全認證階梯，也不把「有認證」換算成供應商份額或價值量。
next_evidence: 取得 OCP ORV3 BBU 規格、UL 1973 與 UL 9540A 正式範圍說明及運輸法規（UN 38.3）條文，逐層對齊測試對象、通過準則、責任方與現場驗收；再查台灣電池模組與電源公司是否有可定位的認證與量產文件。
next_check: 2026-09-15
route: watch_only
sources: OCP ORV3 BBU 相關規格 => https://www.opencompute.org/projects/rack-and-power | UL 1973 標準說明 => https://www.ul.com/services/ul-1973-certification | UL 9540A 測試方法 => https://www.ul.com/services/ul-9540a-test-method
-->

<!-- research_candidate
candidate_id: RC-DC-COOLANT-CHEMISTRY
rank: 3
title: 液冷工作流體化學、水質等級與材料相容性
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: 既有液冷研究處理的是迴路界面與資格認證，工作流體本身仍是黑箱。ASHRAE 的 W1–W4 水質等級、CDU 對 FWS／TCS 的分界，以及導電度、pH、抑制劑與 ASTM D1121／ISO 21058 驗證要求，指向一條與機械設計正交的化學與材料相容性責任鏈
knowledge_gain: 若通過，可補既有 liquid cooling loop boundary 研究缺少的流體側失效模式與維護責任；現在不把水質等級換算成任何材料或散熱公司的受惠
first_rejection: 若一手文件無法把水質等級、導電度與 pH 門檻、抑制劑配方驗證、材料相容性與維護週期分開，或只能取得冷卻液供應商的行銷規格，就不建立流體化學責任鏈，也不推論任何散熱或材料公司的受惠。
next_evidence: 取得 ASHRAE 液冷指引與 OCP 冷板／CDU 一手文件，對齊 W1–W4 定義、導電度與 pH 門檻、抑制劑驗證方法（ASTM D1121、ISO 21058）、材料相容性測試與維護間隔；再查是否有可定位的失效案例與驗收條款。
next_check: 2026-09-15
route: watch_only
sources: ASHRAE TC 9.9 資料中心技術委員會 => https://tpc.ashrae.org/?cmtKey=fd4a4ee6-96a3-4f61-8b85-43418dfa988d | OCP Cold Plate Development and Qualification => https://www.opencompute.org/documents/ocp-cold-plate-development-and-qualification-with-integrated-comments-pdf
-->

<!-- research_candidate
candidate_id: RC-AI-MANAGEABILITY-CONFORMANCE
rank: 4
title: Redfish interoperability profile 與一致性驗收
priority: p2
knowledge_value: medium
status: watch
evidence_posture: preliminary
why_now: DMTF 已同時發布 Redfish 一致性與測試工具白皮書（DSP2068）、Conformance Test Suite 指引（DSP-IS0018）與可執行的 Redfish-Interop-Validator；這使「宣稱支援 Redfish」與「通過某個 interoperability profile」第一次可以被分開檢驗，但尚未確認 AI 機櫃實際採用哪些 profile 與由誰驗收
knowledge_gain: 若通過，可把上一輪動作契約中 OpenRMC／Redfish 那一層從「標準存在」推進到「可驗收」；本輪信任根研究已顯示 SPDM 側一致性指引仍為 WIP，Redfish 側是否較成熟本身就是可對照的問題
first_rejection: 若找不到 AI 機櫃或伺服器平台實際指定的 interoperability profile 與驗收方，或 conformance 結果無法與前一輪 action contract 的 request／isolation 語意對應，就只是通用管理介面測試工具，不建立互通性驗收階梯。
next_evidence: 取得 DSP2068、DSP-IS0018 與 Redfish Interoperability Profile 正式定義，確認 profile 的必要屬性與判定方式；再找 OCP 或平台商是否對 AI 機櫃指定 profile、由誰執行驗收，以及與 OpenRMC／DSX 動作契約的對應關係。
next_check: 2026-09-15
route: watch_only
sources: Redfish Conformance and Test Tools White Paper DSP2068 => https://www.dmtf.org/sites/default/files/standards/documents/DSP2068_1.0.0_0.pdf | Redfish Conformance Test Suite Guidance DSP-IS0018 => https://www.dmtf.org/sites/default/files/standards/documents/DSP-IS0018_1.0.0.pdf | Redfish Interop Validator => https://github.com/DMTF/Redfish-Interop-Validator
-->

## 本輪方法結果

- 研究前凍結四題；只有第一名通過 research-grade article＋graph，第二至第四名維持 watch，沒有為了固定產出數量而升格。
- 四題皆為新問題，沒有任何一題是未到期重選，因此本輪不需 early trigger；上一輪四個 watch 候選仍依其原 next_check 保留在退役雷達上，不因換輪而被重排或提前消耗。
- 升格的是規格層與保證層的分離判讀；production 授權行為、第三方稽核覆蓋範圍與台灣公司財務足跡仍是 active unverified claims。
- 本輪由執行過程發現兩項方法缺陷（事件端點批次不保留導致 coverage 規則可誤標 full；新鮮度時鐘可被新找到的舊文件刷新），已在研究後回顧一併修正。
