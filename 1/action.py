import datetime
import speak
import webbrowser
import weather
import os
import time
import remember
import screenshot
import jokes
import knowing
import username
import wikipedia
import subprocess
import pyautogui
import cpustatus



def Action(send) :   
  
    data_btn  = send.lower()

    
    if "what is your name" in   data_btn :
      speak.speak("my name is Robu")  
      return "my name is Robu"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
          ans=username.username()
          speak.speak(ans)
          return(ans)

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days ma'am") 
            return "I am doing great these days ma'am"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn or "whats time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 
    
    elif "open notepad" in data_btn:
          npath="C:\\Windows\\System32\\notepad.exe"  
          os.startfile(npath)        

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://open.spotify.com/")   
        speak.speak("spotify.com is now ready for you, enjoy your music")                   
        return "spotify.com is now ready for you, enjoy your music"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"  

    elif 'tell me joke' in data_btn or 'make me happy' in data_btn:
         ans = jokes.jokes()
         speak.speak(ans)
         return ans
    
    elif 'whats the weather robu' in data_btn or "weather" in data_btn:
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans
    
    elif 'set a reminder' in data_btn :
       ans   = remember.Remember()
       speak.speak(ans) 
       return ans
    
    elif 'what the reminder' in data_btn :
       ans = knowing.Knowing()
       speak.speak(ans)
       return ans
    

    elif 'screenshot' in data_btn :
       ans   = screenshot.Screenshot()
       speak.speak(ans) 
       return ans
    
    elif 'cpustatus' in data_btn:
        ans  = cpustatus.cpu()
        speak.speak(ans)
        return(ans)
       
    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 
    
    elif 'wikipedia' in data_btn:
          speak.speak('searching...')
          data_btn=data_btn.replace("wikipedia"," ")
          ans=wikipedia.summary(data_btn,sentences=2)
          speak.speak("according to wikipedia")
          speak.speak(ans)
    
    elif 'google' in data_btn or "open google" in  data_btn:
         url = 'https://google.com/'
         webbrowser.get().open(url)
         speak.speak("google open") 
         return "google open" 
    
    elif 'flipkart' in data_btn or "open flipkart" in  data_btn:
        url = 'https://www.flipkart.com/'
        webbrowser.get().open(url)
        speak.speak("flipkart open") 
        return "flipkart open" 
    
    elif 'amazon' in data_btn or "open amazon" in  data_btn:
        url = 'https://www.amazon.in/'
        webbrowser.get().open(url)
        speak.speak("amazon open,enjoy shopping") 
        return "amazon open,,enjoy shopping" 
    
    elif 'coursera' in data_btn or "open coursera " in  data_btn:
        url = 'https://www.coursera.org/'
        webbrowser.get().open(url)
        speak.speak("coursera open,learn new skills") 
        return "courser open,learn new skills" 
    
    elif 'linkedin' in data_btn or "linkedin" in  data_btn:
        url = 'https://in.linkedin.com/'
        webbrowser.get().open(url)
        speak.speak("linkedin open,find your job!") 
        return "linkedin open,find your job!" 
    
    elif 'instagram' in data_btn or "open instagram" in  data_btn:
        url = 'https://www.instagram.com/'
        webbrowser.get().open(url)
        speak.speak("instagram open enjoy to seeing reels") 
        return "instagram open enjoy to seeing reels" 
    
    elif 'where is' in data_btn:
         data_btn=data_btn.replace("where is"," ")
         location=data_btn
         speak.speak("locating....")
         speak.speak(location)
         webbrowser.open("https://www.google.co.in/maps/place/"+location+"")  
   
    elif 'shutdown' in data_btn:
         speak.speak('hold on a second maam! your system is on its way to shutdown')
         speak.speak('make sure all your application are closed')
         time.sleep(5)
         subprocess.call(['shutdown','/s'])
 
    elif 'restart' in data_btn:
         subprocess.call(['shutdown','/r'])

    elif 'switch window' in data_btn:
         pyautogui.keyDown('alt')
         pyautogui.press('tab')
         time.sleep(1)
         pyautogui.keyUp('alt')

    else :
        speak.speak( "i'm unable to understand!")
        return "i'm unable to understand!"       

