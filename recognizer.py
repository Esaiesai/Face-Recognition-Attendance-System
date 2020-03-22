import cv2, numpy as np
import xlwrite,firebase.firebase_ini as fire
import time
import sys
from playsound import playsound

        
        
start=time.time()
period=8
face_cas = cv2.CascadeClassifier('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/haarcascade_frontalface_default.xml')
# Start capturing video 
vid_cam = cv2.VideoCapture(0)
playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/scanning for Attendance.mp3')
playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/please face the camera before you.mp3')
# Detect object in video stream using Haarcascade Frontal Face
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/trainer/trainer.yml')
flag = 0
id=0

filename='filename'

dict = {
            'item1': 1
}
#font = cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    # Capture video frame
    
    _, image_frame = vid_cam.read()
    
    # Convert frame to grayscale
    
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
    
    # Detect frames of different sizes, list of faces rectangles
    faces = face_cas.detectMultiScale(gray, 1.3, 7)
    
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(image_frame, (x,y), (x+w, y+h), (255,0,0),2)
        id,conf=recognizer.predict(roi_gray)
        if(conf < 50):
          if(id==1):
            id='EsaiSelvam'
            playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/hi esaiselvam.mp3')
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',1,id,'yes')
                dict[str(id)]=str(id);
            playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/your attendance is registered.mp3')    
          elif(id==2):
            id = 'Thasbeeha Thasleem'
            playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/hi Thasbeeha Thasleem.mp3')
            if ((str(id)) not in dict):
                filename =xlwrite.output('attendance', 'class1', 2, id, 'yes')
                dict[str(id)] = str(id);
            playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/your attendance is registered.mp3')
          elif(id==3):
            id = 'Raveen'
            if ((str(id)) not in dict):
                filename =xlwrite.output('attendance', 'class1', 3, id, 'yes')
                dict[str(id)] = str(id);
            playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/your attendance is registered.mp3')
          elif(id==4):
            id = 'Sonu'
            if ((str(id)) not in dict):
                filename =xlwrite.output('attendance', 'class1', 4, id, 'yes')
                dict[str(id)] = str(id);
            playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/your attendance is registered.mp3')
          else:
             id = 'Unknown, can not recognize'
             flag=flag+1
             playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/can not recognize. you are new to attendance system.mp3')
             break
        
        cv2.putText(img,str(id)+" "+str(conf),(x,y-10),font,0.55,(120,255,120),1)
        cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255))
    cv2.imshow('frame',img);
    cv2.imshow('gray',gray);
    if flag == 10:
        playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/transactionBlock.mp3')
        print("Transaction Blocked")
        break;
    if time.time()>start+period:
        break;
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;

cap.release();
cv2.destroyAllWindows();
