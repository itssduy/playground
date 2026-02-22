import os
import cv2

img_path = os.path.join("./data/sky.jpg")
img = cv2.imread(img_path)

print(img.shape)
cropped_img = img[100:400, 0:400]

cv2.imshow('image', cropped_img)
cv2.waitKey(0)