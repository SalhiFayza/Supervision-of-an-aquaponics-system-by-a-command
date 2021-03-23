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
  float t = DHT.temperature; // Retrieve the temperature values
  float h = DHT.humidity;  // Retrieve the humidity values
  
float VALTHERMO = (THERMO / 6.388888888889);// conversion of thermostat value -> temperature
 
VALTHERMO = analogRead(THERMO); // read the value of the potentiometer value and store it in the variable (VALTHERMO)
VALTHERMO = map(VALTHERMO, 0, 1023, - 10, 40); // conversion by mapping the potentiometer value for 0 = -10 degrees and 1023 = 40 degrees.
  if (t <= VALTHERMO)//if the temperature is less than or equal to my stored value
  {
    digitalWrite (RELAIS, 1);// then I turn on the relay for my heating
  }
  else
  {
    digitalWrite (RELAIS, 0);
  }

//Serial.print("THERMOSTA(°)");
Serial.print(VALTHERMO);
Serial.print(",");// separator
//Serial.print("Humidite(%)");
Serial.print(h);//Data Humidity
Serial.print(",");// separator
//Serial.print("Temperature(°)");
Serial.println(t);//Data Temperature

curr1 = VALTHERMO;
curr2 = t; 
curr3 = h; 
  delay(10000); // 10 second delay.
}
