import speech_recognition as sr
from requests_html import HTMLSession
import speak

def listen():
    r = sr.Recognizer()

# Use microphone as source
    with sr.Microphone() as source:
      audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
        return text
    except sr.UnknownValueError:
        speak.text_to_speech("sorry")   
    except sr.RequestError:
        speak.text_to_speech('No internet connect please turn on you internet')
 
