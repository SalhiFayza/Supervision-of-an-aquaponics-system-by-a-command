# Supervision of an aquaponics system by a command
# USING:
**************
- VSCode.
- Arduino.
**************
- Carte Raspberry pi 3 B+.
- Carte Arduino UNO.
- DHT22:

![image](https://user-images.githubusercontent.com/60444937/124829577-b327e700-df70-11eb-9333-4b9fcb267525.png)

- Capture the temperature using DHT22.
- Capture the humidity using DHT22.
- Water temperature sensor (DS18B20):

![image](https://user-images.githubusercontent.com/60444937/124829388-7825b380-df70-11eb-8ddd-3eb5a3e93f22.png)

- PH sensor (Pro SKU SEN0169):

![image](https://user-images.githubusercontent.com/60444937/124829681-ce92f200-df70-11eb-9262-ff809b3c52ce.png)

-  2 Fans.
-  Verin.
-  Relay a 4:

![image](https://user-images.githubusercontent.com/60444937/124829742-ec605700-df70-11eb-83a0-f8d185b2d21b.png)
 
 *******************************************
* Sensor test:
  - DHT22 (5s):
       
   ![image](https://user-images.githubusercontent.com/60444937/124831492-334f4c00-df73-11eb-924e-2ffed7fe72ee.png)
       
  - Water temperature sensor (DS18B20) (5s):
      
    Water temperature sensor test result on boiling water:
          
    ![image](https://user-images.githubusercontent.com/60444937/124831827-ac4ea380-df73-11eb-8b74-596b9a3b8b6c.png)
          
    Water temperature sensor test result on melted ice water:
          
    ![image](https://user-images.githubusercontent.com/60444937/124831934-d2744380-df73-11eb-8a4f-a3ee471d28d9.png)
          
  - PH sensor (Pro SKU SEN0169):  

**************************************************
- Connect your Carte Arduino to a carte Raspberry pi 3 B+ with a USB Cable.
- Install Python 3.9 in Raspberry pi 3 B+.
- Install Arduino in Raspberry pi 3 B+.
- Install VSCode in Raspberry pi 3B+.
- Create Python code to save DHT22 data in an excel file.
- Every day (24H) save a new excel file.
**************************************************
- Create file Excel:

![cykhvn](https://user-images.githubusercontent.com/60444937/124834003-ec635580-df76-11eb-9af6-7498f22d59b6.PNG)

**************************************************
- Send Data to Firebase:

![pokjhbv](https://user-images.githubusercontent.com/60444937/124834238-511eb000-df77-11eb-9773-56b2d4d4011e.PNG)

**************************************************
- Send Data to  ile Excel and Firebases:

![999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999](https://user-images.githubusercontent.com/60444937/124834342-7dd2c780-df77-11eb-9cc5-8d2ae761654d.PNG)

**************************************************
- Realization of the voice assistant
To fully understand the ins and outs, it is important to understand the basics that make up a voice assistant. To do this, we divide this operation into 4 main steps: 
     - The capture of the voice.
     - Converting voice to text.
     - Natural Language Understanding (NLU).
     - Text To Speech.
* How the voice assistant works    
![image](https://user-images.githubusercontent.com/60444937/124832593-c6d54c80-df74-11eb-9c60-fca0e76247e5.png)
***************************************************
* Sensor test voice assistant(Dependencies):
Voice Commands:
- What is your name?
- What time is it?
- What date for today?
- What is the temperature value?
- What is the humidity value?
- What is the weather in?
- What is the pH in?
- Play music "YouTube"

![image](https://user-images.githubusercontent.com/60444937/124833434-1405ee00-df76-11eb-9821-8a2ad56b16e5.png)

************************************************
- Every day (24H) send rapport to Gmail(Data Aquaponics).

![qwscxfd](https://user-images.githubusercontent.com/60444937/124834522-d73af680-df77-11eb-9654-7fdae164edaa.PNG)

![ml;ujtghb](https://user-images.githubusercontent.com/60444937/124834502-d013e880-df77-11eb-93c6-51eb564adc6b.PNG)

***********************************************
- Send Mail when the temperature is > a temperature normal:

![rrr](https://user-images.githubusercontent.com/60444937/124834618-fcc80000-df77-11eb-8f93-b937403cbdfe.PNG)

