# JACK LIVE-KONTEXT (auto, 2026-08-14T15:04:10.625326)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-14T15:04:10.616083

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
- JACK kann das Xiaomi 11T Pro per SSH ansprechen, die Verbindung ist aber häufig instabil.
- JACK kann das System live sehen und analysieren.
- JACK kann die Umgebung via Termux-Verzeichnissen analysieren.
- JACK identifiziert sich als KI-OS und Dima als Nutzer.
- JACK hat Zugriff auf Verzeichnisse, die Termux auf dem Honor erlaubt (hauptsächlich unter `/data/data/com.termux/files/home`).
- JACK kann Fehler autonom fixen.
- JACK hat eine Baumstruktur für sein Gedächtnis und kann Momente erinnern.

## Aktive Module (91)
- install_litert.py
- jack_agent.py
- jack_android.py
- jack_approval.py
- jack_audit.py
- jack_autonomous.py
- jack_briefing.py
- jack_budget.py
- jack_bug_fixer.py
- jack_bugfix_loop.py
- jack_calltest.py
- jack_chains.py
- jack_claude.py
- jack_code_writer.py
- jack_coder.py
- jack_config.py
- jack_consolidate.py
- jack_context_ingest.py
- jack_cortex.py
- jack_db_queue.py
- jack_delta.py
- jack_episoden.py
- jack_gedanken.py
- jack_gemini_bridge.py
- jack_guard.py
- jack_haliza.py
- jack_handshake_gen.py
- jack_hey.py
- jack_improve.py
- jack_install.py
- jack_intent.py
- jack_learn.py
- jack_log.py
- jack_logging.py
- jack_lokal.py
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
- jack_router.py
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
- jack_state.py
- jack_talk.py
- jack_telegram.py
- jack_thermal.py
- jack_traceback.py
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
- jack_voraussetzung.py
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
- Offene Fehler: 0
- Erinnerungen: 251
- Dienste:
run: jack_cortex: (pid 7269) 15841s
run: jack_telegram: (pid 8686) 3180s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 7266) 15841s

## Letzte Aenderungen
08228da feat(autonomous): explore_next() in Waechter-Loop alle 300s
36a62fc fix(xiaomi): explore_next() CPU+active_app via Root
ca0b393 fix(xiaomi): explore_next() Output sauber parsen
c4f1428 fix(xiaomi): explore_next() Befehle fuer Android korrigiert
0aeb8f0 feat(xiaomi): ControlMaster + explore_next() autonome Idle-Exploration
209b5ab sec: harden gitignore - exclude state files, secrets, locks, SSH keys
e99e4e9 fix: persona inject syntax warning in jack_talk context builder
66d8580 fix: replace ping with urllib, persona injected into talk, keyboard sig fix
4bf9469 feat(persona): memory trigger in poll-loop + proactive 30min pulse
9f563c3 feat(persona): deep persona DNA, natural memory trigger, foto-persona fix
7856045 feat(core): harden resilience, inject dima-state machine, and upgrade context ingest cleaner
c43cc8b lokale reasoning-engine: modell-agnostisch mit ram/temp-guards, regelbasierter router, offline-fallback in talk
e301b88 cortex: Xiaomi-erreichbar-wieder als status statt error loggen
f3c433f telegram: timeout=0 gegen carrier-nat-kill auf 5g, send-else-zweig wiederhergestellt, /scan aus fast_cmds
d12a288 delta-kontext statt dauerbericht, voraussetzungs-pruefung mit ehrlicher fehlermeldung, xiaomi 15min entprellt max 2/tag, voice text vor sprache, laengere antworten

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-14 00:12:11] WAECHTER-MELDUNG | Xiaomi weg
[2026-08-14 01:15:00] PROFIL-UPDATE | 2 neue Eintraege in kortex_profile.json
[2026-08-14 01:16:26] SCOUT-LAUF | 06a5e8af25a1235c
[2026-08-14 10:40:09] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-08-14 10:40:11] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-08-14 10:40:39] GUARD-OK | selftest gestartet, 3473MB frei
[2026-08-14 10:41:36] SCOUT-LAUF | 3678bf4ddf4c402d
[2026-08-14 11:00:00] CONSOLIDATE | Session gespeichert: 10 Logs, 0 Zugriffe
[2026-08-14 11:11:45] SAGA-CLEANUP | 18 temp-Dateien geloescht: voice_AwACAgIAAxkBAAICQWpXPxFKWbW-dcnUJ3vFpDy9floZAAK9lgACitO4Sk5lylWlJd0_PQQ.ogg,voice_AwACAgIAAxkBAAICQ2pXPySCB38WkXm6NcpVEyVgqqDYAALAlgACitO4Sj1Q1aLix4UzPQQ.ogg,voice_AwACAgIAAxkBAAICmGpaJYeCf1ZQWeBToCAzRFjCwbSlAAInogAChEDRSs9v2VDojJk-PQQ.ogg,voice_AwACAgIAAxkBAAICoWpbtAvZdhpiCUjKFcpuWv5osLmQAAI3oQAChEDZStdBF0bWlF8RPQQ.ogg,voice_AwACAgIAAxkBAAICo2pbtEFADfv7yGBQXoTjMEcKb95PAAI7oQAChEDZSqrk1fHrKW3fPQQ.ogg
[2026-08-14 11:26:10] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-08-14 11:26:10] SELF-IMPROVE | Tagescheck abgeschlossen
[2026-08-14 12:03:39] MONITOR-EVENT | 1 Events
[2026-08-14 12:28:08] MONITOR-AKKU-WARN | 20%
[2026-08-14 12:28:10] MONITOR-EVENT | 1 Events
[2026-08-14 12:34:15] MONITOR-EVENT | 1 Events
[2026-08-14 12:46:23] MONITOR-EVENT | 1 Events
[2026-08-14 12:56:32] MONITOR-EVENT | 1 Events
[2026-08-14 13:26:03] GUARD-OK | whisper gestartet, 2376MB frei
[2026-08-14 14:40:15] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-08-14 14:49:48] MONITOR-EVENT | 1 Events

## Budget heute
Heute: Text 35/300 | Vision 0/40 | Tokens 82698