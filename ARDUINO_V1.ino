const int pins[] = {33,32,31,30,29,28,27,26,25,24,23,22};  // 12 pins
const int inpin[] = {22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33};

const int pinCount = 12;
bool pinStates[12] = {false};  // Track pin states
int in_vals[12] = {false};
const int ledPin = LED_BUILTIN;  // Onboard LED pin (usually pin 13)

void setup() {
  Serial.begin(9600);  // Initialize serial communication at 9600 baud
  pinMode(ledPin, OUTPUT);  // Set onboard LED as output
  for (int i = 0; i < 12; i++) {
    pinMode(pins[i], OUTPUT);
    digitalWrite(pins[i], LOW);
  }

  for (int i = 0; i < 12; i++) {
    pinMode(inpin[i], INPUT);
  }

}

void loop() {
  if (Serial.available()) {
    String received = Serial.readStringUntil('\n'); // Read incoming data
    received.trim(); // Remove extra spaces or newlines

    if (received == "READ") {  
      // Send input pin states as "1,0,1,0"
      for (int i = 0; i < inputPinCount; i++) {
          Serial.print(digitalRead(inputPins[i]));
          if (i < inputPinCount - 1) Serial.print(",");
      }
      Serial.println();  // End response
      return;  // Exit loop to avoid processing further
    }
    else{

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
    }

  }

  // bool temp = false;
  // for (int i = 0; i < 12; i++) {
  //   in_vals[i] = digitalRead(pin);
  // }

  // // Send array as a comma-separated string
  // for (int i = 0; i < numPins; i++) {
  //   Serial.print(pinStates[i]);
  //   if (i < numPins - 1) {
  //       Serial.print(",");  // Add comma between values
  //   }
  // }
}