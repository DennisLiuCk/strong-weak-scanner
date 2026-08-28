# SQLite 儲存容量與後續方案 — 2026-08-29

## 本次決定

暫時保留正式 `data/findmind.db` 與每日 Actions 的現行寫入方式，新增可重跑的唯讀容量
工具。下一步先在隔離環境驗證「壓縮檔＋SHA-256 manifest」的發布與復原流程；
**尚未選定或啟用新的儲存後端，未遷移 DB、重寫 Git 歷史或開啟付費額度。**

GitHub 對一般 Git 檔案 **超過 50 MiB 警告、超過 100 MiB 拒收**；警告不等於本次
push 失敗。這是單檔限制，不能拿本地 `.git` 占用或 Git pack 的壓縮後大小代替。
官方另列 Releases 作為大型二進位檔的分發方式。
[GitHub 大型檔案說明](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)

## 量測範圍與結果

- 基線 commit：`57936fa1d60ca3ae256072d3265741dca9f25b36`，資料日 2026-08-28。
- 母體：該 commit 對應的一個完整 SQLite 檔案；不是抽樣，SE／t 不適用。
  單次橫斷面不能推算何時到達 100 MiB，也不能當成遠端 GitHub 儲存用量。
- 環境：macOS 26.5.2 arm64、pyenv Python 3.11.11、SQLite 3.51.0、預設 UTF-8。
  SQLite 連線強制使用 `db_ro.connect()`，`query_only=1`、journal mode 為 `delete`。
- DB SHA-256：`2a5aeee10bf7619a3bd497d2a071ad27a451441298042b1a29af38f0f2945a20`。
  量測前後相同；這是本次觀測一致性，不是防止其他程序寫入的鎖或備份保證。

| 項目 | 精確 bytes／計數 | 換算與意義 |
|---|---:|---|
| 正式 DB | 58,114,048 bytes | 55.4219 MiB，已超過警告值 |
| 距 100 MiB | 46,743,552 bytes | 44.5781 MiB，不是剩餘可用天數 |
| SQLite page size／page count | 4,096 bytes／14,188 頁 | 與實體檔案長度吻合 |
| freelist | 0 頁 | 沒有整頁空閒；未量測頁內碎片或 VACUUM 效益 |
| gzip level 6、mtime 0 | 19,462,262 bytes | 18.5607 MiB，比原檔少 66.5102% |
| 解壓長度 | 58,114,048 bytes | SHA-256 與原檔一致，另作逐 byte 比對 |

以下是 `dbstat` 的表與所屬索引配置頁數，**不是邏輯資料大小或可以刪除的容量**：

| 表（含索引） | bytes | MiB |
|---|---:|---:|
| `balance_sheet` | 17,256,448 | 16.4570 |
| `observation_metrics` | 5,681,152 | 5.4180 |
| `daily_metrics` | 5,365,760 | 5.1172 |
| `cash_flow` | 4,898,816 | 4.6719 |
| `market_index` | 3,395,584 | 3.2383 |

工具按 owning table 彙總全部 40 組配置。第二條獨立路徑以 SQLite 檔頭解析頁大小、
總頁數和 freelist；另寫 SQL join/group 核對全部配置，並以 `gzip.compress` +
`zlib.decompress` 重算壓縮長度、逐 byte 復原與 SHA-256，全部吻合。
工作證據留在 `tmp/research_work_2026-08-29/storage/final_57936fa/`，不進版控；
較早 7b8f6b9 的量測保留於上層目錄，不把排程新版本與舊版混算。

## 選項比較

| 方案 | 適用處與成本 | 本次判斷 |
|---|---|---|
| 維持原始 DB 入 Git | 不改本地使用、Actions 與 as-seen 契約；每日二進位歷史持續累積 | 短期維持，定期量測，不把 warning 當失敗 |
| 壓縮檔放在獨立分發位置，Git 保存 manifest | 此樣本可無損縮小；需處理下載失敗、權限、版本保留、原子切換及復原 | 優先做隔離原型；尚未驗證遠端發布／復原 |
| 只把 DB 改成 gzip 繼續入 Git | 可降低每個新檔案大小，但不消除歷史累積，也須修改所有 DB 消費端 | 可作原型對照，不視為長期容量解法 |
| Git LFS | Git 只存指標；每次 DB 新版本與下載皆有額度成本，還有 Pages 相容性問題 | 不直接套用於目前網站 repo |
| 拆表、裁切歷史或改 schema | 會擴大研究查詢、first-seen、正式 OOS 快照及重建的相容性風險 | 本次不做，不為節省容量刪掉證據 |

