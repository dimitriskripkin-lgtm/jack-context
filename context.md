# JACK LIVE-KONTEXT (auto, 2026-08-18T05:00:30.040659)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-18T05:00:30.024456

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
[PRIVAT GEFILTERT]
[PRIVAT GEFILTERT]
## Aktive Module (136)
- install_litert.py
- jack_agent.py
- jack_android.py
- jack_approval.py
- jack_audit.py
- jack_audit_run.py
- jack_auto_ingest.py
- jack_autofixer_multi.py
- jack_autofixer_shadow.py
- jack_autolearn_loop.py
- jack_autonomous.py
- jack_briefing.py
- jack_briefing_cron.py
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
- jack_context_compress.py
- jack_context_ingest.py
- jack_cortex.py
- jack_critic.py
- jack_db_optimizer.py
- jack_db_queue.py
- jack_delta.py
- jack_episoden.py
- jack_exec.py
- jack_explorer.py
- jack_explorer_deep.py
- jack_gedanken.py
- jack_gemini_bridge.py
- jack_ghost.py
- jack_grid_vision.py
- jack_groq_bridge.py
- jack_guard.py
- jack_haliza.py
- jack_handshake_gen.py
- jack_harvest.py
- jack_harvest_lernen.py
- jack_hey.py
- jack_improve.py
- jack_inbox.py
- jack_install.py
- jack_intent.py
- jack_learn.py
- jack_live_bridge.py
- jack_log.py
- jack_logging.py
- jack_lokal.py
- jack_math.py
- jack_memory.py
- jack_memory_engine.py
- jack_memory_maintenance.py
- jack_memory_stale.py
- jack_memory_tree.py
- jack_missions.py
- jack_monitor.py
- jack_observer.py
- jack_operator.py
- jack_oracle.py
- jack_orchestrator.py
- jack_outcome.py
- jack_patch.py
- jack_patch_memory.py
- jack_personality.py
- jack_planner.py
- jack_publish.py
- jack_queue.py
- jack_radar.py
- jack_react.py
- jack_reflexion.py
- jack_research_curator.py
- jack_rhythm.py
- jack_router.py
- jack_sanity.py
- jack_scheduler.py
- jack_schema.py
- jack_scout.py
- jack_screen_tracker.py
- jack_self_audit.py
- jack_self_improve.py
- jack_selftest.py
- jack_sensors.py
- jack_skill_builder.py
- jack_skill_lib.py
- jack_skill_self_creation.py
- jack_skill_trainer.py
- jack_skills.py
- jack_skills_db.py
- jack_snapshot.py
- jack_state.py
- jack_subagent.py
- jack_talk.py
- jack_telegram.py
- jack_thermal.py
- jack_traceback.py
- jack_tuev.py
- jack_tuev2.py
- jack_tuev3.py
- jack_ui.py
- jack_ui_agent.py
- jack_v2.py
- jack_vecdb.py
- jack_vinted_radar.py
- jack_vision.py
- jack_voice.py
- jack_voice_ab_test.py
- jack_voice_chat_live.py
- jack_voice_el.py
- jack_voice_live.py
- jack_voice_live_test.py
- jack_voice_ping.py
- jack_voice_processor.py
- jack_voice_router.py
- jack_voice_stability.py
- jack_voraussetzung.py
- jack_web_agent.py
- jack_web_ingest.py
- jack_whisper_async.py
- jack_write.py
- jack_xiaomi.py
- jack_xiaomi_cmd.py
- jack_xiaomi_inspector.py
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
- Erinnerungen: 1199
- Dienste:
run: jack_cortex: (pid 30232) 29557s
run: jack_telegram: (pid 30212) 29557s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 18563) 139851s

## Letzte Aenderungen
cac0fcd Observer-Layer aktiv: jack_exec fängt lügendes OS mit rc=99 ab + Handshake 53
263394f P1-P4 complete: Timeout-Fix, Deep-TB Parser, /find Grid-Vision, SSH Log-Fix
765ede6 Genesis: Threshold zurück auf 2
8432665 Genesis: Threshold auf 1 für Testing
c225406 Genesis: Multi-Log-Quellen + Traceback-Detection
c5ebea5 Genesis: echte Fix-Logik statt Dummy-echo
14992a1 P0 Fix: rag/autolearn_status/ingest_status in handle(), tote Handler entfernt
c471d83 feat: Vision-REST ohne genai, Chat-Harvester (read+swipe only, tap-frei), Lern-Destillierer, Telegram /vision /harvest /fakten
1c06a5c fix: TUEV3 Signaturen korrigiert (exec String, critic Tupel)
3c11786 fix: TUEV1 schliesst auch tuev2.py aus Leak-Scan aus
9c6f27a fix: Dienste-Liste korrekt (kein jack_autolearn/publisher), _xi() nutzt SSH-Alias, collect_status kein ping+alte-IP, update_identity atomic
a27ba0f fix: errors/akku/log/level im Router, TUEV3 Signaturen korrigiert
[PRIVAT GEFILTERT]
e23f258 fix: TUEV-Regex jack_publish.py ausgenommen (Filter-Regeln sind keine Leaks), NOTIFY-Fehler resolved
ea638f5 fix: threading-Import, ERRORS_DB korrekt, Gemini-Fallback [:3000] weg, duplikaten Callback-Handler entfernt

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-18 04:13:09] EXPLORE | Xiaomi: CPU=Load: 1.68 RAM=1988MB frei Akku=100% Temp=31.0C
[2026-08-18 04:13:09] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 04:18:15] EXPLORE | Xiaomi: CPU=Load: 19.30 RAM=1123MB frei Akku=100% Temp=41.7C
[2026-08-18 04:18:15] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 04:23:18] EXPLORE | Xiaomi: CPU=Load: 7.69 RAM=1829MB frei Akku=100% Temp=43.3C
[2026-08-18 04:23:18] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 04:28:21] EXPLORE | Xiaomi: CPU=Load: 1.89 RAM=1934MB frei Akku=100% Temp=35.7C
[2026-08-18 04:28:21] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 04:33:25] EXPLORE | Xiaomi: CPU=Load: 2.48 RAM=1838MB frei Akku=100% Temp=35.1C
[2026-08-18 04:33:25] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 04:38:28] EXPLORE | Xiaomi: CPU=Load: 2.22 RAM=1826MB frei Akku=100% Temp=33.7C
[2026-08-18 04:38:28] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 04:43:31] EXPLORE | Xiaomi: CPU=Load: 2.54 RAM=1667MB frei Akku=100% Temp=33.4C
[2026-08-18 04:43:31] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 04:48:34] EXPLORE | Xiaomi: CPU=Load: 3.47 RAM=1368MB frei Akku=100% Temp=34.3C
[2026-08-18 04:48:34] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 04:53:37] EXPLORE | Xiaomi: CPU=Load: 2.58 RAM=1287MB frei Akku=100% Temp=32.9C
[2026-08-18 04:53:37] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 04:58:40] EXPLORE | Xiaomi: CPU=Load: 2.77 RAM=1341MB frei Akku=100% Temp=32.7C
[2026-08-18 04:58:40] SHADOW-FIXER | Keine offenen Fehler

## Budget heute
Heute: Text 3/300 | Vision 0/40 | Tokens 15800