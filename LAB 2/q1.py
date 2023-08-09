import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resource/bright.jpg', 0)



equ = cv.equalizeHist(img)
res = np.hstack((img,equ))
cv.imwrite('resource/new.jpg',res)

hist, bins = np.histogram(equ.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

res1 = cv.resize(res , [0,0] ,fx = 0.3, fy = 0.3)


cv.imshow("IMAGE", res1 )
cv.waitKey(0)
cv.destroyWindow()