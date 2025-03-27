const int pins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};  // 12 pins
bool pinStates[12] = {false};  // Track pin states
const int ledPin = LED_BUILTIN;  // Onboard LED pin (usually pin 13)

void setup() {
  Serial.begin(9600);  // Initialize serial communication at 9600 baud
  pinMode(ledPin, OUTPUT);  // Set onboard LED as output
  for (int i = 0; i < 12; i++) {
    pinMode(pins[i], OUTPUT);
    digitalWrite(pins[i], LOW);
  }
}

void loop() {
  if (Serial.available() > 0) {
    int buttonIndex = Serial.read();  // Read button index (0 to 11)
    if (buttonIndex >= 0 && buttonIndex < 12) {
      pinStates[buttonIndex] = !pinStates[buttonIndex];  // Toggle the pin state

      int pin_state = HIGH;

      if (pinStates[buttonIndex]) {
        pin_state = HIGH;
      }
      else {
        pin_state = LOW;
      }

      digitalWrite(pins[buttonIndex], pin_state);
      
      // Flicker the onboard LED every time a button is pressed
      // digitalWrite(ledPin, HIGH);
      // delay(10);
      // digitalWrite(ledPin, LOW);
      // delay(10);

      // Send response back to Python
      Serial.print("Pin ");
      Serial.print(pins[buttonIndex]);
      Serial.print(" set to ");
      Serial.println(pin_state);
    }
  }
}