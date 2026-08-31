# NVIDIA Vera Rubin 由路線圖進入量產與首波部署

<!-- research_topic
topic_id: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-07-27
source_published_at: 2026-07-21
last_reviewed_at: 2026-08-12
review_due: 2026-08-15
source_type: official_company
publisher: NVIDIA
publisher_domain: nvidia.com
canonical_url: https://blogs.nvidia.com/blog/vera-rubin/
source_chain_id: nvidia-vera-rubin-20260721
stock_ids: 2376,2382,3231,6669
group_ids: memory,pcb,powersupply,serverodm,thermal
trigger_type: product_ramp_and_deployment
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C11
base_confidence: medium
confidence_basis: NVIDIA 8 月 26 日財報與法說已把 Vera Rubin 推進到公司所稱的 full production、8 月開始 production shipments 與主要客戶類別皆有採購單；CoreWeave、Google 與三家台灣系統廠一手文件另可拆分型錄、未來工廠、整櫃驗證與雲端供應語言，但公開資料仍未給出出貨物件與數量、具名 ODM、客戶驗收或台灣公司收入與獲利橋接
cross_company_numbers: false
schema_migrated_at: 2026-08-02
-->

<!-- transition
date: 2026-07-27
from: initial
to: inbox
reason: weekly_primary_source_scan
evidence: source_chain:nvidia-vera-rubin-20260721
-->
<!-- transition
date: 2026-07-27
from: inbox
to: triaged
reason: cross_group_mapping_completed_with_explicit_evidence_boundaries
evidence: sources:S1,S2,S3,S4,S5
-->
<!-- transition
date: 2026-08-08
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:readability
-->
<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: backfilled_independent_gigabyte_system_vendor_source_without_refreshing_evidence_clock
evidence: sources:S7
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: superseded_coarse_ramp_frame_after_operator_validation_cloud_offer_and_live_system_catalog_evidence
evidence: sources:S8,S9,S10,S11,S12
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_current_platform_system_composition_and_graph_projection_without_changing_financial_boundary
evidence: sources:S13
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: named_project_capacity_and_benchmark_economics_bridges_added_without_supplier_financial_upgrade
evidence: sources:S14,S15,S16
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: shipment_custody_acceptance_and_revenue_event_ledger_added_without_refreshing_thesis_clock
evidence: sources:S17,S18,S19
-->
<!-- transition
date: 2026-08-31
from: triaged
to: triaged
reason: added_platform_production_shipment_and_purchase_order_evidence_without_supplier_financial_attribution
evidence: sources:S20,S21
-->
## 新手先讀：這篇在講什麼

### 名詞小字典

- **量產爬坡**：產品已從設計或樣品走向持續製造，但產量、良率、收入與毛利仍可能逐步增加，不代表一開始就滿載。
- **AI factory**：把大量運算、網路、儲存、電力與散熱設備整合成 AI 基礎設施的資料中心，不是傳統製造工廠。
- **生態系夥伴**：平台商公開列名能配合設計或供應的公司；被列名不等於已取得特定金額的新增訂單。
- **客戶驗收**：客戶確認設備符合規格、可以交付或認列的程序；通常比展示、送樣或合作公告更接近財務貢獻。
- **Rubin 與 Vera**：NVIDIA 下一代平台的兩顆晶片代號——Rubin 是 GPU、Vera 是 CPU，合稱 Vera Rubin 平台。代號只表示產品世代，不表示已量產或已出貨。
- **NVL72**：把 72 顆 GPU 與對應 CPU、互連、電力、散熱及控制整合成機架級系統的名稱。數字是平台配置，不是已出貨 72 櫃或 72 個客戶。
- **GB300**：NVIDIA 前一個 Grace Blackwell Ultra 平台世代。緯創文件說 D1 現在生產 GB300、未來接 Rubin，兩者的動詞與時間不可互換。
- **D1 廠**：緯創在美國德州 Fort Worth 的 AI 智慧工廠名稱；本文只用它定位公司公告中的製造地點，不以廠名推估產能或訂單。
- **CDU（冷卻液分配單元）**：在機架或列級水路控制流量、溫度與壓力的設備。型錄寫 in-row CDU 只表示冷卻配置，仍需接上設施水路並完成現場啟用。
- **Spectrum-6**：NVIDIA 資料中心網路交換平台的新一代產品名稱。它與 Vera Rubin 是同一波發布的不同產品，供應鏈也不同，不應混為一談。
- **HBM**：貼著 GPU 封裝的高頻寬記憶體。本文只涉及 NVIDIA 與記憶體廠的合作揭露，不支持任何台灣記憶體公司的訂單推論。
- **DRAM**：伺服器與一般運算常用的動態隨機存取記憶體；HBM 是其中更靠近加速器、頻寬更高的封裝路徑，不能把兩者的供應關係互相代換。
- **QCT**：廣達旗下的雲端資料中心系統品牌 Quanta Cloud Technology；本文的列名只表示系統夥伴角色，不等於廣達已認列 Vera Rubin 收入。
- **Wistron／Wiwynn**：緯創與緯穎的英文名稱。兩家公司是不同法人；被平台商或自身文件列為合作／展示者，仍不等於具名客戶驗收或財務貢獻。
- **Bring-up（首次帶起）**：把晶片、伺服器、網路、電力、散熱與軟體組合後，第一次成功啟動並進入可測狀態。它比只看零件或展示更進一步，但仍不等於客戶已正式使用。
- **系統級驗證**：不只測單顆零件，而是檢查整個機架架構能否一起運作。測過哪些負載、多久、是否跨多台機架，仍要看文件明示的範圍。
- **Production-ready（可進入生產／部署準備）**：供應商表示設計已準備好承接量產或部署；這是公司自己的成熟度語言，不是全產業統一證書，也不是實際出貨數量。
- **型錄配置**：網站已列出可辨識的產品、機架或功率／散熱組合。型錄回答「廠商願意公開怎麼配」，不自動回答能否立即下單、何時交貨或誰已驗收。
- **Commissioning（站點啟用調校）**：設備裝到資料中心後，依現場電力、冷卻、網路與安全條件做啟動、調校及測試。工廠測過不代表站點啟用已完成。
- **可用性／GA**：客戶能否在指定地區、產品層級與商業條款下實際取得服務。公司說「提供」平台，若沒有 SKU、區域、容量與上線方式，仍不能自行補成全面 GA。
- **L12 整合**：本文沿用緯穎頁面的用語，指機架層級的整合與整套系統驗證。不同公司對 L10／L11／L12 的切分可能不同，研究時要先取得該公司的層級定義，不能把代號當共通標準。
- **SLO（服務目標）**：營運方承諾或追蹤的可用性、延遲、錯誤率等服務表現目標；只說工作負載能跑，還不表示已公布可核對的 SLO。
- **收入認列**：公司依會計政策把已履行的交付轉成財報收入；生產、出貨、驗收與認列的先後會受合約條款影響，不能只看產品出現在工廠或網站。
- **財務歸因**：把某平台帶來的數量、單價、成本與期間，連回特定公司的收入、毛利、存貨或現金流。沒有這座橋，就只能說產業進度，不能說個股已獲利。
- **POD-scale**：把多個各司其職的機架接成一個可共同運作的系統範圍；它比單一 NVL72 機架更大，也不等於整座資料中心都只有一種配置。
- **Configuration lock（組態凍結）**：把硬體料表、纜線、韌體、軟體、電力與冷卻版本固定到可重複製造及驗證的狀態；產品頁列出架構，不代表客戶的最終組態已凍結。
- **Tokens／MW**：每百萬瓦功率能產出的 token 速率，用來描述特定測試邊界內的能源效率；模型、精度、軟體、延遲目標與功率邊界一換，數字就不一定可比。
- **TPS／user**：每位使用者每秒可取得的 token 數，本文把它當互動速度的約束；總吞吐量提高若以更慢回應換得，不能說是同一種體驗。
- **資料中心容量**：公告用來描述站點規模的 MW。若文件沒說是公用電力、IT load、設計容量、已通電容量或哪一期，就不能拿來直接除以單櫃功率。
- **DeepSeek R1**：CoreWeave 本輪用來比較兩代機架的推理模型與工作負載名稱；換成其他模型、輸入／輸出長度或服務目標後，10 倍結果不保證維持。
- **GB200 NVL72**：CoreWeave benchmark 中作為基準的 Grace Blackwell 機架平台，和本文既有的 GB300 是不同型號；比較結果不能在兩者之間互換。
- **Visibility event（供應鏈可視事件）**：記錄某一物件在某時、某地、某個 business step 發生了什麼；同一實體在出貨、收貨與後續處理會留下多筆事件，不代表多出同樣數量的新設備。
- **EPCIS**：GS1 用來建立與交換供應鏈可視事件資料的標準。本文只借用事件欄位與去重思維，不主張 Rubin 供應鏈已部署這套標準。
- **Business step（業務步驟）**：事件發生時正在完成的流程，例如 shipping 或 receiving。只寫「已處理」而不寫是哪一步，無法判斷設備究竟離開工廠、抵達站點，還是完成驗收。
- **eventTime（事件時間）**：EPCIS 用來表示 business step 完成的時點，不是新聞發布日，也不必然等於感測器觀測或資料寫入時間。
- **控制移轉**：客戶取得主導商品或服務使用、並取得其主要利益的會計邊界。IFRS 15 把收入認列連到履約義務完成與控制移轉，不把新聞中的一般「出貨」字眼自動視為充分證據。
- **應收款與收款**：應收款是公司已取得無條件收款權利的帳面資產；現金收款是客戶實際付款。兩者可能落在不同日期，收入也不能與現金畫上等號。
- **存量與流量**：期末已安裝、在途或可用容量是某一時點的存量；本期出貨、驗收、收入與收款是某段期間的流量。不同帳不能直接相加，也不能用其中一個替代另一個。

### 三句話抓重點

