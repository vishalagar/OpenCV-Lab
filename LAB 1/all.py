import cv2
import cv2 as cv

img = cv.imread('resources/image1.jpg', 1)

cv.resize(img, [0,0], fx=0.5, fy = 0.5)
img1 = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

cv.imshow("Image", img1)

cv.waitKey(0)
cv.destroyWindow()