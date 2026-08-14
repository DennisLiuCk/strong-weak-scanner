# AI 電容不是單一受惠品：先按電壓、頻帶與系統位置拆分

<!-- research_topic
topic_id: MI-2026-08-03-AI-CAPACITOR-ROLE-MAP
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-03
source_published_at: 2026-03-01
last_reviewed_at: 2026-08-12
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

<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_effective_capacitance_impedance_ripple_heating_and_lifetime_envelope
evidence: sources:S9,S10,S11
-->

<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_capacitor_energy_voltage_window_esr_droop_and_target_impedance_passport_without_thesis_clock_refresh
evidence: sources:S12,S13,S14
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
- **ESE**：KEMET／YAGEO 的一個 +105°C 徑向鋁電解電容系列；本文引用它的操作指南說明判讀方法，不把該系列公式套用到其他電容。
- **電容量**：電容儲存電荷能力的指標；容量相近，不代表耐壓、反應速度、壽命與適用位置也相同。
- **標稱容量**：料號或資料表在指定量測條件下標出的容量；它是選型起點，不一定等於實際工作時可用的容量。
- **有效容量**：把實際直流電壓、交流訊號、頻率與溫度帶入後，元件在工作點真正呈現的容量。
- **直流偏壓**：電容兩端持續存在的直流工作電壓；部分高介電常數積層陶瓷電容的有效容量會隨它改變。
- **紋波**：電源轉換後仍殘留的週期性電壓或電流起伏；高壓供電路徑的電容會協助平滑這些起伏。
- **紋波電流**：反覆流入、流出電容的交流電流成分；它流過等效串聯電阻時會產生損耗與熱。
- **自發熱**：元件因內部損耗而升溫；電容的紋波電流、等效串聯電阻、散熱路徑與環境溫度會共同影響它。
- **去耦**：把電容放在用電元件附近，短暫補上電流並降低電源雜訊，避免快速變化影響其他電路。
- **頻帶**：元件能有效處理的一段變化速度或頻率範圍；不同頻帶通常需要不同位置與電容特性。
- **瞬態**：負載、電壓或電流在很短時間內突然改變的事件。
- **阻抗**：電路在特定頻率下阻礙電流變化的程度；供電路徑要在目標頻帶維持足夠低的阻抗。
- **可用能量**：電容從允許的最高工作電壓降到最低工作電壓之間，理想上能交出的能量；不能只看滿電時儲存多少。
- **Vhi／Vlo**：一段放電任務允許的最高與最低工作電壓；兩者共同決定可用電壓窗。
- **½CV²**：理想電容在電壓 V 時的儲能關係，其中 C 是電容量；實際系統還要扣掉各種損耗與工作邊界。
- **Hold-up／ride-through**：主電源短暫掉電或切換時，由儲能維持負載的時間；它先是一筆能量與電壓窗的帳。
- **負載階躍（load step）**：負載電流在短時間突然改變；最初的壓降會同時受等效串聯電阻、電容量、寄生電感、走線與控制迴路影響。
- **目標阻抗**：把可容許壓降除以負載電流變化所得的供電路徑阻抗上限；它必須對到指定頻帶，不能只用單一頻率或單一電容判斷。
- **自共振頻率（SRF）**：電容的容性與寄生電感效應互相抵銷附近的頻率；超過後，阻抗可能重新上升，元件不再像理想電容。
- **寄生電感**：導線、接點、電路板與封裝自然帶來的額外電感；距離越遠，越可能削弱高頻去耦效果。
- **任務剖面（mission profile）**：元件在預定使用期間會遭遇的電壓、電流、溫度、頻率、冷卻與運轉時間組合。
- **電路板大容量電容（board bulk）**：放在電路板供電入口或轉換器附近，處理比晶片旁去耦更慢的電流變化。
- **封裝／晶片旁（package／near-die）**：非常靠近晶片的供電位置，用來縮短高頻電流路徑並降低寄生影響。
- **參考設計（reference design）**：供應商公開的可行電路與元件組合，用來示範一種做法；不等於客戶已採用或量產。
- **Selection／選型**：依工作條件挑選料號與配置的工程過程；文件標題出現 Selection，不代表已通過客戶資格驗證。
- **料號（part number）**：用來辨認特定產品規格與版本的編號；只有產品類別，還不能確認實際採用哪一顆元件。
- **客戶資格驗證（qualification）**：客戶依自己的電氣、安全、可靠度與系統條件，確認產品是否可被採用的測試階段。

