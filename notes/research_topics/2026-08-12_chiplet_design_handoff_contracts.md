# 小晶片會連線，還不等於能交付：從 FCSA、CDXML 到 3DK 合規鏈

<!-- research_topic
topic_id: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-12
source_published_at: 2026-02-12
last_reviewed_at: 2026-08-12
review_due: 2026-08-24
source_type: mixed
publisher: Open Compute Project Foundation
publisher_domain: opencompute.org
canonical_url: https://www.opencompute.org/documents/fcsa-1-0-0-pdf
source_chain_id: chiplet-handoff-primary-scan-20260812
stock_ids:
group_ids: ipdesign,packtest,semiequip
trigger_type: chiplet_design_handoff_contract_separation
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C7
base_confidence: medium
confidence_basis: FCSA 正式規格、OCP 3DK 教程、固定 commit 的四份 XSD 全數檢查，以及 Arm、Thrace、Siemens 三條獨立供應端資料，共同支持介面、系統角色、設計資料與合規流程必須分層；公開證據仍未形成跨工具與 foundry／OSAT 的端到端通過紀錄
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-12
from: initial
to: inbox
reason: captured_distinct_interface_architecture_metadata_and_conformance_contracts
evidence: source_chain:chiplet-handoff-primary-scan-20260812
-->
<!-- transition
date: 2026-08-12
from: inbox
to: triaged
reason: reproducible_schema_audit_supports_boundary_article_without_company_value_chain
evidence: sources:S1,S3,S4,S5,S6,S7,S9
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_unit_coordinate_cross_artifact_and_post_assembly_semantic_handoff_passport_without_thesis_clock_refresh
evidence: sources:S3,S5,S11,S12
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **小晶片（Chiplet）**：把原本可能放在一顆大晶片的功能拆成較小晶粒，再共同封裝成一套系統。
- **介面**：兩顆小晶片交換訊號與資料的連接規則；能連線只回答「怎麼說話」，不回答全部交付問題。
- **UCIe**：Universal Chiplet Interconnect Express，通用小晶片互連規格；本文只把它當成封裝內連線例子。
- **FCSA**：Foundation Chiplet System Architecture，基礎小晶片系統架構；定義系統拓撲、角色與必要介面。
- **CDXML**：Chiplet Data Exchange in XML Format，以 XML 描述小晶片機構、接腳、電氣與其他交接資料的格式。
- **XML**：用標籤組織資料的文字格式；格式可讀，不代表內容已符合一套完整設計規則。
- **XSD**：XML Schema Definition，XML 結構規則檔；工具可用它檢查欄位、型別與層級是否符合約定。
- **3DK**：3D-IC Design Kits，立體積體電路設計套件的總稱；它不是一份萬用檔案，而是一組不同資料包。
- **Package**：封裝；把一顆或多顆晶粒、載板與互連組成可測試及裝入系統的實體元件。
- **CDK**：Chiplet Design Kit，小晶片設計套件；交付單顆小晶片的實體、電氣、功能與模型資料。
- **ADK**：Assembly Design Kit，組裝設計套件；描述封裝組裝、間距、尺寸與檢查規則。
- **MDK**：Material Design Kit，材料設計套件；描述介電、熱、膨脹與機械性質。
- **TDK**：Test Design Kit，測試設計套件；描述測試接點、模式、方向與暫時測試接點。
- **EDA**：Electronic Design Automation，電子設計自動化；用軟體完成規劃、模擬、驗證與實體設計。
- **晶圓代工廠（Foundry）**：依設計製造晶圓的工廠；它提供製程規則，不替系統商決定所有小晶片角色。
- **封測廠（OSAT）**：Outsourced Semiconductor Assembly and Test，承接封裝與測試的外部服務商。
- **符合性（Conformance）**：依指定版本、輸入與測試程序確認實作符合規格；有規格名稱不等於已通過。
- **簽核（Sign-off）**：設計進入製造前，確認關鍵電性、熱、機械、測試與製程規則均達標的最後檢查。
- **工具匯入**：設計軟體真正讀進資料、保留單位與版本，並能執行檢查；檔案存在不等於匯入成功。
- **機器可讀**：資料有固定結構，程式可解析；它仍要通過語法、欄位、版本與跨工具一致性檢查。
- **語意驗證（Semantic validation）**：在格式正確之外，再檢查單位、座標、跨檔身分與工程規則是否彼此一致。
- **單位正規化（Unit normalization）**：先把 mm、µm 等量綱換到共同基準，再做比例、面積或距離運算。
- **座標系（Coordinate frame）**：定義位置數字相對哪個原點、軸向與尺度；缺一項就可能把接點放到別處。
- **原點（Origin）**：座標的零點；局部晶粒原點與封裝全域原點不是同一個位置。
- **旋轉約定（Rotation convention）**：說明角度正方向、旋轉中心與先旋轉或先平移，避免相同數字得到不同位置。
- **公差（Tolerance）**：尺寸或位置允許偏離名目值的範圍；它要連到單位、量測方法與放行規則。
- **跨檔身分（Cross-artifact identity）**：同一 pin、net 或 bump 在 LEF、GDS、SPICE、SystemVerilog 與 XML 中可被唯一對回。
- **往返檢查（Round-trip）**：資料匯入工具後再匯出，逐欄比較單位、座標、身分與版本是否被改寫。
- **KGD**：Known Good Die，組裝前已通過指定測試的晶粒；它仍可能在封裝組裝中受損。
- **實體資格驗證（Physical qualification）**：用封裝後樣品完成慢速、全速、可靠度與客戶條件驗收，不由 schema 代替。
- **W3C**：World Wide Web Consortium，制定 XML 等 Web 技術規範的國際組織；本文引用其 schema 驗證邊界。
- **CHI C2C**：Arm 的 Chip-to-Chip 連線協定；本文只把它當成架構案例中的連線層，不替設計資料背書。
- **DRM**：Design Rule Manual，設計規則手冊；記錄封裝或製程限制，PDF 存在不等於工具已能自動檢查。
- **PDK**：Process Design Kit，製程設計套件；把製造規則、模型與工具設定交給設計端。
- **SHA**：Secure Hash Algorithm 雜湊值；用固定字串辨識檔案內容是否完全相同，不代表內容本身正確。
- **DankaChiplet**：Thrace 的 3D-IC 架構工具；本篇只引用其 CDXML 產品自述，不把它當成跨工具測試。
- **Python**：本輪用來執行唯讀解析檢查的程式語言；版本與套件已記在稽核方法，方便重現結果。

