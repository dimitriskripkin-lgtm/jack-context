# JACK LIVE-KONTEXT (auto, 2026-07-13T12:52:31.030304)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-07-13T12:52:31.016855

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
- Dima ist LKW-Fahrer mit Sprinter Kuehlkoffer bei Dalhoff Feinkost in Achim (Nachtschicht).
- Dima ist Hobby-Programmierer.
- Dima nutzt Gemini Plus und Claude.ai.
- JACK ist ein autonomes, lokales AI-OS.
- JACK läuft auf einem Honor Magic8 Pro mit Termux.
- JACK nutzt Gemini 2.5 Flash (Lite) als Hauptdenker.
- JACK soll sich selbst lernen und verbessern.
- JACK steht unter Dimas voller Kontrolle.
- JACK wurde am 18. Juni gebaut.
- JACK verwendet `jack_learn.py` als Lerner.
- JACK nutzt ein Xiaomi 11T Pro als Slave-Gerät via SSH.
- JACK's kostenlose KI-Modelle haben Tageslimits.
- JACK's Chef-KI 'Claude Code' ist ein read-only Berater.
- JACK hat Fähigkeiten wie Text- und Sprachchat, sicheres Code schreiben, autonomes Handeln und Selbstverbesserung.
- JACK nutzt `jack_waechter` für regelbasierte Überwachung und Neustarts.
- JACK's Konfiguration und Logs werden in einem öffentlichen Repo (`jack-context`) geteilt.
- Dima hat KEINEN Hund.
- JACK hat KEINEN direkten Shell- oder Dateizugriff über den Chat.
- Dima ist LKW-Fahrer mit Sprinter Kuehlkoffer, KEIN Fernfahrer.

## Aktive Module (48)
- jack_agent.py
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
- jack_improve.py
- jack_learn.py
- jack_log.py
- jack_math.py
- jack_memory.py
- jack_memory_engine.py
- jack_memory_maintenance.py
- jack_operator.py
- jack_patch.py
- jack_personality.py
- jack_publish.py
- jack_radar.py
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
- kortex_controller.py
- kortex_memory.py
- kortex_profile_updater.py
- kortex_profiler.py
- kortex_sensor_daemon.py
- quick_bridge.py
- test_jack_approval.py

## System-Status
- Offene Fehler: 0
- Erinnerungen: 107
- Dienste:
run: jack_cortex: (pid 20695) 214952s
run: jack_telegram: (pid 7791) 9433s
run: jack_autolearn: (pid 20689) 214952s
run: ollama: (pid 20694) 214952s

## Letzte Aenderungen
592e323 feat: Radar Parser JSON-LD, 20 Treffer live - vorerst deaktiviert
529f84c feat: jack_radar.py - Kleinanzeigen Radar Grundgeruest
c7a1a38 feat: FTS5 Zeitdaempfung - Score sinkt nach 14 Tagen ohne Abruf
0da8631 fix: Session-Text auf 300 Zeichen erweitert
efb0b2c feat: Briefing v2 - Akku, Dienste, Sessions, Fehler, Fixes chronologisch
2e90553 feat: jack_consolidate.py - Session-Konsolidierung taeglich 11:00
45fe598 feat: jack_memory_maintenance.py - Stale-Marking taeglich 06:00
f1ca237 feat: Gedaechtnis gehaertet - last_accessed + importance + Relevanz-Score
8d24455 feat: Persona in AGENTS.md und jack_self.json verlinkt
60a03af feat: jack_persona.json - psychologisches Profil fuer JACK und alle KIs
6a19f35 fix: gedaechtnis zeigt 200 Zeichen
9a73924 fix: Status-Button zeigt 150 Zeichen statt 50/80
8f0d666 fix: raw vor audit-Check definiert
d8a74a9 fix: Bot-Name-Suffix bei Commands ignorieren, /gedaechtnis aus Menü funktioniert
7b62d48 chore: negative_patterns.json tracken

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.234.166.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-07-13 06:51:45] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-07-13 06:52:25] SELF-IMPROVE | jack_cortex 1x, fix=fix_cortex_ssh_timeout_20260713_065225
[2026-07-13 07:00:56] APPROVE-FIX | approve_fix_cortex_ssh_timeout_20260713_065225: Backup: /data/data/com.termux/files/home/jack/jack_cortex.py.bak_autofix
FEHLER:
[2026-07-13 07:02:16] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-13 07:11:08] SELF-IMPROVE | jack_cortex 1x, fix=fix_cortex_ssh_timeout_20260713_071108
[2026-07-13 07:12:00] APPROVE-FIX | approve_fix_cortex_ssh_timeout_20260713_071108: Backup: /data/data/com.termux/files/home/jack/jack_cortex.py.bak_autofix
OK: Fix
[2026-07-13 07:15:44] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-13 07:15:50] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-07-13 07:15:50] SELF-IMPROVE | Tagescheck abgeschlossen
[2026-07-13 08:19:11] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-13 09:02:29] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-13 09:36:57] REJECT-FIX-BUTTON | test abgelehnt
[2026-07-13 10:43:50] MEMORY-MAINTENANCE | Gesamt: 10 Eintraege | Stale: 0
[2026-07-13 10:46:16] CONSOLIDATE | Session gespeichert: 10 Logs, 3 Zugriffe
[2026-07-13 11:00:00] CONSOLIDATE | Session gespeichert: 10 Logs, 4 Zugriffe
[2026-07-13 11:59:44] RADAR | 0 neue Anzeigen gefunden
[2026-07-13 12:02:00] RADAR | 0 neue Anzeigen gefunden
[2026-07-13 12:03:41] RADAR | 20 neue Anzeigen gefunden

## Budget heute
Heute: Text 24/300 | Vision 0/40 | Tokens 49706