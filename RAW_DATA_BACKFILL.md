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

`--backfill-expanded-fields` 自動採 `raw-only`：不讀 FinMind token、不抓事件、不重算
衍生表，也不發布 OOS／archive。它必須明確指定 `--start`，`--end` 省略時為今天。

## 標準流程

先同步並看回補前缺口；audit 退出碼為 `0=PASS`、`1=資料契約失敗`、`2=參數或檔案錯誤`：

```powershell
git pull
uv run --no-project --python 3.12 python scripts/audit_raw_data.py
```

一次補五表：

```powershell
uv run --no-project --python 3.12 python scripts/fetch_daily.py `
  --backfill-expanded-fields --start 2026-03-02 --end 2026-07-17
```

長區間可按 dataset 分段；名稱沿用既有 FinMind selector，但資料仍來自 TWSE／TPEx：

```powershell
uv run --no-project --python 3.12 python scripts/fetch_daily.py `
  --backfill-expanded-fields --datasets TaiwanStockMarginPurchaseShortSale `
  --start 2026-03-02 --end 2026-07-17
```

中斷或端點失敗後，重跑**同一條命令**。每個交易所成功後會立即 commit SQLite；下一輪
會以「缺列，或任一 expanded 欄仍為 `NULL`」重新規劃，只要求尚未完成的股票／日期。
完成後再重跑一次應顯示官方批次 `0` 次，證明冪等且沒有重打來源。

回補後再次稽核；需要機器可讀輸出時加 `--json`：

```powershell
uv run --no-project --python 3.12 python scripts/audit_raw_data.py `
  --start 2026-03-02 --end 2026-07-17
uv run --no-project --python 3.12 python scripts/audit_raw_data.py --json
```

audit 的硬性條件是 current universe × `price ∪ market` 交易日的五表完整 grid、core／
expanded 必備欄非空、SQLite integrity，以及法人與借券公式一致。`market_index` 維持
非阻斷觀察層，因此缺口列為 warning；TPEx 公開端點只驗最新月份可再取得的交易日。
不在交易日 spine 的 legacy row 也只列 warning：它不會灌大完整度，且未經來源查證不要刪除。

## 歷史 restatement 的衍生層重建

只有 audit PASS 後才依序重建：

```powershell
uv run --no-project --python 3.12 python scripts/fetch_daily.py --metrics-only
uv run --no-project --python 3.12 python scripts/score.py
uv run --no-project --python 3.12 python scripts/build_dashboard.py
uv run --no-project --python 3.12 python -m unittest discover -s tests
uv run --no-project --python 3.12 python scripts/daily_brief.py
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
