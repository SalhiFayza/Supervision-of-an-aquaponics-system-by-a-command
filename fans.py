import requests

import time

from datetime import datetime

import serial

from firebase import firebase



import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)

#from RPi.GPIO import OutputDevice

import pandas as pd

import smtplib

from email.mime.text import MIMEText

pinList = [2, 3, 4]



for i in pinList:

    GPIO.setup(i, GPIO.OUT)

    GPIO.output(i, GPIO.HIGH)







def send():

    try:

        sender_address = 'farahbenlassoued1@gmail.com'

        sender_pass = 'farahtaz2020'

        receiver_address = 'fayzasalhif@gmail.com'

        

        msg = """

        <h1 style="text-align:center"><span style="font-size:20px"><span style="color:#c0392b"><strong>A problem has occurred with aquaponics temperature !!</strong></span></span></h1>



        <p style="text-align:center"><span style="color:#c0392b"><strong><img alt="" src='https://i.ibb.co/B2WXJWJ/106387611-731148894326413-817694419904864585-n.gif?fbclid=IwAR3qwMdqPNPtsJkuoumXknTFjhC30ZmrU9c7TS-9cWD780CAfZXNUcUxmrs' style="height:101px; margin:20px 100px; width:100px" /></strong></span></p>

        """

        message = MIMEText(msg, 'html')



        message['From'] = sender_address

        message['To'] = receiver_address

        message['Subject'] = "Notification"

        # Create SMTP session for sending the mail

        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port

        session.starttls()  # enable security

        session.login(sender_address, sender_pass)  # login with mail_id and password

        text = message.as_string()

        session.sendmail(sender_address, receiver_address, text)

        session.quit()

        print('Mail Sent')

    except:

        print('SMTP NOT WORK  ')

send()

   

    

    

# get temperature "File Excel"

def temp():

    try:

        current_date_and_time = datetime.today().strftime('%Y-%m-%d')

        current_date_and_time_string = str(current_date_and_time)

        file_name = current_date_and_time_string + ".csv"

        with open(file_name, "r", encoding="utf-8", errors="ignore") as scraped:

            final_line = scraped.readlines()[-1]

            final_line = final_line.split(',')[3]

            print("Val :::: {0} ".format(final_line))

        return final_line

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
    aa = firebase.FirebaseApplication('https://aquaponicsapp-d4dda-default-rtdb.firebaseio.com/', None)
    Result = aa.get('/temp/data', None)
    print('Resss :',Result)
    if (+int(float(temp())) > +int(Result)) :
      #OutputDevice(GPIO_pin1).on()
      
       GPIO.output(2, GPIO.LOW)
       print('v1')
       time.sleep(900);
       
       GPIO.output(3, GPIO.LOW)
       print('v2')
       time.sleep(900)
    elif (+int(float(temp())) > +int(Result) & +int(float(today())) < +int(Result)): 
        #OutputDevice(GPIO_pin3).on()
         GPIO.output(3, GPIO.LOW)
         print('verin')
         time.sleep(900);
    else:
        send()