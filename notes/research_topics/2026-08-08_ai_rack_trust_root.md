# AI 機櫃如何判斷控制指令可信：確認身分、版本與權限，還要有人查證

<!-- research_topic
topic_id: MI-2026-08-08-AI-RACK-TRUST-ROOT
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-08
source_published_at: 2026-08-04
last_reviewed_at: 2026-08-08
review_due: 2026-08-31
source_type: mixed
publisher: Insyde Software
publisher_domain: insyde.com
canonical_url: https://www.insyde.com/news/press-releases/insyde-software-presents-advances-in-ai-rack-telemetry-and-security-in-openbmc-at-2026-ocp-apac-summit/
source_chain_id: ai-rack-trust-root-primary-scan-20260808
stock_ids: 5274
group_ids: ipdesign,serverodm
trigger_type: security_trust_chain_maturity
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C7
base_confidence: medium
confidence_basis: 規格層由 OCP Caliptra 與 DMTF SPDM 兩條獨立標準鏈各自公開可定位文件，保證層的不對稱也直接來自兩邊自己的公開狀態標示；但本輪只核對規格與索引頁的版本、範圍與狀態，沒有任何實作稽核結果、場域證據或台灣公司財務足跡
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-08
from: initial
to: inbox
reason: captured_silicon_rot_to_rack_authorization_chain
evidence: source_chain:ai-rack-trust-root-primary-scan-20260808
-->
<!-- transition
date: 2026-08-08
from: inbox
to: triaged
reason: separated_specification_layer_from_independently_verifiable_assurance_layer
evidence: sources:S1,S2,S3,S5,S6
-->
<!-- transition
date: 2026-08-08
from: triaged
to: triaged
reason: editorial_rewrite_for_readability_no_conclusion_change
evidence: editorial:readability
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave86_instruction_trust_four_checks_no_conclusion_change
evidence: editorial:plain_language_wave86_instruction_trust_four_checks
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: expanded_attestation_evidence_policy_decision_and_recovery_contract
evidence: sources:S8,S9,S10,S11
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_attestation_token_age_nonce_consumption_and_authorization_boundary_without_thesis_or_clock_refresh
evidence: sources:S8,S9,S12
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **信任根（Root of Trust）**：設備裡最先被信任的一小段硬體或程式，負責檢查下一段程式再把信任往外延伸；它不能替整套機櫃保證安全。
- **Caliptra**：一份開放規格，規定晶片內要有一小塊「保鑣電路」，開機時逐段檢查接下來要執行的程式。它不是某一家公司的產品，也不替任何產品出具合格證明。
- **韌體**：控制晶片或設備底層功能的程式。它通常比作業系統更早啟動，因此若被掉包，後面的安全檢查可能從錯誤起點開始。
- **量測（measurement）**：把韌體或設定算成固定長度的數位指紋並記錄下來，用來比較現在執行的內容是否符合預期。
- **數位指紋／雜湊值**：由一段資料算出的短值；內容只要改動，結果通常就會不同。它能協助比對版本，但不會自行判斷該版本是否安全。
- **數位簽章**：用私密金鑰替資料加上可驗證標記，讓接收者確認資料來自誰、途中有沒有被改動；簽章正確不等於資料內容本身正確。
- **遠端證明（attestation）**：設備把量測結果與簽章交給外部系統查驗，回答「我是誰、現在跑的是哪一版」；它不會自動決定接下來能做什麼。
- **SPDM**：零件之間互相確認身分、交換版本量測與建立安全連線的公開對話規則；另有獨立授權規格處理確認身分後可以執行哪些動作。
- **身分憑證**：把裝置名稱與公鑰等資訊綁在一起的電子證件；驗證成功只表示身分鏈成立，不代表裝置一定沒有漏洞。
- **授權（authorization）**：確認身分後，再判斷該裝置或程式可不可以執行某個動作，例如切斷電源或關閉冷卻液。
- **公開規格**：由標準組織發布的共同要求與對話方法；規格寫好表示有一套可遵循的方法，不表示任一廠商已正確實作。
- **實作**：廠商把規格真正做進晶片、韌體或系統後的行為；它需要測試或稽核，不能只靠產品頁上的「支援」二字判定。
- **一致性測試（conformance test）**：用共同測試題目檢查產品是否照規格回應；通過的範圍仍要看版本、測試項目與被測配置。
- **第三方稽核**：由賣方與買方以外的合格機構檢查實作與證據，讓買方不必只相信廠商自述。
- **OCP S.A.F.E.**：OCP 推動的安全稽核制度，由核可機構檢查裝置硬體與韌體並出具報告；制度存在不等於每一款產品都已送審或通過。
- **草稿／WIP**：尚未正式定稿的工作版本，英文為 work in progress；它可能繼續修改，不能當成正式測試結果。
- **OCP**：開放運算計畫，由雲端業者與硬體商共同制定資料中心硬體規格與驗證制度的組織。
- **DMTF**：制定資料中心管理與裝置互通標準的組織；本文使用它發布的 SPDM 與授權規格。
- **DSP0274／DSP-IS0023**：DMTF 的文件編號；前者是已正式發布的 SPDM 對話規格，後者是仍在草稿階段的共同測試指引。
- **DPE**：Caliptra 裡用來保存量測身分並替外部查驗資料簽章的介面；本文只用它說明兩份規格如何銜接，不代表已有實際部署。
- **Security Review Provider**：OCP 核可、可依 S.A.F.E. 制度執行第三方安全稽核的機構；列入名單不等於它已檢查本文提到的產品。
- **Redfish**：DMTF 制定的設備管理介面，讓管理系統以共同格式讀取狀態或下指令；展示支援不等於已完成客戶部署。
- **BMC**：伺服器裡獨立於主系統的管理晶片。主機關機或當掉時它仍可監控與下指令，所以它自己的身分與程式版本特別重要。
- **AST2700**：信驊（5274）的第八代 BMC 晶片；產品頁載明內建 Caliptra 相關功能，但沒有提供出貨、客戶驗證或財務貢獻。
- **SiRoT**：信驊產品頁對晶片內安全信任根的稱呼；列出這項功能只證明產品規格宣稱，不等於已完成第三方查證。
- **SoC（系統單晶片）**：把運算、控制、記憶體介面等功能整合在同一顆晶片上的設計；Caliptra 規格描述的是其中一小塊安全功能。
- **ROM（唯讀記憶體）**：開機最早執行、通常不容易被改寫的程式儲存區；它可作為信任鏈的起點，但仍只負責自身規定的範圍。
- **正式環境（production）**：產品已在真實營運場域持續使用的狀態，不是展示、樣品或實驗室測試。
- **失敗時的預設動作（safe default）**：驗證失敗時系統預先選定的安全反應，例如拒絕指令、限制功能或等待人工處理；本文尚未取得機櫃場域的具體規則。
- **可獨立查證／保證層**：買方不依賴賣方自述，也能用測試、稽核或驗收證據確認實作符合規格的能力。
- **證據（Evidence）**：裝置交給外部查驗的身分、量測、設定或狀態資料；有簽章只能協助確認來源與完整性，不能自己決定是否合格。
- **證明者（Attester）**：產生證據、希望被信任的裝置或元件，例如 BMC、加速器或其他管理端點。
- **驗證者（Verifier）**：依參考值與評估規則檢查證據，再產生證明結果的角色；它可以和最後下決策的系統分開。
- **依賴方（Relying Party）**：真正依證明結果決定要不要授權、隔離或提供資源的系統；它不是被證明的裝置。
- **參考值（Reference Value）**：用來和實際量測比較的預期值；它可能是版本、允許集合或範圍，不一定只是單一「黃金雜湊值」。
- **評估政策（Appraisal Policy）**：規定哪些證據、參考值與條件算合格的規則；同一份證據套用不同政策，可能得到不同結果。
- **證明結果（Attestation Result）**：驗證者完成判讀後交給依賴方的結果；它可以是通過／不通過，也可以保留更多狀態資訊。
- **新鮮度（freshness）**：確認這份證據反映的是現在，而不是攻擊者重播的舊合格報告。常見方法包含由外部產生的一次性隨機值。
- **重播攻擊（replay attack）**：把以前合法取得的證據或結果重新送出，假裝裝置目前仍是同一狀態。
- **RIM（Reference Integrity Manifest）**：由製造商、整合商或維護者簽署的參考值資料包，讓驗證者知道某個版本與配置預期量到什麼。
- **RFC**：IETF 正式發布並編號保存的技術文件；不同 RFC 可能是標準、最佳實務或資訊性架構，必須看文件狀態，不能一概當成強制認證。
- **IETF**：制定網際網路協定與共同技術文件的開放標準組織；本文使用它的遠端證明架構與 token 規格。
- **EAT（Entity Attestation Token）**：用 CWT 或 JWT 承載遠端證明 claim 的格式；token 能被驗簽，不代表驗證者已執行買方期待的全部檢查。
- **`iat`（Issued At）**：token 建立、claim 被收集並組合簽署的時間；它可用來計算 token 年齡，但被快取的個別 claim 可能比 `iat` 更早。
- **`exp`（Expiration Time）**：JWT 在此時間點起不應再被接受處理的上限；它不是「內容一定夠新」的保證，也不是所有 EAT 都必須帶的欄位。
- **時鐘偏差／寬限（clock skew／leeway）**：不同系統時鐘不完全一致時，驗證端事先允許的小幅時間差；寬限值是實作或政策選擇，不是 RFC 統一指定的秒數。
- **Nonce 消耗帳／重播快取**：記錄哪個挑戰值由誰發出、綁定哪次請求、是否已被使用或失效；只比對 nonce 相同而不記錄狀態，仍可能接受第二次重播。
- **N-42（本文示例 nonce 代稱）**：下方案例為方便閱讀使用的短標籤；它不是實際挑戰值，案例假設底層 nonce 已符合 EAT 至少 64 bits entropy 的要求。
- **Token 處理窗口／本地新鮮度上限**：`exp` 管 token 最晚何時可被處理，本地 max-age 管驗證者願意接受多老的證據；前者通過不代表後者一定通過。
- **TCG**：制定可信運算規格的產業組織；本文使用它的 RIM 資訊模型說明參考值如何隨平台版本與維護變更。

