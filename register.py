from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

        # variables

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_secQ=StringVar()
        self.var_secA=StringVar()
        self.var_pass=StringVar()
        self.var_cnf_pass=StringVar()


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ASUS\Desktop\FACE\college_images\bg.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="#6174FF")
        frame.place(x=685,y=100,width=800,height=630)

        register_lbl=Label(frame,text="Register Here", font=("comic sans ms",26,"bold"),fg="white",bg="#6174FF")
        register_lbl.place(x=20,y=20)
        
        # first name

        fname=Label(frame,text="First Name" ,font=("comic sans",15,"bold"),fg="white",bg="#6174FF")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("comic sans",15))
        self.fname_entry.place(x=53,y=140,width=250)

        # last name
        
        lname=Label(frame,text="Last Name" ,font=("comic sans",15,"bold"),fg="white",bg="#6174FF")
        lname.place(x=440,y=100)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("comic sans",15))
        self.lname_entry.place(x=443,y=140,width=250)

        # contact
        
        cont=Label(frame,text="Contact No" ,font=("comic sans",15,"bold"),fg="white",bg="#6174FF")
        cont.place(x=50,y=200)

        self.cont_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("comic sans",15))
        self.cont_entry.place(x=53,y=240,width=250)

        # email

        email=Label(frame,text="Email" ,font=("comic sans",15,"bold"),fg="white",bg="#6174FF")
        email.place(x=440,y=200)

        self.mail_entry=ttk.Entry(frame,textvariable=self.var_email,font=("comic sans",15))
        self.mail_entry.place(x=443,y=240,width=250)

        # sec ques

        secQ=Label(frame,text="Select Security Question" ,font=("comic sans",15,"bold"),fg="white",bg="#6174FF")
        secQ.place(x=50,y=300)

        self.secQ_entry=ttk.Combobox(frame,textvariable=self.var_secQ,font=("comic sans",15), state="readonly")
        self.secQ_entry["values"]=("Select","Your birth place","Your pet name")
        self.secQ_entry.place(x=53,y=340,width=250)
        self.secQ_entry.current(0)
        
        # security ans
        secA=Label(frame,text="Security Answer" ,font=("comic sans",15,"bold"),fg="white",bg="#6174FF")
        secA.place(x=440,y=300)

        self.secA_entry=ttk.Entry(frame,textvariable=self.var_secA,font=("comic sans",15))
        self.secA_entry.place(x=443,y=340,width=250)

        # create password
        cre_pass=Label(frame,text="Create Password" ,font=("comic sans",15,"bold"),fg="white",bg="#6174FF")
        cre_pass.place(x=50,y=400)

        self.cre_pass_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("comic sans",15))
        self.cre_pass_entry.place(x=53,y=440,width=250)

        # confirm password
        con_pass=Label(frame,text="Confirm Password" ,font=("comic sans",15,"bold"),fg="white",bg="#6174FF")
        con_pass.place(x=440,y=400)

        self.con_pass_entry=ttk.Entry(frame,textvariable=self.var_cnf_pass,font=("comic sans",15))
        self.con_pass_entry.place(x=443,y=440,width=250)
        
        # checkbox
        self.var_check=IntVar()
        checkbox=Checkbutton(frame,variable=self.var_check,text="Read and agree to the terms & conditions" ,font=("comic sans",8),onvalue=1,offvalue=0)
        checkbox.place(x=53,y=520)

        loginbtn1=Button(frame,text="Login",command=self.return_login,font=("cambria",15),bd=2,relief=RAISED,fg="dark blue",bg="light yellow",activeforeground="black",activebackground="light yellow")
        loginbtn1.place(x=440,y=520,width=90,height=35)

        regbtn=Button(frame,text="Register",command=self.register_data,font=("cambria",15),bd=2,relief=RAISED,fg="dark blue",bg="light yellow",activeforeground="black",activebackground="light yellow")
        regbtn.place(x=573,y=520,width=120,height=35)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_secQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!= self.var_cnf_pass.get():
            messagebox.showerror("Error","Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to tthe terms & conditions")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Ma@210103",database="login")
                my_cursor=conn.cursor()
                query=("Select * from register where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exit , please try another email")
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_contact.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_secQ.get(),
                                                                                            self.var_secA.get(),
                                                                                            self.var_pass.get()
                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registered successfully",parent=self.root)
            except Exception as es:
                    messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def return_login(self):
        self.root.destroy()
           

            


        




if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()