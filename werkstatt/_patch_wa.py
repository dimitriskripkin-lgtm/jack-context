p="jack_autonomous.py"
s=open(p).read()
if "_maybe_audit" in s:
    print("audit-hook schon drin")
else:
    func='''def _maybe_audit():
    try:
        import jack_audit, time as _t
        lf = os.path.expanduser("~/jack/.last_audit")
        try: last = float(open(lf).read().strip())
        except Exception: last = 0.0
        if _t.time() - last >= 604800:
            notify("Woechentlicher Audit:" + chr(10) + jack_audit.report())
            open(lf,"w").write(str(_t.time()))
            import jack_log; jack_log.log_decision("WAECHTER-AUDIT","woechentlich verschickt")
    except Exception as e:
        try:
            import jack_log; jack_log.log_decision("WAECHTER-AUDIT-FEHLER", str(e)[:100])
        except Exception: pass

'''
    a1="def main():\n"
    s2=s.replace(a1, func+a1, 1)
    a2="time.sleep(HEARTBEAT)"
    s3=s2.replace(a2, "_maybe_audit()\n        "+a2, 1)
    if s3!=s and "_maybe_audit()" in s3 and s3.count(a2)>=1:
        open(p,"w").write(s3); print("Waechter gepatcht: _maybe_audit + Loop-Aufruf")
    else:
        print("ANKER-PROBLEM - Waechter unveraendert")
