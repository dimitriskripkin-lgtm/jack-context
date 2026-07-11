#!/usr/bin/env python3
import subprocess
print(subprocess.run("ollama list",shell=True,capture_output=True,text=True,timeout=15).stdout.strip())
