# JACK LIVE-KONTEXT (auto, 2026-08-16T10:46:50.416298)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-16T10:46:50.403509

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
- Dima ist LKW-Fahrer mit Sprinter Kühlkoffer bei Dalhoff Feinkost in Achim (Nachtschicht).
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
- Dima hat KEINEN Hund.
- Dima ist LKW-Fahrer mit Sprinter Kühlkoffer, KEIN Fernfahrer.

## Aktive Module (110)
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
- jack_subagent.py
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
- Erinnerungen: 701
- Dienste:
run: jack_cortex: (pid 7269) 173201s
run: jack_telegram: (pid 9861) 75s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 7266) 173201s

## Letzte Aenderungen
02e464c feat: WRITE-Marker - Gemini kann Dateien direkt vorschlagen mit Auto-Button
536d602 fix: Persona - nie behaupten etwas getan zu haben ohne Ausfuehrung
ae6d02c fix: Persona klargestellt - JACK kann Dateien schreiben
af70869 fix: datei_schreiben mit Inline-Button in handle() verdrahtet
b700c5e fix: datei_schreiben korrekt in elif-Kette - kein unbekannt mehr
7580954 fix: propose_write -> propose in datei_schreiben
cd293bb fix: _pre -> d in datei_schreiben handler
4bb67cd feat: datei_schreiben Intent eingebaut
d8a9411 fix: Live-Fakten als unveraenderliche Zone - kein Halluzinieren mehr
5586887 fix: ssh_check Keywords fuer Erreichbarkeit erweitert
0191092 fix: Intent nur bei echten Befehlen - Start-Wort oder kurze Nachricht
d18fc63 feat: Rolling Window - letzte 10 Nachrichten im RAM fuer Gemini-Kontext
2d0afbd fix: schreib und proaktiv Intent auch bei langen Saetzen
960515b fix: Foto-Handler im Poll-Loop wiederhergestellt
1727af6 fix: voice Handler im Poll-Loop wiederhergestellt

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-16 10:33:37] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-16 10:33:39] EXPLORE | Xiaomi: CPU=Load: 5.79 RAM=2412MB frei Akku=100% Temp=31.6C
[2026-08-16 10:33:39] SHADOW-FIXER | Keine offenen Fehler
[2026-08-16 10:34:43] DATEI-SCHREIBEN | test.txt | 10 Zeichen
[2026-08-16 10:34:48] GUARD-OK | whisper gestartet, 2811MB frei
[2026-08-16 10:35:24] GUARD-OK | whisper gestartet, 2966MB frei
[2026-08-16 10:35:54] GUARD-OK | whisper gestartet, 2852MB frei
[2026-08-16 10:38:00] GUARD-OK | whisper gestartet, 2727MB frei
[2026-08-16 10:38:40] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-16 10:38:40] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-16 10:38:42] EXPLORE | Xiaomi: CPU=Load: 4.29 RAM=2286MB frei Akku=100% Temp=31.7C
[2026-08-16 10:38:42] SHADOW-FIXER | Keine offenen Fehler
[2026-08-16 10:38:43] GUARD-OK | whisper gestartet, 3253MB frei
[2026-08-16 10:41:40] GUARD-OK | whisper gestartet, 2989MB frei
[2026-08-16 10:42:49] GUARD-OK | whisper gestartet, 3012MB frei
[2026-08-16 10:43:24] GUARD-OK | whisper gestartet, 2971MB frei
[2026-08-16 10:43:43] SELF-AUDIT | SYSTEM_STATE.md generiert
[2026-08-16 10:43:43] SCHEDULER | Power-Time aktiv - schwere Jobs erlaubt
[2026-08-16 10:43:45] EXPLORE | Xiaomi: CPU=Load: 3.46 RAM=2280MB frei Akku=100% Temp=31.5C
[2026-08-16 10:43:45] SHADOW-FIXER | Keine offenen Fehler

## Budget heute
Heute: Text 43/300 | Vision 0/40 | Tokens 145305