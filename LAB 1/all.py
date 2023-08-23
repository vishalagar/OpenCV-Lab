import cv2 as cv
import numpy as np

#read an image
img = cv.imread('resources/image1.jpg', 1)

#resize the image
cv.resize(img, [0,0], fx=0.5, fy = 0.5)

#rotating the Image
img1 = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

#Pixel value of the image
pix = img[255][255]
print(pix)

blank = np.zeros((500,500,3), dtype="uint8")
cv.rectangle(blank, (10,34), (200,400), (29,234,234))

cv.imshow("Rectangle", blank)
cv.imshow("Image", img1)
cv.waitKey(0)
cv.destroyWindow()