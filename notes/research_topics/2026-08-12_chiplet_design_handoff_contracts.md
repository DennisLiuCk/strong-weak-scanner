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
<!-- transition
date: 2026-08-23
from: triaged
to: triaged
reason: added_fcsa_alpha_compositional_trust_and_runtime_revalidation_without_thesis_clock_refresh
evidence: sources:S13
-->
<!-- transition
date: 2026-08-24
from: triaged
to: triaged
reason: added_pre_and_post_silicon_interoperability_scope_passport_without_thesis_clock_refresh
evidence: sources:S14,S15
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
- **Alpha／Beta／Release**：規格成熟度階段；Alpha 可含明確規則，也可以公開發行，但仍在早期審閱，不能等同正式穩定的合規基線。
- **信任根（Root of Trust，RoT）**：負責保護身分、量測或安全決策的最小可信基礎；不是一句「有安全功能」的行銷名稱。
- **CRoT-A**：Chiplet Root of Trust for Attestation；留在每顆小晶片內，保管晶粒身分並產生韌體、生命週期與除錯狀態的可驗證證據。
- **System RoT**：系統信任根；收齊各顆晶粒證據後，判斷實際組合是否符合允許的清單與政策。
- **證明（Attestation）**：用受保護的身分與量測，回答「現在這顆晶粒是誰、跑哪版程式、處於什麼狀態」；它不是永久有效的通行證。
- **系統清單（System Manifest）**：記錄預期晶粒身分、角色、數量、位置、拓撲與系統信任根的受保護名冊。
- **生命週期（Lifecycle）**：晶粒從製造、寫入安全資料、封裝整合、OEM 佈署、運作到回收／報廢的階段與狀態。
- **失敗關閉（Fail closed）**：證據缺失、過期或不符時，先拒絕建立高保證信任域；若容許降級，仍要隔離並留下可見狀態。
- **Security Platform（安全平台）**：System RoT 接受晶粒身分、證據、拓撲與政策綁定後，跨多顆晶粒建立並持續維護的系統安全域。
- **Declaration（宣告）**：FCSA 規格用來引入概念、術語或資料結構的規範性內容類別；它不描述行為，行為由 Rule 說明。
- **前矽模擬（Pre-silicon simulation）**：晶片製造前，用數位模型、向量與驗證環境檢查狀態機、介面和協定；它看不到完整實體通道與製程變異。
- **實體上電（Live／post-silicon）**：晶片製造並封裝後，以真實矽晶粒建立連線；它比純模擬多跨過實體存在，但通過範圍仍取決於公開測項。
- **PHY**：Physical Layer，實體層；把邏輯資料轉成晶粒間可傳送的電氣訊號，包含數位邏輯與需真實矽驗證的電氣／類比前端。
- **Adapter Layer**：介接層；位於 PHY 與上層協定之間，處理封包格式、CRC、重送、電源與錯誤訊息等功能。
- **RDI**：Raw Die-to-Die Interface，PHY 與 Adapter Layer 之間的標準介面；到 RDI 只代表測試邊界抵達 PHY 上緣。
- **FDI**：Flit Die-to-Die Interface，Adapter Layer 與主機側協定邏輯之間的介面；抵達 FDI 才把 Adapter Layer 納入同一測試範圍。
- **DUT**：Device Under Test，受測裝置；測試報告若不說哪一端是 DUT、另一端是參考模型或晶粒，就很難重現結果。
- **Golden die（黃金晶粒）**：符合性測試用的參考晶粒；若要讓結果可重現，報告需記錄其版本、封裝、功能與測試方法，不能只靠「標準晶粒」名稱背書。
- **ACTIVE**：UCIe 連線訓練完成、可開始傳資料的狀態；進入 ACTIVE 是一個必要里程碑，不等於所有協定、錯誤情境與長時間可靠度都通過。
- **UCIe-S**：UCIe standard package 的實體路徑；本篇 16G 現場展示只直接證實這一種路徑，不替 advanced package 背書。
- **BER**：Bit Error Rate，位元錯誤率；要連同測試位元數、時間、條件與零錯誤時的信賴上限閱讀，不能只寫「無錯」。
- **Cameron Creek**：Intel／Cadence 於 2026 Chiplet Summit 展示所用的名稱；活動頁只稱 test chip，未識別為客戶產品或量產平台。
- **Gbps／GT/s**：Gbps 是每秒十億位元，GT/s 是每秒十億次傳輸；兩者都要搭配 lanes、方向與編碼，不能只看數字比較完整系統吞吐。
- **x64**：本文 Cadence 模型的 64-lane 寬度標記；它描述模型配置，不等於活動回顧已公開 live demo 的 lane count。

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

