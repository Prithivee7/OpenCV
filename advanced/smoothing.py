import cv2

img = cv2.imread('images/tiger.jpg')
cv2.imshow('Original Image', img)

# average blur
blur = cv2.blur(img, (3, 3))
cv2.imshow('Blurred Image', blur)

# gaussian blur
# The third argument is the standard deviation along x axis.
gauss = cv2.GaussianBlur(img, (3, 3), 0)
cv2.imshow('Gaussian Image', gauss)

# median blur
# The second parameter is the kernel. It is the same as (3,3)
median = cv2.medianBlur(img, 3)
cv2.imshow('Median Blur', median)

# Bilateral blurring
# the second parameter is the diameter and not the kernel
bilateral = cv2.bilateralFilter(img, 10, 35, 25)
cv2.imshow('Bilateral Blur', bilateral)

cv2.waitKey(0)
