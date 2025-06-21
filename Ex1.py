import cv2
import numpy as np

img = cv2.imread("picture.jpg")
cv2.imshow("window",img)
cv2.waitKey(0)

print("Image shape:", img.shape)
