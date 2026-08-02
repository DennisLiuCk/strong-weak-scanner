# 研究方法稽核紀錄

這個目錄不是文章庫，而是用來回答「我們有沒有回頭檢驗，以及方法是否真的在改善」。

- `YYYY-MM-DD_NN.json` 是 append-only 方法快照。它保存當時的 claim、source、monitor、
  圖譜與候選雷達覆蓋，不得回頭改寫；同一天重跑就新增下一個 sequence。
- `monitor_reviews.csv` 是 append-only 到期檢查帳本。每一列必須連到既有 topic／monitor。
  `new_support`／`new_contrary` 必須引用已登錄的新來源；`no_new_evidence` 與
  `not_yet_testable` 不得刷新 evidence clock。
- 只有到期 monitor 全部有 review event，且至少累積三個帶新證據的結果時，系統才顯示
  描述性支持率；它仍不是投資命中率、報酬率或因果效果。

每次研究 registry 有變動時執行：

```powershell
python scripts/research_method_audit.py --json
python scripts/research_method_audit.py --lint --baseline-ref HEAD
```

第一個命令產生本次快照內容；用新的 sequence 檔保存後，再用第二個命令確認 registry
fingerprint 一致、舊快照未改寫且 review ledger 只追加新列。
