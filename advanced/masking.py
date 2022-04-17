import cv2
import numpy as np

img = cv2.imread('images/hyena.jpg')
cv2.imshow('Original Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Blank Image", blank)

mask = cv2.circle(
    blank.copy(), (img.shape[1]//2, img.shape[0]//2), 80, 255, -1)
cv2.imshow('mask', mask)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('Masked Image', masked)

# Get wierd shape and apply it as a mask

circle = cv2.circle(
    blank.copy(), (img.shape[1]//2+40, img.shape[0]//2), 70, 255, -1)

rectangle = cv2.rectangle(blank.copy(), (30, 30), (180, 180), 255, -1)

wierd_shape = cv2.bitwise_and(circle, rectangle)
cv2.imshow('Wierd Shape', wierd_shape)

wierd_shape_mask = cv2.bitwise_and(img, img, mask=wierd_shape)
cv2.imshow('Wierd Shaped Mask Picture', wierd_shape_mask)

cv2.waitKey(0)