LFS 每個新版按整個檔案計入儲存，Actions 下載也計入擁有者頻寬；尚未查驗本帳號額度、
預算和實際月下載量，故不提供成本估計或啟用計費。
[Git LFS 計費契約](https://docs.github.com/en/billing/concepts/product-billing/git-lfs)
GitHub 文件也明示 LFS 不支援 Pages sites；即使 DB 僅在建置時使用，仍須另測
checkout／建置／部署流程，不能由「最後只服務 HTML」推定已相容。
[Git LFS 與 Pages 限制](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage)

## 下一階段的驗收條件

1. 在 `tmp/` 或隔離分支使用固定 commit 的副本，保留原檔 SHA、資料日、schema 版本、
   壓縮檔長度與 SHA。gzip 復原必須逐 byte 等於原檔；WAL 模式先取得一致的獨立快照，
   不單獨複製主 DB。
2. 驗證缺檔、截斷、錯誤 SHA、下載中斷與舊 manifest 不會覆蓋可用 DB；先下載並驗證
   到暫存檔，再原子切換。manifest 不得先指向未成功發布的 artifact。
3. 驗證全新 checkout 與乾淨 CI 能還原指定版本；完整 raw audit、ranking／OOS audit、
   測試及 dashboard 重建皆通過，既有 as-seen archive bytes 不變。
4. 為每日 checkpoint、final pass、週報與財報 writer 設計同一版本契約；所有寫 main
   流程保留 `repo-main-writer`、`queue: max`、開跑時 checkout 最新 main，衝突標紅。
   驗收 final commit 與 Pages latest build SHA 一致。
5. 演練回退到上一個可用版本及離線復原，明訂 artifact 保留政策；確認外部服務權限、
   配額／費用後才提出正式切換。歷史 Git 清理另作獨立決策，不隨遷移一起執行。

## 重跑方式與退出碼

```text
python scripts/audit_storage.py
python scripts/audit_storage.py --gzip-probe --json
python -m unittest tests.test_audit_storage -v
```

預設只讀正式 DB；`--db` 可指定另一個既有檔案。壓縮試算只用記憶體，不產生壓縮檔，
不執行 VACUUM、不重建索引。`dbstat` 不支援時明示警告，其他 SQLite 錯誤仍失敗；
使用 `dbstat('main')`，同名普通表不能冒充配置統計。DBSTAT 不包括 freelist 等非 btree 頁，
所以不把表合計直接當成整個檔案。[SQLite DBSTAT 契約](https://www.sqlite.org/dbstat.html)

量測前後核對 DB／WAL 雜湊、檔案識別、大小與修改時間；非 WAL 檔的 SQLite 頁數不得
超過實體大小，合法尾端 bytes 則單獨列差額與警告。觀測不一致、gzip 復原不一致或
超過 100 MiB 時回報錯誤；WAL 主檔的
gzip 試算會拒絕執行，避免誤稱完整備份。

- `0`：量測完成，容許 50 MiB 與 `dbstat` 能力警告。
- `1`：報告含錯誤，不能當成有效容量／復原證據。
- `2`：IO 或 SQLite 執行失敗；不存在的 DB 不會被新建。

建議每週與財報大量更新後執行一次；本次**沒有新增排程或每日阻斷閘門**。
這個工具不取代原始資料完整性、SQLite integrity 或 OOS 品質稽核。

本機預設環境通過 12 項測試，另由獨立 reviewer 重現並驗證原子替換、同名表、
合法尾端 bytes 與 WAL 邊界；初次誤報紀錄與修正後結果分別保留在
`tmp/storage_review_2026-08-29/`。測試／fixture 計數是工作覆蓋，不是統計樣本。
