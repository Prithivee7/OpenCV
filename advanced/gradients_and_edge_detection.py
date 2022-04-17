import cv2
import numpy as np

img = cv2.imread('images/stag.jpg')
cv2.imshow('Original Image', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray scale Image', gray)

#  Laplacian edge detection
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
cv2.imshow('Laplacian Image', laplacian)

# Sobel gradient magnitude representation
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

cv2.imshow('Sobel x representation', sobel_x)
cv2.imshow('Sobel y representation', sobel_y)

sobel_img = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('Sobel final image', sobel_img)

# Canny edge detection
canny = cv2.Canny(gray, 150, 175)
cv2.imshow('Canny', canny)

cv2.waitKey(0)
