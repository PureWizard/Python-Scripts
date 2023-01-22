# just write your message after running out it will automatically convert your text to speech
from gtts import gTTS
import os

def speak():
    sentence = input("Enter the text you want to be spoken: ")
    tts = gTTS(sentence)
    tts.save("output.mp3")
    os.system("start output.mp3")

speak()
