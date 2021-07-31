from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

root=Tk()
root.title("Voting Machine")
root.geometry("800x650+490+100")
root.config(bg="#95B9C7")

title=Label(root,text="~~~~~~~~ VOTING\t MACHINE ~~~~~~~~",relief=GROOVE,font=("black cooper",25,"bold"),bg="black",fg="yellow")
title.pack(side=TOP,fill=X)
#========================================FRAME==============================
frame=Frame(root,bd=4,bg="white",relief=RIDGE)
frame.place(x=0,y=40,width=800,height=600)

#=========================================OPERATIONS===============================
def modi():
    try:
        conn = pymysql.connect(host="localhost",user="root",password="",database="vote_india")
        cursor=conn.cursor()
        cursor.execute("UPDATE `candidate` SET `votes` = votes +1 WHERE party = 'bjp'")
        conn.commit()
        conn.close()
        messagebox.showinfo("Congratulation","You Voted For BJP")
        vote_img1["stat"]="disabled"
        vote_img2["stat"]="disabled"
        vote_img3["stat"]="disabled"
        root.destroy()
    except Exception as es:
        messagebox.showerror("error handle",{str(es)})
        
def rahul():
    try:
        conn = pymysql.connect(host="localhost",user="root",password="",database="vote_india")
        cursor=conn.cursor()
        cursor.execute("UPDATE `candidate` SET `votes` = votes +1 WHERE party = 'congress'")
        conn.commit()
        conn.close()
        messagebox.showinfo("voted","You voted Congress")
        vote_img1["stat"]="disabled"
        vote_img2["stat"]="disabled"
        vote_img3["stat"]="disabled"
        root.destroy()
    except Exception as es:
        messagebox.showerror("error handle",{str(es)})
def kejru():
    try:
        conn = pymysql.connect(host="localhost",user="root",password="",database="vote_india")
        cursor=conn.cursor()
        cursor.execute("UPDATE `candidate` SET `votes` = votes +1 WHERE party = 'aap'")
        conn.commit()
        conn.close()
        messagebox.showinfo("voted","You voted AAP")
        vote_img1["stat"]="disabled"
        vote_img2["stat"]="disabled"
        vote_img3["stat"]="disabled"
        root.destroy()
    except Exception as es:
        messagebox.showerror("error handle",{str(es)})
    
#==========================IMAGES========================================
b_img=ImageTk.PhotoImage(file="image/bjp.png")
bjp_img=Label(frame,image=b_img,bg="white")
bjp_img.grid(row=0,column=0)


m_img1=ImageTk.PhotoImage(file="image/modi.png")
modi_img=Label(frame,image=m_img1,bg="white")
modi_img.grid(row=0,column=1)

v_img=ImageTk.PhotoImage(file="image/vote.png")
vote_img1=Button(frame,image=v_img,bg="white",bd=0,command=modi)
vote_img1.grid(row=0,column=2,padx=50)

c_img=ImageTk.PhotoImage(file="image/congress.png")
congress_img=Label(frame,image=c_img,bg="white")
congress_img.grid(row=1,column=0)

m_img2=ImageTk.PhotoImage(file="image/rahul.png")
rahul_img=Label(frame,image=m_img2,bg="white")
rahul_img.grid(row=1,column=1)


vote_img2=Button(frame,image=v_img,bg="white",bd=0,command=rahul)
vote_img2.grid(row=1,column=2,padx=50)

a_img=ImageTk.PhotoImage(file="image/aap.png")
aap_img=Label(frame,image=a_img,bg="white")
aap_img.grid(row=2,column=0)

m_img3=ImageTk.PhotoImage(file="image/kejru.png")
kejru_img=Label(frame,image=m_img3,bg="white")
kejru_img.grid(row=2,column=1)

vote_img3=Button(frame,image=v_img,bg="white",bd=0,command=kejru)
vote_img3.grid(row=2,column=2,padx=50)
#================================================================================

root.mainloop()

