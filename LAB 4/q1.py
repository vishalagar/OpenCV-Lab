import cv2
import cv2 as cv
import numpy as np

image1 = cv.imread('resource/leg.jpg')
# image1 = cv.resize(image1, [0,0], fx = .5, fy = .5)
img = cv.cvtColor(image1, cv2.COLOR_BGR2GRAY)



ret, thresh1 = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 100, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO_INV)

cv.imshow("orignal", image1)
cv.imshow("Binary", thresh1)
cv.imshow("Binary Inverted", thresh2)
cv.imshow("Truncated", thresh3)
cv.imshow("Set to 0", thresh4)
cv.imshow("Set to 0 Inverted", thresh5)

cv.waitKey(0)
cv2.destroyAllWindows()
