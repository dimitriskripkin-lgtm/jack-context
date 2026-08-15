# JACK LIVE-KONTEXT (auto, 2026-08-15T11:25:07.135340)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-15T11:25:07.119884

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
- Dima ist LKW-Fahrer mit Sprinter Kühlkoffer bei Dalhoff Feinkost in Achim (Nachtschicht).
- Dima ist KEIN Fernfahrer.
- Dima hat KEINEN Hund.
- Dima ist Hobby-Programmierer und Autodidakt, entwickelt hauptsächlich auf dem Smartphone.
- Dima hat mit 28 einen Burnout gehabt und sich selbst daraus gezogen (Stoizismus, Jung, Kiyosaki).
- Dima hat eine Investmentwohnung in Essen.
- Dima möchte mit JACK Unabhängigkeit und Freiheit aufbauen.
- JACK ist das Exit-Vehicle für Dimas Freiheit und Unabhängigkeit.
- JACK ist ein autonomes, lokales AI-OS auf Dimas Honor Magic8 Pro.
- JACK nutzt Gemini als Denkwerkzeug über API-Calls.
- JACK nutzt ollama llama3.2:3b als Offline-Fallback für Gemini.
- JACK verwendet sqlite-vec als Vektordatenbank.
- JACK steht unter Dimas voller Kontrolle.
- JACK kann das Xiaomi 11T Pro per SSH ansprechen, die Verbindung ist aber häufig instabil.
- JACK hat KEINEN direkten Shell- oder Dateizugriff über den Chat.
- JACK ist "Just Autonomous Command Kit" und soll offline-first agieren.
- Dima hat einen Telegram Bot @jackdimachat_bot als Interface.

## Aktive Module (109)
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
- jack_db_optimizer.py
- jack_db_queue.py
- jack_delta.py
- jack_episoden.py
- jack_gedanken.py
- jack_gemini_bridge.py
- jack_groq_bridge.py
- jack_guard.py
- jack_haliza.py
- jack_handshake_gen.py
- jack_hey.py
- jack_improve.py
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
- jack_patch.py
- jack_patch_memory.py
- jack_personality.py
- jack_publish.py
- jack_queue.py
- jack_radar.py
- jack_reflexion.py
- jack_research_curator.py
- jack_rhythm.py
- jack_router.py
- jack_sanity.py
- jack_scheduler.py
- jack_scout.py
- jack_screen_tracker.py
- jack_self_audit.py
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
- Erinnerungen: 416
- Dienste:
run: jack_cortex: (pid 7269) 89098s
run: jack_telegram: (pid 32165) 2248s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 7266) 89098s

## Letzte Aenderungen
f911e83 fix: intent Callback Einzug + Startup-Nachricht bei Neustart
839329b feat: /befehle und /menu direkt in handle() als Buttons
d5bb993 docs: README.md CTO-Portfolio + jack_queue fix
2690fd5 fix: TaskQueue.execute() implementiert
51d4754 fix: jack_queue.py erstellt - ModuleNotFoundError behoben
2d2e037 fix: handle() ruft jack_talk auf statt text zu echoen
e42282a fix: Intent-Ergebnis direkt returnen, Gemini ueberspringen
1564db0 fix: proaktiv_check Basis-Confidence auf 0.75
72e1f3d fix: proaktiv_check Confidence-Threshold auf 0.60 gesenkt
da535b4 fix: proaktiv_check Level 3 in AKTIONEN-Dict
a0a1025 feat: proaktiv_check Handler in jack_intent.execute()
d48bd86 feat: proaktiv_check Intent - sei proaktiv triggert echten System+Xiaomi Check
c4bf10b feat(autonomy): add orchestrator for xiaomi auto-healing and morning briefing
f7289d5 fix(telegram): return early on xiaomi inspect and fix tuple unpacking for fetch_and_process_url
99c8a99 fix(telegram): use updated fetch_and_ingest_url method

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-15 11:03:15] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-15 11:03:15] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-15 11:03:18] EXPLORE | Xiaomi: CPU=Load: 4.73 RAM=2453MB frei Akku=100% Temp=32.9C
[2026-08-15 11:03:18] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 11:08:18] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-15 11:08:18] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-15 11:08:21] EXPLORE | Xiaomi: CPU=Load: 3.81 RAM=2571MB frei Akku=100% Temp=32.9C
[2026-08-15 11:08:21] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 11:13:22] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-15 11:13:22] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-15 11:13:24] EXPLORE | Xiaomi: CPU=Load: 4.84 RAM=2552MB frei Akku=100% Temp=33.1C
[2026-08-15 11:13:24] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 11:18:25] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-15 11:18:25] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-15 11:18:28] EXPLORE | Xiaomi: CPU=Load: 4.16 RAM=2812MB frei Akku=100% Temp=33.4C
[2026-08-15 11:18:28] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 11:23:28] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-15 11:23:28] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-15 11:23:31] EXPLORE | Xiaomi: CPU=Load: 3.94 RAM=2663MB frei Akku=100% Temp=33.4C
[2026-08-15 11:23:31] SHADOW-FIXER | Keine offenen Fehler

## Budget heute
Heute: Text 17/300 | Vision 0/40 | Tokens 76515