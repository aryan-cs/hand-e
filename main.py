import cv2
import math
import mediapipe as mp
import keyboard
import time

# Highlighted landmarks
highlight_color = (255, 255, 255)
highlight_thickness = 3

# Hand and pose detection flags
hand_detection = True
pose_detection = False

# Mediapipe hand landmark model
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
mp_holistic = mp.solutions.holistic

# Webcam setup
wCam, hCam = 960, 540  # Increase width and height for larger size
cam = cv2.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)
fps_start_time = 0
fps_display_interval = 5  # Display FPS every 5 seconds

# Variables to track which hands are on the screen
left_hand_on_screen = False
right_hand_on_screen = False

# Mediapipe Hand Landmark Model
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5, max_num_hands=2) as hands, \
        mp_holistic.Holistic(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as holistic:

    while cam.isOpened():
        success, image = cam.read()

        if keyboard.is_pressed('h'):
            hand_detection = not hand_detection
            print(f"Hand detection: {hand_detection}")

        if keyboard.is_pressed('p'):
            pose_detection = not pose_detection
            print(f"Pose detection: {pose_detection}")

        if not success:
            print("Failed to read frame")
            break

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process hands
        hand_results = hands.process(image_rgb)

        # Process holistic
        holistic_results = holistic.process(image_rgb)

        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        # Draw hand landmarks and lines
        if hand_results.multi_hand_landmarks and hand_detection:
            for hand_landmarks in hand_results.multi_hand_landmarks:
                # Draw hand landmarks
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

                # Get landmarks for thumb and index finger
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                # Draw line from thumb tip to index fingertip
                cv2.line(image, (int(thumb_tip.x * wCam), int(thumb_tip.y * hCam)),
                         (int(index_tip.x * wCam), int(index_tip.y * hCam)), highlight_color, highlight_thickness)

                # Calculate distance between thumb tip and index fingertip
                distance_tip = math.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)

                # Get landmarks for index finger base joint and little/pinky finger base joint
                index_base = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
                little_base = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]

                # Draw line from index finger base joint to little/pinky finger base joint
                cv2.line(image, (int(index_base.x * wCam), int(index_base.y * hCam)),
                         (int(little_base.x * wCam), int(little_base.y * hCam)), highlight_color, highlight_thickness)

                # Calculate distance between index finger base joint and little/pinky finger base joint
                distance_base = math.sqrt((index_base.x - little_base.x) ** 2 + (index_base.y - little_base.y) ** 2)

                # Overlay text on the image
                text = f"Index-Little Distance: {distance_base:.2f} | Index-Thumb Distance: {distance_tip:.2f}"

                # Updated text position for old text (top left)
                text_position_top_left = (20, 30)

                # Add black background box with padding and rounded borders underneath the old text
                text_size_top_left = cv2.getTextSize(text, cv2.FONT_HERSHEY_DUPLEX, 0.5, 1)[0]
                box_padding_top_left = 10
                box_top_left_top_left = (text_position_top_left[0] - box_padding_top_left,
                                         text_position_top_left[1] - text_size_top_left[1] - box_padding_top_left)
                box_bottom_right_top_left = (text_position_top_left[0] + text_size_top_left[0] + box_padding_top_left,
                                             text_position_top_left[1] + box_padding_top_left)
                cv2.rectangle(image, box_top_left_top_left, box_bottom_right_top_left, (0, 0, 0), -1, cv2.LINE_AA)
                cv2.rectangle(image, box_top_left_top_left, box_bottom_right_top_left, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(image, text, text_position_top_left, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1,
                            cv2.LINE_AA)

        # Draw pose landmarks
        if holistic_results.pose_landmarks and pose_detection:
            mp_drawing.draw_landmarks(
                image,
                holistic_results.pose_landmarks,
                mp_holistic.POSE_CONNECTIONS,
                mp_drawing_styles.get_default_pose_landmarks_style()
            )

        # Calculate and display FPS
        fps_end_time = time.time()
        fps = 1 / (fps_end_time - fps_start_time)
        fps_start_time = fps_end_time

        # Display the toggle info box in the bottom left corner with the same style
        toggle_info = f"[H] Toggle Hand Detection | [P] Toggle Pose Detection | [SPACE] Exit | FPS: {int(fps)}"
        text_position_bottom_left = (20, hCam - 20)
        cv2.putText(image, toggle_info, text_position_bottom_left, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1,
                    cv2.LINE_AA)

        # Add black background box with padding for the bottom text
        text_size_bottom_left = cv2.getTextSize(toggle_info, cv2.FONT_HERSHEY_DUPLEX, 0.5, 1)[0]
        box_padding_bottom_left = 10
        box_top_left_bottom_left = (text_position_bottom_left[0] - box_padding_bottom_left,
                                    text_position_bottom_left[1] - text_size_bottom_left[1] - box_padding_bottom_left)
        box_bottom_right_bottom_left = (text_position_bottom_left[0] + text_size_bottom_left[0] + box_padding_bottom_left,
                                        text_position_bottom_left[1] + box_padding_bottom_left)
        cv2.rectangle(image, box_top_left_bottom_left, box_bottom_right_bottom_left, (0, 0, 0), -1, cv2.LINE_AA)
        cv2.rectangle(image, box_top_left_bottom_left, box_bottom_right_bottom_left, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image, toggle_info, text_position_bottom_left, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1,
                    cv2.LINE_AA)

        cv2.imshow('handy', image)

        # End video on spacebar press
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break

# Release the webcam and close the OpenCV window
cam.release()
cv2.destroyAllWindows()