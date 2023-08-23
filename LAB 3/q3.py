import cv2
import numpy 

img = cv2.imread('resource/img1.jpg', 0)

# cv2.imshow("Model", img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img_b_blur_3 = cv2.boxFilter(img, -1, (3, 3))

dst = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)

cv2.imshow('image Gaussian, Box', numpy.hstack((img, dst, img_b_blur_3)))

# cv2.imshow("Blur", img_b_blur_3)
# cv2.imshow("Model ", img)

cv2.waitKey(0)
cv2.destroyAllWindows()