- Vera Rubin 的公開證據已橫跨平台量產、系統型錄、未來工廠、整櫃驗證與雲端供應語言，不能再只用「路線圖／已量產」二分法。
- 每份文件只跨過七關中的一部分：Noetra 的規劃容量、CoreWeave 的單一工作負載 benchmark、Google 的 offer、緯創的未來生產與台灣系統廠型錄都不是同一張證書。
- 8 月 26 日新增的 NVIDIA 財報與法說已把平台時鐘推進到 full production、production shipments 與採購單；但仍沒有一手資料用同一產品鍵把台灣公司 Rubin 的完工、出貨、到貨、驗收、可用、計費、收入與收款完整接起來。

### 為什麼重要

平台從規劃走向部署，會把研究問題從「技術會不會出現」改成「何時通過驗收、出多少、
哪一家公司能留下收入與毛利」。若沒有分清平台里程碑與公司財務證據，讀者很容易把一則
供應鏈新聞誤讀成所有伺服器、散熱、PCB、電源與記憶體公司的共同利多。

### 接下來怎麼追

- 追 NVIDIA 是否公布 Vera Rubin 與 Spectrum-6 的實際部署數量、客戶驗收及量產節奏。
- 看到 `production shipments` 時，先追問出貨物件、數量單位、交易對手、完成日期、驗收／控制條件與收入歸屬；六欄缺一，就不要把平台出貨改寫成特定供應商收入。
- 追 Noetra 專案是否公布分期、實際通電／驗收容量、整數機櫃配置與商業上線時點。
- 追 CoreWeave 的結果能否在其他模型、精度、延遲、營運商與 production SLO 下重現。
- 追被列名系統廠下一次法說是否出現具名產品階段、出貨、收入、毛利、存貨與現金流足跡。
- 追每個出貨數字能否附上產品版本、數量單位、business step、完成時間、來源／目的地、交易雙方與驗收／控制移轉條件。
- 追散熱、PCB、電源與記憶體公司是否以自身一手文件建立供應關係，而不是沿用平台名單。

### 想一想

- 平台商說「量產」時，哪一個公司級數字才能證明台灣供應商真的取得經濟利益？
- 同一批 100 櫃若先後被寫成完工、出貨、到貨與驗收，為什麼不能相加成 400 櫃？
- 若產品如期部署，但供應商毛利與現金流沒有改善，原本的受惠判讀還成立嗎？
- 韓國 HBM 合作為什麼不能直接證明台灣傳統 DRAM 公司受惠？

## 為何值得進佇列

NVIDIA 7 月 21 日已把 Vera Rubin 描述從「規劃採用」推進到 NVL72 量產爬坡、合作夥伴
機架運行與 350 多個 AI factory site 的供應鏈部署；Spectrum-6 也被描述為已進入首批
gigascale AI factories。這是供應鏈時程的重要變化，值得檢查現有小作文是否仍停留在
「未量產／僅路線圖」的舊前提。

## 先把「量產」拆成七個交接關卡

「量產」常被當成一個開關，但機架型 AI 系統其實要連續交接。前一關通過，只表示下一關
值得開始檢查；不能把後面尚未公開的結果自動補上。

| 關卡 | 真正回答的問題 | 本輪可見證據 | 還不能回答什麼 |
|---|---|---|---|
| 1. 平台進入生產 | 平台商是否已把設計推進持續製造與供應鏈爬坡？ | NVIDIA 稱 Vera Rubin 進入 full production，並稱 8 月開始 production shipments | 出貨物件、數量、具名客戶／ODM、個別系統廠良率或收入 |
| 2. 設計／型錄就緒 | 系統廠是否公開可辨識的機架、配置與整合角色？ | 技嘉列出 Vera Rubin NVL72 機架配置；緯穎稱 production-ready | 可立即下單、交期、客戶或出貨量 |
| 3. 工廠實際生產 | 哪一座工廠現在正做哪個世代？ | 緯創稱 Texas D1 現在生產 GB300，Rubin 將接續 | Rubin 已在該廠量產或已形成收入 |
| 4. 整櫃 bring-up／驗證 | 把整個機架帶起後，系統級路徑能否運作？ | CoreWeave 稱完成 NVL72 整櫃 bring-up 與 system-level validation | 測試母體、長時間負載、客戶驗收與廣泛複製 |
| 5. 站點啟用／客戶驗收 | 機架到特定機房後，電力、冷卻、網路與軟體是否完成交接？ | 公開來源尚未提供台灣系統廠可核對的 acceptance 節點 | 誰簽收、何時可計費、多少機架通過 |
| 6. 雲端可用／工作負載運行 | 客戶能否取得服務，且真實工作負載是否持續運作？ | Google 稱 Cloud 提供 Vera Rubin；NVIDIA 列名多個運行站點 | SKU、區域、GA 條款、容量、利用率及 workload SLO |
| 7. 供應商財務歸因 | 哪家公司因哪些數量與單價留下收入、毛利及現金流？ | 尚無可重算的台灣公司 Rubin 橋接 | 個股受惠幅度、份額、獲利與現金回收 |

這張表不是要求所有公司使用相同術語，而是把研究的「停止線」畫清楚。例如，Google 的
`offer` 比單純列名更接近服務端，但若沒有產品代碼、地區、容量與取得方式，就不能自行寫成
全球全面 GA；緯創說「soon」也只能放在未來生產關，不得改寫成當期 Rubin 產量。

### 8 月 26 日新增證據：出貨時鐘前進，台灣公司財務時鐘沒有跟著跳

NVIDIA 在 2026Q2 財報新聞稿稱 Vera Rubin 已進入 full production；同日法說逐字稿再稱公司
於 8 月開始 `production shipments`，並已收到各主要 hyperscaler、AI cloud 與 system OEM
類別的採購單。這比只有路線圖、型錄或未來式工廠計畫更接近實際供應，因此第 1 關的證據
確實前進。

但這兩份文件都來自 NVIDIA 同一消息鏈，也沒有公開出貨的是晶片、托盤、單機、整櫃或其他
組件，沒有數量、具名買方、具名 ODM、站點到貨／驗收、控制移轉或 Rubin 專屬財務分母。
所以它不能替緯創的「未來生產」改成「已生產」，也不能替任何台灣公司補出訂單、營收或
毛利。新手可以把每一則「出貨」公告先拆成六問：**什麼物件、多少單位、交給誰、何時完成、
誰驗收／何時移轉控制、最後在哪一家公司入帳**。目前只有平台商、月份與廣義客戶類別較清楚，
其餘欄位仍待驗證。

## 看到「量產／就緒／驗證／上線」，先補齊五個欄位

同一個成熟度動詞，換了說話者、物件或範圍，意思就可能完全不同。初學者不必先記住所有
產品代號；先把一句公告改寫成下面五欄，就能知道證據落在哪一關，以及還缺哪一張交接單。

| 本文五把尺 | 初學者先問什麼 | 本文例子 | 能阻止的誤讀 |
|---|---|---|---|
| 1. 誰在說 | 是平台商、系統廠、工廠、營運商、雲端商，還是上市公司財務主管？ | NVIDIA 描述平台；CoreWeave 描述自己的 bring-up；緯創描述自己的工廠 | 把一家公司的自述當成全產業共同驗收 |
| 2. 說哪個物件 | 是晶片、單一托盤、NVL72 機架、POD、資料中心站點、雲端 SKU，還是公司收入？ | NVIDIA 現行產品頁把五套機架級系統組成 POD-scale 平台 | 把「平台已生產」改寫成每一座站點都已上線 |
| 3. 用什麼動詞 | 是 listed、production-ready、plans production、bring-up、validation、offer、acceptance，還是 revenue recognition？ | 技嘉的型錄、緯創的 future production、CoreWeave 的 validation 分屬不同關卡 | 把就緒、計畫與驗證都翻成「已出貨」 |
| 4. 範圍與日期 | 哪個版本、地點、客戶、SKU、機架數、測試母體與截止日？ | 動態產品頁只代表 2026-08-12 可見的公開配置；Google remarks 未給區域與容量 | 把當日型錄或單一營運商結果外推到所有部署 |
| 5. 下一份裁決證據 | 哪一份文件能把它推進下一關，或證明原判斷失效？ | Configuration lock、工廠 build、rack test、site acceptance、workload SLO、財務橋接依序補齊 | 用更多同義行銷文案取代真正的新證據 |

這五欄也是知識圖譜的閱讀順序：先看發布者與平台之間的公司線，再看平台跨到哪一個成熟度
節點，最後才沿族群路由檢查台灣公司。若某條線停在 `unverified`，意思是「下一站值得找」，
不是「受惠已成立」。

## 一座 AI 機架不是放大的單機：七條責任鏈要同時接上

Vera Rubin NVL72 不是把 72 顆 GPU 裝進鐵櫃就完成。至少有七條彼此牽制的責任鏈：

1. **運算**：CPU、GPU、主機板與韌體要能啟動、枚舉並執行工作。
2. **記憶體**：HBM、CPU 系統記憶體與資料放置要在容量、頻寬、錯誤處理間配合。
3. **機架內 scale-up**：多顆加速器之間的高速 fabric 要通過訊號、拓樸與 collective 測試。
4. **機架外 scale-out**：網路介面、交換器、光電連線與壅塞控制要把多櫃接成叢集。
5. **電力**：進線、busbar、power shelf、備援與瞬時功率管理要承受整櫃負載。
6. **散熱**：CDU、泵、閥、冷板、流量、溫度與漏液偵測要在現場水路共同閉環。
7. **儲存與控制**：模型、資料、checkpoint、作業排程、監控與復原要能把硬體變成服務。

任何一條鏈沒交接，整櫃都可能只是「能開機」而不是「能承諾服務」。因此 CoreWeave 同一份
文件同時談液冷控制、rack control、網路、DPU 與儲存夥伴，不是旁枝末節，而是在說明
bring-up 為何是跨系統工作。反過來，這仍是營運商自己發布的驗證敘述，不能代替跨站點、
跨客戶與長時間 workload 的獨立結果。

