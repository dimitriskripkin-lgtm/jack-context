#!/usr/bin/env python3
import subprocess
def sh(c):
    try: return subprocess.run(c,shell=True,capture_output=True,text=True,timeout=8).stdout.strip()
    except Exception as e: return f"(fehler: {e})"
print("=== JACK STATUS ===")
print(sh("sv status jack_cortex jack_telegram jack_autolearn jack_publisher jack_waechter ollama"))
print("--- RAM ---")
print(sh("free -h | head -2"))