### 三句話抓重點

- 一條會切斷整櫃水電的指令，不能只看誰送出；系統還要確認送出者真實身分、目前執行的程式版本，以及它是否有權做這件事。
- 前三件事都有公開規格，但規格寫好不等於產品真的照做；買方還需要第四關，由共同測試或第三方稽核來查證實作。
- 晶片側已有第三方稽核制度，零件互驗的共同測試指引卻仍停在草稿；因此產品頁寫「支援 Caliptra／SPDM」，目前不能直接讀成已通過獨立查證，更不能讀成 5274 信驊已有相關訂單或收入。

### 為什麼重要

**先從斷電場景開始。** 資料中心裡有一櫃 AI 伺服器過熱，管理系統送出指令：關掉這一櫃的冷卻液、切掉電源，讓維修員進去換零件。這道指令會讓昂貴設備停機，系統必須先確認送出者真的有權這樣做。

**身分錯了，後面的紀錄都沒有意義。** 上一篇把機櫃控制拆成「誰發請求、誰做裁決、結果怎麼回報」，但它預設請求者身分是真的。如果身分可以偽造，安全護欄與稽核紀錄只會忠實記下一個假名做過什麼。

**規格與查證要分開看。** 產業新聞常寫某晶片「支援 Caliptra」、某平台「採用 SPDM」，這只說明它宣稱遵循某種方法。安全要變成買方可接受的能力，還要看買方能否不靠賣方自述，獨立確認實作真的符合規格。

**最後才連到公司。** 公司新聞至少要再補上具名產品、第三方報告或買方驗收、量產出貨與財務分母，才能從功能宣稱走向商業貢獻。少任何一層，就先停在查核入口。

### 接下來怎麼追

- 先看零件互驗的共同測試指引（DSP-IS0023）是否由草稿轉成正式版本，以及授權白皮書是否如期發布；這會直接改變「規格比查證制度成熟」的判斷。
- 再看 OCP 是否公布新的 S.A.F.E. 稽核報告或新增稽核機構，稽核範圍有沒有從單一晶片延伸到 BMC 或完整機櫃。
- 若平台開始談遠端證明，要求它同時公開證據涵蓋範圍、新鮮度、參考值版本、驗證政策、結果效期、授權後果與失敗復原，不接受只有一張「簽章成功」截圖。
- 最後看 5274 信驊是否首次在季報、法說或重大訊息中，揭露 AST2700 的客戶驗證階段、量產出貨與可辨識收入或毛利。

### 想一想

- 如果身分或程式版本驗證失敗，系統會拒絕斷電指令、進入安全狀態，還是只留下紀錄？公開資料目前說清楚了嗎？
- 同一份量測若昨天通過、今天才被重播，驗證者如何知道設備中間已經更新或被改動？
- 一份第三方報告要寫到哪些被測功能與版本，才足以讓買方少做一次重複測試，而不只是讓賣方多一個標章？
- 共同測試指引停在草稿，可能代表制度尚未成熟，也可能已有其他驗收方式；還要找什麼證據才能分辨？

## 主張與證據帳本

