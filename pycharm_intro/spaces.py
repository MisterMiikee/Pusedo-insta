import cv2 as cv

img = cv.imread('Photos/solo_odst.jfif')
cv.imshow("Solo", img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

cv.imshow("Grey", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(0)
