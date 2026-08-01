# JEDEC 發布 SPHBM4：HBM4 級頻寬可走有機基板，但標準不等於採用

<!-- research_topic
topic_id: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE
schema_version: 3
status: triaged
priority: p2
captured_at: 2026-08-01
source_published_at: 2026-07-13
last_reviewed_at: 2026-08-01
review_due: 2026-08-15
source_type: mixed
publisher_domain: jedec.org
canonical_url: https://www.jedec.org/news/pressreleases/new-jedec%C2%AE-sphbm4-standard-enables-hbm4-class-bandwidth-organic-substrates
source_chain_id: jedec-sphbm4-hbm4-product-clock-20260618-20260713
stock_ids:
group_ids: pcb,ipdesign,packtest
trigger_type: industry_standard
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C2
base_confidence: medium
confidence_basis: 標準內容與產品時鐘有一手資料，但尚未出現 SPHBM4 採用與供應商訂單
cross_company_numbers: false
schema_migrated_at: 2026-08-02
-->

<!-- transition
date: 2026-08-01
from: initial
to: inbox
reason: jedec_sphbm4_standard_captured
evidence: source_chain:jedec-sphbm4-hbm4-product-clock-20260618-20260713
-->

<!-- research_source
source_id: S1
role: standard
publisher: JEDEC
title: JESD330-4 SPHBM4 標準公告
published_at: 2026-07-13
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.jedec.org/news/pressreleases/new-jedec%C2%AE-sphbm4-standard-enables-hbm4-class-bandwidth-organic-substrates
locator: interface base die、4:1 serialization 與 organic substrate 段落
limitation: 標準公告沒有產品、客戶採用、量產時程、良率或供應商名單
-->

<!-- research_source
source_id: S2
role: company_release
publisher: Micron
title: Micron 2026 財年第三季產品與 HBM4 進度
published_at: 2026-06-24
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://investors.micron.com/node/50671
locator: HBM4 high-volume production 段落
limitation: Micron 談的是既有 HBM4 產品，沒有表示採用 SPHBM4
-->

<!-- research_source
source_id: S3
role: competitor_primary
publisher: SK hynix
title: 12 層 HBM4E 樣品公告
published_at: 2026-06-18
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://news.skhynix.com/en/12-layer-hbm4e-sample-1/
locator: sample 與 base die 產品時程段落
limitation: 樣品公告沒有說明 SPHBM4 介面、量產採用或外部封裝供應商
-->

<!-- research_source
source_id: S4
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 台灣基板、矽智財與封測公司季報、法說及重大訊息查找入口
limitation: JEDEC 與記憶體供應商資料只支持技術路徑；入口本身不證明台灣公司料號、認證或量產
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: JEDEC 的 JESD330-4 定義以 interface base die 將 2,048 個 HBM4 資料訊號透過 4 比 1 序列化降為 512 個主機側訊號，並支援標準有機基板
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-07-13
basis: 標準組織公告直接列出訊號數、序列化比例與基板路徑
boundary: 證實的是介面規格，不是產品效能、採用率、良率或量產時程
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: inference
status: active
claim: SPHBM4 提供一條降低主機側連線密度、讓 HBM4 級頻寬可使用有機基板的工程路徑，但近期基準情境仍是補充而非立刻取代既有 HBM4 封裝
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-07-13
basis: JEDEC 已定義新路徑，而兩家記憶體廠同期仍以既有 HBM4 或 HBM4E 產品階段推進
boundary: 沒有 SPHBM4 產品、客戶採用或成本良率資料，不能估計滲透率與替代速度
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: Micron 公告 HBM4 已進入大量生產，SK hynix 公告 HBM4E 仍處於樣品階段
supporting_source_ids: S2,S3
contrary_source_ids:
as_of: 2026-06-24
basis: 兩家記憶體供應商分別直接揭露自身產品階段
boundary: 不同公司的產品名稱與階段不可拿來排名技術優劣，也都沒有證實 SPHBM4 採用
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: unverified
status: active
claim: 台灣 PCB、矽智財或封測公司已取得 SPHBM4 量產訂單或可量化受惠
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-01
basis: JEDEC 與兩家記憶體公司均未列名台灣供應商，也沒有產品級採用資料
boundary: 不建立特定基板材料、base die 設計服務、OSAT 訂單、收入或毛利事實
verification_needed: 需記憶體供應商產品文件與台灣公司法說雙向確認料號、客戶、驗證與量產
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3
metric: 記憶體供應商是否發布 SPHBM4 產品、樣品、客戶採用及功耗延遲數據
source_ids: S1,S2,S3
watch_source_ids: S4
frequency: monthly
frequency_detail: 每月產品公告與每季法說
next_check: 2026-08-15
trigger: 任一供應商首次直接使用 SPHBM4 名稱並揭露樣品、客戶或量產時程
invalidation: 若未出現產品採用且序列化功耗、延遲或可靠度代價抵銷基板優勢，快速採用假說失效
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C4
metric: 台灣基板、矽智財與封測公司的 SPHBM4 料號、認證與量產證據
source_ids: S1,S2,S3,S4
watch_source_ids: S4
frequency: quarterly
frequency_detail: 每季法說與重大訊息
next_check: 2026-10-31
trigger: 公司與記憶體客戶文件可雙向核對相同產品、時程及供應角色
invalidation: 若只有產業標準推導而沒有公司級產品與財務證據，個股受惠映射持續無效
-->

