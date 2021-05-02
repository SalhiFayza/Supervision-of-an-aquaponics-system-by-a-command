#include <dht.h>  // This is a library for the DHT series of low cost temperature / humidity sensors.
#define dataPin 8 // Define the pin number to which the sensor is connected.
#define DHTTYPE DHT22  // we call the dht22 sensor in the library
dht DHT ;
 
int RELAIS = 10; // declaration of PIN 10 for the relay
float THERMO = A0; // declaration of the potentiometer
int curr1, curr2, curr3;



void setup() {
  Serial.begin(9600);  // Open serial port, set data rate to 9600 bps.
  pinMode (THERMO, INPUT);
  pinMode (RELAIS, OUTPUT);
 

}
void loop() {
  int readData = DHT.read22(dataPin); // Read the data from the sensor
  float t = DHT.temperature; // Retrieve the temperature values in degrees Celsius
  float h = DHT.humidity;  // Retrieve the humidity values
  

//Serial.print("THERMOSTA(°)");
Serial.print(THERMO);
Serial.print(",");// separator
//Serial.print("Humidite(%)");
Serial.print(h);//Data Humidity
Serial.print(",");// separator
//Serial.print("Temperature(°)");
Serial.println(t);//Data Temperature

curr1 = THERMO;
curr2 = t; 
curr3 = h; 
  delay(10000); // 10 second delay.
}