# 晶片貼得更近，量產反而更難：混合接合要同時守住五個製程窗口

<!-- research_topic
topic_id: MI-2026-08-02-HYBRID-BONDING-READINESS
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-05-28
last_reviewed_at: 2026-08-02
review_due: 2026-08-16
source_type: mixed
publisher: imec
publisher_domain: imec-int.com
canonical_url: https://www.imec-int.com/en/press/imec-and-ev-group-demonstrate-wafer-wafer-hybrid-bonding-200nm-interconnect-pitch-and-record
source_chain_id: hybrid-bonding-pdk-test-vehicle-tool-20260802
stock_ids:
group_ids: packtest,semiequip,material
trigger_type: advanced_packaging_readiness_update
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C4
base_confidence: medium
confidence_basis: imec 的探索型 PDK與200nm試驗車，加上 Applied Materials 的整合設備客戶使用，可由兩個獨立來源群組重建成熟度階梯；但具名量產產品、客戶資格、良率、throughput 與台灣公司財務映射仍未公開
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_hybrid_bonding_readiness_sources_captured
evidence: source_chain:hybrid-bonding-pdk-test-vehicle-tool-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_pathfinding_test_vehicle_customer_tool_use_and_hvm_evidence
evidence: sources:S1,S2,S3
-->
<!-- transition
date: 2026-08-08
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:readability
-->

<!-- research_source
source_id: S1
role: other_primary
source_kind: document
publisher: imec NanoIC
title: NanoIC opens access to fine-pitch RDL and D2W hybrid bonding interconnect PDKs
published_at: 2026-03-02
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.imec-int.com/en/press/nanoic-opens-access-first-ever-fine-pitch-rdl-and-d2w-hybrid-bonding-interconnect-pdks
locator: exploratory／pathfinding PDK、design rules、validated building blocks 與 future fabrication-ready tape-out 段落
limitation: 這是 pilot line 的 early-access pathfinding PDK；尚未具備完整 tape-out 能力，也不證明客戶量產、良率、throughput 或供應商收入
independence_group: imec
-->

<!-- research_source
source_id: S2
role: other_primary
source_kind: document
publisher: imec and EV Group
title: Wafer-to-wafer hybrid bonding with 200nm interconnect pitch and record overlay accuracy
published_at: 2026-05-28
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.imec-int.com/en/press/imec-and-ev-group-demonstrate-wafer-wafer-hybrid-bonding-200nm-interconnect-pitch-and-record
locator: 200nm Cu pad pitch test vehicle、sub-40nm post-bond overlay、full 300mm wafer 與 CMP／SiCN／pre-bond correction 段落
limitation: 結果來自 imec 試驗車與合作設備；robust、highly yielding 與 world first 是發布者措辭，未提供量產客戶、good-die yield、產能或成本
independence_group: imec-evg-joint
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Applied Materials
title: Applied Materials unveils Kinex integrated die-to-wafer hybrid bonding system
published_at: 2025-10-07
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investors.appliedmaterials.com/node/28506/pdf
locator: PDF page 1 lines 17–31；Kinex integration、inline metrology 與 multiple logic／memory／OSAT customers
limitation: 公司稱設備被多家客戶使用，但未揭露客戶名稱、qualification 階段、出貨量、良率、throughput、收入或終端產品
independence_group: applied-materials-besi
-->

