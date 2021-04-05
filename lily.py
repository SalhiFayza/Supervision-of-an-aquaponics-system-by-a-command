import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from datetime import datetime
import time
import os
from twilio.rest import Client
import webbrowser
#import create_csv
import requests, json
from gtts import gTTS

#The primary purpose of a Recognizer instance is, of course, to recognize speech. 
#(Le but principal d'une instance de reconnaissance est, bien entendu, de reconnaître la parole.)
listener = sr.Recognizer() #initialise a recogniser
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# if you want a men voice change 1 with 0
engine.setProperty('voice', voices[1].id)
# if you want to change wake up word
WAKE = "wake up"


Hello = ["hi","hey","hello","yo","ciao","yalla","amigo"]

#function to test vocal terms exists "True"
def Lily_speak(text):
    engine.say(text)
    engine.runAndWait()

def respond(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")


# listen for audio and convert it to text:
def take_command():
    try:
        with sr.Microphone() as source: # microphone as source("microphone est affiché à la barre d'outils")
            Lily_speak('we is there , How Could i help you ')
            print('listening...')
            voice = listener.listen(source) # listen for the audio through source
            command = listener.recognize_google(voice) # convert audio to text
            command = command.lower() #The lower() method returns a string where all characters are lower case.
            if 'Lily' in command:
                command = command.replace('Lily', '')
    except:
        pass
    return command

# check thermostat
def thermostat():
    current_date_and_time = datetime.today().strftime('%Y-%m-%d')
    current_date_and_time_string = str(current_date_and_time)
    file_name = current_date_and_time_string + ".csv"
    with open(file_name, "r", encoding="utf-8", errors="ignore") as scraped:
        final_line = scraped.readlines()[-1]
        final_line = final_line.split(',')[2]
        Lily_speak('Thermostat is ' + final_line)
    return final_line

# check temperature
def temp():
    current_date_and_time = datetime.today().strftime('%Y-%m-%d')
    current_date_and_time_string = str(current_date_and_time)
    file_name = current_date_and_time_string + ".csv"
    with open(file_name, "r", encoding="utf-8", errors="ignore") as scraped:
        final_line = scraped.readlines()[-1]
        final_line = final_line.split(',')[3]
        Lily_speak('Temperature is ' + final_line)
    return final_line

# check humdity
def hmudity():
    current_date_and_time = datetime.today().strftime('%Y-%m-%d')
    current_date_and_time_string = str(current_date_and_time)
    file_name = current_date_and_time_string + ".csv"
    with open(file_name, "r", encoding="utf-8", errors="ignore") as scraped:
        final_line = scraped.readlines()[-1]
        final_line = final_line.split(',')[4]
        Lily_speak('Humidity is ' + final_line)
    return final_line






# our bot commands ,

def runchatbot():
    try:
        commandx = take_command()
        print(commandx)
        if'hello' in str(commandx):
            Lily_speak('Hy, How can I help you?')
    # 1: Name
        elif 'what is your name' in str(commandx):
            Lily_speak('My name is Lily. What is your name') 
    #if 'time' in voice_data: (date and time) ""from time import ctime""
        #print(ctime())
        elif 'my name is' in str(commandx):
            person_name = commandx.split("is")[-1].strip()
            Lily_speak('welcome ' + person_name +'in my aquaponics')
                  
    # 2: Time
        elif 'time' in str(commandx):
            time = datetime.datetime.now().strftime('%I:%M:%S %p')   
            Lily_speak("" + time)
    # 3: Date  
        elif 'date' in str(commandx):
            date = datetime.datetime.now().strftime('%y-%m-%d')   
            Lily_speak("" + date)  
    # 4: Thermostat     
        elif 'Thermostat' in str(commandx): 
            tmt= thermostat()   
            Lily_speak("the is" + tmt)
    # 5: Temperature     
        elif 'Temperature' in str(commandx): 
            tmp= temp()   
            Lily_speak("the is" + tmp)
    # 6: Humidity
        elif 'Humidity' in str(commandx): 
            hmy= hmudity()   
            Lily_speak("the is" + hmy)  
        elif 'what is the weather in' in str(commandx):
            search_term_google = commandx.split("for")[-1]
            webbrowser.get().open(f"https://www.google.com/search?q=weather&oq=weather+&aqs=chrome..69i57j69i60j69i65j69i60.4151j0j4&sourceid=chrome&ie=UTF-8")
            Lily_speak("" +search_term_google+"")


    # 11: music
        elif 'play' in str(commandx):
            song = commandx.replace('play', '')
            pywhatkit.playonyt(song)   
        else:
            Lily_speak('Please say the command again.')
            runchatbot()
    except:
        pass


## function that gona wake up the bot
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except:
            pass
    return said.lower()


start_time = time.time()
while True:
    #convert audio to text to wake up the bot
    text = get_audio()
    # if you say wake up
    if text.count(WAKE) > 0:
        # if she hear wake up a green led alight
        
        runchatbot()
    else:
        # else a red led alight
        pass
