# AI 機櫃信任根：規格已接上，能獨立驗證的保證層還沒接上

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

## 新手先讀：這篇在講什麼

### 名詞小字典

- **信任根（Root of Trust）**：一塊被假定為可信的最小硬體，開機時先檢查其他程式有沒有被換掉。其他所有安全機制都建立在「這一塊沒被動過」的前提上。
- **量測（Measurement）**：開機時把每一段韌體的內容算成一組指紋並記錄下來。它只忠實記錄「跑的是哪一版」，本身不判斷那一版好不好。
- **證明（Attestation）**：把上述指紋加上簽章交給外部系統看，讓對方能確認這台機器現在跑的是什麼。簽章只保證來源與內容沒被竄改，不保證內容是安全的。
- **授權（Authorization）**：確認「你是誰」之後，再決定「你可不可以做這件事」。這是兩件事，可以只做到前者而完全沒做後者。
- **一致性測試（Conformance test）**：用共同測試套件驗證某個實作真的照規格做。沒有它，「支援某標準」只是廠商自述。
- **BMC**：伺服器裡獨立於主系統的管理晶片，即使主機關機或當掉仍能監控與下指令，因此它自己的可信度特別關鍵。

### 三句話抓重點

- OCP Caliptra 定義晶片內的量測型信任根，DMTF SPDM 定義元件之間如何交換身分與量測，而 SPDM 另有一份已發布的獨立授權規格，三者合起來在規格面已經把「身分→量測→證明→授權」這條鏈補齊。
- 但讓營運方獨立驗證「某個產品真的做到這條鏈」的保證層並不同步：Caliptra 這側已有 OCP S.A.F.E. 稽核報告與第三方稽核機構制度，SPDM 這側的一致性測試指引到 2026-08-08 為止仍標示為 work-in-progress、日期停在 2022-07-11。
- 因此現階段「支援 Caliptra／SPDM」只能讀成宣稱具備該機制，不能讀成授權鏈已被獨立驗證；台灣唯一直接對應的 universe 個股 5274 信驊在產品頁列出 Caliptra SiRoT，但沒有任何出貨、客戶認證或財務揭露可以引用。

### 為什麼重要

上一篇 MI-2026-08-07-AI-RACK-ACTION-CONTRACT 把機櫃控制拆成「身分→具語意數值→誰有權發請求→安全裁決→隔離狀態→維修結果」。那條鏈有一個沒有處理的前提：憑什麼相信發出隔離請求的那個身分是真的？如果身分本身可以被偽造，後面所有 guardrail 與稽核紀錄都只是在記錄一個假名。這篇要處理的就是那個前提。

真正值得學會的判讀方式是：**把「規格存在」與「有人能替你查證」分成兩件事**。產業新聞通常只講到前者——某某晶片「支援 Caliptra」、某某平台「採用 SPDM」。但安全性的商業價值來自後者：買方能不能不靠賣方自述就確認這件事。這兩層在本輪的公開資料裡成熟度明顯不同，而這個落差本身就是可觀察、可反證的研究對象，比爭論「AI 資安是不是題材」有用得多。

### 接下來怎麼追

- DMTF 標準頁上的 DSP-IS0023 SPDM Conformance Test Suite Guidance 是否由 work-in-progress 轉為正式發布，以及 DSP2071 SPDM Authorization White Paper 是否如標示在 2026Q3 出現。
- OCP 是否公布新的 S.A.F.E. 稽核報告或新增 Security Review Provider，特別是稽核範圍有沒有從晶片延伸到 BMC 與機櫃層。
- 5274 信驊的季報、法說或重大訊息是否首次把 AST2700 的出貨量、客戶認證階段與可辨識收入或毛利分開揭露。

### 想一想

- 如果一台機器的 attestation 驗證失敗，它到底會發生什麼事——請求被拒絕、進入安全狀態，還是只寫一行紀錄然後照常執行？找不到這個答案的話，這條鏈算不算真的接上了？
- 「通過稽核」保護的是誰：是買方不必自己重做安全測試，還是賣方多一個可以印在型錄上的標章？兩者要用什麼不同的證據來分辨？
- 一致性測試指引停在 2022 年，究竟代表這件事不重要、已經被別的機制取代，還是產業尚未有人願意承擔測試成本？

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

