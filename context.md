# JACK LIVE-KONTEXT (auto, 2026-08-06T11:40:25.958915)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-06T11:40:25.950889

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
- Dima ist LKW-Fahrer mit Sprinter Kühlkoffer bei Dalhoff Feinkost in Achim (Nachtschicht), kein Fernfahrer.
- Dima ist Hobby-Programmierer.
- Dima hat mit 28 einen Burnout gehabt und sich selbst daraus gezogen.
- Dima sucht mit JACK Unabhängigkeit und Freiheit.
- Dima hat den Befehl gegeben, ins Verzeichnis `~/jack/titan_legacy` zu wechseln und eine Datei von GitHub zu laden.
- JACK ist ein autonomes, lokales AI-OS auf Dimas Honor Magic8 Pro.
- JACK nutzt Gemini als Denkwerkzeug über API-Calls.
- JACK hat ein lokales Gedächtnis in SQLite.
- JACK soll sich selbst lernen und verbessern.
- JACK steht unter Dimas voller Kontrolle.
- JACK hat KEINEN direkten Shell- oder Dateizugriff über den Chat.
- JACK kann das Xiaomi 11T Pro per SSH ansprechen.
- JACK verfügt über Fähigkeiten wie Speichermanagement, Sicherheit und Automatisierung.
- Dima ist kein Fernfahrer.
- Dima hat KEINEN Hund.
- Dima hat auf Xiaomi in Termux sshd eingegeben.
- Dima hat eine autobiographische Information hochgeladen, die JACK durchsuchen soll.
- Dima hat die Anweisung gegeben, in Zukunft bei bestimmten Fragen länger zu antworten.
- Dima ist Autodidakt im Programmieren.

## Aktive Module (75)
- install_litert.py
- jack_agent.py
- jack_android.py
- jack_approval.py
- jack_audit.py
- jack_autonomous.py
- jack_briefing.py
- jack_budget.py
- jack_bug_fixer.py
- jack_claude.py
- jack_code_writer.py
- jack_coder.py
- jack_config.py
- jack_consolidate.py
- jack_cortex.py
- jack_gemini_bridge.py
- jack_haliza.py
- jack_handshake_gen.py
- jack_hey.py
- jack_improve.py
- jack_install.py
- jack_intent.py
- jack_learn.py
- jack_log.py
- jack_math.py
- jack_memory.py
- jack_memory_engine.py
- jack_memory_maintenance.py
- jack_missions.py
- jack_monitor.py
- jack_node_alpha.py
- jack_operator.py
- jack_oracle.py
- jack_patch.py
- jack_patch_memory.py
- jack_personality.py
- jack_publish.py
- jack_radar.py
- jack_sanity.py
- jack_scout.py
- jack_screen_tracker.py
- jack_self_improve.py
- jack_selftest.py
- jack_sensors.py
- jack_skill_builder.py
- jack_skills.py
- jack_skills_db.py
- jack_snapshot.py
- jack_talk.py
- jack_telegram.py
- jack_thermal.py
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
- Erinnerungen: 185
- Dienste:
run: jack_cortex: (pid 14887) 552s
run: jack_telegram: (pid 20267) 19s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 8054) 12766s

## Letzte Aenderungen
b2cea51 intent: xiaomi_status als alias, /level ohne space
1e815d7 talk: few-shot beispiel + mindestlaenge persoenliche fragen | telegram: merke-dir handler
081dbf8 talk: context persoenlicher, nicht ausweichen, kumpel-ton
54df78d bridge: system-prompt reste entfernt, sauber
dfc28fd bridge: system-prompt persoenlicher kumpel-ton, dima-kontext tief
32f837e config: get_val als alias | telegram: /trace zeigt live-zustand jack
1fcafcc session 2026-08-06: 19 bugs gefixt, rag aktiv, oracle instant, voice thread, publisher live
9cb6fe1 autonomous: sanity-thread alle 6h | selftest: temp-schwelle 43->50C
a6e20e4 vecdb: vec0.so absoluter pfad mit expanduser
66eb8c3 memory: save() alle 7 spalten inkl timestamp+source
af861c5 cortex: ssh statt ping, find_xiaomi nur bei fail, root-user fix | memory: save() spalten fix | vecdb: expanduser
303fa37 telegram: oracle-block komplett neu ohne kaputte f-strings
53ea18f telegram: oracle newlines, voice thread, doppel-callback weg | cortex: scan-range fix, find_xiaomi nur bei fail
ef0f434 oracle: direkte subprocess-ausfuehrung statt git-roundtrip, sofortiges ergebnis
13219bf telegram: shebang-fix, kortex sicherer import, voice in thread, hardcode-pfade weg

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

15. Memory: save() Spaltenanzahl-Bug (7 statt 5)
16. VecDB: vec0.so absoluter Pfad - RAG war seit Monaten blind
17. Thermal: Negative Werte (mmw3 -273000) rausfiltern
18. Selftest: jack_selftest.py gebaut - ein Befehl, alles gruen/rot
STATUS: 4/4 Dienste gruen. vec0 laedt, 172 Embeddings verfuegbar.
[2026-08-06 10:53:39] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-08-06 10:55:01] SCOUT-LAUF | 021e2908c65a8686
[2026-08-06 10:55:39] SANITY-ERR | module 'jack_sanity' has no attribute 'check'
[2026-08-06 10:55:48] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-08-06 10:55:50] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-08-06 10:57:10] SCOUT-LAUF | 378a903516f59d33
[2026-08-06 10:57:48] SANITY-ERR | module 'jack_sanity' has no attribute 'check'
[2026-08-06 10:59:50] MONITOR-VOLLSCAN | ok
[2026-08-06 11:00:00] CONSOLIDATE | Session gespeichert: 10 Logs, 0 Zugriffe
[2026-08-06 11:16:10] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-08-06 11:16:11] PROFIL-UPDATE | 7 neue Eintraege in kortex_profile.json
[2026-08-06 11:17:31] SCOUT-LAUF | a77d073fbbb0fdfc
[2026-08-06 11:18:10] SANITY-ERR | module 'jack_sanity' has no attribute 'check'
[2026-08-06 11:31:10] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-08-06 11:31:10] SELF-IMPROVE | Tagescheck abgeschlossen

## Budget heute
Heute: Text 45/300 | Vision 0/40 | Tokens 66996