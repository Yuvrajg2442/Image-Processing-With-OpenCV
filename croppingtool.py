import cv2
import numpy as np

img1 = cv2.imread("picture.jpg")
img = cv2.resize(img1, (620, 620))  # Resize the image to 620x620   

flag = False
ix = -1
iy = -1

def crop_event(event, x, y, flags, param):

    global ix, iy, flag

    if event == 1:
        flag = True
        ix = x
        iy = y

    elif event == 4:
        fx = x
        fy = y
        
        flag = False
        cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(0, 0, 0), thickness=1)
       
        cropped = img[iy:fy, ix:fx]
        cv2.imshow("Cropped Image", cropped)
        cv2.waitKey(0)
        cv2.imwrite("cropped_image.jpg", cropped)  # Save the cropped image


cv2.namedWindow("window")
cv2.setMouseCallback("window", crop_event)

while True:

    cv2.imshow("window", img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break   

cv2.destroyAllWindows()

