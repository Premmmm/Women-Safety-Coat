it#include <SoftwareSerial.h>

SoftwareSerial mySerial(2,3);

int a;
void setup()
{  
  mySerial.begin(9600);   // Setting the baud rate of GSM Module  
  Serial.begin(9600);    // Setting the baud rate of Serial Monitor (Arduino)
  delay(100);
}


void loop()
{
 
if(Serial.available()>0)
switch(Serial.read())
{
  case 's':
   mySerial.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
  delay(1000);  // Delay of 1000 milli seconds or 1 second
  mySerial.println("AT+CMGS=\"+919962490855\"\r"); // Replace x with mobile number
  delay(1000);
  mySerial.println("Hi rahil");// The SMS text you want to send
  delay(100);
   mySerial.println((char)26);// ASCII code of CTRL+Z
  delay(1000);
  break;

  case 'r':
  mySerial.println("AT+CMGT=2,2,0,0,0");
  delay(1000);
  break;
}

if(mySerial.available()>0)
  Serial.write(mySerial.read());

}
  
