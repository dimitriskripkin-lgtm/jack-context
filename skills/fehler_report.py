#!/usr/bin/env python3
import sqlite3, os
db=os.path.expanduser("~/jack/jack_errors.db")
con=sqlite3.connect(db); cur=con.cursor()
rows=cur.execute("SELECT timestamp,module,error_type,error_msg FROM errors WHERE resolved=0 ORDER BY id DESC LIMIT 10").fetchall()
print("Offene Fehler:", len(rows))
for r in rows: print("-", r[0], r[1], r[2], str(r[3])[:60])
con.close()