`證實` 只代表指定來源直接支持下列精確措辭，不代表規格描述的機制已在任何產品中實作、啟用或通過稽核。

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: OCP 的 Caliptra R1 登錄頁把 Caliptra 描述為在 SoC 內實作 Root of Trust for Measurement 區塊的規格、矽邏輯、ROM 與韌體，並標示其目標為資料中心級 CPU、GPU、DPU、TPU，同頁另列出 OCP SAFE Security Conformance Report 與 OCP Security Review Provider 兩個項目
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-08-08
basis: S1 於 2026-08-08 觀察到的說明段落與兩個稽核相關標示直接支持這句描述
boundary: 登錄頁描述規格與稽核制度的存在，不證明任何具體晶片已實作 Caliptra、已送稽核或稽核已通過
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: Caliptra 規格文件把自身範圍明示為刻意最小化，並將 foundry IP 整合、實體設計對策、類比 IP、製造後測試與初始化以及 certification 列為 out of scope；同一文件另說明其 DICE Protection Environment 可作為 SoC 內 SPDM responder 的 signing oracle
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-08-08
basis: S2 於 2026-08-08 觀察到的 scope 與 out-of-scope 清單，以及 DPE 與 SPDM responder 關係的敘述
boundary: out-of-scope 清單描述的是規格分工，不代表這些工作不必做，也不代表任何實作已完成它們；DPE 可作為 signing oracle 是規格所述的可能用法，不是已驗證的部署方式
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: DMTF 的 SPDM 標準頁在 2026-08-08 顯示 DSP0274 已發布至 1.4.1（02 Jul 2026）、另有獨立的 DSP0289 SPDM Authorization Specification 1.0.0 已於 08 Dec 2025 發布為 Standard，而 DSP-IS0023 SPDM Conformance Test Suite Guidance 仍列在 Work in Progress 區、版本標示 1.0.0WIP50、日期為 11 Jul 2022
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-08-08
basis: S3 於 2026-08-08 觀察到的規格清單、狀態欄與日期欄直接列出這三份文件的版本與狀態
boundary: 標準索引頁會持續變動，本 claim 只描述當日所見狀態；規格已發布不代表任何裝置已實作，指引仍為 WIP 也不代表 DMTF 沒有其他驗證途徑
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C4
label: verified
status: active
claim: DSP0274 SPDM Specification 1.4.0 正式文件封面標示 Document Identifier DSP0274、Date 2025-05-15、Document Status Published、Supersedes 1.3.0，其目錄把 identity authentication（含 device、alias 與 generic certificate models）、firmware and configuration measurement 與 secure sessions 分列為不同章節
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-08-08
basis: S4 文件封面與目錄層級可直接讀出上述識別碼、日期、狀態與章節結構
boundary: 本輪只核對封面與目錄層級，未逐節重算訊息欄位或密碼學細節；章節存在不代表任何實作支援全部章節
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: verified
status: active
claim: ASPEED 的 AST2700 產品頁說明該晶片採用 OCP 定義的 Caliptra silicon RoT IP 以確保關鍵操作的完整性與機密性，並在規格列出 Secure boot engine by Caliptra (SiRoT)，同頁另標示 12 奈米製程、四核 ARM Cortex-A35 與兩顆獨立 ARM Cortex-M4
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-08-08
basis: S5 於 2026-08-08 觀察到的 Caliptra 敘述句與規格列項目
boundary: 產品頁規格不證明量產出貨、客戶採用、已通過 OCP S.A.F.E. 稽核，也不支持任何營收、毛利或市占推論
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: Insyde Software 於 2026-08-04 發布的新聞稿說明其 Supervyse OPF OpenBMC 平台整合 ASPEED AST2700 的 silicon-native Root of Trust，內容包含 DICE identity、PUF-based key storage 與 post-quantum crypto readiness，並另以 DMTF Redfish API 暴露 per-lane eye height、BER、link state、error counters 與 LTSSM logs 等 SerDes 層 telemetry；該新聞稿未主張任何量產部署、具名客戶或營收
supporting_source_ids: S6
contrary_source_ids:
as_of: 2026-08-04
basis: S6 直接描述整合內容與 Redfish 暴露的欄位，且全文為峰會議程與展示預告，未出現部署、客戶或財務主張
boundary: 韌體供應商的整合公告是能力展示，不是客戶認證、量產部署或財務證據；Redfish 暴露 telemetry 欄位也不等於已完成授權鏈
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: inference
status: active
claim: 從晶片內量測型信任根到機櫃層動作授權，規格面已由兩個獨立標準組織各自補齊，但讓營運方獨立驗證某個實作真的滿足這條鏈的保證層成熟度並不一致；因此現階段「支援 Caliptra／SPDM」只能讀成宣稱具備該機制，不能讀成授權鏈已被第三方驗證
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-08-08
basis: S1 顯示 Caliptra 這側同時存在稽核報告與第三方 Security Review Provider 制度；S3 顯示 SPDM 這側授權規格已發布為 Standard、但一致性測試指引仍為 WIP 且日期停在 2022；S2 顯示 Caliptra 自己把 certification 列為 out of scope，代表保證責任本來就落在規格之外的制度層。三者共同支持「規格層與保證層成熟度不同步」這項判讀
boundary: 這是對公開規格與稽核制度成熟度的研究判讀，不評價任何產品的實際安全性、不預測標準組織時程，也不推導任何公司的競爭力或訂單
verification_needed: 具名裝置的 S.A.F.E. 稽核報告涵蓋範圍、SPDM 一致性測試結果，或營運方公布的驗收準則
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: inference
status: active
claim: 本篇的信任鏈是 MI-2026-08-07-AI-RACK-ACTION-CONTRACT 動作契約的上游前提：該契約要求分辨請求發布者與最終裁決者，而分辨的前提是身分可被驗證；Caliptra 把 DPE 定位為 SPDM responder 的 signing oracle，正是把晶片內身分接到跨元件協定的接點
supporting_source_ids: S2,S3
contrary_source_ids:
as_of: 2026-08-08
basis: S2 說明晶片內身分如何向外提供簽章能力，S3 說明跨元件的認證、量測與授權由哪些已發布規格承擔；兩者相接即構成動作契約所需的身分前提
boundary: 兩篇研究在概念層相接，不代表任何平台已把 attestation 結果實際用於隔離請求的授權決策，也不代表 DSX 與 SPDM 已完成對應
verification_needed: 平台文件說明 attestation 結果如何進入 request 授權判斷
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: unverified
status: active
claim: AI 機櫃在 production 環境中已把 attestation 驗證失敗作為拒絕隔離請求或進入 safe default 的實際依據
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-08
basis: 現有來源只描述量測、證明與授權的規格能力，沒有任何文件說明驗證失敗時的實際授權後果
boundary: 不得由規格具備該能力推導場域已如此實作；也不得把「沒有找到文件」當成該行為不存在的反證
verification_needed: 平台或場域一手文件說明 attestation 失敗時的具體授權後果、fail-safe 行為、時間與稽核紀錄
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: unverified
status: active
claim: 5274 信驊因 AST2700 的 Caliptra SiRoT 取得可辨識的訂單、量產出貨或毛利貢獻
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-08
basis: 目前只有產品頁規格與一家韌體供應商的整合展示公告，沒有出貨量、客戶認證階段或財務分拆
boundary: 不得由產品頁列出安全功能推導訂單、市占或毛利改善，也不得把生態系整合公告當成客戶採用
verification_needed: 信驊季報、法說或重大訊息揭露 AST2700 出貨量、客戶認證階段與可辨識收入或毛利，或客戶端具名採用文件
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: IETF RFC 9334 把遠端證明分成證明者產生 Evidence、驗證者依 Endorsements／Reference Values／Appraisal Policy 評估後產生 Attestation Result，以及依賴方再依自己的 policy 決定是否允許存取或操作；同一架構另把證據未通過、結果未通過及驗證者不可用列為三種不同失敗位置
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-08-12
basis: S8 §§4–5 與 §§8.1–8.5 直接定義三個角色及四類概念訊息，§5.1 明列 Passport Model 的三種失敗，§10 另處理 Evidence 與 Attestation Result 的新鮮度
boundary: RFC 9334 是資訊性架構與共同名詞，不指定 AI 機櫃協定、評估門檻、依賴方動作、實作品質或買方驗收，也不證明 Caliptra／SPDM 已依這套角色完整整合
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: IETF RFC 9711 的 EAT 規格可用 COSE／JOSE 提供 token 的真實性與完整性，並定義 nonce claim 供重播防護與新鮮度；但規格明示不替驗證者制定統一處理規則，依賴方必須理解各驗證者實際執行了哪些 policy 與檢查，且訊息格式本身不規定實作安全等級
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-08-12
basis: S9 §§1.3.1、8.4 與 9.1 分別說明 Evidence 到 Attestation Result 的 policy 邊界、nonce 的 replay／freshness 用途，以及 claim 格式不保證實作安全等級
boundary: EAT 是可承載 Evidence 或 Attestation Result 的 token 規格，不代表任一 BMC、SPDM endpoint 或 AI rack 已採用 EAT；nonce 存在也不證明產生方式、綁定、效期與重播防護已正確實作
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: verified
status: active
claim: TCG RIM Information Model 1.1 把供驗證者比較 Evidence 的參考值做成可簽署、可識別建立者與版本的 RIM bundle；製造商、系統整合商與維護者若改變韌體、設定或硬體，可以追加並串接新的 bundle，使驗證者取得反映平台生產與維護歷程的 reference-value collection
supporting_source_ids: S10
contrary_source_ids:
as_of: 2026-08-12
basis: S10 pp.9、13–16 與 25–28 直接定義 RIM、Creator、簽章與 critical firmware／event／configuration hash，並說明 pre-delivery modification、maintenance update、patch／upgrade 如何建立 supplemental 或新 RIM 及 backward linkage
boundary: RIM 是通用參考完整性資訊模型，不保證每個供應鏈角色都會及時產生正確 bundle，也不證明 AI rack 的多元件 reference values 已完整聚合、可取得或被客戶採用
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: verified
status: active
claim: NIST SP 800-193 把平台韌體韌性拆成保護未授權變更、偵測偏離授權狀態，以及把韌體程式與關鍵資料安全恢復到完整狀態三項原則；文件明示保護可能不完美或不適用所有裝置，因此偵測與復原是重新取得安全正常運作的獨立能力
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-08-12
basis: S11 §3.1 的 Protection、Detection、Recovery 定義與後續說明直接支持三項責任不可互相替代
boundary: NIST 指引處理一般平台韌體與關鍵資料，Recovery 範圍也明示限於這兩者；它不是 AI 機櫃隔離、冷卻、供電或營運復原標準，不能直接決定 attestation 失敗時的 rack-level 動作
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C15
label: inference
status: active
claim: 要把一份遠端證明升格成可查核的 AI 機櫃授權依據，至少要保存八欄：受測裝置與配置版本、Evidence 內容及涵蓋範圍、新鮮度與重播防護、Endorsements／Reference Values 及變更歷程、驗證者與 Evidence policy、Attestation Result 語意與有效期、依賴方的授權／隔離動作，以及失敗後的安全預設、可信復原與稽核紀錄
supporting_source_ids: S8,S9,S10,S11
contrary_source_ids:
as_of: 2026-08-12
basis: S8 分開角色、policy、結果、失敗與 freshness；S9 縮窄 token 真實性與 policy／實作安全邊界；S10 補足跨製造、整合、維護變更的 reference-value lineage；S11 補足偵測後仍需可信復原，四條來源合併後形成八欄責任護照
boundary: 八欄是研究中心整合四份官方文件的查核方法，不是 IETF、TCG、NIST 或 DMTF 共同發布的單一標準，也不證明八欄齊備就能消除所有攻擊、營運或供應鏈風險
verification_needed: 具名平台依同一版本化配置公開八欄內容、失敗注入、授權結果、復原紀錄與變更後重驗
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C16
label: unverified
status: active
claim: 具名 AI 機櫃 production operator 已對同一版本化配置公開完整八欄遠端證明決策護照，包含新鮮度、參考值生命週期、驗證政策、結果效期、實際授權後果、故障注入、可信復原與稽核結果，並把此能力接到 5274 或其他 universe 公司產品資格、部署、訂單與可辨識財務貢獻
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S8–S11 都是通用架構、token、reference-value 與 firmware-resiliency 文件；既有 S1–S7 只再提供規格、產品能力、展示與公司查詢入口，沒有一條買方到供應商的完整 production 證據鏈
boundary: 沒有找到完整公開鏈是證據缺口，不表示 operator 未在私有環境實作；也不得用一般資安功能、標準支援或單一稽核標章補成客戶部署與財務歸因
verification_needed: operator acceptance／incident／recovery 文件與供應商申報雙向對齊具名 rack configuration、八欄內容、qualification、部署分母、訂單、收入及毛利
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C17
label: verified
status: active
claim: IETF RFC 9334 把 Evidence／Attestation Result 的 freshness 定義為依本地 appraisal policy 的 expiry threshold 判斷，並說明可信同步時鐘、不可預測 nonce 與 epoch ID 三類方法；nonce 比對只能確認 claims 在挑戰值產生後被簽署，仍是粗略 epoch。RFC 9711 另要求所有 EAT use 都提供 freshness mechanism，將 iat 定義為 token 建立、claims 收集與簽署時間，同時提醒個別 cached claim 可能更早；RFC 7519 則把 exp 定義為 token 不應再被接受處理的時間上限、iat 可用來算 token 年齡，並允許實作者為 clock skew 設小幅 leeway
supporting_source_ids: S8,S9,S12
contrary_source_ids:
as_of: 2026-08-14
basis: S8 §10 直接說明本地 expiry threshold、timestamp／nonce／epoch 三種方法、nonce rough epoch 與每個 nonce 的 state；S9 §§4.1、4.3.1、6.3.11、9.3 直接說明 nonce entropy、iat 與 cached claim 邊界，以及 EAT 必須有 freshness mechanism；S12 §§4.1.4–4.1.6 直接定義 exp、nbf、iat 與 clock-skew leeway
boundary: 三份 RFC 定義通用架構與 token claim 語意，不替任何 AI 機櫃指定 60 秒 max-age、5 秒 clock skew、nonce 保存期、時間來源、授權動作或 safe default；同屬 IETF 消息鏈，不計成三個獨立平台或實作樣本
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C18
label: inference
status: active
claim: 遠端證明的簽章、token 處理窗口、Evidence 新鮮度、nonce 是否首次使用與最終授權必須分開裁決；本篇七欄新鮮度與重播帳把 claim 產生時間、token 身分與簽章、iat／現在時間、exp／clock skew、nonce 發出者與綁定、nonce 消耗狀態，以及本地 gate 輸出與下游決策接成可重算紀錄。固定教材中只有 fresh first use 通過 freshness／replay gate，stale-but-unexpired、wrong nonce、replayed nonce 與 expired-beyond-skew 都被拒絕，而通過者仍不能直接升格為允許執行
supporting_source_ids: S8,S9,S12
contrary_source_ids:
as_of: 2026-08-14
basis: S8 把 freshness threshold 留給本地 policy 並說明 nonce state；S9 分開 token iat 與更早的 cached claims，且要求 freshness mechanism；S12 分開 exp 處理窗口與 iat 年齡。把三者轉成七欄帳與五案例 AND gate 是研究中心的責任分解與確定性示例
boundary: 七欄帳、iat 12:00:00、exp 12:02:00、60 秒 max-age、5 秒 leeway、N-42 代稱、五個到達情境及 AND gate 都是教材假設，不是 RFC 預設、產品測試、攻擊實驗或 AI rack acceptance rule；N=5 是固定案例數，沒有 sampling SE／t、失敗率、可用率、部署或財務效果
verification_needed: 具名平台公開同一版本的 claim capture time、iat／exp、可信時間源、clock-skew policy、nonce owner／binding／消耗紀錄、replay case、freshness 結果、後續 appraisal／authorization 與 safe-default test
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 高風險指令要過四關：身分、版本、權限與查證

