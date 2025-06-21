import cv2
import numpy as np

img = cv2.imread("picture.jpg")
# img[:,:,2] = 0  # Set the blue channel to 0
# img[:,:,1] = 0  # Set the green channel to 0        
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_Resize = cv2.resize(img, (640, 640))
cv2.imshow("window",img_Resize)
cv2.waitKey(0)

# print("Image shape:", img_gray.shape)
