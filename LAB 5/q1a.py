import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt




def harris(img, k,thresh):
    img_copy = np.copy(img)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # img_gau = cv.GaussianBlur(img, (3,3),0)

    dx = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=3)
    dy = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=3)


    x2 = dx*dx
    y2 = dy*dy
    xy = dx*dy

    x2 = cv.GaussianBlur(x2, (3, 3), 2)
    y2 = cv.GaussianBlur(y2, (3, 3), 2)
    xy = cv.GaussianBlur(xy, (3, 3), 2)

    h = (x2*y2 - xy*xy) - k * np.square(x2 +y2)

    cv.normalize(h, h, 0, 1, cv.NORM_MINMAX)

    loc = np.where(h >= thresh)
    for i in zip(*loc[::-1]):
        cv.circle(img_copy, i, 2, (0,0,196), 1)

    return img_copy

img = cv.imread('resource/goku.jpg')
img = cv.resize(img, None, fx = 0.5, fy = 0.5)
# cv.imshow("orignal", img)

hr = harris(img, 0.03, .139)

cv.imshow("Harris", hr)


cv.waitKey(0)