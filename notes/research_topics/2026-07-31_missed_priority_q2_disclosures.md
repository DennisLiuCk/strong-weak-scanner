# 六檔漏掃優先研究：Q2 法說的實績、反證與待補文件

<!-- research_topic
topic_id: MI-2026-07-31-MISSED-PRIORITY-Q2
schema_version: 1
status: triaged
priority: p1
captured_at: 2026-07-31
source_published_at: 2026-07-07
last_reviewed_at: 2026-07-31
review_due: 2026-08-05
source_type: mixed
publisher_domain: mopsov.twse.com.tw
canonical_url: https://mopsov.twse.com.tw/server-java/FileDownLoad?step=9&filePath=%2Fhome%2Fhtml%2Fnas%2FSTR%2F&fileName=826120260729M002.pdf&functionName=t100sb02_1
source_chain_id: missed-priority-q2-official-scan-20260731
stock_ids: 2308,2337,3264,6239,6488,8261
group_ids: power,powersupply,memory,packtest,material
trigger_type: quarterly_results_and_company_events
evidence_role: candidate_source
route: formal_note_candidate
-->

<!-- transition
date: 2026-07-31
from: initial
to: inbox
reason: user_requested_missed_priority_research
evidence: source_chain:missed-priority-q2-official-scan-20260731
-->
<!-- transition
date: 2026-07-31
from: inbox
to: triaged
reason: separated_verified_q2_results_from_unproven_market_claims_and_pending_documents
evidence: source_chain:missed-priority-q2-official-scan-20260731
-->

## 為何值得進佇列

這六檔不是因為股價強弱而升為 P1，而是 7 月 24～30 日已有公司 Q2 法說、核閱數或重大
事件，且新資料足以改寫原研究的證據強弱。最重要的共通點不是「營收都變好」，而是 headline
與本業品質出現明顯分歧：富鼎 EPS 年增主要來自業外由負轉正；台達電獲利仍由本業主導，
但毛利率、營益率季減且兩個事業部虧損；欣銓營收與量產里程碑成立，卻同時出現負自由現金流
與負債上升；環球晶 6 月巨額虧損則是 Siltronic 評價噪音，不能誤判成本業崩壞。旺宏與力成
的本業改善較乾淨，但市場流傳的「逐月議價／長供」與「已簽 HBM2 訂單」仍沒有一手證據。

## 來源與證據邊界

### 2308 台達電

