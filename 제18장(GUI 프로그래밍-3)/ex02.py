from tkinter import *

window = Tk()

def key(event):
    print(repr(event.char), "키 입력")

def callback(event):
    frame.focus_set()   # 키보드 포커스
    print(event.x, event.y, "마우스 이벤트")

frame = Frame(window, width=300, height=300)
frame.bind("<Button-1>", callback)
frame.bind("<Key>", key)
frame.pack()

window.mainloop()