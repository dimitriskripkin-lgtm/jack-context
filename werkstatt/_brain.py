import sys, os
sys.path.insert(0, os.path.expanduser("~/jack"))
try:
    from jack_talk import talk_to_gemini
    r = talk_to_gemini("Sag kurz hallo")
    print("Gehirn OK, Antwort:", str(r)[:100])
except Exception:
    import traceback; print("GEHIRN FEHLER:"); traceback.print_exc()
