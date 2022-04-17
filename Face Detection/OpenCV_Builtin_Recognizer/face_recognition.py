import numpy as np
import cv2
import os

haar_cascade = cv2.CascadeClassifier('haar_face.xml')

# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

folders = [folder for folder in os.listdir('images')]

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_recognizer_model.yml')

img = cv2.imread('sachin.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image',gray)

faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces_rect:
    face_region_of_interest = gray[y:y+h,x:x+w]
    label,confidence = face_recognizer.predict(face_region_of_interest)

    print(f'Label = {folders[label]} with a confidence of {confidence}')

    cv2.putText(img,str(folders[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv2.imshow('Recognised Image',img)
cv2.waitKey(0)