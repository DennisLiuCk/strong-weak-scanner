# 八檔優先研究對象：2026Q2 文件上線與事件等待清單

<!-- research_topic
topic_id: MI-2026-07-29-PRIORITY-Q2-DISCLOSURES
schema_version: 1
status: triaged
priority: p1
captured_at: 2026-07-29
source_published_at: 2026-07-28
last_reviewed_at: 2026-07-29
review_due: 2026-08-06
source_type: mixed
publisher_domain: cht-pt.com.tw
canonical_url: https://www.cht-pt.com.tw/xccompdoc?xsmsid=0G328557247962808262
source_chain_id: priority-q2-official-scan-20260729
stock_ids: 3035,6510,3037,3260,6271,3675,3711,3131
group_ids: ipdesign,semiequip,pcb,memory,packtest,power
trigger_type: quarterly_results_and_board_events
evidence_role: candidate_source
route: formal_note_candidate
-->

<!-- transition
date: 2026-07-29
from: initial
to: inbox
reason: priority_targets_primary_source_scan
evidence: source_chain:priority-q2-official-scan-20260729
-->
<!-- transition
date: 2026-07-29
from: inbox
to: triaged
reason: separated_available_q2_documents_from_event_notices_and_no_file_results
evidence: source_chain:priority-q2-official-scan-20260729
-->

## 為何值得進佇列

7 月 28～29 日密集出現第二季法說、董事會與財報事件，但八檔的文件成熟度不同。精測與
欣興已有可下載的公司 Q2 簡報，其中精測另有標示 `Reviewed` 的三頁財務摘要；該摘要不是
含會計師核閱報告與附註的完整季報，不能承擔 evidence pack 的 `latest_quarterly_report`
角色。智原官網已列 7 月 28 日 Q2 法說，仍須把實際簡報納入證據包後才能更新正式筆記。
其餘五檔在本次掃描時只有事件預告，或交易所正式財報文件清單仍無 115Q2 檔案。這批資料
應分成「現在可重做證據包」與「事件後再更新」，不能因公告標題出現「Q2」就先填財務數字。

## 來源與證據邊界

