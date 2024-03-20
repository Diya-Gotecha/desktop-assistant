import spech_to_text
import speak

def Remember():
    speak.speak("What should I remember?")
    Information=spech_to_text.spech_to_text()
    speak.speak('you said me to remember that '+Information)
    rem = open("C:\\Users\\gotec\\Desktop\\6 th sem\\mini project\\1\\data.txt",'w') 
    rem.write(Information) 
    rem.close() 

def Knowing():
    remember=open("C:\\Users\\gotec\\Desktop\\6 th sem\\mini project\\1\\data.txt",'r')
    speak.speak("you said me to remember that"+remember.read())