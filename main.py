from time import strftime
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
import os
from developer import Developer
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from datetime import datetime
from chatbot import ChatBot



class Face:
    def __init__(self, root):

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Header Images

        img = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\fu.jpeg")
        #img=img.resize((1540,170))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=516, height=172)

        img1 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\hp.jpg")
        #img1=img1.resize((1038,172))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=516, y=0, width=516, height=172)

        img2 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\ih.jpg")
        #img2=img2.resize((1038,172))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1032, y=0, width=538, height=172)

    

        # background image

        img3 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\dv.png")
        img3=img3.resize((1540,700))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=170, width=1540, height=700)

        title_lbl = Label(bg_img, text="FACE  RECOGNITION  ATTENDANCE  SYSTEM", font=("Eras Bold ITC", 35, "bold"), bg="#B5FDE4",
                          fg="dark blue")
        title_lbl.place(x=0, y=0, width=1540, height=55)


        def time():
            string=strftime('%H:%M:%S %p')
            lbl1.config(text=string)
            lbl1.after(1000,time)

        lbl1=Label(title_lbl,font=("calibri", 20, "bold"),background="#B5FDE4",foreground="red")
        lbl1.place(x=10,y=0,width=155,height=50)
        time()

        # Student Button

        img4 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\student.png")
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=250, y=100, width=150, height=150)

        b1_1 = Button(bg_img, text="Student Details",  command=self.student_details, cursor="hand2", font=("Calibri", 16, "bold"), bg="light blue",
                          fg="black")
        b1_1.place(x=250, y=230, width=150.5, height=40)

        # Detect Face Button
        img5 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\go.png")
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b2.place(x=550, y=100, width=150, height=150)

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("Calibri", 16, "bold"), bg="light blue",
                      fg="black")
        b2_1.place(x=550, y=230, width=150.5, height=41)

        # Attendance Button

        img6 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\att.png")
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b3.place(x=850, y=100, width=150, height=150)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("Calibri", 16, "bold"), bg="light blue",
                      fg="black")
        b3_1.place(x=850, y=230, width=150.5, height=41)

        # Help Desk Button

        img7 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\chat.jpg")
        img7=img7.resize((200,150))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.chat)
        b4.place(x=1150, y=100, width=150, height=150)

        b4_1 = Button(bg_img, text="ChatBot", cursor="hand2",command=self.chat, font=("Calibri", 16, "bold"), bg="light blue",
                      fg="black")
        b4_1.place(x=1150, y=240, width=150.5, height=41)

        # Train Button

        img8 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\pg.jpg")
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b4 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b4.place(x=250, y=350, width=150, height=150)

        b4_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("Calibri", 16, "bold"), bg="light blue",
                      fg="black")
        b4_1.place(x=250, y=490, width=150.5, height=41)

        # Photo Button

        img9 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\hu.jpg")
        img9=img9.resize((200,180))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b5 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b5.place(x=550, y=350, width=150, height=150)

        b5_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("Calibri", 16, "bold"), bg="light blue",
                      fg="black")
        b5_1.place(x=550, y=490, width=150.5, height=41)

        # Developer Button

        img10 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\de.jpg")
        img10=img10.resize((150,150))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b6 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data)
        b6.place(x=850, y=350, width=150, height=150)

        b6_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=("Calibri", 16, "bold"), bg="light blue",
                      fg="black")
        b6_1.place(x=850, y=490, width=150.5, height=41)

        # Exit Button

        img11 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\exit.jpg")
        img11=img11.resize((150,130))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b7 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b7.place(x=1150, y=350, width=150, height=150)

        b7_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("Calibri", 16, "bold"), bg="light blue",
                      fg="black")
        b7_1.place(x=1150, y=495, width=150.5, height=41)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project", parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


        # function button

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
 
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def chat(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face(root)
    root.mainloop()
