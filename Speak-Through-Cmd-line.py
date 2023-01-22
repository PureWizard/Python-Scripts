# just write your message after running out it will automatically convert your text to speech
import pyttsx3

def speak():
    engine = pyttsx3.init()
    engine.setProperty('rate', -2)

    sentence = input("Enter the text you want to be spoken: ")
    engine.say(sentence)
    engine.runAndWait()
