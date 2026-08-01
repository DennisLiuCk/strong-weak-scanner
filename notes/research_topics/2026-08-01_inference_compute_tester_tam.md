# 推論算力組合擴張：ASIC／CPU 與 GPU 並行，Advantest 上修 tester TAM 約 19%

<!-- research_topic
topic_id: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-01
source_published_at: 2026-07-29
last_reviewed_at: 2026-08-01
review_due: 2026-08-08
source_type: mixed
publisher: Advantest
publisher_domain: advantest.com
canonical_url: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_slide.pdf
source_chain_id: advantest-inference-tester-tam-20260729
stock_ids: 2449,3035,3264,3443,3661,6223,6257,6510,6515,6533
group_ids: ipdesign,packtest,semiequip
trigger_type: demand_validation_and_market_forecast_revision
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C2
base_confidence: medium
confidence_basis: Advantest、Amazon 與 Microsoft 的一手揭露支持需求機制，但三組數字不可橫向比較，台灣公司訂單映射仍待驗證
cross_company_numbers: true
schema_migrated_at: 2026-08-02
-->

<!-- transition
date: 2026-08-01
from: initial
to: inbox
reason: primary_source_hyperscaler_and_test_equipment_scan
evidence: source_chain:advantest-inference-tester-tam-20260729
-->
<!-- transition
date: 2026-08-01
from: inbox
to: triaged
reason: validated_global_demand_but_withheld_taiwan_supplier_attribution
evidence: sources:S1,S2,S3,S4,S5
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **推論算力**：AI 模型回答問題時使用的運算資源；它可以由 GPU、自研 ASIC 與 CPU 等不同晶片共同提供。
- **Tester TAM**：測試設備商估計某一期間整體測試機市場的金額，不等於任何一家台灣供應商已取得的訂單。
- **Test insertion**：晶片製造過程中安排測試的節點與次數；晶片更複雜、測試時間更長，可能提高設備與介面的需求。
- **年化營收規模**：把目前一季或當下速度換算成一年的概略規模，不等於已完成的全年會計收入。

### 三句話抓重點

- Advantest 上修 2026 年 tester TAM，並把推論 ASIC、CPU 與 DRAM 的產量及複雜度列為原因之一。
- Amazon 與 Microsoft 的官方揭露顯示自研晶片持續擴大，但它們仍與 NVIDIA、AMD 等通用加速器並行，而不是立即全面替代。
- 這些資料支持測試需求擴張的研究方向，卻沒有證明任一台灣設計、封測或測試介面公司已取得新增訂單。

### 為什麼重要

市場容易把「自研 ASIC 成長」解讀成 GPU 單向流失，或把全球 tester TAM 上修直接分配給台灣個股。這篇的重要性在於把運算架構、測試需求與公司獲利拆成不同證據層級：晶片種類與複雜度增加只是需求機制，仍要等公司專案、稼動率、售價、收入與毛利才能證明經濟利益落地。

### 接下來怎麼追

- 每季追 Advantest 是否維持 130–145 億美元的 2026 年 tester TAM，並出現實際訂單或出貨證據。
- 追 Amazon Trainium 與 Microsoft Maia 的實際部署，同時確認自研晶片是否仍與 GPU 並行。
- 追台灣公司法說與財報是否同時揭露 NRE、量產、稼動率、ASP、收入及毛利，而不是只談產業 TAM。

### 想一想

- 如果 ASIC 增加但只是取代同等數量的 GPU，整體測試時間與測試設備需求一定會增加嗎？
- Advantest 的全球市場估計要經過哪些公司級證據，才能合理連到某一家台灣供應商的獲利？
- Amazon 的年化營收、Microsoft 的效能比與 Advantest 的市場預估，為什麼不能排成同一張高低榜？

## 主張與證據帳本

`證實` 只表示指定來源直接支持精確措辭；發行人的市場估計、年化數字與效能比較仍受各自定義限制，不代表台灣供應商訂單已被證實。

<!-- research_source
source_id: S1
role: market_estimate
publisher: Advantest
title: FY2026 Q1 Business Briefing
published_at: 2026-07-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_slide.pdf
locator: p.12 tester market outlook
limitation: tester TAM 是 Advantest 的市場估計，沒有拆分 GPU、CPU、ASIC 貢獻或台灣供應商份額
-->

