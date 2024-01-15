from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2 


class Student:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # variables

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.va_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone= StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        img = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\facialrecognition.png")
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=550, height=170)

        img1 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\facialrecognition.png")
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=550, height=170)

        img2 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\facialrecognition.png")
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=170)

        # background image

        img3 = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\bgc.png")
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=170, width=1540, height=700)

        title_lbl = Label(bg_img, text="STUDENT  MANAGEMENT  SYSTEM", font=("arial rounded mt bold", 35, "bold"),
                          fg="#CC14E1",
                          bg="#A8FFB7")
        title_lbl.place(x=0, y=0, width=1540, height=50)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=12, y=63, width=1510, height=550)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="light yellow", relief=RAISED, text="STUDENT DETAILS",
                                font=("calibri", 15, "bold"))
        Left_frame.place(x=10, y=8, width=730, height=530)

        img_left = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\facialrecognition.png")
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=700, height=80)

        # current course

        current_course_frame = LabelFrame(Left_frame, bd=3, bg="light yellow", relief=GROOVE,
                                          text="Current Course Information",
                                          font=("calibri", 15, "bold"))
        current_course_frame.place(x=5, y=85, width=710, height=125)

        # department

        dep_label = Label(current_course_frame, text="Department", font=("Calibri", 12, "bold"), bg="light yellow")
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep , font=("Calibri", 12),
                                 state="readonly")
        dep_combo["values"] = (
            "Select Department", "CSE", "IT", "ELECTRONICS", "CIVIL", "MECHANICAL", "PRODUCTION", "ELECTRICAL", "POWER",
            "IEE", "ARCHITECTURE", "CONSTRUCTION", "PHARMACY")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course

        course_label = Label(current_course_frame, text="Course", font=("Calibri", 12, "bold"), bg="light yellow")
        course_label.grid(row=0, column=2, padx=10)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("Calibri", 12),
                                    state="readonly")
        course_combo["values"] = ("Select Course", "SE", "FE", "BE", "B TECH")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year

        year_label = Label(current_course_frame, text="Year", font=("Calibri", 12, "bold"), bg="light yellow")
        year_label.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("Calibri", 12),
                                  state="readonly")
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester

        sem_label = Label(current_course_frame, text="Semester", font=("Calibri", 12, "bold"), bg="light yellow")
        sem_label.grid(row=1, column=2, padx=10)

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("Calibri", 12),
                                 state="readonly")
        sem_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student

        class_student_frame = LabelFrame(Left_frame, bd=3, bg="light yellow", relief=GROOVE,
                                         text="Class Student Information",
                                         font=("calibri", 15, "bold"))
        class_student_frame.place(x=5, y=200, width=710, height=290)

        # student id

        student_id_label = Label(class_student_frame, text="StudentID:",
                                 font=("Calibri", 12, "bold"),
                                 bg="light yellow")
        student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.va_std_id , width=20,
                                    font=("Calibri", 12))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # student name

        student_name_label = Label(class_student_frame, text="Student Name:", font=("Calibri", 12, "bold"),
                                   bg="light yellow")
        student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20,
                                      font=("Calibri", 12))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class division

        div_label = Label(class_student_frame, text="Class Division:", font=("Calibri", 12, "bold"),
                          bg="light yellow")
        div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)


        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("Calibri", 12),
                                 state="readonly", width=18)
        div_combo["values"] = ("A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # roll no

        roll_label = Label(class_student_frame, text="Roll No:", font=("Calibri", 12, "bold"),
                           bg="light yellow")
        roll_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=("Calibri", 12))
        roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # gender

        gen_label = Label(class_student_frame, text="Gender:", font=("Calibri", 12, "bold"),
                          bg="light yellow")
        gen_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)


        gen_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("Calibri", 12),
                                 state="readonly", width=18)
        gen_combo["values"] = ( "Male", "Female", "Other")
        gen_combo.current(0)
        gen_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # dob

        dob_label = Label(class_student_frame, text="DOB:", font=("Calibri", 12, "bold"),
                          bg="light yellow")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("Calibri", 12))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # email

        mail_label = Label(class_student_frame, text="Email:", font=("Calibri", 12, "bold"),
                           bg="light yellow")
        mail_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        mail_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("Calibri", 12))
        mail_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # ph no

        ph_label = Label(class_student_frame, text="Phone No:", font=("Calibri", 12, "bold"),
                         bg="light yellow")
        ph_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        ph_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("Calibri", 12))
        ph_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # address

        add_label = Label(class_student_frame, text="Address:", font=("Calibri", 12, "bold"),
                          bg="light yellow")
        add_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        add_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("Calibri", 12))
        add_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # teacher

        te_label = Label(class_student_frame, text="Teacher Name:", font=("Calibri", 12, "bold"),
                         bg="light yellow")
        te_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        te_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("Calibri", 12))
        te_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample",
                                    value="Yes")
        radiobtn1.grid(row=6, column=0)

        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample",
                                    value="No")
        radiobtn2.grid(row=6, column=1)

        # button frame

        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=220, width=701, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=10, font=("Calibri", 12, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        up_btn = Button(btn_frame, text="Update", command=self.update_data, width=10, font=("Calibri", 12, "bold"),
                        bg="blue", fg="white")
        up_btn.grid(row=0, column=1)

        del_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=10, font=("Calibri", 12, "bold"),
                         bg="blue", fg="white")
        del_btn.grid(row=0, column=2)

        re_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=10, font=("Calibri", 12, "bold"),
                        bg="blue", fg="white")
        re_btn.grid(row=0, column=3)

        take_btn = Button(btn_frame, text="Take A Photo", command=self.generate_dataset, width=20, font=("Calibri", 12, "bold"), bg="blue", fg="white")
        take_btn.grid(row=0, column=4)

        upt_btn = Button(btn_frame, text="Update The  Photo", width=20, font=("Calibri", 12, "bold"), bg="blue",
                         fg="white")
        upt_btn.grid(row=0, column=5)

        # right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="#FCBBFF", relief=RAISED,
                                 text="STUDENT DETAILS",
                                 font=("calibri", 15, "bold"))
        Right_frame.place(x=750, y=8, width=745, height=530)

        img_right = Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\facialrecognition.png")
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=10, y=0, width=720, height=80)

        # search system

        search_frame = LabelFrame(Right_frame, bd=3, bg="#FCBBFF", relief=GROOVE,
                                  text="Search System",
                                  font=("calibri", 15, "bold"))
        search_frame.place(x=5, y=85, width=725, height=80)

        search_label = Label(search_frame, text="Search By:", font=("Calibri", 15),
                             fg="black", bg="#FCBBFF")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("Calibri", 12), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll No", "Department", "Semester", "Year", "Course")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("Calibri", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=14, font=("Calibri", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        show_btn = Button(search_frame, text="Show All", width=14, font=("Calibri", 12, "bold"), bg="blue", fg="white")
        show_btn.grid(row=0, column=4, padx=6)

        # table frame

        tbl_frame = Frame(Right_frame, bd=3, bg="#FCBBFF", relief=GROOVE)
        tbl_frame.place(x=5, y=175, width=725, height=320)

        scroll_x = ttk.Scrollbar(tbl_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tbl_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(tbl_frame, columns=(
            "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address",
            "teacher",
            "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=150)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=120)
        self.student_table.column("name", width=150)
        self.student_table.column("div", width=150)
        self.student_table.column("roll", width=150)
        self.student_table.column("gender", width=150)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=150)
        self.student_table.column("address", width=200)
        self.student_table.column("teacher", width=150)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # function declaration

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Ma@210103",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                                                                                                                            self.var_dep.get(),
                                                                                                                            self.var_course.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_semester.get(),
                                                                                                                            self.va_std_id.get(),
                                                                                                                            self.var_std_name.get(),
                                                                                                                            self.var_div.get(),
                                                                                                                            self.var_roll.get(),
                                                                                                                            self.var_gender.get(),
                                                                                                                            self.var_dob.get(),
                                                                                                                            self.var_email.get(),
                                                                                                                            self.var_phone.get(),
                                                                                                                            self.var_address.get(),
                                                                                                                            self.var_teacher.get(),
                                                                                                                            self.var_radio1.get()

                                                                                                              ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # fetching data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Ma@210103",
                                       database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get cursor

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update function

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Upadate = messagebox.askyesno("Upadte", "Do you want to update this student details", parent=self.root)
                if Upadate > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Ma@210103",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.va_std_id.get()
                                                                                                                                                                            ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success", "Student detail successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()   
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

                # not working -- update button"""

    # delete function

    def delete_data(self):
        if self.va_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete the details",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Ma@210103",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.va_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted the details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    # reset function

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("A")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ==== Generate data set or take photo samples

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Ma@210103", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.va_std_id.get()
                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # face

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:
                        face_cropped =img[y:y+h,x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed successfully!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)
            





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
