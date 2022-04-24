import cv2
import numpy as np

"""
In case of OpenCV it is height followed by the width but in case of matrix it is width followed by height
"""
img = np.zeros((500, 800, 3), np.uint8)
img[:] = 255, 0, 0
# Building a line
# First parameter contains the image, the second and third parameter consists of starting and end points
# Fourth parameter consists of the colour and last parameter consists of thickness
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# Building a rectangle
# Method1 - manipulating numpy array
# img[:] gives all the rows and all the columns(full image). If we want to have specfic portions
# then we can specify img[200:300,300:600] and set the colour

img[:100, 300:600] = 0, 120, 0
img[200:300, 300:600] = 255, 255, 0

# Method2 - making use of cv builtin function
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.rectangle(img, (300, 300), (400, 450), (0, 0, 255), cv2.FILLED)

# Second parameter - midpoint, third parameter = radius, last parameter = thickness
cv2.circle(img, (400, 50), 30, (255, 0, 255), 5)

# second parameter - text, third parameter - starting point, fourth parameter - font type
# fifth parameter - font size, last parameter - thickness
cv2.putText(img, "OPENCV", (300, 300),
            cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 200), 3)

cv2.imshow("Draw", img)
cv2.waitKey()
