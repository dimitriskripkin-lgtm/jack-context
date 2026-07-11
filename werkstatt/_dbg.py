import sys, os
sys.path.insert(0, os.path.expanduser("~/jack"))
import jack_autonomous as w
import json, urllib.request
tok = w._sec("TELEGRAM_BOT_TOKEN")
cid = w._sec("TELEGRAM_CHAT_ID")
print("Token da:", bool(tok), "| ChatID da:", bool(cid))
if tok and cid:
    try:
        d = json.dumps({"chat_id": cid, "text": "[JACK Waechter] Debug-Sendetest"}).encode()
        req = urllib.request.Request("https://api.telegram.org/bot"+tok+"/sendMessage", data=d, headers={"Content-Type":"application/json"})
        resp = urllib.request.urlopen(req, timeout=10)
        print("Telegram HTTP:", resp.status, "-> Testnachricht muesste ankommen")
    except Exception as e:
        print("SENDE-FEHLER:", repr(e))
else:
    print(">> Secrets fehlen im Waechter-Kontext -> notify() returnt still. Wurzel gefunden.")