### 三句話抓重點

- 小晶片能用共同介面傳資料，只證明連線契約的一部分；系統角色、設計資料與合規流程仍要另外交接。
- FCSA 已有正式架構與分級，OCP 也公開 CDXML 與 3DK 資料；但 TDK 明寫不定義工作流程，公開 XSD 也未全數通過解析。
- 所以目前可建立責任與驗證階梯，不能直接推成跨廠隨插即用、封測訂單、設備需求或任何台灣公司的收入。

### 為什麼重要

**這像蓋房子時的四份契約。** 電線插頭相同，只說設備能接上；房間用途、施工圖、材料表與
驗收程序仍要分開。少其中一份，兩個團隊就可能都「照規格做」，最後卻組不起來。

**機器可讀也有成熟度。** 一份 XSD 放上網站，只代表有人公開欄位規則。它還要能解析、能被
兩套獨立工具匯入、對同一測試資料給出一致結果，最後才輪到工廠與客戶簽核。

**這會改變研究順序。** 先問缺的是介面、角色、資料還是驗收，再找責任人。沒有跨工具與
工廠證據前，不把標準參與、產品頁或聯盟名單外推成訂單。

### 接下來怎麼追

- 先追 FCSA 新版本、實作清單與公開測試套件，確認符合性等級是否有獨立產品通過。
- 再追 CDXML／3DK 是否發布固定版本、完整範例與可執行 validator，四份 XSD 都要能解析與編譯。
- 接著找兩套獨立 EDA 工具匯入同一資料包，核對單位、版本、錯誤位置與通過結果是否一致。
- 最後查 foundry、OSAT、系統整合商與買方共同揭露的 tape-out、封裝簽核、測試與量產資格。

### 想一想

- 如果兩顆小晶片能互相傳資料，但散熱模型與測試接點資料不同，這能叫做隨插即用嗎？
- 同一份檔案能在一套工具開啟，另一套工具卻讀不到，問題在格式、版本、資料或工具哪一層？
- 聯盟成員很多，卻沒有共同測試輸入與通過紀錄時，能用成員數判斷商業成熟度嗎？

## 主張與證據帳本