回到前面的場景。一道「關掉這櫃的水電」的指令要能被信任，不能只驗一張電子身分證；系統要依序回答四個不同問題。

| 驗證關卡 | 系統先問什麼 | 已有的公開機制 | 還不能因此判定 |
|---|---|---|---|
| 1. 確認身分 | 誰在發出或回應這道指令？ | Caliptra 規定晶片內的信任根如何建立身分起點，SPDM 規定零件如何交換身分憑證 | 某一款產品已正確實作、啟用並通過查證 |
| 2. 確認版本 | 現在執行的程式與設定是不是預期版本？ | Caliptra 可量測晶片內程式，SPDM 可把量測結果交給另一端查驗 | 簽章正確的版本一定安全，或驗證失敗後系統一定會停止動作 |
| 3. 核對權限 | 確認身分後，它可不可以切斷水電或隔離設備？ | SPDM 體系另有正式授權規格，專門處理允許哪些動作 | 任一 AI 機櫃已把這套授權規格接進實際控制流程 |
| 4. 查證是否照做 | 買方憑什麼相信廠商的實作符合規格？ | 晶片側已有 OCP S.A.F.E. 第三方稽核制度 | 所有相關產品都已通過稽核；零件互驗的共同測試指引目前仍停在草稿 |

四關有先後順序，也有不同責任。第一與第二關建立「這是誰、現在跑什麼」，第三關才決定「能做什麼」，第四關則讓買方不用只相信廠商自述。前一關通過，不能替後一關出具結果。

