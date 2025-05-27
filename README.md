# Supervision of an Aquaponics System by Command

## USING:
- VSCode
- Arduino

### Hardware:
- Raspberry Pi 3 B+
- Arduino UNO

### Sensors:
- **DHT22**:
  - Captures temperature and humidity

  ![image](https://user-images.githubusercontent.com/60444937/124829577-b327e700-df70-11eb-9333-4b9fcb267525.png)

- **Water Temperature Sensor (DS18B20)**:

  ![image](https://user-images.githubusercontent.com/60444937/124829388-7825b380-df70-11eb-8ddd-3eb5a3e93f22.png)

- **pH Sensor (Pro SKU SEN0169)**:

  ![image](https://user-images.githubusercontent.com/60444937/124829681-ce92f200-df70-11eb-9262-ff809b3c52ce.png)

- 2 Fans
- Verin (Actuator)
- 4-Channel Relay Module:

  ![image](https://user-images.githubusercontent.com/60444937/124829742-ec605700-df70-11eb-83a0-f8d185b2d21b.png)

---

## Sensor Tests

### DHT22 (every 5s):

![image](https://user-images.githubusercontent.com/60444937/124831492-334f4c00-df73-11eb-924e-2ffed7fe72ee.png)

### Water Temperature Sensor (DS18B20) (every 5s):

- Test on boiling water:

  ![image](https://user-images.githubusercontent.com/60444937/124831827-ac4ea380-df73-11eb-8b74-596b9a3b8b6c.png)

- Test on melted ice water:

  ![image](https://user-images.githubusercontent.com/60444937/124831934-d2744380-df73-11eb-8a4f-a3ee471d28d9.png)

### pH Sensor (Pro SKU SEN0169)

---

## Full Sensor Test with Arduino:
**File:** `DTH22_Potentiometer/DTH22_Potentiometer.ino`

![kjhbv](https://user-images.githubusercontent.com/60444937/124835283-fd14cb00-df78-11eb-8e73-6225deb36b44.PNG)

---

## System Setup

- Connect Arduino UNO to Raspberry Pi 3 B+ via USB.
- Install Python 3.9, Arduino IDE, and VSCode on the Raspberry Pi.
- Create Python scripts to:
  - Save DHT22 data to an Excel file.
  - Generate a new Excel file every 24 hours.

---

## Python Script: `import_csv.py`
- Save sensor data to Excel:

  ![cykhvn](https://user-images.githubusercontent.com/60444937/124834003-ec635580-df76-11eb-9af6-7498f22d59b6.PNG)

- Send Data to Firebase:

  ![pokjhbv](https://user-images.githubusercontent.com/60444937/124834238-511eb000-df77-11eb-9773-56b2d4d4011e.PNG)

- Simultaneously send data to Excel and Firebase:

  ![999999...](https://user-images.githubusercontent.com/60444937/124834342-7dd2c780-df77-11eb-9cc5-8d2ae761654d.PNG)

---

## Voice Assistant

### Process Breakdown:
1. Capture voice
2. Convert voice to text
3. Natural Language Understanding (NLU)
4. Convert text to speech (TTS)

**Voice Assistant Diagram:**

![image](https://user-images.githubusercontent.com/60444937/124832593-c6d54c80-df74-11eb-9c60-fca0e76247e5.png)

### Voice Command Script: `lily.py`

Supported Commands:
- What is your name?
- What time is it?
- What date is today?
- What is the temperature value?
- What is the humidity value?
- What is the weather in?
- What is the pH in?
- Play music on YouTube

![image](https://user-images.githubusercontent.com/60444937/124833434-1405ee00-df76-11eb-9821-8a2ad56b16e5.png)

---

## Email Reports

### Daily Reports (Every 24H): `chartsmail.py`

![qwscxfd](https://user-images.githubusercontent.com/60444937/124834522-d73af680-df77-11eb-9654-7fdae164edaa.PNG)
![ml;ujtghb](https://user-images.githubusercontent.com/60444937/124834502-d013e880-df77-11eb-93c6-51eb564adc6b.PNG)

---

## Alert System

### Temperature Threshold Notification via Email: `fans.py`

![rrr](https://user-images.githubusercontent.com/60444937/124834618-fcc80000-df77-11eb-8f93-b937403cbdfe.PNG)

---

## Launch the Full System
Run: `main.py`
