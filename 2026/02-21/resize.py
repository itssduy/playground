import cv2
import os

# read image
img_path = os.path.join("./data/sky.jpg")
image = cv2.imread(img_path)

print(image.shape)

resized_image = cv2.resize(image, (640, 400))
print(resized_image.shape)
# show image
cv2.imshow('image', resized_image)
cv2.waitKey(0)