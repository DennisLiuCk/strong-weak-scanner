# 領先假說第二階段操作手冊

第二階段只評估系統實際捕捉後的前瞻樣本。第一階段 156 則回溯基線可用來測試格式與複核，
不可與前瞻樣本混合計算資訊領先時間或成立率。

## 一、收錄新主張

1. **先判斷是否原子化。** 一則假說只包含一個可判定的公司層主張；客戶、數量、價格、時程
   若能分別成立或失效，拆成不同 H#。
2. **當日留下研究時間。** `research_captured_at` 填研究實際看見並收錄的台灣日期，正文同步寫
   「前瞻捕捉」；不可把較早的消息發布日回填成研究收錄日。
3. **記錄來源而非背書。** `source_type` 描述來源，`evidence_strength` 描述現有證據，兩者分開。
   管理層說法通常仍是待驗證主張，不因具名而自動成為 `strong`。
4. **辨識原始消息鏈。** 多個網址若都轉述同一場法說、同一券商報告或同一匿名消息，使用相同
   `source_chain_id`；只有可辨識為不同原始採訪、文件或調查才增加獨立鏈數。
5. **先寫失敗條件。** 可證偽條件必須在結果揭曉前完成，且能指出期間、指標或事件；「股價沒漲」
   不是公司主張的失敗條件。
6. **設定假說層期限。** `review_due` 是最晚判定或重新評估日；「下次驗證」另寫會提前觸發的
   財報、法說、月營收、重大訊息、認證、量產或驗收事件。

建立完成後執行 lint；若來源只有轉貼搜尋結果、無法定位原始主張或主張無法被未來事件判定，
不納入資料集。

## 二、複核佇列

例行檢查使用：

```powershell
uv run --no-project --python 3.12 python scripts/leading_hypotheses.py --due
uv run --no-project --python 3.12 python scripts/leading_hypotheses.py --due --as-of 2026-08-31
```

除了到期佇列，下列事件可提前複核：正式筆記更新造成 SHA 失配、公司發布財報或法說附件、
重大訊息直接涉及主張、事前指定的量產／驗收／客戶里程碑發生。單純股價或成交量變化不觸發
真偽轉移。

## 三、更新證據維度

新資料出現時，先分別更新三個維度：

- `evidence_strength`：現有證據能否直接支持公司層主張。
- `evidence_flags`：是否仍有匿名、轉述、過度精確或歸因錯置問題。
- 中文「目前狀態」：將上述維度轉成讀者可理解的摘要。

生命週期或 `review_due` 改變時都新增 `transition`；期限變更使用 `open → open`，讓歷史佇列
可以重建。同一生命週期內只有證據強度或警示增減時，可更新欄位並在 git diff 與研究判讀
說明原因；不可為了讓敘事看起來正確而改寫原始市場主張。

## 四、進入終態

| 結果 | `lifecycle` | 中文狀態 | 處理 |
|---|---|---|---|
| 正式證據證實 | `confirmed` | 已驗證成立 | 證據強度改 `strong`，`review_due: none` |
| 正式證據否定 | `refuted` | 已驗證不成立 | 證據強度改 `strong`，`review_due: none` |
| 期限已過仍無法判定 | `expired_unresolved` | 到期仍無法判定 | 不把未知強迫判成錯誤，`review_due: none` |

終態 transition 必須保存正式文件、可重算實績或里程碑的定位；報告內所有假說都進入終態後，
報告 meta `status` 才改為 `closed`，並將報告層 `next_review` 改成 `none`。終態後若發現研究
程序有錯，新增更正紀錄，不刪除舊轉移。

## 五、前瞻成效檢視

只對 `capture_mode: prospective` 計算：

- 30／60／90 日內進入任一終態的可判定率。
- 可判定樣本中的成立率與否定率。
- 到期仍無法判定率。
- 研究收錄日至終態 transition `evidence_published_at` 的資訊領先天數。
- 各來源類型、證據警示及獨立消息鏈數的分組結果。
- 每則假說的搜尋、建檔與複核時間；用來估計每則有效線索的維護成本。

樣本未完成至少一個財報或法說週期前，不因少數成功案例擴張公司數，也不把股價報酬混入真偽
指標。若另研究市場反應，必須預先凍結事件窗與價格計算規則，作為獨立分析層。

## 六、提交前檢查

```powershell
uv run --no-project --python 3.12 python scripts/leading_hypotheses.py --lint
uv run --no-project --python 3.12 python scripts/leading_hypotheses.py --summary
uv run --no-project --python 3.12 python scripts/leading_hypotheses.py --metrics
uv run --no-project --python 3.12 python scripts/build_dashboard.py
uv run --no-project --python 3.12 python -m unittest discover -s tests
git diff --check
```

每次提交應能回答：新增或變更了哪些主張、研究何時實際捕捉、哪一條獨立消息鏈、下一個驗證
事件與期限、是否發生生命週期轉移，以及轉移依據是什麼。
