import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/hyena.jpg')
cv2.imshow('Original image', img)


def histogram_full_image():

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray scale image', gray)

    # Since this is a gray scale image we provide 0 for the channel
    # In this case we are calculating the pixel intensity for the whole image
    gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    plt.figure()
    plt.title('Grayscale Histogram')
    plt.xlabel('bins')
    plt.ylabel('# of pixels')
    plt.plot(gray_hist)
    plt.xlim([0, 256])
    plt.show()

    cv2.waitKey(0)


def histogram_for_masked_part_of_image():

    blank = np.zeros(img.shape[:2], dtype='uint8')
    cv2.imshow("Blank Image", blank)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray scale image', gray)

    mask = cv2.circle(
        blank.copy(), (gray.shape[1]//2, gray.shape[0]//2), 80, 255, -1)
    cv2.imshow('mask', mask)

    masked = cv2.bitwise_and(gray, gray, mask=mask)
    cv2.imshow('Masked Image', masked)

    gray_hist = cv2.calcHist([gray], [0], mask, [256], [0, 256])

    plt.figure()
    plt.title('Grayscale Histogram for masked part')
    plt.xlabel('bins')
    plt.ylabel('# of pixels')
    plt.plot(gray_hist)
    plt.xlim([0, 256])
    plt.show()

    cv2.waitKey(0)


histogram_full_image()
histogram_for_masked_part_of_image()