## 五份一手文件，為什麼不能合併成一句「已上線」

| 發布者 | 文件真的說了什麼 | 在七關中的位置 | 最容易被誤寫成什麼 |
|---|---|---|---|
| CoreWeave | 完成整櫃 bring-up 與 system-level validation，並稱系統 operational | 第 4 關；也提供靠近第 6 關的營運商敘述 | 所有客戶已可取得、已大規模跑 production workload |
| Google | Q2 CEO remarks 稱 Google Cloud `offer` 新 Vera Rubin 平台 | 第 6 關的供應語言 | 全地區 GA、容量充足、已由特定台灣廠出貨 |
| 緯創 | Texas D1 現在做 GB300，Vera Rubin 將在該廠接續生產 | 第 3 關的未來計畫 | Rubin 現在已量產、已認列營收 |
| 技嘉 | GIGAPOD 型錄列出 Vera Rubin NVL72、240 kW 與冷卻配置 | 第 2 關 | 型錄即訂單、出貨或客戶驗收 |
| 緯穎 | 自稱處於 NVL72 commercialization 前線，提供 production-ready rack 與 L12 驗證能力 | 第 2 關的公司成熟度主張 | 已交付多少、哪個客戶驗收、平台毛利已增加 |

文件之間不是互相矛盾，而是觀察單位不同：平台商看世代，系統廠看設計與製造，雲端商看
可營運能力，投資研究最後還要看上市公司的會計結果。把五句話壓成「已上線」，會把所有
還沒公開的交接責任一起藏掉。

## 27,500 顆 GPU、140MW 與 10 倍效率，三種分母不能直接變成營收

NVIDIA 7 月 16 日公告與 Noetra 規劃一座 Vera Rubin AI factory，列出 13,750 顆 Vera
CPU、27,500 顆 Rubin GPU 與 140MW data center capacity；公告使用的是 `working with`、
`will be architected` 與 `will deliver` 等未來式。CoreWeave 7 月 21 日則公布自家測試：在
同一 DeepSeek R1 工作負載、相近互動速度下，Vera Rubin NVL72 的 tokens／MW 是 GB200
NVL72 的 10 倍。前者是**專案規劃容量**，後者是**一個營運商的工作負載效率**；兩者都比
只有產品型錄更具體，但仍不是上線容量、台灣供應商訂單或財務結果。

### 先做容量護照，再決定能不能除

| 公開數字 | 原始分母／邊界 | 可以做的機械核對 | 不能自行補上的結論 |
|---|---|---|---|
| 27,500 顆 Rubin GPU | Noetra 規劃專案的晶片總數 | 依每櫃 72 顆換算為 `27,500 ÷ 72 = 6,875／18 ≈ 381.944` 個配置單位 | 382 櫃確定訂單、交貨或驗收 |
| 13,750 顆 Vera CPU | 同一專案的 CPU 總數 | 依每櫃 36 顆換算也為 `13,750 ÷ 36 = 6,875／18 ≈ 381.944`；GPU：CPU 剛好 2：1 | 尾差究竟來自備品、分期、四捨五入或其他 BOM；原文沒有說明，不能選定其中一種 |
| 140MW data center capacity | 公告未拆公用電力、IT load、設計／已通電容量或建置分期 | 只記為一個具名專案的站點容量標籤 | 直接除以技嘉型錄 240kW 得出機櫃數，或把全部 MW 當成 GPU 可用功率 |
| 80,000 與 800,000 TPS／MW | CoreWeave 頁面：DeepSeek R1、150 TPS／user、GB200 與 Vera Rubin | 在該頁相同口徑下為 10 倍 | 全模型、全延遲、全站點都 10 倍；更不能等同 10 倍收入或 90% 總成本下降 |

兩個除法得到完全相同的非整數，只證明公告中的 CPU／GPU 數量與 72：36 拓撲在比例上
一致；它反而提醒讀者，文件沒有提供「整數機櫃訂單」這個欄位。尾差可能有多種工程或公告
原因，任何一種都需要新文件才能選定。140MW 也不能和單一廠商型錄的 240kW rack power
直接相除：站點容量的量測邊界未揭露，DSX 專案還包含網路、CPU、儲存與其他系統責任。

### 從 benchmark 到財報，還要跨過四座橋

| 橋 | 要回答的問題 | 最低可核對證據 | 少了它會誤讀成什麼 |
|---|---|---|---|
| 1. 技術可重現 | 10 倍是否只屬於 DeepSeek R1、NVFP4 與這套最佳化？ | 公開測試方法、不同模型／精度／延遲點、其他營運商或獨立 benchmark | 把單一最佳化案例當成所有工作負載定律 |
| 2. 營運轉換 | 測試效率能否在長時間服務中保留？ | 上線機櫃數、可用率、利用率、SLO、故障與電力／散熱邊界 | 把短測吞吐量當成可全年計費容量 |
| 3. 商業變現 | 多出的 token 有沒有需求，售價如何變？ | billable token／instance、價格、合約量、客戶留存與折扣 | 把 10 倍產能直接寫成 10 倍營收；忽略每 token 價格下跌或閒置 |
| 4. 財務與供應鏈歸因 | 誰付 CapEx、誰認列收入、誰承擔折舊與電力？ | 專案出貨／驗收、供應商數量與 ASP、收入、毛利、存貨、OCF／FCF 對時 | 把平台效率同時算成雲端商與所有台灣供應商的獲利 |

CoreWeave 已明示測試開啟 expert parallelism、NVFP4、multi-token prediction、disaggregated
prefill／decode、TensorRT-LLM 與 Dynamo，並把目前結果稱為會繼續最佳化的 starting point。
這使結果更可定位，不使它自動變成跨業者基準。研究上應先保存模型、精度、軟體、TPS／user、
功率邊界與測試日期，再等下一條獨立消息鏈重做；若只抄「10x」，就遺失了真正能被推翻的條件。

### 多空小作文要共用同一組裁決欄位

| 版本 | 必須同時成立 | 下一份裁決證據 | 何時下修／失效 |
|---|---|---|---|
| 多方 | 效率在多種 production workload 與 SLO 下保留；電力確實是瓶頸；新增容量有高利用率與可計費需求；專案按期通電驗收；台灣供應商留下具名出貨與毛利／現金流 | 跨營運商 benchmark、site commissioning、可用容量與利用率、價格／合約、買賣雙方財務橋接 | 只能重現單一測試、站點延後、容量閒置、token 售價降幅吃掉效率，或供應商沒有財務足跡 |
| 空方 | 10 倍主要來自特定模型／精度／軟體；網路、儲存、散熱或需求成為新瓶頸；價格競爭把效率讓給客戶；專案規劃未轉成驗收與收入 | 同條件重測顯著縮小、長期 SLO／利用率偏弱、延遲或取消、價格與毛利惡化 | 多工作負載與多站點持續重現、利用率高、售價與單位經濟改善，且供應商收入、毛利與現金同步出現 |

本輪觀察單位是 1 個具名規劃專案，以及 1 家營運商對 1 個具名工作負載、2 個平台的自家
比較；不是 AI factory、雲端業者或台灣供應鏈的抽樣。公告值與兩個除法是確定性核對，沒有
sampling SE／t；CoreWeave 頁面未披露重複試驗、變異或獨立驗證，不能補造誤差範圍。這段
新增的是容量與經濟橋接的閱讀方法，不改寫 C11 七關主命題，也不形成價格、估值或投資建議。

## 從工廠到工作負載的交付順序

初學者可以用一條時間線逐項問，而不是看到最新日期就假設所有前置工作完成：

1. **BOM 與 configuration lock**：料表、韌體、纜線、冷卻與電源配置先凍結到可重複版本。
2. **製造與廠內測試**：零件進料、組裝、燒機與故障隔離能否維持良率及節拍。
3. **機架整合**：伺服器、交換器、power shelf、CDU 與控制器在同一櫃完成 bring-up。
4. **站點準備**：機房要先有足夠的電力、冷源、水質、管路、網路與承重。
5. **Commissioning／驗收**：現場把整櫃接入設施，跑完約定測試並決定是否簽收。
6. **服務與 workload**：雲端 SKU 或自建叢集真正承載工作，留下容量、利用率、SLO 與故障資料。
7. **財務橋接**：依合約確認出貨、驗收、收入認列、成本、存貨與現金回收落在哪一季。

順序不是固定會計模板：有些合約可能出貨認列，有些要到驗收或服務期間才認列。研究者不能
用產業慣例替公司填空，必須回到該公司的合約、會計政策與法說措辭。

## 同一套系統會被數很多次：九事件出貨與會計護照

GS1 的 EPCIS 事件標準提供一個很實用的閱讀方法：每一筆事件都要回答物件、時間、地點、
business context 與物件狀態，也就是 `what／when／where／why／how`。標準還明確區分
`shipping` 與 `receiving` 等 business step，並說 `eventTime` 是該步驟**完成**的時間；
同一實體沿供應鏈移動時會持續產生新的 transaction／visibility event data。本文沒有證據
顯示 Rubin 相關公司採用 EPCIS，這裡只借用它的事件思維，防止把同一批設備在不同階段
重複當成新增量。

| 事件鐘 | 最少要留下什麼 | 只看到這一鐘，還不能說什麼 |
|---|---|---|
| 1. 廠內完工／測試 | 序號或批次、configuration revision、數量、工廠與完成條件 | 已離廠、已交給客戶或可以認列收入 |
| 2. 出廠／shipping | 出貨物件、數量、承運交接、起點、完成時間與合約交付條件 | 已到客戶指定地、已安裝或已驗收 |
| 3. 到站／receiving | 目的地、收貨方、到貨時間、缺損／短少與收貨狀態 | 電力、冷卻、網路與軟體已接通 |
| 4. 安裝／commissioning | 安裝組態、場站條件、實際測項、重工與通過版本 | 客戶已簽收或服務已可對外承諾 |
| 5. 客戶驗收 | 合約測項、通過門檻、簽署方、日期、例外與保留事項 | 工作負載已滿載、供應商已收到現金 |
| 6. 可用容量 | 可服務的 SKU、區域、容量、SLO、維護與故障排除邊界 | 有多少實際需求或計費使用量 |
| 7. 可計費工作量 | 計費單位、使用量、價格、折扣、期間與取消／退款 | 供應商在同一期間認列多少收入與毛利 |
| 8. 收入認列／應收 | 履約義務、控制移轉、交易價格、認列期間與無條件收款權 | 現金已入帳、收入等於自由現金流 |
| 9. 現金回收 | 付款方、金額、幣別、收款日、帳期、融資或扣款 | 毛利品質、專案全生命週期報酬或下一批訂單 |

