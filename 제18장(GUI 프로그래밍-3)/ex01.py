# 위젯.bind(이벤트지정자, 이벤트 처리 함수)

from tkinter import *

window = Tk()

def callback(event):
    print(event.x, event.y, "마우스 이벤트")

frame = Frame(window, width=400, height=400)
frame.bind("<Button-1>", callback)  # 좌측 버튼
frame.bind("<Button-2>", callback)  # 휠
frame.bind("<Button-3>", callback)  # 우측 버튼
frame.pack()

window.mainloop()