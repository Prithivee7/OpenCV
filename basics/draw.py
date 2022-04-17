import cv2
import numpy as np

blank_image = np.zeros((500,500,3),dtype='uint8')
print(f'Shape of blank_image is {blank_image.shape}')

# Set all the pixels to green
blank_image[:] = 0,255,0
x,y = blank_image.shape[1], blank_image.shape[0]

for i in range(0,x,100):
        blank_image[i:i+100,i:i+100] = 0,0,255
        blank_image[i:i+100,x-i-100:x-i] = 0,0,255
cv2.imshow('Colour',blank_image)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Draw a rectangle
blank_image2 = np.zeros((500,500,3),dtype='uint8')
# -1 gives the same result as cv2.FILLED
# cv2.rectangle(blank_image2,(0,0),(40,50),(0,255,255),thickness=2)
# cv2.rectangle(blank_image2,(0,0),(40,50),(0,255,255),thickness=cv2.FILLED)
cv2.rectangle(blank_image2,(0,0),(40,50),(0,255,255),thickness=-1)
cv2.imshow('Rectangle',blank_image2)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Draw a circle
cv2.circle(blank_image2,(blank_image2.shape[1]//2,blank_image2.shape[0]//2),40,(0,0,255),thickness=3)
cv2.imshow('Circle',blank_image2)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Draw a line

cv2.line(blank_image2,(0,0),(300,250),(255,0,255),thickness=5)
cv2.imshow('Line',blank_image2)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Write text on image

cv2.putText(blank_image2,'Hello',(400,400),cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),thickness=3)
cv2.imshow('Text',blank_image2)
cv2.waitKey(0)
