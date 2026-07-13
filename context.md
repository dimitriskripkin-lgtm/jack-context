# JACK LIVE-KONTEXT (auto, 2026-07-13T08:28:52.095575)

# JACK PROJEKT-KONTEXT (auto-generiert)
Stand: 2026-07-13T08:28:52.086767

## Owner / Kern
- Owner: Dimitri
- Hardware: Honor Magic8 Pro (Host/Gehirn) + Xiaomi 11T Pro (Slave via SSH)
- Vision: Lokales autonomes AI-OS, offline-first, JACK als Exit-Vehicle fuer mehr Unabhaengigkeit
- WICHTIG: Dima ist der MENSCH/Nutzer. JACK ist das SYSTEM/die KI. Niemals verwechseln.

## Was JACK ueber Dima gelernt hat
- Dima ist Dimitri.
- Dima ist LKW-Fahrer mit Sprinter Kühlkoffer bei Dalhoff Feinkost in Achim (Nachtschicht).
- Dima ist Hobby-Programmierer.
- Dima nutzt Gemini Plus und Claude.ai.
- JACK ist ein autonomes, lokales AI-OS.
- JACK läuft auf einem Honor Magic8 Pro mit Termux.
- JACK nutzt Gemini 2.5 Flash (Lite) als Hauptdenker.
- JACK soll sich selbst lernen und verbessern.
- JACK steht unter Dimas voller Kontrolle.
- JACK wurde am 18. Juni gebaut.
- JACK verwendet `jack_learn.py` als Lerner.
- JACK nutzt ein Xiaomi 11T Pro als Slave-Gerät via SSH.
- JACK's kostenlose KI-Modelle haben Tageslimits.
- JACK's Chef-KI 'Claude Code' ist ein read-only Berater.
- JACK hat Fähigkeiten wie Text- und Sprachchat, sicheres Code schreiben, autonomes Handeln und Selbstverbesserung.
- JACK nutzt `jack_waechter` für regelbasierte Überwachung und Neustarts.
- JACK's Konfiguration und Logs werden in einem öffentlichen Repo (`jack-context`) geteilt.
- Dima hat KEINEN Hund.
- JACK hat KEINEN direkten Shell- oder Dateizugriff über den Chat.
- Dima ist LKW-Fahrer mit Sprinter Kuehlkoffer, KEIN Fernfahrer.

## Aktive Module (44)
- jack_agent.py
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
- jack_cortex.py
- jack_gemini_bridge.py
- jack_handshake_gen.py
- jack_improve.py
- jack_learn.py
- jack_log.py
- jack_math.py
- jack_memory.py
- jack_memory_engine.py
- jack_operator.py
- jack_patch.py
- jack_personality.py
- jack_publish.py
- jack_self_improve.py
- jack_sensors.py
- jack_skills.py
- jack_snapshot.py
- jack_talk.py
- jack_telegram.py
- jack_v2.py
- jack_vecdb.py
- jack_voice.py
- jack_voice_el.py
- jack_voice_processor.py
- jack_write.py
- jack_xiaomi.py
- kortex_controller.py
- kortex_memory.py
- kortex_profile_updater.py
- kortex_profiler.py
- kortex_sensor_daemon.py
- quick_bridge.py
- test_jack_approval.py

## System-Status
- Offene Fehler: 0
- Erinnerungen: 104
- Dienste:
run: jack_cortex: (pid 20695) 199133s
run: jack_telegram: (pid 30633) 5734s
run: jack_autolearn: (pid 20689) 199133s
run: ollama: (pid 20694) 199133s

## Letzte Aenderungen
317e403 chore: jack_fixes.json nach Test-Fix geleert
a97e7d4 feat: Schwellenwert n>=5, Ruhezeit 16-22, Briefing-Cron 07:55, AGENTS.md
a27ee9d chore: .last_self_improve zu gitignore
1f0eaed feat: Waechter ruft jack_self_improve taeglich auf
ca5742c feat: JACK erste autonome Selbstverbesserung - SSH-Timeout 15->25s per approve_fix
7db5485 feat: jack_self_improve.py - Selbstdiagnose + /approve_fix_ Handler live
a3573b4 feat: jack_self.json - JACKs Selbstbild und Identitaet
6f51505 feat: jack_status_report.sh - Session-Start auf einen Befehl
7cd021f feat: access_count bei Suche + /status_report Telegram-Befehl
5d8602d feat: kortex_profile_updater.py - Profil wird automatisch nach jedem jack_learn aktualisiert
85a0b3a feat: jack_learn schreibt neue Fakten automatisch in kortex_memory.db
6d29dd5 chore: .last_audit aus Git-Tracking entfernt
47e65e6 chore: Silent-Fail Review abgeschlossen - verbleibende except:pass sind bewusste Fallbacks
1528de5 fix: letzte Silent Fails geloggt, alle except:pass im Repo eliminiert
8d5848b fix: restliche 4 Silent Fails geloggt (jack_publish/bug_fixer/sensors/gemini)

## Architektur
Host Honor Magic8 Pro (Termux), Slave Xiaomi 11T (SSH 10.234.166.131:8022).
Gehirn: Gemini 2.5 Flash + llama3.2:3b Fallback + nomic-embed-text.
Gedaechtnis 3-Tier (MemGPT-Muster): Core=identity.json, Recall=Verlauf, Archival=sqlite-vec.
Selbstlernen: jack_learn.py alle 2h. Interfaces: Telegram + Voice.


## Letzte 20 Aktionen (Logbuch)

[2026-07-11 16:15:21] SKILL-AUSGEFUEHRT | gedaechtnis_stats
[2026-07-11 16:15:21] SKILL-AUSGEFUEHRT | modell_check
[2026-07-11 16:15:21] SKILL-AUSGEFUEHRT | budget_rest
[2026-07-11 19:28:02] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-11 19:28:11] WAECHTER-AUDIT | woechentlich verschickt
[2026-07-13 03:53:18] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-13 03:58:33] WAECHTER-AUDIT | woechentlich verschickt
[2026-07-13 04:54:43] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-13 06:51:45] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-07-13 06:52:25] SELF-IMPROVE | jack_cortex 1x, fix=fix_cortex_ssh_timeout_20260713_065225
[2026-07-13 07:00:56] APPROVE-FIX | approve_fix_cortex_ssh_timeout_20260713_065225: Backup: /data/data/com.termux/files/home/jack/jack_cortex.py.bak_autofix
FEHLER:
[2026-07-13 07:02:16] PROFIL-UPDATE | 1 neue Eintraege in kortex_profile.json
[2026-07-13 07:11:08] SELF-IMPROVE | jack_cortex 1x, fix=fix_cortex_ssh_timeout_20260713_071108
[2026-07-13 07:12:00] APPROVE-FIX | approve_fix_cortex_ssh_timeout_20260713_071108: Backup: /data/data/com.termux/files/home/jack/jack_cortex.py.bak_autofix
OK: Fix
[2026-07-13 07:15:44] WAECHTER-START | Nacht-Ueberwachung laeuft
[2026-07-13 07:15:50] SELF-IMPROVE | Analyse abgeschlossen, keine Muster gefunden.
[2026-07-13 07:15:50] SELF-IMPROVE | Tagescheck abgeschlossen
[2026-07-13 08:19:11] WAECHTER-START | Nacht-Ueberwachung laeuft

## Budget heute
Heute: Text 16/300 | Vision 0/40 | Tokens 27005