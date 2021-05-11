import requests
import time
from datetime import datetime
from twilio.rest import Client
import RPi.GPIO as GPIO
from RPi.GPIO import OutputDevice

GPIO_pin1 = 18 #Fan NUM 1
GPIO_pin2 = 17 #Fan NUM 2
GPIO_pin3 = 19 #cylinder

def send():
    account_sid = 'AC6e6dd50f69693d0f751d12bb51fa7fcc'
    auth_token = 'e9cfb0fb09ddf78a74c45b960ac3e758'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="A problem has been occurred for aquaponics  temperature .{}".format(temp()),#alert msg
        from_='+14155238886',
        to='+21692848602'
    )
    print(message.sid)
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
    else:
        send()
        OutputDevice(GPIO_pin3).on()
    # 60*15 min = 900 seconde 
    time.sleep(900)
