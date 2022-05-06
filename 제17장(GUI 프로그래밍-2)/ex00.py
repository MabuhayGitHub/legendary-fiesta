# from tkinter import *

# import os
# scriptpath = os.path.abspath(__file__) 
# scriptdir = os.path.dirname(scriptpath)

# window = Tk()

# photo = PhotoImage(file=scriptdir+".\\images\\a1.gif")
# w = Label(window, image=photo)
# # w.photo = photo
# w.pack()

# window.mainloop()

# ----------------------------------------------------------------

from tkinter import *

window = Tk()

w = Canvas(window, width=300, height=200, bg="white")
w.pack()
i = w.create_line(0, 0, 300, 200, fill="yellow")
# w.coords(i, 0, 0, 300, 100)
# w.itemconfig(i, fill="blue")
# w.delete(i)
# w.delete(ALL)
w.create_line(0, 0, 300, 100, fill="red")
w.create_rectangle(50, 25, 200, 100, outline="blue")
w.create_rectangle(30, 50, 150, 120, fill="#FA88AB")

window.mainloop()