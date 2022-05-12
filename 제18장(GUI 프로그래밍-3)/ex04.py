from tkinter import *

def motion(event):
    print("마우스 포인터 위치:", event.x, event.y)

window = Tk()

frame = Frame(window, width=500, height=500, bg="yellow")
frame.bind("<Motion>", motion)
frame.pack()

window.mainloop()