from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2 
import os
import numpy as np
import csv

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")

        # variables

        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendannce=StringVar()

        img = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\aat.jpg")
        #img=img.resize((1540,170))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=516, height=200)

        img1 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\oh.jpg")
        #img=img.resize((1540,170))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=516, y=0, width=516, height=200)

        img2 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\ju.jpg")
        #img=img.resize((1540,170))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1032, y=0, width=538, height=200)

    

# background image

        img3 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\bh.jpg")
        img3=img3.resize((1540,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1540, height=710)

        title_lbl = Label(bg_img, text=" ATTENDANCE  SYSTEM", font=("Calibri", 35, "bold"), bg="light yellow",
                          fg="dark blue")
        title_lbl.place(x=0, y=0, width=1540, height=55)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=12, y=63, width=1510, height=520)

        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="STUDENT ATTENDANCE DETAILS",
                                font=("calibri", 15, "bold"))
        Left_frame.place(x=10, y=8, width=730, height=500)

        img_left = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\facialrecognition.png")
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=700, height=80)

        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE)
        left_inside_frame.place(x=4, y=145, width=718, height=320)

        # labels and entry

        # attendance id

        attendance_id_label = Label(left_inside_frame, text="AttendanceID:",
                                 font=("Calibri", 12, "bold"))
        attendance_id_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_id ,
                                    font=("Calibri", 12))
        attendanceID_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # roll

        rollLabel = Label(left_inside_frame, text="Roll:",
                                 font=("Calibri", 12,"bold"))
        rollLabel.grid(row=1, column=2, padx=4, pady=8)

        atten_roll = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_roll ,
                                    font=("Calibri", 12))
        atten_roll.grid(row=1, column=3, pady=8)

        # name

        nameLabel = Label(left_inside_frame, text="Name:",
                                 font=("Calibri", 12,"bold"))
        nameLabel.grid(row=2, column=0)

        atten_name = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_name ,
                                    font=("Calibri", 12))
        atten_name.grid(row=2, column=1, pady=8)

        # dept

        depLabel = Label(left_inside_frame, text="Department:",
                                 font=("Calibri", 12,"bold"))
        depLabel.grid(row=2, column=2)

        atten_dep = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_dep ,
                                    font=("Calibri", 12))
        atten_dep.grid(row=2, column=3,pady=8)

        # time

        timeLabel = Label(left_inside_frame, text="Time:",
                                 font=("Calibri", 12,"bold"))
        timeLabel.grid(row=3, column=0)

        atten_time = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_time ,
                                    font=("Calibri", 12))
        atten_time.grid(row=3, column=1, pady=8)

        # date

        dateLabel = Label(left_inside_frame, text="Date:",
                                 font=("Calibri", 12,"bold"))
        dateLabel.grid(row=3, column=2)

        atten_date = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_date,
                                    font=("Calibri", 12))
        atten_date.grid(row=3, column=3, pady=8)

        # attendance

        attendanceLabel = Label(left_inside_frame, text="Attendance Status:",
                                 font=("Calibri", 12,"bold"))
        attendanceLabel.grid(row=4, column=0)

        self.atten_status= ttk.Combobox(left_inside_frame, font=("Calibri", 12),textvariable=self.var_attend_attendannce ,
                                 state="readonly", width=18)
        self.atten_status["values"] = ("Status", "Present", "Absent")
        
        self.atten_status.grid(row=4, column=1,pady=8)
        self.atten_status.current(0)

        # button frame

        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=265, width=692, height=35)

        save_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=26, font=("Calibri", 12, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        up_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=26, font=("Calibri", 12, "bold"),
                        bg="blue", fg="white")
        up_btn.grid(row=0, column=1)

        
        re_btn = Button(btn_frame, text="Reset", command=self.reset_data,  width=31, font=("Calibri", 12, "bold"),
                        bg="blue", fg="white")
        re_btn.grid(row=0, column=2)

        # right  frame

        Right_frame = LabelFrame(main_frame, bd=2,relief=RIDGE,
                                 text="ATTENDANCE",
                                 font=("calibri", 15, "bold"))
        Right_frame.place(x=750, y=8, width=745, height=500)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=730, height=455)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # fetch  data

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    # import csv
    def importCsv(self):
        global mydata
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export csv

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found to export", parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_attend_id.set(row[0])
        self.var_attend_roll.set(row[1])
        self.var_attend_name.set(row[2])
        self.var_attend_dep.set(row[3])
        self.var_attend_time.set(row[4])
        self.var_attend_date.set(row[5])
        self.var_attend_attendannce.set(row[6])

    def reset_data(self):

        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendannce.set("")





if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()