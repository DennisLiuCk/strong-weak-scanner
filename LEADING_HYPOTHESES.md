# 領先假說（市場小作文）研究方法

`notes/leading_hypotheses/` 保存市場流傳、尚未被正式一手文件完整覆蓋，但具體、可追溯且
可被後續事件驗證的主張。它是觀察層，不是正式質化筆記、事實認證、投資建議或評分因子。

## 收錄邊界

- 只為已有有效 `independently_verified` 正式筆記的股票建立報告。
- 每則假說保存首次捕捉日、來源層級、目前狀態、正式資料基準、可證偽條件與下次驗證。
- 報告 meta 必須錨定正式筆記的 `reviewed_content_sha256`；正式筆記更新後，lint 會要求重新對照。
- 搜尋結果、社群貼文、媒體與券商轉述都只能支持「市場正在流傳此主張」，不能自動證明主張為真。
- 多篇轉載同一場法說、股東會或券商報告只算同一原始訊息鏈，不以網頁數灌水可信度。
- 不保存整篇受著作權保護的文章，只記研究所需的主張摘要、定位與原始連結。

## 狀態

| 狀態 | 定義 |
|---|---|
| `management_quoted` | 具名媒體轉述管理層談話，但尚未進入本輪正式 evidence pack |
| `consistent_unconfirmed` | 與正式資料方向一致，關鍵客戶、數量、占比或時程仍未證實 |
| `plausible_lead` | 產業邏輯合理且有明確驗證點，目前證據仍不足 |
| `attribution_error` | 產業、客戶或供應鏈數字被錯誤歸因為公司本身 |
| `unsupported_specificity` | 出現客戶名、台數、單價、占比或目標價等精確值，但原始依據不可追溯 |
| `contradicted` | 已被較強、較新的正式證據否定 |
| `resolved` | 後續證據已完成驗證；正文應保留結果與日期，不刪除歷史 |

`management_quoted` 不是「已獨立核驗」。管理層談話可能是方向、目標或估計，仍須等待財報、
重大訊息、法說附件或可重算營運結果。

## 固定格式與維護

每個 `## H#｜標題` 必須依序含有「市場主張、首次捕捉、來源層級、目前狀態、正式資料基準、
可證偽條件、下次驗證、研究判讀、來源」。建立或更新後執行：

```powershell
uv run --no-project --python 3.12 python scripts/leading_hypotheses.py --lint
uv run --no-project --python 3.12 python scripts/build_dashboard.py
uv run --no-project --python 3.12 python -m unittest discover -s tests
```

更新時不得用股價漲跌判定真偽；應使用假說事前寫下的公司揭露、季度營收／毛利、量產、驗收、
客戶或產能里程碑。失效的假說改標 `contradicted`，獲證實者改標 `resolved`，保留原始時間戳，
避免事後改寫研究紀錄。
