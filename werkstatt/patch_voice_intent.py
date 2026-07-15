import os
path = os.path.expanduser("~/jack/jack_voice_processor.py")
content = open(path).read()

old = '''    # Gemini antworten lassen
    if text.lower().strip().startswith("claude"):
        import jack_claude
        response_text = jack_claude.ask_claude(text)
    else:
        from jack_talk import talk_to_gemini
        response_text = talk_to_gemini(text)'''

new = '''    # Intent-Routing: direkte Befehle ohne Gemini-Umweg
    tlow = text.lower()
    sys.path.insert(0, os.path.expanduser("~/jack"))
    from kortex_memory import add_memory, search_memory

    if "merke" in tlow:
        idx = tlow.find("merke")
        inhalt = text[idx+5:].strip(" ,.:-")
        if inhalt:
            r = add_memory(inhalt, category="voice", source="voice", tags="")
            response_text = f"Gemerkt: {inhalt[:100]}"
        else:
            response_text = "Ich habe nichts zum Merken verstanden."
    elif "such" in tlow:
        idx = tlow.find("such")
        q = text[idx+4:].strip(" ,.:-")
        q = q[1:].strip() if q[:1] == "e" else q
        results = search_memory(q, limit=3) if q else None
        if not results or isinstance(results, dict):
            response_text = f"Nichts gefunden fuer {q}." if q else "Wonach soll ich suchen?"
        else:
            teile = [r["content"][:80] for r in results]
            response_text = "Gefunden: " + " | ".join(teile)
    elif tlow.strip().startswith("claude"):
        import jack_claude
        response_text = jack_claude.ask_claude(text)
    else:
        from jack_talk import talk_to_gemini
        response_text = talk_to_gemini(text)'''

if old not in content:
    print("FEHLER: alter Block nicht 1:1 gefunden - keine Aenderung gemacht")
else:
    content = content.replace(old, new, 1)
    open(path, "w").write(content)
    print("OK: Intent-Routing eingebaut")
