#!/usr/bin/env python3
import subprocess
print(subprocess.run("df -h",shell=True,capture_output=True,text=True,timeout=8).stdout.strip())
