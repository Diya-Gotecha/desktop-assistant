import spech_to_text
import speak
import pyautogui

def Screenshot():
    img = pyautogui.screenshot()
    speak.speak("By what name should I save it?")
    ans=spech_to_text.spech_to_text()
    ans="C:\\Users\\gotec\\Desktop\\6 th sem\\mini project\\store_screenshot"+ans+".png"
    img.save(ans)
    speak.speak("Screenshot taken")