import os
import soundfile as sf
from tango import Tango


tango = Tango("declare-lab/tango")

prompt = "car explosion"
audio = tango.generate(prompt, steps=200)
audio_file_path = os.path.join('audio', "output.wav")
sf.write(audio_file_path, audio, samplerate=16000)