<!-- research_source
source_id: S4
role: other_primary
source_kind: living_index
publisher: imec
title: imec 3D integration research and press updates
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.imec-int.com/en/expertise/cmos-advanced/3d-integration
locator: 2026-08-02 建立的 hybrid bonding、W2W／D2W 與後續試驗結果重查入口
limitation: living index 只用來偵測新文件；頁面敘述本身不會自動升級量產或公司財務狀態
independence_group: imec
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: living_index
publisher: Applied Materials
title: Applied Materials investor news releases
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.appliedmaterials.com/news-releases
locator: 2026-08-02 建立的 Kinex、hybrid bonding、customer qualification 與 advanced packaging 財務更新入口
limitation: 新聞索引只用來找後續文件；產品行銷、合作或市場預測不能代替客戶 qualification 與財務證據
independence_group: applied-materials
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: imec NanoIC 於 2026-03-02 公開的 fine-pitch RDL 與 D2W hybrid bonding PDK 是 early-access exploratory／pathfinding 版本，完整 fabrication-ready tape-out 能力仍被列為後續成熟方向
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-03-02
basis: S1 直接區分 first release、pathfinding PDK 與未來 complete fabrication-ready toolset
boundary: PDK 開放不等於實體產品已 tape-out、客戶量產、製程良率或設備材料需求已形成收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: imec 與 EVG 在 300mm wafer 試驗車上展示 200nm Cu interconnect pad pitch，並報告所有 die 的 post-bond overlay vector 低於 40nm
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-05-28
basis: S2 明列 test vehicle、200nm pad pitch、300mm wafer 與 100% dies 的 sub-40nm overlay result
boundary: 這是合作研發試驗車的量測結果，不是具名客戶產品的 HVM yield、產能、成本或可靠度資料
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: Applied Materials 表示 Kinex 整合 D2W hybrid bonding 關鍵流程與 inline metrology，並已被多家 leading-edge logic、memory 與 OSAT 客戶使用
supporting_source_ids: S3
contrary_source_ids:
as_of: 2025-10-07
basis: S3 PDF page 1 直接列出 integrated process steps、overlay measurement 與 multiple customer categories
boundary: used by multiple customers 沒有揭露客戶、qualification、量產產品、出貨量、收入或高量產良率，不能自動解讀為 HVM adoption
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: active
claim: Hybrid bonding 已同時跨入設計規則、細間距試驗車與整合設備客戶使用三個節點，但現有公開證據仍不足以把整條技術路徑判定為具名產品的高量產成熟
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-08-02
basis: S1 明示 pathfinding 而非 tape-out-ready，S2 是可路由試驗車，S3 只到未具名客戶使用；三者能建立成熟度階梯但沒有完成 HVM 的共同分母
boundary: 不推估 hybrid bonding TAM、量產良率、設備份額、台灣公司訂單或股價；不同 D2W／W2W 用例也不能用單一節距直接比較
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: Universe 內封測、設備或材料公司已因上述 200nm W2W／D2W hybrid bonding 路徑取得可辨識量產訂單、收入或獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有來源只涵蓋 imec／EVG 試驗線與 Applied Materials／Besi 整合設備，沒有台灣公司與客戶對同一製程步驟的雙向核對
boundary: 不以先進封裝能力、一般 CMP／清洗／檢查產品或 OSAT 身分建立公司受惠線
verification_needed: 晶圓廠或 OSAT 的具名產品 qualification，搭配台灣公司料號、製程步驟、量產出貨及財務貢獻
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C4
metric: Hybrid bonding 由 PDK／試驗車進入具名產品 qualification、HVM yield、throughput 與可靠度的成熟度
source_ids: S1,S2,S3
watch_source_ids: S4,S5
frequency: event_driven
frequency_detail: imec、設備商、晶圓廠或 OSAT 發布新 PDK、test chip、qualification 或 HVM 結果時重審
next_check: 2026-08-16
trigger: 具名邏輯或記憶體產品完成客戶 qualification，且公開可定位的 good-die yield、throughput 或量產可靠度
invalidation: 後續證據持續停在 pathfinding PDK、試驗車或未具名客戶使用，HVM 成熟度維持未證並下修商業急迫性
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C5
metric: 台灣封測、設備與材料公司的 hybrid bonding 客戶、製程步驟、量產與財務貢獻
source_ids: S2,S3
watch_source_ids: S5
frequency: quarterly
frequency_detail: 每季重查公司法說、財報與客戶平台文件，要求同一料號或製程步驟可雙向核對
next_check: 2026-10-31
trigger: 台灣公司與客戶對同一 hybrid bonding 產品或製程完成 qualification／量產雙向核對，並出現收入或毛利資訊
invalidation: 公司只使用 hybrid bonding、2.5D／3D 或先進封裝概念詞，未揭露客戶、產品、階段與財務足跡
-->

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave4_packaging_learning_no_conclusion_change
evidence: editorial:plain_language_wave4
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave94_hybrid_bonding_paths_process_windows_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **混合接合（Hybrid bonding）**：不靠凸塊隔開兩層晶片，而讓平坦介電層與細小銅接點直接貼合；連線可更短、更密，表面與對準條件也更嚴格。
- **凸塊（Bump）**：傳統封裝常用的微小金屬連接點，會在兩層晶片之間留下高度；移除凸塊不代表接合製程就更簡單。
- **接點間距（Pitch）**：相鄰接點中心之間的距離。間距變小代表接點更密，不等於良率、成本或量產能力已經更好。
- **晶粒（Die）**：晶圓切割後的單顆晶片。晶粒能否先被挑選，會改變後續接合的良率分母。
- **晶圓（Wafer）**：尚未切成單顆晶粒的圓形半導體基板；整片處理效率高，但也要一起管理全片缺陷與對準。
- **單顆晶粒接晶圓（D2W）**：先挑選單顆晶粒，再逐顆接到目標晶圓；可混搭不同晶粒，但放置速度與逐顆對準也要計入。
- **晶圓接晶圓（W2W）**：把兩片晶圓整面對準後一次接合；平行處理效率高，但上下晶圓的良品位置與缺陷分布會一起影響結果。
- **設計製程套件（PDK）**：把製程可做的線寬、間距、材料與驗證元件整理成設計規則；有套件不等於已有實體量產產品。
- **探索型設計製程套件（Pathfinding PDK）**：讓設計者先找可行路徑的早期版本；可以開始試畫與驗證，不代表已具備完整送製能力。
- **試驗結構（Test vehicle）**：為量測製程、電性與缺陷而設計的測試結構，不是客戶最終商品，也不能直接代表量產良率。
- **對準誤差（Overlay）**：上下兩層接點實際位置的偏差；接點越密，可容忍的偏差通常越小。
- **表面平坦度**：接合前表面的高低差與粗糙程度；表面不夠平，即使平均位置正確也可能貼不牢或導通失敗。
- **潔淨度與顆粒控制**：避免灰塵、殘留物或微小顆粒卡在接合面；局部污染可能造成空洞、未接合或電性缺陷。
- **化學機械研磨（CMP）**：用化學反應與機械研磨把晶圓表面整平，控制介電層、銅接點與凹陷高度。
- **重新佈線層（RDL）**：在晶片或封裝表面重新安排金屬線與接點位置，讓不同晶片能接到更細的互連。
- **介電層**：隔離導電線路的絕緣材料；混合接合時，介電層表面品質會和銅接點一起決定貼合結果。
- **銅接點**：上下兩層用來傳遞訊號或電力的細小銅墊；不只要對準，也要控制表面狀態與接合後電阻。
- **已知良品（Known good die）**：在接合前已完成篩選、較有把握正常工作的晶粒；能先挑良品不代表後續接合不會新增缺陷。
- **合格晶粒良率（Good-die yield）**：經製程與測試後可用晶粒占投入晶粒的比例；必須說清投入、測試與合格定義才能比較。
- **電性良率（Electrical yield）**：通過指定電性測試的比例；接點對準達標不等於所有電路都能正常工作。
- **線上量測（Inline metrology）**：在製程進行中量測位置、表面或缺陷，及早發現漂移；能量到不等於製程已穩定量產。
- **客戶資格認證（Qualification）**：客戶依功能、可靠度與製造條件確認產品是否可採用；設備被使用不等於認證已完成。
- **穩定大量生產（HVM）**：在持續生產中同時守住良率、產能、可靠度與成本，而不是只做出一次試驗結果。
- **每小時產能（Throughput）**：設備或產線在一定時間內可完成的數量；速度要和良率、停機、返工與成本一起看。
- **長期可靠度**：產品經過時間、溫度循環與使用負載後仍能維持功能；短期導通成功不能替代長期測試。
- **返工能力**：發現接合問題後是否能拆解、重做或挽救產品；不同接合路徑的可返工程度會影響實際成本。
- **設計定稿送製（Tape-out）**：設計完成並交給製造端產生實體晶片的節點；探索型規則可用不等於已經完成送製。
- **試製晶片（Pilot silicon）**：用早期製程做出的實體晶片，用來驗證設計與製造；仍排在穩定量產之前。
- **委外封測廠（OSAT）**：承接晶粒封裝、互連與測試的外包廠商；具備一般先進封裝能力不等於已量產特定混合接合產品。
- **Kinex**：Applied Materials 與 Besi 合作的單顆晶粒接晶圓整合設備；多類客戶使用設備，仍不等於具名產品已量產。
- **imec**：進行半導體研發與試驗線驗證的研究機構；試驗結果可證明技術能力，但不能替代客戶產品量產資料。
- **EV Group（EVG）**：參與本輪晶圓接晶圓試驗的設備公司；合作試驗證明設備角色，不等於市場份額或台灣供應商受惠。