<!-- research_claim
claim_id: C15
label: verified
status: active
claim: FCSA 1.1.0 Alpha 0 的 version history 記錄該版於 2026-07-23 發布；同一文件把 Declaration 與 Rule 定義為規範性內容，但只承諾規格進入 beta 後，同一 content item 的 identifier 才會在後續版本保持相同
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-07-23
basis: S13 PDF file p.7 的 version history 列出 2026-07-23 Alpha 0，file p.11 說明 Declaration／Rule 為 normative，並只在 reaches beta 後承諾 identifier 跨後續版本維持相同
boundary: Alpha 文件內可以有規範性規則，不代表 1.1.0 已成為正式穩定 release、每段安全正文都是 Rule、規則編號已鎖定、測試套件完成、產品合規或客戶採用；本輪也沒有觀察到實際 identifier 已變更
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C16
label: verified
status: active
claim: FCSA 1.1.0 Alpha 0 描述參與 attested composition assurance 的每顆小晶片具有 CRoT-A；開機時 System RoT 挑戰各 CRoT-A，驗證證據新鮮度、簽章、憑證鏈、撤銷、回滾與 manifest binding，並核對實際晶粒集合、角色、位置及拓撲後，才授權建立 Security Platform
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-07-23
basis: S13 PDF file pp.165–167 的 sections 9.1.4.1–9.1.4.5 定義 Security Platform、System RoT、CRoT-A 的本地證據責任，以及 boot 時的 challenge、evidence validation、authorized composition check 與 platform formation
boundary: 這是 Alpha 架構描述與資訊內容，不是實作測試、攻擊驗證、產品安全證明、第三方認證或跨廠 interoperability 結果
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C17
label: verified
status: active
claim: FCSA 1.1.0 Alpha 0 把組合信任定義為持續狀態，而非只在開機檢查一次；reset、warm reset、晶粒故障、debug unlock、韌體更新、recovery 或其他會影響 Security Platform 的狀態變化，都會觸發 System RoT 重新驗證
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-07-23
basis: S13 PDF file p.167 section 9.1.4.5 直接列出 runtime 期間 System RoT 維護 system trust model，以及 reset、warm reset、chiplet fault、debug unlock、firmware update、recovery 與其他狀態變化的 revalidation trigger
boundary: 規格列出重新驗證事件，不提供任何產品的偵測延遲、誤報漏報、恢復時間、效能成本、field incident 或通過率
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C18
label: verified
status: active
claim: FCSA 1.1.0 Alpha 0 展示的典型小晶片系統生命週期包含 manufacturing、chiplet provisioning、integration provisioning、OEM provisioning、operation 與 disposal 六階段；每顆晶粒各有自己的 lifecycle state，System RoT 再由多顆證據推導產品定義的 system state，兩者不必相同
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-07-23
basis: S13 PDF file pp.167–168 的 Figure 9.3 與 Table 9.2 列出六階段、stakeholder 與工作；file p.168 說明 per-chiplet lifecycle state 與 product-defined system security state 不需一一相同，並指出 die facility 與 SiP integration facility 的 provisioning 分工形成新攻擊面
boundary: 六階段是規格展示的 typical activity model，不是不可增減的完整 system security state machine，也不等於六個線性認證閘門或任何 foundry、OSAT、OEM 已佈署的流程
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C19
label: inference
status: active
claim: 研究小晶片系統安全時，至少需要一份十欄組合信任護照，把規格版本、預期組合、每顆晶粒身分、韌體量測、生命週期與除錯狀態、證據新鮮度、角色位置拓撲、控制平面與政策綁定、執行期重新驗證，以及各階段保管責任分開記錄
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-08-23
basis: C16 顯示本地證據不能替代系統組合判定；C17 顯示信任會因執行期事件失效而需重驗；C18 顯示晶粒與系統狀態、六個生命週期階段及 stakeholder 不相同，因此本研究中心將必要證據整理為十個不可互換欄位
boundary: 十欄護照是研究中心依單一 OCP／Arm 規格消息鏈建立的查核框架，不是 FCSA 正式表單、產業標準、測試套件、認證或已被供應商共同採用的產品格式
verification_needed: 固定 release 與 test suite 下，由多家晶粒、整合、OEM 與獨立驗證方公布同一 manifest、attestation、事件重驗、失敗處置及資格結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C20
label: unverified
status: active
claim: FCSA 1.1 的組合信任架構已有非 Arm 的獨立產品實作，並以固定版本與測試套件完成跨廠晶粒整合、客戶 qualification、production deployment、field reliability，以及可辨識的台灣供應商訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-23
basis: S2 於 2026-08-12 登錄的公開 implementation snapshot 只列 Arm Chiplet System Architecture 並明示非 endorsement；scan-2026-08-23-fcsa-alpha-compositional-trust 再查同一 living index 仍未找到第二項列名，S13 也沒有具名晶粒組合、test result、customer acceptance、field data 或財務共同鍵
boundary: 公開清單未列出不代表私有或未登錄實作不存在；但聯盟參與、規格規則、一般 secure boot／attestation 能力或供應鏈鄰接，都不能替代此主張所需的端到端證據
verification_needed: 非 Arm 實作者、整合方與買方雙向公布固定 FCSA 1.1 release／level、manifest、CRoT-A／System RoT 測試、runtime revalidation、qualification、部署分母、field 結果及財務對帳
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C21
label: verified
status: active
claim: Cadence 2024 白皮書記錄一組 Intel 向量與 Cadence UCIe advanced-package PHY 模型的前矽互通：環境使用 x64 lanes、在 16 Gbps 操作，找出 lane check 順序、狀態跳過、PLL 等待時間與 eye-sweep 次數不一致，調整向量與環境後兩端建立連線並進入 ACTIVE
supporting_source_ids: S15
contrary_source_ids:
as_of: 2024-08-02
basis: S15 的 UCIe Verification Challenges、Simulation Logistics、Simulation - Interoperability over UCIe 與 Conclusion 逐項記錄 x64 model、16 Gbps、四類不一致、修正及 ACTIVE 結果
boundary: 這是 Cadence 撰寫的前矽案例，不是獨立 benchmark；向量曾加入 delay／response、修正 state sequence 與 eye-sweep 次數，D2C point test 也曾暫時關閉，初始範圍只到 RDI 且沒有公開完成 controller／Adapter／FDI／protocol 下一步、真實類比前端、封裝通道、BER、溫壓角落、產品 qualification、部署或財務結果
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C22
label: verified
status: active
claim: UCIe Consortium 2026 Chiplet Summit 紀錄顯示，Cameron Creek 現場展示以獨立設計的 Intel 與 Cadence 晶粒、16G UCIe-S PHY 完成跨供應商實體互通測試
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-03-05
basis: S14 的 live demonstration 段落直接列出 Cameron Creek、independently designed Intel and Cadence chiplets、16G UCIe-S PHY IP 與 successful UCIe Interoperability Testing
boundary: 活動回顧沒有揭露 UCIe revision、lane count、封裝與通道、traffic／protocol、運作時間、錯誤或 BER、電壓溫度、樣品與批次、Adapter Layer 覆蓋、CDXML／3DK、foundry／OSAT、客戶 qualification、量產或財務結果；同頁的 UCIe 3.0 48／64 GT/s 是另一段規格敘述，不能補成展示版本
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C23
label: inference
status: active
claim: 研究小晶片互通時，應用一份八欄「互通範圍護照」分開記錄受測物件與版本、證據階段、參與角色、層與介面邊界、速率與實體路徑、刺激與協定、樣本環境及錯誤覆蓋、下游交付與資格；前矽模擬、實體 PHY 連線、完整 Adapter／protocol、設計資料交接及客戶 qualification 不能共用一個 pass 標記
supporting_source_ids: S14,S15
contrary_source_ids:
as_of: 2026-08-24
basis: S15 把 electrical／mechanical、PHY、RDI、Adapter、FDI、protocol 與 golden-die compliance 拆開，並顯示前矽向量能找出數位狀態與時序差異但類比前端需實體矽；S14 又只直接證實 16G UCIe-S 的現場實體連線，因此本研究中心把每筆互通證據整理為八個不可互換欄位
boundary: 八欄護照是研究中心的證據稽核框架，不是 UCIe、OCP、Intel 或 Cadence 的官方表單；它不否定未公開測試，也不因欄位完整就自動證明 CDXML／3DK、foundry／OSAT、產品量產或財務材料性
verification_needed:
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

