from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql



class Registration:
    def __init__(self,root):
        self.root=root
        self.root.title('VOTER REGISTRATION')
        self.root.geometry("1000x563+490+100")
        self.root.iconphoto(True,PhotoImage(file="icons/logo.png"))
        self.root.config(bg="white")
        self.root.resizable(0,0)
        #===================================================
        self.root.bg=ImageTk.PhotoImage(file="image/registration.jpg")
        bg=Label(root,image=self.root.bg,background="steelblue").place(x=0,y=0,relwidth=1,relheight=1)

        
        frame=Frame(self.root,bg="white")
        frame.place(x=80,y=80,height=400,width=830)

        self.img=ImageTk.PhotoImage(file="icons/user_img.png")
        user_img=Label(self.root,image=self.img,bg="light blue").place(x=455,y=10,width=60,height=60)


        Vid=Label(frame,text="Voter ID :",bg="white",font=("times new roman",12)).grid(row=0,column=0)
        self.txt_Vid=Entry(frame,font=("times new roman",16),bg="white")
        self.txt_Vid.grid(row=0,column=1)


        Name=Label(frame,text="Full Name :",bg="white",font=("times new roman",12)).grid(ipadx=50,pady=30,row=1,column=0)
        self.txt_Name=Entry(frame,font=("times new roman",11),bg="white")
        self.txt_Name.grid(row=1,column=1)

        Email=Label(frame,text="Email Id :",bg="white",font=("times new roman",12)).grid(row=1,column=2)
        self.txt_Email=Entry(frame,font=("times new roman",11),bg="white")
        self.txt_Email.grid(row=1,column=3)

        Pno=Label(frame,text="Phone No :",bg="white",font=("times new roman",12)).grid(ipadx=50,pady=30,row=2,column=0)
        self.txt_Pno=Entry(frame,font=("times new roman",11),bg="white")
        self.txt_Pno.grid(row=2,column=1)

        State=Label(frame,text="Choose State :",font=("times new roman",12),bg="white").grid(row=2,column=2)
        self.cmb_State=ttk.Combobox(frame,font=("times new roman",9),state='readonly',justify=CENTER)
        self.cmb_State['values']=("","Bihar","Delhi","Mumbai","Madhya Pradesh","Uttar Pradesh")
        self.cmb_State.grid(row=2,column=3)
        self.cmb_State.current(0)

        Age=Label(frame,text="Age :",bg="white",font=("times new roman",12)).grid(ipadx=50,pady=30,row=3,column=0)
        self.txt_Age=Entry(frame,font=("times new roman",11),bg="white")
        self.txt_Age.grid(row=3,column=1)
        

        Gender=Label(frame,text="Gender :",font=("times new roman",12),bg="white").grid(row=3,column=2)
        self.cmb_Gender=ttk.Combobox(frame,font=("times new roman",8),state='readonly',justify=CENTER)
        self.cmb_Gender['values']=("","MALE","FEMALE","OTHERS")
        self.cmb_Gender.grid(row=3,column=3)
        self.cmb_Gender.current(0)

        

        Pwd=Label(frame,text="Password :",bg="white",font=("times new roman",12)).grid(row=4,column=0)
        self.txt_Pwd=Entry(frame,font=("times new roman",11),bg="white")
        self.txt_Pwd.grid(row=4,column=1)

        Cpwd=Label(frame,text="Confirm Password :",bg="white",font=("times new roman",12)).grid(row=4,column=2)
        self.txt_Cpwd=Entry(frame,font=("times new roman",11),bg="white")
        self.txt_Cpwd.grid(ipadx=50,pady=30,row=4,column=3)

        #=====================BUTTON===========================================
        self.root.btn_img=ImageTk.PhotoImage(file="icons/register.png")
        btn_img=Button(self.root,image=root.btn_img,bg="steel blue",activebackground="light blue",bd=0,cursor="hand2",command=self.register).place(x=370,y=480,height=45,width=170)



    def register(self):
        
        if self.txt_Vid.get() == "" or self.txt_Name.get()=="" or self.txt_Email.get()=="" or self.txt_Pno.get()=="" or self.txt_Age.get()=="" or self.txt_Pwd.get()=="" or self.txt_Cpwd.get()=="" or self.cmb_State.get()=="" or self.cmb_Gender.get()=="":
            
            messagebox.showerror("warning","All fields are required to fill",parent=self.root )
        elif self.txt_Pwd.get() != self.txt_Cpwd.get():
            messagebox.showerror("warning","password and confirm password should be same",parent=self.root)
        
        else:
            try:
                conn = pymysql.connect(host="localhost",user="root",password="",database="vote_india")
                cursor=conn.cursor()
                cursor.execute("insert into voter_registration(voter_id,name,email,phone_no,state,age,gender,password)values(%s,%s,%s,%s,%s,%s,%s,%s)",
                               (
                                   self.txt_Vid.get(),
                                   self.txt_Name.get(),
                                   self.txt_Email.get(),
                                   self.txt_Pno.get(),
                                   self.cmb_State.get(),
                                   self.txt_Age.get(),
                                   self.cmb_Gender.get(),
                                   self.txt_Pwd.get(),

                                   ))
                conn.commit()
                conn.close()
                messagebox.showinfo("success","Register successfully",parent=self.root)
                root.destroy()
            except Exception as es:
                messagebox.showerror("error","error handle,{str(es)}",parent=self.root)
                            

root=Tk()
obj=Registration(root)
root.mainloop()
