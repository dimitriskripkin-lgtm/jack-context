# JACK LIVE-KONTEXT (auto, 2026-08-08T13:34:46.827081)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-08T13:34:46.817043

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
- Dima ist LKW-Fahrer mit Sprinter Kühlkoffer bei Dalhoff Feinkost in Achim (Nachtschicht).
- Dima ist Hobby-Programmierer und Autodidakt.
- Dima hat mit 28 einen Burnout gehabt und sich selbst daraus gezogen (Stoizismus, Jung, Kiyosaki).
- Dima möchte mit JACK Unabhängigkeit und Freiheit aufbauen.
- JACK ist das Exit-Vehicle für Dimas Freiheit und Unabhängigkeit.
- JACK ist ein autonomes, lokales AI-OS auf Dimas Honor Magic8 Pro.
- JACK nutzt Gemini als Denkwerkzeug über API-Calls.
- JACK steht unter Dimas voller Kontrolle.
- JACK kann das Xiaomi 11T Pro per SSH ansprechen.
- Dima hat KEINEN Hund.
- Dima ist KEIN Fernfahrer.
- JACK hat KEINEN direkten Shell- oder Dateizugriff über den Chat.
- Dima hat die Anweisung gegeben, bei bestimmten Fragen länger zu antworten.
- Dima ist jemand, der nach der Nachtschicht im Sprinter lieber noch Code schreibt als schläft.
- Dima hat einen Joint zum Entspannen genehmigt.
- Das Xiaomi ist oft nicht erreichbar.
- Die SSH-Verbindung zum Xiaomi ist häufig instabil.
- JACK verfügt über Fähigkeiten wie Speichermanagement, Sicherheit und Automatisierung.
- Dima hat Dima als Nutzer und JACK als KI-OS identifiziert.

## Aktive Module (80)
- install_litert.py
- jack_agent.py
- jack_android.py
- jack_approval.py
- jack_audit.py
- jack_autonomous.py
- jack_briefing.py
- jack_budget.py
- jack_bug_fixer.py
- jack_calltest.py
- jack_chains.py
- jack_claude.py
- jack_code_writer.py
- jack_coder.py
- jack_config.py
- jack_consolidate.py
- jack_cortex.py
- jack_db_queue.py
- jack_gemini_bridge.py
- jack_haliza.py
- jack_handshake_gen.py
- jack_hey.py
- jack_improve.py
- jack_install.py
- jack_intent.py
- jack_learn.py
- jack_log.py
- jack_logging.py
- jack_math.py
- jack_memory.py
- jack_memory_engine.py
- jack_memory_maintenance.py
- jack_memory_tree.py
- jack_missions.py
- jack_monitor.py
- jack_operator.py
- jack_oracle.py
- jack_patch.py
- jack_patch_memory.py
- jack_personality.py
- jack_publish.py
- jack_radar.py
- jack_reflexion.py
- jack_sanity.py
- jack_scout.py
- jack_screen_tracker.py
- jack_self_improve.py
- jack_selftest.py
- jack_sensors.py
- jack_skill_builder.py
- jack_skills.py
- jack_skills_db.py
- jack_snapshot.py
- jack_talk.py
- jack_telegram.py
- jack_thermal.py
- jack_ui.py
- jack_v2.py
- jack_vecdb.py
- jack_vinted_radar.py
- jack_voice.py
- jack_voice_ab_test.py
- jack_voice_chat_live.py
- jack_voice_live.py
- jack_voice_live_test.py
- jack_voice_ping.py
- jack_voice_processor.py
- jack_voice_router.py
- jack_voice_stability.py
- jack_write.py
- jack_xiaomi.py
- jack_xiaomi_cmd.py
- kortex_controller.py
- kortex_memory.py
- kortex_profile_updater.py
- kortex_profiler.py
- kortex_sensor_daemon.py
- litert_watchdog.py
- quick_bridge.py
- test_jack_approval.py

## System-Status
- Offene Fehler: 1
- Erinnerungen: 199
- Dienste:
run: jack_cortex: (pid 31748) 108799s
run: jack_telegram: (pid 414) 9079s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 11415) 110583s

## Letzte Aenderungen
2688e1d jack_calltest: prueft alle modulaebergreifenden Aufrufe + tote Waechter-Threads
01c4105 Telegram: Offset persistent + sofortige Bestaetigung + Absturz-Log (behebt Replay-Loop)
ebb1b09 Telegram: Timestamp am Ende jeder Nachricht
c766375 jack_reflexion: Aktions-IDs + Nacht-Reflexions-Loop -> Langzeitgedaechtnis
8fab8e0 jack_sanity: check()-Alias fuer Waechter-Thread (behebt SANITY-ERR)
030eb0e db_queue: import als fallback in cortex/missions/memory_engine
c65b048 telegram: foto-analyse immer auf deutsch
171ddfd ci: github actions - pytest bei jedem push auf master
bf51ca0 telegram: foto-analyse mit ffmpeg-komprimierung, async thread
25be220 tests: duplikat-test raeumt vor testlauf auf
943ee8a selftest: cpu-die 91C, akku 50C - zwei separate sensoren
f827ff1 selftest: cpu-die 91C, akku 50C - zwei separate sensoren
cca6d62 tests: 5 kern-tests fuer memory, intent, selftest, chains
8dbcf19 memory: fts duplikate-fix, rebuild fts index
e2be96d memory: schema fix 5->7 spalten, monkey-patch weg, schreibt via db_queue

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-08 10:23:36] HALIZA-SYNTAX-STOP | File "/data/data/com.termux/files/home/jack/.haliza_check.py", line 1
    def hallo(
             ^
SyntaxError: '(' was
[2026-08-08 10:25:22] HALIZA-START | test.py: test
[2026-08-08 10:26:14] HALIZA-START | test.py: Test-Funktion
[2026-08-08 10:26:14] HALIZA-MEM-STOP | File "/data/data/com.termux/files/home/jack/.haliza_check.py", line 1
    def hallo(
             ^

[2026-08-08 10:30:03] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-08-08 10:31:19] SCOUT-LAUF | b138de15975dc9f6
[2026-08-08 10:32:34] MONITOR-DIENST-TOT | jack_telegram
[2026-08-08 10:32:35] MONITOR-EVENT | 1 Events
[2026-08-08 10:34:36] MONITOR-EVENT | 1 Events
[2026-08-08 11:00:00] CONSOLIDATE | Session gespeichert: 9 Logs, 0 Zugriffe
[2026-08-08 11:13:01] MONITOR-EVENT | 1 Events
[2026-08-08 11:36:22] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-08-08 11:36:22] SELF-IMPROVE | Tagescheck abgeschlossen
[2026-08-08 13:22:18] MONITOR-EVENT | 1 Events

## Budget heute
Heute: Text 7/300 | Vision 0/40 | Tokens 24570