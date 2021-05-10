from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import os

td = datetime.date.today()

# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-minimized') #maximized
wd = webdriver.Chrome(r'D:/Learning/Practice/Selenium/chromedriver.exe',options=CO)

# Format for printing output
print ("Connecting to Worldwide weather data, Please wait .....\n")
weather_site = "https://www.timeanddate.com/weather/?sort=6&low=4"
wd.get(weather_site)
wd.implicitly_wait(wait_imp)

temp_raw = wd.find_elements_by_class_name('rbi')
temp_1 = []

for val in temp_raw:
    t1 = (val.text).split()
    if t1[0] != "N/A":
        temp_1.append (int(t1[0]))
      
temp_1.sort(reverse = True)
max_temp = max(temp_1)
min_temp = min(temp_1)

# Read table
table_data = wd.find_element(By.CLASS_NAME, 'zebra.fw.tb-theme')
table_row = wd.find_elements(By.TAG_NAME, "tr")
city_name = []
temp_val = []

lst = [0,4,8]
for i in range(1,len(table_row)):
    for j in lst:
        col = table_row[i].find_elements(By.TAG_NAME, "td")[j].text
        tmp = table_row[i].find_elements(By.TAG_NAME, "td")[j+3].text
        t6 = tmp.split()
        print (col, t6)
        city_name.append(col)
        temp_val.append(t6)
        
for p in range(len(temp_val)):
    if temp_val[p][0] == str(max_temp):
        c_name_H = city_name[p]
        print (c_name_H)
        break
p = 0
for p in range(len(temp_val)):
    if temp_val[p][0] == str(min_temp):
        c_name_C = city_name[p]
        print (city_name[p])
        break

print ("Date:",td.strftime("%b-%d-%Y"))
print ("--------------------------------------------------------------------")
print (">>>>>>>>>>>>>>>>>>> World's Hottest and Coldest Place <<<<<<<<<<<<<<")
print ("------------------------------------------------------------------\n")

print ("Highest Temperature on the Earth is: {} deg C and Place is: {}".format(max_temp,c_name_H))
print ("Lowest Temperature on the Earth is : {} deg C and Place is: {}".format(min_temp, c_name_C))
wd.close()