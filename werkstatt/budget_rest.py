#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.expanduser("~/jack"))
import jack_budget
print(jack_budget.status())
