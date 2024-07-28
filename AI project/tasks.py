import speak
import datetime
import webbrowser
import weather
import os


def work(send):
        

    your_data  = send.lower()
    
    if "what is your name" in   your_data :
        speak.text_to_speech("my name is virtual Assistant")  
        return "my name is virtual Assistant"


    elif "hello" in your_data  or "hye" in your_data  or "hay" in your_data: 
        speak.text_to_speech("Hey there, How i can  help you !")  
        return "Hey there, How i can  help you !"

    elif "how are you" in  your_data :
        speak.text_to_speech("I am doing great these days") 
        return "I am doing great these days "  

    elif "thanku" in your_data or "thankyou" in your_data:
        speak.text_to_speech("its my pleasure sir to stay with you")
        return "its my pleasure sir to stay with you"     

    elif "good morning" in your_data:
        speak.text_to_speech("Good morning dear, i think you might need some help")
        return "Good morning , i think you might need some help"   

    elif "time now" in your_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
        speak.text_to_speech(Time)
        return str(Time) 

    elif "shutdown" in your_data or "quit" in your_data:
        speak.text_to_speech("ok sure")
        return "ok sure"  


    elif "play music" in your_data or "song" in your_data:
        webbrowser.open("https://gaana.com/")   
        speak.spetext_to_speechak("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"

    elif 'open google' in your_data or 'google'  in your_data or 'open google for me'  in your_data:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.text_to_speech("google open")  
        return "google open"

    elif 'youtube' in your_data or "open youtube" in  your_data:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.text_to_speech("YouTube open") 
        return "YouTube open"    
    
    
    elif 'weather' in your_data or 'may i know the weather today'  in your_data or 'give me todays weather'  or 'todays weather' in your_data :
       ans   = weather.weather()
       speak.text_to_speech(ans) 
       return ans
    
    elif 'music from my laptop' in your_data:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.text_to_speech("songs playing...")
        return "songs playing..." 

    else :
        speak.text_to_speech( "i'm unable to understand!")
        return "i'm unable to understand!"       