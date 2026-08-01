# 推論算力組合擴張：ASIC／CPU 與 GPU 並行，Advantest 上修 tester TAM 約 19%

<!-- research_topic
topic_id: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM
schema_version: 1
status: triaged
priority: p1
captured_at: 2026-08-01
source_published_at: 2026-07-29
last_reviewed_at: 2026-08-01
review_due: 2026-08-08
source_type: mixed
publisher_domain: advantest.com
canonical_url: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_slide.pdf
source_chain_id: advantest-inference-tester-tam-20260729
stock_ids: 2449,3035,3264,3443,3661,6223,6257,6510,6515,6533
group_ids: ipdesign,packtest,semiequip
trigger_type: demand_validation_and_market_forecast_revision
evidence_role: candidate_source
route: market_issue_watch
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
evidence: source_chain:advantest-inference-tester-tam-20260729
-->

## 為何值得進佇列

7 月底出現了比「CSP 會做自研晶片」更可驗證的組合證據：Amazon 的 chips business 已
超過 250 億美元年化營收規模，Microsoft 的 Maia 200 正擴大使用，而 Advantest 同時把
CY2026 tester TAM 中值上修約 19%。最重要的判讀不是「ASIC 取代 GPU」，而是推論工作負載
讓 ASIC、CPU、DRAM 與 GPU 並行，晶片數量、複雜度與 test insertion 共同抬高測試需求。
這能驗證全球需求機制，仍不能自動驗證任何台灣設計服務、封測或測試介面公司的訂單。

## 三組相互校驗的證據

| 來源 | 已驗證 | 必須保留的邊界 |
|---|---|---|
| Advantest 2026-07-29 | CY2026 SoC＋memory tester TAM 上修至 130–145 億美元：SoC 105–115 億、memory 25–30 億；較 4 月預估中值約增 19%。公司歸因於 AI 晶片產量、複雜度，特別是推論用 ASIC、CPU、DRAM | 這是 Advantest 的市場估計；Q&A 明說無法拆分 GPU／CPU／ASIC 各自貢獻，GPU 目前仍是最大市場 |
| Amazon 2026-07-30 | AWS chips business 年化營收規模超過 250 億美元且年增三位數；Trainium 取得 Anthropic、OpenAI 多年、多 GW 承諾 | 250 億美元包含 Graviton、Trainium、Nitro，不能全算 Trainium；容量承諾不等於晶片採購金額，Amazon 也同時大量採用 NVIDIA |
| Microsoft 2026-07-29 | Maia 200 持續擴大，已支援 OpenAI 與 MAI models；公司稱相對其 fleet 最新硬體 performance／dollar 高 30%，MAI models 的 performance／watt 高 40% | 比較基準是 Microsoft 自有 fleet，並非點名擊敗特定 GPU；同一段明說自研晶片與 NVIDIA、AMD 並行 |

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

## 下一個可證明／否定的節點

- Advantest 下一次展望是否維持 130–145 億美元 CY2026 tester TAM，並披露實際訂單／出貨而非只有估計。
- Amazon 是否把多年、多 GW 承諾轉成 Trainium 實際部署；Microsoft 是否持續擴大 Maia 使用且仍與 GPU 並行。
- 矽智財公司是否以一手文件揭露 NRE、tape-out、量產與收入；未點名客戶時不得自行補上 AWS／Meta／Microsoft。
- 封測與測試介面公司是否同時出現稼動率、ASP、營收與毛利改善；若只有擴產或市場 TAM 上修，證據不足。
- 若 Advantest 下修 TAM、推論專案延期，或公司級測試需求與毛利沒有跟上，應下修此題；不得只用股價反應續留。