### 三句話抓重點

- 兩層晶片讓平坦表面與細小銅接點直接貼合後，連線可以更短、更密，但一點灰塵、高低差或錯位都可能造成失敗。
- 本輪已有「設計規則可用、試驗結構做出細接點、整合設備被多類客戶使用」三種進展，證明技術往前走了一段。
- 但還沒有具名產品認證、穩定良率、每小時產能、長期可靠度、量產出貨與供應商收入，不能把試驗成功直接讀成量產成熟。

### 為什麼重要

混合接合讓邏輯、記憶體與小晶片之間的接點更密，可能縮短資料路徑與降低傳輸能耗；但接點越密，
表面平坦度、潔淨度、對準、良品挑選與接合後檢查就越需要一起控制。只看最小接點間距，會把研發
紀錄誤讀成量產良率，也容易把材料、設備、封測與客戶產品四種不同責任混成同一種受惠。

### 接下來怎麼追

- 先問每份新資料位於設計規則、試驗結構、設備使用、客戶認證、穩定量產還是財務貢獻哪一關。
- 把逐顆接合與整片接合分開追蹤，分別核對良率分母、對準分布、每小時產能、返工與長期可靠度。
- 公司映射必須同時找到客戶端的具名製程與供應商端的料號、量產及收入，缺一邊就維持待驗證。