## 同樣叫互通，模擬與實體上電不是同一張證書

把小晶片互通想成兩家公司通電話。模擬可以先檢查雙方是否依正確順序問候、等待與回覆；實體
上電則證明真的有兩支電話、線路接得起來。但一通電話接通，不代表兩家公司接著交換的施工圖、
材料表、驗收表與付款資料也相容。UCIe 連線、FCSA 系統角色、CDXML／3DK 設計資料與產品資格
就是不同張證書。

### 先問證據在哪一層，不要先問有沒有 pass

| 證據層 | 白話問題 | 可能暴露的失敗 | 還不能替代 |
|---|---|---|---|
| 1. 規格與解讀 | 兩邊讀的是哪一版、同一條規則嗎？ | 名詞、狀態與欄位理解不同 | 任何實作已通過 |
| 2. 前矽模擬 | 數位模型按共同刺激能走完狀態嗎？ | 順序、握手、等待、通道檢查與錯誤處理差異 | 真實電壓、通道、封裝與製程變異 |
| 3. 實體 PHY 連線 | 真實晶粒能訓練並建立電氣連線嗎？ | 類比前端、實體通道與封裝才會出現的問題 | Adapter、所有 protocol、長時間與故障覆蓋 |
| 4. Adapter／protocol／traffic | CRC、重送、傳輸單元（flit）、協定與工作負載是否一起通？ | 上層格式、錯誤注入與服務行為差異 | 設計資料、製造與封測簽核 |
| 5. 設計資料與製造交接 | 同一 bundle 能被工具、foundry 與 OSAT 重現嗎？ | 單位、座標、模型、版本、waiver 與測試接取差異 | 客戶產品已接受與量產 |
| 6. 客戶資格與商業化 | 具名產品在共同條件下能否持續交付？ | 可靠度、良率、供應、成本與實際服務問題 | 其他產品或全產業等比例受惠 |

