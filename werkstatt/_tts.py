import os
def sec(k):
    for l in open(os.path.expanduser("~/.jack_secrets")):
        if k in l and "=" in l: return l.split("=",1)[1].strip().strip('"').strip("'")
try:
    from elevenlabs.client import ElevenLabs
    c = ElevenLabs(api_key=sec("ELEVENLABS_API_KEY"))
    audio = c.text_to_speech.convert(text="Test", voice_id=sec("ELEVENLABS_VOICE_ID"), model_id="eleven_flash_v2_5")
    n = sum(len(chunk) for chunk in audio)
    print("ElevenLabs OK, Audio-Bytes:", n)
except Exception:
    import traceback; print("ELEVENLABS FEHLER:"); traceback.print_exc()
