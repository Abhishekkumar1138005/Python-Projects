from tkinter import*
from PIL import ImageTk

root=Tk()
root.title("Narendra Modi")
root.iconphoto(True,PhotoImage(file="icons/logo.png"))
bjpDetails=ImageTk.PhotoImage(file="image/modi-achievements-2014-2019-again-list.jpg")
bjp=Label(root,image=bjpDetails)
bjp.pack()
root.mainloop()
