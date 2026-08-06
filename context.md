# JACK LIVE-KONTEXT (auto, 2026-08-06T09:47:32.956877)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-08-06T09:47:32.944586

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
- Dima ist LKW-Fahrer mit Sprinter Kühlkoffer bei Dalhoff Feinkost in Achim (Nachtschicht).
- Dima ist Hobby-Programmierer.
- Dima ist aus Russland nach Deutschland migriert, Baujahr ca. 1996.
- Dima ist Einzelkind.
- JACK ist ein autonomes, lokales AI-OS auf Dimas Honor Magic8 Pro.
- JACK nutzt Gemini als Gehirn (API-Calls).
- JACK hat ein lokales Gedächtnis in SQLite.
- JACK soll sich selbst lernen und verbessern.
- JACK steht unter Dimas voller Kontrolle.
- JACK speichert alle Fragen und Antworten mit Zeitstempel im Gedächtnis.
- Dima hat KEINEN Hund (Rex war nur ein Test).
- JACK hat KEINEN direkten Shell- oder Dateizugriff über den Chat.
- Dima testet das Gedächtnis.
- Dima hat auf Xiaomi in Termux sshd eingegeben.
- Dima hat eine autobiographische Information hochgeladen, die JACK durchsuchen soll.
- Dima hat den Befehl gegeben, ins Verzeichnis `~/jack/titan_legacy` zu wechseln und eine Datei von GitHub zu laden.

## Aktive Module (73)
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
- Erinnerungen: 171
- Dienste:
run: jack_cortex: (pid 10434) 1111997s
run: jack_telegram: (pid 22987) 145844s
fail: jack_autolearn: unable to change to service directory: file does not exist
run: ollama: (pid 8054) 5993s

## Letzte Aenderungen
bc6974f publisher: push() loop-fix, thermal: negative sensor filter
8c08356 publisher: push() statt nur build() im waechter-loop, thermal: negative sensor-werte rausfiltern
b4ecf05 jack_talk: check aus math_signals entfernt - verhinderte Antworten auf Alltagsfragen
81d3f6e Cleanup: Muell-Datei entfernt
951762d Ollama: Vulkan-Env in runit run-Datei, Thermal-Monitor filtert Schwellwerte
8d1dc8b feat: jack_ui.py - schöne Konsolen-Ausgabe mit Farben + Boxen
130c329 feat: Stack B mit Vulkan GPU-Beschleunigung (6.6s statt 35-85s)
67c6321 fix: Watchdog zeigt echtes Limit an (95°C)
5f65efc feat: litert_watchdog.py - Temperatur-sicherer LLM-Runner (85°C Limit)
e7fba45 jack_hey: Loop-Overhead weg, Stille-Pruefung schaltet sich bei lauter Umgebung ab
807a1c3 jack_hey: Standardzeit 5s, Stille-Schwelle -45dB (fahrendes Auto hat -18dB Grundrauschen)
adfd702 jack_hey: Stille-Erkennung - Aufnahme stoppt automatisch nach 2s Ruhe
211513e Voice-Aufraeumen: jack_hey Argument-Bug gefixt, 3 tote Module archiviert, Shortcuts beschriftet
add6692 feat: Router-Logging für Transparenz
9ee8d53 feat: Aufnahmezeit 5s -> 10s

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-08-05 22:16:16] AUTOLEARN-ERR | module 'jack_config' has no attribute 'get_val'
[2026-08-06 00:16:16] AUTOLEARN-ERR | module 'jack_config' has no attribute 'get_val'
[2026-08-06 02:16:16] AUTOLEARN-ERR | module 'jack_config' has no attribute 'get_val'
[2026-08-06 04:16:16] AUTOLEARN-ERR | module 'jack_config' has no attribute 'get_val'
[2026-08-06 04:26:16] MONITOR-NOTIFY-ERR | <urlopen error [Errno 7] No address associated with hostname>
[2026-08-06 04:26:16] MONITOR-EVENT | 1 Events
[2026-08-06 04:50:32] MONITOR-EVENT | 1 Events
[2026-08-06 04:54:34] MONITOR-NOTIFY-ERR | <urlopen error [Errno 7] No address associated with hostname>
[2026-08-06 04:54:34] MONITOR-EVENT | 1 Events
[2026-08-06 05:04:39] MONITOR-NOTIFY-ERR | <urlopen error [Errno 7] No address associated with hostname>
[2026-08-06 05:04:39] MONITOR-EVENT | 1 Events
[2026-08-06 06:00:00] MEMORY-MAINTENANCE | 1 Eintraege als 'stale' markiert | 1 Stale-Eintraege geloescht | Verbleibend: 27 Eintraege
[2026-08-06 06:16:16] AUTOLEARN-ERR | module 'jack_config' has no attribute 'get_val'
[2026-08-06 06:53:29] MONITOR-EVENT | 1 Events
[2026-08-06 07:09:39] MONITOR-EVENT | 1 Events
[2026-08-06 07:55:04] MONITOR-VOLLSCAN | ok
[2026-08-06 08:16:16] AUTOLEARN-ERR | module 'jack_config' has no attribute 'get_val'
[2026-08-06 09:23:17] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-08-06 09:23:17] AUTOLEARN-ERR | module 'jack_config' has no attribute 'get_val'
[2026-08-06 09:24:43] SCOUT-LAUF | 20083632b0872eff

## Budget heute
Heute: Text 7/300 | Vision 0/40 | Tokens 0