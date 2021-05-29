from datetime import datetime
import time
from typing import ContextManager
from matplotlib import colors
import pandas as pd
import smtplib
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
import mplfinance as mpf 
import numpy as np
import mplcyberpunk
import matplotlib.dates as mdates



plt.style.use('cyberpunk')

current_date_and_time = datetime.today().strftime('%Y-%m-%d')
current_date_and_time_string = str(current_date_and_time)
file_name = current_date_and_time_string + ".csv"


def read():
    I020 = [ line.strip('\n').split(",") for line in open(file_name)][1:]
    Time = [datetime.strptime(line[1],"%H:%M:%S") for line in I020]
    
    temp = [float(line[3]) for line in I020]
    humy = [float(line[2]) for line in I020]
    Water = [float(line[4]) for line in I020]
    ph = [float(line[5]) for line in I020]

    plt.figure(1)
    plt.suptitle('$Data\ For\ Aquaponics$', size=20)
#Plot temperature
    x0 = Time
    y0 = temp
    plt.subplot(221)
    plt.plot(x0,y0)
    plt.title("Temperature(°C)", size=16)
    mplcyberpunk.add_glow_effects()
    
    plt.xticks(rotation=30)
#Plot humidity    
    x1 = Time
    y1 = humy
    plt.subplot(222)
    plt.title("Humidity(%)", size=16)
    plt.plot(x1,y1)
    mplcyberpunk.add_glow_effects()
    plt.xticks(rotation=30)
#Plot watertemp
        
    x3 = Time
    y3 = Water
    plt.subplot(223)
    plt.xlabel("WaterTemp(°C)", size=16)
    plt.plot(x3,y3)
    
    mplcyberpunk.add_glow_effects()
    plt.xticks(rotation=30)
#Plot ph
    x4 = Time
    y4 = ph
    plt.subplot(224)
    plt.plot(x4,y4)
    plt.xticks(rotation=30)
    plt.xlabel("pH", size=16)
    mplcyberpunk.add_glow_effects()
    
    msg1 =plt.show()
    
    try:
        sender_address = 'farahbenlassoued1@gmail.com'
        sender_pass = 'farahtaz2020'
        receiver_address = 'fayzasalhif@gmail.com'
       
        msg = msg1
        message = MIMEText(msg)
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = "Rapport Of {} ".format(current_date_and_time)
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
read()