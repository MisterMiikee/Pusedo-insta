import cv2 as cv
import numpy as np

img = cv.imread("Photos/spaceship_launch.jpg")
cv.imshow("Reach", img)

grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("Grey Reach", grey)

# Laplacian
lap =cv.Laplacian(grey, cv.CV_64F)
lao = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)


# Sobel
sobelx = cv.Sobel(grey, cv.CV_64F, 1, 0)
sobely = cv.Sobel(grey, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel X", sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow("Combined Sobel", combined_sobel)

canny = cv.Canny(grey, 150, 175)
cv.imshow("Canny", canny)

cv.waitKey(0)