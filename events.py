import cv2
import numpy as np

# The code creates a black image and displays it in a window. The window will close when the 'q' key is pressed.

def draw(event, x, y, flags, param):
  
  if event == 1 :
    cv2.circle(img, center=(x, y), radius=50, color=(0, 0, 255), thickness=-1)  # Draw a red circle on left click
  
cv2.namedWindow(winname = "window")
cv2.setMouseCallback("window", draw)  # Set the mouse callback function to draw circles on left click

img = np.zeros((512,512,3))

while True:
    cv2.imshow("window", img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
