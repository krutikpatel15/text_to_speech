'''
from gtts import gTTS
import os

# text = "welcome krutik to vs code"
text = input()

# convert text to speech(initialize)
text_to_speech = gTTS(text=text, lang='en')

# save the audio file
text_to_speech.save('test.mp3')

# play the audio
os.system('test.mp3') '''


## OFFLINE - pyttsx
import pyttsx3
text = "welcome krutik to vs code"
text_to_speech = pyttsx3.init()

# adjust the speed
text_to_speech.setProperty('rate', 100)

# change the voice
voices = text_to_speech.getProperty('voices')
text_to_speech.setProperty('voice', voices[0].id) # 0 for male voice and 1 for female voice

text_to_speech.say(text)
text_to_speech.runAndWait()
