# AI 電容不是單一受惠品：先按電壓、頻帶與系統位置拆分

<!-- research_topic
topic_id: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-03
source_published_at: 2026-03-01
last_reviewed_at: 2026-08-03
review_due: 2026-09-01
source_type: mixed
publisher: Open Compute Project
publisher_domain: opencompute.org
canonical_url: https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf
source_chain_id: ai-capacitor-role-primary-scan-20260803
stock_ids:
group_ids: passive,powersupply
trigger_type: architecture_standard_and_supplier_role_map
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C4
base_confidence: medium
confidence_basis: OCP 與 TI 可定位 rack CBU 角色，TDK 與 Murata 兩條獨立供應商鏈又分別公開高低壓及 PDN 頻帶角色；足以建立「位置×電壓×頻帶×任務」框架，但供應商文件仍是自身產品地圖，尚無共同量產 BOM、替代率、台灣公司 qualification 或財務分母
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-03
from: initial
to: inbox
reason: captured_rack_bus_board_and_package_capacitor_roles
evidence: source_chain:ai-capacitor-role-primary-scan-20260803
-->
<!-- transition
date: 2026-08-03
from: inbox
to: triaged
reason: separated_capacitors_by_system_position_voltage_frequency_and_task
evidence: sources:S1,S2,S3,S4
-->

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:high_frequency_glossary
-->

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave5_power_system_learning_no_conclusion_change
evidence: editorial:plain_language_wave5
-->

<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave82_capacitor_positions_no_conclusion_change
evidence: editorial:plain_language_wave82_capacitor_positions
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **CBU（Capacitor Bank Unit）**：靠近機架、用電容或超級電容吸收快速功率波動的儲能模組；它不是處理器旁的一顆去耦電容。
- **BBU（Battery Backup Unit，電池備援單元）**：用電池支撐較長的斷電或切換過渡。它和處理快速功率波動的 CBU 是不同機架選項。
- **Rack（機架／機櫃）**：集中安裝運算、電源、儲能與冷卻設備的結構單位。同一機架裡的電容，仍可能位在完全不同的電氣節點。
- **DC link／高壓直流匯流排**：電源轉換級之間輸送數百伏直流電的節點；此處元件先面對耐壓、紋波、壽命與安全條件。
- **PDN（Power Delivery Network）**：從電源轉換器、電路板、封裝到晶片的供電路徑；頻率越高，元件位置與寄生電感通常越重要。
- **ESR／ESL**：電容不是理想元件；等效串聯電阻與電感會限制它在不同頻率處理紋波或瞬態的能力。
- **MLCC（積層陶瓷電容）**：把多層陶瓷介質與電極疊合的小型電容，常用於去耦與濾波；不同尺寸、介質與耐壓不可視為同一產品。
- **EDLC（電雙層電容）**：以電雙層儲能的超級電容，適合高功率充放電；它和晶片旁 MLCC 的位置與時間尺度不同。
- **電容量**：電容儲存電荷能力的指標；容量相近，不代表耐壓、反應速度、壽命與適用位置也相同。
- **紋波**：電源轉換後仍殘留的週期性電壓或電流起伏；高壓供電路徑的電容會協助平滑這些起伏。
- **去耦**：把電容放在用電元件附近，短暫補上電流並降低電源雜訊，避免快速變化影響其他電路。
- **頻帶**：元件能有效處理的一段變化速度或頻率範圍；不同頻帶通常需要不同位置與電容特性。
- **瞬態**：負載、電壓或電流在很短時間內突然改變的事件。
- **阻抗**：電路在特定頻率下阻礙電流變化的程度；供電路徑要在目標頻帶維持足夠低的阻抗。
- **寄生電感**：導線、接點、電路板與封裝自然帶來的額外電感；距離越遠，越可能削弱高頻去耦效果。
- **電路板大容量電容（board bulk）**：放在電路板供電入口或轉換器附近，處理比晶片旁去耦更慢的電流變化。
- **封裝／晶片旁（package／near-die）**：非常靠近晶片的供電位置，用來縮短高頻電流路徑並降低寄生影響。
- **參考設計（reference design）**：供應商公開的可行電路與元件組合，用來示範一種做法；不等於客戶已採用或量產。
- **料號（part number）**：用來辨認特定產品規格與版本的編號；只有產品類別，還不能確認實際採用哪一顆元件。
- **客戶資格驗證（qualification）**：客戶依自己的電氣、安全、可靠度與系統條件，確認產品是否可被採用的測試階段。