`證實` 只代表指定文件或可重現檢查直接支持精確措辭。它不表示四層契約已被整合成同一套
量產流程，也不表示任何台灣公司已取得設計、封裝、測試或設備收入。

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: FCSA 1.0.0 定義共同系統拓撲、小晶片類型、功能與介面要求，並設置 level 0、level 1 與 full 三個符合性等級；同一規格說明它把介面描述映射到既有 protocol／transport，而不是另創一套實體互連標準
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-02-12
basis: S1 PDF file pp.13–20 定義架構層級、system／chiplet designer、類型與三個 compliance level；file pp.120–122 說明 interface mapping 與版本相容要求
boundary: FCSA 符合性只涵蓋 FCSA 規則，不替 UCIe、CDXML、3DK、EDA 匯入、封裝製程或客戶產品資格背書
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
claim: OCP 2025 3DK 教程把 3DK 拆成 CDK、ADK、MDK、TDK、package DRM 與 SI／PI design kit，並分別放入小晶片選擇、封裝規劃、系統規劃、效能分析、測試設計、繞線與 sign-off
supporting_source_ids: S3
contrary_source_ids:
as_of: 2025-01-21
basis: S3 PDF pp.2–3 直接列出六類套件與 architecture、design、sign-off 各階段用途
boundary: 教程是工作分解與提案，不證明六類套件已有同一版本、共同 validator、跨工具相同結果或量產客戶
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
claim: OCP 教程把 TDK 定義為 CDXML 的測試資料延伸，可攜帶接點結構、測試模式與接腳用途；同一頁明確說 TDK 不指定 workflow／methodology，也不另創 DFT 與測試技術
supporting_source_ids: S3
contrary_source_ids:
as_of: 2025-01-21
basis: S3 PDF pp.19–24 直接列出 TDK 的範圍、排除事項、工作階段資料變化與 XML 範例
boundary: TDK 有欄位草案不等於已有測試流程、共同向量、治具、設備程式、判定門檻或跨廠簽核
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
claim: 截至 2026-08-12，OCP FCSA 工作流列示 1.0.0 為 release、1.1.0 Alpha 0 為 for review，implementation 區只列 Arm Chiplet System Architecture，且頁面明示列名不構成 endorsement
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-08-12
basis: S2 Recent Deliverables 與 Implementations 表格直接列出版本、日期、狀態、單一實作與免責說明
boundary: 動態清單只反映已向工作流登錄的公開項目；不能證明沒有未登錄、保密或尚未發布的 FCSA 實作
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
claim: 對 ODSA-CDXML commit 5a725e45784471e7887d0359daaf4f80223fafb4 的四份 XSD 全數檢查時，mdk.xsd 與 tdk.xsd 可編譯，cdxml.xsd 與 adk.xsd 因未宣告 xs namespace prefix 而在 XML 解析階段失敗
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-08-12
basis: 完整母體 n=4、非抽樣故無抽樣 SE；Python 3.11.11 stdlib ElementTree 先解析，Python 3.12.13＋lxml 6.0.2 再編譯 XSD，兩種檢查都在 cdxml.xsd line 69、adk.xsd line 188 重現 unbound prefix，MDK／TDK 為 XSD_COMPILE_OK
boundary: 結果只適用該固定 commit 的公開原始檔；不排除私有修正版、工具前處理或後續 commit，亦不代表 CDXML 概念本身不可修復
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
claim: OCP Marketplace 目前列出 Thrace DankaChiplet 為使用 CDXML 與 IEEE 2416 的 3D-IC 架構工具，可探索 power、bump、substrate 與 interposer connectivity；頁面沒有發布第二套獨立工具對同一輸入的 conformance comparison
supporting_source_ids: S6
contrary_source_ids:
as_of: 2026-08-12
basis: S6 產品頁直接列出標準與可探索功能；同頁只有該產品說明與供應者，未提供共同測試向量、另一工具輸出或一致性報告
boundary: 這證實一項供應商自述的單工具能力，不證明 CDXML 完整匯入範圍、XSD 版本、結果正確性、跨工具互通或客戶量產
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
claim: 小晶片開放生態應分成連線介面、系統角色、設計資料與符合性流程四層契約；截至本輪公開證據，FCSA、CDXML／3DK 與單一工具各自跨過部分門檻，但尚不能組成可重現的跨工具、foundry／OSAT 與客戶端到端 conformance workflow
supporting_source_ids: S1,S3,S4,S5,S6,S7,S9
contrary_source_ids:
as_of: 2026-08-12
basis: S1 建立架構與 FCSA compliance；S3 建立 3DK 分工且明示 TDK 不含 workflow；S5 的固定版本稽核顯示公開 schema 尚未全數可編譯；S6 只到單工具產品自述；S7 仍以 committed to formally adopt 描述；S4 與 S9 分別把多供應商平台與第三方 chiplet 整合描述為進行中
boundary: 這是公開證據成熟度判讀，不是全產業不存在私有量產流程的斷言；也不把四層契約視為只能由單一標準組織提供
verification_needed: 固定版本 3DK bundle、完整 validator 與測試資料，由至少兩套獨立工具重現相同結果，再由 foundry／OSAT 與買方公布 tape-out、sign-off、qualification
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: unverified
status: active
claim: 兩套以上獨立 EDA 工具可匯入同一固定版本 CDXML／3DK package，完整保留單位與版本，並對相同正反測試資料輸出一致的錯誤位置與 pass／fail
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: 現有來源只有標準、教程、schema、單工具產品頁與採用承諾，沒有公開 cross-tool test vector、輸出差異與共同判定報告
boundary: 單一工具能開檔、聯盟成員名單、conference demo 或未公開客戶案例都不能替代跨工具重現
verification_needed: 兩家 EDA vendor 公布 tool version、schema SHA、input bundle、negative cases、units、diagnostics 與一致結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: unverified
status: active
claim: Foundry、substrate vendor 或 OSAT 已用同一 3DK conformance package 完成具名多供應商 chiplet 的 tape-out、封裝 sign-off、測試與客戶資格
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: Arm 公開平台案例只揭露 CSA、CHI C2C、參與者、製程與封裝方向，未揭露 CDXML／3DK 版本、tool import、共同測試資料與 sign-off 結果
boundary: 多供應商合作、晶片回片或介面互通不自動證明設計資料與製造規則已走完同一合規鏈
verification_needed: 買方與製造／封測方雙向文件列出 bundle version、EDA tool、DRC／thermal／SI-PI／TDK checks、waiver 與 qualification 結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: unverified
status: active
claim: 本 universe 的矽智財、封測或半導體設備公司已因 FCSA／CDXML／3DK conformance workflow 取得具名 design win、測試服務、設備訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: 現有標準與工具來源沒有連到 universe 公司、買方 BOM、qualification、設備型號、出貨分母或可辨識財務科目
boundary: 標準會員、先進封裝能力、一般 EDA／測試能力或產業相鄰關係都不能改寫成此主張已成立
verification_needed: 買方與公司雙向文件確認具名產品或服務、流程角色、客戶資格、部署／出貨數量、收入及毛利
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: OCP 的 CDX 模型標準化提案把小晶片交接拆成熱、機構、實體、功能、功耗、SI／PI、電氣、測試、安全與文件模型，並建議 Package LEF、GDS、SPICE 與 SystemVerilog 的 pin name 保持一致；機構資料另需表達 x、y、z、tolerance 與單位
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-08-14
basis: S11 PDF file pp.8–13 列出模型堆疊、Package LEF／GDS／OASIS 實體 pin geometry、跨 LEF／GDS／SPICE／SystemVerilog pin-name 一致性與 JEP30-P101 機構描述；file pp.17–18 說明 XML 可表達自訂 unit／data，機構資料含 x、y、z 與 tolerance
boundary: 這是 OCP 的 proposed standardization 與建議基線，不是正式 conformance release、工具測試、製造簽核或產品資格結果
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
claim: W3C 的 XML Schema Requirements 說明 schema validation 只檢查 schema 已表達的語法、結構與值限制；任意或複雜的應用限制仍需額外驗證，版本演進也會增加資料交換複雜度
supporting_source_ids: S12
contrary_source_ids:
as_of: 1999-02-15
basis: S12 的 Abstract、Conformance 與 Requirements 說明 schema 可表達 syntactic、structural、value constraints，應用若需要 arbitrary／complicated constraints 必須再做 additional validation，versioning 會使 data exchange 更複雜
boundary: 這是通用 XML schema 邊界，不是 CDXML 檔案、EDA 工具、封裝資料或任何小晶片產品的驗證結果
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
claim: OCP 的 CDX 模型提案明示 pre-tested KGD 仍可能在 assembly 中受損或變成 defective，組裝後仍需對個別小晶片與 die-to-die 介面做 slow-speed 與 at-speed 測試
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-08-14
basis: S11 PDF file pp.19–23 的 test models 段落說明 KGD 在組裝中仍可能受損，並列出 post-assembly 對 individual chiplets 與 D2D interfaces 的 slow-speed／at-speed test 要求及 machine-readable model 仍需文件與指南
boundary: 這是一般設計與測試指引，不證明任何具名晶粒、封裝批次、OSAT 流程或客戶產品已通過組裝後測試
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: inference
status: active
claim: 可交付的小晶片資料包至少需要一份十欄語意交接護照，把 bundle 身分、單位座標、跨檔身分、模式角落、模型邊界、schema 與語意 validator、跨工具往返差異、foundry／OSAT 簽核、組裝後實體測試及商業財務結果分開記錄
supporting_source_ids: S3,S5,S11,S12
contrary_source_ids:
as_of: 2026-08-14
basis: S3 顯示 3DK 是多資料包且 TDK 不定義 workflow；S5 顯示 schema 檔存在不保證全部可執行；S11 要求跨模型與跨檔交接且組裝後仍需測試；S12 限定 schema validation 只涵蓋已表達的限制，因此需把語法、工程語意、工具、製造、實體與商業證據分層
boundary: 十欄是本研究中心的稽核框架，不是 OCP、W3C、foundry、OSAT 或 EDA vendor 已共同採用的正式表單；也不表示任何產品已完成十欄
verification_needed: 固定版本資料包填滿十欄，由兩套獨立工具、foundry／OSAT 與買方共同公布差異、waiver、實體資格與量產結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 先分四層契約，才知道問題卡在哪裡

