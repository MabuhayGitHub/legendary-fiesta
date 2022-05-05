from tkinter import *

def callback():
    button["text"] = "버튼이 클릭되었어요"

window = Tk()
window.title = "이벤트 실습"

button = Button(window, text="버튼을 누르세요", command=callback)
button.pack(side=LEFT)

window.mainloop()