### 三句話抓重點

- AI 機櫃裡的電容至少出現在四個不同位置：機櫃旁的電容儲能模組、高壓直流匯流排、電路板，以及封裝或晶片旁；位置不同，處理的電力變化也不同。
- 分完位置後還要再過四道檢查，並把可用能量、電壓窗、等效串聯電阻壓降與電容量壓降分帳；同樣的標稱容量不代表可互換，也不代表能交出相同能量或瞬態支撐。
- 因此，現有證據只能用來分清電容放在哪裡、負責什麼，還不能證明台灣被動元件或電源供應公司已進入量產材料清單、取得訂單或形成可辨識獲利。

### 為什麼重要

**先找電容放在哪裡。** 機櫃旁的電容儲能模組、高壓直流匯流排、電路板，以及封裝或晶片旁，是四個不同位置，不能把它們視為同一份需求。

**再看它處理哪一種電力變化。** 機櫃級模組緩衝快速功率波動，高壓位置要兼顧耐壓、紋波與壽命，電路板大容量電容處理較慢變化，晶片旁去耦則處理高頻變化。容量或材料名稱相近，不代表任務相同。

**同一位置也要帶入實際工作條件。** 高介電常數積層陶瓷電容的有效容量可能受直流偏壓影響；電解電容的阻抗、可承受紋波與壽命又會隨頻率、溫度及散熱條件改變。資料表上的容量值不能單獨回答能否替換。

**最後才談公司與價值。** 先確認產品位置、規格與客戶資格驗證，才能判斷規格升級是增加顆數、提高單價、減少其他元件，還是把價值移到另一種電容。

### 接下來怎麼追

- 追 OCP 或平台文件是否公布同一量產機櫃中，電容儲能模組、高壓直流匯流排、電路板與晶片旁供電路徑的介面、額定條件及客戶資格驗證。
- 追元件供應商是否從產品角色圖推進到具名料號、客戶測試、量產出貨，以及可以重建的替代與用量資料。
- 追同一具名料號在實際直流電壓、溫度與頻率下的有效容量、阻抗曲線、紋波溫升及壽命計算，避免只比較標稱容量。
- 追同一平台是否同時公布最高／最低工作電壓、負載波形、hold-up 時間、等效串聯電阻／電感與目標阻抗，才能重建能量及瞬態兩本帳。
- 追台灣被動元件與電源供應公司的法說、季報及重大訊息，確認客戶與供應商是否能雙向對齊產品位置、規格、量產節點、收入與毛利。

### 想一想

- 兩顆電容的容量即使相近，一顆放在高壓供電路徑、另一顆放在晶片旁，為什麼不能直接互換？
- 即使兩顆電容位在同一位置、都標示相同容量，直流偏壓、阻抗曲線與散熱條件不同時，哪一顆才真正能完成任務？
- 同樣 1,000 µF，若可用電壓窗分別是 48→40V 與 12→10V，為什麼不能用容量相同就推定可用能量相同？
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

<!-- research_source
source_id: S9
role: company_release
source_kind: document
publisher: TDK Corporation
title: Challenges in Next Generation Power Semiconductors and Application of MLCCs
published_at: 2026-07-09
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://product.tdk.com/en/techlibrary/applicationnote/snubber_mlcc.html
locator: Selection Criteria for Snubber Capacitors，Figures 5–8；Class 2 MLCC 要看實際工作電壓下的 effective capacitance，紋波電流經 ESR 產生 W=ESR×I² 自發熱，且應以接近實際的電壓波形核對溫升與壽命
limitation: 這是 TDK 對高 dV/dt snubber 應用與自身 MLCC 測試的技術文件；20°C 溫升建議、波形結果與材料差異不能外推成所有 AI PDN、所有電容技術或共同客戶 qualification
independence_group: tdk
-->

