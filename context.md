# JACK LIVE-KONTEXT (auto, 2026-08-14T21:35:16.969745)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-14T21:35:16.960242

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

## Aktive Module (105)
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
- jack_patch.py
- jack_patch_memory.py
- jack_personality.py
- jack_publish.py
- jack_radar.py
- jack_reflexion.py
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
- Erinnerungen: 277
- Dienste:
run: jack_cortex: (pid 7269) 39307s
run: jack_telegram: (pid 30926) 7478s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 7266) 39307s

## Letzte Aenderungen
e071cac feat(ingest): add jack_web_ingest module with html cleaning and rag chunking
f805527 docs: restore full CTO portfolio README via clean python writer
b9679da docs: add CTO portfolio README via base64 stream
6560a7b feat: Groq bekommt RAG-Memories + Identity-Kontext
1c43d1e fix: /status KeyError cortex behoben
4b0396b fix: Groq-Keywords erweitert inkl Umlaute
e94f4cb feat: Groq llama3.3-70b fuer persoenliche Gespraeche, Gemini fuer System-Calls
835e862 fix: JACK kann Dateien schreiben - Falschaussage korrigiert
d178737 fix: voice fast-lane vor shebang entfernt, korrekt nach imports platziert
a604bdd feat(voice): wire live voice bridge fast-lane into telegram bot
4de7c2e feat(voice): add ultra-low latency live voice bridge module prototype
8bf30b7 refactor(talk): move system constraints to bottom of prompt with strict XML tags
f0a4853 fix: hardcoded Beispiel-Text aus Gemini-Prompt entfernt - nur noch jack_persona.md
4f208ed feat(persona): komplette Neufassung - Titan-Geschichte + Levelsystem + Anti-Repetition
a4829a5 feat: jack_db_optimizer.py + SYSTEM_STATE.md (Qwen build)

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-14 17:43:34] GUARD-OK | whisper gestartet, 2522MB frei
[2026-08-14 17:44:59] GUARD-OK | whisper gestartet, 2659MB frei
[2026-08-14 17:45:56] GUARD-OK | whisper gestartet, 3023MB frei
[2026-08-14 17:47:15] GUARD-OK | whisper gestartet, 2827MB frei
[2026-08-14 17:57:20] GUARD-OK | whisper gestartet, 2432MB frei
[2026-08-14 17:58:20] GUARD-OK | whisper gestartet, 2517MB frei
[2026-08-14 18:00:40] GUARD-OK | whisper gestartet, 2826MB frei
[2026-08-14 18:03:45] GUARD-OK | whisper gestartet, 2862MB frei
[2026-08-14 18:06:10] GUARD-OK | whisper gestartet, 3019MB frei
[2026-08-14 18:08:23] GUARD-OK | whisper gestartet, 2807MB frei
[2026-08-14 18:13:37] GUARD-OK | whisper gestartet, 2348MB frei
[2026-08-14 18:14:28] GUARD-OK | whisper gestartet, 2574MB frei
[2026-08-14 18:15:05] GUARD-OK | whisper gestartet, 2879MB frei
[2026-08-14 18:34:43] GUARD-OK | whisper gestartet, 2804MB frei
[2026-08-14 18:44:53] GUARD-OK | whisper gestartet, 2821MB frei
[2026-08-14 19:01:24] GUARD-OK | whisper gestartet, 2629MB frei
[2026-08-14 19:07:27] GUARD-OK | whisper gestartet, 2806MB frei
[2026-08-14 19:22:17] GUARD-OK | whisper gestartet, 2347MB frei
[2026-08-14 19:55:53] GUARD-OK | whisper gestartet, 2606MB frei
[2026-08-14 20:43:09] WAECHTER-MELDUNG | Xiaomi weg

## Budget heute
Heute: Text 171/300 | Vision 0/40 | Tokens 463991