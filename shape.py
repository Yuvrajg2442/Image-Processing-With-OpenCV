import cv2
import numpy as np

img = np.zeros((512,512,3))  # Create a black image

cv2.rectangle(img, pt1=(100, 100), pt2=(400, 400), color= (255, 0, 0), thickness= -1)  # Draw a blue rectangle
cv2.line(img, pt1=(0, 0), pt2=(512, 512), color= (0, 255, 0), thickness= 2)  # Draw a green line
cv2.circle(img, center=(256, 256), radius=50, color=(0, 0, 255), thickness=-1)  # Draw a red circle
cv2.putText(img, text="OpenCV", org=(200, 500), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(255, 255, 255), thickness=3)  # Add white text
cv2.imshow("window",img)
cv2.waitKey(0)