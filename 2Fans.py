import requests
import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import RPi.GPIO as GPIO
from RPi.GPIO import OutputDevice

GPIO_pin1 = 18 #Fan NUM 1
GPIO_pin2 = 17 #Fan NUM 2
GPIO_pin3 = 19 #cylinder

cred = credentials.Certificate('file_data.json')

firebase_admin.initialize_app(cred,{'databaseURL': "https://aquaponicsapp-d4dda-default-rtdb.firebaseio.com/"})
ref = db.reference('Meassage')
def send():
    ref.set({"A problem has occurred with aquaponics temperature."})
    
    
# get temperature "File Excel"
def temp():
    try:
        current_date_and_time = datetime.today().strftime('%Y-%m-%d')
        current_date_and_time_string = str(current_date_and_time)
        file_name = current_date_and_time_string + ".csv"
        with open(file_name, "r", encoding="utf-8", errors="ignore") as scraped:
            final_line = scraped.readlines()[-1]
            final_line = final_line.split(',')[3]
        return int(final_line)
    except:
        print("Rapport of {0} not found !!!".format(file_name))
# get temperature with sfax
def today():
    try:
        api_key = "6ef0657b8bbe7a8463d13bacbd037251"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + "Sfax"
        response = requests.get(complete_url)
        x = response.json()
        y = x["main"]
        current_temperature = y["temp"]
        valeur = current_temperature - 273.15
        print(str(valeur))
        return int(valeur)
    except:
        print("No internet found !! or maybe ur key not work")


while True:
    if (temp() > 30) :
      OutputDevice(GPIO_pin1).on()
    elif (temp() >30) :
      OutputDevice(GPIO_pin2).on()
    elif(temp()>30 & today()<30): 
        OutputDevice(GPIO_pin3).on()
    else:
        send()
    # 60*15 min = 900 seconde 
    time.sleep(900)
