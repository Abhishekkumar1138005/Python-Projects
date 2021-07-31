from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import datetime as dt
import pymysql

import os


class Main:
    def __init__(self,root):
        
        global frame2
        self.root=root
        self.root.title("VOTE INDIA")
        self.root.config(bg="#2B547E")
        self.root.iconphoto(True,PhotoImage(file="icons/logo.png"))
        self.root.state("zoomed")

        self.bg=ImageTk.PhotoImage(file="image/bg.png")
        bg=Label(self.root,image=self.bg).place(x=80,y=60)

        
        title=Label(self.root,text="VOTE INDIA",relief=GROOVE,font=("black cooper",40,"bold"),bg="black",fg="yellow")
        title.pack(side=TOP,fill=X)
        #===============================================FRAME1=============================
        frame1=Frame(self.root,bd=4,bg="white",relief=RIDGE)
        frame1.place(x=30,y=100,width=250,height=650)



        #===============================================FRAME2=============================        
        frame2=Frame(self.root,bd=4,bg="#E3E4FA",relief=RIDGE)
        frame2.place(x=500,y=100,width=1000,height=650)
        
        
        

        #=================================================================================================
        root.btn1=ImageTk.PhotoImage(file="icons/registration.png")
        btn1=Button(frame1, text="REGISTER",image=root.btn1,compound=RIGHT,font=("cooper black",18,"bold"),bg="#659EC7",fg="white",cursor="hand2",command=self.registration)
        btn1.pack(padx=5,pady=10,fill=X)

        root.btn2=ImageTk.PhotoImage(file="icons/details.png")
        btn2=Button(frame1, text="CANDIDATE\nDETAILS",image=root.btn2,compound=RIGHT,font=("cooper black",18,"bold"),bg="#38ACEC",fg="white",cursor="hand2",command=self.details)
        btn2.pack(padx=5,pady=10,fill=X)

        root.btn3=ImageTk.PhotoImage(file="icons/voting.png")
        btn3=Button(frame1, text="VOTE",image=root.btn3,compound=RIGHT,font=("cooper black",18,"bold"),bg="#5E5A80",fg="white",cursor="hand2",command=self.vote)
        btn3.pack(padx=5,pady=10,fill=X)

        
        clock=Label(frame1,text=f"{dt.datetime.now():%a,%b %d %y}",font=("cooper black",18,"bold"),bg="#4E9258",fg="white")
        clock.pack(padx=5,pady=10,ipady=30,fill=X)

        name=Label(frame1,text="Abhishek Kumar\n0103EE181007\nElectrical\nEngineering",font=("cooper black",16,"bold"),bg="#E3E4FA",fg="black")
        name.pack(padx=5,pady=10,fill=X)

        root.btn5=ImageTk.PhotoImage(file="icons/exit.png")
        btn5=Button(frame1, text="EXIT",image=root.btn5,compound=RIGHT,font=("cooper black",18,"bold"),bg="#800517",fg="white",cursor="hand2",command=self.exit)
        btn5.pack(padx=5,pady=10,fill=X,side=BOTTOM)

#===============================================================================================================================================================================================
    def registration(self):
        os.startfile("registration.py")
        
    def details(self):
        global frame2
        root.btnb=ImageTk.PhotoImage(file="image/bjp.png")
        btnb=Button(frame2, text="BJP",image=root.btnb,compound=TOP,font=("cooper black",18,"bold"),bg="#FFDAB9",fg="gray",cursor="hand2",command=self.bjpDetails)
        btnb.pack(padx=60,pady=10,side=LEFT)

        root.btna=ImageTk.PhotoImage(file="image/aap.png")
        btna=Button(frame2, text="AAP",image=root.btna,compound=TOP,font=("cooper black",18,"bold"),bg="#FFDAB9",fg="gray",cursor="hand2",command=self.aapDetails)
        btna.pack(padx=25,pady=10,side=LEFT)

        root.btnc=ImageTk.PhotoImage(file="image/congress.png")
        btnc=Button(frame2, text="CONGRESS",image=root.btnc,compound=TOP,font=("cooper black",18,"bold"),bg="#FFDAB9",fg="gray",cursor="hand2",command=self.congressDetails)
        btnc.pack(padx=60,pady=10,side=LEFT)
        


    def bjpDetails(self):
        os.startfile("bjpDetails.py")
        
    def congressDetails(self):
        pass
    
    def aapDetails(self):
        os.startfile("aapDetails.py")

    def result(self):
        pass
        
    def vote(self):
        os.startfile("login.py")
        
    def exit(self):
        root.destroy()


root=Tk()
obj=Main(root)
root.mainloop()
