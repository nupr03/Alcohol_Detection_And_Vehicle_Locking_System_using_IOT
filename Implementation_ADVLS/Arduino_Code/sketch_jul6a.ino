   // Define the pin to which the sensor is connected
#define green 8
#define red 9
#define motor 7
const int sensorPin = A0;

void setup() {
  // Initialize serial communication
  pinMode(green, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(motor, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  // Read the analog value from the sensor
  int sensorValue = analogRead(sensorPin);
  // Serial.print("Sensor Value: ");
  Serial.println(sensorValue);
  if (sensorValue < 300                                                                                                                                                                                                                                                                                                                                                                                                                                ) {
    digitalWrite(green, HIGH);
    digitalWrite(red, LOW);
    digitalWrite(motor, LOW);
  }

  else {
    digitalWrite(red, HIGH);
    digitalWrite(green, LOW);
    digitalWrite(motor, HIGH);
  }


  delay(300); // Delay for 1 second
}

