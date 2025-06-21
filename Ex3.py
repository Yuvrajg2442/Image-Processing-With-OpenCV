import cv2
import numpy as np

img = cv2.imread("picture.jpg")
    
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("window",img_gray)
cv2.waitKey(0)