**和上一篇的關係。** 上一篇談的是「誰發請求、誰做最終裁決」；本篇補上那個請求者的身分與版本如何被確認。兩篇在概念上相接，但目前沒有平台文件說明驗證失敗時，斷電指令會被拒絕、進入安全狀態，還是只留下紀錄後照常執行。

## 有簽章的量測報告，為什麼仍不是「可以執行指令」

IETF 的 RATS 架構用護照解釋這個差別：申請人交出的出生證明等資料像 **Evidence**，發照機關
像 **Verifier**，護照像 **Attestation Result**，真正決定能不能入境的海關才是
**Relying Party**。[S8] 一份出生證明是真的，不代表海關必須准許入境；同樣地，裝置交出的
量測有合法簽章，也不代表機櫃控制器必須接受它的斷電請求。

遠端證明至少要走完七站，任何一站少資料，研究結論就停在那一站：

| 決策站 | 白話問題 | 需要的資料 | 前一站不能替它證明什麼 |
|---|---|---|---|
| 1. 裝置產生證據 | 誰在報告哪一個元件與狀態？ | 裝置身分、配置版本、量測涵蓋範圍與簽章 | 簽章正確不代表量測涵蓋所有關鍵韌體與設定 |
| 2. 確認證據夠新 | 這是現在的狀態，還是昨天的舊報告？ | 外部一次性隨機值、時間或 epoch，以及結果有效期 | 身分正確不代表報告沒有被重播 |
| 3. 準備比較基準 | 目前版本應該量到什麼？ | 建立者可查的參考值、適用產品／版本、簽章與變更歷程 | 實際量測值本身不會說明「合格值」是什麼 |
| 4. 驗證者判讀 | 誰用哪套規則比較？ | 驗證者身分、Evidence policy、參考值與例外規則 | 兩個驗證者看同一份證據，不一定採相同門檻 |
| 5. 產生證明結果 | 結果究竟代表什麼、能用多久？ | 通過／不通過或詳細狀態、簽章、產生時間與效期 | token 能被驗簽，不代表結果欄位已照買方期待檢查 |
| 6. 依賴方做決定 | 這個結果允許哪一個動作？ | 依賴方政策、請求權限、允許／限制／隔離結果 | 證明結果是決策輸入，不等於授權決策本身 |
| 7. 失敗與復原 | 驗證失敗、服務不可用或韌體受損時怎麼辦？ | 安全預設、隔離、可信映像、復原步驟、重驗與稽核紀錄 | 偵測異常不代表裝置能安全恢復，也不代表機櫃已回到可服務狀態 |

第二站尤其容易被忽略。RFC 9334 說明證據與證明結果都要有新鮮度，RFC 9711 另定義 nonce
供重播防護與 token freshness；但 nonce 欄位存在，仍不能替產生方式、綁定對象、有效期間及
實作安全背書。[S8][S9]

第三站也不是把一份「黃金雜湊值」永久放進資料庫。TCG 的 RIM 模型允許製造商先建立 primary
bundle，系統整合商、維護者及後續 patch／upgrade 再追加有簽章且彼此串接的 bundle。[S10]
因此韌體合法更新後量測改變，可能代表「參考值也應更新」，不一定代表遭入侵；反過來，若
參考值來源、版本或變更鏈不清楚，量測完全相等也不足以證明比較基準可信。

最後一站借用 NIST 的平台韌體韌性邊界：**保護、偵測、復原是三件事**。[S11] 遠端證明可以
協助偵測偏離，卻不能自動產生可信映像、恢復韌體、重建服務或決定整櫃水電狀態。NIST 文件也
只處理韌體程式與關鍵資料；把它延伸成 AI 機櫃級復原，仍需要平台自己的程序與實測。

## 簽章有效、token 沒過期，為什麼仍可能被拒絕

**先把五個判斷拆開。** 驗簽只回答 token 是否來自預期金鑰、內容是否在途中被改動；`exp`
回答它是否仍在處理窗口；`iat` 可協助計算 token 年齡；nonce 回答這是不是對本次挑戰的回應；
最後還要由本地 policy 決定多老算 stale，再把合格 Evidence 交給 Reference Value、Appraisal
Policy 與 Relying Party。五關任一個缺失，都不能用「簽章成功」補過去。

RFC 9334 把 freshness 門檻明確留給本地 appraisal policy，並提供可信同步時鐘、不可預測 nonce
與 epoch ID 三條路。[S8] Nonce 的用途是讓查驗方知道 claims 在它發出挑戰後才被簽署；它建立的
只是粗略 epoch，而且通常要為每個 nonce 保存狀態。RFC 9711 再要求 EAT 必須有 freshness
mechanism、EAT nonce 至少有 64 bits entropy，並提醒 `iat` 是 token 組合簽署時間，個別 cached
claim 可能早在幾天前產生。[S9] 所以「token 很新」與「裡面每個量測都很新」仍是兩個問題。

JWT 的 `exp` 與 `iat` 又是另一層。RFC 7519 定義 `exp` 為 token 不應再被接受處理的時間上限，
`iat` 可用來算 token 年齡，並允許實作者為 clock skew 設小幅 leeway。[S12] 但 RFC 沒有規定本文
下面的 60 秒與 5 秒，也沒有說尚未到 `exp` 就必然符合某個 attestation profile 的 freshness。

### 同一組時間與簽章狀態下的五個命運

以下純為可重算教材，不是 AI 機櫃標準：假設五個訊息都已通過簽章、issuer／audience 與 profile
檢查，`iat=12:00:00`、`exp=12:02:00`；本地 policy 另設 `max-age=60 秒`、clock-skew leeway
`5 秒`，預期 nonce 為 `N-42`。`N-42` 只是方便閱讀的代稱，實際挑戰假設符合 EAT 至少 64 bits
entropy 的要求。為了隔離 token 與 replay 邊界，本例還假設各 claim 都在 `iat` 當下收集；真實
系統必須逐項記錄更早的 claim capture time。

本文示例 gate 為：`簽章有效 AND 現在時間 < exp+leeway AND token age ≤ max-age AND nonce 相符
AND nonce 尚未消耗`。這個 AND 式與邊界等號是示例 policy，不是 RFC 強制公式。

