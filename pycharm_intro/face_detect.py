import cv2 as cv
####################################
#
#   D LIBS FACES RECOGNIZERS ARE BETTER
#
########################
img = cv.imread('Photos/group.jpg')
cv.imshow("People", img)

grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("People Grey", grey)

haar_cascade = cv.CascadeClassifier('harr_face.xml')

faces_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5)

print(f'Number of Faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)

cv.imshow('Dectected Faces', img)

cv.waitKey(0)