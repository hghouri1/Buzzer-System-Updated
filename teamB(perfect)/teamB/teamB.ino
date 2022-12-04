/////////////////////////////////
// Generated with a lot of love//
// with TUNIOT FOR ESP8266     //
// Website: Easycoding.tn      //
/////////////////////////////////
#include <ESP8266WiFi.h>

#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

WiFiClient wifiClient;
String  mystring;
long  i;
String  httpurl;
String  TheHiddenAnswerOfClient;
int buzzerPin = 13;
int lightPin = 12;
int switchPin = 4;
String answer;
HTTPClient http;

const char* ssid = "Hsquare-Group"; //Enter SSID
const char* password = "H^2square"; //Enter Password

String SendWithAnswer(String IPcache, String monmessagecache) {
httpurl = "http://";
httpurl+=IPcache;
httpurl+="/";
httpurl+=monmessagecache;
http.begin(wifiClient,httpurl);
http.GET();
TheHiddenAnswerOfClient = (http.getString());
http.end();
return TheHiddenAnswerOfClient;
}

void setup()
{
  //WiFiManager wifiManager;
  pinMode(lightPin,OUTPUT);
  pinMode(buzzerPin,OUTPUT);
  pinMode(switchPin,INPUT);
  //wifiManager.autoConnect("AutoConnectAP");
  mystring = "TeamA";

  i = 0;
  Serial.begin(9600);
  WiFi.disconnect();
  delay(3000);
  Serial.println("START");
  WiFi.begin(ssid,password);
  while ((!(WiFi.status() == WL_CONNECTED))){
    delay(300);
    Serial.print("..");
    digitalWrite(buzzerPin,HIGH);

  }
  Serial.println("Connected");
  Serial.println("Your IP is");
  Serial.println((WiFi.localIP().toString()));

}


void loop()
{

    if (digitalRead(switchPin) == 1){
        answer = (SendWithAnswer("192.168.1.108:8080",mystring));
        Serial.println(answer);
        if (answer=="on"){
          digitalWrite(buzzerPin, LOW);
          digitalWrite(lightPin,LOW);
          delay(500);
          digitalWrite(lightPin,HIGH);
          delay(500);
          digitalWrite(buzzerPin,HIGH);
          digitalWrite(lightPin,LOW);
          delay(500);
          digitalWrite(lightPin,HIGH);
          delay(500);
          digitalWrite(lightPin,LOW);
          delay(500);
          digitalWrite(lightPin,HIGH);
          delay(500);
          digitalWrite(lightPin,LOW);
          delay(500);
          digitalWrite(lightPin,HIGH);
          delay(500);
          digitalWrite(lightPin,LOW);
          delay(500);
          digitalWrite(lightPin,HIGH);
          delay(500);
          digitalWrite(lightPin,LOW);
          delay(500);
          digitalWrite(lightPin,HIGH);
          delay(500);
          digitalWrite(lightPin,LOW);
          delay(500);
          digitalWrite(lightPin,HIGH);
          delay(500);
          digitalWrite(lightPin,LOW);
          delay(500);
          digitalWrite(lightPin,HIGH);
          delay(500);
          digitalWrite(lightPin,LOW);
          delay(500);
          digitalWrite(lightPin,HIGH);
          delay(500);
          
        }else{
          digitalWrite(lightPin,HIGH);
          digitalWrite(buzzerPin,HIGH);
        }
        
    }else{
      while((!(WiFi.status() == WL_CONNECTED))){
       digitalWrite(lightPin,LOW);
       delay(50);
     }
      digitalWrite(lightPin,HIGH);
      digitalWrite(buzzerPin,HIGH);
    }


//   i = i + 1;
//    digitalWrite(9,HIGH);
//    digitalWrite(10,HIGH);
//    delay(10000);
//    digitalWrite(9,LOW);
//    digitalWrite(10,LOW);
   // delay(2000);
}
