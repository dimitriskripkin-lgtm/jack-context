p="jack_telegram.py"
s=open(p).read()
if "/audit" in s:
    print("audit schon drin")
else:
    anchor="def handle(text):\n"
    add='    if text.strip() == "/audit":\n        import jack_audit; return jack_audit.report()\n'
    new=s.replace(anchor, anchor+add, 1)
    if new!=s:
        open(p,"w").write(new); print("TG gepatcht: /audit eingefuegt")
    else:
        print("ANKER NICHT GEFUNDEN - TG unveraendert")