九鐘不是所有合約都必須照同一順序，也不是把產業流程改成會計規則。它的用途是要求每一個
headline 先選定事件：同一批 100 櫃若依序完工、出貨、收貨與驗收，仍是 100 櫃經過四個
事件，不是 400 櫃。只有在同一物件鍵、期間與調整口徑下，才能寫出例如
`期末在途＝期初在途＋本期出貨－本期收貨±更正` 的存量／流量對帳；若出貨是 GPU 顆數、
收貨是 compute rack、驗收是整套 POD，公式根本沒有共同單位。

### 七欄事件護照：先對物件，再對數量與控制

| 護照欄位 | 必問問題 | Rubin 文章目前的缺口 |
|---|---|---|
| 1. 物件與版本 | 是 GPU、compute tray、compute rack、network／storage rack、POD 還是站點？哪個 revision？ | 多數來源只在平台、機架或專案層敘述，沒有跨公司共用的序號／組態鍵 |
| 2. 數量與階層 | 單位是顆、板、托盤、櫃、POD、MW 或 token？父子組成與備品怎麼算？ | 27,500 顆 GPU 只能和 72 GPU／rack 做比例核對，不能補出整數交付櫃數或輔助機架 |
| 3. 事件與判準 | 是 built、tested、shipped、received、installed、accepted、available、billable 還是 recognized？完成條件是什麼？ | 公開文件橫跨多個動詞，但沒有同一批設備逐關對帳 |
| 4. 時間口徑 | 是事件完成日、資料登錄日或公告日？是本期流量、累計量或期末存量？時區為何？ | 現有公告日期不能替代實際出貨、到貨、驗收與認列日期 |
| 5. 地點與交易雙方 | 起點、目的地、交付方、收貨方、驗收方與最後責任人是誰？ | 多數文件未把台灣供應商連到具名站點與驗收方 |
| 6. 淨額調整 | 是否含備品、替換、重工、退貨、取消、短少、跨期或重複登錄？ | 非整數配置尾差沒有分解，不能任選備品或四捨五入解釋 |
| 7. 控制與財務 | 何時移轉控制、滿足履約義務、形成應收、認列收入、收現與反映毛利？ | 尚無 Rubin 專屬合約與財務分母，不能用產業慣例代填 |

IFRS Foundation 對 IFRS 15 的摘要把收入認列連到履約義務完成與客戶取得承諾商品或服務的
控制。緯穎 2025 合併財報提供一個**公司層級例子**：KPMG 把收入認列時點列為關鍵查核事項；
公司商品銷售政策再把控制移轉連到指定地點交付、陳舊／損失風險移轉，以及客戶已驗收、
驗收條款失效或有客觀證據證明條件完成，並在交付形成無條件收款權時認列應收。這只說明
「合約條件與控制邊界不能省」，不證明緯穎已有任何 Rubin 出貨或收入，也不能替其他系統廠
決定會計時點。

### 存量、事件流量、可用容量與金額要分四本帳

| 帳本 | 典型問題 | 可比較的必要條件 | 常見錯誤 |
|---|---|---|---|
| 實體存量 | 期末有多少在製、在途、已安裝或已驗收物件？ | 同一產品鍵、地點、截止日與淨額調整 | 把不同位置的同一物件各算一套 |
| 事件流量 | 本期有多少物件完成 shipping、receiving 或 acceptance？ | 同一事件定義、期間、單位與去重鍵 | 把完工、出貨、到貨、驗收相加成總出貨 |
| 營運容量／活動 | 多少已安裝容量可用？多少時間真的承載 billable workload？ | 同一 reference plane、SKU、區域、SLO 與時間窗 | 把 installed MW 當平均活躍 MW，或把可用當滿載 |
| 財務金額 | 哪一方在何期認列收入、應收、毛利與現金？ | 同一合約、控制移轉、幣別、期間與會計主體 | 把供應商收入、雲端計費與客戶 CapEx 當同一筆錢 |

因此 `installed`、`available`、`billable`、`revenue` 與 `cash` 不是五個同義詞。若同一站點
只有 installed capacity，還要等 commissioning、可用性與工作負載資料；若供應商已認列
收入，仍要另外檢查毛利、應收與現金。反過來，某些合約的控制移轉可能不等待本文排列的
所有營運事件，所以研究者也不能武斷要求「一定到第 7 鐘才可認列」；唯一安全做法是保存
公司自己揭露的政策與具體合約證據。

### 多空小作文共用同一張事件對帳表

| 版本 | 必須看見的共同證據 | 何時下修／失效 |
|---|---|---|
| 多方 | 同一產品鍵的完工→出貨→到貨→驗收數量可對帳；等待時間沒有持續拉長；可用與 billable 容量跟上；收入、毛利、應收與現金的跨期差異有合約解釋 | 數量換單位後無法重算、同一物件重複計數、驗收或啟用累積卡住、應收／存貨上升而現金與毛利未跟上 |
| 空方 | headline 主要停在 built／shipped 或累計 installed，site constraint、重工、替換、退貨、驗收延遲、低利用率或價格壓力使經濟價值落後 | 同一批次快速通過 acceptance、可用與 billable 事件，跨公司財務亦在合理帳期閉合，且反方無法指出重複或停滯 |

本輪是 `N=3` 條定向一手消息鏈：GS1 事件標準、IFRS Foundation 準則頁、緯穎／KPMG 合併
財報；它們不是 Rubin 機架、客戶、供應商、台灣 121 檔或全市場的抽樣。兩份官方 PDF 的
實際引用頁及相鄰頁已逐頁目視核對，SHA-256 分別記於 S17、S19；本文沒有新估計值、抽樣
效果或可報的 sampling SE／t。新增的是事件與會計邊界教材，不改 C11 主命題、T4 到期日、
`last_reviewed_at`、`review_due` 或 `base_confidence`，也不形成價格、估值、部位或投資建議。

## 用雙向證據把平台進度連回台灣公司

個股歸因至少要有兩個方向同時閉合：

- **平台／客戶端往回找**：具名系統、供應商、料號、工廠、驗收或部署，能辨識是哪一家公司。
- **台灣公司端往前找**：同一平台或可核對代號的 qualification、量產、出貨、收入與毛利足跡。

若只有 NVIDIA 或雲端商列名，最多證明需求鏈存在；若只有台灣公司說「AI 伺服器成長」，
也無法證明增量來自 Rubin。兩端還要在**產品身分、期間、交付階段與經濟量**對得上，才有
資格從產業 tailwind 升成公司財務主張。這也是為什麼本篇即使新增三家台灣公司的自身文件，
仍維持 `medium` 信心，而不估訂單、份額或獲利。

## 新手最常混淆的六件事

1. **平台 full production ≠ 每家供應商都在量產**：平台商可能在彙總不同零件與地點。
2. **型錄有產品 ≠ 可以立即下單**：還要找 orderability、交期、SKU 與商業條款。
3. **Production-ready ≠ 已出貨**：它描述準備狀態，不提供數量、客戶與認列期間。
4. **Bring-up／validation ≠ customer acceptance**：營運商或工程團隊測過，不代表客戶已簽收。
5. **雲端 offer ≠ 全面 GA 與滿載**：區域、配額、預覽／一般可用、利用率是不同欄位。
6. **營收成長 ≠ Rubin 財務歸因**：還要排除其他平台、價格、匯率、併購與產能變動。

## 在研究中心裡接著怎麼學

- 先讀〈人工智慧資料為什麼要分層存放：正在運算、等待取用與長期保存各有位置〉，理解 HBM、CPU memory、context 與 storage 為何不是同一層。
- 再讀〈AI 儲存不是容量越大越好：先分清餵資料、保存進度與搬模型〉，把模型、訓練資料與 checkpoint 放回工作負載生命週期。
- 接著讀〈資料從一顆運算晶片走到另一顆：先分清機架內外，再判斷跨廠互通〉，分清 scale-up、scale-out、規格與互通結果。
- 讀〈AI 機櫃儲能要接力：短暫尖峰、機櫃備援與設施儲能各有任務〉，把電源瞬態、備援與設施時鐘接回整櫃交付。
- 最後讀〈液冷不是買完設備就能運作：冷源、管路、伺服器與控制必須共同交接〉，理解工廠測試為什麼不能替代站點 commissioning。

## 來源與證據邊界

<!-- research_source
source_id: S1
role: company_release
publisher: NVIDIA
title: NVIDIA Vera Rubin Platform Enters Full Production
published_at: 2026-07-21
captured_at: 2026-07-27
accepted_at: 2026-07-27
status: active
url: https://blogs.nvidia.com/blog/vera-rubin/
locator: 量產爬坡、合作夥伴機架運行與 AI factory site 部署段落
limitation: 只支持 NVIDIA 平台階段與公開部署敘述，不支持任何台灣公司的新增訂單、收入或毛利
-->

<!-- research_source
source_id: S2
role: company_release
publisher: NVIDIA
title: NVIDIA Spectrum-6 Arrives in Gigascale AI Factories
published_at: 2026-07-21
captured_at: 2026-07-27
accepted_at: 2026-07-27
status: active
url: https://blogs.nvidia.com/blog/nvidia-spectrum-six-arrives-in-gigascale-ai-factories/
locator: Spectrum-6 首批 gigascale AI factory 導入段落
limitation: 沒有公布具體部署量、台灣零組件供應商、訂單金額或獲利分配
-->

