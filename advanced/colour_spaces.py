import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('images/hyena.jpg')
cv2.imshow('Original', img)

plt.imshow(img)
plt.show()

# bgr to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# bgr to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# bgr to LAB
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

cv2.waitKey(0)
