import cv2 as cv
import numpy as np
import os
import glob

CHECKBOARD = (12, 12)

criteria = (cv.TermCriteria_EPS + cv.TERM_CRITERIA_MAX_ITER, 50, 0.0001)

objpoints = []

imgpoints = []

objp = np.zeros((1, CHECKBOARD[0] * CHECKBOARD[1], 3), np.float32)
objp[0, :, :2] = np.mgrid[0:CHECKBOARD[0], 0:CHECKBOARD[1]].T.reshape(-1,2)

prev_img_shape = None

images = glob.glob('./resource/*.tif')

for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ret, corners = cv.findChessboardCorners(gray, CHECKBOARD,
                                            cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_FAST_CHECK
                                            + cv.CALIB_CB_NORMALIZE_IMAGE)

    if ret == True:
        objpoints.append(objp)

        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)

        img = cv.drawChessboardCorners(img, CHECKBOARD, corners2, ret)
    cv.imshow("img", img)
    cv.waitKey(0)