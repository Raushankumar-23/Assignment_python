# Gaussian blur

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Raushan Kumar\\OneDrive\\Pictures\\img_2.png", cv2.IMREAD_COLOR)

resize = cv2.resize(img,(640,640))

ksize = (7,7)
sigmax = 0
sigmay = 0

blur = cv2.GaussianBlur(resize,ksize,sigmax)

cv2.imshow("Input ", resize)
cv2.imshow("Output", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()