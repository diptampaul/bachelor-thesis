import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pandas as pd

# from PIL import ImageGrab

def findEncodings(images):
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def recognize():
    path = 'face_recog_attendance/Training_images'
    images = []
    classNames = []
    print('Directories')
    print(os.listdir())
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    return classNames, encodeListKnown
    