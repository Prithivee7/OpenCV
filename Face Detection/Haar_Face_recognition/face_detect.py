import cv2

img = cv2.imread('rahul_dravid.jpg')
cv2.imshow("Original Image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray scale image', gray)

haar_cascade = cv2.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=7)
print(f'Number offaces in image is {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv2.imshow('Bounding Boxes on Face', img)
cv2.waitKey(0)