<!-- research_source
source_id: S2
role: company_release
publisher: Amazon
title: Amazon 2026 Q2 Results
published_at: 2026-07-30
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx
locator: AWS chips business 與 Trainium 客戶承諾段落
limitation: chips business 包含 Graviton、Trainium 與 Nitro，年化規模不是 Trainium 單一產品收入或採購金額
-->

<!-- research_source
source_id: S3
role: management_commentary
publisher: Microsoft
title: Microsoft FY2026 Q4 Earnings Call
published_at: 2026-07-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4
locator: Maia 200、OpenAI／MAI models 與異質運算段落
limitation: 效能比較以 Microsoft 自有 fleet 為基準，沒有提供晶片數量、外部售價或台灣供應商映射
-->

<!-- research_source
source_id: S4
role: management_commentary
publisher: Advantest
title: FY2026 Q1 Business Briefing Notes
published_at: 2026-07-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_note.pdf
locator: p.12 tester market trends、130–145 億美元區間與推論 ASIC／CPU／DRAM 需求段落
limitation: 管理層簡報附註仍是 Advantest 的市場預估，沒有拆出各運算架構或台灣供應商的實際貢獻
-->

<!-- research_source
source_id: S5
role: management_commentary
publisher: Advantest
title: Q1 FY2026 Financial Briefing Q&A Summary
published_at: 2026-07-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_QA.pdf
locator: pp.1–2 GPU、custom ASIC 與 CPU tester demand 問答
limitation: 管理層明示難以切分 GPU、CPU 與 custom ASIC 對 TAM 增量的相對貢獻，前瞻說法也不是已實現收入
-->

<!-- research_source
source_id: S6
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 台灣設計服務、封測與測試介面公司季報、法說及重大訊息查找入口
limitation: 雲端自研晶片與 tester TAM 只構成查找 trigger；入口本身不支持任何台灣公司訂單
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: Advantest 將 CY2026 SoC 與 memory tester TAM 更新為 130–145 億美元，並把推論 ASIC、CPU 與 DRAM 的產量及複雜度列為需求因素
supporting_source_ids: S1,S4
contrary_source_ids:
as_of: 2026-08-01
basis: S1 p.12 可直接定位市場預估區間與需求說明
boundary: 這是設備商的市場估計，不是已實現市場收入，也不證明任何台灣公司訂單、市占或獲利
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: inference
status: active
claim: 推論工作負載正擴大 ASIC、CPU、DRAM 與 GPU 並行的異質算力組合，晶片數量與複雜度可能共同增加測試需求
supporting_source_ids: S1,S2,S3,S4,S5
contrary_source_ids:
as_of: 2026-08-01
basis: S1 的 tester TAM 驅動因素與 S2、S3 的自研晶片擴大揭露共同支持此基準情境
boundary: 這是跨來源研究推論，不代表各架構的測試貢獻相同，也不自動成立於每一家台灣同族群公司
verification_needed: 後續 tester 訂單出貨、實際測試時間與台灣公司量產收入及毛利
resolution:
-->

<!-- research_claim
claim_id: C3
label: unverified
status: active
claim: 2449、3035、3264、3443、3661、6223、6257、6510、6515、6533 已因這波推論算力擴張取得可量化新增訂單與獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-01
basis: 三份來源都沒有點名上述台灣公司，也沒有提供其專案份額、收入、稼動率、ASP 或毛利
boundary: 只能作為公司級搜尋與複核清單，不得寫入正式筆記事實或當成既成受惠
verification_needed: 台灣公司正式法說、季報或公告須揭露專案階段並出現可辨識收入、毛利與現金流證據
resolution:
-->

## 為何值得進佇列

7 月底出現了比「CSP 會做自研晶片」更可驗證的組合證據：Amazon 的 chips business 已
超過 250 億美元年化營收規模，Microsoft 的 Maia 200 正擴大使用，而 Advantest 同時把
CY2026 tester TAM 中值上修約 19%。最重要的判讀不是「ASIC 取代 GPU」，而是推論工作負載
讓 ASIC、CPU、DRAM 與 GPU 並行，晶片數量、複雜度與 test insertion 共同抬高測試需求。
這能驗證全球需求機制，仍不能自動驗證任何台灣設計服務、封測或測試介面公司的訂單。

## 跨公司數字與可比性

### 三組相互校驗的證據

