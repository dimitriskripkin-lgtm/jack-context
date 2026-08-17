# JACK LIVE-KONTEXT (auto, 2026-08-17T21:55:29.654237)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-17T21:55:29.634500

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
[PRIVAT GEFILTERT]
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
- Erinnerungen: 1115
- Dienste:
run: jack_cortex: (pid 30232) 4056s
run: jack_telegram: (pid 30212) 4056s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 18563) 114350s

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

[2026-08-17 21:08:43] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 21:13:46] EXPLORE | Xiaomi: CPU=Load: 3.72 RAM=1986MB frei Akku=100% Temp=32.9C
[2026-08-17 21:13:46] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 21:18:49] EXPLORE | Xiaomi: CPU=Load: 4.33 RAM=2134MB frei Akku=100% Temp=32.8C
[2026-08-17 21:18:49] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 21:23:51] EXPLORE | Xiaomi: CPU=Load: 4.05 RAM=2170MB frei Akku=100% Temp=32.7C
[2026-08-17 21:23:51] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 21:28:54] EXPLORE | Xiaomi: CPU=Load: 4.05 RAM=2249MB frei Akku=100% Temp=32.6C
[2026-08-17 21:28:54] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 21:33:56] EXPLORE | Xiaomi: CPU=Load: 4.20 RAM=2004MB frei Akku=100% Temp=33.3C
[2026-08-17 21:33:56] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 21:38:59] EXPLORE | Xiaomi: CPU=Load: 4.30 RAM=1987MB frei Akku=100% Temp=32.8C
[2026-08-17 21:38:59] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 21:40:40] MONITOR-VOLLSCAN | ok
[2026-08-17 21:44:02] EXPLORE | Xiaomi: CPU=Load: 5.82 RAM=1696MB frei Akku=100% Temp=33.8C
[2026-08-17 21:44:02] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 21:49:06] EXPLORE | Xiaomi: CPU=Load: 4.21 RAM=1431MB frei Akku=100% Temp=37.5C
[2026-08-17 21:49:06] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 21:54:10] EXPLORE | Xiaomi: CPU=Load: 3.70 RAM=1309MB frei Akku=100% Temp=37.6C
[2026-08-17 21:54:10] SHADOW-FIXER | Keine offenen Fehler

## Budget heute
Heute: Text 85/300 | Vision 37/40 | Tokens 439259