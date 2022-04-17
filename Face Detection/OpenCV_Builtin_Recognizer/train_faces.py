import os
from pyexpat import features
import cv2
import numpy as np


def create_training_set():
    folders = [folder for folder in os.listdir('images')]
    haar_cascade = cv2.CascadeClassifier('haar_face.xml')
    features, labels = [],[]

    for folder in folders:
        path = os.path.join('images',folder)
        label = folders.index(folder)
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_array = cv2.imread(img_path)
            gray = cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_region_of_interest = gray[y:y+h,x:x+w]
                features.append(faces_region_of_interest)
                labels.append(label)
    return features,labels

features,labels = create_training_set()
features = np.array(features,dtype=object)
labels = np.array(labels)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)

face_recognizer.save('face_recognizer_model.yml')
np.save('feaures.npy',features)
np.save('labels.npy',labels)