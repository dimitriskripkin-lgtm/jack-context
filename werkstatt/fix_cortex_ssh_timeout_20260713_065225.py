#!/usr/bin/env python3
"""
AUTO-FIX: fix_cortex_ssh_timeout_20260713_065225
Generiert: 2026-07-13T06:52:25.805003
Modul: jack_cortex.py
Beschreibung: SSH-Timeout zu kurz. Vorschlag: Timeout von 10 auf 20 Sekunden erhoehen.
ACHTUNG: Nur ausfuehren nach Dimas Bestaetigung via Telegram.
"""
import shutil, py_compile, os

quell = "/data/data/com.termux/files/home/jack/jack_cortex.py"
bak = quell + ".bak_autofix"
shutil.copy2(quell, bak)
print(f"Backup: {bak}")

content = open(quell).read()
if "timeout=10" not in content:
    print("FEHLER: Anker nicht gefunden. Abbruch.")
else:
    content = content.replace("timeout=10", "timeout=20", 1)
    open(quell, "w").write(content)
    try:
        py_compile.compile(quell, doraise=True)
        print("OK: Fix eingespielt und Syntax geprueft.")
    except Exception as e:
        shutil.copy2(bak, quell)
        print(f"SYNTAX-FEHLER: {e} — Rollback!")