### 三句話抓重點

- AI 機櫃裡的電容至少出現在四個不同位置：機櫃旁的電容儲能模組、高壓直流匯流排、電路板，以及封裝或晶片旁；位置不同，處理的電力變化也不同。
- OCP 與 TI 顯示機櫃級電容儲能角色，TDK 與 Murata 的產品圖再分出高壓、板級與晶片旁電容；這些是公開架構與供應商角色圖，不是全產業共同用量表。
- 因此，現有證據只能用來分清電容放在哪裡、負責什麼，還不能證明台灣被動元件或電源供應公司已進入量產材料清單、取得訂單或形成可辨識獲利。

### 為什麼重要

**先找電容放在哪裡。** 機櫃旁的電容儲能模組、高壓直流匯流排、電路板，以及封裝或晶片旁，是四個不同位置，不能把它們視為同一份需求。

**再看它處理哪一種電力變化。** 機櫃級模組緩衝快速功率波動，高壓位置要兼顧耐壓、紋波與壽命，電路板大容量電容處理較慢變化，晶片旁去耦則處理高頻變化。容量或材料名稱相近，不代表任務相同。

**最後才談公司與價值。** 先確認產品位置、規格與客戶資格驗證，才能判斷規格升級是增加顆數、提高單價、減少其他元件，還是把價值移到另一種電容。

### 接下來怎麼追

- 追 OCP 或平台文件是否公布同一量產機櫃中，電容儲能模組、高壓直流匯流排、電路板與晶片旁供電路徑的介面、額定條件及客戶資格驗證。
- 追元件供應商是否從產品角色圖推進到具名料號、客戶測試、量產出貨，以及可以重建的替代與用量資料。
- 追台灣被動元件與電源供應公司的法說、季報及重大訊息，確認客戶與供應商是否能雙向對齊產品位置、規格、量產節點、收入與毛利。

### 想一想

- 兩顆電容的容量即使相近，一顆放在高壓供電路徑、另一顆放在晶片旁，為什麼不能直接互換？
- 如果某一段供電路徑用了效能更高、但數量更少的元件，只看「規格升級」會不會高估整體價值？
- 供應商的產品角色圖和客戶實際量產材料清單之間，還缺哪些資格驗證、份額與財務證據？

## 主張與證據帳本

本文的「證實」只表示指定官方文件直接支持產品或架構角色。TDK 與 Murata 的文件是發行人
對自身產品組合的說法；沒有被改寫成全產業標準、台灣供應商訂單或被動元件需求倍數。

<!-- research_source
source_id: S1
role: standard
source_kind: document
publisher: Open Compute Project
title: Diablo 400 Project Rack and Power Specification 0.7.0
published_at: 2026-03-01
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf
locator: PDF pp.14–15，7.2 Energy Storage Solutions、7.2.1 BBU Option 與 7.2.2 Capacitor Bank Option；rack 支援 BBU 與 CBU，CBU 的 power 與 capacity 依 application 決定
limitation: 這是 OCP Diablo 400 0.7.0 的 rack option，不是所有 AI rack 的共同 production BOM；沒有 CBU 材料、元件數、供應商、採購量或財務資料
independence_group: open-compute-project
-->

<!-- research_source
source_id: S2
role: company_release
source_kind: document
publisher: Texas Instruments
title: TI unveils complete 800 VDC power architecture for future generation AI data centers with NVIDIA
published_at: 2026-03-16
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html
locator: Complete power solution；hot-swap、800V-to-6V、6V-to-<1V 分列，另展示以 EDLC super capacitor cells 實作、40W/in³ 的 800V CBU
limitation: TI 展示與 reference design 支持技術角色及公司產品能力，不等於指定客戶 qualification、production deployment、固定 BOM 或台灣供應商參與
independence_group: texas-instruments
-->

