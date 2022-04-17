import cv2
import numpy as np

img = cv2.imread('images/hyena.jpg')
cv2.imshow('BGR', img)

b, g, r = cv2.split(img)

cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)

# Merge an image
merged = cv2.merge([b, g, r])
cv2.imshow('Merged', merged)

blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])

cv2.imshow('Blue_merged', blue)
cv2.imshow('Green_merged', green)
cv2.imshow('Red_merged', red)

cv2.waitKey(0)
