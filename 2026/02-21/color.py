import os
import cv2

img_path = os.path.join("./data/sky.jpg")
img = cv2.imread(img_path)

# convert colorspace
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('image', img)
cv2.imshow('rgbimage', img_rgb)
cv2.imshow('grayimage', img_gray)
cv2.imshow('hsvimage', img_hsv)
cv2.waitKey(0)