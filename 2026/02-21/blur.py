import cv2
import os

# read image
img_path = os.path.join("./data/sky.jpg")
image = cv2.imread(img_path)

k_size=15
blurred_image = cv2.blur(image, (k_size, k_size))
gaussian_blur_img = cv2.GaussianBlur(image, (k_size, k_size), 3)

cv2.imshow('image', blurred_image)
cv2.imshow('gaussian blur', gaussian_blur_img)
cv2.waitKey(0)