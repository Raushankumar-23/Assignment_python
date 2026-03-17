# Accessing the webcam

import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Frame", frame)

    if cv2.waitKey(10) == ord('z'):
        break

cap.release()
cv2.destroyAllWindows()