import cv2
import numpy as np

"""
    Warp perspective is used to get a bird's eye view of an image
    It separates a particular image from many images.
    Initially we have to specify the points of the images(boundaries) -> Paint
    Then we sepecify how the images are present normally - (width,height) so that
    the algorithm knows which points are present where 

"""
img_address = "./Images/cards.jpg"
img = cv2.imread(img_address)
width, height = 250, 350
pts1 = np.float32([[197, 33], [374, 73], [140, 288], [326, 300]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Original", img)
cv2.imshow("Warped Image", imgOutput)
cv2.waitKey(0)