<!-- research_source
source_id: S10
role: company_release
source_kind: document
publisher: Murata Manufacturing
title: The voltage characteristics of electrostatic capacitance
published_at: 2012-11-28
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://article.murata.com/en-eu/article/voltage-characteristics-of-electrostatic-capacitance
locator: DC bias characteristic，Figures 1–2；高介電常數 MLCC 施加直流電壓後 effective capacitance 會改變，選型時不能只接受 catalog capacitance，須在實際電壓條件下核對
limitation: 文中百分比是指定 6.3V、100µF、1.8V 與介質的示例，不是所有 MLCC 或其他電容類型的共同降額；文章也沒有 AI 平台、量產 BOM 或客戶資格資料
independence_group: murata
-->

<!-- research_source
source_id: S11
role: company_release
source_kind: document
publisher: KEMET / YAGEO Group
title: Radial Aluminum Electrolytic Capacitors ESE +105°C — Application & Operation Guidelines
published_at: 2026-06-30
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://content.kemet.com/datasheets/KEM_A4055_ESE.pdf
locator: PDF pp.12–16；effective capacitance、ESR、ESL 與 impedance 的頻率／溫度關係，最大 ripple current 的環境溫度、散熱面積、ESR 與頻率條件，以及 operating temperature 對 expected life 的系列公式
limitation: 這是 ESE +105°C 徑向鋁電解系列的應用指南；等效電路、圖線與壽命公式不可直接套到 MLCC、polymer、film、EDLC 或未指定的 AI 系統任務剖面
independence_group: yageo-kemet
-->

<!-- research_source
source_id: S12
role: company_release
source_kind: living_index
publisher: Eaton
title: Supercapacitor Modules Frequently Asked Questions
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.eaton.com/sg/en-us/products/electronic-components/faq/supercapacitor-modules-frequently-asked-questions.html
locator: Energy and Power Calculation、Voltage、State of Charge；儲能以 ½CV² 計，peak power 另含 ESR，state of charge 以量測電壓平方除設計電壓平方表示，工作電壓範圍又會影響壽命
limitation: 這是 Eaton 現行超級電容模組 FAQ，頁面未標發布日；公式只建立理想能量、功率與電壓平方關係，不是所有電容技術、AI rack、CBU 量產 BOM、效率、可用壽命或財務資料
independence_group: eaton
-->

<!-- research_source
source_id: S13
role: company_release
source_kind: living_index
publisher: Eaton
title: Supercapacitor Applications Guide
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.eaton.com/us/en-us/products/electronic-components/topics/supercapacitor-applications-guide.html
locator: Discharge Characteristics、General Application Information、Lifetime；定電流放電把 resistive 與 capacitive drop 分列為 Vdrop＝I×(R＋t／C)，短時間高電流脈衝較受 ESR 主導，較低電流長時間放電較受 capacitance 主導，並另列電壓、溫度、串聯均壓與壽命邊界
limitation: 這是 Eaton 對自身超級電容產品的現行應用指南，頁面未標發布日；定電流近似不能直接套用定功率轉換器、MLCC、鋁電解、薄膜、含 ESL／控制迴路的完整 PDN 或客戶 qualification
independence_group: eaton
-->

