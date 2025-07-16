#include <Servo.h>

Servo handServo;

const int servoPin = 9;

// Define angles for each gesture
const int ROCK = 0;
const int PAPER = 60;
const int SCISSORS = 120;

void setup() {
  handServo.attach(servoPin);
  randomSeed(analogRead(A0)); // Seed RNG with noise from unused analog pin
}

void loop() {
  // Cycle through gestures 3 times
  for (int i = 0; i < 3; i++) {
    handServo.write(ROCK);
    delay(500);
    handServo.write(PAPER);
    delay(500);
    handServo.write(SCISSORS);
    delay(500);
  }

  // Randomly pick a final gesture
  int choice = random(3); // 0 = Rock, 1 = Paper, 2 = Scissors

  if (choice == 0) {
    handServo.write(ROCK);
  } else if (choice == 1) {
    handServo.write(PAPER);
  } else {
    handServo.write(SCISSORS);
  }

  delay(3000); // Hold the final gesture for 3 seconds
}
