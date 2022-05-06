from msilib.schema import File
from tkinter import *
import os
scriptpath = os.path.abspath(__file__) 
scriptdir = os.path.dirname(scriptpath)

window = Tk()

photo = PhotoImage(file=scriptdir+".\\images\\a1.gif")

label1 = Label(window, image=photo)
label1.photo = photo
label1.pack()

window.mainloop()