/* Autonomous Vehicle */
#include <SoftwareSerial.h>

// Bluetooth communication
#define TXD 2
#define RXD 3
SoftwareSerial bluetooth(TXD, RXD);

// const int led = 9;
const int motor[2] = {9,10};
int led2= 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // pinMode(led, OUTPUT);
  pinMode(motor[0], OUTPUT);
  pinMode(motor[1], OUTPUT);
  // digitalWrite(motor[1], LOW);
  analogWrite(motor[0], 0);

}

void loop() {
  if (Serial.available()){
    char a = Serial.read();
    switch(a){
      // case '1':
      //   digitalWrite(led, HIGH);
      //   break;
      // case '2':
      //   digitalWrite(led, LOW);
      //   break;
      // case '3':
      //   digitalWrite(led, HIGH);
      //   delay(1000);
      //   digitalWrite(led, LOW);
      //   delay(1000);
      //   digitalWrite(led, HIGH);
      //   delay(1000);
      //   digitalWrite(led, LOW);
      //   delay(1000);
      //   break;
      // case '4':
      //   digitalWrite(led, HIGH);
      //   delay(500);
      //   digitalWrite(led, LOW);
      //   delay(500);
      //   digitalWrite(led, HIGH);
      //   delay(500);
      //   digitalWrite(led, LOW);
      //   delay(500);
      //   break;

      case 'w':
        Serial.println('w');
        analogWrite(motor[0], 255);
        // digitalWrite(motor[1], HIGH);
        // delay(500); d
        // digitalWrite(led, LOW);
        // delay(1000);
        break;
      case 's':
        Serial.println('s');
        analogWrite(motor[0], 120);
        // digitalWrite(motor[1], LOW);
        // digitalWrite(led2, HIGH);
        // delay(1000);
        // digitalWrite(led2, LOW);
        // delay(1000);
        break;
      case 't':
        Serial.println('t');
        // digitalWrite(led, LOW);
        analogWrite(motor[0], 0);
        // digitalWrite(motor[1], LOW);
        // delay(500);
        // delay(1000);
        // digitalWrite(led2, LOW);
        // delay(1000);
        break;
    }
  }

}
