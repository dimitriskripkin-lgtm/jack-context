import jack_skills as s
skills=[("ram_check","RAM frei/belegt"),("disk_check","Speicherplatz"),("fehler_report","Offene Fehler aus DB"),("git_status","Git-Stand beider Repos"),("gedaechtnis_stats","Gedaechtnis-Zahlen"),("modell_check","Ollama-Modelle"),("budget_rest","API-Budget heute")]
for n,d in skills:
    ok,m=s.save_skill(n,n+".py",d); print("SAVE",n,"->",ok)
print("=== BIBLIOTHEK ==="); print(s.list_skills())
for n,_ in skills:
    ok,out=s.run_skill(n); print("--- RUN",n,"(ok=%s) ---"%ok); print((out or "")[:400])