<!-- research_source
source_id: S3
role: company_filing
source_kind: document
publisher: TDK Corporation
title: Full Year Performance Briefing Fiscal Year March 2026
published_at: 2026-04-28
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.tdk.com/system/files/2026_4q01_0mqf56xw_en.pdf
locator: PDF p.30（投影片 29），400–800V High-Voltage Capacitors 圖與講稿；列出 aluminum capacitors、MLCCs、film capacitors，並把 polymer／MLCC 等低壓元件映射到 48V、12V、<1V 與 package 區域
limitation: 這是 TDK 對自身產品與成長機會的管理層地圖，不是中立的系統 requirement、客戶 production BOM、跨供應商份額或台灣公司證據
independence_group: tdk
-->

<!-- research_source
source_id: S4
role: management_commentary
source_kind: document
publisher: Murata Manufacturing
title: AI System with Advanced Packaging Webinar Q&A
published_at: 2026-04-25
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.murata.com/-/media/webrenewal/campaign/events/asean/2026/apr26_ai-system-with-advance-packaging/qna.ashx?cvid=20260425083237000000&la=en-sg
locator: PDF p.3，Q21；選型依 target impedance、transient requirement 與 placement constraint，MLCC 對應 high-frequency decoupling、silicon capacitor 靠近 die 的 ultra-fast response、polymer capacitor 對應 low-frequency bulk stability
limitation: 這是 Murata webinar Q&A 對自身 PDN 解法的回答，沒有共同測試條件、跨廠替代率、量產客戶、BOM 數量、價格或財務分母
independence_group: murata
-->

<!-- research_source
source_id: S5
role: standard
source_kind: living_index
publisher: Open Compute Project
title: Open Rack Specifications and Designs
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.opencompute.org/wiki/Open_Rack/SpecsAndDesigns
locator: 2026-08-03 的 Open Rack 規格索引；持續回查 Diablo／rack power／energy storage 的正式版本與附件
limitation: 動態索引不能替代已發布文件或證明量產採用；出現新附件時須另建 document source
independence_group: open-compute-project
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: living_index
publisher: TDK Corporation
title: TDK Investor Relations Events
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.tdk.com/en/ir/ir_events/index.html
locator: 2026-08-03 的 IR events 索引；回查後續決算、Investor Day 與 AI data center passive-component 資料
limitation: 動態索引只供未來重查；不能證明產品已 qualification、出貨、形成份額或達到成長目標
independence_group: tdk
-->

<!-- research_source
source_id: S7
role: company_release
source_kind: living_index
publisher: Murata Manufacturing
title: Murata Product and Event News
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.murata.com/news
locator: 2026-08-03 的產品與活動新聞索引；回查 AI server PDN、MLCC、silicon 與 polymer capacitor 新文件
limitation: 動態索引不能替代具日期的產品文件，也不證明客戶 BOM、量產採用、份額或台灣公司曝險
independence_group: murata
-->

