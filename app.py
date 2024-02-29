import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import soundfile as sf
from tango import Tango


app = FastAPI()

tango = Tango("declare-lab/tango")

AUDIO_DIRECTORY = 'audio'


@app.get('/generate')
def make_audio(prompt: str):
    if prompt != '':
        audio = tango.generate(prompt, steps=200)
        audio_file_path = os.path.join(AUDIO_DIRECTORY, "output.wav")
        sf.write(audio_file_path, audio, samplerate=16000)
        return prompt
    return "Audio generated"


@app.get('/audio/{filename}')
async def get_audio(filename: str):
    return FileResponse(f"{AUDIO_DIRECTORY}/{filename}")


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='localhost')