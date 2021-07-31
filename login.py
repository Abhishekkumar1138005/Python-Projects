from time import strftime
from tkinter.ttk import *
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import os

root=Tk()
root.title('Login')
root.config(bg="#566D7E")

root.geometry("600x600+660+130")
root.resizable(0,0)
root.iconphoto(True,PhotoImage(file="icons/logo.png"))
root.bg=ImageTk.PhotoImage(file="image/login.png")
bg=Label(root,image=root.bg).place(x=0,y=0)
#=======================================Functions======================================
def signin():
    if txt_Vid.get() == "" or txt_Pwd.get()=="" :
        messagebox.showerror("warning","All fields are required to fill",parent=root )
    else:
        try:
            conn=pymysql.connect(host="localhost",user="root",password="",database="vote_india")
            cur=conn.cursor()
            cur.execute("SELECT * FROM voter_registration where voter_id=%s and password=%s",[txt_Vid.get(),txt_Pwd.get()])
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Invalid","Invalid Id or Password")                  
            else:
                messagebox.showinfo("success","login successful.")
                checkVstatus()
                
                    
            conn.commit()
            conn.close()
                    
        except Exception as es:
            messagebox.showerror("error handle",{str(es)})

def updateVstatus():
    try:
        conn=pymysql.connect(host="localhost",user="root",password="",database="vote_india")
        cur=conn.cursor()
        cur.execute("UPDATE voter_registration SET vote_status=true WHERE voter_id=%s",[txt_Vid.get()])
        root.destroy()
        os.startfile("voting machine.py")
        conn.commit()
        conn.close()
                    
    except Exception as es:
        messagebox.showerror("error handle",{str(es)})

def checkVstatus():
    try:
        conn=pymysql.connect(host="localhost",user="root",password="",database="vote_india")
        cur=conn.cursor()
        cur.execute("SELECT vote_status FROM voter_registration WHERE voter_id=%s",[txt_Vid.get()])
        r=cur.fetchone()
        if r==((1,)):
            messagebox.showinfo("sorry","you have already voted!")
        else:
            messagebox.showinfo("welcome","you can vote")
            updateVstatus()
            
        
        conn.commit()
        conn.close()
                    
    except Exception as es:
        messagebox.showerror("error handle",{str(es)})

def time():
    string=strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)
#=============================================================UI================================
label=Label(root,font=("ds-digital",30),bg="black",fg="white")
label.pack(anchor="center")
time()

Vid=Label(root,text="Voter id",bg="#566D7E",font=("times new roman",14),bd=0).place(x=180,y=195,height=50,width=80)
txt_Vid=Entry(root,font=("times new roman",16),bd=0,bg="#566D7E",fg="white")
txt_Vid.place(x=260,y=195,width=180,height=50)


txt_Pwd=Entry(font=("times new roman",16),bg="#566D7E",bd=0,fg="white")
txt_Pwd.place(x=210,y=290,width=180,height=50)

login=Button(root,text="Login",fg="blue",bg="white",font=("times new roman",16),cursor="hand2",bd=0,command=signin).place(x=150,y=420,width=280,height=50)


                                



root.mainloop()
