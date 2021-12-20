#define pirPIN 7
int value=0;

void setup() {
  pinMode(pirPIN,INPUT);
  Serial.begin(9600);
}

void loop() {
  value=digitalRead(pirPIN);
  Serial.println(value);
}
