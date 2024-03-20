import pyttsx3
engine = pyttsx3.init()#use to ininitialize the Text-to-Speech (TTS) engine
    
def speak(text):
    engine = pyttsx3.init()#use to ininitialize the Text-to-Speech (TTS) engine
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.say(text)
    engine.runAndWait()