- [精測 2026Q2 官方營運說明會入口](https://www.cht-pt.com.tw/xccompdoc?xsmsid=0G328557247962808262)、
  [法說簡報](https://www.cht-pt.com.tw/files/file_pool/1/0Q209650487702138855/26Q2%20%E6%B3%95%E8%AA%AA%E6%9C%83_CN.pdf)與
  [Reviewed 財務摘要](https://www.cht-pt.com.tw/files/file_pool/1/0Q210669178494948819/CHPT%20Financial%20Report_2026Q2.pdf)
  （2026-07-29）。可核對營收、產品／應用組合、毛利、營業利益、EPS、現金流與資產負債
  摘要；正式筆記只能用 Q2 法說中可直接核對的數字，完整季報角色仍須使用 2026Q1 核閱
  財報。這些資料不等於 H1 的 2028 需求具約束性，也未自動證實 H2 的 8 月產能翻倍或具名
  合作。
- [欣興官方法說頁](https://www.unimicron.com/money03.html)與
  [2026Q2 合併營運簡報](https://www.unimicron.com/files/money/Earnings/ch/2026-Q2-consolidated-ch.pdf)
  （2026-07-29）。可使用簡報明示的 Q2 營運、產品應用、毛利與展望；正式 Q2 財報尚未
  定位，故不能補現金流、存貨、應收或借款明細，也不能把整體展望改寫成 H1 的長約細節。
- [智原官方法說頁](https://www.faraday-tech.com/tw/html/IR/QuarterlyResults.html)
  已列 2026-07-28 Q2 法說。事件成立不等於簡報中的任一財務或專案數字已被重算；正式
  筆記只在文件納入 evidence pack 後更新。
- [同欣電 8 月 5 日 Q2 法說預告](https://www.theil.com/zh-tw/information.php?act=view&id=246)、
  [Q2 董事會預告](https://www.theil.com/zh-tw/information.php?act=view&id=245)與
  [公司財報頁](https://www.theil.com/zh-tw/financial_report.php)。截至本次掃描，公司頁
  仍只列 2026Q1 財報；預告不能支持產品組合、菲律賓廠進度或光通訊收入。
- [德微 Q2 董事會預告](https://www.eris.com.tw/ShowMops.php?seq_no=1&spoke_time=153338&spoke_date=1150721)
  與[公司財報頁](https://www.eris.com.tw/financialReport.php)。截至本次掃描只確認開會
  事件，不能據此更新毛利、現金流、庫存或 H1／H2 商業化規模。
- 交易所正式文件清單在本次掃描時，對
  [威剛](https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id=3260&year=115&seamon=2&mtype=A)、
  [日月光投控](https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id=3711&year=115&seamon=2&mtype=A)與
  [弘塑](https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id=3131&year=115&seamon=2&mtype=A)
  均無可定位的 115Q2 正式財報 PDF。這只描述 7 月 29 日的查找結果；Q2 法定申報期限
  尚未到，不代表逾期或未通過董事會。

## 影響路由

<!-- impact
group_id: ipdesign
stock_ids: 3035
direction: uncertain
hypothesis_refs: 3035:H1,3035:H2
note_action: update_required
action_due: 2026-07-31
rationale: 公司 Q2 法說已舉行，先定位並封存實際簡報，再重算專案組合、毛利與履約路徑
evidence_boundary: 法說事件與網頁索引本身不支持專案金額、投片時程或 NRE 轉 MP 結論
-->

<!-- impact
group_id: semiequip
stock_ids: 6510
direction: mixed
hypothesis_refs: 6510:H1,6510:H2
note_action: done
action_due:
rationale: 已以 2026Q1 完整核閱季報與 Q2 法說重做 frozen pack，排除三頁 Q2 摘要的季報角色，並完成獨立 reviewer 離線重算
evidence_boundary: Q2 法說數字可檢查 H1 的逐季路徑，但不證實 2028 約束性訂單；三頁摘要沒有完整核閱報告與附註，簡報未明示的 H2 細節仍保持未證
-->

<!-- impact
group_id: pcb
stock_ids: 3037
direction: mixed
hypothesis_refs: 3037:H1,3037:H2
note_action: done
action_due:
rationale: 已用 2025 年報／查核財報、2026Q1 完整核閱季報與 Q2 法說建立 frozen pack，並完成不同 reviewer 的離線重算
evidence_boundary: 簡報可支持公司明示數字，不自動證實長約、預付款、鎖定產能或供應商交期傳聞
-->

<!-- impact
group_id: memory
stock_ids: 3260
direction: uncertain
hypothesis_refs: 3260:H1,3260:H2
note_action: review_due
action_due: 2026-08-01
rationale: 本次未定位到 115Q2 正式附件，待公司或交易所檔案上線後再檢查存貨、現金流與應收
evidence_boundary: 月營收與股價只能觸發搜尋，不能證實缺貨延續、2027 長約或全年營收倍增
-->

<!-- impact
group_id: packtest
stock_ids: 6271,3711
direction: uncertain
hypothesis_refs: 6271:H1,6271:H2,3711:H1,3711:H2
note_action: review_due
action_due: 2026-08-06
rationale: 同欣電等待 8 月 5 日法說與正式附件；日月光投控等待可下載 Q2 正式文件
evidence_boundary: 事件預告或產業封裝需求不能替代公司收入組合、產能、毛利與具名客戶證據
-->

<!-- impact
group_id: power
stock_ids: 3675
direction: uncertain
hypothesis_refs: 3675:H1,3675:H2
note_action: review_due
action_due: 2026-08-01
rationale: 已有董事會事件但尚無本次可重算的 Q2 正式附件，待公司財報頁更新
evidence_boundary: 董事會預告不能支持 AI server 晶圓商業化或小訊號產品量產規模
-->

<!-- impact
group_id: semiequip
stock_ids: 3131
direction: uncertain
hypothesis_refs: 3131:H1,3131:H2
note_action: watch
action_due: 2026-08-05
rationale: Q2 董事會預計 8 月 4 日召開，事件後檢查設備收入、合約負債、在製與毛利
evidence_boundary: 產業 CoWoS 需求不能替代弘塑具名急單或全年營收大於 80 億元的公司證據
-->

## 下一個可證明／否定的節點

- 精測與欣興完成 focused evidence pack、獨立 reviewer 重算及正式筆記簽核；未通過前只
  顯示草稿狀態，不把 Q2 簡報摘要當成已核驗文章。
- 智原定位並封存 7 月 28 日實際簡報；若仍無穩定來源，依 10 分鐘上限記錄 timeout，
  刪除無法驗證的新增主張。
- 8 月 1 日前重查威剛、德微與日月光投控的公司 IR／交易所正式文件；8 月 4 日後重查
  弘塑；8 月 5 日同欣電法說後再做公司層級更新。
- 任一事件若只有標題、董事會預告或媒體數字，保持 `review_due`／`watch`，不更新正式
  筆記、不轉移 H# 生命週期，也不改量化分數。