<!-- research_source
source_id: S14
role: company_release
source_kind: document
publisher: Texas Instruments
title: Input and Output Capacitor Selection
published_at: 2006-02-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.ti.com/lit/an/slta055/slta055.pdf
locator: PDF pp.7–10；電容阻抗受 C／ESR／ESL 與自共振限制，多種電容覆蓋不同頻帶；快速負載階躍的立即壓降下限以 ΔI×並聯 ESR 說明，分散式電源匯流排以 Z＝ΔV／ΔI 建立目標阻抗
limitation: 文件頁首只標 February 2006，本文以 2006-02-01 做月精度正規化且不主張日精度；這是舊式 PTH regulator 應用報告，公式、頻帶與算例不是 AI rack、特定板卡、量產驗收、BOM 或財務證據
independence_group: texas-instruments
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
supporting_source_ids: S1,S2,S3,S4,S9,S10,S11
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

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: Murata 表示高介電常數 MLCC 施加直流電壓後有效容量會改變，選型不能只接受 catalog capacitance；TDK 亦要求 Class 2 MLCC 以實際工作電壓下的 effective capacitance 判斷
supporting_source_ids: S9,S10
contrary_source_ids:
as_of: 2026-08-12
basis: S10 的 DC bias characteristic 與 S9 的 Selection Point 2 都直接要求把實際直流工作電壓帶入容量判斷
boundary: 不同介質、尺寸、額定電壓、容量、溫度與工作點的曲線不同；本文不發布共同降額百分比，也不把 MLCC 特性套到所有電容技術
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: KEMET／YAGEO 的 ESE 應用指南把有效容量、ESR、ESL 與總阻抗分開，並明示阻抗不是常數，而會隨頻率與溫度改變；超過共振區後，繞組與端子的感抗會使阻抗上升
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-08-12
basis: S11 pp.12–14 的等效電路、impedance-frequency 圖與逐段解釋直接支持 ESE 系列的頻率／溫度依賴
boundary: 只證實該鋁電解系列的一般應用指南；不固定其他電容的共振點、目標頻帶、電路穩定性或跨材料替代關係
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: TDK 把 MLCC 自發熱寫成 ESR×I² 並要求以實際波形與溫度條件評估；KEMET／YAGEO 的 ESE 指南則把可承受紋波電流連到環境溫度、散熱面積、ESR、頻率與熱應力下的預期壽命
supporting_source_ids: S9,S11
contrary_source_ids:
as_of: 2026-08-12
basis: S9 的 Selection Points 3–4／高 dV/dt evaluation 與 S11 pp.15–16 的 ripple-current、thermal-stress 及 expected-life 段落直接支持各自元件範圍內的熱與壽命條件
boundary: TDK 的 20°C 建議與 KEMET ESE 的壽命公式屬不同技術及測試範圍，不能合併成全產業共同 pass line，也不能替代客戶任務剖面與可靠度試驗
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: inference
status: active
claim: 兩顆電容即使標稱容量相同，也應依序核對實際偏壓與溫度下的有效容量、目標頻帶阻抗、紋波造成的溫升，以及任務剖面下的壽命；四道條件未對齊前不能視為可替換或直接比較價值
supporting_source_ids: S9,S10,S11
contrary_source_ids:
as_of: 2026-08-12
basis: S9／S10 建立 effective capacitance 與實際波形條件，S11 建立 frequency-dependent impedance、ripple thermal stress 與系列壽命條件；研究端把它們整理成同一選型次序
boundary: 四道檢查是研究與選型框架，不是跨材料的通用計分、唯一設計流程或 qualification；不支持料號、顆數、供應商、份額、價格、訂單、收入或獲利
verification_needed: 同一 production platform 的 part-specific curves、完整 ripple spectrum、熱邊界、mission profile、qualification pass／fail、BOM 與 field reliability
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: Eaton 的超級電容模組 FAQ 以 E＝½CV² 表示理想儲能，並以量測電壓平方除設計電壓平方表示 state of charge；因此容量相同時，工作電壓與可用電壓窗仍會改變可交出的理想能量
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-08-14
basis: S12 的 Energy and Power Calculation 與 State of Charge 段落直接列出兩個平方關係
boundary: 只證實 Eaton 超級電容模組的理想計算關係；沒有納入電壓相依容量、ESR／ESL、轉換效率、漏電、熱、老化、保護下限、AI 平台或量產 BOM
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: Eaton 的超級電容應用指南在定電流放電近似下把總壓降分成 I×ESR 與 I×t／C，並指出短時間高電流脈衝較受 ESR 主導，較低電流長時間放電較受 capacitance 主導
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-08-14
basis: S13 的 Discharge Characteristics 直接給出 Vdrop＝I×(R＋t／C)，並逐段說明 resistive／capacitive component 與 current／duration 邊界
boundary: 這是定電流、固定參數的超級電容近似；不含 ESL、走線、控制迴路、定功率負載、非線性容量、熱、老化或其他電容技術，不是完整 AI PDN 通過公式
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
claim: TI 的應用報告以 ΔI×並聯 ESR 說明非常快速負載階躍的最佳情況立即壓降，並以 Zmax＝可容許 ΔV／ΔI 建立分散式供電匯流排的目標阻抗；同一文件亦指出單一電容不能覆蓋全部頻帶
supporting_source_ids: S14
contrary_source_ids:
as_of: 2006-02-01
basis: S14 PDF pp.7–10 分列 C／ESR／ESL、自共振、多電容頻帶配置、快速 load transient 與 ΔV／ΔI 目標阻抗
boundary: 文件算例屬指定 PTH regulator 與元件組合；立即 ESR 壓降不是總壓降，目標阻抗也必須對到頻帶、走線、ESL、控制迴路與量測，不支持 AI rack 的共同數值或材料排名
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: inference
status: active
claim: 電容研究應把可用能量、hold-up 電壓窗、等效串聯電阻壓降與電容量壓降分成四本帳，再以位置、負載語意、頻帶、熱與壽命組成同一份十欄護照；只有 µF、額定電壓或單點 ESR，均不足以推導替代、系統價值或公司受惠
supporting_source_ids: S9,S10,S11,S12,S13,S14
contrary_source_ids:
as_of: 2026-08-14
basis: S12 建立電壓平方能量，S13 分開 ESR 與 capacitance 壓降，S14 建立頻帶與目標阻抗；S9–S11 補上有效容量、熱與任務壽命，研究端將其整理成可重建護照
boundary: 四本帳與十欄護照是本文的研究框架，不是唯一設計流程、跨材料評分、qualification 規格或需求預測；不支持料號、顆數、平均售價、份額、訂單、收入、毛利或股價尚未反映
verification_needed: 同一 production platform 的具名位置、拓撲、電壓窗、負載波形、part-specific C／ESR／ESL／Z 曲線、熱與壽命、qualification、BOM 及客戶—供應商財務共同鍵
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

