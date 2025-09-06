#include <Servo.h>

Servo servo;

void setup() {
  servo.attach(9);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');

    if (input == "Plastic") servo.write(30);
    else if (input == "Paper") servo.write(60);
    else if (input == "Metal") servo.write(90);
    else if (input == "Organic") servo.write(120);
    else if (input == "Glass") servo.write(150);

    delay(2000);
    servo.write(0);  // Reset position
  }
}
