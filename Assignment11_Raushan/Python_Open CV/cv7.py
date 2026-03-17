
#  Image Rotation
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Raushan Kumar\\OneDrive\\Pictures\\img_2.png",cv2.IMREAD_COLOR)

column = img.shape[1]
row = img.shape[0]

center = (column/2,row)
angle = 90

r = cv2.getRotationMatrix2D(center,angle,1)

rotate = cv2.warpAffine(img,r,(column,row))

cv2.imshow("Rotated ",rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()

