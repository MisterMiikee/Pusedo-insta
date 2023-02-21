import cv2 as cv
import numpy as np

img = cv.imread('Photos/odst_classic.jpg')
cv.imshow("ODST", img)

# Same size canvas as odst_classic
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)


grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# cv.imshow("Grey ODST", grey)

blurr = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blurr", blurr)

# canny = cv.Canny(blurr, 125, 175)
# cv.imshow("Canny ODST", canny)

ret, thresh = cv.threshold(grey, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)


contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found! ')


cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)



cv.waitKey(0)
