# JACK LIVE-KONTEXT (auto, 2026-08-17T15:10:25.591008)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-17T15:10:25.579473

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
[PRIVAT GEFILTERT]
## Aktive Module (124)
- install_litert.py
- jack_agent.py
- jack_android.py
- jack_approval.py
- jack_audit.py
- jack_autofixer_multi.py
- jack_autofixer_shadow.py
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
- jack_groq_bridge.py
- jack_guard.py
- jack_haliza.py
- jack_handshake_gen.py
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
- jack_ui.py
- jack_ui_agent.py
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
- Offene Fehler: 1
- Erinnerungen: 1034
- Dienste:
run: jack_cortex: (pid 25040) 11650s
run: jack_telegram: (pid 12021) 10140s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 18563) 90046s

## Letzte Aenderungen
1c8234a security: CLAUDE.md + Alt-Handshakes + Verhaltensprofil untracked, TUEV-Pruefstand aufgenommen, Regex praezisiert
a4eca6d feat: deterministischer Befehls-Router mit Gemini-Catch-All, Prompt-Konsistenz + Marker-Verbot, Skill-Builder auf Trainer-Schema via Mantel
9d13c5a feat: Voll-Button-Bedienung - cmd:-Callback routet Buttons durch handle(), Kategorie-Menues als Tap-Grids, Ketten-Schnellwahl
539bcc2 fix: /kette und /bugfix Handler verdrahtet - Menue war Attrappe, jetzt feuern jack_chains und jack_bugfix_loop
6a0a734 security: DBs untracked, Anti-Halluzinations-Regel, Test-Eintrag resolved
cc185a7 fix: ehrliches Quellen-Label in talk, private JSONs geprueft
6b2a9e7 feat: Einheits-Fehlerkanal via jack_log-Mantel, SSH-Multiplexing global, WAL auf allen DBs, ehrlicher Ollama-Fallback, Skill-Trainer mit Sicherheits-Gate
a37fbcf security: persona+context endgueltig untracked
b57b627 security: Persona/Context/Export aus Tracking, Talk-Regel neutralisiert, Cortex ARP-Discovery statt Subnetz-Blindscan
7e4f7ee refactor: errors.db korrekt verdrahtet, ARP-Discovery, set_level config.ini, Persona lokal, Waechter geheilt, private Dateien untracked
3a3a094 fix: intent liest config.ini statt .autonomie_level, Cortex IP-Find auf log_status
1c2301e fix: Schema-Queries auf state/VERIFIED, Briefing-Fehler geloggt, Circuit-Breaker Cooldown+Reset
eb59bdb Circuit Breaker gefixt: Reset nach 300s Cooldown, cb_fail nur bei finalem Fehlschlag, UnboundLocalError behoben
e2d5ff4 fix: Auto-Explore deaktiviert - war zu aggressiv
647cbd8 fix: _termux_cmd definiert, /ssh funktioniert mit echtem Output

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-17 14:40:05] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-17 14:40:05] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-17 14:40:08] EXPLORE | Xiaomi: CPU=Load: 4.39 RAM=1812MB frei Akku=100% Temp=32.3C
[2026-08-17 14:40:08] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 14:45:08] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-17 14:45:08] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-17 14:45:11] EXPLORE | Xiaomi: CPU=Load: 4.89 RAM=1916MB frei Akku=100% Temp=34.4C
[2026-08-17 14:45:11] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 14:50:11] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-17 14:50:11] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-17 14:50:14] EXPLORE | Xiaomi: CPU=Load: 3.79 RAM=1911MB frei Akku=100% Temp=32.2C
[2026-08-17 14:50:14] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 14:55:14] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-17 14:55:14] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-17 14:55:17] EXPLORE | Xiaomi: CPU=Load: 4.79 RAM=2366MB frei Akku=100% Temp=31.9C
[2026-08-17 14:55:17] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 15:00:26] EXPLORE | Xiaomi: CPU=Load: 4.18 RAM=2377MB frei Akku=100% Temp=31.8C
[2026-08-17 15:00:26] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 15:05:30] EXPLORE | Xiaomi: CPU=Load: 4.03 RAM=2604MB frei Akku=100% Temp=32.0C
[2026-08-17 15:05:30] SHADOW-FIXER | Keine offenen Fehler

## Budget heute
Heute: Text 45/300 | Vision 0/40 | Tokens 262040