# 마우스 클릭 이벤트

from tkinter import *

# window = Tk()

def sClick(event):
    print(event.x, event.y, "단일 클릭 마우스 이벤트")

def dClick(event):
    print(event.x, event.y, "더블 클릭 마우스 이벤트")

button = Button(None, text="마우스 클릭")
button.bind("<Button-1>", sClick)
button.bind("<Double-1>", dClick)
button.pack()

button.mainloop()