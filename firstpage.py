#import module from tkinter for UI
from tkinter import *
from playsound import playsound
import os
from datetime import datetime;
playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/Welcome to automatic face recognition attendance system.mp3')
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("400x400")

def function1():
    playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/creating samples for dataset.mp3')
    os.system("py dataset_capture.py")
    
def function2():
    playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/training data set with your images.mp3')
    os.system("py training_dataset.py")

def function3():
    playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/activating recognition.mp3')
    os.system("py recognizer.py")

def function5():    
    playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/opening developers credit.mp3')    
    os.startfile(os.getcwd()+"/developers/diet1frame1first.html");
   
def function6():
    playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/Thankyou.mp3')
    root.destroy()

def attend():
    playsound('D:/Face-Recognition-Attendance-System-master/Face-Recognition-Attendance-System-PROJECT/attendance/Sound_command/opening attendance sheet.mp3')
    os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')

#stting title for the window   .....#0D47A1
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
l1=Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="#623AA2",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
b1=Button(root,text="Create Dataset Samples",font=("times new roman",20),bg="#EF96C5",fg='black',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
b2=Button(root,text="Train Dataset",font=("times new roman",20),bg="#EF96C5",fg='black',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
b3=Button(root,text="Recognize + Attendance",font=('times new roman',20),bg="#EF96C5",fg="black",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
b4=Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#EF96C5",fg="black",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

b5=Button(root,text="Developers's Credits",font=('times new roman',20),bg="#EF96C5",fg="black",command=function5).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

b6=Button(root,text="Exit",font=('times new roman',20),bg="#623AA2",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
