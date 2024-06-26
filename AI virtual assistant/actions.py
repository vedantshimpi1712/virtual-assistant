import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Actions(data):
    user_data=data.lower()

    if"what's your name"in user_data:
        text_to_speech.text_to_speech("My name is AI assistant")
        return("My name is AI assistant")
        
        
    elif"hello"in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("hey,how can i help you")
        return("hey,how can i help you")
    
    
    elif"good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir")
        return("good morning sir!")
        
    elif"time now"in user_data:
        current_time=datetime.datetime.now()
        Time=(str)(current_time)+"Hour:",(str)(current_time.minute)+"Minute"
        text_to_speech.text_to_speech(Time)
        return Time
    
    
    elif"shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return ("ok sir")
    
    
    elif"play music"in user_data:
        webbrowser.open("https://spotify.com/")
        text_to_speech.text_to_speech("spotify.com is ready for you")
        return("spotify.com is ready for you")
    
        
    elif"youtube"in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is ready for you")
        return("youtube.com is ready for you")
    
        
    elif"open chrome"in user_data:
        webbrowser.open("https://chrome.com/")
        text_to_speech.text_to_speech("chrome.com is ready for you")
        return("chrome.com is ready for you")
    
        
    elif"weather"in user_data:
        ans=weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans
        
        
    else:
        text_to_speech.text_to_speech("Sorry sir,I am unable to understand")
        
