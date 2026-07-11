#!/usr/bin/env python3
import subprocess
print("=== JACK STATUS ===")
print(subprocess.run("sv status jack_cortex jack_telegram jack_autolearn jack_publisher jack_waechter ollama",shell=True,capture_output=True,text=True,timeout=8).stdout.strip())
print("--- RAM ---")
print(subprocess.run("free -h",shell=True,capture_output=True,text=True,timeout=8).stdout.strip())
