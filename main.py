import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime


r=sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
           assistant_speak(ask)
        audio=r.listen(source)
        voicedata=''
        try:
            voicedata=r.recognize_google(audio)
        except sr.UnknownValueError:
           assistant_speak('sorry i did not get that')
        except sr.RequestError:
           assistant_speak("sorry my voive is down") 
        return voicedata

def assistant_speak(audio_string):
    tts=gTTS(text=audio_string, lang='en')     
    r=random.randint(1,1000000)   
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voicedata):
    #name
    if 'what is your name' in voicedata:
       assistant_speak("My name is your assistant")
    #time
    if 'what time is it'  in voicedata:
       assistant_speak(ctime())  
    #google search
    if 'search ' in voicedata:
        search=record_audio('what do you want to search for')  
        url='https://www.google.com/search?q='+ search
        webbrowser.get().open(url)
        assistant_speak('here i found for' + search)  
    #youtube
    if 'youtube videos ' in voicedata:
        youvideos=record_audio('Name of video')  
        url='https://www.youtube.com/results?search_query={youvideos}'
        webbrowser.get().open(url)
        assistant_speak('Here is the video '+youvideos)  
    #exit    
    if 'exit' in voicedata:
        exit()


time.sleep(1)
assistant_speak("How can i help you")  
while 1:          
    voicedata=record_audio()
    respond(voicedata)