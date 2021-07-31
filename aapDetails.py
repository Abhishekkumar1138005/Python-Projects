from tkinter import*
from PIL import ImageTk

root=Tk()
root.title("Arvind Kejriwal")
root.iconphoto(True,PhotoImage(file="icons/logo.png"))
aapDetails=ImageTk.PhotoImage(file="image/kejruAchivement.jpg")
aap=Label(root,image=aapDetails)
aap.pack()
root.mainloop()