| 假想情境 | 到達時間／token age | 距名目 `exp` | Nonce 狀態 | 本地 freshness／replay gate | Gate 後仍要做什麼 |
|---|---:|---:|---|---|---|
| fresh first use | 12:00:40／40 秒 | +80 秒 | `N-42` 相符、未消耗 | pass | 查參考值、Appraisal Policy，再由 Relying Party 授權 |
| stale but unexpired | 12:01:10／70 秒 | +50 秒 | `N-42` 相符、未消耗 | fail：超過 60 秒 max-age | 拒絕作為新鮮證據；不能因尚未到 `exp` 放行 |
| wrong nonce | 12:00:40／40 秒 | +80 秒 | 非 `N-42` | fail：挑戰不相符 | 拒絕；簽章與時間通過不能替代 request binding |
| replayed nonce | 12:00:41／41 秒 | +79 秒 | `N-42` 相符、但已消耗 | fail：第二次使用 | 拒絕重播；調查 nonce ledger 與重送原因 |
| expired beyond skew | 12:02:10／130 秒 | −10 秒，亦超過 5 秒 leeway | `N-42` 相符、未消耗 | fail：處理窗口與 max-age 均失敗 | 拒絕並重新挑戰，不沿用舊 token |

Python `Fraction` 與獨立 `awk` 整數路徑都得到同一組結果：五例的 age 為
`40／70／40／41／130 秒`、距名目 `exp` 為 `+80／+50／+80／+79／−10 秒`，只有第一例通過
完整 gate。這是 `N=5` 個固定案例的確定性規則展開，不是抽樣、攻擊測試或 production log，
沒有 sampling SE／t、拒絕率、延遲、可用率、客戶部署或公司財務。

**第一例也只取得「可繼續判讀」資格。** 它還沒證明 claim 涵蓋完整、參考值正確、
Verifier policy 通過，更沒有替 Relying Party 決定能否切斷水電。把 freshness pass 直接顯示成
「已授權」，等於把本篇七站中的第二站跳接到第六站。

### 多空小作文要共享七欄新鮮度與重播帳

| 七欄帳 | 至少保存什麼 | 缺少時多空兩邊都不能說什麼 |
|---|---|---|
| 1. Claim 產生時間與範圍 | 每個量測／設定何時取得、是否快取、涵蓋哪個元件與版本 | 不能用 token `iat` 代替所有 claim age |
| 2. Token 身分與完整性 | issuer、audience、profile、key／algorithm、簽章結果 | 不能只憑「有簽章」判定來自正確角色 |
| 3. `iat`、現在時間與時間源 | token 建立時間、驗證端現在時間、時鐘來源與同步狀態 | 不能重算 token age，也不能評估時鐘是否可信 |
| 4. `exp`、`nbf` 與 clock skew | token 處理窗口、leeway 值、邊界比較規則與 policy 版本 | 不能分辨逾期、尚未生效與寬限放行 |
| 5. Nonce 發出者與綁定 | 誰產生挑戰、entropy、綁定裝置／request／stage 與有效期 | 不能證明回應屬於這一次查驗 |
| 6. Nonce 消耗與重播紀錄 | issued／consumed／expired 狀態、首次使用時間、重送與衝突 | 不能分辨合法第一次使用與舊 token 重播 |
| 7. Gate 輸出與下游決策 | 每一 gate pass／fail 原因、Evidence appraisal、授權／隔離／人工覆核與 safe default | 不能把 freshness pass 改寫成最終允許執行 |

偏多小作文會說，版本化 freshness policy、可信時間源與一次性 challenge 能讓大批機櫃在不用人工
逐台確認的情況下持續驗證，因而提高安全自動化與可管理性；偏空小作文則會說，時鐘同步、nonce
state、replay cache 與驗證服務本身增加延遲、狀態與故障面，過嚴 max-age 甚至可能讓正常設備被
隔離。兩邊都要交同一張七欄帳、同一政策版次、accept／stale／replay／service-unavailable 分母、
決策延遲、safe-default 測試與後續授權結果。少了這些，偏多不能把「支援 EAT」推成可大規模自動
授權，偏空也不能把一次拒絕推成架構不可用，更不能直接連到 5274 或其他公司的訂單與損益。

## 用八欄遠端證明決策護照查一份平台資料

遇到「支援遠端證明」「安全啟動已完成」或「驗證通過」的產品資料，可以把下列八欄抄成一張
護照。八欄不是要廠商公開私密金鑰或完整防禦規則，而是讓買方知道結果適用哪個版本、由誰判讀、
能支持哪個動作，以及失敗後是否可回到可信狀態。

| 八欄護照 | 至少記下什麼 | 缺少時最容易誤讀成 |
|---|---|---|
| 1. 受測物與版本 | 晶片、板卡、BMC／韌體、設定、機櫃配置與各自版本 | 「同系列產品」都得到同一結果 |
| 2. Evidence 與涵蓋範圍 | 哪些量測、憑證、設定與 telemetry 被收集，哪些沒收集 | 有簽章就等於整台設備都可信 |
| 3. 新鮮度與重播防護 | nonce／時間／epoch 的產生者、綁定對象、效期與拒絕舊結果規則 | 舊合格報告仍代表現在狀態 |
| 4. Endorsement／Reference Value | 誰發布、適用版本、簽章、primary／supplemental lineage 與撤銷／更新 | 比對相等就代表比較基準正確 |
| 5. 驗證者與 Evidence policy | 驗證者身分、信任錨、門檻、例外、缺值及不可用時怎麼處理 | 所有驗證者都會得到同一判斷 |
| 6. Attestation Result | 欄位語意、簽章、產生時間、效期及哪些 claim 已檢查或只轉傳 | token 可驗簽就代表所有 claim 都已查過 |
| 7. 依賴方決策 | 哪個控制器依哪套 policy 做允許、降權、隔離、拒絕或人工覆核 | 驗證通過就自動擁有所有操作權限 |
| 8. 失敗、復原與稽核 | failure injection、safe default、可信恢復來源、重驗、時間與 audit trail | 發現異常就等於安全復原並恢復服務 |

這張護照把「技術可以做」與「正式環境已採用」分開。完整規格或 demo 最多證明某些欄位可實作；
要升到客戶資格，還要有同一版本配置的 acceptance plan、失敗注入、結果與復原紀錄。再往公司
財務走，仍須買方與供應商雙向對上具名產品、部署分母、訂單、收入或毛利，不能用八欄方法本身
推導 5274 或其他公司受惠。

## 什麼證據會讓這個判斷改變

目前的判斷是：公開規格已把身分、版本與權限的分工寫清楚，但可讓買方獨立查證實作的制度成熟度不同。若零件互驗的共同測試指引正式發布，並出現可查的裝置測試結果，「只能讀成廠商宣稱」這句話就必須縮窄。

另一種改變來自買方。若營運方公開採購驗收條款、自建測試或其他可重複查證方法，證明它已經不依賴賣方自述，第三方共同測試尚未定稿就不再代表買方缺少查證路徑。

反過來也要說清楚：測試指引長期停在草稿，不證明 SPDM 不安全、沒人採用或即將被取代；它只證明本文尚未找到一條正式、共同且可查的測試路徑。

## 用四個問題判讀公司新聞

這篇現在不支持任何個股動作。它的用途是一張查核表：看到公司寫「支援 Caliptra」或「採用 SPDM」時，先按下列順序找證據。

| 公司新聞查核問題 | 要找的具體證據 | 找不到時停在哪裡 |
|---|---|---|
| 1. 新聞在說哪一關？ | 具名晶片、程式版本、身分互驗或權限判斷功能 | 只知道公司使用安全名詞，還不知道它負責哪一層 |
| 2. 有沒有獨立查證？ | 第三方稽核報告、共同測試結果或買方驗收條款 | 停在廠商自述，不寫成已通過驗證 |
| 3. 有沒有買方採用？ | 具名客戶、驗證階段、量產配置或部署文件 | 停在產品能力，不寫成訂單或市占 |
| 4. 有沒有財務足跡？ | 出貨量、可辨識收入、毛利或可重建的財務分母 | 停在技術查核入口，不做個股貢獻判斷 |