<!-- research_source
source_id: S8
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-03 起追蹤 passive 與 powersupply 族群公司的法說、季報、重大訊息與產品說明
limitation: 索引頁本身不證明任何公司具有 AI capacitor BOM、qualification、訂單、收入或獲利；命中文件後須另建 document source
independence_group: twse-mops
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: OCP Diablo 400 0.7.0 把 rack BBU 與 CBU 分成不同 energy-storage options，CBU 的 power 與 capacity 由 application 決定；TI 另展示以 EDLC super capacitor cells 實作的 800V CBU
supporting_source_ids: S1,S2
contrary_source_ids:
as_of: 2026-03-16
basis: S1 的 7.2.1／7.2.2 與 S2 的 Complete power solution 可直接定位 BBU、CBU 及 EDLC 實作
boundary: 只證實兩份公開架構與 reference design；不固定所有平台的 CBU 容量、cell chemistry、元件數、供應商、採用率或財務貢獻
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
claim: TDK 在 2026-04-28 的公司簡報把 400–800V 區域映射到高壓 aluminum、MLCC 與 film capacitors，並把 polymer／MLCC 等低壓電容映射到 48V、12V、<1V 與 package 附近
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-04-28
basis: S3 p.30（投影片 29）的產品地圖與同頁管理層講稿直接列出電壓區域及公司產品類別
boundary: 這是 TDK 自身 portfolio／opportunity map，不代表所有 AI rack 採同一配置，也不支持跨公司用量、份額或營收比較
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
claim: Murata 的 webinar Q&A 表示 PDN capacitor 選型由 target impedance、transient 與 placement 約束共同決定，並把 MLCC、silicon capacitor、polymer capacitor 分別對應 high-frequency decoupling、near-die ultra-fast response 與 low-frequency bulk stability
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-04-25
basis: S4 p.3 Q21 直接回答三類電容在該公司 PDN 解法中的角色與選擇目標
boundary: 只支持 Murata 的技術角色說法；沒有共同頻帶切點、跨供應商替代率、量產客戶、價格或財務資料
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: active
claim: AI 電容需求應先按系統位置、工作電壓、主要頻帶與任務分層，再談材料、數量與供應商；CBU、高壓 bus／DC link、板級 bulk 與 package／near-die decoupling 可同時存在，但不能合併成單一「電容受惠」需求或預設彼此可替代
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-08-03
basis: S1／S2 建立 rack CBU，S3 建立高低壓位置地圖，S4 建立頻帶、瞬態與 placement 分工；四條獨立來源鏈共同支持先分層再映射的研究框架
boundary: 這是研究端的分類推論，不宣稱唯一架構、固定頻帶、材料優劣、元件數、單機價值、供應商份額、價格、收入或股價尚未反映
verification_needed: 需同一 production platform 的完整 PDN／CBU design、qualification、BOM、field data 與客戶—供應商雙向文件驗證實際配置及替代
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: 台灣 passive 或 powersupply 族群已有公司以具名電容產品進入上述 AI CBU、800V bus、board 或 package PDN 的 production BOM，並取得可辨識份額、訂單、收入與毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-03
basis: 現有一手來源只到 OCP／TI 架構及 TDK／Murata 自身產品角色，沒有 universe 公司與客戶雙向核對的 part number、qualification、production BOM、數量、價格及財務分母
boundary: 不把架構必要性、海外供應商產品地圖、AI 關鍵字或同族群營收成長改寫成台灣公司供貨事實
verification_needed: 客戶 qualification／採購或 production BOM，並與台灣公司法說、季報或重大訊息交叉核對具名產品、位置、規格、量產、收入及毛利
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 四個位置、四種任務：先找電容放在哪裡

| 電容位置 | 它主要處理什麼 | 目前一手證據 | 還不能因此判定 |
|---|---|---|---|
| 機櫃旁的電容儲能模組（CBU） | 快速補上功率缺口，以電容短暫儲能與放電 | OCP 把電容與電池備援分列；TI 展示以超級電容實作的 800V 模組 | 電芯材料、容量、元件數、供應商或已實際部署 |
| 400–800V 高壓直流匯流排 | 平滑高壓電力起伏、承受紋波並支援電源轉換 | TDK 自家產品圖列出鋁電解、積層陶瓷與薄膜電容 | 全產業使用共同材料清單、三類元件同步增加、替代率或市占 |
| 48V／12V 電路板大容量電容 | 處理較慢的電流變化，穩定轉換器輸入與輸出 | TDK 低壓產品圖與 Murata 對聚合物電容角色的說法 | 每張板的顆數、容量、價格、壽命或已通過客戶驗證 |
| 封裝或晶片旁的去耦電容 | 壓低高頻阻抗、縮短供電路徑並支援快速瞬態 | Murata 對積層陶瓷與矽電容頻帶、放置位置的說法 | 固定頻帶切點、哪一材料勝出、量產用量或良率 |

這張表不是替電容材料排名，而是先把四個位置分開。確認元件放在哪裡、承受什麼電壓、要處理
多快的變化，以及失效時影響哪一段供電後，才能追問規格升級會增加顆數、提高單價、減少其他
元件，還是只把價值移到另一種電容。跳過這一步，就容易把機櫃儲能、高壓匯流排、電路板與
晶片旁的電容重複加總。

## 怎麼用這張表判讀公司新聞

1. **先找客戶的量產架構**：供應商參考設計只能證明做得到；客戶平台文件才可能固定元件位置與接口。
2. **再找具名產品與驗證**：料號、電壓、容量、電阻與電感特性、溫度、壽命及失效測試，必須對到同一個應用位置。
3. **最後才對回公司財務**：客戶與供應商雙向確認後，再查出貨量、平均售價、份額、收入與毛利；缺一層就維持觀察。
4. **避免重複計算**：高規格元件可能減少顆數或取代另一層零件，不能直接加總每家供應商的機會地圖。