| 契約層 | 它回答什麼 | 本篇例子 | 通過前仍可能失敗 |
|---|---|---|---|
| 1. 連線介面 | 兩顆晶粒如何傳送位元、封包或協定 | UCIe、CHI C2C | 角色不一致、模型不足、工具讀不到 |
| 2. 系統角色 | 系統有哪些拓撲、哪種小晶片要有哪些功能與介面 | FCSA | 相同角色仍可能交付不同格式與版本 |
| 3. 設計資料 | 熱、電、機構、材料、封裝與測試資料怎麼交接 | CDXML、3DK | schema 可壞、單位可錯、工具結果可不同 |
| 4. 符合性流程 | 誰用哪一版資料、測哪些正反案例、誰簽名放行 | validator、cross-tool test、foundry／OSAT sign-off | 沒共同輸入與輸出，就無法重現通過結果 |

這四層彼此相連，卻不能互相代替。介面測試可證明特定速度與協定會通；FCSA 可約束角色與
必要介面；CDXML／3DK 則要把實際設計資料交給工具與工廠。

最後一層才把前三層變成可稽核流程。它需要固定版本、檔案雜湊、正反測試資料、預期錯誤、
工具版本、結果差異與簽核責任，而不只是規格名稱。

## 3DK 不是一個檔案，而是六種交接責任

| 資料包 | 主要內容 | 先交給誰 | 最容易被誤讀成 |
|---|---|---|---|
| CDK | 單顆小晶片的機構、電氣、功能與模型 | 系統架構、EDA、封裝整合 | 有產品型錄就等於資料完整 |
| ADK | 封裝組裝、尺寸、間距、堆疊與檢查規則 | 封裝設計、OSAT、EDA | 有 PDF 設計規則就能自動檢查 |
| MDK | 介電、損耗、導熱、膨脹與機械性質 | 熱、電磁與可靠度分析 | 有典型值就能涵蓋溫度與方向 |
| TDK | 測試接點、模式、方向與暫時接點 | DFT、測試工程、OSAT | 有欄位就等於已有測試流程 |
| DRM／PDK | 封裝堆疊、線寬、過孔與製程規則 | substrate vendor、foundry、OSAT | 規則存在就代表客戶已簽核 |
| SI／PI DK | 訊號與電源完整性的目標及模型 | EDA、IP、封裝與 sign-off 團隊 | 模擬通過就等於實體量產合格 |

同一個 System-in-Package 可能同時需要六種資料包。供應者、更新頻率、保密範圍與簽核者都
不同，因此「CDXML 支援」不能代表整個 3DK 已完整。

## 公開 schema 的可重現檢查

本輪固定在 ODSA-CDXML commit `5a725e45784471e7887d0359daaf4f80223fafb4`，不以之後會
變動的 `main` 代替版本。完整檢查四份 XSD，結果如下。

| 檔案 | 對應資料 | XML 解析 | XSD 編譯 | 本輪判讀 |
|---|---|---|---|---|
| `cdxml.xsd` | 小晶片共同資料 | 失敗 | 未進入編譯 | 第 69 行使用未宣告 `xs:` 前綴 |
| `adk.xsd` | 組裝規則 | 失敗 | 未進入編譯 | 第 188 行使用未宣告 `xs:` 前綴 |
| `mdk.xsd` | 材料資料 | 通過 | 通過 | 只證明 schema 可編譯，不證明範例與工具結果 |
| `tdk.xsd` | 測試資料 | 通過 | 通過 | 只證明 schema 可編譯；教程明寫不含 workflow |

