import os, hashlib
p = os.path.expanduser("~/.jack_secrets")
lines = [l for l in open(p) if "TELEGRAM_BOT_TOKEN" in l and "=" in l]
def v_wa(l): return l.split("=",1)[1].strip().strip('"').strip("'")
def v_tg(l): return l.split('"')[1] if '"' in l else ""
def fp(x): return hashlib.sha256(x.encode()).hexdigest()[:8] if x else "LEER"
print("Anzahl Token-Zeilen:", len(lines))
if lines:
    print("Waechter liest (erste):  fp", fp(v_wa(lines[0])))
    print("Bot liest (letzte):      fp", fp(v_tg(lines[-1])))
    print("GLEICH:", v_wa(lines[0]) == v_tg(lines[-1]) and v_wa(lines[0]) != "")
