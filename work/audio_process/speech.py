import speech_recognition
import sys
import subprocess as sp
import time
import os

voice = "voice.wav"

print("please input voice")
os.system('arecord -D plughw:1,0 -d 3 voice.wav')
print("voice set")

r = speech_recognition.Recognizer()
with speech_recognition.AudioFile(voice) as source:
    audio = r.record(source)
a = r.recognize_google(audio, language="ja-JP")
print(a)
