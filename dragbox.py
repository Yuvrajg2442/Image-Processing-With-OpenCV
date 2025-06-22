import cv2
import numpy as np

# The code creates a black image and allows drawing rectangles with the mouse.
flag = False
ix = -1
iy = -1

def draw(event, x, y, flags, param):
    global ix, iy, flag

    if event == cv2.EVENT_LBUTTONDOWN:
        flag = True
        ix = x
        iy = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if flag:
            temp_img = img.copy()
            cv2.rectangle(temp_img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 0), thickness=-1)
            cv2.imshow("window", temp_img)

    elif event == cv2.EVENT_LBUTTONUP:
        flag = False
        cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 0), thickness=-1)

cv2.namedWindow("window")
cv2.setMouseCallback("window", draw)

img = np.zeros((512, 512, 3), np.uint8)

while True:
    cv2.imshow("window", img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
