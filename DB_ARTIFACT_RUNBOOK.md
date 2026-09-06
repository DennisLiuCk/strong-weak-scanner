# DB artifact 隔離演練

這是儲存遷移前的復原原型。正式 `data/findmind.db` 仍隨 Git 入庫，所有每日、財報與週報
writer 維持原流程；本工具沒有正式切換開關、不連外、不啟用 LFS 或其他儲存後端。

## 版本與安全邊界

- 建立來源必須是完整 40 碼 commit；直接讀該 commit 的 `data/findmind.db` blob，
  不讀可能正被 Actions、fetch 或人工分析變更的工作樹 DB。Git 物件查詢停用 replace refs，
  避免本地替代物件借用舊 SHA 的標籤。
- manifest 保存原檔／gzip 長度與 SHA-256、來源 commit、SQLite schema/user version、
  schema hash，以及 price／market／daily_scores 各自的最新日期。checkpoint 不假裝 final。
- gzip 完成後才在 staging 寫 manifest，供實際復原驗證使用；驗證成功後，本地以
  同檔案系統 rename 一次發布整包。指定輸出目錄必須尚不存在，不能覆蓋已發布版本。
- 復原同時要求 `--expected-commit` 與 `--expected-manifest-sha256`。這兩個 pin 必須來自
  可信的建立紀錄、受控版本或同次 Actions job output；**不可只對剛下載的 manifest
  自行算 SHA 再把它當可信 pin**。SHA 提供完整性，不是簽章或來源身分認證。
- 先驗 manifest 與 gzip，再於目的地同檔案系統解壓至暫存檔；限制解壓長度，核對原檔 SHA、
  SQLite integrity、schema 與日期，最後才以 `os.replace` 切換。可用 DB 不因下載缺檔、
  截斷、錯誤版本、錯誤 SHA 或解壓／切換失敗而被先刪除。
