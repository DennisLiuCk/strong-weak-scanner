@echo off
REM 雙擊此檔:抓下雲端最新資料 → 用預設瀏覽器開儀表板。純本機、不外流。
cd /d "%~dp0"
echo 抓取雲端最新資料中...
git pull --quiet
if errorlevel 1 echo (git pull 失敗,仍以本機現有版本開啟)
start "" "index.html"
