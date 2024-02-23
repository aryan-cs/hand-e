import cv2
import math
import tkinter as tk
from tkinter import *
import mediapipe as mp
from PIL import Image, ImageTk
import threading
from tkinter import filedialog

# Highlighted landmarks
highlight_color = (255, 255, 255)
highlight_radius = 25
highlight_thickness = 3

# Mediapipe hand landmark model
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
mp_holistic = mp.solutions.holistic

# Webcam setup
wCam, hCam = 640, 480
cam = cv2.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)

# Variables to track which hands are on the screen
left_hand_on_screen = False
right_hand_on_screen = False

# Mediapipe Hand Landmark Model
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5, max_num_hands=2) as hands, \
     mp_holistic.Holistic(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as holistic:
    
    # Function to calculate and display angle between thumb and index finger
    def thumb_index_angle(hand_landmarks):
                # Calculate angle between thumb and index finger
                thumb_tip = hand_landmarks.landmark[4]
                index_tip = hand_landmarks.landmark[8]

                x1, y1 = int(thumb_tip.x * wCam), int(thumb_tip.y * hCam)
                x2, y2 = int(index_tip.x * wCam), int(index_tip.y * hCam)

                angle_rad = math.atan2(y2 - y1, x2 - x1)
                angle_deg = math.degrees(angle_rad)

                # Adjust angle to range from 0 to 90
                adjusted_angle = min(abs(angle_deg), 90 - abs(angle_deg))

                # Display the adjusted angle based on hand position
                if hand_landmarks.landmark[0].x > hand_landmarks.landmark[17].x:
                    left_hand_on_screen = True
                    right_hand_on_screen = False
                    cv2.putText(image, f'Angle (Left Hand): {adjusted_angle:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (255, 0, 0), 2, cv2.LINE_AA)
                else:
                    right_hand_on_screen = True
                    left_hand_on_screen = False
                    cv2.putText(image, f'Angle (Right Hand): {adjusted_angle:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (255, 0, 0), 2, cv2.LINE_AA)

    # Live video stream
    while cam.isOpened():
        success, image = cam.read()

        image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process hands
        hand_results = hands.process(image)

        # Process holistic
        holistic_results = holistic.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw hand landmarks
        if hand_results.multi_hand_landmarks:
            for hand_landmarks in hand_results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

            # thumb_index_angle(hand_landmarks)

        # Draw pose landmarks
        if holistic_results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image,
                holistic_results.pose_landmarks,
                mp_holistic.POSE_CONNECTIONS,
                mp_drawing_styles.get_default_pose_landmarks_style()
            )

        # Reset hand tracking variables if no hands are detected
        if not hand_results.multi_hand_landmarks:
            left_hand_on_screen = False
            right_hand_on_screen = False

        cv2.imshow('handy', image)

        # End video on spacebar press
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break

cam.release()
cv2.destroyAllWindows()