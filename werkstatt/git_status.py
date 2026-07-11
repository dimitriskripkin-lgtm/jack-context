#!/usr/bin/env python3
import subprocess, os
for name, p in [("core","~/jack"), ("context","~/jack-context")]:
    path=os.path.expanduser(p)
    print("===", name, "===")
    out=subprocess.run(["git","-C",path,"status","-s"],capture_output=True,text=True).stdout.strip()
    print(out if out else "(sauber)")
