import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import tempfile
import scipy.io.wavfile as wav
import os

print("Loading Whisper medium model (one-time)...")
MODEL = WhisperModel("medium", device="cpu", compute_type="int8")
print("Whisper model loaded.")

def listen_and_transcribe(sample_rate=16000):
    print("\nPress ENTER to start speaking...")
    input()

    print("🎤 Recording... Press ENTER again to stop.")
    audio_chunks = []

    def callback(indata, frames, time, status):
        audio_chunks.append(indata.copy())

    with sd.InputStream(
        samplerate=sample_rate,
        channels=1,
        callback=callback,
        dtype="float32"
    ):
        input()

    # -------- SAFETY CHECK --------
    if len(audio_chunks) == 0:
        print("No audio captured.")
        return ""
    # ------------------------------

    audio = np.concatenate(audio_chunks, axis=0)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        wav.write(tmp.name, sample_rate, audio)
        audio_path = tmp.name

    segments, _ = MODEL.transcribe(audio_path, language="en")
    text = " ".join(segment.text for segment in segments).strip()

    os.remove(audio_path)

    print("Transcribed Text:", text)
    return text

