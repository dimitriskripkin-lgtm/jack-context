# JACK LIVE-KONTEXT (auto, 2026-08-08T05:06:07.870977)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-08T05:06:07.855092

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

## Aktive Module (78)
- install_litert.py
- jack_agent.py
- jack_android.py
- jack_approval.py
- jack_audit.py
- jack_autonomous.py
- jack_briefing.py
- jack_budget.py
- jack_bug_fixer.py
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
run: jack_cortex: (pid 31748) 78280s
run: jack_telegram: (pid 27719) 34398s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 11415) 80064s

## Letzte Aenderungen
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
c51e96d memory_tree: schreibt via db_queue (thread-safe) | offene aenderungen synchronisiert
9457fb2 db_queue: thread-safe write-queue | gemini: bare except geloggt | logging in kernmodulen
bae4bcf db_queue: thread-safe sqlite write-queue, ein writer pro db
5409af4 memory-tree: baumstruktur mit parent_id, auto-chaining in sessions, /baum befehl
9397b65 logging: blinde excepts in 5 kernmodulen geloggt | memory: parent_id baumstruktur

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-07 07:21:26] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-08-07 07:22:52] SCOUT-LAUF | ed2368d2cfce9100
[2026-08-07 07:23:26] SANITY-ERR | module 'jack_sanity' has no attribute 'check'
[2026-08-07 07:55:01] MONITOR-VOLLSCAN | ok
[2026-08-07 11:00:00] CONSOLIDATE | Session gespeichert: 10 Logs, 0 Zugriffe
[2026-08-07 11:31:30] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-08-07 11:31:30] SELF-IMPROVE | Tagescheck abgeschlossen
[2026-08-07 12:06:23] MONITOR-VOLLSCAN | ok
[2026-08-07 13:23:26] SANITY-ERR | module 'jack_sanity' has no attribute 'check'
[2026-08-07 15:10:33] MONITOR-EVENT | 1 Events
[2026-08-07 15:40:53] MONITOR-EVENT | 1 Events
[2026-08-07 17:21:40] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-08-07 19:21:43] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-08-07 19:23:26] SANITY-ERR | module 'jack_sanity' has no attribute 'check'
[2026-08-07 20:11:44] MONITOR-EVENT | 1 Events
[2026-08-07 20:13:53] MONITOR-VOLLSCAN | ok
[2026-08-07 21:40:39] MONITOR-NOTIFY-ERR | <urlopen error [Errno 7] No address associated with hostname>
[2026-08-07 21:40:39] MONITOR-EVENT | 1 Events
[2026-08-07 21:44:42] MONITOR-EVENT | 1 Events
[2026-08-08 01:23:26] SANITY-ERR | module 'jack_sanity' has no attribute 'check'

## Budget heute
Heute: Text 2/300 | Vision 0/40 | Tokens 7020