## 信任鏈的五層：規格分工與保證分工不是同一件事

把公開文件攤開後，這條鏈可以拆成五個責任不同的層，且每層的「誰負責」與「誰能查證」都不一樣。

1. **晶片內量測**：Caliptra 定義 SoC 內的 RTM 區塊，處理身分、measured boot 與證明能力（C1）。它刻意最小化，並把 certification 明確排除在規格之外（C2）——也就是說，規格本身從一開始就假設保證工作由別的制度承擔。
2. **元件間傳遞**：SPDM 定義元件之間如何提供身分憑證、執行執行期認證、取得韌體與組態量測，以及建立加密工作階段（C4）。Caliptra 的 DPE 可作為這一層的簽章來源（C2），這是兩份規格實際接合的地方。
3. **授權**：認證與授權在 SPDM 體系中是分開的文件——DSP0289 SPDM Authorization Specification 已於 2025-12-08 發布為 Standard（C3）。這一點值得注意：能證明「你是誰」的規格早於能決定「你可以做什麼」的規格，而後者發布至今仍未有對應的白皮書（標示目標為 2026Q3）。
4. **保證與稽核**：Caliptra 這側可看到 OCP S.A.F.E. 稽核報告與第三方 Security Review Provider 制度（C1）；SPDM 這側的一致性測試指引仍為 work-in-progress，日期停在 2022-07-11（C3）。兩側都存在，但成熟度不同步。
5. **平台落地**：AST2700 在產品頁列出 Caliptra SiRoT（C5），Insyde 於 2026-08-04 公布把它整合進 OpenBMC 平台並以 Redfish 暴露 SerDes telemetry（C6）。這一層目前只有能力展示，沒有部署、認證或財務足跡。

## 這條鏈接到上一篇的哪裡

MI-2026-08-07-AI-RACK-ACTION-CONTRACT 的第三層是 action ownership——分辨誰可以發請求、誰持有語意、誰負最終裁決責任。那個分辨動作預設身分是可信的。本篇的第一到第三層正好補上這個預設：晶片內身分（Caliptra）→ 跨元件證明（SPDM 認證與量測）→ 授權判斷（SPDM Authorization）。C8 只把這個接點寫成推論，不宣稱任何平台已經把 attestation 結果實際接進隔離請求的裁決邏輯；那仍是 C9 的未驗證項。

## 研究判定

主命題 C7 是判讀，不是事件。它可被兩種結果推翻：其一，SPDM 一致性測試指引正式發布並出現可查的裝置測試結果，那麼「保證層不同步」的描述就必須縮窄；其二，若找到營運方已用其他機制（例如採購驗收條款或自建測試）實質完成獨立驗證，則「只能讀成宣稱」的措辭同樣過強。這兩種結果都由 T1 與 T2 明確監測。

反向也要說清楚：一致性指引長期維持 WIP 並不證明 SPDM 不安全或不被採用，只證明買方目前缺少一條標準化的第三方查證路徑。把前者說成後者是本篇最容易犯的錯，因此 C7 的 boundary 明確排除對產品實際安全性的評價。

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

## 目前不能下的結論／待驗證

- 不能把「支援 Caliptra」或「採用 SPDM」寫成安全性已被驗證；規格具備能力與實作通過查證是兩件事，這正是 C7 的全部內容。
- 不能由一致性測試指引仍為 WIP 推論 SPDM 不安全、採用率低或將被取代；本篇只描述買方缺少標準化第三方查證路徑。
- 不能由 5274 產品頁列出安全功能推導訂單、市占、毛利或競爭優勢；公司映射在 C10 與 ipdesign impact 中維持未驗證。
- 不能把 Insyde 的整合展示當成客戶採用或部署證據；該新聞稿本身即明示未主張部署、客戶與營收。
- 不能宣稱 attestation 失敗在任何 production 機櫃會導致特定授權後果；該行為在 C9 維持未驗證，需要平台或場域文件。
