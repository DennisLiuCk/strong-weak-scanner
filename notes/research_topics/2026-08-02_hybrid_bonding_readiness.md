# Hybrid bonding 的真正門檻：PDK、200nm 試驗車與客戶設備使用仍不等於 HVM

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

## 新手先讀：這篇在講什麼

### 名詞小字典

- **Hybrid bonding**：不用凸塊把兩層晶片隔開，而是讓平坦介電層與細小銅接點直接貼合；間距可更小，但表面與對準誤差也更難容忍。
- **D2W／W2W**：D2W 是把挑好的單顆 die 接到晶圓，W2W 是整片晶圓對整片晶圓；兩者的良率分母、彈性與適用產品不同。
- **PDK**：把製程能做什麼整理成設計規則與驗證元件的工具包；探索型 PDK 能開始畫設計，不代表已能送量產 tape-out。
- **Overlay**：上下兩層接點的對準誤差；接點間距愈小，允許的偏差愈小。
- **Test vehicle**：為了量製程與電性而設計的測試結構，不是客戶最終商品。

### 三句話抓重點

- 2026 年的進展讓 hybrid bonding 同時有 pathfinding PDK 與 200nm W2W 試驗車，不再只是概念圖。
- Applied Materials 的 Kinex 又提供整合設備與多類客戶使用節點，但官方沒有公開具名量產產品、qualification、yield 或 throughput。
- 因此最有價值的判讀是「技術階梯向前」，不是「所有相關封測、設備與材料公司已開始賺錢」。

### 為什麼重要

Hybrid bonding 把接點做得更密，能讓邏輯、記憶體與 chiplet 之間更快、更省電；但它也把失敗風險集中到
表面平坦度、潔淨度、疊對、已知良品挑選與接合後檢查。若只看最小 pitch，很容易把研發紀錄誤當成
量產良率，也會把所有具備 CMP、清洗、檢查或封裝能力的公司都畫成同樣受惠。

### 接下來怎麼追

- 先問每份新資料位於 PDK、test vehicle、customer qualification、HVM 還是財務貢獻哪一級。
- 對 W2W 與 D2W 分開追 good-die yield、overlay distribution、throughput、返工能力與長期可靠度。
- 公司映射必須同時找到客戶端的具名流程與供應商端的料號／量產／收入，缺一邊就保留細線。

### 想一想

- 一個 200nm 試驗車的 overlay 很好，還缺哪些資料才能證明它能在客戶產品上長期大量生產？
- D2W 可以挑已知良品、W2W 可以整片處理，兩者的良率與成本應該用同一個分母比較嗎？
- 設備被多家客戶「使用」，和設備已完成 HVM qualification 並貢獻收入，中間還有哪些節點？

## 成熟度階梯：三個進展，三個不能跳過的邊界

| 節點 | 已證實 | 仍待驗證 |
|---|---|---|
| 設計入口 | NanoIC 提供 fine-pitch RDL 與 D2W pathfinding PDK | 完整 tape-out、實體 pilot silicon 與設計採用 |
| 製程試驗 | 200nm W2W test vehicle 與 sub-40nm overlay 結果 | 客戶產品 good-die yield、throughput、可靠度與成本 |
| 設備使用 | Kinex 整合流程與 inline metrology，Applied 稱多類客戶使用 | 具名客戶、qualification、量產出貨、設備收入與份額 |

這三列是相互補充，不是三張同義的「量產證明」。尤其 S2 的 100% dies 指的是 overlay vector 條件，
不能改寫成 100% electrical yield；S3 的 customer use 也不能改寫成客戶已大量出貨最終產品。

## 製程因果鏈

1. PDK 先把可製造的線寬、間距、材料與設計規則交給設計者。
2. 晶圓需要 CMP 與清洗把介電層、銅墊與 recess 控制在很窄的窗口。
3. Bonding tool 負責高精度對準；inline metrology 需要及早發現 overlay drift。
4. 試驗車確認連通、電阻與缺陷後，才進入具名客戶 qualification。
5. HVM 還要同時通過 good-die yield、throughput、可靠度與成本，最後才可能形成供應商財務貢獻。

任何新聞只要缺少第 4、5 步，就不應直接畫出高強度公司曝險線。

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
