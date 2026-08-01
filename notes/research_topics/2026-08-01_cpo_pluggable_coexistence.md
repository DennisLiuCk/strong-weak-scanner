# NVIDIA Spectrum-X CPO 已進入量產，但 1.6T 可插拔仍同步放量

<!-- research_topic
topic_id: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE
schema_version: 2
status: triaged
priority: p1
captured_at: 2026-08-01
source_published_at: 2026-05-31
last_reviewed_at: 2026-08-01
review_due: 2026-08-15
source_type: mixed
publisher_domain: nvidia.com
canonical_url: https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory
source_chain_id: nvidia-cpo-production-marvell-1p6t-20260312-20260721
stock_ids: 3711
group_ids: packtest
trigger_type: product_ramp
evidence_role: candidate_source
route: market_issue_watch
-->

<!-- transition
date: 2026-08-01
from: initial
to: inbox
reason: official_cpo_production_and_pluggable_volume_sources_captured
evidence: source_chain:nvidia-cpo-production-marvell-1p6t-20260312-20260721
-->

<!-- transition
date: 2026-08-01
from: inbox
to: triaged
reason: architecture_coexistence_and_taiwan_mapping_reviewed
evidence: source_chain:nvidia-cpo-production-marvell-1p6t-20260312-20260721
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **CPO（共同封裝光學）**：把光學元件放到交換晶片旁邊，縮短高速電訊號在電路板上行走的距離，以降低耗電與訊號損失。
- **可插拔光模組（pluggable optics）**：裝在交換器面板、可以拔換的光通訊模組；維修與升級彈性較高，資料中心已累積成熟的部署流程。
- **SerDes**：把晶片內的平行資料轉成高速序列訊號、再在另一端還原的介面；速度愈高，傳輸距離、耗電與訊號完整性愈難兼顧。
- **1.6T**：每秒 1.6 兆位元的光連線容量，描述連線速度，不等於某一種固定封裝或光學架構。

### 三句話抓重點

- NVIDIA 已把 Spectrum-X Ethernet Photonics CPO 交換器定義為進入量產，並直接列名 SPIL 負責晶片級封裝、組裝與測試。
- 同一代 Spectrum-6 同時支援 CPO 與可插拔形式，Marvell 的 1.6T Ara 可插拔 DSP 也已大量出貨，因此基準情境應是分工共存而非一夜替代。
- 對台灣供應鏈，目前只有 SPIL 的角色被平台商直接點名；頎邦與訊芯的 CPO 主張仍要等待公司文件證明客戶、量產收入與毛利。

### 為什麼重要

「CPO 量產」看似是一句產業利多，真正影響卻取決於它取代的是哪一段連線、部署在多少交換器，以及價值從可插拔模組轉到光引擎、封裝測試或交換器系統的哪一環。把架構選擇、產品階段與公司曝險拆開，才能避免把技術突破直接抄成所有矽光子公司的訂單故事。

### 接下來怎麼追

- 追 NVIDIA 首批採用者的實際部署、Spectrum-6 中 CPO／可插拔機型組合，以及 2026 年秋季 Vera Rubin 出貨後的交換器 attach rate。
- 追日月光投控是否在法說或財報拆出 SPIL 光電共同封裝的收入、產能、客戶驗證與毛利，而不只停在生態系列名。
- 追 6147:H1／H2 與 6451:H1／H2 是否從「送樣、小量生產、媒體轉述」前進到正式客戶、規模收入與獲利證據。

### 想一想

- 若 Spectrum-6 本身同時支援兩種形式，CPO 最先會取代所有連線，還是只先解決功耗與可靠度最吃緊的特定位置？
- 平台商宣布「量產」之後，哪一個數字最能證明台灣供應商真的取得經濟利益：出貨量、收入占比、稼動率還是毛利？
- 可插拔模組若繼續大量出貨，這代表 CPO 失敗，還是兩種架構各自服務不同距離、維修與成本需求？

## 已驗證的兩條量產路徑

| 路徑 | 一手來源明講的事實 | 仍屬發行人主張或未知 |
|---|---|---|
| NVIDIA CPO | 2026-05-31 新聞稿稱 Spectrum-X Ethernet Photonics 已進入生產，採 200Gb/s SerDes；CoreWeave、Lambda、OCI 被列為首批生態系採用者。 | 5 倍功耗效率、5 倍 uptime 與 1.3 倍部署速度是 NVIDIA 的比較結果；未見獨立測試、部署數量、售價或收入。
| 台灣製造鏈 | NVIDIA 2026-06-01 更新列名 TSMC 做矽光子製造、SPIL 做晶片級封裝／組裝／測試、TFC 做雷射模組、Foxconn 做系統組裝。 | 列名角色不等於新增訂單金額、市占或毛利；也不能把未列名的同業自動放進同一供應鏈。
| 同代雙架構 | NVIDIA 2026-07-21 說明 Spectrum-6 支援可插拔與 CPO 兩種 form factor。 | 官方沒有公布兩種形式的出貨配比、使用位置與生命週期成本。
| 1.6T 可插拔 | Marvell 2026-03-12 表示 Ara 1.6T 光 DSP 正大量出貨給全球客戶，用於可插拔連線。 | 「大量」未附數量、客戶拆分或市占；新 Ara 衍生產品的效能與成本優勢仍是供應商描述。

