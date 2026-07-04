# strong-weak-scanner · 汰弱留強掃描器

台股半導體三族群(**被動元件 / 功率元件 / 封測**,共 30 檔)的「汰弱留強」量化掃描系統。
每天抓取五元素、落地 SQLite,並定期用 Claude 交叉比對驗證假設、持續優化策略。

## 五元素框架

| 元素 | 指標 | 意義 |
|---|---|---|
| ① 價 | 距波段高、反彈幅度 | 表象 |
| ② 量 | 周轉率、量能放大 | 價格真假 |
| ③ 外資 | 持股比例變化(pp) | 國際法人方向 |
| ④ 投信 | 買賣超 / 認養 | 本土法人 / 作帳 |
| ⑤ 融資券 | 散戶水位、券資比 | 散戶籌碼與未來賣壓 |

> 核心觀念:**價是表象,量定真假,籌碼(外資/投信/融資券)決定歸屬與賣壓。** 五者交叉才看得出誰真強、誰是出貨陷阱、誰是外資默默佈局的蓄勢股。

## 架構

```
每日(雲端 routine)     → fetch_daily.py 抓 4 datasets × 30 檔 → SQLite
每週(Claude 半自動)    → 前瞻報酬 by tier / element IC / 假設命中 → 調策略 → 重生儀表板
```

## 目錄

```
config/universe.csv      30 檔清單(id, name, group)
scripts/fetch_daily.py   零依賴 ETL(stdlib urllib + sqlite3);抓取 + 重算五元素
data/findmind.db         SQLite(方案 A 靠它 commit 跨天累積狀態)
  ├ price / inst / margin / holding   FinMind 原始四表(可重算)
  └ daily_metrics                     五元素衍生指標
```

## 用法

```bash
# 增量(每日;預設補最近 15 天、自動 upsert 去重、重算五元素)
uv run --no-project python scripts/fetch_daily.py

# 回補歷史
uv run --no-project python scripts/fetch_daily.py --start 2026-03-01 --end 2026-07-03
```

Token 讀取順序:環境變數 `FINMIND_TOKEN` → 本機 `.mcp.json`(已被 `.gitignore` 排除)。
雲端 routine 用 secret 注入 `FINMIND_TOKEN`。

## 資料註記

- 原始(未還原)股價,適合短線比較;長期報酬應改用還原股價。
- 券商分點(真主力)需 FinMind **Sponsor** 等級,目前未開通。
- 回測要用「當日可得」資料避免 lookahead(外資持股有申報遞延);本表只 append、不覆寫。
- 本專案為量化籌碼研究,**非投資建議**。

## 視覺化儀表板

30 檔 × 五元素互動熱力圖(hover 看數據與理由):
<https://claude.ai/code/artifact/5c32b02f-fbf0-4195-91dd-6257b62d0432>
