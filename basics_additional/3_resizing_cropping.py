import cv2
import numpy as np

"""
    In normal graphs the y axis move from bottom to top but according to OpenCV conventions the 
    y axis goes from top to bottom. 
    Suppose if the shape of the image is (704,1252,3) 
    704 is height and 1252 is the width
"""


def resize_image(image):
    img = cv2.imread(image)
    print("Size of original Image is", img.shape)
    imgResize = cv2.resize(img, (400, 200))
    print("Size of original Image is", imgResize.shape)
    cv2.imshow("Original Image", img)
    cv2.imshow("Resized Image", imgResize)
    cv2.waitKey(0)
    return imgResize


"""
In case of OpenCV it is height followed by the width but in case of matrix it is width followed by height
"""


def cropped_image(image):
    img = cv2.imread(image)
    print("Size of original Image is", img.shape)
    cropped_image = img[:200, :400]
    cv2.imshow("Original Image", img)
    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)
    return cropped_image


img_address = "./Images/house.jpg"
imgResize = resize_image(img_address)
cropped_image = cropped_image(img_address)
