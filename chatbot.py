from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x710+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg="powder blue", width=610)
        main_frame.pack()

        img_chat=Image.open(r"C:\Users\ASUS\Desktop\FACE\college_images\chat.jpg")
        img_chat=img_chat.resize((130,70))
        self.photoimg=ImageTk.PhotoImage(img_chat)

        title_lbl = Label(main_frame,bd=3,relief=RAISED,anchor="nw",width=730,compound=LEFT,image=self.photoimg,text=" Hi ! KiWi HERE...", font=("Eras Bold ITC", 35, "bold"), bg="white",
                          fg="dark blue")
        title_lbl.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=10,relief=RAISED,font=("comic sans ms",14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg="white",width=730)
        btn_frame.pack()

        lable1=Label(btn_frame,text="ASK ME",font=("comic sans ms",15,"bold"),fg="purple",bg="white")
        lable1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=35,font=("calibri",16))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send >>",command=self.send,width=8,font=("comic  sans ms",14,"bold"),background="purple",fg="white")
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear All",command=self.clear_all,width=8,font=("comic  sans ms",13,"bold"),background="light yellow",fg="black")
        self.clear.grid(row=0,column=3,padx=5,sticky=W)


        self.msg=''
        self.lable2=Label(btn_frame,text=self.msg,font=("comic sans ms",15,"bold"),fg="purple",bg="white")
        self.lable2.grid(row=1,column=1,padx=5,sticky=W)

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
    
    def clear_all(self):
        # Clear the chat window
        self.text.delete(1.0, END)
        self.entry.set('')


        # function

    def send(self):
        send='t\t\t'+ 'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==""):
            self.msg='        Please enter some input'
            self.lable2.config(text=self.msg,fg="red")
        else:
            self.msg=''
            self.lable2.config(text=self.msg,fg="red")

        if (self.entry.get()=="Hello"):
            self.text.insert(END,'\n\n'+'KIWI: Hi')

        elif (self.entry.get()=="Hi"):
            self.text.insert(END,'\n\n'+'KIWI: Hello')

        elif (self.entry.get()=="How does the face recognition attendance system work?"):
            self.text.insert(END,'\n\n'+'KIWI: The system uses facial recognition technology\n to identify and verify individuals based on unique facial features.\n It captures an image of face of a person, extracts facial features,\n and compares them with stored data to determine identity.')
        
        elif (self.entry.get()=="What are the key advantages of using face recognition for attendance tracking?"):
            self.text.insert(END,'\n\n'+'KIWI: Face recognition offers quick and accurate identification,\n eliminates the need for physical contact (e.g.,fingerprint scanning),\n and provides a non-intrusive and user-friendly experience.')

        elif (self.entry.get()=="How secure is the face recognition attendance system?"):
            self.text.insert(END,'\n\n'+'BOT: Face recognition systems are generally secure,\n employing advanced algorithms and encryption methods.\n However, like any technology, they require proper implementation \nand regular updates to guard against potential security threats.')
        
        elif (self.entry.get()=="Can the system recognize faces in different lighting conditions?"):
            self.text.insert(END,'\n\n'+'BOT: Yes, most modern face recognition systems are designed \nto work in various lighting conditions. They often include \nalgorithms that adapt to changes in lighting, ensuring reliable performance.')
        
        elif (self.entry.get()=="How does the system handle variations such as facial hair or changes in hairstyle?"):
            self.text.insert(END,'\n\n'+'BOT:  The system is trained to recognize facial features \nrather than specific details like hairstyle. It can accommodate \nvariations such as facial hair or changes in hairstyle within\n certain limits, providing flexibility for users.')
        
        elif (self.entry.get()=="Can the system be integrated with existing attendance management software?"):
            self.text.insert(END,'\n\n'+'BOT: Yes, face recognition attendance systems are often designed \nto be compatible with various software solutions. Integration can \nstreamline attendance tracking and provide seamless data transfer \nto existing management systems.')

        elif (self.entry.get()=="Who is the developer?"):
            self.text.insert(END,'\n\n'+'KIWI: Mainak Roy')

        elif (self.entry.get()=="Who is mainak's gf?"):
            self.text.insert(END,'\n\n'+'KIWI: peru')
        elif (self.entry.get()=="Who is mainak's teacher?"):
            self.text.insert(END,'\n\n'+'KIWI: Monidip Saha')


        
        elif (self.entry.get()=="What is the accuracy rate of the face recognition system in identifying individuals?"):
            self.text.insert(END,'\n\n'+'KIWI: The accuracy of face recognition systems can vary, \nbut modern systems typically achieve high accuracy rates, often surpassing \nother biometric methods. The accuracy is influenced by factors such as\n the quality of the hardware, the training data, and the algorithms used.')
        elif (self.entry.get()=="How does the system handle privacy concerns?"):
            self.text.insert(END,'\n\n'+'KIWI: Privacy is a priority in face recognition systems.\nData protection measures, including encryption and secure storage practices, \nare implemented. Additionally, some systems allow users to opt in or out \nand provide transparency about how the collected data is used.')
        elif (self.entry.get()=="Can the system generate attendance reports for administrators?"):
            self.text.insert(END,'\n\n'+'KIWI: Yes, most face recognition attendance systems offer reporting features.\n Administrators can generate detailed attendance reports, \nincluding information such as attendance patterns, late arrivals, and absences.')
        elif (self.entry.get()=="What types of businesses or organizations can benefit from a face recognition attendance system?"):
            self.text.insert(END,'\n\n'+'KIWI: Face recognition attendance systems are versatile and \ncan be beneficial for various industries, including education,\n corporate offices, healthcare, and government institutions.')
        elif (self.entry.get()=="Bye"):
            self.text.insert(END,'\n\n'+'KIWI: Thank you . Hope the queries are solved')

        else:
            self.text.insert(END,'\n\n'+'KIWI: Sorry I did  nott get it..')

        









if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