前四層拆的是介面測試範圍，後兩層是設計交付與商業門檻，不是 UCIe protocol stack。這六層是
研究中心的閱讀順序，也不是 UCIe 官方成熟度等級。前一層通常能降低下一層風險，卻不會自動讓
下一層畢業；同一個「interoperability」字樣也可能只覆蓋其中一格。

### Cadence 案例：模擬最有價值的地方，是提早看見不一致

Cadence 2024 白皮書回顧 Intel 與 Cadence 的前矽合作。測試使用 Cadence advanced-package PHY
的 x64 model、Intel 提供的向量與 16 Gbps 操作；向量推進過快時，Cadence 端還沒完成目前狀態，
兩邊便失去同步。實際找到的問題包括通道檢查（lane check）順序、非法跳過狀態、鎖相迴路
（PLL）鎖定等待不足、眼圖掃描（eye-sweep）步數及重複次數不同。

團隊加入等待與必要回覆、修正向量及檢查順序後，兩端能建立連線並進入 `ACTIVE`。這是有用的
工程證據，因為問題在晶片製造前就被看見；它也不是一張無條件證書。白皮書同時記錄資料相對
時鐘（D2C）取樣點測試曾暫時關閉，而且初始 PHY interop 的邊界只到 RDI。文件把加入 controller
寫成下一步；若完成，測試範圍才會經過 Adapter Layer 的側帶控制（sideband）、主資料通道
（mainband）、CRC 與重送，延伸到主機側 FDI，但頁面沒有公開這一步的完成結果。

來源還特別把矽的角色說清楚：PHY 的數位邏輯、Adapter 與 protocol 可以在前矽階段先測，
電氣／類比前端才依賴真實矽。換句話說，模擬通過能提高數位實作信心，不能量到
真實封裝通道的 BER、電壓／溫度角落或長時間可靠度。

### 現場 demo 前進一格，仍要打開測試包絡

另一份同樣由 Intel／Cadence 參與的 UCIe Consortium 2026 活動回顧，則把公開證據帶到實體層：
Cameron Creek 現場連接獨立設計的
Intel 與 Cadence chiplet，使用 16G UCIe-S PHY 完成跨供應商互通測試。這比紙上規格、模擬或
tape-out 多證明一件事——真實晶粒確實建立過指定實體連線。

兩份來源沒有共同的 chip／IP revision、輸入、test-plan version 或結果 ID，因此不能把 2024
模型與向量案例、2026 test chip 自動串成同一受測物或一條連續驗證計畫。

但短篇活動回顧沒有列 UCIe revision、lane count、package／channel、traffic／protocol、運作
時間、錯誤與 BER、電壓溫度、晶粒或批次分母，以及 Adapter／FDI 覆蓋。頁面另一段提到 UCIe
3.0 的 48／64 GT/s，也不能倒填成這個 16G demo 使用 UCIe 3.0。更不能因為兩顆晶粒會連線，
就補上 CDXML／3DK、跨工具、foundry／OSAT、客戶 qualification 或量產收入。

這也說明「較晚、較實體」不等於每個維度都更完整。現場 demo 在物件成熟度上領先模擬，
白皮書卻在測項、失敗與修正細節上揭露更多；研究時要同時保存物件階段與測試覆蓋，不能只排
一條高低階梯。

### 一份互通範圍護照至少要有八欄

| 欄位 | 最少記錄 | 沒有它會混淆什麼 |
|---|---|---|
| 1. 受測物件與版本 | 晶粒／model／向量／spec／test plan 身分與 SHA | 同名不同版 |
| 2. 證據階段 | 模擬、tape-out、回片、live demo、compliance、qualification | 設計存在冒充實體通過 |
| 3. 參與角色 | 兩端供應者、DUT、reference／golden die、測試與簽核者 | 同源自測冒充獨立互通 |
| 4. 層與介面邊界 | 類比前端、PHY logic、RDI、Adapter、FDI、protocol | 進入 ACTIVE 冒充全 stack 通過 |
| 5. 速率與實體路徑 | data rate、lanes、UCIe-S／A、package、channel、電壓／溫度極端條件 | 16G 特定路徑冒充 64G 或所有封裝 |
| 6. 刺激與服務 | 向量、state、traffic、protocol、CRC／retry、error injection | 單一握手冒充工作負載與故障覆蓋 |
| 7. 樣本與結果 | die／package／lot、時間、環境、pass／fail、BER、coverage、例外放行 | 一次展示冒充分布與可靠度 |
| 8. 下游交付 | CDXML／3DK、cross-tool、foundry／OSAT sign-off、客戶與財務共同鍵 | 介面互通冒充可製造、可賣與有收入 |