## 研究判定

- **目前可保留的結論**：機櫃儲能、高壓直流匯流排、電路板大容量電容，以及封裝或晶片旁去耦，是四個不同查核位置；四條一手來源鏈足以建立角色邊界。
- **可信度為中而不是高**：OCP 與 TI 支持機櫃架構，TDK 與 Murata 支持供應商產品角色；目前仍缺同一量產平台的完整供電路徑、共同測試與材料清單。
- **目前不能發布的結論**：所有電容同步增加、指定材料或台灣公司勝出、顆數、平均售價、市占、訂單、獲利，以及市場是否已反映。
- **需要看到什麼才能前進**：買方量產文件與供應商申報雙向對齊具名產品、客戶資格驗證、實際配置、出貨及財務分母。

## 來源

- [OCP：Diablo 400 Rack and Power Specification 0.7.0](https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf)
- [Texas Instruments：800 VDC architecture 與 EDLC CBU](https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html)
- [TDK：FY March 2026 Full Year Performance Briefing](https://www.tdk.com/system/files/2026_4q01_0mqf56xw_en.pdf)
- [Murata：AI System with Advanced Packaging Webinar Q&A](https://www.murata.com/-/media/webrenewal/campaign/events/asean/2026/apr26_ai-system-with-advance-packaging/qna.ashx?cvid=20260425083237000000&la=en-sg)
- [OCP Open Rack 規格索引](https://www.opencompute.org/wiki/Open_Rack/SpecsAndDesigns)
- [TDK IR events](https://www.tdk.com/en/ir/ir_events/index.html)
- [Murata news](https://www.murata.com/news)
- [公開資訊觀測站](https://mops.twse.com.tw/mops/web/index)

## 族群影響

<!-- impact
group_id: passive
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: 電容角色可把 passive 族群的公司研究從 AI 關鍵字改為 CBU、high-voltage bus、board bulk 與 near-die decoupling 的具名產品及資格查核
evidence_boundary: 現有來源沒有台灣公司 production BOM、份額、訂單或財務分母；不做材料、公司或受惠排行
-->

<!-- impact
group_id: powersupply
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: 電源模組與板級 PDN 整合會決定電容位置、額定與替代關係，適合追具名模組、客戶 qualification 與 BOM 變化
evidence_boundary: 不把外部供應商產品圖或 reference design 改寫成台灣電源公司已採用、量產、取得訂單或改善毛利
-->

## 監測器

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C4
metric: OCP／平台與元件供應商是否把 capacitor role map 推進到共同介面、具名 part、qualification 與 production configuration
source_ids: S1,S2,S3,S4
watch_source_ids: S5,S6,S7
frequency: monthly
next_check: 2026-09-01
trigger: 新規格或 production 文件同時公布系統位置、電壓、頻帶／瞬態、元件類型、qualification 與可重建配置
invalidation: 新平台顯示本文分層無法描述實際 PDN，或供應商後續文件撤回／實質縮窄原產品角色
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C5
metric: 台灣 passive／powersupply 公司是否出現客戶與供應商雙向核對的具名 capacitor、量產 BOM、份額與財務分母
source_ids: S1,S2,S3,S4
watch_source_ids: S8
frequency: quarterly
next_check: 2026-09-30
trigger: 公司申報與客戶文件同時指向具名產品、系統位置、qualification、量產出貨、收入及毛利
invalidation: 公司明確否認相關產品或應用，或產品長期停在樣品／機會地圖而沒有 qualification 與 production evidence
-->

## 什麼會推翻這篇

- Production platform 證明不同位置與頻帶的電容可在相同可靠度、成本與空間條件下完全互換，使本文分層失去解釋力。
- OCP／平台移除 CBU 或重新定義其任務，而現場資料顯示它與 BBU／board bulk 的邊界不成立。
- 若台灣公司長期只有「AI、高壓、被動元件」敘事而沒有具名產品、資格、量產與財務分母，族群 route 應維持待驗證，不能因題材熱度升格。
