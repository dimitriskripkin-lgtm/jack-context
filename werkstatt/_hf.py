import os, subprocess, sys
sys.path.insert(0, os.path.expanduser("~/jack"))
HOME = os.path.expanduser("~")
WHISPER = HOME + "/whisper.cpp/build/bin/whisper-cli"
MODEL = HOME + "/whisper.cpp/models/ggml-base.bin"
REC, WAV, RESP = HOME+"/.jack_hf.m4a", HOME+"/.jack_hf.wav", HOME+"/.jack_hf_resp.mp3"
def sec(k):
    for l in open(os.path.expanduser("~/.jack_secrets")):
        if k in l and "=" in l: return l.split("=",1)[1].strip().strip('"').strip("'")
if not os.path.exists(REC) or os.path.getsize(REC) < 1000:
    print("KEINE Aufnahme da - Mikro-Permission fuer Termux:API erteilt?"); sys.exit()
subprocess.run(["ffmpeg","-y","-i",REC,"-ar","16000","-ac","1",WAV], check=True, capture_output=True)
res = subprocess.run([WHISPER,"-m",MODEL,"-f",WAV,"-l","de","-nt","-t","6"], capture_output=True, text=True)
heard = " ".join(res.stdout.split()).strip()
print("GEHOERT:", repr(heard))
if not heard:
    print("Nichts verstanden - Abbruch"); sys.exit()
from jack_talk import talk_to_gemini
answer = talk_to_gemini(heard)
print("JACK SAGT:", answer)
from elevenlabs.client import ElevenLabs
c = ElevenLabs(api_key=sec("ELEVENLABS_API_KEY"))
audio = c.text_to_speech.convert(text=answer, voice_id=sec("ELEVENLABS_VOICE_ID"), model_id="eleven_flash_v2_5")
with open(RESP,"wb") as f:
    for chunk in audio: f.write(chunk)
print("Antwort-Audio:", os.path.getsize(RESP), "bytes")