## 同樣的容量，為什麼仍不能互換：四道可用能力檢查

| 本文 4 把尺 | 先回答什麼 | 讀資料表時核對什麼 | 還不能因此判定 |
|---|---|---|---|
| 1. 有效容量 | 在實際直流電壓與溫度下，還剩多少容量？ | 具名料號的直流偏壓、交流電壓與溫度曲線；不能只抄標稱容量 | 所有積層陶瓷電容採同一降額，或其他材料也照同一曲線 |
| 2. 頻率阻抗 | 在真正要處理的紋波或瞬態頻帶，阻抗是否夠低？ | 阻抗、等效串聯電阻、等效串聯電感與自共振頻率隨頻率及溫度的曲線 | 容量相同就有相同濾波效果，或低阻抗在所有控制迴路都更好 |
| 3. 紋波溫升 | 實際交流電流流過元件後，會升溫多少？ | 紋波電流頻譜、等效串聯電阻、環境溫度、散熱面積、板子與冷卻條件 | 額定紋波值可脫離頻率與溫度直接跨料號比較 |
| 4. 任務壽命 | 在預定電壓、溫度、運轉時間與冷卻條件下，能撐多久？ | 產品適用的壽命曲線或模型、熱點溫度、額定電壓與電流、加速試驗及失效判準 | 供應商計算值等於客戶保固、現場可靠度或所有電容技術的共同壽命 |

同樣的 µF 只是一個起點。這張表只把選型縮成四個需要同時通過的工作條件；它不能替任何平台指定材料、料號、顆數或供應商。

**第一道先把標稱容量換成有效容量。** Murata 與 TDK 都提醒，高介電常數積層陶瓷電容施加直流電壓後，工作中的容量可能不同於資料表標稱值。要用具名料號在實際電壓與溫度下的曲線，不能拿單一示例百分比套遍所有產品。

