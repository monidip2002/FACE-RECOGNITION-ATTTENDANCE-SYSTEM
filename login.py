from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from main import Face 
from register import Register   

class Login_window:
    def __init__(self, root):

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ASUS\Desktop\FACE\college_images\fc.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="#A5EED5")
        frame.place(x=555,y=140,width=425,height=450)

        img1=Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\LoginIconAppl.png")
        img1=img1.resize((90,90))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_1=Label(image=self.photoimage1,bg="#A5EED5",borderwidth=0)
        lbl_1.place(x=725,y=165,width=90,height=90)

        get_str=Label(frame,text="Get Started", font=("calibri",18,"bold"),fg="black",bg="#A5EED5")
        get_str.place(x=155,y=120)

        username=lbl_1=Label(frame,text="Username", font=("comic sans MS",16),fg="black",bg="#A5EED5")
        username.place(x=28,y=195)

        self.txtuser=ttk.Entry(frame, font=("calibri",12))
        self.txtuser.place(x=137,y=200,width=220)

        password=lbl_1=Label(frame,text="Password", font=("comic sans MS",16),fg="black",bg="#A5EED5")
        password.place(x=30,y=263)

        self.txtpass=ttk.Entry(frame, font=("calibri",12))
        self.txtpass.place(x=137,y=270,width=220)

        img2=Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\LoginIconAppl.png")
        img2=img2.resize((22,22))
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_1=Label(image=self.photoimage2,bg="#A5EED5",borderwidth=0)
        lbl_1.place(x=920,y=338,width=22,height=22)

        img3=Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\kk.png")
        img3=img3.resize((22,22))
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_1=Label(image=self.photoimage3,bg="#A5EED5",borderwidth=0)
        lbl_1.place(x=920,y=410,width=22,height=22)

        loginbtn=Button(frame,text="L o g i n",command=self.login ,font=("rog fonts",15),bd=2,relief=RAISED,fg="dark blue",bg="light yellow",activeforeground="black",activebackground="light yellow")
        loginbtn.place(x=150,y=330,width=125,height=40)

        registerbtn=Button(frame,text="Not Registered? Register here !",command=self.register_window, font=("aptos narrow",9),borderwidth=0,fg="dark blue",bg="#A5EED5",activeforeground="black",activebackground="#A5EED5")
        registerbtn.place(x=70,y=390)

        forgotbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window, font=("aptos narrow",9),borderwidth=0,fg="dark blue",bg="#A5EED5",activeforeground="black",activebackground="#A5EED5")
        forgotbtn.place(x=255,y=390)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "Mainak" and self.txtpass.get() == "Roy":
            messagebox.showinfo("Success", "Welcome to Face Recognition Attendance System")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Ma@210103", database="login")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (self.txtuser.get(), self.txtpass.get()))
                row = my_cursor.fetchone()
                
                if row is None:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    open_main = messagebox.askyesno("YesNo", "Access only admin")
                    if open_main:
                        if not hasattr(self, "new_window") or not self.new_window:
                            self.new_window = Toplevel(self.root)
                            self.app = Face(self.new_window)
                    else:
                        if not open_main:
                            return
            except Exception as e:
                print("Error:", e)
            finally:
                conn.commit()
                conn.close()
                


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Ma@210103", database="login")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("My Error","Please enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("315x420+610+170")
                self.root2.configure(bg="#6174FF")

                l=Label(self.root2,text="Forgot Password",font=("aptos",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=0,relwidth=1)

                # sec ques

                secQ=Label(self.root2,text="Security Question" ,font=("comic sans",15,"bold"),fg="white",bg="#6174FF")
                secQ.place(x=30,y=80)

                self.secQ_entry=ttk.Combobox(self.root2,font=("comic sans",15), state="readonly")
                self.secQ_entry["values"]=("Select","Your birth place","Your pet name")
                self.secQ_entry.place(x=33,y=110,width=250)
                self.secQ_entry.current(0)
                
                # security ans
                secA=Label(self.root2,text="Security Answer" ,font=("comic sans",15,"bold"),fg="white",bg="#6174FF")
                secA.place(x=30,y=150)

                self.secAns_entry=ttk.Entry(self.root2,font=("comic sans",15))
                self.secAns_entry.place(x=33,y=180,width=250)

                new_pass=Label(self.root2,text="New Password" ,font=("comic sans",15,"bold"),fg="white",bg="#6174FF")
                new_pass.place(x=30,y=220)

                self.new_pass_entry=ttk.Entry(self.root2,font=("comic sans",15))
                self.new_pass_entry.place(x=33,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("cambria",15),bd=2,relief=RAISED,fg="dark blue",bg="light yellow",activeforeground="black",activebackground="light yellow")
                btn.place(x=85,y=320,width=150)

    def reset_pass(self):
        if self.secQ_entry.get()=="Select":
           messagebox.showerror("Error","Select Security Question" ,parent=self.root2)
        elif self.secAns_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.new_pass_entry.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Ma@210103", database="login")
            my_cursor = conn.cursor()
            qury=("select * from register where email=%s and secQ=%s and secA=%s")
            vlaue=(self.txtuser.get(),self.secQ_entry.get(),self.secAns_entry.get(),)
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("My Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_pass_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset",parent=self.root2)
                self.root2.destroy()



if __name__ == "__main__":
    root = Tk()
    obj = Login_window(root)
    root.mainloop()