- [2026Q2 官方法說簡報](https://filecenter.deltaww.com/ir/download/calendar/2Q26_Analyst%20Meeting.pdf)
  pp.4–10 顯示 Q2 營收 1,832 億元、毛利率 35.6%、營益率 16.7%、歸母淨利
  251.36 億元、EPS 9.68 元。營業利益年增約 119.02 億元，業外年增 35.27 億元，
  因此獲利成長以本業為主，但不能忽略業外約占稅前增量 23%。
- 同份簡報 p.6 顯示電源及零組件、基礎設施量利成長，交通與自動化仍為部門虧損；
  p.4–5 顯示毛利率、營益率分別季減 1.4、1.1 個百分點。這些數字不能直接映射為 AI、
  液冷或 HVDC 收入，公司也沒有提供「Q4 營收高於 Q3」的正式財測。

### 2337 旺宏

- [公司季度法說入口](https://www.mxic.com.tw/zh-tw/about/investor-relations/Pages/quarterly-results.aspx/financial-reports.aspx)與
  [2026Q2 官方法說簡報](https://mopsov.twse.com.tw/nas/STR/233720260728M001.pdf) pp.5–6
  顯示 Q2 營收 191.25 億元、毛利率 64.4%、營益率 46.9%、EPS 3.91 元；H1 EPS
  4.82 元。Q2 業外只占稅前約 2.5%，headline 與本業方向一致。
- 簡報 pp.14、17 支持高容量 NOR 與 SLC／eMMC 缺貨、需求及當期價格方向；p.17 另顯示
  eMMC 季增 317%／年增 5,334%。它沒有證明「逐月議價」、產能全滿、長期供應合約或
  下半年高毛利保證，64.4% 毛利率也未拆價格、組合、稼動率與存貨評價橋接。

### 3264 欣銓

- [2026Q2 官方法說簡報](https://www.ardentec.com/UserFiles/2026Q2%E6%B3%95%E8%AA%AA%E6%9C%83%E7%B0%A1%E5%A0%B1%20%E4%B8%AD%E6%96%87_20260724%282%29.pdf)
  pp.5–12 顯示 Q2 營收 45.34 億元、毛利率 40.2%、營益率 30.4%、EPS 2.44 元；
  H1 營業現金流 25.41 億元、設備支出 70.07 億元、自由現金流負 44.66 億元，銀行
  借款淨增加 33.28 億元。龍潭廠完成客戶驗證並自 7 月量產，是時程里程碑，不是 AI
  ASIC 客戶、收入或利用率證據。
- pp.21–24 支持 CPO／矽光子的一站式能力、逾 150 台 EIC／PIC 測試設備、湖口新廠
  Q3 量產與逾 10 家新客戶導入／設計中；但沒有揭露收入、毛利、大量出貨或客戶實名，
  不能把「能力與導入」改寫成已完成商業化。

### 6239 力成

- [公司官方法說頁](https://www.pti.com.tw/zh/ir/news)的 2026Q2 簡報 pp.5–7 顯示 Q2
  營收 231.16 億元、毛利率 21.8%、營益率 15.3%、EPS 3.00 元；營業利益季增
  7.70 億元，業外反而減少 2.66 億元，因此 EPS 季增主要由本業改善推動。簡報明示
  Q2 數字尚未經會計師查核。
- pp.19–23 只支持 HBM 需求、先進封裝轉型、大尺寸 FC-BGA MCM 能力、FOPLP 客戶
  驗證與 2027 量產目標；全文沒有 HBM2 客戶、訂單、認證完成、產能或收入。原本「已簽
  HBM2 封裝訂單」必須維持未證，8 月 31 日仍沒有直接證據時應轉逾期未決，而不是硬判真。

### 6488 環球晶

- [公司 Q2 營收公告](https://www.sas-globalwafers.com/en/gwc_news_en_20260707/)顯示 Q2
  營收 152 億元、季增 8.79%／年減 4.96%，H1 營收 292 億元、年減 7.6%；營收回升
  不能自行歸因於漲價。
- [7 月 29 日 MOPS 自結公告](https://mopsov.twse.com.tw/mops/web/ajax_t05st01?TYPEK=otc&step=2&firstin=true&off=1&co_id=6488&spoke_date=20260729&spoke_time=170710&seq_no=4)
  顯示 6 月未核閱歸母淨損 39.55 億元、EPS 負 8.27 元；公司明示主因是 Siltronic
  股價及相關海外附認股權公司債的非現金評價損失。缺毛利與營業利益，不能用單月 EPS
  推論本業崩壞，也不能只採公司「本業穩健」文字替代營運數據。
- [7 月 22 日 Novara 火災公告](https://mopsov.twse.com.tw/mops/web/ajax_t05st01?TYPEK=otc&step=2&firstin=true&off=1&co_id=6488&spoke_date=20260722&spoke_time=193616&seq_no=1)
  確認 8 吋線停產、12 吋線未受影響；復工、設備損失與供貨影響仍待評估。
  [8 月 4 日法說公告](https://mopsov.twse.com.tw/mops/web/ajax_t05st01?TYPEK=otc&step=2&firstin=true&off=1&co_id=6488&spoke_date=20260720&spoke_time=151446&seq_no=1)
  只證實事件時間，不支持漲價或方形晶圓量產主張。

### 8261 富鼎

- [2026Q2 官方法說簡報](https://mopsov.twse.com.tw/server-java/FileDownLoad?step=9&filePath=%2Fhome%2Fhtml%2Fnas%2FSTR%2F&fileName=826120260729M002.pdf&functionName=t100sb02_1)
  pp.3–6 顯示 Q2 營收 8.77 億元、毛利率 34.2%、營益率 22.3%、EPS 1.51 元；
  營收季增 12.2%，毛利率與營益率卻分別季減 3.9、3.4 個百分點。EPS 年增 125.4%
  主要來自業外由負 1.14 億元轉為正 0.27 億元，同期營業利益反而年減 10.7%。
- pp.8、11–13 顯示 H1 高壓占比 14%，低於 2025 年 16%；Q2 SPS 季增 21%／年增
  24%，DC Fan 季減 8%／年增 44%，Computing 季增 38%／年減 46%。風扇年增方向
  仍相符，但季比轉弱且沒有 AI／一般伺服器拆分；全年雙位數成長與高壓組合升級仍未證。

## 影響路由

<!-- impact
group_id: power
stock_ids: 8261
direction: mixed
hypothesis_refs: 8261:H1,8261:H2
note_action: done
action_due:
rationale: 已用 2025 年報／查核財報、2026Q1 完整核閱季報與 Q2 法說建立 frozen pack，並由不同 reviewer 完成離線重算
evidence_boundary: Q2 簡報可支持核閱摘要；完整 H1 財報尚未上架，負債增加原因與現金流不自行推論
-->

<!-- impact
group_id: powersupply
stock_ids: 2308
direction: mixed
hypothesis_refs: 2308:H1
note_action: update_required
action_due: 2026-08-03
rationale: Q2 量利成長與部門分化須同步寫入正式筆記，並建立含最新法說與可用完整財報的 frozen pack
evidence_boundary: 基礎設施成長不等於 AI 或液冷收入，Q2 實績也不能裁決 Q4 是否高於 Q3
-->

<!-- impact
group_id: memory
stock_ids: 2337
direction: tailwind
hypothesis_refs: 2337:H1,2337:H2
note_action: update_required
action_due: 2026-08-03
rationale: Q2 本業與 eMMC 數字大幅改變舊筆記基準，需更新財務品質、產品結構與資本支出
evidence_boundary: 缺貨與當期價格方向已證，但逐月議價、滿載、長供合約與下半年持續性仍未證
-->

<!-- impact
group_id: packtest
stock_ids: 3264
direction: mixed
hypothesis_refs: 3264:H1,3264:H2
note_action: update_required
action_due: 2026-08-03
rationale: 龍潭量產與 CPO 能力里程碑成立，但 H1 負自由現金流、借款增加與流動比率下降需升為核心風險
evidence_boundary: 量產時程與客戶導入不等於 AI ASIC 歸因、收入、毛利或大量出貨
-->

<!-- impact
group_id: packtest
stock_ids: 6239
direction: tailwind
hypothesis_refs: 6239:H1,6239:H2
note_action: update_required
action_due: 2026-08-03
rationale: Q2 本業毛利與營益改善需更新正式筆記，並把 HBM 敘事降回產業需求與技術線索
evidence_boundary: 管理層簡報數字未經查核，且沒有 HBM2 訂單、客戶、認證、產能或收入證據
-->

<!-- impact
group_id: material
stock_ids: 6488
direction: mixed
hypothesis_refs: 6488:H1,6488:H2
note_action: review_due
action_due: 2026-08-05
rationale: 8 月 4 日法說後一次核對完整 Q2 營運、Siltronic 評價橋接、Novara 復工與兩則 H#
evidence_boundary: 單月未核閱自結與營收不足以判斷毛利、ASP、客戶接受度或方形晶圓量產
-->

## 下一個可證明／否定的節點

- 富鼎完成不同 reviewer 對同一 frozen pack 的離線重算後，才把正式筆記恢復為
  `independently_verified`；H1／H2 維持 open，到 8 月 31 日依原規格裁決。
- 8 月 3 日前依序補台達電、旺宏、欣銓與力成的正式筆記／證據包；若完整 Q2 季報尚未
  上架，可用最新法說加上當下最新完整季報，但必須在正文標清財務口徑與缺口。
- 8 月 4 日環球晶法說後優先核對毛利、營業利益、Siltronic 評價橋接、8 吋復工與供貨、
  晶圓 ASP／客戶接受度、方形晶圓驗證及量產；沒有直接證據就維持 H# open。
- 所有 H# 均保留原 deadline。市場價格、單日法人或月營收只能觸發搜尋，不得作為生命週期
  轉移證據；到期仍無足夠一手證據時使用 `expired_unresolved`，不可硬判 confirmed／refuted。
