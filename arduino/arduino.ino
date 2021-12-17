#define sw 8
int flag = 0;

void setup() {
  pinMode(sw,INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(sw) == LOW) {
    if(flag == 0) {
//      Serial.print(1);
      Serial.println(1);
      
      flag = 1;

      delay(10);
    }
  } 
  else if(digitalRead(sw) == HIGH) {
    flag = 0;
  }
}
