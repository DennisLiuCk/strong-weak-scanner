# 背面供電跨過概念期：Intel 已進生產、台積電 A16 進入 2026 下半年量產時鐘

<!-- research_topic
topic_id: MI-2026-08-02-BACKSIDE-POWER-DELIVERY
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-04-16
last_reviewed_at: 2026-08-02
review_due: 2026-08-09
source_type: mixed
publisher: Taiwan Semiconductor Manufacturing Company
publisher_domain: investor.tsmc.com
canonical_url: https://investor.tsmc.com/static/annualReports/2025/english/index.html
source_chain_id: backside-power-manufacturing-milestones-20260802
stock_ids:
group_ids: semiequip,material,ipdesign
trigger_type: process_manufacturing_milestone
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C4
base_confidence: medium
confidence_basis: 台積電、Intel 與 imec 一手資料可交叉確認技術機制及製造里程碑，但晶圓代工廠節點定義不可直接相比，台灣設備材料商的具名步驟與財務貢獻仍未證實
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_source_backside_power_scan
evidence: source_chain:backside-power-manufacturing-milestones-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_foundry_manufacturing_milestones_from_supplier_revenue_exposure
evidence: sources:S1,S2,S3
-->

<!-- research_source
source_id: S1
role: company_filing
source_kind: document
publisher: Taiwan Semiconductor Manufacturing Company
title: TSMC 2025 Annual Report
published_at: 2026-04-16
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investor.tsmc.com/static/annualReports/2025/english/index.html
locator: Business Overview；N2、N2P、A16 roadmap 段落，A16 Super Power Rail 與 2026 下半年量產時程
limitation: 公司自述製程路線圖；沒有客戶名稱、量產晶圓數、良率或個別供應商內容
independence_group: tsmc
-->

<!-- research_source
source_id: S2
role: competitor_primary
source_kind: document
publisher: Intel Foundry
title: Intel Foundry Details Process Milestones and Future Innovation at VLSI Symposium
published_at: 2026-06-16
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.intel.com/intel-foundry/intel-foundry-details-process-milestones-future-innovation-at-vlsi-symposium
locator: Intel 18A entered production in 2025；Intel 18A-P now in risk production 段落
limitation: Intel 的 production／risk production 定義、產品組合與節點基準不能直接套用到台積電 A16
independence_group: intel
-->

<!-- research_source
source_id: S3
role: other_primary
source_kind: document
publisher: imec
title: Backside power delivery
published_at: 2022-11-25
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.imec-int.com/en/articles/how-power-chips-backside
locator: Promises of a backside power delivery network；Buried power rail and nano-through-silicon-vias；overall process flow 段落
limitation: 研究機構的技術機制與試驗流程不是晶圓廠量產良率、客戶採用或設備商訂單證據
independence_group: imec
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: living_index
publisher: Taiwan Semiconductor Manufacturing Company
title: TSMC A16 Technology
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_A16
locator: 2026-08-02 查得 A16 integrates nanosheet transistors with backside power rail，並標示 2H26 production-ready
limitation: 產品技術頁會持續更新；頁面本身不證明實際量產、客戶採用、良率或供應商收入
independence_group: tsmc
-->

