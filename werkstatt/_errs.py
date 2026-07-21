import sqlite3, os
con = sqlite3.connect(os.path.expanduser("~/jack/jack_errors.db"))
for r in con.execute("SELECT timestamp,module,error_type,error_msg FROM errors WHERE resolved=0 ORDER BY id DESC").fetchall():
    print("-", r[0], "|", r[1], "|", r[2], "|", str(r[3])[:140])
con.close()
