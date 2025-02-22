void setup() {
    Serial.begin(115200);  // Match this baud rate with Python
}

void loop() {
    if (Serial.available()) {
        String input = Serial.readStringUntil('\n');
        Serial.println("Arduino received: " + input);
    }
}
