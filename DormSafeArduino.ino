
#include <Firebase_Arduino_WiFiNINA.h>
#include <Firebase_Arduino_WiFiNINA_HTTPClient.h>



#include "Firebase_Arduino_WiFiNINA.h"
#include "Arduino_LSM6DS3.h"

#define FIREBASE_HOST "URL"
#define FIREBASE_AUTH "AUTH Pass"
#define WIFI_SSID "Wifi"
#define WIFI_PASSWORD "PASSWORD"

FirebaseData firebaseData;


#include <Servo.h>

  Servo servo1;

  
void setup() {
  // put your setup code here, to run once:

    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

      WiFi.localIP();
 // Serial.println();
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH, WIFI_SSID, WIFI_PASSWORD);

servo1.attach(6);
  pinMode(3, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  
  
}

void loop() {
  // put your main code here, to run repeatedly:


  servo1.write(0);
  servo1.writeMicroseconds(500);

  bool val = Firebase.getBool(firebaseData, "/tempLoginVal");

if(val==true)
{
   digitalWrite(12, HIGH);
  delay(1000);
  digitalWrite(12, LOW);
  
}
val = Firebase.getBool(firebaseData, "/tempLoginVal");
if(val==false)
{
   digitalWrite(12, HIGH);
  
}

}