<!-- transition
date: 2026-08-01
from: inbox
to: triaged
reason: standard_product_timeline_and_supplier_boundary_reviewed
evidence: sources:S1,S2,S3
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **HBM4**：把多層 DRAM 疊在一起、用很寬的介面連到運算晶片的第四代高頻寬記憶體；重點是同時傳輸大量資料，不只是單顆記憶體跑得快。
- **有機基板（organic substrate）**：由樹脂等有機材料製成、負責在晶片與電路板之間扇出訊號與電源的封裝基板；「有機」不是指環保認證。
- **interface base die**：位在記憶體堆疊底部、管理高速介面與資料傳送的邏輯晶片；SPHBM4 會更換這一層，而不是更換上方的 HBM4 DRAM dies。
- **序列化（serialization）**：用較少的實體訊號線、讓每條線跑得更快；SPHBM4 以 4:1 序列化降低訊號數，代價要由功耗、延遲與訊號完整性驗證裁決。

### 三句話抓重點

- JEDEC 的 JESD330-4 SPHBM4 標準使用與 HBM4 相同的 DRAM dies，改用新 base die，將 2,048 個資料訊號縮成 512 個並以 4:1 序列化維持總頻寬。
- 這個設計讓 HBM4 級頻寬能連到標準有機基板，但 JEDEC 只發布標準，沒有公布產品、客戶、認證、量產或供應商。
- Micron 的傳統 HBM4 已進入大量出貨、SK hynix 的 HBM4E 已送樣，顯示既有路徑的產品時鐘領先；不能把 SPHBM4 寫成 CoWoS 立即退場或台灣載板廠立即得單。

### 為什麼重要

HBM 的瓶頸不只有 DRAM 產能，也包含 base die、微凸塊、矽中介層、基板面積與封裝良率。SPHBM4 若被實際產品採用，可能改變訊號如何從記憶體走到運算晶片，進而重新分配基板、邏輯晶片與封裝測試的價值；但在第一個具名產品出現以前，它仍是「設計選項」，不是「供應鏈訂單」。

### 接下來怎麼追

- 追 Samsung、SK hynix、Micron 的產品路線圖是否首次出現 SPHBM4 樣品、認證與量產時程，而不只是持續推出傳統 HBM4／HBM4E。
- 追加速器或 base-die 廠是否公布 JESD330-4 支援，以及功耗、延遲、訊號完整性、封裝面積與可用 stack 數的實測。
- 追有機基板供應商是否被具名、是否完成材料與可靠度認證；沒有供應商與客戶名稱前，不建立 3037、3189、8046 等台廠曝險。

### 想一想

- 把 2,048 個資料訊號降到 512 個，是單純降低成本，還是把困難從高密度接點搬到高速 SerDes、功耗與長通道訊號完整性？
- 一個標準發布後，至少還要經過哪些樣品、認證與量產節點，才可以從「可能使用有機基板」升級成「某家公司有收入」？
- 如果傳統 HBM4 已大量出貨，SPHBM4 最可能是全面替代、特定大封裝的補充方案，還是暫時沒有產品化？

## 規格改了什麼，沒有改什麼

| 問題 | 傳統 HBM4 路徑 | SPHBM4（JESD330-4） | 研究含義 |
|---|---|---|---|
| 上方記憶體 | HBM4 DRAM dies | 使用相同 HBM4 DRAM dies | 不是新的 DRAM 世代，也不能外推到 HBM4E dies。
| 底層介面 | 高密度 HBM4 介面 | 新 interface base die | base die 的設計、製程、功耗與供應者成為新驗證點。
| 資料訊號 | 2,048 個 data signals | 512 個 data signals | 不是「總共只有 512 pins」；封裝還有電源、命令與時脈等接點。
| 傳輸方式 | 大量平行訊號 | 4:1 序列化、每條線以更高頻率傳輸 | JEDEC 說總 throughput 可相同，但公開資料未量化系統功耗、延遲或良率。
| 連接基板 | 高密度連接通常仰賴矽基路徑 | 可連到標準有機基板 | 這是架構可行性，不等於特定 ABF／BT 規格或台廠訂單。
| 商業階段 | Micron 已稱 HBM4 對主力客戶平台大量出貨 | 標準發布 | 兩者成熟度不能放在同一條時間軸上比較。

