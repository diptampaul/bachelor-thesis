from django.shortcuts import render
from .models import studentDetails, attendanceMark
from .utils import recognize
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pandas as pd

# Create your views here.
def dashboard(request):
    students = studentDetails.objects.all()
    return render(request, 'f_dashboard.htm', {'student_obj': students,})

def attendance(request):
    if request.method == 'POST':
        photo = request.FILES.get('user_photo', False)
        #photo = request.FILES['user_photo']
        upload_obj = attendanceMark(
            uploaded_photo = photo
        )
        upload_obj.save()
        file_path = f'media/{upload_obj.uploaded_photo}'
        
        classNames, encodeListKnown = recognize()
        img = cv2.imread(file_path)
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        try:
            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    print(name)
            student = studentDetails.objects.get(call_name=name)
            student.attendance_count += 1
            student.save()
        except:
            name = None
        students = studentDetails.objects.all()
        return render(request, 'f_dashboard.htm', {'student_obj': students,})
    else:
        return render(request, 'attendance.htm')