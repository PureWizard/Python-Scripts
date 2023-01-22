# just write your message after running out it will automatically convert your text to speech
from gtts import gTTS
import os
import subprocess

def speak():
    sentence = input("Enter the text you want to be spoken: ")
    tts = gTTS(sentence)
    tts.save("output.mp3")
    subprocess.Popen(['start', 'output.mp3'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

speak()
