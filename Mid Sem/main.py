import cv2 as cv
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resource/1.jpg')
im_blurred = cv2.GaussianBlur(img, (7,7), 0)
img = cv2.addWeighted(img, 2.0, im_blurred, -1.0, 30)
# Gaussian = cv2.GaussianBlur(img, (7, 7), 0)

IMD = 'IMD436'
# Read the image and perfrom an OTSU threshold
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh =    cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Remove hair with opening
kernel = np.ones((2,2),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# Combine surrounding noise with ROI
kernel = np.ones((6,6),np.uint8)
dilate = cv2.dilate(opening,kernel,iterations=3)

# Blur the image for smoother ROI
blur = cv2.blur(dilate,(15,15))

# Perform another OTSU threshold and search for biggest contour
ret, thresh =     cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
contours, hierarchy =     cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt = max(contours, key=cv2.contourArea)

# Create a new mask for the result image
h, w = img.shape[:2]
mask = np.zeros((h, w), np.uint8)

# Draw the contour on the new mask and perform the bitwise operation
cv2.drawContours(mask, [cnt],-1, 255, -1)
res = cv2.bitwise_and(img, img, mask=mask)
res = cv.resize(res, None, fx = 0.5, fy = .5)
# Display the result
# cv2.imwrite(IMD+'.png', res)

im_blurred = cv2.GaussianBlur(res, (7,7), 0)
im1 = cv2.addWeighted(res, 2.0, im_blurred, -1.0, -30)

# ret, thresh3 = cv.threshold(res, 100, 255, cv.THRESH_TOZERO)
cv.imshow("sharp", im1)



#Image segmentation


kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations = 25)
bg = cv2.dilate(closing, kernel, iterations = 3)
dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
ret, fg = cv2.threshold(dist_transform, 0.02*dist_transform.max(), 255, 0)


# cv.imshow("Segmented", fg)

plt.plot()
plt.imshow(fg )
plt.axis('off')
plt.title("Segmented Image")
plt.show()

# ret, thresh = cv2.threshold(res, 0, 255,cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)
# plt.figure(figsize=(8,8))
# plt.imshow(thresh)
# plt.axis('off')
# plt.title("Threshold Image")
# plt.show()

# cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

