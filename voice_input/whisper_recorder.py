import whisper
import os
from pydub import AudioSegment
import sounddevice as sd
import soundfile as sf

model = whisper.load_model("base")

def record_and_transcribe(filename="voice.wav", duration=5):
    fs = 44100
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    sf.write(filename, recording, fs)
    print("Transcribing...")
    result = model.transcribe(filename)
    return result['text']
