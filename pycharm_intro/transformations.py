import cv2 as cv
import numpy as np

img = cv.imread('Photos/silk_choc.png')
cv.imshow('Silk', img)


# Translation

def translate(img, x, y):
    transMate = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMate, dimensions)


translated = translate(img, 100, 100)
cv.imshow("Translated", translated)


# Roatation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)


# Flip Image   0 == x-axis  1 == y-axis -1 == both
flip = cv.flip(img, 1)
cv.imshow("Flip", flip)


cv.waitKey(0)
