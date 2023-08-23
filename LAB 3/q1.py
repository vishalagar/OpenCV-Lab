import cv2
import matplotlib.pyplot as plt

im = cv2.imread("resource/img1.jpg")
im_blurred = cv2.GaussianBlur(im, (7,7), 0)
im1 = cv2.addWeighted(im, 2.0, im_blurred, -1.0, -30)
# im1 = im +3 * (im - im_blurred) -50


cv2.imshow("Orignal", im)
cv2.imshow("Sharp", im1)
cv2.waitKey(0)

# plt.figure(figsize=(10,10))
# plt.subplot(121),plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB)), plt.axis('off'), plt.title('Original Image', size=10)
# plt.subplot(122),plt.imshow(cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)), plt.axis('off'), plt.title('Sharpened Image', size=10)
# plt.show()