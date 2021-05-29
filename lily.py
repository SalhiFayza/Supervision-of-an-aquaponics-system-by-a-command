import speech_recognition as sr # recognise speech
import random
import webbrowser # open browser
from  datetime import date 
import pyttsx3
import pywhatkit
import time

import datetime
#Create a class named person (Une classe est comme un constructeur d'objet, ou un "plan" pour créer des objets.)
class person: 
    name = ''  #Create variable
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    def setName(self, name): #use the setName() function to assign value for name 
        self.name = name

#function to test vocal terms exists "True"
def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

#The primary purpose of a Recognizer instance is, of course, to recognize speech. 
#(Le but principal d'une instance de reconnaissance est, bien entendu, de reconnaître la parole.)
listener = sr.Recognizer() # initialise a recogniser            
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# if you want a men voice change 1 with 0
engine.setProperty('voice', voices[1].id)
def lily_speak(text):
    engine.say(text)
    engine.runAndWait()

# check thermostat
def thermostat():
    current_date_and_time = datetime.today().strftime('%Y-%m-%d')
    current_date_and_time_string = str(current_date_and_time)
    file_name = current_date_and_time_string + ".csv"
    with open(file_name, "r", encoding="utf-8", errors="ignore") as scraped:
        final_line = scraped.readlines()[-1]
        final_line = final_line.split(',')[2]
        lily_speak('Thermosta is ' + final_line)
    return final_line

# check tem
def temp():
    current_date_and_time = datetime.today().strftime('%Y-%m-%d')
    current_date_and_time_string = str(current_date_and_time)
    file_name = current_date_and_time_string + ".csv"
    with open(file_name, "r", encoding="utf-8", errors="ignore") as scraped:
        final_line = scraped.readlines()[-1]
        final_line = final_line.split(',')[3]
        lily_speak('The Temperature is ' + final_line)
    return final_line

# check humdity
def hmudity():
    current_date_and_time = datetime.today().strftime('%Y-%m-%d')
    current_date_and_time_string = str(current_date_and_time)
    file_name = current_date_and_time_string + ".csv"
    with open(file_name, "r", encoding="utf-8", errors="ignore") as scraped:
        final_line = scraped.readlines()[-1]
        final_line = final_line.split(',')[4]
        lily_speak('Thermosta is ' + final_line)
    return final_line
# if you want to change wake up word
WAKE = "wake up"

# listen for audio and convert it to text:
def record_audio():
    listener = sr.Recognizer() # initialise a recogniser 
    with sr.Microphone() as source: # microphone as source("microphone est affiché à la barre d'outils")
        audio = listener.listen(source)  # listen for the audio through source
        voice_data = ''       
        try:
            voice_data = listener.recognize_google(audio)  # convert audio to text
            print(voice_data)
        except Exception as e:
            print(str(e))
    return voice_data.lower() #The lower() method returns a string where all characters are lower case.
while True:
    voice_data = record_audio();
    if voice_data.count(WAKE) > 0:
        lily_speak("hy, How can I help you?")
        voice_data = record_audio()    

    # 1: Greeting==>(Salutation) "1" 
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)] # using random.randint(0, len(greetings) - 1), the function is limited to picking a valid index for the greetings list.
        lily_speak(greet)

    # 2: Name ==> question for Lily
    if there_exists(["what is your name","what's your name","tell me your name"]): 
        if person_obj.name:
            lily_speak("my name is Lily") # msg for the first answer
        else:
            lily_speak("my name is Lily. what's your name?") # msg for the second answer

    # 2: Name ==> answer for the question Lily
    if there_exists(["my name is"]): 
        person_name = voice_data.split("is")[-1].strip() #exp ==> my name is Fayza | or | my name is Farah
        lily_speak(f"okay, i will remember that {person_name}") # exp ==> okay, i will remember that Fayza |or| okay, i will remember that Farah
        person_obj.setName(person_name) # remember name in person object

    # 3: Greeting ==>(Salutation) "2"
    if there_exists(["how are you","how are you doing"]):
        lily_speak(f"I'm very well, thanks for asking {person_obj.name}")
    # 4: Time ==> question for time

    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        lily_speak(time)

    # 5: Date ==> question for date
    if there_exists(["what is the date today"]):
        date = date.today().strftime('%m %d, %Y')
        lily_speak(date)

    # 6: Thermosta     
    if there_exists(["Thermosta"]): 
        tmt= thermostat()   
        lily_speak("the is" + tmt)

    # 7: Temperature     
    if there_exists(["Temperature"]): 
        tmp= temp()   
        lily_speak("the is" + tmp)

    # 8: Humidity
    if there_exists(["Humidity"]): 
        hmy= hmudity()   
        lily_speak("the is" + hmy) 
    # 9: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term_google = voice_data.split("for")[-1]
        webbrowser.get().open(f"https://google.com/search?q={search_term_google}")
        lily_speak(f'Here is what I found for {search_term_google} on google')

    # for play song in youtube
    if 'play' in voice_data:
        song = voice_data.replace('play', '')
        pywhatkit.playonyt(song)

    # 10: to leave Mariya     
    if there_exists(["exit", "quit", "goodbye"]):
        lily_speak("going offline")
        exit()


         

    person_obj = person()
#print('How can I help you?')
#lily_speak('hy, How can I help you?')