八欄護照是研究中心的查核工具，不是產業共同表格。用途是讓下一位讀者知道這個 pass 真正停在
哪裡；空白欄位不必推翻已量到的結果，但必須阻止跨層外推。

### 多空小作文：兩邊共用同一份互通成績單

本輪只支持第 2、3 層各一筆公開紀錄；第 4–6 層以及財務共同觀測仍是 `N=0`。

**偏多版本。** 如果同一對多供應商晶粒能把前矽發現的差異一路關閉，實體測試再公開
固定測試計畫（fixed test plan）、層級覆蓋、錯誤、長時間與多顆分布；若同一 bundle 還能跨工具、foundry／OSAT 與客戶
資格回溯，標準化才可能降低重工與整合週期，讓 IP、驗證、封裝與測試服務形成可重複交付。

**偏空版本。** 每次 demo 都更換版本、封裝與測試方法，只公布進入 ACTIVE，向量與私有對照
規則（mapping）仍靠雙方人工調整；公開名稱看似相容，設計資料、完整 protocol、故障覆蓋與客戶產品卻無法接成
同一條證據鏈。這時聯盟動能可能主要停在整合活動，不能換算成開放市場或供應商財務。

兩邊共用的裁決，是同一受測物件沿八欄留下可重現的前後紀錄，而不是 demo 次數或最高 data
rate。本輪是 `N=2` 份官方紀錄、`N=2` 條發布消息鏈，兩份都涉及 Intel／Cadence 這組供應商
配對，卻不足以證明同一受測物或連續測試計畫，也不是兩組獨立產品、客戶或 deployment 樣本；
具名 CDXML／3DK handoff、foundry／OSAT sign-off、
產品 qualification、production 與財務共同觀測均為 `N=0`。這些是文件紀錄而非抽樣估計，
因此 sampling SE／t 不適用。

## 每顆晶粒都能安全開機，仍不等於整個封裝可信

安全不是四層之外再加一個口號，而是橫跨「系統角色、交付資料、符合性流程」的組合契約。
一顆小晶片可以正確驗證自己的開機程式，另一顆也可以；如果系統不知道它們是否是原先允許的
那兩顆、放在正確位置、扮演正確角色，或其中一顆已進入除錯狀態，就還不能說整套封裝可信。

把它想成飯店入住。每位旅客各有真護照，只回答「這個人是誰」；櫃台還要核對訂房名冊、房號、
同行者與有效期限，才回答「這一組人能不能進這一層」。房卡被重設、有人換房或開啟維修門後，
先前的判定也不能永久沿用。FCSA 1.1 Alpha 把這兩段工作分給每顆晶粒的 CRoT-A 與 System RoT。

### Alpha 有規範性規則，仍不是已發布產品證書

新手最容易把「文件內寫了 shall／must」與「版本已穩定、產品已通過」混成同一件事。本輪要同時
保留四個不同狀態。

| 狀態 | 目前可說什麼 | 目前不能說什麼 |
|---|---|---|
| 文件內容 | Declaration 與 Rule 是該規格內的規範性內容 | 每個實作者已遵守 |
| 版本成熟度 | OCP 於 2026-08-12 的既有快照把 1.1.0 Alpha 0 列為 for review | 1.1.0 已成為正式穩定 release 或已進入 beta |
| 規則身分 | 規格只承諾到 beta 後 content identifier 跨版維持相同 | Alpha 規則編號與文字已鎖定 |
| 實作與商用 | 公開清單仍只列 Arm CSA，且列名不是 endorsement | 已有獨立合規、客戶資格或量產收入 |

所以 Alpha 不是「沒有內容」，也不是「已經落地」。它最適合用來提早建立應查欄位與反證，
不能拿來計算採用率、供應商市占或財務受惠。

### 信任要做兩次：先證明每顆，再判斷整組

第一段是**晶粒本地證據**。每顆參與組合保證的晶粒用 CRoT-A 保管不可偽造的身分，量測或驗證
開機韌體，並回報 lifecycle、debug、test、scan、manufacturing 與安全關鍵設定。這只證明它
能為自己的狀態負責，不能替相鄰晶粒或整個封裝作決定。

