import pyttsx3
def text_to_speech(text):

    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-60)
    engine.say(text)
    engine.runAndWait()

