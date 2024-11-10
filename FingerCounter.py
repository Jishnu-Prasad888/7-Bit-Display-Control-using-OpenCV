import cv2
import mediapipe as mp
import serial
import time

# Serial port settings
port = 'COM9'
baud_rate = 9600

# Text settings for overlaying the finger count on the video
org = (50, 50)  # Position of the text
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)  # Red
thickness = 2
lineType = cv2.LINE_AA

# Initialize serial communication with Arduino
ser = serial.Serial(port, baud_rate, timeout=1)
time.sleep(2)  # Give time for the serial connection to establish

def pass_stuff_to_arduino(number_of_fingers):
    """
    Sends the number of fingers detected to the Arduino via serial.
    
    :param number_of_fingers: Integer representing the number of fingers raised
    """
    ser.write(str(number_of_fingers).encode())  # Send the count as a byte-encoded string

def read_video():
    """
    Captures video from the webcam, detects hand landmarks using MediaPipe, 
    counts the number of fingers raised, and displays the result on the video feed.
    It also sends the finger count to the Arduino.
    """
    # Initialize MediaPipe Hands module
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=2)  # Detect up to 2 hands

    # Drawing utilities to visualize hand landmarks
    mp_drawing = mp.solutions.drawing_utils

    # Open video capture
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Exit if video capture fails

        frame = cv2.flip(frame, 1)  # Flip the frame horizontally (mirror effect)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame to RGB (MediaPipe expects RGB)
        results = hands.process(rgb_frame)  # Process the frame to detect hands

        # If hands are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                finger_count = 0
                landmarks = hand_landmarks.landmark

                # Count raised fingers based on the relative positions of landmarks
                if landmarks[4].y < landmarks[3].y:  # Thumb
                    finger_count += 1
                if landmarks[8].y < landmarks[6].y:  # Index
                    finger_count += 1
                if landmarks[12].y < landmarks[10].y:  # Middle
                    finger_count += 1
                if landmarks[16].y < landmarks[14].y:  # Ring
                    finger_count += 1
                if landmarks[20].y < landmarks[18].y:  # Pinky
                    finger_count += 1

                # Send finger count to Arduino
                pass_stuff_to_arduino(finger_count)

                # Display the finger count on the video frame
                cv2.putText(frame, str(finger_count), (10, 30), fontFace, fontScale, (0, 255, 0), thickness, lineType)

        # Show the frame with the overlayed finger count
        cv2.imshow('Finger Counter', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources and close the serial connection
    cap.release()
    cv2.destroyAllWindows()
    ser.close()

# Start the video reading and finger counting process
if __name__ == "__main__":
    read_video()
