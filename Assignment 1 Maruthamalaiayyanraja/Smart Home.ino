// C++ code
//
void setup()
{
  pinMode(2, INPUT);
  pinMode(4, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int m=digitalRead(2);
  Serial.print("Motion Detected:");
  Serial.println(m);
  if(m==1)
  {
    digitalWrite(4, HIGH);
    digitalWrite(7, LOW);
  }
  else
  {
    digitalWrite(7, HIGH);
    digitalWrite(4, LOW);
  }
  double a=analogRead(A1);
  Serial.print("ADC Value:");
  Serial.println(a);
  double v=a/1024;
  double volt=v*5;
  Serial.print("Temp Value:");
  Serial.println(volt);
  double x=volt-0.5;
  double t=x*100;
  Serial.print("Temperature:");
  Serial.println(t);
  if(t>35)
  {
    digitalWrite(8, HIGH);
  }
  else
  {
    digitalWrite(8, LOW);
  }
  delay(3000);
}