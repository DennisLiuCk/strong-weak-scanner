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
- 最後看 5274 信驊是否首次在季報、法說或重大訊息中，揭露 AST2700 的客戶驗證階段、量產出貨與可辨識收入或毛利。

### 想一想

- 如果身分或程式版本驗證失敗，系統會拒絕斷電指令、進入安全狀態，還是只留下紀錄？公開資料目前說清楚了嗎？
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

## 還不能下哪些結論

- 產品頁寫「支援 Caliptra」或「採用 SPDM」，只代表廠商宣稱具備某項機制，不能改寫成安全性已被獨立驗證。
- 共同測試指引仍是草稿，只代表本文尚未找到正式的標準化查證路徑；不能因此推論 SPDM 不安全、採用率低或即將被取代。
- 5274 信驊產品頁列出安全功能，不等於已取得訂單、市占、毛利或競爭優勢；目前仍缺買方採用與財務證據。
- 韌體供應商的整合展示證明功能可以被放在同一套展示裡，不等於已有客戶部署、量產出貨或營收。
- 身分或版本驗證失敗後，機櫃究竟會拒絕指令、限制功能或只留下紀錄，目前沒有平台或場域文件可以判定。
