from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("arial rounded mt bold", 35, "bold"),
                          fg="#CC14E1",
                          bg="#A8FFB7")
        title_lbl.place(x=0, y=0, width=1540, height=50)


        img_top = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\dev.jpg")
        img_top=img_top.resize((1540,740))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=60, width=1540, height=740)

        main_frame = Frame(f_lbl, bd=2)
        main_frame.place(x=1000, y=5, width=510, height=700)

        img_top1 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\me.jpg")
        img_top1=img_top1.resize((200,250))
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=320, y=0, width=215, height=220)

        # developer info

        dev_label = Label(main_frame, text=" Hello , My  name  is  Mainak ", font=("Comic sans MS", 16,"bold"))
        dev_label.place(x=2,y=10)

        dev1_label = Label(main_frame, text="My latest creation, the \nFace Recognition Attendance \nSystem, epitomizes my \ncommitment to efficiency and \ntechnological advancement. \nLet's explore opportunities for \ncollaboration and growth. ", font=("Comic sans MS", 14))
        dev1_label.place(x=20,y=45)

        




if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()