import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Open the default camera

while True:

    ret, frame = cap.read()  # Read a frame from the camera

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale



    cv2.imshow("Camera Feed", img_gray)  # Display the frame

    print(ret)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break   

cv2.destroyAllWindows()

