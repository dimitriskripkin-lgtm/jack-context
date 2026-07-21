import sys, os, sqlite3, inspect
sys.path.insert(0, os.path.expanduser("~/jack"))
db = os.path.expanduser("~/jack/jack_memory.db")
c = sqlite3.connect(db)
cols = [r[1] for r in c.execute("PRAGMA table_info(memory)").fetchall()]
c.close()
print("memory-Spalten (live):", cols)
import jack_memory
print("save-Signatur:", inspect.signature(jack_memory.save))
try:
    jack_memory.save("TESTNOTIZ merk dir bitte", "Dima testet das Gedaechtnis", "notiz")
    print("save() OK - Schreibung durchgelaufen")
    print("query zurueck:", jack_memory.query("TESTNOTIZ"))
except Exception:
    import traceback; print("SAVE-FEHLER:"); traceback.print_exc()