第二段是**系統組合判定**。System RoT 發出 challenge，檢查回覆是否新鮮、簽章與憑證鏈是否
有效、有沒有被撤銷或回滾，並把證據綁回受保護的 manifest。接著還要核對實際晶粒集合、數量、
角色、位置與拓撲。這些條件都接受後，才建立受保護的控制平面並授權 Security Platform 成形。

| 問題 | CRoT-A 主要回答 | System RoT 主要回答 |
|---|---|---|
| 身分 | 我是哪一顆晶粒、持有哪組受保護憑證 | 現場晶粒是否都在允許名冊 |
| 韌體 | 我目前量測到哪一版開機與安全程式 | 版本是否符合政策、是否回滾或已撤銷 |
| 狀態 | 我處於哪個 lifecycle、debug／test 狀態 | 這組狀態能否形成指定安全域 |
| 組合 | 不替其他晶粒背書 | 角色、位置、拓撲與 policy binding 是否一致 |

「每顆都有 secure boot」因此只是必要條件，不是充分條件。反過來，System RoT 也不能在沒有
各顆可驗證證據時憑名單猜測狀態；本地信任與組合信任缺一不可。

### 開機通過不是永久通行：狀態變了就要重新判定

信任會隨狀態改變。FCSA Alpha 明列 reset、warm reset、晶粒故障、debug unlock、韌體更新與
recovery 等事件會觸發重新驗證；其他足以改變 Security Platform 的狀態變化也同樣適用。
這表示「開機 attestation pass」不能替代執行期事件帳。

| 事件 | 為什麼舊判定可能失效 | 下一筆最少證據 |
|---|---|---|
| Reset／warm reset | 晶粒重新進入初始化或不同韌體路徑 | reset 原因、版本、重新量測與新 verdict |
| Debug unlock | 原本隔離的觀察或修改能力被打開 | 授權者、範圍、時效、隔離與關閉紀錄 |
| Firmware update | 被量測程式與 rollback 邊界改變 | image 身分、簽章、版本、成功／回復狀態 |
| Chiplet fault | 缺席或失效晶粒可能改變角色與拓撲 | 故障身分、隔離、降級模式與重新組合結果 |
| Recovery | 系統可能以較低保證狀態恢復服務 | 進入條件、可用功能、告警與回到高保證的門檻 |

高保證系統遇到缺席、過期、撤銷或不符證據時，預設做法應是 fail closed；若產品允許 degraded
mode，也要明示隔離範圍與狀態，不能靜默沿用先前信任。這是規格 implementation note 對高保證
系統的預設做法，不是所有正文都是 normative Rule，也不是任何產品已達到零攻擊、零誤判或零停機的證明。

### 生命週期不是一條公司內流程，而是六段保管交接

FCSA 展示的典型 lifecycle 包含製造、晶粒 provisioning、整合 provisioning、OEM provisioning、
運作與 disposal。這是活動模型，不是不可增減的完整安全狀態機。特別之處是安全資料可能先在
晶粒製造端寫入，再到 SiP 整合端建立組合資料；兩段若由不同 stakeholder 負責，交接本身就是
新的攻擊面。

每顆晶粒也可以處於不同 lifecycle state。System RoT 要從多顆 attestation 推導產品定義的
system state，而不是拿某一顆的狀態直接代表全系統。RMA 或報廢時尤其重要：進入診斷／失效分析
可能開放 debug，但不能讓原先的 operation 權限與密鑰無條件延續。

### 一份組合信任護照至少要有十欄

| 欄位 | 最少記錄 | 沒有它會混淆什麼 |
|---|---|---|
| 1. 規格與產物身分 | FCSA maturity／version、profile、文件與測試 SHA | Alpha 冒充固定 release |
| 2. 預期組合 | manifest version、晶粒集合、數量、角色、位置、拓撲 | 名單中有晶粒就冒充正確組合 |
| 3. 晶粒本地身分 | CRoT-A、憑證鏈、供應者、唯一晶粒身分 | 同型號冒充同一實體 |
| 4. 韌體與量測 | boot image、security firmware、measurement、rollback index | secure boot 存在冒充版本合格 |
| 5. Lifecycle 與 DFX | manufacturing／provisioning／operation／disposal、debug／test／scan | 運作狀態冒充維修狀態 |
| 6. 證據時效 | challenge／nonce、時間、freshness、revocation | 舊的有效回覆被重播 |
| 7. 組合核對 | observed set、role、placement、topology 與 manifest 差異 | 每顆各自有效冒充整組有效 |
| 8. 控制平面與政策 | authenticated path、policy version、domain binding | 資料正確冒充傳遞與授權安全 |
| 9. 事件與重新驗證 | reset、fault、debug unlock、update、recovery、verdict、處置 | 開機 pass 冒充永久信任 |
| 10. 保管責任 | 六階段 owner、交接時間、授權、撤銷、RMA／disposal 證據 | 上一手寫入冒充下一手已驗收 |