| 來源 | 已驗證 | 必須保留的邊界 |
|---|---|---|
| Advantest 2026-07-29 | CY2026 SoC＋memory tester TAM 上修至 130–145 億美元：SoC 105–115 億、memory 25–30 億；較 4 月預估中值約增 19%。公司歸因於 AI 晶片產量、複雜度，特別是推論用 ASIC、CPU、DRAM | 這是 Advantest 的市場估計；Q&A 明說無法拆分 GPU／CPU／ASIC 各自貢獻，GPU 目前仍是最大市場 |
| Amazon 2026-07-30 | AWS chips business 年化營收規模超過 250 億美元且年增三位數；Trainium 取得 Anthropic、OpenAI 多年、多 GW 承諾 | 250 億美元包含 Graviton、Trainium、Nitro，不能全算 Trainium；容量承諾不等於晶片採購金額，Amazon 也同時大量採用 NVIDIA |
| Microsoft 2026-07-29 | Maia 200 持續擴大，已支援 OpenAI 與 MAI models；公司稱相對其 fleet 最新硬體 performance／dollar 高 30%，MAI models 的 performance／watt 高 40% | 比較基準是 Microsoft 自有 fleet，並非點名擊敗特定 GPU；同一段明說自研晶片與 NVIDIA、AMD 並行 |

三個 headline 分別是設備市場預估、晶片業務年化收入規模與相對效能比，期間、單位與定義都不同。下列帳本把它們歸在同一個研究問題下，但明確判定為 `not_comparable`，只用來交叉觀察推論算力需求，不能橫向排名或加總。對應比較帳本：`M1`。

<!-- metric_comparison
comparison_id: M1
comparison_kind: heterogeneous_evidence
observation_id: M1-O1
claim_id: C2
entity: Advantest
metric: SoC and memory tester TAM forecast
value_kind: range
reported_value: 13.0..14.5
period_start: 2026-07-29
period_end: 2026-07-29
period_basis: management_forecast_observed_on_2026-07-29_for_CY2026_horizon
unit: USD_billion
definition_key: soc_memory_tester_tam_forecast
definition: 2026-07-29 發布、預測涵蓋 CY2026 的 SoC 與 memory tester 整體可服務市場區間
evidence_ids: S1,S4,S5
comparability: not_comparable
comparability_reason: 這是設備市場全年預估，不是雲端晶片收入或單一晶片效能指標
-->

<!-- metric_comparison
comparison_id: M1
comparison_kind: heterogeneous_evidence
observation_id: M1-O2
claim_id: C2
entity: Amazon
metric: AWS chips business annualized revenue run rate
value_kind: lower_bound
reported_value: 25
period_start: 2026-06-30
period_end: 2026-06-30
period_basis: annualized_run_rate_as_of_quarter_end
unit: USD_billion_per_year
definition_key: aws_chips_business_annualized_revenue_run_rate
definition: Graviton、Trainium 與 Nitro 合計 chips business 的年化營收規模
evidence_ids: S2
comparability: not_comparable
comparability_reason: 這是多項 AWS 晶片業務的年化收入速度，不是 tester TAM、採購金額或 Trainium 單項收入
-->

<!-- metric_comparison
comparison_id: M1
comparison_kind: heterogeneous_evidence
observation_id: M1-O3
claim_id: C2
entity: Microsoft
metric: Maia 200 performance per dollar improvement
value_kind: point
reported_value: 30
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: fiscal_quarter_management_comparison
unit: percent
definition_key: maia_200_performance_per_dollar_vs_latest_fleet_hardware
definition: Maia 200 相對 Microsoft fleet 最新硬體的 performance per dollar 改善幅度
evidence_ids: S3
comparability: not_comparable
comparability_reason: 這是公司自有硬體基準的相對效能比，不是收入、TAM、晶片出貨量或跨公司 benchmark
-->

## 來源與證據邊界

- [Advantest FY2026 Q1 簡報](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_slide.pdf)（p.12，2026-07-29）。
- [Advantest 簡報附註](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_note.pdf)（tester market 段落，2026-07-29）。
- [Advantest Q&A](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_QA.pdf)（pp.1–2，2026-07-29）。
- [Amazon 2026Q2 結果](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx)（2026-07-30）。
- [Microsoft FY2026Q4 法說逐字稿](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)（2026-07-29）。

這批來源沒有點名 3035、3443、3661、6533 的新 NRE／tape-out／量產案，也沒有點名
2449、3264、6257 或 6223、6510、6515 的訂單、稼動率、ASP 或市占。Advantest 的 TAM
上修只能作為測試鏈需求的外部 trigger。由於本輪沒有一致預期、估值與即時持倉資料，
不宣稱這些公司「尚未反映」或 tester TAM 上修必然造成倍數擴張。

