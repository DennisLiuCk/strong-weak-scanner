# 原始表欄位回補與正式 DB 稽核

本 runbook 處理兩種低頻維運工作：原始表 schema 新增欄位後的歷史回補，以及
`data/findmind.db` 的全期完整度驗收。一般每日缺口仍走 `scripts/run_daily.py` 或
`fetch_daily.py` 預設智慧補缺，不要套用本文件的歷史模式。

## 先選對模式

| 情境 | 指令／模式 | 語意 |
|---|---|---|
| 每日端點延遲、Action 中斷 | 預設智慧補缺 | 只補缺列與新交易日 |
| schema 新增原始欄位，舊列該欄為 `NULL` | `--backfill-expanded-fields` | 只掃既有交易日與 `RAW_COLUMN_MIGRATIONS` 缺欄，可續跑 |
| 交易所已公告來源修正版，既有非空值也必須覆寫 | `--force` | 無條件重抓指定範圍；不具欄位缺口續跑語意 |
| 只想確認正式 DB | `scripts/audit_raw_data.py` | SQLite `mode=ro`＋`query_only`，不做 schema migration 或寫入 |
| 往 2026-03-02 之前延伸歷史（pre-IS 檢定場） | `--db tmp/history.db --start …` | **必須另開 db**；對正式 db 會被擋下（見下節） |

## 歷史延伸（2026-03-02 之前）必須落在另一個 db

`fetch_daily.py` 的 `HISTORY_FLOOR = 2026-03-02` 是正式 DB 的起算日。`--start` 早於它
而 `--db` 仍指向正式 DB 時，argparse 直接 `exit 2`。

**理由不是潔癖，是實測結果（2026-07-26）**：把 2026-02 一個月接到既有歷史前面之後，
**3～4 月既有的個股綜合分有 51% 改變**——評分是族群內排名，而 `rs20`／`dist_hi60` 的
視窗一旦有了更早資料，就從 `NULL` 變成有值，連帶改寫排名與 tier。正式 DB 正在累積
不可改寫的 as-seen 快照；底下的重算歷史若被延伸改掉，快照與歷史就不再可比，且不可逆。

整條鏈都支援改道：`fetch_daily.py --db`、`score.py --db`、`validate.py --db`、
`audit_raw_data.py --db`。

一個月試跑（2026-02，12 個交易日）的實測結果與已知限制：

| 項目 | 結果 |
|---|---|
| 五張原始表 | 每表 1452 列＝121 檔 × 12 日，**零缺漏**；148 次官方批次請求，免 token |
| 還原股價 | 正確。83 檔與原始價不同，且**全部**都有 2 月之後的除權息；最新日錨點差異 0 |
| 大盤指數（regime 來源） | `--raw-only` 不碰 FinMind，`market` 會是空的；需另跑 `fetch_index` 補（實測可回補） |
| TPEx 報酬指數 | **永久無法回補**——櫃買 OpenAPI 只服務當月。屬觀察層，不進 regime／評分／發布門檻 |
| 冷啟動 | 起點前 20 日無 `rs20`、60 日無 `dist_hi60`，但 `composite` 仍會產出（缺項以 0 計）→ **回補起點必須比預計分析的最早日再往前 ≥60 個交易日**，否則前段分數不可比 |
| TDCC | 不可回補（缺週＝永久洞） |

`--backfill-expanded-fields` 自動採 `raw-only`：不讀 FinMind token、不抓事件、不重算
衍生表，也不發布 OOS／archive。它必須明確指定 `--start`，`--end` 省略時為今天。

## 標準流程

先同步並看回補前缺口；audit 退出碼為 `0=PASS`、`1=資料契約失敗`、`2=參數或檔案錯誤`：

```powershell
git pull
python scripts/audit_raw_data.py
```

一次補五表：

```powershell
python scripts/fetch_daily.py `
  --backfill-expanded-fields --start 2026-03-02 --end 2026-07-17
```

長區間可按 dataset 分段；名稱沿用既有 FinMind selector，但資料仍來自 TWSE／TPEx：

```powershell
python scripts/fetch_daily.py `
  --backfill-expanded-fields --datasets TaiwanStockMarginPurchaseShortSale `
  --start 2026-03-02 --end 2026-07-17
```

中斷或端點失敗後，重跑**同一條命令**。每個交易所成功後會立即 commit SQLite；下一輪
會以「缺列，或任一 expanded 欄仍為 `NULL`」重新規劃，只要求尚未完成的股票／日期。
完成後再重跑一次應顯示官方批次 `0` 次，證明冪等且沒有重打來源。

回補後再次稽核；需要機器可讀輸出時加 `--json`：

```powershell
python scripts/audit_raw_data.py `
  --start 2026-03-02 --end 2026-07-17
python scripts/audit_raw_data.py --json
```

audit 的硬性條件是 current universe × `price ∪ market` 交易日的五表完整 grid、core／
expanded 必備欄非空、SQLite integrity，以及法人、融資、融券與借券公式一致。唯一例外是
官方 price 列可嚴格重算的零交易 pair：price 的 OHLC 可空、inst 可不列；margin／holding／
sbl 仍須完整。`market_index` 維持
非阻斷觀察層，因此缺口列為 warning；TPEx 公開端點只驗最新月份可再取得的交易日。
不在交易日 spine 的 legacy row 也只列 warning：它不會灌大完整度，且未經來源查證不要刪除。

## 歷史 restatement 的衍生層重建

只有 audit PASS 後才依序重建：

```powershell
python scripts/fetch_daily.py --metrics-only
python scripts/score.py
python scripts/build_dashboard.py
python -m unittest discover -s tests
python scripts/daily_brief.py
```

歷史 restatement 不得執行 `snapshot_signals.py --publish`，也不得覆寫既有
`archive/<資料日>.html`；它們是 as-seen OOS 證據。`build_dashboard.py` 只應刷新目前首頁，
既有 archive 會由程式保留。最後 review `data/findmind.db`、`index.html` 與文件差異後再 commit。

## 請求量與逾時判讀

欄位回補的官方請求量約為 `2 × 不完整的 dataset-day`。五表 × 95 個既有交易日為
`2 × 5 × 95 = 950` 次；交易所請求內建 0.5 秒禮貌間隔，最低約 8 分鐘，應預留更長的
command timeout。process 逾時不代表已完成資料消失；先重跑 audit，再用同一回補命令續接。

不要因逾時改用 `--force`。`--force` 的用途是覆寫已存在且非空的來源修正版；它會重抓
完整指定範圍，價格也會探測範圍內日曆日，成本與誤觸限流風險都較高。
