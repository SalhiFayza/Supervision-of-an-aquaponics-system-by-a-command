#include <OneWire.h>
#include <DallasTemperature.h>
#define tempEau A0 
#include <dht.h>  // This is a library for the DHT series of low cost temperature / humidity sensors.
#define dataPin A1 // Define the pin number to which the sensor is connected.
#define DHTTYPE DHT22  // we call the dht22 sensor in the library
dht DHT ;
#define SensorPin A2          // the pH meter Analog output is connected with the Arduino’s Analog
unsigned long int avgValue;  //Store the average value of the sensor feedback( float b)
float b;
int buf[10],temp;
            



OneWire oneWire(tempEau); 
DallasTemperature sensors(&oneWire);

int  curr0, curr1, curr2, curr3;



void setup() {
  Serial.begin(9600);  // Open serial port, set data rate to 9600 bps.


}
void loop() {
  int readData = DHT.read22(dataPin); // Read the data from the sensor
  float t = DHT.temperature; // Retrieve the temperature values in degrees Celsius
  float h = DHT.humidity;  // Retrieve the humidity values
   sensors.requestTemperatures();
  double dTempWater = sensors.getTempCByIndex(0);

  for(int i=0;i<10;i++)       //Exp: (Get 10 sample value from the sensor for smooth the value)
  { 
    buf[i]=analogRead(SensorPin);
    delay(10);
  }
  for(int i=0;i<9;i++)        
  {
    for(int j=i+1;j<10;j++)
    {
      if(buf[i]>buf[j])
      {
        temp=buf[i];
        buf[i]=buf[j];
        buf[j]=temp;
      }
    }
  }
  avgValue=0;
  for(int i=2;i<8;i++)                     
    avgValue+=buf[i];
  float phValue=(float)avgValue*5.0/1024/6; //convert the analog into millivolt
  phValue=3.5*phValue; 



//Serial.print("Humidite(%)");
Serial.print(h);//Data Humidity
Serial.print(",");// separator
//Serial.print("Temperature(°C)");
Serial.print(t);//Data Temperature
Serial.print(",");
//Serial.print("TempératureEau (°C)");
Serial.print(dTempWater);
//Serial.print("    pH:");
 Serial.print(",");
 Serial.println(phValue,2);

digitalWrite(13, HIGH);       
delay(800);
digitalWrite(13, LOW); 

curr0 = h; 
curr1 = t; 
curr2 = dTempWater;
curr3 = phValue;
  delay(10000); // 10 second delay.
}
