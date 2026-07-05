# strong-weak-scanner · 汰弱留強掃描器

台股半導體三族群(**被動元件 / 功率元件 / 封測**,共 30 檔)的「汰弱留強」量化掃描系統。
每天抓取五元素、落地 SQLite,並定期用 Claude 交叉比對驗證假設、持續優化策略。

## 元素框架(族群內排名制)

| 元素 | 指標 | 權重 | 意義 |
|---|---|---|---|
| ① 相對強弱 | rs20(20日報酬 − 族群中位)族群內排名 | 1.4 | 族群內誰在領漲 |
| ① 抗跌 | down_rs20(族群下跌日相對表現)排名 | 1.0 | 修正時誰站得住 |
| ② 量 | 量比(相對自身 60 日中位) | 0.3 | 活絡/枯竭 + 過熱旗標 |
| ③ 外資 | 20 日持股 pp 變化 排名 | 0.5 | 族群層訊號為主 |
| ③′ 逆勢買超 | 族群下跌日外資淨買 20 日累計/股本 | 0(tier 用)| 蓄勢偵測、儀表板顯示 |
| ④ 投信 | 近 5 日淨額佔股本 排名 | 0.8 | 本土法人 / 作帳 |
| ⑤ 融資券 | 價×融資交互 + 散戶水位封頂 | 0.4 | 散戶籌碼與未來賣壓 |

> 設計原則:**族群內選股靠價格相對因子(相對強弱、抗跌),籌碼是族群層訊號**
> (用於判斷哪個族群正在被佈局,而非族群內排序)。tier 需連 2 日同向才轉層;
> 綜合分取 3 日平滑。權重與門檻的實證依據見 [CHANGELOG.md](CHANGELOG.md)。

## 架構

```
每日(雲端 routine) → fetch_daily.py:4 datasets × 30 檔 + 除權息/分割事件 + TAIEX
                      → SQLite → 還原價 → 五元素 → 族群層聚合(group_metrics/market_daily)
                      → score.py(族群內排名 + tier)→ build_dashboard.py(index.html)
每週(六 09:00 自動)  → validate.py → reports/validate_*.md(元素 IC 分 regime/IS/OOS、
                      tier 超額與轉移事件、新舊制對照、族群層命中率)
                      → 依 WEEKLY_REVIEW.md 檢視報告 → 調策略(一次最多 1~2 個旋鈕)
```

週檢視的標準程序與行動判準:**[WEEKLY_REVIEW.md](WEEKLY_REVIEW.md)**;
盤後日常檢視(確認 Actions、今日簡報、討論):**[DAILY_CHECK.md](DAILY_CHECK.md)**。

**兩層訊號分工**:個股層 = 族群內排名選強汰弱;族群層 = 佈局廣度 + 修正日中位
逆勢買超,找出正在被佈局的族群;大盤層 = 報酬指數距 20 日高的修正 regime 旗標。
版本沿革與設計決策的實證依據見 [CHANGELOG.md](CHANGELOG.md),滾動驗證見
`reports/validate_*.md`。

## 目錄

```
config/universe.csv      30 檔清單(id, name, group)
scripts/fetch_daily.py   零依賴 ETL(stdlib urllib + sqlite3);抓取 + 重算五元素
data/findmind.db         SQLite(方案 A 靠它 commit 跨天累積狀態)
  ├ price / inst / margin / holding   FinMind 原始四表(append-only,可重算)
  ├ dividend_result / price_adj       除權息結果(FinMind 免費)→ 本地自算還原股價(每次重建)
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

## Universe 治理

- **規則**:R1 業務歸屬(主營收 >50% 屬族群業務,人工覆核)/ R2 市值遲滯
  (≥50 億納入、現有成員 <30 億才剔除,防反覆進出)/ R3 近 20 日中位成交值
  ≥3,000 萬 / R4 上市 ≥60 交易日。族群定義在 `config/groups.csv`(名稱/tag/排序),
  成員在 `config/universe.csv`(代號/名稱/族群/主業)。
- **節奏**:每季跑 `scripts/screen.py`(現有成員體檢 + `config/candidates.csv`
  候選提名),覆核後改 universe.csv → `fetch_daily.py --start <窗首>` 回補 →
  變更記入 CHANGELOG。
- **注意**:universe 變更後全歷史按新名單重算(族群中位、排名都會變),
  變更的審計軌跡以 CHANGELOG 為準。

## 資料註記

- 價格類指標(ret1 / 距 20/60 日高)用**還原股價**(`price_adj`),除權息不會造成假跌;原始 `price` 表保留未還原價供顯示。周轉率 / 散戶水位 / 投信佔股本用**當日**發行股數(非最新股本回填,避免前視)。
- 券商分點(真主力)需 FinMind **Sponsor** 等級,目前未開通。
- 回測要用「當日可得」資料避免 lookahead(外資持股有申報遞延);本表只 append、不覆寫。
- 本專案為量化籌碼研究,**非投資建議**。

## 視覺化儀表板

<https://dennisliuck.github.io/strong-weak-scanner>
