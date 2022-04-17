from configparser import Interpolation
from turtle import left, right, up
import cv2
import numpy as np

img = cv2.imread('images/hyena.jpg')
cv2.imshow('Original Image', img)


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    print(transMat)
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> Down


translated = translate(img, 50, -70)
cv2.imshow('Translated image', translated)


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint == None:
        rotPoint = (width//2, height//2)
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv2.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)
cv2.imshow('Rotated 45', rotated)

rotated = rotate(img, -90)
cv2.imshow('Rotated 90', rotated)

# resizing
resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_LINEAR)
cv2.imshow('Resizing', resized)

# flip
# 0 flips the image vetically -> over x axis
# 1 flips the image horizontally -> over y axis
# -1 flips the image both vertically and horizontally

flip = cv2.flip(img, 0)
cv2.imshow('Flip Vertically', flip)


cv2.waitKey(0)