這十欄是研究中心的查核護照，不是 FCSA 官方模板。它只把「哪顆、哪版、哪個狀態、由誰在何時
重新接受」變成可追蹤問題；產品 qualification、field reliability、部署量與財務結果仍要另接
客戶及商業證據，不能塞進技術 pass 後自動變成真。

它也不能替代後文的「語意交接護照」：組合信任護照追的是身分、狀態、政策與保管；語意交接
護照追的是設計檔版本、單位、座標、跨工具與實體資格。安全判定正確，不代表幾何與模型正確；
設計資料通過，也不代表現場晶粒與韌體仍是被授權的那一組。

### 多空小作文：同一張護照，正反敘事才可比較

**偏多版本。** 如果多家晶粒都能輸出同版可驗證證據，整合商以固定 manifest 重現組合判定，
更新、除錯與 RMA 也沿同一鍵重驗，多供應商 chiplet 就可能減少私有安全整合與事故追溯成本；
可重用的安全 IP、provisioning、驗證工具與封裝整合服務才有形成收費能力的可能。

**偏空版本。** Alpha 規則持續變動，各家憑證、lifecycle 與 debug 模型仍靠私有 mapping，System
RoT 只能接受同一供應者的封閉組合；新增 manifest、密鑰、provisioning 與事件紀錄反而增加交接
成本。即使技術可行，也可能沒有第二家實作、客戶採用或可辨識的供應商收入。

兩邊共用同一裁決：固定 release 與 test suite、至少一個非 Arm 實作、具名多供應商組合的 manifest
與 attestation transcript、六類事件重新驗證、客戶 qualification、field 分母及財務共同鍵。偏多
不能用 Alpha 發布當落地，偏空也不能因仍是 Alpha 就斷言組合信任無法實現。

本輪是 `N=1` 份 FCSA 1.1.0 Alpha 0 固定文件加 `N=1` 個同一 OCP 工作流 living index，兩者同屬
一條 OCP／Arm 規格消息鏈，不是兩套獨立實作或兩個產品樣本；沒有 sampling SE 或 t 值。非 Arm
實作、固定測試套件、多供應商資格、production deployment、field 結果與財務共同觀測均為
`N=0`。PDF 已固定 SHA-256 並逐頁渲染核對實際引用頁及相鄰頁，但這只能提高文件查核可重現性，
不能提高商用結論的證據等級。

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

<!-- research_source
source_id: S13
role: standard
source_kind: document
publisher: Open Compute Project Foundation / Arm Ltd.
independence_group: ocp-fcsa-standard
title: Foundation Chiplet System Architecture 1.1.0 Alpha 0
published_at: 2026-07-23
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://drive.google.com/file/d/1AtQF1KovNFulIGcrIMhTwIY0MfEhXNex/view
locator: PDF file p.7 的 version history；file p.11 的 normative content 與 beta 後 identifier 穩定範圍；file pp.165–168 的 Security Platform、System RoT、CRoT-A、composition assurance 與 typical lifecycle；file pp.197–200 的 manifest、attestation、policy response 與 fail-closed／degraded-mode implementation notes；本輪下載檔 SHA-256 51e37dc30084c14191701a97dc6a1e18e01bd77f3d1a7a8c3820d80a676b14d2
limitation: 這是 1.1.0 Alpha 0 文件且與 S1／S2 同屬 OCP／Arm 規格消息鏈；部分安全內容為 information 或 implementation note，不是全部皆為 normative Rule，也沒有固定 conformance test suite、獨立實作、攻擊測試、客戶 qualification、production deployment、field 統計或財務結果
-->

<!-- research_source
source_id: S14
role: other_primary
source_kind: document
publisher: UCIe Consortium
independence_group: ucie-consortium
title: Chiplet Summit 2026: UCIe Momentum Across a Growing Ecosystem
published_at: 2026-03-05
captured_at: 2026-08-24
accepted_at: 2026-08-24
status: active
url: https://www.uciexpress.org/post/chiplet-summit-2026-ucie-momentum-across-a-growing-ecosystem
locator: first live UCIe-S interoperability demonstration 段落的 Cameron Creek、Intel／Cadence independently designed chiplets、16G PHY 與 successful UCIe Interoperability Testing；UCIe 3.0 48／64 GT/s 是後續另一段
limitation: Consortium 活動回顧只直接證實一組 16G UCIe-S 現場展示；沒有 revision、lane count、package／channel、traffic／protocol、duration、error／BER、voltage／temperature、sample／lot、Adapter／FDI、CDXML／3DK、foundry／OSAT、customer qualification、production 或 financial result
-->

