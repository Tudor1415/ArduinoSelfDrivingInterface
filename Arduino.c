
const int forward=8;
const int backward=9;
const int right=10;
const int left=11;


int value=0;

void setup() 
   { 
      Serial.begin(9600); 
      
      pinMode(forward, OUTPUT);
      digitalWrite (forward, HIGH);

      pinMode(backward, OUTPUT);
      digitalWrite (backward, HIGH);

      pinMode(right, OUTPUT);
      digitalWrite (right, HIGH);

      pinMode(left, OUTPUT);
      digitalWrite (left, HIGH);
      
      Serial.println("Connection established...");


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

   }