方法是完整母體四份檔案，`n=4`，不是抽樣，所以沒有抽樣標準誤。第一步使用 Python
3.11.11 標準函式庫解析 XML；第二步使用 Python 3.12.13 與 lxml 6.0.2 編譯 XSD。

這個結果不能推成「CDXML 永遠不可用」。它只證明在指定公開 commit 中，檔案存在與四份
schema 都可被標準工具執行不是同一件事，也說明正式合規包必須固定版本並跑自動檢查。

## Schema 通過不是幾何正確：先鎖單位、座標與跨檔身分

W3C 對 XML schema 的邊界很清楚：驗證器只檢查 schema 已寫進去的語法、結構與值限制。
如果工程規則沒有被表達，檔案即使顯示通過，也不會自動證明尺寸、座標或另一份模型一致。

OCP 的 CDX 提案也不是只列 XML 欄位。它把熱、機構、實體、功能、功耗、SI／PI、電氣、
測試、安全與文件分成多種模型，建議 Package LEF、GDS、SPICE 與 SystemVerilog 的 pin name
一致，並要求機構資料能表達 x、y、z、公差與單位。這是跨檔語意問題，不是單一 XSD 能
獨自判定的產品資格。

### 單位不正規化，線性差 1,000 倍、面積差 1,000,000 倍

以下是匿名教學幾何，不對應任何產品。假設小晶片寬 20 mm、高 15 mm，接點 pitch 為
400 µm。先把長度統一成 µm，寬度才是 20,000 µm，寬度可容納的理想 pitch 間隔為 50。

| 算法 | 運算 | 結果 | 與正確值的差異 |
|---|---|---:|---:|
| 正規化後的線性比值 | 20,000 µm ÷ 400 µm | 50 | 基準 |
| 忽略單位的原始數字 | 20 ÷ 400 | 0.05 | 少 1,000 倍 |
| 正確面積 | 20,000 µm × 15,000 µm | 300,000,000 µm² | 基準 |
| 把 20 × 15 誤當 µm² | 20 µm × 15 µm | 300 µm² | 少 1,000,000 倍 |

50 只是理想線性間隔，不是可用 bump 數；邊界禁佈區、排列方向、pad 尺寸、逃線、冗餘與
良率都還沒進來。這個例子只示範量綱錯誤如何在第一步就放大，不能推成封裝密度。

### 同一座標數字，旋轉原點不同會落在另一處

再看一個匿名座標。局部 bump 位於（2, 3）mm，晶粒放置原點是全域（100, 50）mm。
若不旋轉，全域位置為（102, 53）mm；若依「繞局部原點逆時針 90°，再平移」約定，
局部座標先由（x, y）變為（−y, x），全域位置就成為（97, 52）mm。

| 解讀 | 全域 x | 全域 y | 相對不旋轉位置 |
|---|---:|---:|---:|
| 不旋轉後平移 | 102 mm | 53 mm | 基準 |
| 逆時針 90° 後平移 | 97 mm | 52 mm | Δx = −5 mm；Δy = −1 mm |

兩個答案相距 √26 = 5.099019514 mm。兩邊即使都忠實讀到數字 2 與 3，只要沒有共同記錄
座標系、原點、軸向、旋轉正方向、旋轉中心、鏡射、運算順序與單位，就不是同一個位置。

### XSD pass 檢查已宣告文法，不檢查所有工程語意

一個 validator 可以確認必填欄位存在、數字型別正確、值落在已宣告範圍；但它不會憑空知道
LEF 的 pin A 是否就是 SPICE 的 A、GDS 幾何原點是否與 XML 放置原點相同，或 400 的單位
究竟是 mm、µm 還是工具預設 database unit。這些規則必須另寫成語意檢查，並留下跨檔差異。

最基本的往返測試是：固定整包檔案與雜湊，工具 A 匯入再匯出，工具 B 做同樣動作；除了
比較 pass／fail，還要逐欄比較單位、座標轉換、pin／net／bump 身分、模型版本與 waiver。

### 組裝後仍要重驗，KGD 不是永久證書

OCP 提案明示，組裝前已測過的 KGD 仍可能在 assembly 中受損或變成 defective。完成封裝後，
個別小晶片與 die-to-die 介面仍要做 slow-speed 與 at-speed test。因此證據鏈不能在「供應者
交付 KGD」停止，更不能把機器可讀模型當成封裝後實體樣品已通過。

### 一份語意交接護照至少要有十欄

| 欄位 | 最少記錄 | 沒有它會混淆什麼 |
|---|---|---|
| 1. Bundle 身分 | release、commit、每檔 SHA、建立者、時間 | 同名不同版 |
| 2. 單位與座標 | 每量綱單位、database unit、座標系、原點、旋轉、鏡射、公差 | 數字相同就等於位置相同 |
| 3. 跨檔身分 | pin、net、bump、die 與 model 的唯一鍵及 mapping | 各檔同名或異名無法對回 |
| 4. 模式與角落 | power state、test mode、PVT、頻率、方向 | 典型值冒充所有條件 |
| 5. 模型邊界 | fidelity、適用範圍、缺省值、已知限制 | 模型存在冒充物理真實 |
| 6. Schema 與語意檢查 | XSD 結果、跨欄與跨檔規則、正反案例 | 文法通過冒充工程正確 |
| 7. 跨工具往返 | 工具版本、匯入匯出差異、診斷、允許偏差 | 單工具開檔冒充互通 |
| 8. 製造與封測簽核 | PDK／ADK／MDK／TDK 版本、DRC、SI／PI、熱、waiver、簽名 | 模擬通過冒充可製造 |
| 9. 組裝後實體資格 | 樣品、批次、slow／at-speed test、可靠度、失效與重測 | KGD 冒充封裝後合格 |
| 10. 商業與財務 | 客戶產品、量產數、價格、收入、成本與毛利分母 | 技術活動冒充材料性 |

