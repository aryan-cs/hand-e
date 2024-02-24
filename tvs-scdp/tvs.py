import cv2
import math
import mediapipe as mp
import keyboard
import time

# Highlighted landmarks
highlight_color = (235, 52, 189)
highlight_thickness = 8

# Hand and pose detection flags
hand_detection = True
pose_detection = False

# Mediapipe hand landmark model
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
mp_holistic = mp.solutions.holistic

# Webcam setup
wCam, hCam = 960, 540  # [640, 480], [1280, 720]
cam = cv2.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)
fps_start_time = 0

# Mediapipe Hand Landmark Model
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5, max_num_hands=2) as hands, \
    mp_holistic.Holistic(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as holistic:
    
    def draw_hands():
        mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )
        
    def draw_pose():
        mp_drawing.draw_landmarks(
                image,
                holistic_results.pose_landmarks,
                mp_holistic.POSE_CONNECTIONS,
                mp_drawing_styles.get_default_pose_landmarks_style()
            )
    
    def check_hotkeys():
        if keyboard.is_pressed('h'):
            hand_detection = not hand_detection
            print(f"Hand detection: {hand_detection}")

        if keyboard.is_pressed('p'):
            pose_detection = not pose_detection
            print(f"Pose detection: {pose_detection}")
    
    def index_thumb():
        # Get landmarks for thumb and index finger
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

        # Get depth of the index fingertip and thumb tip
        index_tip_depth = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z
        thumb_tip_depth = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].z

        # Draw line from thumb tip to index fingertip
        cv2.line(image, (int(thumb_tip.x * wCam), int(thumb_tip.y * hCam)),
                        (int(index_tip.x * wCam), int(index_tip.y * hCam)), highlight_color, highlight_thickness)
        
        # Calculate distance between thumb tip and index fingertip based on depth information
        return math.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)
    
    def index_little():
        # Get landmarks for index finger base joint and little/pinky finger base joint
        index_base = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
        little_base = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]

        # Draw line from index finger base joint to little/pinky finger base joint
        cv2.line(image, (int(index_base.x * wCam), int(index_base.y * hCam)),
                        (int(little_base.x * wCam), int(little_base.y * hCam)), highlight_color, highlight_thickness)
        
        # Calculate distance between index finger base joint and little/pinky finger base joint
        return math.sqrt((index_base.x - little_base.x) ** 2 + (index_base.y - little_base.y) ** 2)
    
    def index_distance():
        # Get depth of the index fingertip
        index_tip_depth = hand_results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z

        # Calculate distance to the camera based on depth information
        return abs(1 / index_tip_depth)
    
    def data():
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
        cv2.putText(image, text, text_position_top_left, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    def fps():
        global fps_start_time
        fps_end_time = time.time()
        fps = 1 / (fps_end_time - fps_start_time)
        fps_start_time = fps_end_time
        return fps
    
    def tooltip(text):
        toggle_info = text
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
        cv2.putText(image, toggle_info, text_position_bottom_left, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    while cam.isOpened():

        success, image = cam.read()
        if not success: print("Failed to read frame"); break

        check_hotkeys()

        # Camera & processing
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        hand_results = hands.process(image_rgb)
        holistic_results = holistic.process(image_rgb)
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        # Draw hand landmarks and lines
        if hand_detection and hand_results.multi_hand_landmarks:
            
            for hand_landmarks in hand_results.multi_hand_landmarks:

                draw_hands()

                text = f"Index-Little Distance: {index_little():.2f} | " + \
                       f"Index-Thumb Distance: {index_thumb():.2f} | " + \
                       f"Distance to Camera: {index_distance():.2f}"

                data()

        # Draw pose landmarks
        if pose_detection and holistic_results.pose_landmarks: draw_pose()

        # Display the toggle info box in the bottom left corner with the same style
        tooltip(f"[H] Toggle Hand Detection | [P] Toggle Pose Detection | [SPACE] Exit | FPS: {int(fps())}")

        cv2.imshow('ahnd-e', image)

        # End video on spacebar press
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break

# Release the webcam and close the OpenCV window
cam.release()
cv2.destroyAllWindows()