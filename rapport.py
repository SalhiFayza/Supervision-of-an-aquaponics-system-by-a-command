from datetime import datetime
from typing import ContextManager
import pandas as pd
import smtplib
from email.mime.text import MIMEText

current_date_and_time = datetime.today().strftime('%Y-%m-%d')
current_date_and_time_string = str(current_date_and_time)
file_name = current_date_and_time_string + ".csv"

def read():
    df = pd.read_csv(file_name)
    minValueOfTemperature = df.query('Temperature == Temperature.max()')
    maxvalueOFTemperature = df.query('Temperature == Temperature.min()')
    minValueOfHumidity = df.query('Humidity == Humidity.max()')
    maxvalueOFHumidity = df.query('Humidity == Humidity.min()')
    minWaterTemp = df.query('WaterTemp == WaterTemp.max()')
    maxWaterTemp = df.query('WaterTemp == WaterTemp.min()')
    minpH = df.query('pH == pH.max()')
    maxpH = df.query('pH == pH.min()')
    print("===========Max Temperature ===========")
    print(minValueOfTemperature)
    print("===========Min Temperature ===========")
    print(maxvalueOFTemperature)
    print("===========Max Humidity ===========")
    print(minValueOfHumidity) 
    print("===========Min Humidity ===========")
    print(maxvalueOFHumidity)
    print("===========Max WaterTemp ===========")
    print(minWaterTemp)
    print("===========Min WaterTemp ===========")
    print(maxWaterTemp)
    print("===========Max pH ===========")
    print(minpH) 
    print("===========Min pH ===========")
    print(maxpH)
    information ='Min Temperature \n' + str(minValueOfTemperature) + '\n Max Temperature \n' + str(maxvalueOFTemperature) + '\nMin Humidity \n' + str(minValueOfHumidity) + '\nMax Humidity \n' + str(maxvalueOFHumidity)+ 'Min WaterTemp \n' + str(minWaterTemp) + '\n Max  WaterTemp \n' + str(maxWaterTemp) + '\nMin pH \n' + str(minpH) + '\nMax pH \n' + str(maxpH)

    try:
        sender_address = 'farahbenlassoued1@gmail.com'
        sender_pass = 'farahtaz2020'
        receiver_address = 'fayzasalhif@gmail.com'
        
        msg = information
        message = MIMEText(msg)
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = "Rapport Of {} ".format(current_date_and_time)
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass) 
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
    except:
        print('SMTP NOT WORK  ')
read()