四筆證據合在一起，比單看任一新聞更有用：CPO 已跨過純路線圖階段，但可插拔並未因此退出；甚至 NVIDIA 自己也保留雙形式。合理的研究問題不是「誰消滅誰」，而是**哪一種連線位置先切換、切換速度多快、價值量搬到哪裡**。

## 產業鏈與投資判讀

### 先按使用場景，而不是按口號分類

- **CPO 較可能先被採用的地方**：頻寬密度、功耗或可靠度已逼近前面板光模組限制，而且營運者願意接受更複雜的維修方式。
- **可插拔較可能保留的地方**：需要現場替換、跨供應商互通、較彈性的升級節奏，或功耗尚未成為首要瓶頸。
- **真正要量的分母**：不是 CPO 產品有沒有出貨，而是 CPO 占交換器埠數、光連線數或網路資本支出的比例；目前官方資料尚未提供這些分母。

### 公司證據要走完四級階梯

1. 平台商或公司列名技術合作。
2. 樣品、工程驗證或小量生產。
3. 客戶量產、可辨識收入與產能利用。
4. 毛利、現金流與資本支出證明經濟利益留下來。

SPIL 已有第 1 級且平台已宣布量產，但 NVIDIA 沒有給 SPIL 的公司級第 3、4 級數字。頎邦與訊芯在 repo 既有 H# 中有送樣／小量生產等主張，卻沒有被上述 NVIDIA 或 Marvell 文件列名；它們仍需自己的正式文件補齊，不得借用 SPIL 的證據升級。

## 來源與證據邊界

- [NVIDIA：Vera Rubin 與 Spectrum-X Ethernet Photonics 進入生產，2026-05-31](https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory)
- [NVIDIA GTC Taipei：列名 TSMC、SPIL、TFC、Foxconn 的製造角色，2026-06-01 更新](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/)
- [NVIDIA：Spectrum-6 同時支援可插拔與 CPO，2026-07-21](https://blogs.nvidia.com/blog/nvidia-spectrum-six-arrives-in-gigascale-ai-factories/)
- [Marvell：Ara 1.6T 可插拔 DSP 大量出貨，2026-03-12](https://www.marvell.com/company/newsroom/marvell-1-6t-optical-dsp-ai-data-center-connectivity.html)
- [ASE：SPIL 為日月光投控子公司，2025-01-16](https://www.aseglobal.com/press-room/spil-hosts-nvidia-founder-and-ceo-at-new-factory-site/)

**已知：** CPO 平台已被 NVIDIA 定義為進入生產，SPIL 被直接列名；Spectrum-6 與 Marvell 的資料同時證明可插拔路徑仍在量產生態中。

**還不知道：** CPO／可插拔的實際出貨配比、部署位置、每埠成本、故障率、台灣供應商收入與毛利，以及 6147、6451 是否參與上述具名平台。

**不可外推：** NVIDIA 與 Marvell 的效能、可靠度或成本敘述屬供應商主張；沒有價格、估值、共識與部位資料，本題不判斷市場是否已反映。

## 影響路由

對 `packtest` 的方向定為 `mixed`：CPO 增加光電共同封裝與測試內容量，但可插拔持續放量，也表示價值不會一次全部移轉。公司級處理分成「直接列名」與「待自身文件證明」兩層。

<!-- impact
group_id: packtest
stock_ids: 3711
direction: mixed
hypothesis_refs:
note_action: review_due
action_due: 2026-08-15
rationale: SPIL 被 NVIDIA 直接列為 CPO 封裝組裝測試夥伴，需由日月光投控正式文件裁決量產收入與獲利。
evidence_boundary: 平台量產與生態系列名不等於 3711 已有可量化新增訂單；不建立收入、市占或毛利事實，6147與6451僅保留在正文的既有 H# 複核清單。
-->

## 下一個可證明／否定的節點

- **平台層**：首批雲端採用者是否公布 CPO 交換器數量、部署位置、可靠度或節能的實際值；若只停在展示或少量部署，量產解讀要降級。
- **架構層**：Spectrum-6 後續產品組合是否仍維持雙形式；若可插拔占比長期居高且 CPO 未擴到更多場景，「快速替代」假說被否定。
- **公司層**：3711 是否拆出光電共同封裝的收入／毛利；6147、6451 是否由送樣或小量生產轉為正式量產收入。沒有公司文件，就不把平台證據寫進正式筆記事實。
- **經濟層**：新增封裝與測試內容量是否高於所需資本支出、良率爬坡與維修成本；若收入增加但毛利、現金流未改善，受惠只停在營收表面。
