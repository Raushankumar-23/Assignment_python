import cv2

img = cv2.imread("C:\\Users\\Raushan Kumar\\OneDrive\\Pictures\\img_2.png", 1)

print("Dimension of the image:", img.shape)

width = 400
height = 400
dim = (width, height)

resized = cv2.resize(img, dim)

cv2.imshow("window", resized)   # display resized image

cv2.imwrite('car.jpg', resized) # save resized image

cv2.waitKey(0)

cv2.destroyAllWindows()