# Edge Detection
# 1 Noise reduction
# 2 Intensive of the gradient of the image
# 3 Non-maximum suppression
# 4 Thresholding



import cv2

img = cv2.imread("C:\\Users\\Raushan Kumar\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-03-17 014957.png")

resize = cv2.resize(img,(520,520))


min_thresh = 100 # below 100 con to black
max_thresh = 100

edges = cv2.Canny(resize,min_thresh,max_thresh)

cv2.imshow("Original",resize)
cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()