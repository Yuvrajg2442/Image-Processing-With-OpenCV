import cv2
import numpy as np

img = cv2.imread("picture.jpg")
img_crop = img[10:1400, 10:1500]  # Crop the image from (10, 10) to (1400, 1500)

img = cv2.resize(img_crop, (620, 620))  # Resize the image to 620x620   
cv2.imshow("window",img)
cv2.waitKey(0)


