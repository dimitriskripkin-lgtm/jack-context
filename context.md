# JACK LIVE-KONTEXT (auto, 2026-07-15T00:28:05.440457)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-07-15T00:28:05.433560

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
- Dima hat KEINEN Hund.
- JACK hat KEINEN direkten Shell- oder Dateizugriff über den Chat.
- JACK's Entwickler Dima hat das Host-Gerät als Honor Magic8 Pro (nicht Honor 8) korrigiert.
- JACK hat Telegram-Commands aktualisiert, committed und gepusht.

## Aktive Module (49)
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
- voice_service_v2.py

## System-Status
- Offene Fehler: 1
- Erinnerungen: 121
- Dienste:
run: jack_cortex: (pid 21793) 116582s
run: jack_telegram: (pid 23977) 116334s
run: jack_autolearn: (pid 20689) 343086s
run: ollama: (pid 20694) 343086s

## Letzte Aenderungen
e213119 chore: Karpathy-Guidelines in AGENTS.md integriert
6e0e880 feat: voice_poller.sh + record_trigger.sh - Mikrofon-Trigger fuer Xiaomi
7d10661 feat: voice_service_v2 non-blocking funktioniert - Stabilitaets-Check fuer M4A
37f5dec feat: voice_service_v2 Poller-Ansatz - non-blocking Aufnahme funktioniert
2602703 feat: send_webapp + /radar_ergebnisse Telegram-Button
cf8bb21 feat: WebApp-Routen /radar/webapp und /radar/kleinanzeigen
08306dd fix: Xiaomi IP 10.234->10.244 in jack_config.py
9cfeba1 chore: Xiaomi IP auf 10.244.147.131 aktualisiert
9e6b605 feat: /radar_an /radar_aus /vinted_an /vinted_aus /radar_intervall /vinted_intervall
8459198 chore: Config-Dateien mit Tokens aus Git entfernt
859f8bd feat: jack_vinted_radar.py - Vinted Radar live, 96 Items gefunden
592e323 feat: Radar Parser JSON-LD, 20 Treffer live - vorerst deaktiviert
529f84c feat: jack_radar.py - Kleinanzeigen Radar Grundgeruest
c7a1a38 feat: FTS5 Zeitdaempfung - Score sinkt nach 14 Tagen ohne Abruf
0da8631 fix: Session-Text auf 300 Zeichen erweitert

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.234.166.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-07-13 08:19:11] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-13 09:02:29] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-13 09:36:57] REJECT-FIX-BUTTON | test abgelehnt
[2026-07-13 10:43:50] MEMORY-MAINTENANCE | Gesamt: 10 Eintraege | Stale: 0
[2026-07-13 10:46:16] CONSOLIDATE | Session gespeichert: 10 Logs, 3 Zugriffe
[2026-07-13 11:00:00] CONSOLIDATE | Session gespeichert: 10 Logs, 4 Zugriffe
[2026-07-13 11:59:44] RADAR | 0 neue Anzeigen gefunden
[2026-07-13 12:02:00] RADAR | 0 neue Anzeigen gefunden
[2026-07-13 12:03:41] RADAR | 20 neue Anzeigen gefunden
[2026-07-13 21:03:43] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-14 01:03:50] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-14 06:00:00] MEMORY-MAINTENANCE | Gesamt: 15 Eintraege | Stale: 0
[2026-07-14 07:04:01] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-14 07:16:40] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-07-14 07:16:40] SELF-IMPROVE | Tagescheck abgeschlossen
[2026-07-14 09:04:04] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-14 11:00:01] CONSOLIDATE | Session gespeichert: 10 Logs, 0 Zugriffe
[2026-07-14 11:04:06] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-14 17:04:29] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-14 23:04:37] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json

## Budget heute
Heute: Text 0/300 | Vision 0/40 | Tokens 0