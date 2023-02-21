import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos/reach_halo.jpg")
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

cv.imshow("ODST", gray)
blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank, (img.shape[1]//2 + 300, img.shape[0]//2 - 200), 150, 255, -1)

# # Passed in the color image
# masked = cv.bitwise_and(img, img, mask=circle)
# cv.imshow('Masked1', masked)

# Passed in the greyscale image
masked = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Masked', masked)

# Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
gray_masked_hist = cv.calcHist([gray], [0], masked, [256], [0, 256])


# Building a Graph
# plt.figure('Plot')
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()
#
# Greyscale Masked
# plt.figure('Masked Plot')
# plt.title('Grayscale Masked Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_masked_hist)
# plt.xlim([0, 256])
# plt.show()

# Colored Histogram change {None} to {masked} to just get the masked portions
plt.figure('Plot')
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()



cv.waitKey(0)