from datetime import date
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
import time 



ser = serial.Serial("COM3", 9600)  # open serial port
ser.flushInput()
ser_bytes = ser.readline().decode().strip().split(',')  # use split(',') to seperate ser_byte string to list
cred = credentials.Certificate('file_data.json')

firebase_admin.initialize_app(cred,{'databaseURL': "https://aquaponicsapp-d4dda-default-rtdb.firebaseio.com/"})
ref = db.reference('DHT22')


while True:
   
    ser_bytes = ser.readline().decode().strip().split(',')
    new_ser_bytes = [float(i) for i in ser_bytes]
    temperature = new_ser_bytes[1]
    humidity = new_ser_bytes[2]
    temperatureEau =new_ser_bytes[3]
    ph =new_ser_bytes[4]
    if humidity is not None and temperature is not None:
        time.sleep(5)

        print('Temperature={0:0.1f} °C Humidity={1:0.1f} % TemperatureEau={2:0.1f} °C PH={3:0.1f}'.format(temperature, humidity, temperatureEau, ph))
    else:
        print('Failed to get reading. Try again!')
        time.sleep(10)
        
    ref.set({
        
        'Temperature':{"Data":' %.1f °C' % temperature}, 
        'Humidity': {"Data":' %.1f %%' % humidity},
        'TempEau':{"Data": ' %.1f °C' % temperatureEau},
        'PH':{"Data": ' %.1f' % ph}
     }) 
    time.sleep(10) 
       

    	