目前唯一直接對應的 5274 信驊，能引用的只有 AST2700 產品頁所列功能；沒有第三方查證結果、客戶驗證階段、量產出貨與拆分收入或毛利。這四問也能套用到其他宣稱提供 AI 機櫃安全功能的公司，不限於信驊。

## 來源

<!-- research_source
source_id: S1
role: standard
source_kind: living_index
publisher: Open Compute Project
independence_group: caliptra-project
title: Caliptra R1 產品與規格登錄頁
published_at:
captured_at: 2026-08-08
accepted_at: 2026-08-08
status: active
url: https://www.opencompute.org/products/575/caliptra
locator: 2026-08-08 觀察到 Caliptra R1 說明段（IP 與韌體、targets datacenter-class SoCs、RTM block inside an SoC）以及 OCP SAFE Security Conformance Report 與 OCP Security Review Provider 兩個標示
limitation: 產品登錄頁會持續更新且無單一發布日；列出稽核報告與稽核機構制度不等於任何具體裝置已送稽核或已通過
-->

<!-- research_source
source_id: S2
role: standard
source_kind: living_index
publisher: Caliptra project (CHIPS Alliance hosted)
independence_group: caliptra-project
title: Caliptra 規格文件
published_at:
captured_at: 2026-08-08
accepted_at: 2026-08-08
status: active
url: https://chipsalliance.github.io/Caliptra/doc/Caliptra.html
locator: 2026-08-08 觀察到 Revision 2.1 Version 0.1 標示、minimalistic scope 敘述、out-of-scope 清單（foundry IP integration、physical design countermeasures、analog IPs、post manufacture test and initialization、certification），以及 DPE 作為 SPDM responder signing oracle 的段落
limitation: 該頁隨 revision 更新且未標示正式發布日期；規格描述不代表任何矽晶片已實作或啟用對應功能
-->

<!-- research_source
source_id: S3
role: standard
source_kind: living_index
publisher: DMTF
title: DMTF SPDM 工作組與標準清單頁
published_at:
captured_at: 2026-08-08
accepted_at: 2026-08-08
status: active
url: https://www.dmtf.org/standards/spdm
locator: 2026-08-08 觀察到 DMTF Specifications 表中 DSP0274 1.4.1（02 Jul 2026）、DSP0289 1.0.0（08 Dec 2025）、DSP0277 2.0.0（08 Dec 2025），Work in Progress 表中 DSP-IS0023 1.0.0WIP50 SPDM Conformance Test Suite Guidance（11 Jul 2022），以及 Upcoming Deliverables 中 DSP2071 SPDM Authorization White Paper 目標 2026Q3
limitation: 標準索引頁會持續變動，只能證明當日所見版本與狀態；規格已發布不代表任何裝置實作或通過測試，指引仍為 WIP 也不代表沒有其他驗證途徑
-->

<!-- research_source
source_id: S4
role: standard
source_kind: document
publisher: DMTF
title: Security Protocol and Data Model (SPDM) Specification 1.4.0（DSP0274）
published_at: 2025-05-15
captured_at: 2026-08-08
accepted_at: 2026-08-08
status: active
url: https://www.dmtf.org/sites/default/files/standards/documents/DSP0274_1.4.0.pdf
locator: 封面 Document Identifier DSP0274、Date 2025-05-15、Document Status Published、Supersedes 1.3.0；目錄 7.2 Identity authentication（7.2.1.1.1 device、7.2.1.1.2 alias、7.2.1.1.3 generic certificate model）、7.3 Firmware and configuration measurement、7.4 Secure sessions
limitation: 本輪只核對封面與目錄層級，未逐節重算訊息欄位、狀態機或密碼學細節；此為 1.4.0，索引頁顯示現行版本已為 1.4.1
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: living_index
publisher: ASPEED Technology
title: ASPEED AST2700 產品頁
published_at:
captured_at: 2026-08-08
accepted_at: 2026-08-08
status: active
url: https://www.aspeedtech.com/server_ast2700/
locator: 2026-08-08 觀察到「AST2700 adapts "Caliptra" which is a silicon RoT IP defined by OCP」敘述句、規格列的 Secure boot engine by Caliptra (SiRoT)，以及 12nm、四核 ARM Cortex-A35 1.6GHz 與兩顆 ARM Cortex-M4 400MHz
limitation: 產品頁無發布日且會更新；規格列項目不證明量產出貨、客戶採用、稽核通過或任何財務貢獻
-->

<!-- research_source
source_id: S6
role: competitor_primary
source_kind: document
publisher: Insyde Software
title: Insyde Software Presents Advances in AI Rack Telemetry and Security in OpenBMC at 2026 OCP APAC Summit
published_at: 2026-08-04
captured_at: 2026-08-08
accepted_at: 2026-08-08
status: active
url: https://www.insyde.com/news/press-releases/insyde-software-presents-advances-in-ai-rack-telemetry-and-security-in-openbmc-at-2026-ocp-apac-summit/
locator: AST2700 silicon-native Root of Trust 整合 Supervyse OPF 段落（open-source Caliptra specification with DICE identity、PUF-based key storage、post-quantum crypto readiness），以及 SerDes-level telemetry 經 DMTF Redfish APIs 暴露 per-lane eye height、BER、link state、error counters 與 LTSSM logs 的段落
limitation: 全文為峰會議程與展示預告，明確未主張量產部署、具名客戶或營收；第三方韌體商的整合敘述也不能替代 ASPEED 自身揭露
-->

<!-- research_source
source_id: S7
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-08
accepted_at: 2026-08-08
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-08 以 5274 代號重查季報、法說與重大訊息的入口；當日未由此入口取得任何 AST2700 安全功能相關的公司揭露
limitation: 查詢入口會持續更新，入口本身不證明出貨、客戶認證或財務貢獻，也不能替代公司正式文件內容驗證
-->

<!-- research_source
source_id: S8
role: standard
source_kind: document
publisher: Internet Engineering Task Force
independence_group: ietf-rats
title: RFC 9334 Remote ATtestation procedureS (RATS) Architecture
published_at: 2023-01-13
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.rfc-editor.org/rfc/rfc9334.html
locator: §§4.1–4.2 定義 Attester／Verifier／Relying Party、Evidence／Attestation Result／Reference Values／Appraisal Policies；§§5.1–5.2 描述 passport／background-check models 與三種失敗；§§8.1–8.5 說明概念訊息；§10 說明 timestamp、nonce、epoch 的 freshness
limitation: RFC 9334 是 IETF consensus 的 Informational 架構，不是 AI rack protocol、產品安全認證、評估 policy 或實作測試結果；其角色可由同一實體合併，不能由概念圖反推實際部署拓撲
-->

<!-- research_source
source_id: S9
role: standard
source_kind: document
publisher: Internet Engineering Task Force
independence_group: ietf-rats
title: RFC 9711 The Entity Attestation Token (EAT)
published_at: 2025-04-30
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.rfc-editor.org/rfc/rfc9711.html
locator: §§1.3–1.3.1 說明 verifier 將 Evidence 轉成 Attestation Results 且處理規則屬 local policy；§8.4 定義由遠端來源衍生 nonce 的 replay protection／token freshness；§9.1 明示 claim semantics 不規定 attester 或實作的安全等級
limitation: EAT 是 CWT／JWT 上的 attestation-oriented claims 與 token 格式，不等於任一裝置已採用、policy 已公開或安全實作已驗證；IETF 與 S8 同一標準鏈，不另計獨立來源組
-->

