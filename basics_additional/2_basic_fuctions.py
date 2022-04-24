import cv2
import numpy as np

"""
    In OpenCV instead of using RGB we use BGR
    In convert_colour_to_gray_scale function colour image is converted to a gray scale image
"""


def convert_colour_to_gray_scale(image):
    img = cv2.imread(image)
    imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original Image", img)
    cv2.imshow("Grey Image", imGray)
    cv2.waitKey(0)
    return imGray


"""
    To convert real image to a blurred image Gaussian Blur function is used.
    As parameters kernel size and sigmaX need to be passed.
    kernel size has to be in odd numbers like (1,1), (3,3), (7,7) etc.,
    We can blur both the colour and the gray scale image
"""


def convert_to_blur_image(image):
    img = cv2.imread(image)
    imBlur = cv2.GaussianBlur(img, ksize=(11, 11), sigmaX=0)
    cv2.imshow("Blurred Image", imBlur)
    cv2.waitKey(0)
    return imBlur


def convert_to_canny(image):
    img = cv2.imread(image)
    imCanny = cv2.Canny(img, 150, 200)
    cv2.imshow("Canny Image", imCanny)
    cv2.waitKey(0)
    return imCanny


def convert_to_Dialation(canny_image, kernel):
    imDialated = cv2.dilate(canny_image, kernel, iterations=1)
    cv2.imshow("Dilated Image", imDialated)
    cv2.waitKey(0)
    return imDialated


def convert_to_Eroded(dialated_image, kernel):
    imEroded = cv2.erode(dialated_image, kernel, iterations=1)
    cv2.imshow("Eroded Image", imEroded)
    cv2.waitKey(0)
    return imEroded


img_address = "./Images/house.jpg"
kernel = np.ones((5, 5), np.uint8)

imGray = convert_colour_to_gray_scale(img_address)
imBlur = convert_to_blur_image(img_address)
imCanny = convert_to_canny(img_address)
imDialated = convert_to_Dialation(imCanny, kernel)
imEroded = convert_to_Eroded(imDialated, kernel)
