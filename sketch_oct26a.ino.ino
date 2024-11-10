const int segmentPins[] = {2, 3, 4, 5, 6, 7, 8};

// Define which segments light up for each digit
const bool digits[10][7] = {
    {true, true, true, true, true, true, false},   // 0
    {false, true, true, false, false, false, false}, // 1
    {true, true, false, true, true, false, true},  // 2
    {true, true, true, true, false, false, true},  // 3
    {false, true, true, false, false, true, true}, // 4
    {true, false, true, true, false, true, true},  // 5
    {true, false, true, true, true, true, true},   // 6
    {true, true, true, false, false, false, false}, // 7
    {true, true, true, true, true, true, true},    // 8
    {true, true, true, true, false, true, true}    // 9
};

void setup() {
    Serial.begin(9600);
    // Set each segment pin as an output
    for (int i = 0; i < 7; i++) {
        pinMode(segmentPins[i], OUTPUT);
    }
}

void displayDigit(int digit) {
    for (int i = 0; i < 7; i++) {
        digitalWrite(segmentPins[i], digits[digit][i] ? HIGH : LOW);
    }
}

void loop() {
    if (Serial.available() > 0) { // Check if data is available to read
        char character = Serial.read(); // Read the character
        Serial.print("Character received: ");
        Serial.println(character);

        // Check if the character is a digit (0-9)
        if (character >= '0' && character <= '9') {
            int digit = character - '0'; // Convert char to int
            displayDigit(digit); // Display the corresponding digit
        } else {
            Serial.println("Invalid input: Not a digit");
        }
    }
}
