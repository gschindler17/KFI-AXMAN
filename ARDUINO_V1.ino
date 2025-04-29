const int pins[] =  {2,3,4,5,6,7,8,9,10,11,12,13};  // 12 pins
const int inpin[] = {52,50,48,46,44,42,40,38,36,34,32,28};

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
    pinMode(inpin[i], INPUT_PULLUP);
  }

}

void loop() {
  if (Serial.available()) {
    String received = Serial.readStringUntil('\n'); // Read incoming data
    received.trim(); // Remove extra spaces or newlines

    // Serial.print(received);

    if (received == "READ") {  
      // Send input pin states as "1,0,1,0"
      for (int i = 0; i < pinCount; i++) {
          Serial.print(digitalRead(inpin[i]));
          if (i < pinCount - 1) Serial.print(",");
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
              Serial.print(pin);
              Serial.print(state);
              Serial.println();  // End response
              break;
          }
      }
    }

  }


}