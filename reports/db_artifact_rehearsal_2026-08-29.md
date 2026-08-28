# 固定版本 DB artifact 復原演練 — 2026-08-29

## 決定

保留正式 DB 入 Git；新增離線 gzip＋manifest 原型及手動 CI 演練。沒有正式遷移、
刪資料、重寫 Git 歷史、啟用 LFS 或增加付費額度。操作契約見
[DB artifact runbook](../DB_ARTIFACT_RUNBOOK.md)。

## 本機實測

- DB 基線：`1f51c61c94d3eb366600b4f37617cac0d15ca837` 的 Git blob；price、market、
  daily_scores 最新日期均為 2026-08-28。程式使用本輪待提交版本，不宣稱舊 commit 已含原型。
- 環境：macOS 26.5.2 arm64、`python` 3.11.11、SQLite 3.51.0、stdout UTF-8、
  `utf8_mode=0`，未設定 `PYTHONUTF8`／`PYTHONIOENCODING`。
- 範圍：一個完整 DB、確定性 bytes／schema／HTML 比對與測試 fixtures；不是抽樣，
  SE／t 不適用。不做績效、未來檔案成長或遠端帳號儲存費用推估。

| 驗收 | 實際結果 |
|---|---|
| 原始 bytes | 58,114,048 |
| gzip level 6、mtime 0 | 19,462,262 bytes |
| 復原原檔 SHA-256 | `2a5aeee10bf7619a3bd497d2a071ad27a451441298042b1a29af38f0f2945a20`，另逐 byte 相等 |
| gzip SHA-256 | `c9a29346115528db396cba13e311c6d2b9e79e07243be2f16874425f19dbc1b3` |
| manifest SHA-256 | `a7994bc45278b72811a7ad42aef27c890eeee29f367daaf9c8f53b23bb92d625` |
| SQLite | integrity ok；schema_version 1418、user_version 0；schema hash 完全一致 |
| Raw audit | exit 0；既有 74 筆 spine 外 inst 警告保留，沒有將警告改成缺口已修 |
| Ranking／OOS audit | exit 0、hard_errors 空；D 覆蓋 117/121 的既有警告保留 |
| validate | exit 0，輸出只寫入隔離目錄；未改正式 reports 或宣稱策略有效 |
| 完整 unittest | 642 項通過，含新增 22 項 artifact 測試 |
| HTML | 原 DB 與復原副本產生的 index／research 逐檔 SHA 相同 |
| 保護資料 | 正式 DB、archive 所有檔案前後 SHA 與清單相同；副本 DB 未被 consumer 修改 |

本輪檢核版程式 SHA：`db_artifact.py` 為
`1d2b9b84260c141ca0cab340824b4c5b8f5837243f6470820f881304fc87ad0d`，
`check_db_artifact.py` 為
`df44d50806e422e759831331af472ae96025871e1b2fa1bdb535413db9b4cf4f`。
原始 JSON 與 log 位於 `tmp/db_artifact_2026-08-29/check_final_1f51c61/`，不進 Git。

## 已驗證的故障與更正

缺檔、截斷、錯誤 SHA、過期 commit、錯誤 schema／資料日、路徑穿越、重複 JSON key、
錯誤 UTF-8／deflate、WAL、symlink／hardlink、寫入中斷、原子切換失敗、驗證期間檔案
替換與舊版回退均有測試。既有離線 DB 不先刪除；未成功的包也不發布可見 manifest。

第一輪 WAL fixture 發現唯讀 SQLite 開啟可能仍需輔助檔，已在開啟前依檔頭拒絕 WAL。
獨立 reviewer 另實際重現 Git replace refs 可讓舊 SHA 讀到替代 DB 的問題；物件查詢已加入
`--no-replace-objects`，commit／blob 兩類替換皆重測。超過 1 GiB 也會在抽出 blob 前拒絕。

不同 reviewer 在固定程式 SHA 上重跑 22 項測試，並以另外 8 項小型故障探針核對；
其中 helper wiring 使用真實小型復原與 consumer 路徑 spy，不能冒充完整正式 DB 稽核。
本報告上表的完整 DB／HTML 結果來自 root 的實際執行，兩者分開。
獨立重現及修正後記錄留在 `tmp/research_work_2026-08-29/db_artifact_review/`。

## 遠端驗收與下一階段

本機結果不替代遠端驗收。手動 `db-artifact-smoke` 的 publish／restore 是兩個獨立
runner，依固定 commit、不可變 artifact ID 與另一通道傳遞的 manifest pin 驗證。
原型 artifact 只保留一天，不是長期備份政策。遠端結果須以實際 Actions run 補記。

正式切換前仍需決定長期後端、保留／離線災難復原政策、權限與配額費用，並整合
checkpoint／final／財報／週報的共同版本契約。所有 main writer 的排隊與衝突標紅、
final commit 與 Pages SHA 一致性仍是必驗條件；這次沒有改動它們。
