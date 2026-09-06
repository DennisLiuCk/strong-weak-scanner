# 資料庫容量與復原進度 · 2026-09-07

本機量測完成，遠端演練待授權；沒有切換正式儲存方式。

- 本機執行環境：Windows 11 10.0.26200、Python 3.12.10、SQLite 3.49.1、預設 stdout cp950。
- 基準：遠端 main `fd4a4ab2b9741b895483675d6be917f05eb3f1a1` 的已發布 9/4 DB。
- 原檔 60,551,168 bytes（57.74609375 MiB）；頁面 14,783 × 4,096 bytes 獨立吻合。
- gzip level 6／mtime 0：20,387,195 bytes；第二條獨立 `gzip.compress` 路徑吻合，
  解壓 bytes 與原檔逐 byte 相同。
- 原檔及復原 SHA-256 均為
  `ca7e8fc90305b648838d75843df729e0d7006f7734fb9ecfb77668a5652823e1`。
- 完整檔案量測與確定性比較，非抽樣；SE／t 不適用，不推估成長速度或剩餘可用天數。
- 本機 SQLite 未提供 dbstat，無逐表配置明細；檔案與頁數量測不受此限制。

GitHub 一般 Git 單檔超過 50 MiB 會警告、超過 100 MiB 受限制，見
[GitHub 官方文件](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)。
每週 workflow 新增容量與 gzip 回復普查；75／90 MiB 營運門檻及正式遷移保留需求見
[DB artifact runbook](../DB_ARTIFACT_RUNBOOK.md)。

2026-09-07 嘗試觸發既有 `db-artifact-smoke` 遭自動授權審核拒絕：完整 SQLite 上傳至
Actions artifact 的資料傳輸尚需使用者明確同意。沒有改用其他上傳途徑，也沒有產生新的
run 或宣稱遠端復原成功。核准後應保存實際 run、兩個 runner 的結果、可信 manifest pin
與 byte／raw／OOS／HTML 驗收；失敗則維持 Git 為正式來源並依原始 log 修復。
