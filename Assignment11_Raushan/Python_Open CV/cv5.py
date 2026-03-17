import cv2
import numpy as np

#img = cv2.imread("C:\\Users\\Raushan Kumar\\OneDrive\\Pictures\\img_2.png",cv2.IMREAD_COLOR)

img = np.zeros(shape = [600,800,3],dtype='uint8')
img.fill(255)

cv2.line(img,(0,0),(15,150),(255,0,0),2)
cv2.rectangle(img,(200,150),(250,300),(255,0),3)
cv2.circle(img,(300,75),70,(255,0,255),3)

pts_poygon = np.array([[100,50],[100,300],[588,58],[500,388]], np.int32)
cv2.polylines(img,[pts_poygon],True,(0,255,255),3)


font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,'HELLO',(10,500),font, 3,(288,255,255),8,cv2.LINE_AA)

cv2.imshow('Image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
