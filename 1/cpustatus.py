import psutil
import speak
import spech_to_text

def cpu():
    usage=str(psutil.cpu_percent())
    speak.speak("CPU is at"+usage)
    battery=str(psutil.sensors_battery())
    speak.speak("CPU is at"+battery)