#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""db_ro.py — 唯讀開啟 SQLite 的唯一入口(零第三方依賴)。

**為什麼需要它**(2026-07-26 檢討):那天我對你宣稱「分析全程唯讀」,事後清點發現
15 支分析腳本裡有 **11 支**是用 `sqlite3.connect(DB)` 開正式庫的。db 沒被寫壞是運氣,
不是保證——而「宣稱一個自己沒有強制的性質」正是那天九個錯誤裡反覆出現的形狀。

這支模組把唯讀變成**阻力最小的路徑**,順手擋掉兩個陷阱:

1. `sqlite3.connect("typo.db")` 會**默默建一個空 db**;`mode=ro` 會直接報錯。
   打錯路徑時,前者讓你對著空表分析半小時,後者立刻叫你。
2. 只加 `mode=ro` 仍可能被 `ATTACH`/暫存表繞過;再下 `PRAGMA query_only` 是雙保險。

用法(分析腳本、報告產生器、任何只讀的工具):

    import db_ro
    con = db_ro.connect("data/findmind.db")     # row_factory 預設 sqlite3.Row
"""
import os
import pathlib
import sqlite3


def uri(path):
    """把檔案路徑轉成唯讀 URI。用 as_uri() 處理 Windows 磁碟機與需轉義的字元。"""
    return pathlib.Path(os.path.abspath(path)).as_uri() + "?mode=ro"


def connect(path, row=True):
    """唯讀連線。檔案不存在會拋 sqlite3.OperationalError,而不是無聲建立空 db。"""
    if not os.path.exists(path):
        raise sqlite3.OperationalError(f"資料庫不存在:{path}(唯讀模式不會替你建立)")
    con = sqlite3.connect(uri(path), uri=True)
    con.execute("PRAGMA query_only = 1")     # mode=ro 之外的第二道
    if row:
        con.row_factory = sqlite3.Row
    return con
