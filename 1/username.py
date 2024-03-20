import spech_to_text
import speak

def username():
    speak.speak("waht should i call you ma'am?")
    username=spech_to_text.spech_to_text()
    fname=(str)(username)
    speak.speak("welcome miss" + fname)
    speak.speak("how can  i help you , ma'am?")

    