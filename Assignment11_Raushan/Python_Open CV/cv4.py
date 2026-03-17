import cv2

img = cv2.imread("C:\\Users\\Raushan Kumar\\OneDrive\\Pictures\\img_2.png")

print("Dimension of Original image",img.shape)

scale = 150

width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)

dim = (width,height)

resized = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print("Dimension of resized image",resized.shape)

cv2.imshow("Resized",resized)
cv2.imshow("Original",img)




cv2.waitKey(0)
cv2.destroyAllWindows()