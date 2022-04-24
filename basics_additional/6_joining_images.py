import cv2
import numpy as np


def stack_images_numpy():
    img_Horizontal = np.hstack((img, img))
    img_Vertical = np.vstack((img, img))
    cv2.imshow("Horizontal", img_Horizontal)
    cv2.imshow("Vertical", img_Vertical)
    cv2.waitKey(0)
    return img_Horizontal, img_Vertical


def stack_images(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(
                        imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(
                    imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(
                    imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


img_address = "./Images/cards.jpg"
img_address2 = "./Images/audi.jpg"
img = cv2.imread(img_address)
img2 = cv2.imread(img_address2)
img_Horizontal, img_Vertical = stack_images_numpy()
img_Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
stacked_image = stack_images(0.5, ([img, img_Gray, img], [img, img, img2]))
# stacked_image = stack_images(0.5, ([img], [img2]))
cv2.imshow("Stacked Image", stacked_image)
cv2.waitKey(0)
