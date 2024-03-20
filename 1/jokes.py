import spech_to_text
import speak
import pyjokes

def jokes():
    
    joke = pyjokes.get_joke()
    speak.speak(joke)