**第二道看目標頻帶的阻抗。** KEMET／YAGEO 的鋁電解指南把容量、等效串聯電阻與等效串聯電感拆開；頻率升高到共振區之後，元件可能由容性轉為感性。這解釋了為什麼相同容量不等於相同的瞬態或濾波能力。

**第三道把紋波換成溫升。** 交流電流流過等效串聯電阻會產生損耗，但實際溫升還取決於電流頻譜、環境溫度、散熱面積、板子與冷卻。只比較額定紋波安培數，仍可能把不同測試條件混在一起。

**第四道才核對任務壽命。** KEMET／YAGEO 的 ESE 公式只適用指定鋁電解系列，TDK 的溫升建議也只屬其高壓積層陶瓷電容情境。平台要用自己的任務剖面、加速試驗與失效判準完成資格驗證，不能把供應商示例直接當成現場壽命。

## 同樣 1,000 µF，為什麼可用能量與瞬態壓降仍不同

前一節回答「這顆電容在工作條件下還能不能用」；這一節再把兩種常被混在一起的任務拆開：
hold-up／ride-through 是能量與電壓窗問題，負載階躍是時間、電阻、電感、頻帶與控制問題。
Eaton 的超級電容資料把理想能量寫成 ½CV²，也把定電流壓降拆成 I×ESR 與 IΔt／C；
TI 的電源應用報告則用 ΔI×Z 把可容許壓降連回目標阻抗，並提醒單一電容不能覆蓋全部頻帶。

### 第一本帳：可用能量看電壓平方，不只看 µF

電容從 Vhi 降到 Vlo 的理想可用能量是 ½C×（Vhi²−Vlo²）。下面固定 C＝1,000 µF，
而且兩個案例的 Vlo／Vhi 都是 5／6；只改電壓尺度，結果就不同。

| 假想能量案例 | C | Vhi→Vlo | 理想可用能量 | 能回答什麼 | 仍沒算什麼 |
|---|---:|---:|---:|---|---|
| A | 1,000 µF | 48→40V | 0.352J | 指定理想電壓窗內的能量 | 有效容量、ESR／ESL、效率、熱、保護與壽命 |
| B | 1,000 µF | 12→10V | 0.022J | 同上 | 同上 |

A 是 B 的 16 倍，並不是 48V 系統一定需要更多電容；它只示範能量隨電壓平方改變。
反過來說，較高匯流排電壓在相同理想能量與電壓窗假設下，也可能減少所需容量或顆數，
所以「電壓升級」不能直接翻譯成「電容價值量同比增加」。

### 第二本帳：hold-up 要先固定負載語意與最低電壓

若把負載簡化成定功率 P，忽略損耗、轉換器限流、電容量變化與保護動作，維持 Δt 所需的
理想容量可寫成 C＝2PΔt／（Vhi²−Vlo²）。固定 P＝1kW、Δt＝10ms、Vhi＝48V：

| 假想 hold-up 案例 | 允許電壓窗 | 理想所需容量 | 相對結果 |
|---|---:|---:|---:|
| H1 | 48→44V | 54,347.826 µF | 電壓窗較窄，需要較多容量 |
| H2 | 48→40V | 28,409.091 µF | 電壓窗較寬，需要較少容量 |

H1 是 H2 的 1.913 倍。這個差異來自假想的最低工作電壓，而不是任何 OCP、Eaton、TI
或 AI 平台規格。真實設計還要加入效率、有效容量、容差、串並聯均壓、老化、最大電流、
重新充電、故障模式與轉換器可接受的輸入範圍。

### 第三本帳：負載階躍要把 ESR 與電容量壓降分開

在 Eaton 所述的定電流、固定參數近似下，ΔV＝I×ESR＋IΔt／C。固定 C＝0.1F、
I＝100A、Δt＝1ms，電容量項都是 1.0V；只把 ESR 從 5mΩ 改成 10mΩ：

| 假想脈衝案例 | ESR 壓降 | 電容量壓降 | 兩項合計 | 判讀 |
|---|---:|---:|---:|---|
| P1：ESR 5mΩ | 0.5V | 1.0V | 1.5V | 此時間窗內電容量項較大 |
| P2：ESR 10mΩ | 1.0V | 1.0V | 2.0V | 相同 C 仍因 ESR 不同而多掉 0.5V |

