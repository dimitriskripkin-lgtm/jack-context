# JACK LIVE-KONTEXT (auto, 2026-08-15T20:16:15.782718)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-15T20:16:15.761130

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
- Erinnerungen: 526
- Dienste:
run: jack_cortex: (pid 7269) 120966s
run: jack_telegram: (pid 26098) 20365s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 7266) 120966s

## Letzte Aenderungen
960515b fix: Foto-Handler im Poll-Loop wiederhergestellt
1727af6 fix: voice Handler im Poll-Loop wiederhergestellt
0d7429d fix: /selftest direkt in handle() verankert
f5ee770 fix: Level 3 Handlungs-Direktive in Persona
b7afff2 fix: Intent nur bei kurzen Texten <60 Zeichen ausfuehren
f16399f fix: ssh_check kein einzelnes 'xiaomi' mehr als Keyword
958d945 fix: nachfragen deaktiviert - kein Intent-Prompt bei Fliesstext
5890033 fix: proaktiv_check Keywords praeziser - kein Fliesstext-Match
28bed1b fix: xiaomi_akku Keywords praeziser - kein Substring-Match mehr
8cd6357 fix: xiaomi inspector trigger eingeschraenkt - nur bei explizitem Befehl
c4d488a feat: /befehle Xiaomi Akku Button + Honor Akku getrennt
623ef5a fix: xiaomi_akku via su -c statt dumpsys
9ae43fd fix: xiaomi_akku Keywords Prioritaet vor ssh_check
cc71719 feat: Haptik-Feedback via termux-vibrate bei Startup, Button, Nachricht
6b5d942 feat: xiaomi_akku Intent + xiaomi_wake via ControlMaster

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-15 19:28:53] EXPLORE | Xiaomi: CPU=Load: 3.61 RAM=2765MB frei Akku=100% Temp=32.0C
[2026-08-15 19:28:53] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 19:33:57] EXPLORE | Xiaomi: CPU=Load: 4.11 RAM=2960MB frei Akku=100% Temp=32.3C
[2026-08-15 19:33:57] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 19:39:00] EXPLORE | Xiaomi: CPU=Load: 3.30 RAM=2918MB frei Akku=100% Temp=33.0C
[2026-08-15 19:39:00] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 19:44:03] EXPLORE | Xiaomi: CPU=Load: 3.89 RAM=2794MB frei Akku=100% Temp=33.9C
[2026-08-15 19:44:04] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 19:49:07] EXPLORE | Xiaomi: CPU=Load: 4.90 RAM=2529MB frei Akku=100% Temp=34.0C
[2026-08-15 19:49:07] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 19:54:10] EXPLORE | Xiaomi: CPU=Load: 4.02 RAM=2548MB frei Akku=100% Temp=30.0C
[2026-08-15 19:54:10] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 19:59:13] EXPLORE | Xiaomi: CPU=Load: 4.08 RAM=2236MB frei Akku=100% Temp=32.1C
[2026-08-15 19:59:13] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 20:04:17] EXPLORE | Xiaomi: CPU=Load: 4.06 RAM=2461MB frei Akku=100% Temp=31.8C
[2026-08-15 20:04:17] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 20:09:20] EXPLORE | Xiaomi: CPU=Load: 3.54 RAM=2473MB frei Akku=100% Temp=31.4C
[2026-08-15 20:09:20] SHADOW-FIXER | Keine offenen Fehler
[2026-08-15 20:14:23] EXPLORE | Xiaomi: CPU=Load: 3.55 RAM=2222MB frei Akku=100% Temp=32.0C
[2026-08-15 20:14:23] SHADOW-FIXER | Keine offenen Fehler

## Budget heute
Heute: Text 48/300 | Vision 0/40 | Tokens 204057