<!-- research_source
source_id: S10
role: standard
source_kind: document
publisher: Trusted Computing Group
independence_group: trusted-computing-group
title: TCG Reference Integrity Manifest Information Model Version 1.1 Revision 1.0
published_at: 2024-04-26
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://trustedcomputinggroup.org/wp-content/uploads/TCG-Reference-Integrity-Manifest-RIM-Information-Model-Version-1.1-Revision-1.0_pub-1.pdf
locator: PDF pp.9、13–16 定義 RIM、Creator、Base／Support／Composite bundles、critical firmware／event／configuration digests、signature 與 backward-linked collection；pp.25–28 說明 installation、pre-delivery modification、maintenance update、patch 與 upgrade 的新 RIM／supplemental RIM 責任
limitation: 此為通用 reference integrity information model，不是 Caliptra、SPDM、AI rack 或客戶 qualification；PDF header 日期為 2024-04-10，TCG resource page 將 Version 1.1 Revision 1.0 列為 2024-04-26 發布
-->

<!-- research_source
source_id: S11
role: regulator_or_policy
source_kind: document
publisher: National Institute of Standards and Technology
independence_group: nist
title: NIST SP 800-193 Platform Firmware Resiliency Guidelines
published_at: 2018-05-04
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-193.pdf
locator: §3.1（PDF pp.17–18、printed pp.10–11）分別定義 Protection、Detection、Recovery，並說明保護機制可能不完美或不適用所有裝置，需由偵測與復原重新取得正常安全運作
limitation: 指引適用一般平台韌體與關鍵資料，Recovery 範圍亦明示限於兩者；不是 AI rack attestation、機櫃水電隔離、整體服務復原或任何產品／公司的驗收與財務證據
-->

<!-- research_source
source_id: S12
role: standard
source_kind: document
publisher: Internet Engineering Task Force
independence_group: ietf-rats
title: RFC 7519 JSON Web Token (JWT)
published_at: 2015-05-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.rfc-editor.org/rfc/rfc7519.html
locator: RFC header 與 §§4.1.4–4.1.6；exp 定義 current time 必須早於 expiration、可為 clock skew 提供小幅 leeway，nbf 定義 not-before，iat 可用來判斷 token age；RFC header 只標 May 2015，帳本日期以 2015-05-01 正規化且不主張日精度
limitation: JWT 是通用 claims token 規格，exp／nbf／iat 都是 optional，並不指定 EAT profile、attestation freshness max-age、nonce lifecycle、時間可信度、授權或 AI rack safe default；與 S8／S9 同屬 IETF 標準鏈，不另計獨立產品、平台或實作樣本
-->

## 族群影響

<!-- impact
group_id: ipdesign
stock_ids: 5274
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-11-14
rationale: 5274 是 universe 中唯一在產品頁直接對應本信任鏈的個股，AST2700 明示採用 Caliptra SiRoT，因此是此議題的第一查核位置
evidence_boundary: 只有產品頁規格與第三方韌體商整合公告，沒有出貨量、客戶認證階段、稽核結果或財務分拆；不建立受惠推論或排行
-->

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-11-14
rationale: 系統與機櫃整合商位於 BMC、平台韌體與客戶驗收條款的交界，是觀察保證層是否被寫進採購驗收的路由位置
evidence_boundary: 沒有任何 universe 公司具名承擔 attestation 或授權鏈責任的文件、驗收條款或財務分母，僅作搜尋路由
-->

## 監測器

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C3,C7
metric: SPDM 側保證層文件狀態，包含 DSP-IS0023 一致性測試指引是否轉為正式發布、DSP2071 授權白皮書是否發布，以及 DSP0274 1.5 的 PQC 混合支援計畫進展
source_ids: S3,S4
watch_source_ids: S3
frequency: monthly
next_check: 2026-08-31
trigger: DSP-IS0023 由 Work in Progress 轉為正式版本、DSP2071 白皮書發布，或出現可查的 SPDM 一致性測試結果
invalidation: 指引持續維持 WIP 且無授權白皮書與測試結果，則 C7 的保證層不同步判讀維持不變；若同時出現正式指引與裝置測試結果，C7 措辭必須縮窄
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C1,C2,C7
metric: OCP S.A.F.E. 稽核制度的覆蓋範圍與 Caliptra 規格範圍變動，包含新稽核報告、新增 Security Review Provider 與稽核是否延伸至 BMC 或機櫃層
source_ids: S1,S2
watch_source_ids: S1
frequency: quarterly
next_check: 2026-09-30
trigger: OCP 公布涵蓋 BMC 或機櫃層的 S.A.F.E. 稽核報告、新增稽核機構，或 Caliptra 新 revision 改變 RTM 與 certification 的範圍分工
invalidation: 稽核制度長期僅覆蓋晶片層而未延伸到平台，或 Caliptra 範圍縮小，均使「規格已補齊」的措辭需要重新界定
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C5,C6,C10
metric: 5274 信驊是否首次把 AST2700 的出貨量、客戶認證階段與可辨識收入或毛利分開揭露
source_ids: S5,S6
watch_source_ids: S7
frequency: quarterly
frequency_detail: 每季財報與法說後複核
next_check: 2026-11-14
trigger: 公司季報、法說或重大訊息首次分開揭露 AST2700 出貨、客戶認證與財務貢獻，或客戶端出現具名採用文件
invalidation: 僅有產品頁規格更新與生態系整合公告而無出貨與財務足跡，則 C10 維持未驗證，不得升格為公司事實
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C11,C12,C13,C14,C15,C16
metric: 具名平台是否把 Evidence 涵蓋範圍 新鮮度 Reference Value lineage Verifier policy Attestation Result 效期 Relying Party 動作 failure injection 可信復原與稽核紀錄接成同一版本化遠端證明決策鏈
source_ids: S8,S9,S10,S11
watch_source_ids: S1,S3
frequency: quarterly
next_check: 2026-11-14
trigger: OCP DMTF 或具名 operator／platform 公開同一配置的八欄 acceptance plan 測試結果 失敗授權後果及 recovery evidence，並可回查產品版本與責任人
invalidation: 若後續正式架構顯示八欄遺漏會改變安全判讀的角色或狀態，則追加修正 claim 縮窄 C15；若 production 文件完整交付八欄，則 C16 應由待驗證改以新 claim 升級
-->

## 還不能下哪些結論

- 產品頁寫「支援 Caliptra」或「採用 SPDM」，只代表廠商宣稱具備某項機制，不能改寫成安全性已被獨立驗證。
- 共同測試指引仍是草稿，只代表本文尚未找到正式的標準化查證路徑；不能因此推論 SPDM 不安全、採用率低或即將被取代。
- 5274 信驊產品頁列出安全功能，不等於已取得訂單、市占、毛利或競爭優勢；目前仍缺買方採用與財務證據。
- 韌體供應商的整合展示證明功能可以被放在同一套展示裡，不等於已有客戶部署、量產出貨或營收。
- 身分或版本驗證失敗後，機櫃究竟會拒絕指令、限制功能或只留下紀錄，目前沒有平台或場域文件可以判定。
- token 簽章可驗證、nonce 欄位存在或量測等於某個參考值，都不能單獨證明 policy、授權後果、結果效期與可信復原已正確實作。
- RATS、EAT、RIM 與 NIST 韌性指引可以共同建立查核欄位，但四份文件沒有共同認證任何 AI 機櫃，也沒有把技術鏈接到 universe 公司資格、部署或財務。
