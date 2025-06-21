import cv2
import numpy as np

img = cv2.imread("picture.jpg")
# img[:,:,2] = 0  # Set the blue channel to 0
# img[:,:,1] = 0  # Set the green channel to 0        
img[:,:,0] = 0  # Set the red channel to 0        

cv2.imshow("window",img)
cv2.waitKey(0)


