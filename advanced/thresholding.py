import cv2

img = cv2.imread('images/hyena.jpg')
cv2.imshow('Original Image', img)
print('Shape of BGR image', img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray scale Image', gray)
print("Shape of gray scale image", gray.shape)

# Simple Thresholding
threshold, thresholded_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholded image', thresholded_image)
print("Shape of thresholded image", thresholded_image.shape)

# Thresholding Inverse
threshold, inv_thresholded_image = cv2.threshold(
    gray, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Inverse Thresholded image', inv_thresholded_image)
print("Shape of Inverse thresholded image", inv_thresholded_image.shape)

# Adaptive Thresholding
adaptive_thresh_mean = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)
cv2.imshow('Adaptive Threshold Using Mean', adaptive_thresh_mean)

adaptive_thresh_gaussian = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)
cv2.imshow('Adptive Thresholde Using gaussaian', adaptive_thresh_gaussian)

cv2.waitKey(0)
