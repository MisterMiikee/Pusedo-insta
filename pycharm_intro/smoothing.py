import cv2 as cv


img = cv.imread("Photos/odst_look.jpg")
cv.imshow("ODST", img)

# Averaging

average = cv.blur(img, (5, 5))
cv.imshow("AVE Blur", average)

gaussian = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow("Gas Blur", gaussian)

# Reduces some edges
median = cv.medianBlur(img, 3)
cv.imshow("Median", median)


# Bilateral Blur but retains the edges
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)