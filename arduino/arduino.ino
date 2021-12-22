#define sw 8
#define led 7
int flag = 0;

void setup() {
  pinMode(sw,INPUT_PULLUP);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(led, HIGH);
  if(digitalRead(sw) == LOW) {
    if(flag == 0) {
//      Serial.print(1);
      Serial.println(1);
      digitalWrite(led, LOW);
      delay(100);
      digitalWrite(led, HIGH);
      delay(100);
      digitalWrite(led, LOW);
      delay(100);
      digitalWrite(led, HIGH);
      delay(100);
      digitalWrite(led, LOW);
      delay(100);
      digitalWrite(led, HIGH);
      delay(100);
      digitalWrite(led, LOW);
      delay(100);
      digitalWrite(led, HIGH);
      
      flag = 1;

      delay(10);
    }
  } 
  else if(digitalRead(sw) == HIGH) {
    flag = 0;
  }
}