### 想一想

- 如果所有接點都對得很準，還有哪些灰塵、表面高低差、壞晶粒與熱循環問題可能讓成品失敗？
- 逐顆挑選後再接合，與兩片晶圓整面接合，為什麼不能只用一個良率分母比較？
- 設備已被客戶使用後，還要看到哪些認證、產能、可靠度與財務資料才算量產成熟？

## 先分清兩種「貼法」的良率分母

| 本文兩條接合路徑 | 怎麼接 | 主要優點 | 主要風險 | 為什麼不能直接比較 |
|---|---|---|---|---|
| 單顆晶粒接晶圓（D2W） | 先挑單顆晶粒，再逐顆放到目標晶圓 | 能先挑已知良品，也較容易混搭不同尺寸或製程的晶粒 | 逐顆放置速度、每顆對準、接合後新增缺陷與返工 | 良率從「已挑過的晶粒」開始算，不能和整片晶圓用同一投入分母 |
| 晶圓接晶圓（W2W） | 兩片晶圓整面對準後一次接合 | 可同時處理大量接點，平行效率高 | 上下晶圓良品位置是否匹配、全片翹曲、顆粒與局部錯位 | 分母同時受到兩片晶圓缺陷分布與接合後成品影響，不能只比最小間距 |

這張表只說明本文為何要把兩條路徑分開閱讀，不是完整製程規格，也不代表其中一條一定更便宜、
良率更高或更早量產。

## 再看五個量產窗口如何接力

| 本文五個量產窗口 | 先回答什麼 | 主要接力角色 | 失敗會怎樣 | 本輪可確認到哪裡 |
|---|---|---|---|---|
| 1. 設計規則與試驗結構 | 設計者知道哪些線寬、間距與材料可製造嗎？ | 研究機構、設計工具與晶圓製程團隊 | 規則畫得出來，實體卻做不出或無法量測 | 已有探索型設計規則與細接點試驗結構；完整送製能力仍未公開 |
| 2. 表面平坦與銅高度 | 介電層、銅接點與凹陷高度是否落在可接合窗口？ | 材料、研磨、沉積與表面處理設備 | 局部接觸不足、空洞、電阻不穩或整片報廢 | 試驗文件列出研磨與表面條件；沒有具名產品長期製程分布 |
| 3. 潔淨與顆粒控制 | 接合面能否在搬運、清洗與貼合前維持乾淨？ | 清洗設備、化學材料、晶圓廠與封測廠 | 一顆微粒就可能造成局部未接合或缺陷擴散 | 已知潔淨是製程節點；沒有量產缺陷密度與停機資料 |
| 4. 對準、接合與量測 | 上下接點是否持續對準、導通，並能及早發現漂移？ | 接合設備、線上量測、檢查與製程整合團隊 | 接點錯位、開路、短路，或直到後段才發現損失 | 試驗結構有細間距與對準結果，整合設備也被多類客戶使用 |
| 5. 良率、產能與可靠度 | 好產品比例、每小時產能、返工與長期壽命能否一起達標？ | 晶圓廠、封測廠、產品客戶與財務團隊 | 技術可做卻成本過高、產量不足或使用後失效 | 沒有具名產品良率、產能、長期可靠度、出貨與收入 |

五個窗口是接力關係：前一站達標不會自動替下一站畢業。這是本文的製程責任地圖，不是供應商名單、
訂單判定、公司快慢或投資排序。

