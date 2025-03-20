const int pins[] = {22, 23, 24, 25};  // Pins you want to toggle
bool pinStates[] = {false, false, false, false};  // Track pin states

void setup() {
  Serial.begin(9600);  // Initialize serial communication at 9600 baud
  for (int i = 0; i < 4; i++) {
    pinMode(pins[i], OUTPUT);
    digitalWrite(pins[i], LOW);
  }
}

void loop() {
  if (Serial.available() > 0) {
    int buttonIndex = Serial.read();  // Read button index (0 to 3)
    if (buttonIndex >= 0 && buttonIndex < 4) {
      pinStates[buttonIndex] = !pinStates[buttonIndex];  // Toggle the pin state
      digitalWrite(pins[buttonIndex], pinStates[buttonIndex] ? HIGH : LOW);
    }
  }
}
