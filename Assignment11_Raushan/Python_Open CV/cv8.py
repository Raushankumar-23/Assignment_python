# Thresholding

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Raushan Kumar\\OneDrive\\Pictures\\img_2.png", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshold_value = 137

ret, binary_threshold = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", img)
cv2.imshow("Binary Threshold", binary_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()


