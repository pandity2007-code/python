import pyttsx3
engine=pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.say("my name is yash")
engine.runAndWait()

engine.setProperty('voice',voices[1].id)
engine.say("my name is yash")
engine.runAndWait()