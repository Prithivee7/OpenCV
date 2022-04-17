import cv2

img = cv2.imread('images/lion.jpg')
print('Shape of the image',img.shape)
print('Type of the image',type(img))

cv2.imshow('Lion',img)
cv2.waitKey(0)