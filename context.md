# JACK LIVE-KONTEXT (auto, 2026-07-17T22:32:36.707418)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-07-17T22:32:36.696573

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
- Dima ist LKW-Fahrer mit Sprinter Kühlkoffer bei Dalhoff Feinkost in Achim (Nachtschicht).
- Dima ist Hobby-Programmierer.
- Dima nutzt Gemini Plus und Claude.ai.
- JACK ist ein autonomes, lokales AI-OS.
- JACK läuft auf einem Honor Magic8 Pro mit Termux.
- JACK nutzt Gemini 2.5 Flash (Lite) als Hauptdenker.
- JACK soll sich selbst lernen und verbessern.
- JACK steht unter Dimas voller Kontrolle.
- JACK verwendet `jack_learn.py` als Lerner.
- JACK nutzt ein Xiaomi 11T Pro als Slave-Gerät via SSH.
- JACK's kostenlose KI-Modelle haben Tageslimits.
- JACK's Chef-KI 'Claude Code' ist ein read-only Berater.
- JACK hat Fähigkeiten wie Text- und Sprachchat, sicheres Code schreiben, autonomes Handeln und Selbstverbesserung.
- JACK nutzt `jack_waechter` für regelbasierte Überwachung und Neustarts.
- JACK's Konfiguration und Logs werden in einem öffentlichen Repo (`jack-context`) geteilt.
- Dima hat KEINEN Hund (Rex war nur ein Test).
- Dima ist LKW-Fahrer mit Sprinter Kuehlkoffer, KEIN Fernfahrer.
- JACK hat KEINEN direkten Shell- oder Dateizugriff über den Chat.
- JACK hat Telegram-Commands aktualisiert, committed und gepusht.

## Aktive Module (53)
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
- jack_improve.py
- jack_learn.py
- jack_log.py
- jack_math.py
- jack_memory.py
- jack_memory_engine.py
- jack_memory_maintenance.py
- jack_node_alpha.py
- jack_operator.py
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
- Erinnerungen: 122
- Dienste:
run: jack_cortex: (pid 21793) 368853s
run: jack_telegram: (pid 11956) 122509s
run: jack_autolearn: (pid 20689) 595357s
run: ollama: (pid 20694) 595357s

## Letzte Aenderungen
c081ad6 chore: runtime files
a7ea6e2 Merge branch 'master' of https://github.com/dimitriskripkin-lgtm/jack-core
3dcb140 fix: /xiaomi handler + telegram fixes
0ed075c feat: Node Alpha Lern-System, Skill-Generator gefixt
340dba9 feat: jack_xiaomi_cmd - Telegram /xiaomi Loop komplett, ADB tap funktioniert
7299e40 feat: jack_node_alpha daemon + ADB tap funktioniert autonom
6435547 fix: MIUI uiautomator via Datei, Gemini 2.5-flash-lite, Quote-Strip
f52ad49 feat: jack_android
a84c96e fix: IP 10.234.166.x -> 10.244.147.x in allen Modulen
6913a0a feat: Circuit Breaker in jack_agent - Abbruch nach 3x gleichem Fehler
e213119 chore: Karpathy-Guidelines in AGENTS.md integriert
6e0e880 feat: voice_poller.sh + record_trigger.sh - Mikrofon-Trigger fuer Xiaomi
7d10661 feat: voice_service_v2 non-blocking funktioniert - Stabilitaets-Check fuer M4A
37f5dec feat: voice_service_v2 Poller-Ansatz - non-blocking Aufnahme funktioniert
2602703 feat: send_webapp + /radar_ergebnisse Telegram-Button

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-07-14 07:16:40] SELF-IMPROVE | Tagescheck abgeschlossen
[2026-07-14 09:04:04] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-14 11:00:01] CONSOLIDATE | Session gespeichert: 10 Logs, 0 Zugriffe
[2026-07-14 11:04:06] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-14 17:04:29] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-14 23:04:37] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-15 06:00:01] MEMORY-MAINTENANCE | Gesamt: 21 Eintraege | Stale: 0
[2026-07-15 07:20:13] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-07-15 07:20:13] SELF-IMPROVE | Tagescheck abgeschlossen
[2026-07-15 11:00:00] CONSOLIDATE | Session gespeichert: 10 Logs, 0 Zugriffe
[2026-07-16 06:00:00] MEMORY-MAINTENANCE | Gesamt: 23 Eintraege | Stale: 0
[2026-07-16 07:23:42] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-07-16 07:23:42] SELF-IMPROVE | Tagescheck abgeschlossen
[2026-07-16 11:00:00] CONSOLIDATE | Session gespeichert: 10 Logs, 0 Zugriffe
[2026-07-16 11:05:30] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-16 13:05:35] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-17 06:00:00] MEMORY-MAINTENANCE | Gesamt: 28 Eintraege | Stale: 0
[2026-07-17 07:27:16] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-07-17 07:27:16] SELF-IMPROVE | Tagescheck abgeschlossen
[2026-07-17 11:00:00] CONSOLIDATE | Session gespeichert: 10 Logs, 0 Zugriffe

## Budget heute
Heute: Text 13/300 | Vision 0/40 | Tokens 63345