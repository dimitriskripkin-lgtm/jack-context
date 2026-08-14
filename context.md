# JACK LIVE-KONTEXT (auto, 2026-08-14T18:27:18.105057)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-14T18:27:18.093549

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

## Aktive Module (102)
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
- jack_guard.py
- jack_haliza.py
- jack_handshake_gen.py
- jack_hey.py
- jack_improve.py
- jack_install.py
- jack_intent.py
- jack_learn.py
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
- Erinnerungen: 265
- Dienste:
run: jack_cortex: (pid 7269) 28029s
run: jack_telegram: (pid 6690) 1164s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 7266) 28029s

## Letzte Aenderungen
a4829a5 feat: jack_db_optimizer.py + SYSTEM_STATE.md (Qwen build)
f04370e fix: Handlungs-Regel - reden vs handeln
3ec30b6 fix: persona anti-repeat - zeigen statt nacherzaehlen
c9ae8d6 fix: anti-repetitions-regel in persona
1503a4b fix: persona Datei-Faehigkeit + Temperatur-Guard 58C Schwelle
b3f71b7 feat: confirm_write/cancel_write Callback verdrahtet
6a1fd6a fix: send_keyboard tuple format fuer Schreibvorschlag-Buttons
b312e40 fix: Schreibvorschlag -> Inline-Button statt Text
a6a3990 feat(agent): add lightweight web agent engine with domain recipe storage
8536a2c feat(core): add tiered memory consolidation and multi-file shadow execution engine
a144af1 feat(cron): add 06:00 AM daily briefing cronjob script and crontab integration
62deb53 feat(core): add non-blocking whisper, procedural rhythm engine and stale memory marking
e511931 docs: authentic CTO-grade README based on live system state
084d9b9 feat(rag): implement working context ingest pipeline with md5 dedup and html cleaner
d2e2087 Revert "docs: professional CTO-outreach portfolio README"

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-14 16:53:13] MONITOR-EVENT | 1 Events
[2026-08-14 17:08:57] GUARD-OK | whisper gestartet, 2518MB frei
[2026-08-14 17:34:25] MERKE-DIR | für die Zukunft immer mit das als Copy und Paste für mein Termux geben
[2026-08-14 17:39:42] DATEI-SCHREIBEN | hallobro_20260814_1739.txt | 8 Zeichen
[2026-08-14 17:39:55] GUARD-OK | whisper gestartet, 2387MB frei
[2026-08-14 17:42:31] DATEI-SCHREIBEN | 20260814_1742_hallobro.txt | 8 Zeichen
[2026-08-14 17:43:15] DATEI-SCHREIBEN | thermox_commands_20260814.log | 38 Zeichen
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

## Budget heute
Heute: Text 128/300 | Vision 0/40 | Tokens 355892