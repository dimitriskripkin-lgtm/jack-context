# JACK LIVE-KONTEXT (auto, 2026-07-13T05:33:16.341819)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-07-13T05:33:16.333032

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
- Dima ist LKW-Fahrer mit Sprinter Kuehlkoffer, KEIN Fernfahrer

## Aktive Module (42)
- jack_agent.py
- jack_approval.py
- jack_audit.py
- jack_autonomous.py
- jack_budget.py
- jack_bug_fixer.py
- jack_claude.py
- jack_code_writer.py
- jack_coder.py
- jack_config.py
- jack_cortex.py
- jack_gemini_bridge.py
- jack_handshake_gen.py
- jack_improve.py
- jack_learn.py
- jack_log.py
- jack_math.py
- jack_memory.py
- jack_memory_engine.py
- jack_operator.py
- jack_patch.py
- jack_personality.py
- jack_publish.py
- jack_sensors.py
- jack_skills.py
- jack_snapshot.py
- jack_talk.py
- jack_telegram.py
- jack_v2.py
- jack_vecdb.py
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
- Erinnerungen: 104
- Dienste:
run: jack_cortex: (pid 20695) 188597s
run: jack_telegram: (pid 19928) 244s
run: jack_autolearn: (pid 20689) 188597s
run: ollama: (pid 20694) 188597s

## Letzte Aenderungen
7cd021f feat: access_count bei Suche + /status_report Telegram-Befehl
5d8602d feat: kortex_profile_updater.py - Profil wird automatisch nach jedem jack_learn aktualisiert
85a0b3a feat: jack_learn schreibt neue Fakten automatisch in kortex_memory.db
6d29dd5 chore: .last_audit aus Git-Tracking entfernt
47e65e6 chore: Silent-Fail Review abgeschlossen - verbleibende except:pass sind bewusste Fallbacks
1528de5 fix: letzte Silent Fails geloggt, alle except:pass im Repo eliminiert
8d5848b fix: restliche 4 Silent Fails geloggt (jack_publish/bug_fixer/sensors/gemini)
4e2ae04 fix: Silent Fails ausgeraeumt - alle except:pass loggen jetzt nach jack_decisions.log
dcc487f feat: kortex_bridge runit-Service, Bridge startet automatisch nach Reboot
c883aae feat: /merke /suche /gedaechtnis - Gedaechtnis per Telegram live
e5138fe feat: kortex_profile.json v2.0 - strukturiertes Wissen, Profiler schreibt nur sensoren-Block
94b1dcd fix: Shebang-Position + psutil aus Setup entfernt
7fc9e3c feat: kortex_memory.py - semantisches Gedaechtnis mit FTS5, 3 Flask-Routen live
98e2044 Fix: _sec() Token-Parse auf Bot-Logik angeglichen, notify() funktioniert wieder
a35bb6e jack_audit: Gesundheits+Sicherheits-Check (Dienste/Secrets/Scrubber/Gate); verwaistes jack_health nach LEGACY_ARCHIVE

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.234.166.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-07-11 15:23:19] SKILL-AUSGEFUEHRT | jack_status
[2026-07-11 16:15:20] SKILL-GESPEICHERT | ram_check
[2026-07-11 16:15:20] SKILL-GESPEICHERT | disk_check
[2026-07-11 16:15:20] SKILL-GESPEICHERT | fehler_report
[2026-07-11 16:15:20] SKILL-GESPEICHERT | git_status
[2026-07-11 16:15:20] SKILL-GESPEICHERT | gedaechtnis_stats
[2026-07-11 16:15:20] SKILL-GESPEICHERT | modell_check
[2026-07-11 16:15:20] SKILL-GESPEICHERT | budget_rest
[2026-07-11 16:15:20] SKILL-AUSGEFUEHRT | ram_check
[2026-07-11 16:15:20] SKILL-AUSGEFUEHRT | disk_check
[2026-07-11 16:15:20] SKILL-AUSGEFUEHRT | fehler_report
[2026-07-11 16:15:21] SKILL-AUSGEFUEHRT | git_status
[2026-07-11 16:15:21] SKILL-AUSGEFUEHRT | gedaechtnis_stats
[2026-07-11 16:15:21] SKILL-AUSGEFUEHRT | modell_check
[2026-07-11 16:15:21] SKILL-AUSGEFUEHRT | budget_rest
[2026-07-11 19:28:02] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-11 19:28:11] WAECHTER-AUDIT | woechentlich verschickt
[2026-07-13 03:53:18] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-13 03:58:33] WAECHTER-AUDIT | woechentlich verschickt
[2026-07-13 04:54:43] WAECHTER-START | Nacht-Ueberwachung laeuft

## Budget heute
Heute: Text 15/300 | Vision 0/40 | Tokens 23079