<!-- research_source
source_id: S3
role: company_release
publisher: NVIDIA / NAVER / Brookfield
title: NAVER NVIDIA and Brookfield Korea AI Factory Buildout Proposal
published_at: 2026-07-24
captured_at: 2026-07-27
accepted_at: 2026-07-27
status: active
url: https://investor.nvidia.com/news/press-release-details/2026/NAVER-NVIDIA-and-Brookfield-to-Expand-Koreas-National-AI-Factory-Infrastructure-Buildout/default.aspx
locator: 合作架構、非拘束性條款與後續條件段落
limitation: 提案與非拘束性條款不等於已交付設備、確定採購量或已認列收入
-->

<!-- research_source
source_id: S4
role: company_release
publisher: NVIDIA / SK Group
title: SK Group and NVIDIA Expand AI Factory and Memory Partnership
published_at: 2026-07-24
captured_at: 2026-07-27
accepted_at: 2026-07-27
status: active
url: https://investor.nvidia.com/news/press-release-details/2026/SK-Group-and-NVIDIA-Expand-Strategic-Partnership-Across-AI-Factories-and-Next-Generation-Memory/default.aspx
locator: HBM4、下一代 AI memory 與合作意向段落
limitation: SK hynix 合作意向只支持韓國 HBM 路徑，不能映射成台灣 DRAM 公司訂單
-->

<!-- research_source
source_id: S5
role: company_release
publisher: NVIDIA
title: NVIDIA Unveils Vera CPU for Agents
published_at: 2026-05-31
captured_at: 2026-07-27
accepted_at: 2026-07-27
status: active
url: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Unveils-Vera-the-CPU-for-Agents/default.aspx
locator: GIGABYTE、QCT、Wistron 與 Wiwynn 系統夥伴列名段落
limitation: 生態系列名證明合作角色存在，不等於個別公司新增訂單、出貨占比或獲利
-->

