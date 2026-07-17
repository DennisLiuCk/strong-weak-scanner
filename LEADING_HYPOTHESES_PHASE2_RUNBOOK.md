# 領先假說第二階段操作手冊

第二階段只評估系統實際捕捉後的前瞻樣本。第一階段及覆蓋補齊的 196 則回溯基線可用來測試格式與複核，
不可與前瞻樣本混合計算資訊領先時間或成立率。

回溯基線已於 2026-07-12 封存；此後新增 H# 一律使用 `capture_mode: prospective`。lint 會拒絕
研究收錄日晚於封存日的 `retrospective`，不能為了補齊歷史新聞而回填研究日期。

## 〇、捕捉掃描:來源清單與觸發器

前瞻捕捉的價值取決於掃描面向;單一新聞源會漏掉整類主張。每次為一檔股票做捕捉
掃描時,依序過一遍下列面向(對應既有 `source_type` 分類法,來源仍只證明
「市場正在流傳」):

| 面向 | 典型來源 | source_type |
|---|---|---|
| 公司正式管道 | MOPS 重大訊息/法說公告、公司 IR 新聞稿、股東會訊息 | `official_company` |
| 管理層談話 | 法說逐字/摘要、媒體具名採訪、股東會答詢 | `management_direct`/`management_relay` |
| 法人與券商 | 券商報告轉述、投顧晨會紀要、外資評等消息 | `broker_relay` |
| 產業媒體 | TechNews、DigiTimes、經濟日報、工商時報、鉅亨網 | `media_report` |
| 供應鏈耳語 | 匿名供應鏈消息、同業法說中點名的客戶/對手訊號 | `anonymous_supply_chain` |
| 社群與自媒體 | PTT Stock、Dcard、CMoney、X/Twitter、投資部落格 | `social_post`/`self_media` |
| 產業鏈交叉 | 同族群其他公司的正式筆記與假說、`notes/events/` 台積電法說族群指引 | 依原始來源 |

自家量化 db 是**捕捉觸發器**而非證據來源:`--context` 快照或每日儀表板出現異常
(單月營收暴衝、借券/大戶比急變、處置注意旗標、族群內排名跳動)時,回頭掃上表
找「市場怎麼說」,把可證偽的版本收進 H#;異常本身不構成主張,股價與成交量
變化也永遠不觸發生命週期轉移。

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

7. **同步補多空觀點。** 新增或更新 H# 後,執行
   `leading_hypotheses.py --context <股號>` 產生量化背景,依
   [LEADING_HYPOTHESES.md「多空觀點」](LEADING_HYPOTHESES.md#多空觀點小作文與量化背景)
   撰寫/改寫看多小作文、看空小作文與勝負手;敘事只能使用 H#、正式筆記與量化背景
   已有的材料,兩篇都要以「最脆弱處」自陳弱點。既有 H# 生命週期轉移時,小作文
   應一併檢視是否已被拆掉。

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
