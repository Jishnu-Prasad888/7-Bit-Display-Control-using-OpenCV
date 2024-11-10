# Hand Gesture to 7-Segment Display

This project uses a hand gesture recognition system to control a 7-segment display. The system detects the number of fingers held up using a webcam and sends the corresponding number (0-5) to an Arduino via a serial connection. The Arduino then displays this number on a 7-segment display.

## Components

- **Webcam**: For capturing hand gestures.
- **Arduino**: Used to drive the 7-segment display.
- **7-segment display**: Displays the number of fingers recognized by the hand gesture detection system.

### Software Requirements

- **Python 3.x**
    - OpenCV
    - MediaPipe
    - pySerial
- **Arduino IDE**

### Hardware Requirements

- **Arduino Board (e.g., Arduino Uno)**
- **7-segment display** (Common cathode or anode)
- **Jumper wires** for connecting the Arduino to the 7-segment display

## Installation and Setup

### Step 1: Install Python Dependencies

You will need to install the required Python libraries to run the hand gesture detection part of the project. You can install them via `pip`:

```bash
pip install opencv-python mediapipe pyserial 
```

### Step 2: Set Up the Arduino Code

1. Connect the 7-segment display to your Arduino according to the pin configuration in the code.
2. Upload the Arduino code to your Arduino board using the Arduino IDE.

The Arduino code listens for serial data from the Python program and displays the corresponding digit on the 7-segment display. Each segment of the display is controlled by one of the digital pins on the Arduino. When a digit is received over serial, the Arduino lights up the appropriate segments to display that number.

### Step 3: Connect the Webcam

Make sure your webcam is connected and working. The Python code uses OpenCV to capture video from the camera.

### Step 4: Run the Python Code

The Python script will:

1. Capture video from the webcam.
2. Use MediaPipe to recognize hand gestures and count the number of fingers.
3. Send the finger count to the Arduino via a serial connection.
4. Display the finger count on the webcam feed and on the Arduino's 7-segment display.

To run the Python code, simply execute the script:
```bash
python finger_counter.py
```

### Step 5: Interact with the System

- Hold up your hand in front of the webcam, and the system will count the number of fingers.
- The number of fingers will be displayed both in the webcam window and on the 7-segment display connected to the Arduino.
- If you hold up more than 5 fingers, the system will still only count 0-5.
- Press `q` to quit the webcam feed.

## Code Explanation

### Python Code

- **`read_video()`**: Captures video from the webcam using OpenCV and uses MediaPipe to detect hand landmarks. It counts the number of fingers based on the relative position of landmarks for each finger.
- **`pass_stuff_to_arduino(number_of_fingers)`**: Sends the number of fingers detected (as a string) to the Arduino over a serial connection.
- **`cv2.putText()`**: Displays the finger count on the webcam feed in the top-left corner.

### Arduino Code

- **`segmentPins[]`**: Defines the pins connected to the 7-segment display.
- **`digits[10][7]`**: A lookup table that maps each digit (0-9) to the corresponding segments that need to be lit up on the display.
- **`displayDigit(digit)`**: Lights up the correct segments on the 7-segment display based on the digit received.
- **`loop()`**: Continuously checks for serial input, converts it to a digit, and calls `displayDigit()` to show it on the 7-segment display.

## Troubleshooting

- If the webcam feed isn't showing up, ensure that your camera is working properly and not being used by any other application.
- If the Arduino is not displaying the correct digits, check the wiring of the 7-segment display and ensure the serial connection between the Python script and Arduino is working.
- Ensure the correct COM port is specified in the Python script for the serial connection (`COM9` in this case).
