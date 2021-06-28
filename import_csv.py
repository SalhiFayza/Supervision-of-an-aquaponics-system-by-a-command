import csv  # lib csv for excel
import serial  # lib serial for read the port usb Arduino uno
from datetime import datetime
import os
from datetime import date  
import time


ser = serial.Serial("COM3", 9600)  # open serial port
ser.flushInput()  # input data Arduino uno
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
   
    ser_bytes = ser.readline().decode().strip().split(',')  # use split(',') to seperate ser_byte string to list
    new_ser_bytes = [float(i) for i in ser_bytes]  # using list comprehension to perform conversion to float
    t = time.localtime()  # time location
    decoded_time1 = time.strftime('%Y-%m-%d', t)  # for date
    decoded_time2 = time.strftime('%H:%M:%S', t)  # for time
    current_date_and_time = date.today().strftime('%Y-%m-%d')
    current_date_and_time_string = str(current_date_and_time)
    file_name = current_date_and_time_string + ".csv"
    print(decoded_time1, decoded_time2, ser_bytes)  # print date , time, and data Arduino uno
    with open(file_name, "a", newline='') as f:  # create and open the file csv
        writer = csv.writer(f, delimiter=",")  # Split the string, using comma, followed by a space, as a separator
        writer.writerow([decoded_time1, decoded_time2, ser_bytes[0], ser_bytes[1],
                         ser_bytes[2], ser_bytes[3]])  # writerow with seperate data, time , data1 and data2
        f.close()  # close file test_file.csv
    # 1h for sleep
    time.sleep(10)