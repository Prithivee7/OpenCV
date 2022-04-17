import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/hyena.jpg')
cv2.imshow('Original image', img)


def histogram_colour_for_image():
    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()
    cv2.waitKey(0)


def histogram_colour_for_masked_part():
    blank = np.zeros(img.shape[:2], dtype='uint8')
    cv2.imshow("Blank Image", blank)

    mask = cv2.circle(
        blank.copy(), (img.shape[1]//2, img.shape[0]//2), 80, 255, -1)
    cv2.imshow('Mask', mask)

    masked = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('Masked Image', masked)

    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv2.calcHist([img], [i], mask, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()
    cv2.waitKey(0)


histogram_colour_for_image()
histogram_colour_for_masked_part()
