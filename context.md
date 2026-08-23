# JACK LIVE-KONTEXT (auto, 2026-08-23T15:41:10.431476)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-23T15:41:10.422289

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
[PRIVAT GEFILTERT]
[PRIVAT GEFILTERT]
## Aktive Module (173)
- diag_full_dump.py
- diag_snapshot.py
- jack_accessibility_listener.py
- jack_activity_logger.py
- jack_agent.py
- jack_android.py
- jack_anomaly.py
- jack_approval.py
- jack_ast_gate.py
- jack_audit.py
- jack_audit_run.py
- jack_aufraeumen.py
- jack_auto_ingest.py
- jack_autofixer_shadow.py
- jack_autolearn_loop.py
- jack_autonomous.py
- jack_briefing.py
- jack_briefing_cron.py
- jack_budget.py
- jack_budget_status.py
- jack_bug_fixer.py
- jack_bugfix_loop.py
- jack_calltest.py
- jack_chains.py
- jack_circuit_breaker.py
- jack_claude.py
- jack_cmd_crawler.py
- jack_code_writer.py
- jack_coder.py
- jack_config.py
- jack_consolidate.py
- jack_context_compress.py
- jack_context_ingest.py
- jack_cortex.py
- jack_critic.py
- jack_curiosity.py
- jack_db_optimizer.py
- jack_db_queue.py
- jack_delta.py
- jack_episoden.py
- jack_error_to_rule.py
- jack_errors_status.py
- jack_exec.py
- jack_exec_parser.py
- jack_explorer.py
- jack_explorer_deep.py
- jack_faehigkeiten.py
- jack_focus_monitor.py
- jack_freigabe.py
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
- jack_heartbeat.py
- jack_heat_protection.py
- jack_hey.py
- jack_improve.py
- jack_inbox.py
- jack_install.py
- jack_intent.py
- jack_intent_apps.py
- jack_intent_lookup.py
- jack_intent_parser.py
- jack_karte.py
- jack_karte_loop.py
- jack_learn.py
- jack_lerner.py
- jack_live_bridge.py
- jack_log.py
- jack_log_rotate.py
- jack_logging.py
- jack_lokal.py
- jack_loop.py
- jack_math.py
- jack_mcp_server.py
- jack_memory.py
- jack_memory_maintenance.py
- jack_memory_pruning.py
- jack_memory_stale.py
- jack_memory_tree.py
- jack_missions.py
- jack_monitor.py
- jack_nav_learn.py
- jack_navi.py
- jack_observer.py
- jack_operator.py
- jack_oracle.py
- jack_orchestrator.py
- jack_outcome.py
- jack_outcome_tracker.py
- jack_patch.py
- jack_patch_memory.py
- jack_personality.py
- jack_planner.py
- jack_publish.py
- jack_publisher_loop.py
- jack_queue.py
- jack_radar.py
- jack_react.py
- jack_read_curl.py
- jack_reflexion.py
- jack_rhythm.py
- jack_router.py
- jack_sanity.py
- jack_scheduler.py
- jack_schema.py
- jack_scout.py
- jack_screen_mapper.py
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
- jack_stress.py
- jack_subagent.py
- jack_system_tools.py
- jack_talk.py
- jack_telegram.py
- jack_thermal.py
- jack_traceback.py
- jack_tuev2.py
- jack_tuev3.py
- jack_tuev4.py
- jack_tuev5.py
- jack_tuev6.py
- jack_ui.py
- jack_ui_agent.py
- jack_ui_elements.py
- jack_ui_read.py
- jack_vecdb.py
- jack_vinted_radar.py
- jack_vision.py
- jack_vision_once.py
- jack_vision_selector.py
- jack_voice.py
- jack_voice_chat_live.py
- jack_voice_el.py
- jack_voice_live.py
- jack_voice_processor.py
- jack_voice_router.py
- jack_voraussetzung.py
- jack_web_agent.py
- jack_web_ingest.py
- jack_whisper_async.py
- jack_wissen_ernte.py
- jack_wissen_tief.py
- jack_workers.py
- jack_write.py
- jack_xiaomi.py
- jack_xiaomi_inspector.py
- jack_xiaomi_think.py
- jack_xiaomi_unlock.py
- jack_xiaomi_web.py
- jack_yt_sido.py
- kortex_controller.py
- kortex_memory.py
- kortex_profile_updater.py
- kortex_sensor_daemon.py
- wirkungs_check.py

