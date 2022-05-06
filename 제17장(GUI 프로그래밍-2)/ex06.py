# 텍스트 위젯 = Textarea

from tkinter import *

window = Tk()

t = Text(window, height=50, width=200)
t.insert(END, "텍스트 위젯")
t.pack()

window.mainloop()