<!-- research_source
source_id: S15
role: competitor_primary
source_kind: document
publisher: Cadence Design Systems
independence_group: cadence-eda-vendor
title: Intel and Cadence Collaboration on UCIe: Demonstration of Simulation Interoperability
published_at: 2024-08-02
captured_at: 2026-08-24
accepted_at: 2026-08-24
status: active
url: https://www.cadence.com/en_US/home/resources/white-papers/intel-and-cadence-collaboration-on-ucie-wp.html
locator: UCIe Compliance Challenges、Role of Pre-Silicon Interoperability、Verification Challenges、Simulation Logistics、Initial Interop、Simulation - Interoperability over UCIe、Controller Simulation Interop 與 Conclusion
limitation: Cadence 撰寫的供應商案例使用 model、partner vectors 與可調整 test environment；沒有獨立第三方 benchmark、完整 analog／package path、公開 golden-die compliance report、BER／corner／duration／sample distribution、customer qualification、production deployment 或 financial result
-->

<!-- research_source
source_id: S16
role: other_primary
source_kind: living_index
publisher: UCIe Consortium
independence_group: ucie-consortium
title: UCIe Consortium Events Index
published_at:
captured_at: 2026-08-24
accepted_at: 2026-08-24
status: active
url: https://www.uciexpress.org/events
locator: 2026-08-24 的 upcoming／past events 與 Chiplet Summit 2026 Cameron Creek recap 入口，供後續尋找新的 live demonstration、test report 或公開活動附件
limitation: 動態活動頁會變動，且活動列名、攤位或 recap 不是固定 test plan、raw result、conformance certificate、customer deployment 或 financial evidence
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

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C15,C16,C17,C18,C19,C20
metric: FCSA 1.1 組合信任是否由 Alpha 推進 beta／release、固定測試套件、非 Arm 實作、多供應商資格與可重現執行期重新驗證
source_ids: S13
watch_source_ids: S2
frequency: event_driven
frequency_detail: FCSA 1.1 maturity、security content、test deliverable、implementation 或 customer qualification 更新後複核
next_check: 2026-09-30
trigger: 固定 FCSA 1.1 release 與 test suite 下，非 Arm 實作公布具名 CRoT-A／System RoT、manifest、六類事件 revalidation、失敗處置及跨廠 qualification 結果
invalidation: 若 beta／release 移除或實質改寫組合判定、lifecycle 或 runtime revalidation，則依新固定版本重寫 C15–C19；若只是沒有實作，C20 維持未驗證而不把架構判為失效
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C21,C22,C23
metric: 同一具名 UCIe 跨廠組合的互通範圍，是否能由前矽模擬一路對齊實體 PHY、Adapter／protocol、固定測試包絡及下游設計資料與產品資格
source_ids: S14,S15
watch_source_ids: S16
frequency: event_driven
frequency_detail: UCIe Consortium 或 Intel／Cadence 公布新 live demo、compliance report、test plan、customer qualification 或 production evidence 後複核
next_check: 2026-09-30
trigger: 同一受測組合公開 spec／IP／test-plan version、兩端角色、Analog／PHY／RDI／Adapter／FDI／protocol scope、rate／lanes／package／traffic、duration／error／BER／corner／sample 分母，並可連回 CDXML／3DK、foundry／OSAT 或客戶 qualification
invalidation: 若後續固定報告顯示前矽與實體結果不能對回同一物件、必要 test 被 workaround 排除、或 interface pass 無法延伸到宣稱層級，則依實際邊界修正 C21–C23，不以新 demo 數量補齊缺欄
-->

## 目前不能下的結論／待驗證

- 不能把 FCSA compliance、UCIe interoperability 與 CDXML／3DK conformance 當成同一張證書；三者檢查的對象不同。
- 不能把前矽模擬進入 ACTIVE，改寫成真實類比前端、封裝通道、BER、電壓溫度、長時間與客戶產品已通過。
- 不能把 16G UCIe-S 現場 demo 的成功，倒填成 UCIe 3.0 48／64 GT/s、完整 Adapter／protocol、設計資料交接或量產資格。
- 不能由 OCP 已公開 schema，推成四份 XSD 都可執行；固定 commit 的完整檢查已顯示兩份解析失敗。
- 不能由 DankaChiplet 或任何單一工具宣稱支援 CDXML，推成兩套 EDA 工具對同一資料會得到相同結果。
- 不能把 Arm 多供應商平台的 CSA／CHI C2C 敘述，改寫成已採用 CDXML／3DK 或已通過 foundry／OSAT 共同簽核。
- 不能把每顆晶粒各自 secure boot／attestation，改寫成整個封裝的晶粒集合、角色、位置、拓撲與執行期狀態已通過組合信任判定。
- 不能把 FCSA 1.1.0 Alpha 0 的安全框架，改寫成固定 release、conformance test、非 Arm 實作、客戶 qualification、production deployment 或台灣供應商財務受惠。
- 不能由公司加入聯盟、具備先進封裝、EDA、測試或設備能力，推導具名 design win、訂單、收入、毛利或投資建議。