<!-- research_source
source_id: S5
role: competitor_primary
source_kind: living_index
publisher: Intel Foundry
title: Intel Foundry Newsroom
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.intel.com/intel-foundry
locator: 2026-08-02 查得 2026-06-16 Intel 18A-P risk production 更新及後續 Foundry 公告入口
limitation: 新聞索引只用來偵測新文件；任何新主張仍須回到具體公告或申報文件
independence_group: intel
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: 台積電 2025 年報把 A16 定位為採用 Super Power Rail 的 N2 家族延伸，並把 A16 與 N2P 的量產排在 2026 下半年
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-04-16
basis: S1 的 A16 roadmap 段落直接列示技術定位與 volume production 時程
boundary: 這是公司量產計畫，不等於截至 2026-08-02 已完成量產、客戶採用、良率或收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: Intel 表示 18A 已於 2025 年進入生產，18A-P 則在 2026-06-16 進入風險生產
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-06-16
basis: S2 標題與製程里程碑段落直接區分 18A production 與 18A-P risk production
boundary: Intel 的里程碑不能改寫成外部晶圓代工客戶已大量採用，也不能與台積電 A16 的量產定義直接排名
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: imec 將背面供電的核心機制描述為把供電網路與前側訊號網路分離，並把埋置電源軌、晶圓薄化與 nano-TSV 列為關鍵製程步驟
supporting_source_ids: S3
contrary_source_ids:
as_of: 2022-11-25
basis: S3 的 BSPDN 原理、BPR／nTSV 與 overall process flow 段落直接列出機制及步驟
boundary: 技術必要步驟不等於每一家晶圓廠採用完全相同流程、工具、材料或供應商
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: active
claim: 背面供電已由研究概念跨入具名製程的生產與量產時鐘，但目前最可用的研究單位仍是各晶圓廠自己的成熟度階梯，而不是跨廠效能排名或台灣供應鏈受惠名單
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-08-02
basis: S3 建立技術機制，S1 與 S2 分別提供 A16、18A／18A-P 的製造里程碑；三份來源支持方向但沒有共同可比的節點定義與供應商財務資料
boundary: 不推估市占、量產晶圓數、設備內容量、供應商份額或獲利，也不把 Intel 的 production 等同台積電的 volume production
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: 台灣半導體設備、材料或矽智財公司已因 A16／PowerVia 取得可辨識訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有一手來源只證實晶圓廠里程碑與一般製程步驟，未列出台灣供應商、料號、產線或財務貢獻
boundary: 不以「晶圓薄化、CMP、蝕刻、量測可能需要更多」直接建立公司受惠關係
verification_needed: 需晶圓廠與供應商文件雙向核對具名製程步驟、量產資格、出貨與可辨識財務貢獻
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C4
metric: A16、18A 與 18A-P 的實際量產、客戶產品與製造成熟度里程碑
source_ids: S1,S2
watch_source_ids: S4,S5
frequency: weekly
frequency_detail: 每週檢查晶圓廠技術頁、新聞稿與法說；重大製程更新即重審
next_check: 2026-08-09
trigger: 台積電確認 A16 實際進入量產或具名客戶產品，或 Intel 更新 18A／18A-P 出貨與外部客戶狀態
invalidation: A16 時程延後、18A 量產問題或客戶改採不含背面供電的替代節點，均下修近期商業成熟度
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C3,C5
metric: BPR、晶圓薄化、bonding、nTSV、背面金屬與量測步驟的具名供應商資格及財務轉換
source_ids: S3
watch_source_ids: S4,S5
frequency: event_driven
frequency_detail: 晶圓廠或供應商發布具名 A16／18A 製程工具、材料、資格或量產結果時檢查
next_check: 2026-08-16
trigger: 至少一組晶圓廠與供應商文件可雙向核對同一製程步驟、量產狀態與收入邊界
invalidation: 若製程整合由晶圓廠自有方案完成、供應商無具名資格或只有研發合作，台灣公司映射維持未證
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **背面供電（BSPDN）**：把原本和訊號線擠在晶片正面的電源網路移到晶圓背面，讓電力用較直接的路徑抵達電晶體。
- **Super Power Rail／PowerVia**：分別是台積電與 Intel 對背面供電實作的名稱；名稱不同，不代表可以只看一個效能數字直接判輸贏。
- **埋置電源軌（BPR）**：埋在電晶體下方的金屬電源軌，配合背面導通結構把電力送到元件。
- **nano-TSV**：從薄化後的晶圓背面連到前側元件附近的微小矽穿孔，是 imec 描述的一種實作路徑。
- **風險生產**：製程已進入早期製造驗證，但仍不是成熟量產、客戶大量出貨或穩定良率的同義詞。

### 三句話抓重點

- 台積電已把 A16 背面供電放進 2026 下半年量產時鐘；Intel 則表示 18A 已生產、18A-P 進入風險生產。
- 兩家公司的節點名稱、基準與成熟度定義不同，能比較的是「各自走到哪一階」，不是把公司效能數字排成一張排行榜。
- 對台灣供應鏈而言，真正缺的仍是具名製程步驟、量產資格、出貨與財務貢獻；技術上需要某道工序，不等於任一公司已拿到訂單。

### 為什麼重要

