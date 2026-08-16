# JACK LIVE-KONTEXT (auto, 2026-08-17T01:25:48.336064)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-17T01:25:48.322429

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
- Dima ist LKW-Fahrer im Nachtdienst bei Dalhoff Feinkost in Achim und fährt einen Sprinter Kühlkoffer.
- Dima hat KEINEN Hund.
- Dima ist Hobby-Programmierer und Autodidakt, entwickelt hauptsächlich auf dem Smartphone.
- Dima hat mit 28 einen Burnout gehabt und sich selbst daraus gezogen (Stoizismus, Jung, Kiyosaki).
- Dima besitzt eine Investmentwohnung in Essen.
- Mit JACK baut Dima an seiner Freiheit und Unabhängigkeit.
- JACK ist ein autonomes, lokales AI-OS, das auf Dimas Honor Magic8 Pro läuft.
- JACK nutzt Gemini per API-Calls als Haupt-Denkwerkzeug.
- JACK hat ollama llama3.2:3b als Offline-Fallback.
- JACK verwendet sqlite-vec als Vektordatenbank.
- Dima behält die volle Kontrolle über JACK.
- JACK kann das Xiaomi 11T Pro per SSH ansprechen, die Verbindung ist aber oft instabil.
- JACK ist "Just Autonomous Command Kit" und legt Wert auf Offline-Fähigkeit.
- Dimas Interface zu JACK ist ein Telegram Bot namens @jackdimachat_bot.

## Aktive Module (122)
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
- jack_skills.py
- jack_skills_db.py
- jack_snapshot.py
- jack_state.py
- jack_subagent.py
- jack_talk.py
- jack_telegram.py
- jack_thermal.py
- jack_traceback.py
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
- Offene Fehler: 0
- Erinnerungen: 874
- Dienste:
run: jack_cortex: (pid 18928) 26449s
run: jack_telegram: (pid 11952) 27124s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 18563) 40569s

## Letzte Aenderungen
e2d5ff4 fix: Auto-Explore deaktiviert - war zu aggressiv
647cbd8 fix: _termux_cmd definiert, /ssh funktioniert mit echtem Output
fc25048 feat: /ssh Befehl - direkter SSH-Output ohne Gemini-Umweg
c551a46 fix: netz_da multi-URL, agent immer Dollar-Prefix fuer SSH
569eb34 feat: /agent - ReAct UI-Agent mit Gemini live auf Xiaomi
33fd615 inbox: System Health Check v3
ce68d65 inbox: System Health Check v2
79401fc inbox: Outcome Types Test
d412483 inbox: Retest
7a4c36c inbox: Level4 Mission 3 - Lernlog
bc1e4bb inbox: Level4 Mission 2 - Xiaomi Kontrolle
f9d8024 inbox: Level4 Mission 1 - Systemstatus
4a83395 feat: jack_explorer_deep
59dceef fix: explore pm list mit su -c, max_apps auf 50 erhoeht
c46791f feat: Skill-Lifecycle verifiziert - CANDIDATE/TESTING/VERIFIED live

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-17 00:38:25] EXPLORE | Xiaomi: CPU=Load: 4.35 RAM=2271MB frei Akku=100% Temp=33.6C
[2026-08-17 00:38:25] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 00:43:28] EXPLORE | Xiaomi: CPU=Load: 6.33 RAM=1812MB frei Akku=100% Temp=33.8C
[2026-08-17 00:43:28] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 00:48:31] EXPLORE | Xiaomi: CPU=Load: 4.33 RAM=1838MB frei Akku=100% Temp=33.3C
[2026-08-17 00:48:31] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 00:53:35] EXPLORE | Xiaomi: CPU=Load: 4.68 RAM=1729MB frei Akku=100% Temp=33.5C
[2026-08-17 00:53:35] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 00:58:37] EXPLORE | Xiaomi: CPU=Load: 4.34 RAM=1753MB frei Akku=100% Temp=33.4C
[2026-08-17 00:58:37] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 01:03:41] EXPLORE | Xiaomi: CPU=Load: 4.30 RAM=1798MB frei Akku=100% Temp=33.3C
[2026-08-17 01:03:41] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 01:08:44] EXPLORE | Xiaomi: CPU=Load: 4.46 RAM=1795MB frei Akku=100% Temp=33.4C
[2026-08-17 01:08:44] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 01:13:47] EXPLORE | Xiaomi: CPU=Load: 4.05 RAM=1926MB frei Akku=100% Temp=33.4C
[2026-08-17 01:13:47] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 01:18:50] EXPLORE | Xiaomi: CPU=Load: 4.56 RAM=1946MB frei Akku=100% Temp=33.4C
[2026-08-17 01:18:50] SHADOW-FIXER | Keine offenen Fehler
[2026-08-17 01:23:54] EXPLORE | Xiaomi: CPU=Load: 4.11 RAM=2464MB frei Akku=100% Temp=33.1C
[2026-08-17 01:23:54] SHADOW-FIXER | Keine offenen Fehler

## Budget heute
Heute: Text 1/300 | Vision 0/40 | Tokens 5117