## System-Status
- Offene Fehler: 0
- Erinnerungen: 2395
- Dienste:
run: jack_cortex: (pid 11260) 677s
run: jack_telegram: (pid 17005) 363s
run: jack_autolearn: (pid 14990) 479s
fail: ollama: unable to change to service directory: file does not exist

## Letzte Aenderungen
106324a Haertung 2: Sandbox nur Werkstatt, Log-Rotation, SSH-Alias Sensors, Bridge-IP sauber
744385c Haertung: TG-Heartbeat, Circuit-Breaker-Gemini, SQLite-Monkeypatch-weg, Sandbox-fix, Config-IP
2462759 Fix: detect_futile_skills korrekt eingefuegt, Heartbeat im Loop
34b79da Heartbeat-System: Liveness-Monitoring + Futility-Detector fuer alle Dienste
37e810c Fix: Sensoren+Audit IP aus config (Augen repariert), Flask-Import-Sideeffect entschaerft, Dienstlisten bereinigt
eac822e Fix: Xiaomi-IP aus config statt hardcoded, Ollama auf Xiaomi, NameError fname
a89a8dd NIGHT-FIX: Shadow-Fixer skippt wenn Xiaomi offline (kein Error-Loop mehr)
6fb261c NIGHT-FIX: jack_cortex still bei Xiaomi-Offline + emergency_stop() bei >80°C
8dd72fb NOTFALL: jack_cortex pausiert wenn Xiaomi offline (verhindert Fehler-Loop bei 103°C)
feac0da loop: JACK result
8d47c4d FIX: ssh_tunnel_ollama runit HOME PATH ControlMaster=no AUTOSSH_GATETIME=0
0ccc7df FIX: autolearn log sources full path, tilde junk gone
457c903 FIX: startup SVDIR plus autolearn genesis liest fail in startup.log
d3868a7 Phase 2: jack_vision_selector.py - text-basierte Element-Suche (su -c fix)
cac2d9f Phase 1 FIX: Connection-close + flush + setsid-Start (MCP-Server stabil auf Xiaomi)

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-21 10:22:32] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-21 10:22:32] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-21 10:22:34] EXPLORE | Xiaomi: CPU=Load: 0.54 RAM=2193MB frei Akku=100% Temp=33.6C
[2026-08-21 10:22:34] SHADOW-FIXER | Keine offenen Fehler
[2026-08-21 10:27:34] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-21 10:27:34] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-21 10:27:35] EXPLORE | Xiaomi: CPU=Load: 0.34 RAM=2421MB frei Akku=100% Temp=33.0C
[2026-08-21 10:27:35] SHADOW-FIXER | Keine offenen Fehler
[2026-08-21 10:32:35] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-21 10:32:35] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-21 10:32:37] EXPLORE | Xiaomi: CPU=Load: 0.59 RAM=2422MB frei Akku=100% Temp=32.7C
[2026-08-21 10:32:37] SHADOW-FIXER | Keine offenen Fehler
[2026-08-21 10:37:37] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-21 10:37:37] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-21 10:37:38] EXPLORE | Xiaomi: CPU=Load: 0.90 RAM=2122MB frei Akku=100% Temp=32.7C
[2026-08-21 10:37:38] SHADOW-FIXER | Keine offenen Fehler
[2026-08-21 10:42:38] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-21 10:42:38] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-21 10:42:40] EXPLORE | Xiaomi: CPU=Load: 0.64 RAM=1732MB frei Akku=100% Temp=32.2C
[2026-08-21 10:42:40] SHADOW-FIXER | Keine offenen Fehler

## Budget heute
Heute: Text 24/300 | Vision 1/40 | Tokens 105727