- 禁止寫正式 `data/`、正式 DB 的 symlink／hardlink 別名，以及 artifact 自身。
  WAL 檔頭、WAL／SHM／journal sidecar 都直接拒絕；若要支援 WAL，須另設一致快照流程。
  檔頭版本 2 的定義見 [SQLite 檔案格式](https://www.sqlite.org/fileformat.html#file_format_version_numbers)。
- 這些是誤用防護，**不是跨程序鎖、ACL 安全邊界或斷電持久性保證**。目的地必須是無其他
  reader／writer 使用的離線副本；目前不支援 live DB restore。輸入檔上限為 1 GiB。
  SQLite 讀取一律經 `db_ro.connect()`；輸出檔案本來就會寫入，不能稱整個演練唯讀。

## 本地操作

先 `git pull`，保留一個確定的 commit。以下尖括號是需要替換的值，不是可直接執行的參數。
所有輸出使用已忽略的 `tmp/`；Python 使用專案規定的 `python`。

```text
python scripts/db_artifact.py create --source-commit <完整40碼commit> --output-dir tmp/db-artifacts/version-a
python scripts/db_artifact.py restore --manifest tmp/db-artifacts/version-a/manifest.json --expected-commit <同一commit> --expected-manifest-sha256 <建立時回傳的SHA256> --destination tmp/db-restored/findmind.db
python scripts/check_db_artifact.py --manifest tmp/db-artifacts/version-a/manifest.json --expected-commit <目前checkout的commit> --expected-manifest-sha256 <建立時回傳的SHA256> --output-dir tmp/db-checks/version-a
python -m unittest tests.test_db_artifact -v
```

create／restore 成功輸出 JSON、exit 0；IO、格式、版本、SHA 或 SQLite 檢查失敗 exit 2。
check 的輸出目錄也必須不存在。它不修改來源 DB／archive，會：

1. 驗證 checkout HEAD 與 commit pin 相同，復原副本並與來源逐 byte 比較。
2. 對復原副本執行 raw audit、ranking／OOS audit 與 validate（報告只寫入該輸出目錄）。
3. 執行完整 unittest；此步測試 fixtures／程式契約，不宣稱每個測試都使用復原 DB。
4. 分別以原始 DB 與復原副本建置 HTML，兩次皆輸出到隔離目錄並使用 archive 副本。
   核對兩份 HTML 一致、既有 archive bytes 不變、正式 DB／archive 前後 SHA 相同。
5. 保存 `verification.json` 與每項 `.log`；警告必須讀原始 log，不把 exit 0 解讀成零警告。

若來源日期尚無正式 OOS 快照，`--require-current-snapshot` 會使演練失敗，不能因此繞過
正式 final gate。請改用已完成 final 的 commit。

## GitHub Actions 演練

`db-artifact-smoke` **只有 workflow_dispatch，沒有 cron 或 push trigger**，權限僅
`contents: read`；不屬於 main writer，也不改動既有 `repo-main-writer` concurrency 契約。

- publish job checkout 觸發當下的固定 SHA，建立、驗證後上傳 gzip＋manifest。
- restore job 使用全新 runner，checkout 同一 SHA，依 publish 回傳的不可變 artifact ID
  下載；manifest pin 另由 job output 傳入，並把下載 digest mismatch 設為 error。
- 原型包與演練 log 均只保留 **1 天**，不重複上傳解壓 DB 或 HTML。失敗會標紅。
  每次重跑使用 run attempt 區分 artifact，不覆蓋前次包。

目前使用 [官方 upload-artifact](https://github.com/actions/upload-artifact) 與
[官方 download-artifact](https://github.com/actions/download-artifact) 的 artifact ID、
retention、digest 檢查契約。一般 Actions artifact 有保留期限與帳號配額，
**這不是已選定的長期 DB 分發或備份後端**；本演練未更改付費額度。

## 離線回退與正式遷移前待辦

### 容量與保留的執行門檻

每週驗證 workflow 執行 `audit_storage.py --gzip-probe`，將檔案／頁面容量、SHA 與
壓縮回復結果寫入 job summary。50／100 MiB 是 GitHub 既有單檔警告／限制；下列
75／90 MiB 是本專案預留處理時間的營運門檻，不是平台額外限制，也不估算哪天會到達。

| 正式 DB 容量 | 應完成的工作 |
|---|---|
| 超過 50 MiB | 維持每週容量記錄，完成固定版本遠端復原演練；現行 Git 繼續保存 DB |
| 達 75 MiB | 必須具備成功的遠端復原與舊版回退紀錄，完成長期後端權限／配額／成本比較 |
| 達 90 MiB | 將儲存遷移列為最高維運優先；先交付經驗收的 writer/reader 切換方案，避免拖到平台拒收 |
| 超過 100 MiB | 一般 Git 推送將受單檔限制；不得以刪除歷史、縮減 OOS 或裁切原始資料掩蓋 |

目前仍以 Git 中的每個版本為可重建來源；Actions 演練 artifact 保留 1 天，不調高配額，
也不以尚未執行的演練當作成功備份。正式後端尚未選定前，不自動移除 DB 或啟用清理。

正式遷移方案至少需要下列保留契約，數量是待實作的營運需求，**不是目前已啟用的備份**：

- 完整 final：每日 14 份、每週 8 份、每月 12 份；同一份可同時滿足週／月槽位。
- 未完成 checkpoint：至少保存最近兩個已驗證版本，並與 final 標籤分開。
- commit、manifest pin、DB SHA、artifact locator、來源資料日與驗收紀錄另行長期保存；
  至少兩個已驗證的 final 包可用，才有資格回收較舊的暫存包。
- 保留一份獨立位置的離線完整包與可信 pin；每月在乾淨環境驗完整復原，每季實際驗舊版回退。
- 所有保留期限、費用與存取範圍須在選定後端後實測，不能把 Actions 的一天原型設定直接當長期方案。

新 spec 尚無正式日更的 commit 不適合跑 `--require-current-snapshot`；演練應選既有
已完成 final 的固定版本，或等新版本的第一個真實 final。不能為讓演練變綠而補造舊日快照。

回退不是忽略版本檢查。保留前一版本的完整包，以及獨立保存的 commit／manifest pin，
明確指定舊版兩個 pin 復原到離線副本，完成稽核後才討論正式切換。
沒有網路也能執行 restore；若包已到期且本地未留存，目前仍可從原 Git commit 重新建立。
這個保障來自 **DB 尚在 Git**，不能推論移出 Git 後也有同樣保障。

正式遷移另需完成：長期後端權限／配額／費用、版本保留與災難復原、checkpoint/final/
財報/週報所有 writer 的共同版本契約、多 writer 與中途故障演練，以及最終 Pages commit
一致性驗收。不得在這個原型中刪 DB、重寫 Git 歷史、修改 OOS／first-seen 或裁切 archive。
