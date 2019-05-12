#include <Servo.h>

const int forward=8;
const int backward=9;
const int right=10;
const int left=11;
const int ENA = 2;
const int in1a = 3;
const int in2a = 4;
const int ENB = 8;
const int in1b = 5;
const int in2b = 6;
const int ServoM = 9;

int value=0;
Servo Servo1;
void setup()
   {
      Serial.begin(9600);

      pinMode(forward, OUTPUT);
      digitalWrite (forward, HIGH);
      Servo1.attach(ServoM);
      pinMode(backward, OUTPUT);
      digitalWrite (backward, HIGH);

      pinMode(right, OUTPUT);
      digitalWrite (right, HIGH);

      pinMode(left, OUTPUT);
      digitalWrite (left, HIGH);

      Servo1.attach(Servo1);
      Serial.println("Connection established...");


   }
void turnAngle(angle){
   Servo1.write(angle);
}
void loop()
   {
     while (Serial.available())
        {
           value = Serial.read();
        }


     if (value == 'f'){
        digitalWrite (forward, LOW);
     }
     else if (value == 'b'){
        digitalWrite (backward, LOW);
     }
     else if (value == 'r'){
        digitalWrite (right, LOW);
     }
     else if (value == 'l'){
        digitalWrite (left, LOW);
     }
     else if (value == 'o'){
        digitalWrite (forward, HIGH);
        digitalWrite (backward, HIGH);
        digitalWrite (right, HIGH);
        digitalWrite (left, HIGH);
     }
     else if (value == 'y'){
        digitalWrite (ENA, HIGH);
        digitalWrite (ENB, HIGH);
        digitalWrite (in1a, LOW);
        digitalWrite (in1b, HIGH);
        digitalWrite (in2a, LOW);
        digitalWrite (in2b, HIGH);

     }
     else if (value == 'h'){
        digitalWrite (ENA, HIGH);
        digitalWrite (ENB, HIGH);
        digitalWrite (in1a, HIGH);
        digitalWrite (in1b, LOW);
        digitalWrite (in2a, HIGH);
        digitalWrite (in2b, LOW);
     }
     else if (value == 'j'){
        Servo1.write(45);
     }
     else if (value == 'g'){
        Servo1.write(-45);
     }
     else if (isDigit(value)) {  // tests if myChar is a digit
        turnAngle(value)
     }
   }
