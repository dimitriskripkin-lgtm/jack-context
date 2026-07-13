# JACK LIVE-KONTEXT (auto, 2026-07-13T03:00:09.830807)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-07-13T03:00:09.817477

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

## Aktive Module (40)
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
- kortex_profiler.py
- kortex_sensor_daemon.py
- quick_bridge.py
- test_jack_approval.py

## System-Status
- Offene Fehler: 1
- Erinnerungen: 99
- Dienste:
run: jack_cortex: (pid 20695) 179410s
run: jack_telegram: (pid 23876) 114106s
run: jack_autolearn: (pid 20689) 179410s
run: ollama: (pid 20694) 179410s

## Letzte Aenderungen
a35bb6e jack_audit: Gesundheits+Sicherheits-Check (Dienste/Secrets/Scrubber/Gate); verwaistes jack_health nach LEGACY_ARCHIVE
aebe902 Skill-Gate (Weg 1): assess_skill_risk - subprocess via Whitelist erlaubt, Killer-Muster hart geblockt, /code-Gate unberuehrt
f724f96 ARCHITEKTUR.md: auf Live-Stand - erledigte Baustellen (Keys/SSH/Log/Augen/Selbstverbesserung) raus, neue Schichten+Befehle rein, ehrliche OFFEN-Liste
b55f1d6 CLAUDE.md: auf Live-Stand konsolidiert - jack_waechter->jack_autonomous Mapping, alle 6 Dienste, DB-Schemas, erledigte Baustellen raus
60a9c28 Fix: jack_taskrunner-Gespenst entfernt (nie gebaut), Waechter + CLAUDE.md sauber. Notiz: Xiaomi-Status pushen + Claude-Schreibrechte Xiaomi = spaeter
3641e51 taskrunner neu gestartet, Waechter-Baseline frisch
c088322 Nacht-Waechter: regelbasierte Selbstueberwachung, meldet nur echte Probleme per Telegram, restartet tote Dienste, erster Lauf nur Baseline (weckt nicht)
60f557c Aufraeumen: jack_learning_loop.py + Backups stillgelegt, CLAUDE.md mit echter Dienstliste - verhindert dass Claude Code aus toten Dateien liest
61694b6 Claude Code Bruecke: /cc im Telegram (Text) + Sprach-Routing (Voice startet mit 'claude'). Read-only Berater kennt die ganze Umgebung, laeuft ueber Abo
ff4ac38 CLAUDE.md Wissensbasis + Publisher pusht ganze Umgebung (Werkstatt/Skills/Logs)
b56a851 Memory: absolute Korrekturen (kein Hund/LKW-Fahrer) verankert, Publish-Scrub praeziser
a98e082 Rate-Limit-Fix: Modellwechsel auf freies Gemini-Modell, Token-Zaehler eingebaut, Agent-Kaskaden-Bug behoben (Fehlermeldung nicht mehr als Code), Runden-Pause
2cc5b3f Gemini-Bridge: Retry+Backoff gegen HTTP 429 (Rate-Limit) - Agent + Chat laufen jetzt drosselfest
58360e2 Autonomer Agent: /auto <ziel> - JACK loest Ziele selbststaendig in der Werkstatt (schreibt+testet+verbessert, max 4 Runden), im Hintergrund-Thread, harte Sandbox-Waende bleiben
b683f1f Skill-Bibliothek: erfolgreiche Code-Bausteine speichern (/skill save) + kostenlos wiederverwenden (/skill <name>) - senkt API-Kosten, macht JACK unabhaengiger

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.234.166.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-07-11 01:22:09] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-11 15:08:46] SKILL-GESPEICHERT | jack_status
[2026-07-11 15:23:19] SKILL-GESPEICHERT | jack_status
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

## Budget heute
Heute: Text 0/300 | Vision 0/40 | Tokens 0