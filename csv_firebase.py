from datetime import date
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
import time 
import os
import csv  # lib csv for excel
import requests
import time
from datetime import datetime

from firebase import firebase




ser = serial.Serial("COM3", 9600)  # open serial port
ser.flushInput()
ser_bytes = ser.readline().decode().strip().split(',')  # use split(',') to seperate ser_byte string to list
cred = credentials.Certificate('file_data.json')

firebase_admin.initialize_app(cred,{'databaseURL': "https://aquaponicsapp-d4dda-default-rtdb.firebaseio.com/"})
ref = db.reference('DATA')

    
while True:
    
    ser_bytes = ser.readline().decode().strip().split(',') # use split(',') to seperate ser_byte string to list
    new_ser_bytes = [float(i) for i in ser_bytes]# using list comprehension to perform conversion to float
    humidity = new_ser_bytes[0]
    temperature = new_ser_bytes[1]
    WaterTemp =new_ser_bytes[2]
    ph =new_ser_bytes[3]
    

    if humidity is not None and temperature is not None and WaterTemp is not None and ph is not None:
        time.sleep(5)

        print('Humidity={0:0.2f} % Temperature={1:0.2f} °C WaterTemp={2:0.2f} °C pH={3:0.2f}'.format(humidity, temperature, WaterTemp, ph))
    else:
        print('Failed to get reading. Try again!')
        time.sleep(10)
        
    ref.set({
        'Humidity': {"Data":' %.2f %%' % humidity},
        'Temperature':{"Data":' %.2f °C' % temperature}, 
        'WaterTemp':{"Data": ' %.2f °C' % WaterTemp},
        'pH':{"Data": ' %.2f' % ph}
     }) 
  
 
    
    # 60*15 min = 900 seconde 
    time.sleep(900)
     
       
    
    
    
    	