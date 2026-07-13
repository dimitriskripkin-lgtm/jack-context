#!/usr/bin/env python3
"""
AUTO-FIX: fix_cortex_ssh_timeout_20260713_071108
Generiert: 2026-07-13T07:11:08.496359
Modul: jack_cortex.py
Beschreibung: Xiaomi SSH wiederholt nicht erreichbar. WiFi-Recovery-Timeout erhoehen.
ACHTUNG: Nur ausfuehren nach Dimas Bestaetigung via Telegram.
"""
import shutil, py_compile, os

quell = "/data/data/com.termux/files/home/jack/jack_cortex.py"
bak = quell + ".bak_autofix"
shutil.copy2(quell, bak)
print(f"Backup: {bak}")

content = open(quell).read()
if "capture_output=True, text=True, timeout=15" not in content:
    print("FEHLER: Anker nicht gefunden. Abbruch.")
else:
    content = content.replace("capture_output=True, text=True, timeout=15", "capture_output=True, text=True, timeout=25", 1)
    open(quell, "w").write(content)
    try:
        py_compile.compile(quell, doraise=True)
        print("OK: Fix eingespielt und Syntax geprueft.")
    except Exception as e:
        shutil.copy2(bak, quell)
        print(f"SYNTAX-FEHLER: {e} — Rollback!")
