from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2 
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")


        title_lbl = Label(self.root, text="Train Dataset", font=("arial rounded mt bold", 35, "bold"),
                          fg="#CC14E1",
                          bg="#A8FFB7")
        title_lbl.place(x=0, y=0, width=1540, height=50)

        img_top = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\facialrecognition.png")
        img_top=img_top.resize((1530,325))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=60, width=1535, height=325)

        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("Calibri", 36, "bold"), bg="light blue",
                          fg="black")
        b1_1.place(x=500, y=392, width=540, height=60)

        img_bottom = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\facialrecognition.png")
        img_bottom=img_bottom.resize((1530,325))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=450, width=1535, height=345)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # train the classifier and save

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()