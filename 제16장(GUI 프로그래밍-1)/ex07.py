# Entry widget

from tkinter import *

window = Tk()
window.title = "엔트리 위젯 실습"
window.geometry("400x200")

entry = Entry(window, fg="black", bg="yellow", width=80)
entry.pack()

window.mainloop()