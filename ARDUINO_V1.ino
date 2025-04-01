const int pins[] = {33,32,31,30,29,28,27,26,25,24,23,22};  // 12 pins
const int inpin[] = {22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33};
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
    
    delay(100);  // Allow time for serial buffer to fill (adjust if needed)
    
    int buttonIndex = Serial.read();  // Read button index (0 to 11)
    Serial.print("Raw input: ");
    Serial.print(buttonIndex);
    if (buttonIndex >= 22 && buttonIndex <= 33) {
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
      Serial.println("Pin ");
      Serial.print(pins[buttonIndex]);
      Serial.print(" set to ");
      Serial.println(pin_state);

      Serial.flush();  // Clear any remaining serial buffer data
    }
  }
}