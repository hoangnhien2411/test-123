import streamlit as st
import os
from audiorecorder import audiorecorder
from client_sample_2 import  with_azure_openai
import asyncio

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Click to stop recording")
OUTPUT_FILE = "output2"
if not os.path.exists(OUTPUT_FILE):
    os.makedirs(OUTPUT_FILE)

IN_FILE = "input"
if not os.path.exists(IN_FILE):
    os.makedirs(IN_FILE)

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.export().read())  

    # To save audio to a file, use pydub export method:
    audio.export("input/audio.wav", format="wav")

    # To get audio properties, use pydub AudioSegment properties:
    st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")
    asyncio.run(with_azure_openai('input/audio.wav', OUTPUT_FILE))
    