十欄不是新的產業標準，而是研究中心把「讀得到、對得上、簽得過、量得出、賣得掉」拆開
稽核的護照。任何一欄空白都不必否定技術，但必須停止跨越該欄的外推。

### 多空小作文：同一張護照，正反敘事才可比較

**偏多版本。** 固定 bundle 讓供應者與工具共用身分、單位與座標，跨工具往返差異收斂，
foundry／OSAT 的 waiver 與組裝後測試能沿同一鍵回溯；若重工、驗證週期與客戶導入時間同步
下降，資料 authoring、validator、封裝整合與測試工作可能形成可收費的產品或服務。

**偏空版本。** Schema 雖發布，各工具仍靠私有 mapping 修正單位與座標，pin 身分需人工
對照，組裝後失敗無法回連模型版本；共同格式反而只增加轉檔與維護層，生態成員、demo 或
KGD 數量都無法轉成可重現量產與財務貢獻。

兩個版本共用同一組反證：第二套獨立工具的固定輸入輸出、跨檔差異、foundry／OSAT waiver、
組裝後 slow／at-speed 測試、客戶資格與財務分母。偏多不能只靠規格發布，偏空也不能只靠
公開草案尚未完整就宣稱路線失敗。

### 樣本、誤差與可外推範圍

單位案例是 1 組匿名幾何、2 條固定解讀路徑；座標案例也是 1 組匿名位置、2 條固定轉換路徑。
這些是決定性單位換算與幾何運算，不是抽樣，因此不報抽樣 SE 或 t 值。Python Fraction／math
與獨立 awk 公式逐項得到相同的 50、0.05、1,000 倍、300,000,000 µm²、1,000,000 倍、
（102, 53）、（97, 52）與 5.099019514 mm。

本輪具名產品、工具往返、foundry／OSAT sign-off、組裝批次、客戶資格與財務觀測均為 N=0。
OCP 與 W3C 文件只建立方法與標準邊界，不是產品或量產樣本；上述算術也不能估計實際 bump
良率、錯位率、測試通過率、重工成本、收入或毛利。

## 用六關判斷是否真的能跨公司交接

| 關卡 | 最少要看到什麼 | 本輪位置 | 仍不能推成 |
|---|---|---|---|
| 1. 名詞與規格發布 | 角色、欄位、版本與適用範圍 | FCSA 1.0 已發布；3DK 有教程 | 工具已實作 |
| 2. schema 可執行 | 全部 XSD 可解析、編譯，正反範例可驗證 | 四份中兩份通過、兩份失敗 | 資料語意正確 |
| 3. 單工具匯入 | 具名工具、版本、輸入與功能範圍 | DankaChiplet 有 CDXML 產品自述 | 跨工具一致 |
| 4. 跨工具重現 | 兩套獨立工具對同一資料給出一致結果 | 待驗證 | 工廠可製造 |
| 5. 製造與封測簽核 | foundry／OSAT 用同一包完成設計與測試放行 | 待驗證 | 客戶已量產 |
| 6. 客戶與財務 | 具名產品資格、量產數量、服務收入與毛利 | 待驗證 | 全產業等比例受惠 |

第二關不是挑語法小錯。若公開版本、namespace、單位或 include 關係無法固定，後續工具就
可能各自修補，最後產生看似都成功、實際版本不同的結果。

第四關是最重要的分水嶺。跨工具測試要公開相同輸入、預期錯誤、版本與輸出差異；只展示
一張工具畫面或一個 conference demo，仍無法判斷另一套工具會不會得到相同結論。

## 誰負責交接，誰不能替別人背書

| 角色 | 應交付或確認 | 不能單獨背書 |
|---|---|---|
| 系統設計者 | FCSA system type、拓撲、chiplet type、profile 與整體驗收目標 | 單顆晶粒的模型完整性 |
| 小晶片／IP 供應者 | CDK、介面版本、功能模型、功耗熱與測試資料 | 封裝製程與客戶量產資格 |
| Foundry／substrate vendor | PDK／DRM、材料與製程視窗、可製造性規則 | 多供應商系統功能正確 |
| OSAT | ADK、組裝、測試接取、可靠度與封裝 sign-off | 晶片 IP 的內部功能與軟體 |
| EDA／測試工具商 | 匯入、validator、診斷、版本追蹤與結果重現 | 客戶採用、訂單與收入 |
| 系統整合商／買方 | 最終工作負載、可靠度、供應鏈與產品 qualification | 上游每個模型的原始正確性 |

責任鏈的價值在於能追錯。熱模擬失敗時，先看 MDK 的材料條件、CDK 的功耗邊界、封裝堆疊
與 solver 版本；測試接點失敗時，則要追 TDK、ADK、治具與測試程式。

若所有問題都只寫成「小晶片不相容」，研究就無法辨識是介面、角色、資料、工具、製造還是
客戶驗收出錯，也無法判斷哪個族群真正增加工作量。

## 這篇對個股判斷的用處與界線

本篇先建立三個搜尋入口：矽智財與設計服務要查資料 authoring 與 tool validation；封測要查
ADK／TDK、封裝 sign-off 與客戶資格；設備要查共同測試方法是否改變量測或測試機需求。

目前沒有任何入口跨到 universe 公司。沒有買方、具名產品、流程版本、qualification、數量與
財務分母，就只保留族群研究路由，不建立受惠、排名或財務材料性。

