import cv2 as cv

img = cv.imread("Photos/colorful_field.jpg")
# cv.imshow("Reach", img)

grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("FIELD_Grey", grey)

# Simple Thresholding/ Inverse Thresholding
threshold, thresh = cv.threshold(grey, 100, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)

threshold, thresh_inv = cv.threshold(grey, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow("Threshold_Inv", thresh_inv)


# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 10)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 10)
cv.imshow('Adaptive Gaussian Thresholding', adaptive_thresh)


cv.waitKey(0)