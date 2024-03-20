import remember
import speak



def Knowing():
    remember=open("C:\\Users\\gotec\\Desktop\\6 th sem\\mini project\\1\\data.txt",'r')
    speak.speak("you said me to remember that"+remember.read())