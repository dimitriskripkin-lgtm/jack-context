# JACK LIVE-KONTEXT (auto, 2026-07-10T00:38:39.462160)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-07-10T00:38:39.446364

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri, ein Nachtschicht-LKW-Fahrer und Hobby-Programmierer.
- Dima arbeitet bei Dalhoff Feinkost in Achim.
- Dima fährt einen Sprinter (Kühlkoffer) bei Dalhoff Feinkost.
- Dima hat KEINEN Hund.
- JACK ist ein autonomes, lokales AI-OS, das auf einem Honor Magic8 Pro mit Termux läuft.
- JACK verwendet Gemini 2.5 Flash als Haupt-Denker.
- JACK soll sich selbst lernen und verbessern.
- JACK steht unter Dimas voller Kontrolle.
- JACK beinhaltet das `jack_math.py`-Modul für einfache mathematische Operationen.
- JACK wurde am 18. Juni gebaut.
- JACK hat über den Chat keinen direkten Shell- oder Dateizugriff.
- JACK verwendet `jack_learn.py` als Lerner.
- Dima nutzt Gemini Plus und Claude.ai.
- JACK läuft auf einem Honor Magic8 Pro mit 16GB RAM und Termux.
- JACK nutzt ein Xiaomi 11T Pro als Slave-Gerät via SSH.
- JACK's kostenlose KI-Modelle sind limitiert (Tageslimits).
- JACK's Chef-KI 'Claude Code' ist ein read-only Berater, erreichbar via Telegram.
- JACK hat Fähigkeiten wie Text- und Sprachchat, sicheres Code schreiben, autonomes Handeln und Selbstverbesserung.
- JACK nutzt `jack_waechter` für regelbasierte Überwachung und Neustarts.
- JACK's Konfiguration und Logs werden in einem öffentlichen Repo (`jack-context`) geteilt.

## Aktive Module (40)
- jack_agent.py
- jack_approval.py
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
- jack_health.py
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
- Offene Fehler: 0
- Erinnerungen: 93
- Dienste:
run: jack_cortex: (pid 11922) 35704s
run: jack_telegram: (pid 23044) 11840s
run: jack_autolearn: (pid 12394) 13879s
run: ollama: (pid 12229) 50480s

## Letzte Aenderungen
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
77a3333 Kosten-Bremse: Tageslimits Gemini Text(300)+Vision(40), /budget-Befehl - schuetzt vor Kosten-Explosion bei Bild-/Sensordaten
14fb2a3 Entscheidungs-Logbuch: jede JACK-Aktion nachvollziehbar (jack_log), /log in Telegram - Grundstein fuer sichere Autonomie
b372e98 Selbstverbesserung jack_math.py (JACK-Vorschlag, Dima-Freigabe)
6768994 Fix: doppelte tote GEMINI-Key-Zeile entfernt (401-Ursache), Bot-Loop + propose_improvement gegen Absturz/Crashloop abgesichert

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.234.166.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-07-09 16:13:29] AGENT-ERFOLG | Schreibe ein Python-Programm das di -> script_20260709_1613.py
[2026-07-09 16:16:28] AGENT-START | Schreibe ein Programm das alle Primzahlen bis 50 ausgibt
[2026-07-09 16:16:39] AGENT-START | Schreibe ein Programm das alle Primzahlen bis 50 ausgibt
[2026-07-09 20:04:23] AGENT-START | Schreibe ein Programm das alle Primzahlen bis 50 ausgibt
[2026-07-09 20:04:36] AGENT-RUNDE | Schreibe ein Programm das alle Prim #1 | nachbessern
[2026-07-09 20:04:48] AGENT-RUNDE | Schreibe ein Programm das alle Prim #2 | nachbessern
[2026-07-09 20:05:01] AGENT-RUNDE | Schreibe ein Programm das alle Prim #3 | nachbessern
[2026-07-09 20:05:13] AGENT-RUNDE | Schreibe ein Programm das alle Prim #4 | nachbessern
[2026-07-09 20:05:19] AGENT-START | Schreibe ein Programm das meine Secrets Datei ausliest und anzeigt
[2026-07-09 20:05:31] AGENT-RUNDE | Schreibe ein Programm das meine Sec #1 | nachbessern
[2026-07-09 20:05:44] AGENT-RUNDE | Schreibe ein Programm das meine Sec #2 | nachbessern
[2026-07-09 20:05:56] AGENT-RUNDE | Schreibe ein Programm das meine Sec #3 | nachbessern
[2026-07-09 20:06:09] AGENT-RUNDE | Schreibe ein Programm das meine Sec #4 | nachbessern
[2026-07-09 20:19:38] AGENT-START | Schreibe ein Programm das alle Primzahlen bis 50 ausgibt
[2026-07-09 20:19:48] AGENT-RUNDE | Schreibe ein Programm das alle Prim #1 | ok
[2026-07-09 20:19:48] AGENT-ERFOLG | Schreibe ein Programm das alle Prim -> script_20260709_2019.py
[2026-07-09 21:30:57] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-09 21:33:21] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-09 21:35:12] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-09 22:21:13] DATEI-SCHREIBEN | konventionen_fuer_gemini_20260709_2220.json | 1563 Zeichen

## Budget heute
Heute: Text 0/300 | Vision 0/40 | Tokens 0