JEDEC 另稱較長通道可能容納更多記憶體 stacks。關鍵字是「可能」：能放更多，不代表系統一定會放更多，也不代表功耗、散熱、控制器與封裝尺寸允許。研究端要等產品設計與實測，不把規格上限當成出貨配置。

## 產品時鐘：既有 HBM4 已先跑

- Micron 2026-06-24 表示 HBM4 已對主力客戶平台進行大量出貨，並向多個終端客戶提供認證樣品；這是公司對自身產品進度的正式披露。
- 同一份 Micron 文件把 HBM4E 量產預期放在 2027 年，屬前瞻時程，不是已完成事項。
- SK hynix 2026-06-18 宣布送出 12 層 HBM4E 樣品，但未承諾精確量產日期；樣品也不等於 SPHBM4。
- 本輪沒有找到 Micron、SK hynix 或加速器平台商宣布採用 JESD330-4。這個「缺少具名採用」正是目前最重要的負證據。

因此不能用「SPHBM4 標準已發布」去覆蓋「傳統 HBM4 已在出貨」的現實。較合理的基準情境是：既有 HBM4 繼續服務近期平台，SPHBM4 從標準開始累積產品與認證證據，兩條時鐘分開追。

## 來源與證據邊界

- [JEDEC：JESD330-4 SPHBM4 標準，2026-07-13](https://www.jedec.org/news/pressreleases/new-jedec%C2%AE-sphbm4-standard-enables-hbm4-class-bandwidth-organic-substrates)
- [Micron：2026 財年第三季產品進度，2026-06-24](https://investors.micron.com/node/50671)
- [SK hynix：12 層 HBM4E 樣品，2026-06-18](https://news.skhynix.com/en/12-layer-hbm4e-sample-1/)

**已知：** SPHBM4 的介面結構、訊號數與有機基板方向已成為 JEDEC 標準；傳統 HBM4 已有記憶體供應商宣稱大量出貨。

**還不知道：** 第一個 SPHBM4 記憶體產品、加速器客戶、base-die 供應者、封裝商、基板材料、認證時程，以及相對傳統 HBM4 的成本、功耗、延遲、良率與可靠度。

**不可外推：** 「標準有機基板」不能直接等同 ABF 或 BT，也不能指定欣興、景碩、南電；「HBM4 級頻寬」是 JEDEC 的架構敘述，不是公開系統 benchmark。沒有價格、估值、共識與部位資料，本題不判斷市場是否已反映。

## 影響路由

本題只做**低信心族群 watch**，不列個股。方向是價值可能重新分配，而不是整條鏈一致受惠。

<!-- impact
group_id: pcb
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: SPHBM4 明確把介面導向標準有機基板，可能改變高階基板需求，但尚無材料規格、供應商、客戶或量產。
evidence_boundary: JEDEC 未指定 ABF或BT，也未列名3037、3189、8046；只構成族群搜尋觸發。
-->

<!-- impact
group_id: ipdesign
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: 新 interface base die 與高速序列化提高邏輯設計重要性，但尚無架構、IP供應商或商業模式揭露。
evidence_boundary: 不能把需要base die自動映射成任一台灣ASIC設計服務或高速介面公司訂單。
-->

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: 從矽基高密度路徑轉向有機基板可能改變組裝與測試流程，但尚無封裝商、良率或量產線證據。
evidence_boundary: 記憶體供應商具自有封裝能力，標準發布不等於外部OSAT承接；不列個股。
-->

## 下一個可證明／否定的節點

- **產品化**：任一記憶體廠公布 SPHBM4 樣品、容量、速度與量產時程；若未出現，維持標準觀察。
- **客戶採用**：任一加速器或系統廠具名採用 JESD330-4，並說明傳統 HBM4 與 SPHBM4 的使用場景；沒有具名客戶，不談滲透率。
- **工程裁決**：公開功耗、延遲、bit error rate、封裝面積、良率與可靠度。若序列化與長通道代價抵銷基板優勢，快速採用假說被否定。
- **台灣映射**：只有當正式文件列出基板種類、認證與供應者，才把族群 watch 升成個股 review；未列名之前，3037／3189／8046 不進 metadata。
