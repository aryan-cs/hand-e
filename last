from cvzone.HandTrackingModule import HandDetector
import cv2
import socket
import time

wCam, hCam = [1280, 720]
cam = cv2.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)
success, image = cam.read()
h, w, _ = image.shape
detector = HandDetector(detectionCon = 0.8, maxHands = 2)
fps_start_time = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

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

while True:

    success, image = cam.read()
    hands, image = detector.findHands(image)

    tooltip(f"[SPACE] Exit | FPS: {int(fps())}")

    data = []

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        for lm in lmList:
            data.extend([lm[0], h - lm[1], lm[2]])

        sock.sendto(str.encode(str(data)), serverAddressPort)
        
    cv2.imshow("hand-e", image)
    if cv2.waitKey(1) & 0xFF == ord(' '): break;