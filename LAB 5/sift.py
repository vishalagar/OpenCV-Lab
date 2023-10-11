import numpy as np
import cv2 as cv
img = cv.imread('resource/goku.jpg')

# gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# sift = cv.SIFT_create()
# kp = sift.detect(gray,None)
# img=cv.drawKeypoints(gray,kp,img)

# cv.imshow("SIFT", img)
# cv.waitKey(0)


import cv2
#
# # Loading the image
# img = cv2.imread('geeks.jpg')

# Converting image to grayscale
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Applying SIFT detector
sift = cv2.SIFT_create()
kp = sift.detect(gray, None)

# Marking the keypoint on the image using circles
img=cv2.drawKeypoints(gray ,kp ,img ,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img = cv.resize(img, None, fx = 0.5, fy = 0.5)
cv2.imshow('image-with-keypoints.jpg', img)
cv.waitKey(0)