標準若成功，價值也未必只新增。共同格式可能減少重工與客製服務，也可能把驗證工作移到
EDA、IP、OSAT 或系統整合商之間；必須先量出誰少做、誰多做，才能談收入方向。

## 來源

<!-- research_source
source_id: S1
role: standard
source_kind: document
publisher: Open Compute Project Foundation / Arm Ltd.
independence_group: ocp-fcsa-standard
title: Foundation Chiplet System Architecture 1.0.0
published_at: 2026-02-12
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/fcsa-1-0-0-pdf
locator: PDF file pp.13–20 的 sections 1–2 與 compliance levels；file pp.120–122 的 interface mapping and compatibility
limitation: 規格由 Arm 主導並在 OCP 發布；定義 FCSA 架構與符合性，不提供 CDXML／3DK tool import、foundry／OSAT sign-off 或客戶量產結果
-->

<!-- research_source
source_id: S2
role: standard
source_kind: living_index
publisher: Open Compute Project Foundation
independence_group: ocp-fcsa-standard
title: FCSA workstream deliverables and implementations index
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/wiki/Server/OCE/FCSA
locator: 2026-08-12 的 Recent Deliverables 顯示 1.0.0 release、1.1.0 Alpha 0 for review；Implementations 只列 ACSA 並附非 endorsement 說明
limitation: 動態索引可隨時更新，且只含向工作流登錄的項目；不排除未公開或未登錄實作
-->

<!-- research_source
source_id: S3
role: standard
source_kind: document
publisher: Open Compute Project Foundation
independence_group: ocp-3dk-contributors
title: 3D-IC Design Kits for Drop-in Chiplets: MDK, ADK, TDK
published_at: 2025-01-21
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://drive.google.com/file/d/10QpQ-o-SX10qFPyrVmgM3wnWvevbemeD/view?usp=drive_link
locator: PDF pp.2–3 的 3DK 分工與應用；pp.19–24 的 TDK scope、非 workflow 聲明、資料變化與 XML 範例
limitation: OCP 贊助教程由 3DK 貢獻者製作，包含提案與示例；不等同正式版本、跨工具 conformance report 或量產資格
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: document
publisher: Arm
independence_group: arm-issuer
title: Arm Chiplet System Architecture Makes New Strides in Accelerating the Evolution of Silicon
published_at: 2025-01-21
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://newsroom.arm.com/blog/arm-chiplet-system-architecture-accelerating-evolution-of-silicon
locator: Advancing the chiplet ecosystem、first public specification 與 ADTechnology／Samsung／Rebellions platform 段落
limitation: Arm 自述 CSA 生態與多供應商平台；未揭露 CDXML／3DK 版本、EDA import、共同測試向量、foundry／OSAT sign-off 或客戶財務
-->

<!-- research_source
source_id: S5
role: standard
source_kind: document
publisher: Open Compute Project Foundation
independence_group: ocp-cdxml-standard
title: ODSA-CDXML repository snapshot at commit 5a725e45784471e7887d0359daaf4f80223fafb4
published_at: 2025-02-06
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://github.com/opencomputeproject/ODSA-CDXML/tree/5a725e45784471e7887d0359daaf4f80223fafb4
locator: cdxml.xsd、adk.xsd、mdk.xsd、tdk.xsd 全四檔；commit SHA 固定版本，解析與編譯方法列於 C5 basis
limitation: 公開 repository snapshot 不是正式 release bundle；本輪結果只適用該 commit，不排除私有修正、工具前處理或後續版本
-->

<!-- research_source
source_id: S6
role: competitor_primary
source_kind: living_index
publisher: Thrace Systems / Open Compute Project Marketplace
independence_group: thrace-eda-vendor
title: DankaChiplet Platform for 3D-IC Architects listing
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/chiplets/57/thrace-systems-dankachiplettm-platform-for-3d-ic-architects
locator: 2026-08-12 產品說明列出 CDXML、IEEE 2416、power analysis、bump planning、substrate 與 interposer connectivity
limitation: 供應商產品自述沒有 schema version、測試輸入、第二套工具輸出、客戶 qualification 或 production deployment
-->

<!-- research_source
source_id: S7
role: competitor_primary
source_kind: living_index
publisher: Siemens EDA
independence_group: siemens-eda-vendor
title: Siemens 3D IC Design and Packaging Solutions
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://eda.sw.siemens.com/en-US/eda-cloud-solutions/ic-packaging/3d-ic-design/
locator: FAQ 的 design-kit integration、CDX／OCP 3DK initiatives 與 committed to formally adopt in tools and workflows 段落
limitation: 頁面使用採用承諾措辭，未提供完成匯入的 CDXML／3DK 版本、cross-tool test 或 foundry／OSAT qualification
-->

<!-- research_source
source_id: S8
role: standard
source_kind: living_index
publisher: Open Compute Project Foundation
independence_group: ocp-cdxml-standard
title: ODSA-CDXML repository main branch index
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://github.com/opencomputeproject/ODSA-CDXML
locator: 2026-08-12 可見 CDK checklist、CDXML 文件、四份 XSD、validator example 與 repository history
limitation: main branch 會變動，只供監測新 commit、tag、release 與修正；主張重算必須固定 SHA
-->

<!-- research_source
source_id: S9
role: other_primary
source_kind: document
publisher: Open Compute Project Foundation
independence_group: ocp-foundation
title: The OCP Open Chiplet Economy Marketplace Opens its Doors
published_at: 2024-10-15
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/blog/the-ocp-open-chiplet-economy-marketplace-opens-its-doors
locator: 第三方 known-good dies 尚不 straightforward，以及 3D-IC design kits、testing 與 EDA integration 為 near-term challenge 的段落
limitation: OCP 對自有 marketplace 與工作流的進度說明；不是獨立工具 benchmark、客戶採購資料或 2026 年完整產業普查
-->