- [Vera Rubin 量產與部署](https://blogs.nvidia.com/blog/vera-rubin/)（NVIDIA，2026-07-21）。
- [Spectrum-6 首波導入](https://blogs.nvidia.com/blog/nvidia-spectrum-six-arrives-in-gigascale-ai-factories/)（NVIDIA，2026-07-21）。
- [NAVER／NVIDIA／Brookfield 韓國 AI factory 擴建提案](https://investor.nvidia.com/news/press-release-details/2026/NAVER-NVIDIA-and-Brookfield-to-Expand-Koreas-National-AI-Factory-Infrastructure-Buildout/default.aspx)（NVIDIA，2026-07-24；含非拘束性條款與條件）。
- [SK Group／NVIDIA AI factory 與 HBM 合作意向](https://investor.nvidia.com/news/press-release-details/2026/SK-Group-and-NVIDIA-Expand-Strategic-Partnership-Across-AI-Factories-and-Next-Generation-Memory/default.aspx)（NVIDIA，2026-07-24；LOI／計畫，不是已交付訂單）。
- [NVIDIA 先前列名的台灣 Vera 系統廠](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Unveils-Vera-the-CPU-for-Agents/default.aspx)（NVIDIA，2026-05-31）包含 GIGABYTE、QCT、Wistron、Wiwynn。
- [NVIDIA／Noetra 日本 physical AI 基礎設施公告](https://investor.nvidia.com/news/press-release-details/2026/Japan-Government-Industrial-Leaders-and-NVIDIA-Launch-the-Worlds-First-National-AI-Infrastructure/default.aspx)（NVIDIA，2026-07-16；規劃容量與未來式架構）。
- [CoreWeave Vera Rubin tokens／MW 測試](https://coreweave.com/blog/nvidia-vera-rubin-nvl72-on-coreweave-10x-more-tokens-per-megawatt-than-blackwell)（CoreWeave，2026-07-21；單一營運商自家測試）。
- [CoreWeave Vera Rubin 動態產品頁](https://www.coreweave.com/products/nvidia-vera-rubin)（擷取於 2026-08-14；保存 150 TPS／user 下的 80,000／800,000 TPS／MW 口徑）。
- [GS1 EPCIS Standard 2.0.1](https://ref.gs1.org/standards/epcis/2.0.1/)（GS1，2025-07-01；只借用事件資料的物件、時間、地點、business step 與狀態欄位，不表示本文公司採用 EPCIS）。
- [IFRS 15 Revenue from Contracts with Customers](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/)（IFRS Foundation；現行準則頁，擷取於 2026-08-14）。
- [緯穎 2025 年合併財務報告](https://www.wiwynn.com/hubfs/Investors/Financial_Report/Wiwynn_2025Q4_Financial.pdf)（緯穎／KPMG，2026-02-26；公司層級收入政策與查核事項，不是 Rubin 交易證據）。
- [NVIDIA 2027 財年第二季財務結果](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx)（NVIDIA，2026-08-26；full production 與運行地點，不含台灣供應商財務歸因）。
- [NVIDIA 2027 財年第二季法說逐字稿](https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)（NVIDIA，2026-08-26；production shipments 與廣義 PO 類別，不含物件、數量、驗收或 ODM 分配）。

上述資料已把 NVIDIA 平台證據推進到管理層所稱的 production shipments，但仍只證實平台商
與其公開列名生態系。它沒有披露技嘉、廣達、緯創或緯穎的
新增訂單、單價、出貨占比或獲利；也沒有點名本 universe 的散熱、PCB、電源或記憶體個股。
SK hynix 的 HBM 合作尤其不能外推為台灣傳統 DRAM 廠的直接受惠證據。

## Claim–evidence ledger

<!-- research_source
source_id: S6
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-07-27
accepted_at: 2026-07-27
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 台灣系統與零組件供應商季報、法說與重大訊息查找入口
limitation: 平台量產與韓國合作不能替代台灣供應商自己的毛利、存貨與現金流文件
-->

<!-- research_source
source_id: S7
role: competitor_primary
publisher: GIGABYTE / Giga Computing
title: Giga Computing Expands AI Infrastructure Portfolio with Next-Gen Solutions at COMPUTEX 2026
published_at: 2026-06-01
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://www.gigabyte.com/vn/press/news/2393
locator: Vera Rubin NVL72 展示段落與 HGX Rubin NVL8 系統 G2L4-SD4 段落
limitation: 技嘉自身文件獨立支持其展示 Vera Rubin NVL72 元件與具名 Rubin NVL8 系統角色；不支持客戶驗收、量產出貨、訂單金額、收入或毛利
-->

<!-- research_source
source_id: S8
role: company_release
source_kind: document
publisher: CoreWeave
title: CoreWeave Completes Industry-First Bring-Up and Validation of NVIDIA Vera Rubin NVL72
published_at: 2026-06-01
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://coreweave.com/news/coreweave-completes-industry-first-bring-up-of-nvidia-vera-rubin-nvl72
locator: Vera Rubin NVL72 bring-up、entire rack-scale architecture system-level validation、fully operational 敘述；液冷、rack control、network、BlueField-4 與 Dell／Micron 夥伴段落
limitation: CoreWeave 自身發布支持單一營運商的整櫃帶起與驗證主張；未披露測試母體、長期 production workload、服務 SKU／區域、機架數、台灣系統廠、客戶驗收或供應商收入
independence_group: coreweave
-->

<!-- research_source
source_id: S9
role: company_release
source_kind: document
publisher: Google / Alphabet
title: Q2 2026 earnings call: Remarks from our CEO
published_at: 2026-07-22
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/
locator: Google Cloud 段落稱其 accelerators 包含 new NVIDIA Vera Rubin platform
limitation: CEO remarks 的 offer 語言未披露 SKU、地區、preview／GA 狀態、容量、利用率、工作負載、供應商、機架數或 Rubin 專屬收入
independence_group: google
-->

<!-- research_source
source_id: S10
role: competitor_primary
source_kind: document
publisher: Wistron
title: Wistron Celebrates Grand Opening of First U.S. Smart Factory Marking Milestone in Global Smart Manufacturing Strategy
published_at: 2026-07-21
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.wistron.com/en/Newsroom/2026-07-22
locator: Texas D1 facility 現在生產 GB300、未來／soon 生產 Vera Rubin 的段落
limitation: 緯創自身文件把 GB300 現況與 Rubin 未來計畫分開；不支持 Rubin 已在該廠量產、出貨、客戶驗收、數量、收入或毛利
independence_group: wistron
-->

<!-- research_source
source_id: S11
role: competitor_primary
source_kind: living_index
publisher: GIGABYTE
title: GIGAPOD Rack Scale
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.gigabyte.com/us/Enterprise/GIGAPOD-Rack-Scale
locator: 2026-08-12 可見 NVIDIA Vera Rubin NVL72 型錄列、240 kW rack power、power shelf 與 in-row CDU 配置
limitation: 動態型錄只支持當日公開配置；頁面未提供首次上線日、orderability、SKU 商業條款、交期、實際生產、出貨、客戶驗收、收入或毛利
independence_group: gigabyte
-->

<!-- research_source
source_id: S12
role: competitor_primary
source_kind: living_index
publisher: Wiwynn
title: AI Infrastructure
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.wiwynn.com/solutions/ai-infrastructure
locator: 2026-08-12 Vera Rubin commercialization、production-ready rack-scale solutions、L12 integration 與 full system-level validation 段落
limitation: 緯穎自身產品行銷頁支持其公開定位與能力主張；未披露首次上線日、具名客戶、實際 Rubin 機架出貨、驗收、數量、收入、毛利或獨立測試
independence_group: wiwynn
-->

<!-- research_source
source_id: S13
role: company_release
source_kind: living_index
publisher: NVIDIA
title: NVIDIA Vera Rubin Platform
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.nvidia.com/en-us/data-center/technologies/rubin/
locator: 2026-08-12 可見的 POD-scale system、five purpose-built rack-scale systems，以及 Vera Rubin NVL72、NVLink、Spectrum-X／Quantum-X、liquid-cooled Vera CPU 與 BlueField storage 段落
limitation: 動態產品頁只支持當日平台組成與 NVIDIA 自身架構描述；不證明客戶最終 configuration lock、所有部署採相同選配、orderability、出貨、客戶驗收、台灣供應商分配或財務貢獻
independence_group: nvidia
-->

<!-- research_source
source_id: S14
role: company_release
source_kind: document
publisher: NVIDIA / Noetra
title: Japan Government Industrial Leaders and NVIDIA Launch the World's First National AI Infrastructure
published_at: 2026-07-16
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://investor.nvidia.com/news/press-release-details/2026/Japan-Government-Industrial-Leaders-and-NVIDIA-Launch-the-Worlds-First-National-AI-Infrastructure/default.aspx
locator: News Summary 與 AI factory 段落的 13,750 Vera CPUs、27,500 Rubin GPUs、140MW data center capacity、NVL72／DSX／Spectrum-X 與 FRONTia Project 敘述
limitation: NVIDIA／Noetra 公告以 working with、will be architected 與 will deliver 描述規劃；沒有建置分期、整數機櫃數、電力邊界、通電、驗收、order、台灣供應商或財務橋接，且與 S1／S13 同屬 NVIDIA 消息鏈
independence_group: nvidia
-->

<!-- research_source
source_id: S15
role: company_release
source_kind: document
publisher: CoreWeave
title: NVIDIA Vera Rubin NVL72 on CoreWeave 10x More Tokens Per Megawatt Than Blackwell
published_at: 2026-07-21
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://coreweave.com/blog/nvidia-vera-rubin-nvl72-on-coreweave-10x-more-tokens-per-megawatt-than-blackwell
locator: DeepSeek R1、matched interactivity、10x tokens-per-second per megawatt、已開啟的 inference optimizations 與 starting point 段落
limitation: 單一營運商自家發布、單一工作負載與未披露重複試驗的測試；沒有獨立重現、完整功率邊界、上線機櫃數、利用率、價格、收入、成本、客戶驗收或台灣供應商歸因；擷取 HTML SHA-256 ef1ca7edeb08edf5b345bc3b23617c7860a9fe122f0c3a208cc6ce966e73910e
independence_group: coreweave
-->

<!-- research_source
source_id: S16
role: company_release
source_kind: living_index
publisher: CoreWeave
title: NVIDIA Vera Rubin on CoreWeave Cloud
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.coreweave.com/products/nvidia-vera-rubin
locator: 2026-08-14 可見的單櫃 72 Rubin GPUs／36 Vera CPUs，以及 DeepSeek R1、150 TPS／user 下 GB200 80,000 與 Vera Rubin 800,000 TPS／MW 表格
limitation: 動態產品頁與 S15 同屬 CoreWeave 消息鏈；頁面數值不提供測試樣本、變異、完整方法、獨立驗證、商業價格、利用率或財務結果；擷取 HTML SHA-256 8ec7effe7831d334e07432cc24606a757078544e6c31805e8acdcb960481147b
independence_group: coreweave
-->

<!-- research_source
source_id: S17
role: standard
source_kind: document
publisher: GS1
title: EPCIS Standard 2.0.1
published_at: 2025-07-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://ref.gs1.org/standards/epcis/2.0.1/
locator: PDF pp.24、47、59、67；transaction／visibility event data 隨同一物件移動持續產生、what／when／where／why／how 五維、shipping／receiving business step，以及 eventTime 表示 business step 完成時點
limitation: GS1 是通用事件資料標準；本文只借用其可稽核欄位設計，不能據此宣稱 NVIDIA、Rubin 客戶或台灣供應商採用 EPCIS，也不提供任何 Rubin 數量、驗收或財務結果；官方 PDF SHA-256 6c9b2b51b41cd2cf169f6723001cac56a31c574e9c79ec8d4d52d2bf505f8eaa
independence_group: gs1
-->

<!-- research_source
source_id: S18
role: standard
source_kind: living_index
publisher: IFRS Foundation
title: IFRS 15 Revenue from Contracts with Customers
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/
locator: About 與五步驟摘要；履約義務完成、承諾商品或服務移轉，以及客戶取得控制時認列收入
limitation: 準則頁提供一般原則，不判定任何具體 Rubin 合約的履約義務、控制移轉時點、交易價格、驗收條款、收入期間或現金回收
independence_group: ifrs-foundation
-->

<!-- research_source
source_id: S19
role: company_filing
source_kind: document
publisher: Wiwynn / KPMG
title: Wiwynn Corporation and Subsidiaries Consolidated Financial Statements for the Years Ended December 31 2025 and 2024
published_at: 2026-02-26
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.wiwynn.com/hubfs/Investors/Financial_Report/Wiwynn_2025Q4_Financial.pdf
locator: auditor report p.4-1（PDF p.5）收入認列時點關鍵查核事項；note 4(n) pp.22–23（PDF pp.25–26）控制移轉、指定地點交付、風險移轉、客戶驗收／條款失效／客觀條件與應收款政策
limitation: 財報只支持緯穎集團所揭露商品銷售的一般會計政策與 2025 年查核風險；沒有具名 Rubin 合約、機櫃數、出貨、到貨、驗收、收入、毛利或現金，不能外推成其他公司或所有 AI 機架的共同條款；官方 PDF SHA-256 74f781c2f3863c7fb772908f289504cd1c0039ce760fbca922da424c236a101d
independence_group: wiwynn
-->

<!-- research_source
source_id: S20
role: company_filing
source_kind: document
publisher: NVIDIA
title: NVIDIA Announces Financial Results for Second Quarter Fiscal 2027
published_at: 2026-08-26
captured_at: 2026-08-31
accepted_at: 2026-08-31
status: active
url: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx
locator: Data Center highlights 的 Vera Rubin ramping into full production，以及 racks running at CoreWeave、Google Cloud、Microsoft Azure、OCI 與 Nebius
limitation: NVIDIA 財報新聞稿只支持公司對平台生產階段與具名運行地點的陳述；未披露 production shipment 的物件、數量、具名 ODM、站點驗收、Rubin 專屬收入或台灣供應商財務歸因，且與 S21 同屬 NVIDIA 消息鏈
independence_group: nvidia
-->

<!-- research_source
source_id: S21
role: company_filing
source_kind: document
publisher: NVIDIA
title: NVIDIA Corporation Q2 Fiscal 2027 Earnings Call Corrected Transcript
published_at: 2026-08-26
captured_at: 2026-08-31
accepted_at: 2026-08-31
status: active
url: https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf
locator: prepared remarks 的 commenced production shipments of Vera Rubin earlier this month，以及 purchase orders from every major hyperscaler、AI cloud and system OEM
limitation: 公司法說逐字稿支持管理層對 8 月 production shipments 與廣義採購單類別的陳述；沒有物件、數量、具名交易對手、ODM 分配、客戶 acceptance、控制移轉或供應商財務共同鍵，也不能把 PO 當成已驗收或已認列收入
independence_group: nvidia
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: NVIDIA 在 2026-07-21 將 Vera Rubin 描述為 NVL72 量產爬坡、合作夥伴機架運行與供應鏈部署階段，並稱 Spectrum-6 已進入首批 gigascale AI factories
supporting_source_ids: S1,S2
contrary_source_ids:
as_of: 2026-07-27
basis: S1 與 S2 的產品階段及部署段落直接支持這項平台里程碑
boundary: 這只證實 NVIDIA 對自身平台階段的正式敘述，不證明台灣供應商的公司級出貨或財務貢獻
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: inference
status: superseded
claim: 研究重點應由是否仍在路線圖轉向客戶驗收、量產出貨、收入認列與獲利品質
supporting_source_ids: S1,S2,S5,S7
contrary_source_ids:
as_of: 2026-07-27
basis: 平台已公開進入量產與部署且系統夥伴先前被列名，因此下一個可裁決階段已移到公司執行與財務足跡
boundary: 這是研究流程的階段推論，不代表任何被列名公司一定取得新增訂單或較高毛利
verification_needed: 被列名公司後續法說、財報、出貨與客戶驗收資料
corrected_by_claim_id: C11
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: 2026-07-24 的韓國 AI factory 與記憶體合作文件包含非拘束性提案或合作意向，尚不是已交付訂單
supporting_source_ids: S3,S4
contrary_source_ids:
as_of: 2026-07-27
basis: S3 與 S4 對合作形式、條件及意向的原始措辭直接支持此敘述
boundary: 不能把合作規模或平台規劃當成當期設備採購、HBM 出貨或收入認列
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: verified
status: active
claim: NVIDIA 先前公開列名 GIGABYTE、QCT、Wistron 與 Wiwynn 為 Vera 系統夥伴
supporting_source_ids: S5,S7
contrary_source_ids:
as_of: 2026-07-27
basis: S5 的系統夥伴段落直接列出四家公司
boundary: 夥伴列名不等於新增訂單金額、出貨占比、市占、收入或毛利
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: 技嘉、廣達、緯創、緯穎及散熱、PCB、電源、台灣記憶體公司已因本次平台量產取得可量化新增獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-07-27
basis: 既有來源只到平台進度、合作意向與生態系列名，沒有公司級訂單及財務資料
boundary: 不得把此主張寫入正式公司筆記或作為 H# 終態證據
verification_needed: 公司一手文件須提供驗證、量產、客戶驗收、收入及毛利或現金流足跡
resolution:
-->

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: CoreWeave 於 2026-06-01 宣稱已把 Vera Rubin NVL72 整櫃帶起、完成整個 rack-scale architecture 的 system-level validation，並稱該系統 fully operational
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-06-01
basis: S8 的 bring-up、system-level validation 與 operational 段落直接支持這項營運商里程碑
boundary: 這是 CoreWeave 對單一整櫃與自身工程能力的公司主張；未披露測試母體、長時間客戶 workload、可取得的服務 SKU、機架數、跨站點複製或台灣供應商財務結果
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: Google／Alphabet 2026Q2 CEO remarks 稱 Google Cloud 提供的加速器組合包含 new NVIDIA Vera Rubin platform
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-07-22
basis: S9 的 Google Cloud 段落直接使用 offer 與 including the new NVIDIA Vera Rubin platform 的公司措辭
boundary: 只證實 Google 的供應語言；未披露 SKU、地區、preview／GA、容量、利用率、工作負載、系統供應商或 Rubin 專屬收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: 緯創 2026-07-21 文件稱 Texas D1 當時生產 GB300，Vera Rubin 將在該廠接續生產，因此 Rubin 在這份文件仍是未來製造計畫
supporting_source_ids: S10
contrary_source_ids:
as_of: 2026-07-21
basis: S10 同一段以 right now／produces 描述 GB300，並以 going to／soon 描述 Vera Rubin
boundary: 工廠與未來產品已具名，不等於 Rubin 已在該廠量產、出貨、客戶驗收、形成收入或帶來毛利
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: 技嘉 GIGAPOD 現行型錄於 2026-08-12 可見 Vera Rubin NVL72 機架列，並列出 240 kW、power shelf 與 in-row CDU 等公開配置
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-08-12
basis: S11 的 Vera Rubin NVL72 型錄列直接提供 GPU／CPU、rack power、power shelf 與 cooling 欄位
boundary: 動態型錄與配置不證明能立即下單、交期、實際生產、出貨、客戶驗收、訂單金額、收入或毛利
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: 緯穎現行 AI Infrastructure 頁面於 2026-08-12 把自身定位在 Vera Rubin NVL72 commercialization，稱提供 production-ready rack-scale solutions，並具 L12 integration 與 full system-level validation 能力
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-08-12
basis: S12 的 Vera Rubin 與 Full-stack System Integration 段落直接支持這些公司自述
boundary: Production-ready、commercialization 與能力行銷不披露實際 Rubin 機架出貨、客戶驗收、部署量、獨立測試、收入或毛利
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C11
label: inference
status: active
claim: Vera Rubin 的公開成熟度不能只分成路線圖與量產；現行研究至少要分成平台生產、系統設計／型錄就緒、工廠實際生產、整櫃 bring-up／系統驗證、站點啟用／客戶驗收、雲端可用／工作負載運行、供應商財務歸因七個可分別失敗的交接關卡
supporting_source_ids: S1,S7,S8,S9,S10,S11,S12
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C2；S1 定位平台生產，S7／S11／S12 提供系統展示、型錄與 production-ready 語言，S10 把當前 GB300 生產與未來 Rubin 分開，S8 提供整櫃帶起與系統驗證，S9 提供雲端 offer 語言；各來源證明的交接不同，足以取代原先從路線圖直接跳到驗收與財務的粗框架
boundary: 七關是研究用責任與證據分類，不主張每家公司採相同術語或固定順序，也不把任何一關自動推成下一關；截至本日仍不能估台灣公司 Rubin 訂單、出貨量、份額、收入、毛利、現金流或投資報酬
verification_needed: 同一具名平台須留下可對時的 factory build、rack validation、site commissioning／acceptance、service SKU／workload 與台灣公司財務橋接，才能裁決七關是否閉合或需再拆分
correction_kind: supersedes
corrects_claim_id: C2
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: NVIDIA 現行產品頁於 2026-08-12 將 Vera Rubin 描述為由五套 purpose-built rack-scale systems 組成的 multi-rack POD-scale system，並分列 NVL72 運算、NVLink scale-up、Spectrum-X／Quantum-X scale-out、液冷 Vera CPU 與 BlueField storage 等系統責任
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-08-12
basis: S13 的平台總覽與五套機架級系統段落直接列出上述組成及角色
boundary: 這是 NVIDIA 的當日架構與產品描述，不是客戶最終 configuration lock、所有站點的共同 BOM、可下單狀態、供應商分配、出貨、客戶驗收、收入或毛利證據
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C13
label: verified
status: active
claim: NVIDIA 於 2026-07-16 宣布正與 Noetra 規劃一座採 Vera Rubin NVL72／DSX 與 Spectrum-X 的 AI factory，公告列出 13,750 顆 Vera CPU、27,500 顆 Rubin GPU 與 140MW data center capacity
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-08-14
basis: S14 的 News Summary 與 AI factory 段落直接列出專案、晶片數量、容量及架構
boundary: 這是 NVIDIA／Noetra 的未來式專案公告，不證明建置分期、已通電容量、整數機櫃訂單、交貨、站點驗收、台灣供應商或收入／毛利
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C14
label: inference
status: active
claim: 將 Noetra 公告的 27,500 顆 GPU 與 13,750 顆 CPU 分別除以 CoreWeave 公開的每櫃 72／36 顆，兩者都得到 6,875／18、約 381.944 個配置單位；這只驗證 2：1 拓撲比例一致，不能把非整數結果四捨五入成 382 櫃確定訂單
supporting_source_ids: S14,S16
contrary_source_ids:
as_of: 2026-08-14
basis: S14 提供專案晶片總數，S16 提供單櫃 72 GPU／36 CPU；Python Fraction 與 awk 兩條獨立路徑重算皆得到 6,875／18 及 GPU：CPU 2：1
boundary: 原文未說非整數尾差是四捨五入、備品、分期或其他 BOM，也未定義 140MW 的設施／IT／分期邊界；不得拿站點 MW 與另一廠商單櫃 kW 直接推估訂單、收入或市占
verification_needed: Noetra／NVIDIA 提供有版本的 configuration、分期、rack count、order／shipment、commissioning 與 acceptance
resolution:
-->

<!-- research_claim
claim_id: C15
label: verified
status: active
claim: CoreWeave 於 2026-07-21 自行公布 Vera Rubin NVL72 在相近 interactivity、同一 DeepSeek R1 工作負載下達 GB200 NVL72 的 10 倍 tokens／MW；其動態產品頁於 2026-08-14 列出 150 TPS／user 下 800,000 對 80,000 TPS／MW
supporting_source_ids: S15,S16
contrary_source_ids:
as_of: 2026-08-14
basis: S15 的 matched interactivity 與 10x 段落，以及 S16 同口徑產品表格直接支持 CoreWeave 公開的比較主張
boundary: 這是 1 家營運商、1 個具名工作負載、2 平台的自家測試，且開啟多項最佳化；沒有重複試驗、變異、獨立重現、完整功率邊界或跨模型證據，不代表全站點 10 倍、10 倍收入或 90% 總成本下降
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C16
label: inference
status: active
claim: 從 tokens／MW benchmark 推進到供應商獲利，至少要分別跨過技術可重現、長時間營運、商業變現、財務與供應鏈歸因四座橋；任一橋缺失時，10 倍效率都不能直接改寫成 10 倍營收或所有台灣供應商共同受惠
supporting_source_ids: S14,S15,S16
contrary_source_ids:
as_of: 2026-08-14
basis: S14 只到未來式專案容量，S15／S16 只到特定測試與動態產品表；三份來源都未提供利用率、價格、供應商出貨、收入、毛利、存貨與現金流，因此必須保留四段橋接
boundary: 四橋是可證偽的研究責任分類，不主張橋與橋之間固定線性、10 倍結果必然失效或任何公司一定受惠／受害；本文未評估價格、估值、共識、部位或投資報酬
verification_needed: 其他營運商與工作負載的同條件重測、production SLO／利用率、billable demand／pricing、站點 acceptance，以及台灣買賣雙方同期間財務橋接
resolution:
-->

<!-- research_claim
claim_id: C17
label: verified
status: active
claim: GS1 EPCIS 2.0.1 把供應鏈事件拆成 what、when、where、why、how 五個維度，以 business step 區分 shipping／receiving 等流程，並把 eventTime 定義為該 business step 的完成時點；同一物件沿供應鏈移動會持續產生新的 transaction／visibility event data
supporting_source_ids: S17
contrary_source_ids:
as_of: 2026-08-14
basis: S17 PDF pp.24、47、59、67 直接說明同一實體移動時持續產生事件資料、五個事件維度、business step 與 eventTime 語意
boundary: 這只證明 GS1 的通用事件資料模型；本文借用欄位做研究護照，不主張 NVIDIA、Rubin 客戶、緯穎或其他台灣公司實際採用 EPCIS，也不提供 Rubin 出貨數量
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C18
label: verified
status: active
claim: IFRS Foundation 將 IFRS 15 的收入認列連到履約義務完成與客戶取得控制；緯穎 2025 合併財報則把商品收入政策連到指定地點交付、風險移轉與客戶驗收條件，KPMG 並把收入認列時點列為關鍵查核事項
supporting_source_ids: S18,S19
contrary_source_ids:
as_of: 2026-08-14
basis: S18 的 IFRS 15 五步驟摘要直接說明控制移轉原則；S19 auditor report p.4-1 與 note 4(n) pp.22–23 直接列出緯穎收入時點查核風險、交付、風險移轉、驗收及應收政策
boundary: 準則原則與緯穎公司層級政策都不能判定任何 Rubin 合約的控制移轉、驗收、收入或現金；緯穎政策也不是其他系統廠或所有 AI 機架的共同合約
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C19
label: inference
status: active
claim: Rubin 出貨研究應用同一產品與版本鍵保存物件／數量階層、business step、完成時間、地點與交易雙方、淨額調整及控制／財務七欄，並把完工、出貨、到貨、commissioning、驗收、可用、可計費、收入與收款當成九個不可直接相加的事件鐘
supporting_source_ids: S17,S18,S19
contrary_source_ids:
as_of: 2026-08-14
basis: S17 證明同一實體會留下多個供應鏈事件且事件必須有物件、時間、地點與流程語意；S18／S19 證明收入還要另核對控制、合約及驗收，因此需要用共同物件鍵把實體、營運與財務事件逐筆串接
boundary: 九鐘與七欄是可證偽的研究責任分類，不宣稱所有合約固定依序發生、每家公司採相同術語，或任一 Rubin 事件已實際完成；本文沒有把事件數換算成新增設備或收入
verification_needed: 具名買賣雙方對同一 Rubin configuration／serial range 公開逐期 built、shipped、received、installed、accepted、available、billable、revenue／receivable 與 cash reconciliation，含更正、備品、替換、退貨及取消
resolution:
-->

<!-- research_claim
claim_id: C20
label: unverified
status: active
claim: 截至 2026-08-14，公開一手資料尚未以同一產品鍵把任何台灣系統廠 Rubin 的完工、出貨、到貨、驗收、可用／可計費容量、收入、應收與現金回收完整對帳
supporting_source_ids: S1,S10,S11,S12,S13,S19
contrary_source_ids:
as_of: 2026-08-14
basis: 平台、工廠、型錄、能力與公司財報分屬不同文件與觀察單位；S19 只有公司一般政策，現有來源沒有 Rubin 專屬序號／版本、交易雙方、事件數量與財務共同鍵
boundary: 缺乏公開完整帳本不代表沒有實際訂單、出貨或收入，只表示本文不能從現有證據估數量、份額、營收、毛利、現金流或投資報酬
verification_needed: 台灣公司或具名客戶提供可對時的 Rubin 產品版本、數量單位、shipping／receiving、site acceptance、available／billable capacity、收入／應收與收款，並能排除備品、替換、退貨、取消及重複計數
resolution:
-->

<!-- research_claim
claim_id: C21
label: verified
status: active
claim: NVIDIA 於 2026-08-26 的 2027 財年第二季財報稱 Vera Rubin 正進入 full production；同日法說管理層稱 8 月較早時已開始 production shipments，並已收到各主要 hyperscaler、AI cloud 與 system OEM 類別的採購單
supporting_source_ids: S20,S21
contrary_source_ids:
as_of: 2026-08-26
basis: S20 的 Data Center highlights 與 S21 的 prepared remarks 分別直接提供 full production、production shipments 月份及採購單對手類別；兩份文件屬同一 NVIDIA 消息鏈，不當作兩條獨立市場觀測
boundary: 文件未定義出貨物件、數量、具名買方、具名 ODM、站點收貨／驗收、控制移轉或 Rubin 專屬收入；PO 也不等於已出貨、已驗收或供應商已認列收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C22
label: inference
status: active
claim: NVIDIA 的 8 月 production shipment 與採購單陳述使七關中的平台生產證據前進，但在出貨物件、數量、具名交易雙方、ODM 工廠、site acceptance、service workload 與台灣公司財務共同鍵缺失時，不能據此關閉工廠生產、站點驗收、工作負載或供應商財務歸因關卡
supporting_source_ids: S20,S21
contrary_source_ids:
as_of: 2026-08-31
basis: S20／S21 明確提供平台階段、出貨月份與廣義 PO 類別，也同時缺少 C11 七關後段與 C19 七欄事件護照所需的物件、交易、驗收及財務欄位
boundary: 這是研究成熟度分類，不否定實際供應鏈可能已有未公開生產或收入；也不估台灣公司的份額、營收、毛利、現金流、價格或投資報酬
verification_needed: NVIDIA、具名客戶與 ODM 對同一 Rubin configuration 公開可對時的 shipment object／quantity、factory build、received／accepted、service SKU／workload，以及台灣公司收入、毛利、存貨或現金流共同鍵
resolution:
-->

## 影響路由

<!-- impact
group_id: serverodm
stock_ids: 2376
direction: tailwind
hypothesis_refs:
note_action: done
action_due:
rationale: 已把技嘉小作文中未加日期限定的「Rubin 仍在 early-stage」改回 5/15 公司法說的歷史切面，並收窄公司級驗證節點
evidence_boundary: 正式筆記的 5/15 歷史紀錄與 H1 均未改；NVIDIA 平台 ramp 不證實技嘉新增訂單、收入或毛利
-->

<!-- impact
group_id: serverodm
stock_ids: 2382,3231,6669
direction: tailwind
hypothesis_refs:
note_action: review_due
action_due: 2026-08-03
rationale: 三份小作文沒有過時的 Rubin 階段敘述，只需在下一公司 IR 檢查驗證、量產、客戶驗收與財務認列
evidence_boundary: QCT、Wistron、Wiwynn 被列入生態系不等於個別公司新增訂單、收入或毛利
-->

<!-- impact
group_id: thermal
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-03
rationale: Spectrum-6 與 Vera Rubin 公告明確提到液冷及高溫進水設計，可能改變散熱內容量
evidence_boundary: NVIDIA 未在這批公告點名 universe 散熱供應商
-->

<!-- impact
group_id: pcb
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-03
rationale: 更高密度互連與交換器量產構成檢查高階板需求的產業觸發
evidence_boundary: 未有公司層級料號、份額或訂單證據
-->

<!-- impact
group_id: powersupply
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-03
rationale: 大型 AI factory 與每瓦效能訴求構成檢查電源架構變化的產業觸發
evidence_boundary: 未有公司層級供應關係或財務貢獻證據
-->

<!-- impact
group_id: memory
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-03
rationale: SK hynix 與 NVIDIA 正式揭露 HBM4 及下一代 AI memory 合作，需檢查台灣記憶體小作文是否誤用同業事件
evidence_boundary: SK hynix HBM 合作不是台灣 DRAM 個股直接受惠證據
-->

## 持續驗證帳本

<!-- monitoring_item
monitor_id: T1
status: retired
claim_ids: C1,C2,C4
metric: Vera Rubin 與 Spectrum-6 的客戶驗收、量產出貨及公司收入認列
source_ids: S1,S2,S5
watch_source_ids: S6
frequency: event_driven
next_check: 2026-08-03
trigger: NVIDIA 或被列名系統廠公布具體量產、部署、驗收、出貨或收入節點
invalidation: 平台時程延後、部署停留展示，或公司文件仍無產品與財務對應
retired_at: 2026-08-12
retirement_reason: C2 已由 C11 修正為七關交接框架；T1 的台灣系統廠 shipment／acceptance／revenue trigger 經本輪 no_new_evidence 回查後，由 T3 接續逐關追蹤
-->

<!-- monitoring_item
monitor_id: T2
status: retired
claim_ids: C2,C3,C5
metric: 系統與零組件供應商的毛利、存貨、營業現金流及韓國 HBM 合作落地
source_ids: S1,S3,S4,S5,S6
watch_source_ids: S6
frequency: quarterly
next_check: 2026-08-15
trigger: 公司法說或財報把具名平台連到量產收入、獲利與現金流
invalidation: 只有合作意向或營收敘事，沒有公司級產品、客戶與獲利交叉證據
retired_at: 2026-08-12
retirement_reason: T2 依賴已被 C11 取代的 C2 粗框架；未因到期結果改判，改由 T4 以雙向平台與公司財務橋接接續原 2026-08-15 檢查期限
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C1,C6,C7,C8,C9,C10,C11
metric: Vera Rubin 七關交接的公開進度：平台生產、系統型錄、工廠生產、整櫃驗證、站點驗收、雲端 workload 與供應商財務歸因
source_ids: S1,S8,S9,S10
watch_source_ids: S11,S12
frequency: weekly
frequency_detail: 每週保存技嘉與緯穎動態頁，並回查 NVIDIA、CoreWeave、Google 與具名系統廠是否新增下一關的一手節點
next_check: 2026-08-19
trigger: 任一來源首次提供可定位日期、產品／SKU、地點、機架數或 workload，將現有型錄／future plan／validation／offer 推進到下一個交接關卡
invalidation: 時程延後、型錄撤除、工廠仍停留未來式、validation 無法擴展、雲端缺乏可取得 SKU 或 workload 結果，使相應關卡成熟度下修
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C5,C8,C9,C10,C11
metric: 台灣系統與零組件公司能否以雙向證據把 Rubin 的 qualification／生產／驗收連到收入、毛利、存貨與現金流
source_ids: S5,S10
watch_source_ids: S6,S11,S12
frequency: quarterly
frequency_detail: 對齊公司法說與財報，另保存台灣系統廠動態型錄；只有產品身分、期間、交付階段與經濟量同時對上才升格
next_check: 2026-08-15
trigger: 平台／客戶端與台灣公司端同時具名 Rubin，並留下量產出貨或驗收及可核對的收入、毛利、存貨或現金流橋接
invalidation: 只有 AI server 總營收、平台列名、型錄、未來生產或管理層方向敘事，沒有 Rubin 專屬產品、期間與財務交叉證據
-->

<!-- monitoring_item
monitor_id: T5
status: active
claim_ids: C12
metric: Vera Rubin 平台組成、可選配置與交付狀態是否形成有版本的系統契約
source_ids: S13
watch_source_ids: S13
frequency: monthly
frequency_detail: 每月與重大產品事件保存 NVIDIA 動態頁，逐項比對五套 rack-scale systems、NVL72、網路、CPU 冷卻、storage 與商業狀態是否改版
next_check: 2026-08-31
trigger: NVIDIA 或具名客戶公布有版本的 BOM／configuration matrix、qualified system、orderability、site acceptance 或 workload contract
invalidation: 動態頁撤除或改寫既有系統組成，或後續客戶文件證明配置僅屬選配、未通過資格或與實際交付不一致
-->

## 下一個可證明／否定的節點

- 技嘉下一份公司 IR 是否把 Rubin 從生態系／開發名單推進到可量化的驗證、量產出貨、
  客戶驗收或收入認列；正式筆記仍保留 5/15 當時的公司揭露，不以 NVIDIA 公告覆寫。
- 廣達、緯創、緯穎下一次法說或財務結果是否明確區分驗證、量產、出貨、收入認列，
  並留下毛利、存貨、現金流或淨利的公司級足跡。
- 散熱、PCB、電源供應商是否以一手文件揭露 Rubin/Spectrum-6 相關產品與量產時程。
- 若只看到產業轉述或股價反應，維持 `watch`；不得升格為正式筆記或 H# 終態證據。
