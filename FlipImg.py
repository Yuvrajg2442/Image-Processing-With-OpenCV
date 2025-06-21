import cv2
import numpy as np

img = cv2.imread("picture.jpg")
img_flip = cv2.flip(img, 1)  # Flip the image horizontally
# img_flip = cv2.flip(img, 0)  # Flip the image horizontally
# img_flip = cv2.flip(img, -1)  # Flip the image on both axes

img = cv2.resize(img_flip, (340, 340))  # Resize the flipped image to 640x640   

cv2.imshow("window",img)
cv2.waitKey(0)