<!-- research_source
source_id: S10
role: standard
source_kind: living_index
publisher: Open Compute Project Foundation
independence_group: ocp-open-chiplet-economy
title: Open Chiplet Economy workstreams and recordings index
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/wiki/Server/OpenChipletEconomy
locator: 2026-08-12 顯示 CDX／3DK／MDK、Chiplet Systems、FCSA、Chiplet PoC 與 Virtual Chiplet Ecosystems 等工作流入口
limitation: 工作流存在不代表 deliverable、實作、合規或量產已完成；只供後續定位正式附件與錄影
-->

<!-- research_source
source_id: S11
role: standard
source_kind: document
publisher: Open Compute Project Foundation
independence_group: ocp-cdx-model-proposal
title: OCP ODSA - CDX Proposed Standardization of Chiplet Models for Heterogeneous Integration
published_at: 2021-11-16
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.opencompute.org/documents/ocp-odsa-cdx-proposed-standardization-of-chiplet-models-for-heterogeneous-integration-2-pdf?ga4-reseller=1620
locator: PDF file pp.8–13 的 model stack、physical pin geometry、跨 LEF／GDS／SPICE／SystemVerilog pin identity 與 JEP30-P101；pp.17–18 的 XML unit／x-y-z／tolerance；pp.19–23 的 KGD 組裝風險與 post-assembly slow／at-speed test
limitation: OCP PDF 本身未標示發行日，published_at 採同題論文在 IEEE 3DIC 2021 官方 program 的發表日；文件是 proposed standardization 與設計指引，沒有正式 release tag、跨工具 conformance、foundry／OSAT sign-off、具名產品資格或財務結果
-->

<!-- research_source
source_id: S12
role: standard
source_kind: document
publisher: World Wide Web Consortium
independence_group: w3c-xml-schema
title: XML Schema Requirements
published_at: 1999-02-15
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.w3.org/TR/NOTE-xml-schema-req
locator: Abstract、Conformance 與 Requirements 對 schema constraint、additional validation 與 versioning 的邊界
limitation: 通用 XML schema 要求文件不是 CDXML、EDA、封裝或小晶片產品驗證；只用來界定 schema pass 能與不能證明的性質
-->

## 族群影響

<!-- impact
group_id: ipdesign
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-31
rationale: CDK／CDXML authoring、介面與系統角色對齊、tool import 與版本管理，是矽智財與設計服務的第一個查核入口
evidence_boundary: 本輪沒有 universe 公司具名 FCSA／CDXML／3DK 產品、客戶 qualification、design win、收入或毛利；只建立研究問題
-->

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-31
rationale: ADK、MDK、TDK、封裝 sign-off 與測試接取可能改變 OSAT 的資料交接與驗收責任，是封測族群的查核入口
evidence_boundary: 沒有 universe OSAT 與買方雙向揭露固定 bundle、EDA tool、封裝資格、量產數量、服務價格或財務貢獻
-->

<!-- impact
group_id: semiequip
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: 若共同 TDK 與 conformance plan 落地，才進一步查量測、測試與失效分析設備是否新增具名測項或產能需求
evidence_boundary: TDK 現有公開資料明示不定義 workflow；目前沒有共同 test vector、設備程式、產能分母、訂單或收入
-->

## 監測器

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C4,C7,C8
metric: FCSA 是否增加獨立實作、固定 compliance test suite、指定符合性等級與可重現通過結果
source_ids: S1
watch_source_ids: S2
frequency: event_driven
frequency_detail: FCSA workstream 新 release、implementation 或 compliance deliverable 後複核
next_check: 2026-08-24
trigger: implementation 清單新增非 Arm 的具名產品，並同時公開 FCSA version、level、test suite、輸入與通過結果
invalidation: 若後續規格取消分級、實作無法引用固定版本，或公開測試顯示角色與介面規則不足以重現，則重寫 C1 與四層契約的架構層
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C2,C3,C5,C6,C7,C8,C9,C10
metric: CDXML／3DK 是否形成固定 release bundle、全 XSD 自動檢查、跨工具結果與 foundry／OSAT／買方共同簽核
source_ids: S3,S5,S9
watch_source_ids: S6,S7,S8,S10
frequency: monthly
next_check: 2026-08-31
trigger: 固定 tag 與 SHA 下四份 XSD 全數可編譯，至少兩套獨立工具對共同正反案例給出一致結果，並有 foundry／OSAT 或買方公開 sign-off
invalidation: 若標準工作流改採另一格式、私有 mapping 成為必要中介，或跨工具差異無法收斂，則 CDXML／3DK 不得被描述為共同 conformance layer
-->

## 目前不能下的結論／待驗證

- 不能把 FCSA compliance、UCIe interoperability 與 CDXML／3DK conformance 當成同一張證書；三者檢查的對象不同。
- 不能由 OCP 已公開 schema，推成四份 XSD 都可執行；固定 commit 的完整檢查已顯示兩份解析失敗。
- 不能由 DankaChiplet 或任何單一工具宣稱支援 CDXML，推成兩套 EDA 工具對同一資料會得到相同結果。
- 不能把 Arm 多供應商平台的 CSA／CHI C2C 敘述，改寫成已採用 CDXML／3DK 或已通過 foundry／OSAT 共同簽核。
- 不能由公司加入聯盟、具備先進封裝、EDA、測試或設備能力，推導具名 design win、訂單、收入、毛利或投資建議。
