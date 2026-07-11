#!/usr/bin/env python3
import json, os
d=json.load(open(os.path.expanduser("~/jack/jack_identity.json")))
print("Gelernte Fakten:", len(d.get("learned_facts",[])))
print("Korrekturen:", len(d.get("korrekturen",[])))
print("Zuletzt gelernt:", d.get("last_learned","?"))
