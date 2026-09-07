# 研究方法稽核紀錄

這個目錄不是文章庫，而是用來回答「我們有沒有回頭檢驗，以及方法是否真的在改善」。

- `YYYY-MM-DD_NN.json` 是 append-only 方法快照。它保存當時的 claim、source、monitor、
  圖譜與候選雷達覆蓋，不得回頭改寫；同一天重跑就新增下一個 sequence。
- `monitor_reviews.csv` 是 append-only 到期檢查帳本。每一列必須連到既有 topic／monitor。
  `new_support`／`new_contrary` 必須引用已登錄的新來源；`no_new_evidence` 與
  `not_yet_testable` 不得刷新 evidence clock。
- 即使累積三個帶新證據的到期結果，也只顯示結果分類與計數，不計支持率。
  `new_support` 可能只是取得附件或完成簽核，不代表主命題成立；目前 outcome schema
  尚未編碼主命題真假，更不能換算成投資命中率、報酬率或因果效果。

每次研究 registry 有變動時執行：

```powershell
python scripts/research_method_audit.py --json
python scripts/research_method_audit.py --lint --baseline-ref <本輪修改前的完整SHA>
```

第一個命令產生本次快照內容；用新的 sequence 檔保存後，再用第二個命令確認 registry
fingerprint 一致、舊快照未改寫且 review ledger 只追加新列。

來源及流程同步檢查：正式筆記完成後，回查相關 topic 的 impact、摘要與下一步，避免
仍標為待辦；完成狀態依已提交 note meta、manifest 與簽核紀錄判定，不重複聲稱本輪執行
獨立複核。工作進度日期與主命題 evidence clock 分開，只有命中原證據條件才更新後者。

正式發布使用 `prepublish_check.py --baseline-ref <本輪修改前的完整SHA>`；基準不隨
commit 或重試改成最新 HEAD。快照輸出直接以 UTF-8／LF 寫入新檔，不用 Windows shell
重導向，以免入庫前後換行不同造成歷史誤判。
