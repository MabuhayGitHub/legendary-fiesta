from tkinter import *
from tkinter import messagebox

def click(event):
    test = entry.get()
    messagebox.showinfo("name", test)

window = Tk()

entry = Entry(window)
entry.bind()
button = Button(window, text="확인")
entry.pack(side=LEFT, padx=5)
button.pack(side=LEFT)

button.bind("<Button-1>", click)

window.mainloop()