這不是完整 PDN 模擬。更短的前緣還會受 ESL、連接器、母排與走線影響；更長的時間窗則會
進入控制迴路、上游轉換器、溫升與電壓相依容量。把 ESR 壓降和 IΔt／C 壓降分帳，目的
是找出瓶頸，不是把兩項相加後就宣布客戶資格驗證通過。

### 第四本帳：目標阻抗是頻帶契約，不是單一料號標籤

假想負載增加 20A、可容許壓降 50mV，Zmax＝ΔV／ΔI＝2.5mΩ。若電容群並聯 ESR
已是 1.5mΩ，立即電阻壓降是 30mV，占壓降預算 60%，名目只剩 20mV。剩下的 40%
不能自動全配給電容量：ESL、佈局、供電平面、頻率相依阻抗與控制迴路都要用同一量測
參考點和頻帶核對。TI 的報告因此用不同類型電容覆蓋不同頻帶，而不是尋找一顆「全頻萬能」電容。

以上共有 N＝2 個能量案例、N＝2 個 hold-up 電壓窗、N＝2 個定電流脈衝案例及 N＝1 個
目標阻抗算例。Python Fraction 與獨立 awk 在顯示精度內完全一致；這些是固定假想輸入的
確定性換算，不是抽樣、元件量測、rack 測試或客戶驗收，因此沒有 sampling SE／t，也沒有
需求、顆數、價格、收入、毛利或公司效果。

### 多空小作文共用的電容能量—瞬態十欄護照

| 護照欄位 | 必須留下什麼 | 缺少時容易犯的錯 |
|---|---|---|
| 1. 位置與任務 | CBU、DC-link、board bulk 或 near-die；hold-up、load step、ripple 或 decoupling | 把不同時間尺度重複加總 |
| 2. 負載語意 | 定功率／定電流、ΔI、Δt、duty cycle、波形與頻譜 | 把定電流公式套到定功率負載 |
| 3. Bank 拓撲 | 具名料號、串並聯、均壓、冗餘、連接器與 layout | 用單顆規格推整個模組 |
| 4. 電壓窗 | 額定、derating、Vhi、Vlo、保護與轉換器工作範圍 | 用滿電能量冒充可用能量 |
| 5. 實際容量 | nominal／effective C、容差、偏壓、溫度與老化 | 用標稱 µF 當全生命週期容量 |
| 6. 能量交付 | 所需／可交能量、時間、效率、漏電與邊界 | 把理想 ½CV² 當系統可用輸出 |
| 7. 阻抗頻譜 | ESR、ESL、Z(f)、溫度／老化、SRF 與量測參考點 | 用單點 ESR 宣稱全頻通過 |
| 8. 壓降拆解 | resistive、capacitive、inductive、layout 與 control response | 只報總壓降，找不到真正瓶頸 |
| 9. 熱、壽命與故障 | ripple heat、環境／冷卻、mission life、inrush、recharge、fault | 把一次脈衝能力當長期可靠度 |
| 10. 商業共同鍵 | 客戶 qualification、production BOM、替代顆數、成本、份額與財務分母 | 從公式直接跳到訂單或獲利 |

**多方版本要成立，** 必須看到同一平台的功率波形、電壓窗或瞬態預算更嚴格，且供應商以
更高可用能量、更低頻帶阻抗、可控溫升與壽命完成 qualification；之後還要證明每系統價值、
份額、量產與財務貢獻，而不只是規格表變漂亮。

**空方版本要成立，** 可能是較高匯流排電壓讓相同理想能量所需容量下降、主動控制減少
被動元件、CBU／BBU／上游轉換器重新分工，或更高單價被更少顆數抵銷。只要缺 production
BOM、替代前後顆數、qualification 與財務分母，就不能把「AI 功率更大」寫成所有電容同步受惠。

## 怎麼用這張表判讀公司新聞

