import cv2 as cv

img = cv.imread('resource/bright.jpg', 1)

print(img.shape)
tag = img[500:1300, 300:1050]

tag = cv.resize(tag, [0,0], fx =0.5,fy = 0.5)

cv.imshow("corpped", tag)
cv.waitKey(0)
cv.destroyWindow()