## 傳導與投資判讀

```text
推論工作負載擴張
  → ASIC／CPU／DRAM／GPU 異質組合增加
  → 更多設計、test insertion 與更長測試時間
  → tester TAM 上升
  → 只有在公司取得專案且轉成稼動率、ASP、收入與毛利時，才構成台股公司證據
```

- **主要驅動 KPI**：量產 silicon 數量、測試 insertion／時間、公司級 NRE 與量產認列。
- **次要 KPI**：封測稼動率、tester／probe card／socket 產能、ASP 與毛利。
- **常見假訊號**：把 hyperscaler capex、AWS chips run rate 或 Advantest TAM 全數映射到單一台灣供應商。
- **最關鍵分歧**：異質運算是否增加整體測試內容量，而非單純在 GPU 與 ASIC 之間搬移同一筆支出。

## 影響路由

<!-- impact
group_id: ipdesign
stock_ids: 3035,3443,3661,6533
direction: mixed
hypothesis_refs: 3035:H1,3035:H2,3443:H1,3443:H2,3661:H1,3661:H2,6533:H1
note_action: review_due
action_due: 2026-08-08
rationale: 既有 H# 分別主張雲端 AI ASIC、CSP 訂單、Trainium 與 MTIA，應以公司文件核對 NRE、tape-out、量產與收入節點
evidence_boundary: Amazon、Microsoft 與 Advantest 均未指認這四家公司，也未證實專案份額、收入或毛利
-->

<!-- impact
group_id: packtest
stock_ids: 2449,3264,6257
direction: mixed
hypothesis_refs: 2449:H1,2449:H2,3264:H1,6257:H1,6257:H2
note_action: review_due
action_due: 2026-08-08
rationale: Advantest 的產量與複雜度論點直接觸發 AI 測試擴產、客戶案與價格假說的公司級複核
evidence_boundary: tester TAM 是設備市場估計，不等於台灣測試廠訂單、稼動率、報價或客戶歸屬
-->

<!-- impact
group_id: semiequip
stock_ids: 6223,6510,6515
direction: mixed
hypothesis_refs: 6223:H1,6223:H2,6510:H1,6510:H2,6515:H1,6515:H2
note_action: review_due
action_due: 2026-08-08
rationale: 更多 test insertion 與複雜度可能增加 probe card、load board 與 socket 內容，但需公司級接單、產能與毛利證據
evidence_boundary: Advantest 沒有點名本 universe 測試介面廠，不能由全球 TAM 上修推導個股市占或獲利
-->

## 持續驗證清單

`review_due` 維持原訂 2026-08-08，等於所有 active monitoring item 中最早的 `next_check`；本次 schema 搬遷不前移 evidence clock。

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2
metric: Advantest tester TAM、訂單與實際出貨
source_ids: S1,S4,S5
watch_source_ids: S6
frequency: event_driven
next_check: 2026-08-08
trigger: Advantest 更新 2026 tester TAM，或揭露 AI 相關 tester 的訂單與實際出貨
invalidation: TAM 區間下修、推論專案延後，或估計未轉成設備訂單與出貨
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C2,C3
metric: 自研晶片部署與台灣供應商可辨識財務貢獻
source_ids: S2,S3,S6
watch_source_ids: S6
frequency: quarterly
next_check: 2026-08-15
trigger: Amazon 或 Microsoft 揭露實際部署，且台灣公司文件出現 NRE、量產、稼動率、收入與毛利證據
invalidation: 自研晶片時程延後，或台灣公司只有題材與擴產而沒有量產及獲利交叉證據
-->

## 下一個可證明／否定的節點

- Advantest 下一次展望是否維持 130–145 億美元 CY2026 tester TAM，並披露實際訂單／出貨而非只有估計。
- Amazon 是否把多年、多 GW 承諾轉成 Trainium 實際部署；Microsoft 是否持續擴大 Maia 使用且仍與 GPU 並行。
- 矽智財公司是否以一手文件揭露 NRE、tape-out、量產與收入；未點名客戶時不得自行補上 AWS／Meta／Microsoft。
- 封測與測試介面公司是否同時出現稼動率、ASP、營收與毛利改善；若只有擴產或市場 TAM 上修，證據不足。
- 若 Advantest 下修 TAM、推論專案延期，或公司級測試需求與毛利沒有跟上，應下修此題；不得只用股價反應續留。
