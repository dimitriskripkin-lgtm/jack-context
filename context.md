# JACK LIVE-KONTEXT (auto, 2026-08-18T00:21:21.440893)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-18T00:21:21.429505

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
- Erinnerungen: 1144
- Dienste:
run: jack_cortex: (pid 30232) 12808s
run: jack_telegram: (pid 30212) 12808s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 18563) 123102s

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

[2026-08-17 23:35:16] EXPLORE | Xiaomi: CPU=Load: 3.11 RAM=1617MB frei Akku=100% Temp=32.5C
[2026-08-17 23:35:16] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 23:40:19] EXPLORE | Xiaomi: CPU=Load: 2.32 RAM=1690MB frei Akku=100% Temp=31.9C
[2026-08-17 23:40:19] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 23:45:22] EXPLORE | Xiaomi: CPU=Load: 2.82 RAM=1549MB frei Akku=100% Temp=32.2C
[2026-08-17 23:45:22] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 23:50:26] EXPLORE | Xiaomi: CPU=Load: 2.20 RAM=1476MB frei Akku=100% Temp=31.8C
[2026-08-17 23:50:26] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 23:55:29] EXPLORE | Xiaomi: CPU=Load: 3.38 RAM=1535MB frei Akku=100% Temp=31.9C
[2026-08-17 23:55:29] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 00:00:32] EXPLORE | Xiaomi: CPU=Load: 2.35 RAM=1635MB frei Akku=100% Temp=31.8C
[2026-08-18 00:00:32] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 00:05:35] EXPLORE | Xiaomi: CPU=Load: 2.25 RAM=1301MB frei Akku=100% Temp=31.7C
[2026-08-18 00:05:35] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 00:10:38] EXPLORE | Xiaomi: CPU=Load: 1.47 RAM=1400MB frei Akku=100% Temp=31.3C
[2026-08-18 00:10:38] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 00:15:41] EXPLORE | Xiaomi: CPU=Load: 2.08 RAM=1507MB frei Akku=100% Temp=31.0C
[2026-08-18 00:15:41] SHADOW-FIXER | Keine offenen Fehler
[2026-08-18 00:20:45] EXPLORE | Xiaomi: CPU=Load: 2.07 RAM=1543MB frei Akku=100% Temp=31.0C
[2026-08-18 00:20:45] SHADOW-FIXER | Keine offenen Fehler

## Budget heute
Heute: Text 0/300 | Vision 0/40 | Tokens 0