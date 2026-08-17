# JACK LIVE-KONTEXT (auto, 2026-08-17T16:37:08.855590)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-17T16:37:08.840288

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
## Aktive Module (128)
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
- Erinnerungen: 1052
- Dienste:
run: jack_cortex: (pid 25040) 16853s
run: jack_telegram: (pid 26547) 363s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 18563) 95249s

## Letzte Aenderungen
8dfc03c fix: TUEV3 Signaturen korrigiert (exec String, critic Tupel)
a32dee7 fix: TUEV1 schliesst auch tuev2.py aus Leak-Scan aus
aab8759 fix: Dienste-Liste korrekt (kein jack_autolearn/publisher), _xi() nutzt SSH-Alias, collect_status kein ping+alte-IP, update_identity atomic
d59b710 fix: errors/akku/log/level im Router, TUEV3 Signaturen korrigiert
[PRIVAT GEFILTERT]
cc22923 fix: TUEV-Regex jack_publish.py ausgenommen (Filter-Regeln sind keine Leaks), NOTIFY-Fehler resolved
48f22ff fix: threading-Import, ERRORS_DB korrekt, Gemini-Fallback [:3000] weg, duplikaten Callback-Handler entfernt
aa15766 fix: jack_voice_el.py Stub - verhindert crash in Voice-Loop, Groq-Quelle ermitteln
d04325b fix: [:3800]-Kuerzer korrekt entfernt via Python-Replace (sed hat auf Android versagt)
2a04d63 fix: send()-Splitter aktiv - [:3800]-Kuerzer aus Router entfernt, push()->build() im Waechter, Privat-Filter fuer context.md
1c8234a security: CLAUDE.md + Alt-Handshakes + Verhaltensprofil untracked, TUEV-Pruefstand aufgenommen, Regex praezisiert
a4eca6d feat: deterministischer Befehls-Router mit Gemini-Catch-All, Prompt-Konsistenz + Marker-Verbot, Skill-Builder auf Trainer-Schema via Mantel
9d13c5a feat: Voll-Button-Bedienung - cmd:-Callback routet Buttons durch handle(), Kategorie-Menues als Tap-Grids, Ketten-Schnellwahl
539bcc2 fix: /kette und /bugfix Handler verdrahtet - Menue war Attrappe, jetzt feuern jack_chains und jack_bugfix_loop
6a0a734 security: DBs untracked, Anti-Halluzinations-Regel, Test-Eintrag resolved

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-17 16:32:43] TUEV-ERR | Kanaltest
[2026-08-17 16:32:59] MONITOR-VOLLSCAN | ok
[2026-08-17 16:32:59] TUEV2-ERR-0 | Lasttest Eintrag 0
[2026-08-17 16:32:59] TUEV2-ERR-1 | Lasttest Eintrag 1
[2026-08-17 16:32:59] TUEV2-ERR-2 | Lasttest Eintrag 2
[2026-08-17 16:32:59] TUEV2-ERR-3 | Lasttest Eintrag 3
[2026-08-17 16:32:59] TUEV2-ERR-4 | Lasttest Eintrag 4
[2026-08-17 16:32:59] TUEV2-ERR-5 | Lasttest Eintrag 5
[2026-08-17 16:32:59] TUEV2-ERR-6 | Lasttest Eintrag 6
[2026-08-17 16:32:59] TUEV2-ERR-7 | Lasttest Eintrag 7
[2026-08-17 16:32:59] TUEV2-ERR-8 | Lasttest Eintrag 8
[2026-08-17 16:32:59] TUEV2-ERR-9 | Lasttest Eintrag 9
[2026-08-17 16:33:06] MONITOR-VOLLSCAN | ok
[2026-08-17 16:33:12] MONITOR-VOLLSCAN | ok
[2026-08-17 16:33:18] MONITOR-VOLLSCAN | ok
[2026-08-17 16:34:42] MONITOR-VOLLSCAN | ok
[2026-08-17 16:34:47] MONITOR-VOLLSCAN | ok
[2026-08-17 16:34:52] MONITOR-VOLLSCAN | ok
[2026-08-17 16:36:10] EXPLORE | Xiaomi: CPU=Load: 4.23 RAM=2118MB frei Akku=100% Temp=32.2C
[2026-08-17 16:36:10] SHADOW-FIXER | Keine offenen Fehler

## Budget heute
Heute: Text 67/300 | Vision 0/40 | Tokens 324514