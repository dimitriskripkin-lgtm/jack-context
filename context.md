# JACK LIVE-KONTEXT (auto, 2026-08-15T01:42:20.296247)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-15T01:42:20.281603

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
- JACK ist "Just Autonomous Command Kit" und soll offline-first agieren.
- Dima entwickelt hauptsächlich auf dem Smartphone.
- Dima hat eine Investmentwohnung in Essen.
- Dima hat einen Telegram Bot @jackdimachat_bot als Interface.
- JACK nutzt ollama llama3.2:3b als Offline-Fallback für Gemini.
- JACK verwendet sqlite-vec als Vektordatenbank.

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
- Erinnerungen: 303
- Dienste:
run: jack_cortex: (pid 7269) 54131s
run: jack_telegram: (pid 5400) 6819s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 7266) 54131s

## Letzte Aenderungen
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
0741870 fix(web_ingest): add browser headers and fallback chunking for quiet sites
3f169c1 feat(research): fix function call in curator module and test knowledge distillation
35035f0 feat(telegram): fix syntax and integrate xiaomi inspector + web ingest

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-15 00:53:50] EXPLORE | Xiaomi: CPU=Load: 3.33 RAM=2325MB frei Akku=100% Temp=30.8C
[2026-08-15 00:53:50] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 00:58:53] EXPLORE | Xiaomi: CPU=Load: 4.64 RAM=2150MB frei Akku=100% Temp=31.1C
[2026-08-15 00:58:53] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 01:03:57] EXPLORE | Xiaomi: CPU=Load: 4.08 RAM=2187MB frei Akku=100% Temp=30.8C
[2026-08-15 01:03:57] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 01:09:00] EXPLORE | Xiaomi: CPU=Load: 4.34 RAM=1843MB frei Akku=100% Temp=30.8C
[2026-08-15 01:09:00] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 01:14:03] EXPLORE | Xiaomi: CPU=Load: 4.03 RAM=1788MB frei Akku=100% Temp=31.5C
[2026-08-15 01:14:03] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 01:19:07] EXPLORE | Xiaomi: CPU=Load: 4.33 RAM=1838MB frei Akku=100% Temp=30.9C
[2026-08-15 01:19:07] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 01:24:10] EXPLORE | Xiaomi: CPU=Load: 4.33 RAM=1810MB frei Akku=100% Temp=30.8C
[2026-08-15 01:24:10] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 01:29:13] EXPLORE | Xiaomi: CPU=Load: 4.48 RAM=2097MB frei Akku=100% Temp=30.6C
[2026-08-15 01:29:13] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 01:34:16] EXPLORE | Xiaomi: CPU=Load: 3.96 RAM=1995MB frei Akku=100% Temp=30.5C
[2026-08-15 01:34:16] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 01:39:19] EXPLORE | Xiaomi: CPU=Load: 4.23 RAM=1900MB frei Akku=100% Temp=30.7C
[2026-08-15 01:39:19] SHADOW-FIXER | Keine offenen Fehler

## Budget heute
Heute: Text 7/300 | Vision 0/40 | Tokens 18701