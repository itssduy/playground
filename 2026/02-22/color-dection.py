import cv2
import os
import numpy as np

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([35, 255, 255])

img_path = os.path.join("./data/banana.webp")
image = cv2.imread(img_path)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(image_hsv,lower_yellow, upper_yellow)

contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 1000: #noise filter
        x, y, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(
            image,
            (x,y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )
cv2.imshow("image2", image)
cv2.waitKey(0)

