from cvzone.HandTrackingModule import HandDetector
import cv2
import socket
import time
import serial  # Import the serial library

wCam, hCam = [340, 180]
cam = cv2.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)
success, image = cam.read()
h, w, _ = image.shape
detector = HandDetector(detectionCon=0.8, maxHands=2)
fps_start_time = 0

# Open serial port for communication with Arduino
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to the port where your Arduino is connected

def fps():
    global fps_start_time
    fps_end_time = time.time()
    fps = 1 / (fps_end_time - fps_start_time)
    fps_start_time = fps_end_time
    return fps

def tooltip(text):
    # Your tooltip code remains the same

while True:
    success, image = cam.read()
    image = cv2.flip(image, 1)
    hands, image = detector.findHands(image)

    tooltip(f"[SPACE] Exit | FPS: {int(fps())}")

    data = []

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        for lm in lmList:
            data.extend([lm[0], h - lm[1], lm[2]])

        # Convert the data list to a string and send it to the Arduino
        data_str = ','.join(map(str, data))
        ser.write(data_str.encode())

    cv2.imshow("localhost:" + str(PORT), image)
    if cv2.waitKey(1) & 0xFF == ord(' '): 
        ser.close()  # Close the serial port before exiting
        break
