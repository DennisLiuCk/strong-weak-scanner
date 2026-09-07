# 資料庫容量與復原進度 · 2026-09-07

本機量測與固定版本的跨 runner 還原演練已完成；正式資料庫仍由 Git 保存。

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

## 遠端復原驗收

使用者明確同意後，既有 `db-artifact-smoke` 的
[run 34072575089](https://github.com/DennisLiuCk/strong-weak-scanner/actions/runs/34072575089)
於台灣 2026-09-07 09:18–09:19 成功完成；attempt 1，來源固定為上述 `fd4a4ab`。
publish 與 restore 是兩個獨立 runner job，權限為 `contents: read`。

- 環境：Ubuntu 24.04.4、Python 3.12.14、SQLite 3.45.1、stdout UTF-8，
  `utf8_mode=0`、未設 `PYTHONUTF8`。
- manifest 可信 pin 取自 publish 建立紀錄與 job output：
  `b9bfdc987360ad09f9ce4e92dee6ee0be6056b4de364b673939c29437212c196`。
- gzip SHA-256：`7e4e3111cce17705ef6b8703de45816bf9325214c4226c75f6487e52e886a14b`；
  長度與本機量測相同，復原後 DB SHA 與 60,551,168 bytes 原檔逐 byte 相同。
- DB artifact ID `10000938716`；下載容器的 SHA-256 為
  `8eca3aafd3e4348cfa8008d3b1c3a3bf1eadba7e4bd42c7142d59cbb30858779`，
  20,388,486 bytes（包含 gzip、manifest 與容器封裝）。實際到期時間為
  `2026-09-08T01:18:20Z`，符合一天原型保留設定。
- raw、ranking/OOS、validate 與基準版本完整 643 項測試均 exit 0；兩個 DB 建出的
  首頁與研究頁 SHA 各自相同，正式 DB 與 43 份 archive 保持不變。
- 原始表稽核保留一項警告：法人表 74 筆既有 grid 外資料未納入完整度；舊版 D 視角
  仍為 16/121，保留 `partial_coverage`。演練成功只證明既有版本可復原，不代表警告消失。
- 此次使用舊 ranking spec `e51579e313c6e3fbac9cb180539ce1d0cb4f67f06ee7e56dc5c2756b998a72f9`
  的既有正式快照；不把這次通過當作 9/7 新 spec 的正式 OOS 證據。

原始驗收 JSON 保存於 [db_artifact_smoke_2026-09-07.json](db_artifact_smoke_2026-09-07.json)。
演練 log artifact ID 為 `10000954164`，到期時間 `2026-09-08T01:19:15Z`；永久保留上述
commit、pin 與驗收紀錄。這次完成單一固定版本復原，未驗收舊版切換、長期後端、保留清理
或正式 writer/reader 遷移；後續仍按 runbook 的容量門檻處理。
