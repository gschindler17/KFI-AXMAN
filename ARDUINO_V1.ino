const int pins[] = {33,32,31,30,29,28,27,26,25,24,23,22};  // 12 pins
const int inpin[] = {22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33};
const int pinCount = 12;
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
  if (Serial.available()) {
    String received = Serial.readStringUntil('\n'); // Read incoming data
    received.trim(); // Remove extra spaces or newlines

    int commaIndex = received.indexOf(',');
    if (commaIndex == -1) return; // Invalid format, ignore
    
    int pin = received.substring(0, commaIndex).toInt();
    String state = received.substring(commaIndex + 1);

    // Validate pin and set state
    bool validPin = false;
    for (int i = 0; i < pinCount; i++) {
        if (pins[i] == pin) {
            validPin = true;
            digitalWrite(pin, state == "HIGH" ? HIGH : LOW);
            break;
        }
    }

    // Send response
    if (validPin) {
        Serial.print("Set Pin ");
        Serial.print(pin);
        Serial.print(" to ");
        Serial.println(state);
    } else {
        Serial.println("Invalid pin");
    }
  }
}