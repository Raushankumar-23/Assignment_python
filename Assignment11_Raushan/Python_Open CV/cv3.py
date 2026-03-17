#Flipping an image

import cv2

img = cv2.imread("C:\\Users\\Raushan Kumar\\OneDrive\\Pictures\\img_2.png")

width = 400
height = 850
dim = (width, height)

resized = cv2.resize(img, dim)

cv2.imshow("Original ",resized)
print("Size in bytes",img.size)

# flip = cv2.flip(resized,1)
# cv2.imshow("Horizontal ",flip)

# flip1 = cv2.flip(resized,0)
# cv2.imshow("Vertical ",flip1)

# flip2 = cv2.flip(resized,-1)
# cv2.imshow("Vertical ",flip2)


cv2.waitKey(0)
cv2.destroyAllWindows()