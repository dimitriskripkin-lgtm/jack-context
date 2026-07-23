# JACK LIVE-KONTEXT (auto, 2026-07-23T03:24:40.374361)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-07-23T03:24:40.365196

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
- Dima ist LKW-Fahrer mit Sprinter Kühlkoffer bei Dalhoff Feinkost in Achim (Nachtschicht).
- Dima ist Hobby-Programmierer.
- Dima ist aus Russland nach Deutschland migriert, Baujahr ca. 1996.
- Dima ist Einzelkind.
- JACK ist ein autonomes, lokales AI-OS auf Dimas Honor Magic8 Pro.
- JACK nutzt Gemini als Gehirn (API-Calls).
- JACK hat ein lokales Gedächtnis in SQLite.
- JACK soll sich selbst lernen und verbessern.
- JACK steht unter Dimas voller Kontrolle.
- JACK speichert alle Fragen und Antworten mit Zeitstempel im Gedächtnis.
- Dima hat KEINEN Hund (Rex war nur ein Test).
- JACK hat KEINEN direkten Shell- oder Dateizugriff über den Chat.
- Dima testet das Gedächtnis.
- Dima hat auf Xiaomi in Termux sshd eingegeben.
- Dima hat eine autobiographische Information hochgeladen, die JACK durchsuchen soll.
- Dima hat den Befehl gegeben, ins Verzeichnis `~/jack/titan_legacy` zu wechseln und eine Datei von GitHub zu laden.

## Aktive Module (55)
- jack_agent.py
- jack_android.py
- jack_approval.py
- jack_audit.py
- jack_autonomous.py
- jack_briefing.py
- jack_budget.py
- jack_bug_fixer.py
- jack_claude.py
- jack_code_writer.py
- jack_coder.py
- jack_config.py
- jack_consolidate.py
- jack_cortex.py
- jack_gemini_bridge.py
- jack_handshake_gen.py
- jack_hey.py
- jack_improve.py
- jack_learn.py
- jack_log.py
- jack_math.py
- jack_memory.py
- jack_memory_engine.py
- jack_memory_maintenance.py
- jack_node_alpha.py
- jack_operator.py
- jack_oracle.py
- jack_patch.py
- jack_personality.py
- jack_publish.py
- jack_radar.py
- jack_screen_tracker.py
- jack_self_improve.py
- jack_sensors.py
- jack_skills.py
- jack_snapshot.py
- jack_talk.py
- jack_telegram.py
- jack_v2.py
- jack_vecdb.py
- jack_vinted_radar.py
- jack_voice.py
- jack_voice_el.py
- jack_voice_processor.py
- jack_write.py
- jack_xiaomi.py
- jack_xiaomi_cmd.py
- kortex_controller.py
- kortex_memory.py
- kortex_profile_updater.py
- kortex_profiler.py
- kortex_sensor_daemon.py
- quick_bridge.py
- test_jack_approval.py
- voice_service_v2.py

## System-Status
- Offene Fehler: 4
- Erinnerungen: 140
- Dienste:
run: jack_cortex: (pid 4424) 3843s
run: jack_telegram: (pid 9882) 425s
run: jack_autolearn: (pid 7339) 146932s
run: ollama: (pid 7342) 146932s

## Letzte Aenderungen
f3d1cdd Oracle: deutsche Aliase + Ergebnis-Stack (letzte 5)
2e72523 oracle_result bugfix: json import
b494b09 oracle bugfix: import vor json.dumps gezogen
dcbaff7 oracle bugfix: json import im block
bc451eb Telegram: /oracle + /oracle_result
f5c4768 Security: Flask von 0.0.0.0 auf 127.0.0.1 (kein offener Endpoint mehr)
e374319 7 Dienste: jack_oracle live, Meilenstein 2026-07-22
9de06fc jack_oracle: bidirektionaler Claude<->JACK Kanal via GitHub, Live-Test erfolgreich (free -h)
0955315 Prompt: Titan-Lektionen still integriert
8e20a4e titan_legacy: falsche context.md entfernt, Ordner bleibt leer bis bewusste Entscheidung
ab0073f titan_legacy: Kern-DNA gesichert (Persona+Anchor+Evolution)
66d036b titan_legacy: Ordner angelegt, Ingest folgt
a410265 titan_legacy: Ordner vorbereitet fuer Kontext-Ingest
5e7e277 Dima-Profil v1: persoenlicher Kontext fuer JACK und alle KI-Partner
4850d0d Prompt-Fix: JACK kennt jetzt ehrlich seine eigene Architektur (Gemini als Werkzeug)

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-07-21 11:00:00] CONSOLIDATE | Session gespeichert: 10 Logs, 0 Zugriffe
[2026-07-22 03:55:50] PROFIL-UPDATE | 2 neue Eintraege in kortex_profile.json
[2026-07-22 04:29:53] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-22 04:30:02] WAECHTER-AUDIT | woechentlich verschickt
[2026-07-22 06:00:00] MEMORY-MAINTENANCE | 10 Eintraege als 'stale' markiert | Gesamt: 41 Eintraege | Stale: 10
[2026-07-22 10:01:09] PROFIL-UPDATE | 6 neue Eintraege in kortex_profile.json
[2026-07-22 10:40:42] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-07-22 10:40:42] SELF-IMPROVE | Tagescheck abgeschlossen
[2026-07-22 11:00:00] CONSOLIDATE | Session gespeichert: 10 Logs, 0 Zugriffe
[2026-07-22 12:12:25] PROFIL-UPDATE | 2 neue Eintraege in kortex_profile.json
[2026-07-22 14:53:25] ORACLE-EINGANG | init: echo JACK_ORACLE_READY
[2026-07-22 14:59:04] ORACLE-EINGANG | test-001: free -h
[2026-07-22 16:26:04] ORACLE-EINGANG | live-001: sv status jack_cortex jack_telegram jack_autolearn jack_publisher jack_waechter
[2026-07-23 02:22:08] DATEI-SCHREIBEN | jack_cmd.json | 169 Zeichen
[2026-07-23 02:44:09] ORACLE-EINGANG | tg-17847: free -h
[2026-07-23 02:54:13] ORACLE-EINGANG | tg-17847: df -h
[2026-07-23 03:04:40] ORACLE-EINGANG | tg-17847: sv status jack_cortex jack_telegram jack_autolearn jack_publisher jack_waechter
[2026-07-23 03:17:43] ORACLE-EINGANG | tg-17847: sv status jack_cortex jack_telegram jack_autolearn jack_publisher jack_waechter
[2026-07-23 03:19:45] ORACLE-EINGANG | tg-17847: sv status jack_cortex jack_telegram jack_autolearn jack_publisher jack_waechter
[2026-07-23 03:20:01] PROFIL-UPDATE | 2 neue Eintraege in kortex_profile.json

## Budget heute
Heute: Text 3/300 | Vision 0/40 | Tokens 7398