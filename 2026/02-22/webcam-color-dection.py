import cv2
import numpy as np

# yellow
lower = np.array([25, 150, 150])
upper = np.array([35, 255, 255])

# read webcam
webcam = cv2.VideoCapture(2)

# read frames
while True:
    ret, frame = webcam.read()

    if not ret:
        break

    blurred_imaged = cv2.GaussianBlur(frame, (5,5), 0)
    hsv_image = cv2.cvtColor(blurred_imaged, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_image, lower, upper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
    for cnt in contours:
        if cv2.contourArea(cnt) > 800:
            x, y, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)

    cv2.imshow("image", frame)
    if cv2.waitKey(40) == ord("q"):
        break



webcam.release()
cv2.destroyAllWindows()