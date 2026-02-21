import cv2
import os 

image_path = os.path.join("./data/morioh-sky.jpg")

img = cv2.imread(image_path)

cv2.imwrite(os.path.join("./data/sky.jpg"), img)
print(img.shape)

cv2.imshow('image', img)
cv2.waitKey(0)