# JACK LIVE-KONTEXT (auto, 2026-07-23T20:48:36.271875)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-07-23T20:48:36.256827

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
- JACK speichert alle Fragen und Antworten mit Zeitstempel im Gedächtnis.
- Dima hat auf Xiaomi in Termux sshd eingegeben.
- Dima hat JACK das Ziel gegeben, sich selbst zu lernen und zu verbessern.
- Dima hat JACK das Ziel gegeben, unter seiner Kontrolle zu stehen.
- Dima hat den Befehl gegeben, ins Verzeichnis `~/jack/titan_legacy` zu wechseln und eine Datei von GitHub zu laden.
- Dima ist nicht daran interessiert, Befehle wie `/cost`, `/cc`, `/oracle`, `/oracle_result` auszuführen oder zu verstehen.
- Dima hat KEINEN Hund (Rex war nur ein Test).
- Dima ist LKW-Fahrer mit Sprinter Kuehlkoffer, KEIN Fernfahrer.
- JACK hat KEINEN direkten Shell- oder Dateizugriff ueber den Chat.
- JACK erinnert sich an vergangene Gespräche mit Zeitstempel.

## Aktive Module (55)
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
- jack_handshake_gen.py
- jack_hey.py
- jack_improve.py
- jack_learn.py
- jack_log.py
- jack_math.py
- jack_memory.py
- jack_memory_engine.py
- jack_memory_maintenance.py
- jack_node_alpha.py
- jack_operator.py
- jack_oracle.py
- jack_patch.py
- jack_personality.py
- jack_publish.py
- jack_radar.py
- jack_screen_tracker.py
- jack_self_improve.py
- jack_sensors.py
- jack_skills.py
- jack_snapshot.py
- jack_talk.py
- jack_telegram.py
- jack_v2.py
- jack_vecdb.py
- jack_vinted_radar.py
- jack_voice.py
- jack_voice_el.py
- jack_voice_processor.py
- jack_write.py
- jack_xiaomi.py
- jack_xiaomi_cmd.py
- kortex_controller.py
- kortex_memory.py
- kortex_profile_updater.py
- kortex_profiler.py
- kortex_sensor_daemon.py
- quick_bridge.py
- test_jack_approval.py
- voice_service_v2.py

## System-Status
- Offene Fehler: 1
- Erinnerungen: 157
- Dienste:
run: jack_cortex: (pid 12726) 30434s
run: jack_telegram: (pid 21411) 33164s
run: jack_autolearn: (pid 7339) 209568s
run: ollama: (pid 7342) 209568s

## Letzte Aenderungen
9660995 Security: Shell-Injection-Schutz (Pipes/Chaining geblockt) + alias in Telegram
37b56f6 Oracle: chr(10) statt Newline-Literal + Audit 7/7 Nenner fix
139042b Oracle: Ergebnis automatisch per Telegram nach Ausfuehrung + Audit 7/7
3957896 Audit: 7 Dienste + Oracle UUID auf Millisekunden fuer einzigartige Button-Klicks
fefc1f1 Telegram: Oracle-Dispatcher an Anfang von handle() - Gemini wird nie mehr fuer /oracle aufgerufen
0ed4d1c Telegram: Start-Offset fix wiederhergestellt
72ba9fd Telegram: oracle Callback-Handler in handle_callback
e22d3f9 Telegram: buttons Format fix fuer send_keyboard
58392b1 Telegram: send_buttons -> send_keyboard fix
eba34ba Telegram: oracle+befehle Dispatcher vor Gemini-Fallback eingefuegt
4542529 Telegram: /oracle und /oracle_result Dispatcher wiederhergestellt
76119de Telegram: doppelte handle_callback entfernt, Oracle in Haupt-Handler integriert
cd3655e Cleanup: kritische bare excepts durch logging ersetzt
b8c74eb Telegram: Start-Offset auf neuestes Update gesetzt, kein Backlog mehr
b1b190d Cortex: notify True korrekte Stelle

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.244.147.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-07-23 02:54:13] ORACLE-EINGANG | tg-17847: df -h
[2026-07-23 03:04:40] ORACLE-EINGANG | tg-17847: sv status jack_cortex jack_telegram jack_autolearn jack_publisher jack_waechter
[2026-07-23 03:17:43] ORACLE-EINGANG | tg-17847: sv status jack_cortex jack_telegram jack_autolearn jack_publisher jack_waechter
[2026-07-23 03:19:45] ORACLE-EINGANG | tg-17847: sv status jack_cortex jack_telegram jack_autolearn jack_publisher jack_waechter
[2026-07-23 03:20:01] PROFIL-UPDATE | 2 neue Eintraege in kortex_profile.json
[2026-07-23 05:20:03] PROFIL-UPDATE | 3 neue Eintraege in kortex_profile.json
[2026-07-23 06:00:00] MEMORY-MAINTENANCE | 2 Eintraege als 'stale' markiert | Gesamt: 58 Eintraege | Stale: 12
[2026-07-23 07:20:05] PROFIL-UPDATE | 2 neue Eintraege in kortex_profile.json
[2026-07-23 10:42:22] WAECHTER-NEUSTART | jack_telegram
[2026-07-23 10:42:22] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-07-23 10:42:22] SELF-IMPROVE | Tagescheck abgeschlossen
[2026-07-23 11:00:00] CONSOLIDATE | Session gespeichert: 10 Logs, 0 Zugriffe
[2026-07-23 11:01:07] ORACLE-EINGANG | btn-1784: ollama list
[2026-07-23 11:20:10] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-23 11:21:11] ORACLE-EINGANG | btn-1784: tail -10 /data/data/com.termux/files/home/jack/jack_decisions.log
[2026-07-23 11:31:13] ORACLE-EINGANG | btn-1784: free -h
[2026-07-23 11:38:43] ORACLE-EINGANG | btn-1784: sv status jack_cortex jack_telegram jack_autolearn jack_publisher jack_waechter
[2026-07-23 11:43:52] ORACLE-EINGANG | btn-1784: python3 -c "import sys,os; sys.path.insert(0,os.path.expanduser('~/jack')); impo
[2026-07-23 13:20:12] PROFIL-UPDATE | 2 neue Eintraege in kortex_profile.json
[2026-07-23 19:20:31] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json

## Budget heute
Heute: Text 45/300 | Vision 0/40 | Tokens 93831