1. **先找客戶的量產架構**：供應商參考設計只能證明做得到；客戶平台文件才可能固定元件位置與接口。
2. **再找具名產品與驗證**：料號、可用電壓窗、負載波形、有效容量、阻抗頻譜、壓降拆解、溫度、壽命及失效測試，必須對到同一個應用位置。
3. **最後才對回公司財務**：客戶與供應商雙向確認後，再查出貨量、平均售價、份額、收入與毛利；缺一層就維持觀察。
4. **避免重複計算**：高規格元件可能減少顆數或取代另一層零件，不能直接加總每家供應商的機會地圖。

## 研究判定

- **目前可保留的結論**：先分機櫃儲能、高壓直流匯流排、電路板與封裝／晶片旁四個位置，再核對有效容量、可用能量、電壓窗、ESR／電容量壓降、頻率阻抗、紋波溫升與任務壽命，才能討論元件是否可替換。
- **可信度為中而不是高**：OCP 與 TI 支持機櫃架構，TDK、Murata 與 KEMET／YAGEO 支持供應商技術邊界；目前仍缺同一量產平台的完整供電路徑、共同測試與材料清單。
- **目前不能發布的結論**：所有電容同步增加、指定材料或台灣公司勝出、顆數、平均售價、市占、訂單、獲利，以及市場是否已反映。
- **需要看到什麼才能前進**：買方量產文件與供應商申報雙向對齊具名產品、客戶資格驗證、實際配置、出貨及財務分母。

## 來源

- [OCP：Diablo 400 Rack and Power Specification 0.7.0](https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf)
- [Texas Instruments：800 VDC architecture 與 EDLC CBU](https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia.html)
- [TDK：FY March 2026 Full Year Performance Briefing](https://www.tdk.com/system/files/2026_4q01_0mqf56xw_en.pdf)
- [Murata：AI System with Advanced Packaging Webinar Q&A](https://www.murata.com/-/media/webrenewal/campaign/events/asean/2026/apr26_ai-system-with-advance-packaging/qna.ashx?cvid=20260425083237000000&la=en-sg)
- [TDK：高 dV/dt 電路的 MLCC 選型與實際波形評估](https://product.tdk.com/en/techlibrary/applicationnote/snubber_mlcc.html)
- [Murata：電容量的直流與交流電壓特性](https://article.murata.com/en-eu/article/voltage-characteristics-of-electrostatic-capacitance)
- [KEMET／YAGEO：ESE 鋁電解電容應用與操作指南](https://content.kemet.com/datasheets/KEM_A4055_ESE.pdf)
- [Eaton：超級電容模組常見問題與能量計算](https://www.eaton.com/sg/en-us/products/electronic-components/faq/supercapacitor-modules-frequently-asked-questions.html)
- [Eaton：超級電容應用指南與放電壓降拆解](https://www.eaton.com/us/en-us/products/electronic-components/topics/supercapacitor-applications-guide.html)
- [Texas Instruments：Input and Output Capacitor Selection](https://www.ti.com/lit/an/slta055/slta055.pdf)
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

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C6,C7,C8,C9
metric: 具名料號在實際偏壓、溫度、頻率與紋波下的有效容量、阻抗、溫升、壽命及 qualification 結果
source_ids: S9,S10,S11
watch_source_ids: S6,S7
frequency: monthly
next_check: 2026-09-01
trigger: 平台與元件供應商公布同一料號、工作點、完整頻譜、熱邊界、任務剖面及客戶 pass／fail，可逐步重建四道可用能力檢查
invalidation: 量產平台證明本文四道檢查遺漏決定性條件，或實際 qualification 顯示標稱容量已足以在所有相關位置可靠判定互換
-->

## 什麼會推翻這篇

- Production platform 證明不同位置與頻帶的電容可在相同可靠度、成本與空間條件下完全互換，使本文分層失去解釋力。
- OCP／平台移除 CBU 或重新定義其任務，而現場資料顯示它與 BBU／board bulk 的邊界不成立。
- 若台灣公司長期只有「AI、高壓、被動元件」敘事而沒有具名產品、資格、量產與財務分母，族群 route 應維持待驗證，不能因題材熱度升格。
