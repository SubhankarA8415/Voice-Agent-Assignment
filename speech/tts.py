from gtts import gTTS
import os
import tempfile
import platform

# gTTS does NOT support Odia, so we use Hindi as fallback
TTS_LANGUAGE = "hi"   # Hindi

def speak_text(text):
    tts = gTTS(text=text, lang=TTS_LANGUAGE)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts.save(tmp.name)
        audio_path = tmp.name

    if platform.system() == "Windows":
        os.system(f'start {audio_path}')
    elif platform.system() == "Darwin":
        os.system(f'afplay {audio_path}')
    else:
        os.system(f'mpg123 {audio_path}')