背面供電會改變電源與訊號的佈線方式，也新增或提高晶圓薄化、接合、背面對準、nTSV、
金屬與製程控制的整合難度。它因此可能重畫先進邏輯的製程鏈，但也最容易產生「看見一個
必要步驟，就自動配對一家受惠公司」的錯誤。先建立成熟度與證據邊界，才能追蹤真正的商業轉換。

### 接下來怎麼追

- 先追台積電是否從「2026 下半年規劃」更新為 A16 已量產，並說明客戶產品與爬坡範圍。
- 再追設備／材料商是否用具名 A16、18A 或背面供電步驟揭露 qualification、出貨與財務影響。
- 每次看到供應商新聞，要求晶圓廠端與供應商端能對上同一製程、同一成熟度與同一期間。

### 想一想

- 「需要晶圓薄化」和「某家薄化設備商會增加獲利」之間，還缺哪些資格、份額與價格證據？
- 若 A16 如期量產，但沒有任何台灣設備商揭露具名曝險，應該上調技術主題信心，還是公司受惠信心？

## 已證實的製造成熟度

台積電在 2025 年報中把 A16 描述為 N2 家族延伸，結合 nanosheet 與 Super Power Rail，
並把 A16／N2P volume production 排在 2026 下半年。Intel 在 2026 VLSI 更新中則表示，
18A 已於 2025 年進入 production，18A-P 在 2026 年 6 月進入 risk production。這些都是
比研究試驗更靠近製造的里程碑，但名詞由公司自行定義，不能把「production」、「risk
production」與「volume production 計畫」當成同一個量尺。

## 技術鏈怎麼連起來

imec 的流程說明提供了一張不綁特定供應商的因果圖：背面供電先把供電與前側訊號佈線
分離，再透過埋置電源軌與 nano-TSV 接近元件；為了從背面加工，又需要載體接合、極薄
晶圓、背面對準、蝕刻、填金屬與後續檢查。這張圖能用來問「哪一道能力需要被驗證」，
不能直接回答「哪一家公司有多少訂單」。

## 來源與證據邊界

- [TSMC 2025 Annual Report](https://investor.tsmc.com/static/annualReports/2025/english/index.html)（A16 roadmap 與量產時程）。
- [Intel Foundry 2026 VLSI update](https://newsroom.intel.com/intel-foundry/intel-foundry-details-process-milestones-future-innovation-at-vlsi-symposium)（18A 與 18A-P 製造里程碑）。
- [imec backside power delivery](https://www.imec-int.com/en/articles/how-power-chips-backside)（BPR、晶圓薄化、nTSV 與整合流程）。

本輪沒有使用跨公司效能數字做比較，也沒有一致預期、估值或即時部位資料，因此不判斷
題材是否已反映。台積電是觀察層公司，不因其代號出現在技術路線圖就把 universe 內設備、
材料或 IP 公司自動連線。

## 影響路由

<!-- impact
group_id: semiequip
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-16
rationale: 晶圓薄化、接合、背面對準、蝕刻、金屬與製程控制形成設備研究路由，但仍缺具名供應商資格與財務證據
evidence_boundary: 技術流程的必要性不證明任一 universe 公司已供貨、取得份額或增加獲利
-->

<!-- impact
group_id: material
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-16
rationale: BPR、nTSV、蝕刻停止層與背面金屬涉及材料整合問題，值得追蹤晶圓廠與材料商的具名 qualification
evidence_boundary: imec 研究流程不是台積電或 Intel 的完整量產配方，也沒有列名台灣材料供應商
-->

<!-- impact
group_id: ipdesign
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-16
rationale: 背面供電需要設計技術共同最佳化與新 PDK，但目前沒有 universe 公司具名 IP、客戶採用或授權收入證據
evidence_boundary: PDK 與 DTCO 需求不等於本地 IP／ASIC 設計服務商已有可辨識財務曝險
-->

## 下一個可證明／否定的節點

- 台積電正式宣布 A16 進入量產，並提供至少一個客戶產品、爬坡或製造範圍。
- Intel 將 18A／18A-P 的製造節點連到外部 foundry 客戶實際產品，而非只停在自有產品與風險生產。
- 設備或材料商以正式文件揭露同一背面供電步驟的 qualification、出貨與財務貢獻，且可由晶圓廠端交叉核對。
- 若只有製程概念、效能目標或合作名單而沒有量產與財務足跡，技術主題可維持，個股映射不得升級。