## 最後用六關分開技術進展與收入

| 本文六關 | 這一關要證明 | 本輪已有證據 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 開放設計入口 | 設計者有可用規則與驗證元件 | NanoIC 提供探索型設計製程套件 | 完整送製工具、實體試製晶片與設計採用 | 規則可用不等於產品已做出或量產 |
| 2. 試驗結構成功 | 特定接點結構能被製作、對準與量測 | imec／EVG 在 300 毫米晶圓試驗結構展示 200 奈米接點間距與低於 40 奈米的接合後對準誤差 | 電性良率、缺陷分布、重複批次與長期可靠度 | 對準達標不等於所有電路正常或良率 100% |
| 3. 整合設備與流程使用 | 接合與量測步驟能在整合設備中運作 | Applied Materials 表示 Kinex 已被多類邏輯、記憶體與封測客戶使用 | 具名客戶、使用階段、設備數量與產品結果 | 客戶使用不等於資格認證、量產或設備收入份額 |
| 4. 具名產品資格認證 | 特定產品通過客戶功能與可靠度要求 | 未公開 | 客戶與製造端對上同一產品、製程與認證結果 | 試驗結構或未具名客戶不能替代產品認證 |
| 5. 穩定大量生產 | 良率、每小時產能、返工、可靠度與成本能持續達標 | 未公開 | 具名產品的批次良率、產能、停機、可靠度與成本 | 單次紀錄、最小間距或設備安裝不等於穩定量產 |
| 6. 重複出貨與形成收入 | 供應商產品或服務可重複交付並反映在財務 | 未公開 | 客戶與供應商雙向核對料號、量產出貨、收入或毛利 | 製程需要某類材料或設備不等於台灣公司已受惠 |

本輪三份核心資料只把公開證據推進到第 1～3 關；第 4～6 關仍缺資料。六關是本文的查證順序，
不是共同產業標準，也不替公司建立量產名次、供應份額、訂單或財務貢獻。

## 來源與證據邊界

- [imec NanoIC：fine-pitch RDL 與 D2W pathfinding PDK](https://www.imec-int.com/en/press/nanoic-opens-access-first-ever-fine-pitch-rdl-and-d2w-hybrid-bonding-interconnect-pdks)
- [imec／EVG：200nm W2W hybrid bonding test vehicle](https://www.imec-int.com/en/press/imec-and-ev-group-demonstrate-wafer-wafer-hybrid-bonding-200nm-interconnect-pitch-and-record)
- [Applied Materials：Kinex integrated D2W hybrid bonder](https://investors.appliedmaterials.com/node/28506/pdf)

本篇沒有把 imec 的效能改善、Applied Materials 的產品優勢或「highly yielding」措辭拿來做跨公司數字比較；
也沒有 HVM 良率、每小時產能、每片成本與市場份額的共同定義，因此 `cross_company_numbers` 維持 false。

## 影響路由

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-31
rationale: D2W／W2W hybrid bonding 會改變 known-good-die、接合、檢查與可靠度流程，但本輪沒有 universe OSAT 的具名客戶產品與量產財務證據
evidence_boundary: 一般先進封裝能力、技術論壇或設備安裝不等於 hybrid bonding 客戶 qualification、量產訂單或毛利
-->

<!-- impact
group_id: semiequip
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-31
rationale: CMP、清洗、bonding、overlay metrology 與檢查是明確製程節點，但已證實工具來自 EVG、Applied Materials／Besi，尚未核對 universe 設備商
evidence_boundary: 製程需要某類工具不等於任一台灣設備商已通過客戶 qualification 或取得量產收入
-->

<!-- impact
group_id: material
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-31
rationale: SiCN、銅表面、清洗化學品與 CMP 耗材形成材料研究入口，但公開試驗流程未揭露 universe 材料供應商
evidence_boundary: 材料類別被研究機構使用不證明台灣公司供貨、份額、獨家性或財務貢獻
-->

## 下一個可證明／否定的節點

- NanoIC PDK 由 pathfinding 進入 fabrication-ready tape-out，並有實體 silicon 結果。
- 具名邏輯、記憶體或 OSAT 客戶公布 D2W／W2W qualification、good-die yield、throughput 與可靠度。
- 台灣公司與客戶文件能對上同一工具、材料或製程，並披露量產與財務足跡。
- 若未來一年仍只有試驗車與未具名 customer use，研究應把商業成熟度維持在 capability，而非 HVM。
