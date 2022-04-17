import cv2
import numpy as np

img = cv2.imread('images/hyena.jpg')
blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow('Blank', blank)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)

canny = cv2.Canny(blur, 125, 175)
cv2.imshow('Canny', canny)

contours, hierarchies = cv2.findContours(
    canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

print('Number of contours found is', len(contours))
cv2.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv2.imshow('Contours drawn', blank)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

ret, thresh = cv2.threshold(gray, 125, 256, cv2.THRESH_BINARY)
cv2.imshow('Threshold', thresh)

contours, hierarchies = cv2.findContours(
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print('Number of contours found is', len(contours))

# Draw contours in a blank image
# -1 refers to all the contours --> we want all the contours to be displayed.

# cv2.drawContours(blank, contours, -1, (0, 0, 255), 2)
# cv2.imshow('Contours drawn', blank)
cv2.waitKey(0)
