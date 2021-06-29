from datetime import date
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
import time 
import os
import csv  # lib csv for excel


ser = serial.Serial("COM3", 9600)  # open serial port
ser.flushInput()
ser_bytes = ser.readline().decode().strip().split(',')  # use split(',') to seperate ser_byte string to list
cred = credentials.Certificate('file_data.json')

firebase_admin.initialize_app(cred,{'databaseURL': "https://aquaponicsapp-d4dda-default-rtdb.firebaseio.com/"})
ref = db.reference('DATA')
def createfile():
    current_date_and_time = date.today().strftime('%Y-%m-%d')
    current_date_and_time_string = str(current_date_and_time)
    file_name = current_date_and_time_string + ".csv"
    if not os.path.isfile(file_name):
        with open(file_name, "a", newline='') as f:  # create and open the file csv
            writer = csv.writer(f, delimiter=",")  # Split the string, using comma, followed by a space, as a separator
            writer.writerow(
                ["date", "Time","Humidity","Temperature",  "WaterTemp","pH"])  # titles for columns file excel

            f.close()  # close file test_file.csv
    else:
        pass

while True:
    createfile()
    ser_bytes = ser.readline().decode().strip().split(',') # use split(',') to seperate ser_byte string to list
    new_ser_bytes = [float(i) for i in ser_bytes]# using list comprehension to perform conversion to float
    humidity = new_ser_bytes[0]
    temperature = new_ser_bytes[1]
    WaterTemp =new_ser_bytes[2]
    ph =new_ser_bytes[3]
    t = time.localtime()  # time location
    decoded_time1 = time.strftime('%Y-%m-%d', t)  # for date
    decoded_time2 = time.strftime('%H:%M:%S', t)  # for time
    current_date_and_time = date.today().strftime('%Y-%m-%d')
    current_date_and_time_string = str(current_date_and_time)
    file_name = current_date_and_time_string + ".csv"

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
    with open(file_name, "a", newline='') as f:  # create and open the file csv
        writer = csv.writer(f, delimiter=",")  # Split the string, using comma, followed by a space, as a separator
        writer.writerow([decoded_time1, decoded_time2, ser_bytes[0], ser_bytes[1],
                         ser_bytes[2], ser_bytes[3]])  # writerow with seperate data, time , data1 and data2
        f.close()  # close file test_file.csv
    # 1h for sleep

    time.sleep(10) 
       
    
    
    
    	