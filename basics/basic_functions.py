import cv2

img = cv2.imread('images/hyena.jpg')
cv2.imshow('Coloured',img)

# Convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray scale',gray)

# Blurring an image
blur = cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow('Blurred image',blur)

# Edge Cascading or edge detection
canny = cv2.Canny(img,125,175)
cv2.imshow('Canny',canny)

# We can get better result when we provide the blurred image as input to Canny
canny_blur = cv2.Canny(blur,125,175)
cv2.imshow('Canny Blurred',canny_blur)

# Dilating the image
dilate = cv2.dilate(canny_blur,(7,7),iterations=5)
cv2.imshow('Dilated',dilate)

# Eroding the image
erode = cv2.erode(dilate,(7,7),iterations=5)
cv2.imshow('Eroded',erode)

# Resizing the image
resize = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow('Enlarge',resize)

# Cropped the image
crop = img[50:170,10:250]
print(crop.shape)
print(img.shape)
cv2.imshow('Cropped',crop)
cv2.waitKey(0)