import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/hyena.jpg')
cv2.imshow('Original Image', img)

kernel_size_3 = np.array([(1, 1, 1), (1, 1, 1), (1, 1, 1)])*(1/9)
kernel_size_5 = np.array(
    [(1, 1, 1, 1, 1), (1, 1, 1, 1, 1), (1, 1, 1, 1, 1), (1, 1, 1, 1, 1), (1, 1, 1, 1, 1)])*(1/25)

img_shape = img.shape
kernel_shape = kernel_size_5.shape

# To find the number of rows and columns to be added.
#  If the size of the kernel is (3,3) we add one row and one column
# If the size of the kernel is (5,5) we add 2 rows ad 2 columns

top = bottom = int((kernel_shape[0]-1)/2)
left = right = int((kernel_shape[1]-1)/2)

# Padding can be considered as adding borders
# Method 1 - Adding zeros in border
padded_image_with_zero = cv2.copyMakeBorder(
    img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255, 255, 255])
cv2.imshow('Padded Image With Zero', padded_image_with_zero)

# Method 2 - Adding the boundary pixels as borders.
padded_image_reflect = cv2.copyMakeBorder(
    img, top, bottom, left, right, cv2.BORDER_REFLECT)
cv2.imshow('Padded Image with reflection', padded_image_reflect)

# We can compare the shape of the padded image and the original image
print(f'Shape of original image {img.shape}')
print(
    f'Shape of padded Image with border as zero {padded_image_with_zero.shape}')
print(f'Shape of padded Image with reflection {padded_image_reflect.shape}')
cv2.waitKey(0)
