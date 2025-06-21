import cv2
import numpy as np

img = cv2.imread("picture.jpg")
img_Resize = cv2.resize(img, (640, 640))
cv2.imshow("window",img_Resize)
cv2.waitKey(0)
