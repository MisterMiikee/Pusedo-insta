import cv2 as cv

img = cv.imread('Photos/odst_look.jpg')
cv.imshow('ODST', img)

# Grey Scale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("Grey ODST", gray)

# Blurr Image
blurr = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blurr", blurr)

# Edge Cascade Detector
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edge", canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

# Eroded
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow("Eroded", eroded)


# Resize

resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resize)

# Cropped
cropped = img[500:1100, 900:1100]
cv.imshow("Cropped", cropped)


cv.waitKey(0)