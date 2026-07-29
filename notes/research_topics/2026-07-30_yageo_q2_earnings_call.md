# 國巨 2026Q2 法說：毛利率、AI 組合與被動元件需求更新

<!-- research_topic
topic_id: MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL
schema_version: 1
status: triaged
priority: p1
captured_at: 2026-07-30
source_published_at: 2026-07-29
last_reviewed_at: 2026-07-30
review_due: 2026-07-31
source_type: official_company
publisher_domain: yageogroup.com
canonical_url: https://yageogroup.com/SalesResources/ResourceLibrary/item/19061
source_chain_id: yageo-2q26-earnings-call-20260729
stock_ids: 2327
group_ids: passive
trigger_type: quarterly_results_and_earnings_call
evidence_role: candidate_source
route: formal_note_candidate
-->

<!-- transition
date: 2026-07-30
from: initial
to: inbox
reason: caught_by_official_event_calendar_backfill_after_priority_scan_omission
evidence: source_chain:yageo-2q26-earnings-call-20260729
-->
<!-- transition
date: 2026-07-30
from: inbox
to: triaged
reason: official_q2_deck_directly_hits_registered_h1_h2_proof_points
evidence: source_chain:yageo-2q26-earnings-call-20260729
-->

## 為何值得進佇列

國巨在 7 月 29 日法說發布的官方簡報顯示，2026Q2 營收 444.56 億元，季增 16.5%、
年增 35.7%；毛利率 38.5%，季增 0.4 個百分點、年增 2.9 個百分點。公司並揭露 AI
終端占營收 16%，鉭質電容銷售額季增 14.1%、年增 44%，MLCC 與電阻的成長幅度高於
整體。這些資料直接命中 `2327:H1`、`2327:H2` 與既有多空小作文預先登錄的 Q2
毛利率、產品組合、AI 占比和價格效果驗證點，因此應列為 P1 更新，而非等到原訂
8 月 15 日或 8 月 31 日才處理。

## 來源與證據邊界

- [國巨官方 2026Q2 法說頁](https://yageogroup.com/SalesResources/ResourceLibrary/item/19061)
- [國巨官方中文法說簡報](https://www.yageogroup.com/content/Resource%20Library/Financial/YAGEO%202Q26_Earnings%20Conference%20Presentation_CH.pdf)
- 簡報第 4 頁表示，毛利率改善主要受惠於價格調整與 AI 產品組合優化，但投入成本
  上升及標準品需求增加抵銷部分效益；這能更新獲利品質判讀，不能直接推成特定 MLCC
  料號已全面漲價。
- 簡報第 6 頁確認 AI 相關需求帶動多個產品類別，卻沒有揭露交期、稼動率、訂單覆蓋率、
  客戶合約或單一料號收入；因此尚不能把 `2327:H1` 的產業交期敘事升格為公司事實。
- 第 11 至 13 頁標示為「國巨合併（已檢閱）」摘要，但 14 頁法說簡報不等同含會計師
  核閱報告及附註的完整 2026Q2 財務報告；正式筆記的 `latest_quarterly_report`
  仍須取得完整一手文件並走同一 evidence pack 的離線獨立重算。
- 現有正式筆記仍以 2024 年報與 2026Q1 為基準；這次重展開時須納入已發布的 2025
  年報，不能只在舊筆記補兩行 Q2 數字。

## 影響路由

<!-- impact
group_id: passive
stock_ids: 2327
direction: mixed
hypothesis_refs: 2327:H1,2327:H2
note_action: update_required
action_due: 2026-07-31
rationale: Q2 毛利率、AI 營收占比、MLCC 與特殊品成長及價格效果已直接命中既有 H1/H2 與多空小作文的預先登錄勝負手
evidence_boundary: 官方簡報支持 Q2 結果與管理層產品組合說法，但未提供交期、稼動率、訂單覆蓋率、客戶合約或特定 MLCC 全面漲價證據
-->

## 下一個可證明／否定的節點

- 取得完整 2026Q2 核閱財務報告，核對會計師核閱範圍、附註、現金流與併購後資產負債
  變化，再建立 focused evidence pack。
- 複核法說問答或公司後續正式說明，確認價格調整的產品範圍、交期、稼動率與通路庫存；
  若沒有一手揭露，保留為未驗證，不把簡報用語擴寫成 MLCC 全面漲價。
- 更新 2327 多空小作文的量化背景與 Q2 證據；正式筆記完成獨立 reviewer 簽核後，再決定
  `H1`、`H2` 的生命週期是否轉移。
