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
confidence_basis: NVIDIA、CoreWeave、Google 與三家台灣系統廠一手文件已能把平台、型錄、未來工廠、整櫃驗證與雲端供應語言拆成不同成熟度關卡；但台灣公司實際 Rubin 出貨、客戶驗收、收入與獲利橋接仍無可重算證據
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

### 三句話抓重點

- Vera Rubin 的公開證據已橫跨平台量產、系統型錄、未來工廠、整櫃驗證與雲端供應語言，不能再只用「路線圖／已量產」二分法。
- 每份文件只跨過七關中的一部分：CoreWeave 的 rack bring-up、Google 的 offer、緯創的未來生產、技嘉的型錄與緯穎的 production-ready 都不是同一張證書。
- 截至 2026-08-12，仍沒有一手資料把台灣公司實際 Rubin 出貨、客戶驗收、平台收入與獲利完整接起來；平台成熟不等於個股財務受惠已證實。

### 為什麼重要

平台從規劃走向部署，會把研究問題從「技術會不會出現」改成「何時通過驗收、出多少、
哪一家公司能留下收入與毛利」。若沒有分清平台里程碑與公司財務證據，讀者很容易把一則
供應鏈新聞誤讀成所有伺服器、散熱、PCB、電源與記憶體公司的共同利多。

### 接下來怎麼追

- 追 NVIDIA 是否公布 Vera Rubin 與 Spectrum-6 的實際部署數量、客戶驗收及量產節奏。
- 追被列名系統廠下一次法說是否出現具名產品階段、出貨、收入、毛利、存貨與現金流足跡。
- 追散熱、PCB、電源與記憶體公司是否以自身一手文件建立供應關係，而不是沿用平台名單。

### 想一想

- 平台商說「量產」時，哪一個公司級數字才能證明台灣供應商真的取得經濟利益？
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
| 1. 平台進入生產 | 平台商是否已把設計推進持續製造與供應鏈爬坡？ | NVIDIA 稱 Vera Rubin 進入 full production／ramp | 個別系統廠拿到多少量、良率或收入 |
| 2. 設計／型錄就緒 | 系統廠是否公開可辨識的機架、配置與整合角色？ | 技嘉列出 Vera Rubin NVL72 機架配置；緯穎稱 production-ready | 可立即下單、交期、客戶或出貨量 |
| 3. 工廠實際生產 | 哪一座工廠現在正做哪個世代？ | 緯創稱 Texas D1 現在生產 GB300，Rubin 將接續 | Rubin 已在該廠量產或已形成收入 |
| 4. 整櫃 bring-up／驗證 | 把整個機架帶起後，系統級路徑能否運作？ | CoreWeave 稱完成 NVL72 整櫃 bring-up 與 system-level validation | 測試母體、長時間負載、客戶驗收與廣泛複製 |
| 5. 站點啟用／客戶驗收 | 機架到特定機房後，電力、冷卻、網路與軟體是否完成交接？ | 公開來源尚未提供台灣系統廠可核對的 acceptance 節點 | 誰簽收、何時可計費、多少機架通過 |
| 6. 雲端可用／工作負載運行 | 客戶能否取得服務，且真實工作負載是否持續運作？ | Google 稱 Cloud 提供 Vera Rubin；NVIDIA 列名多個運行站點 | SKU、區域、GA 條款、容量、利用率及 workload SLO |
| 7. 供應商財務歸因 | 哪家公司因哪些數量與單價留下收入、毛利及現金流？ | 尚無可重算的台灣公司 Rubin 橋接 | 個股受惠幅度、份額、獲利與現金回收 |

這張表不是要求所有公司使用相同術語，而是把研究的「停止線」畫清楚。例如，Google 的
`offer` 比單純列名更接近服務端，但若沒有產品代碼、地區、容量與取得方式，就不能自行寫成
全球全面 GA；緯創說「soon」也只能放在未來生產關，不得改寫成當期 Rubin 產量。

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

上述資料只證實 NVIDIA 平台與其公開列名生態系。它沒有披露技嘉、廣達、緯創或緯穎的
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
