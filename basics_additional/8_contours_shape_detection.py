import cv2
import numpy as np

"""
    From Canny we can get the edges
    We can find the area, perimeter, number of corner points of each shape
    With the number of corner points we can approximate the shape.
    3 - Traingle, 4 - Square/ Rectangle, above 4 is a circle
"""


def stackImages(scale, imgArray):
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


"""
    Contours can be explained simply as a curve joining all the continuous points (along the boundary),
    having same color or intensity. The contours are a useful tool for shape analysis and object detection
    and recognition.
    For applying contours we need only binary image(black and white). What we want to detect will be in white
    and the rest will be in black. So for this purpose we apply Canny.
    there are three arguments in cv.findContours() function, first one is source image, 
    second is contour retrieval mode, third is contour approximation

    Contours are the boundaries of a shape with same intensity. It stores the (x,y) coordinates
    of the boundary of a shape. But does it store all the coordinates ? That is specified by this contour
    approximation method.

    If you pass cv.CHAIN_APPROX_NONE, all the boundary points are stored.

    The cv2.boundingRect() function of OpenCV is used to draw an approximate rectangle around the binary image.
    This function is used mainly to highlight the region of interest after obtaining contours from an image.
"""


def getContours(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # print(contours)
    # print(hierarchy)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # Get perimeter
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            # Get the corner points
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            # print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.98 and aspRatio < 1.03:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType = "None"

            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)


path = './Images/shape.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

imgBlank = np.zeros_like(img)
imgStack = stackImages(0.5, ([img, imgBlur],
                             [imgCanny, imgContour]))

cv2.imshow("Stack", imgStack)

cv2.waitKey(0)
