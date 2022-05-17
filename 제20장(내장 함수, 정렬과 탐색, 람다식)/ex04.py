from tkinter import *

window = Tk()

btn1 = Button(window, text="버튼1", command=lambda : print("버튼 1이 눌러짐"))
btn1.pack(side=LEFT)
btn2 = Button(window, text="버튼2", command=lambda : print("버튼 2이 눌러짐"))
btn2.pack(side=LEFT)
btnQuit = Button(window, text="종료", fg="red", command=quit)
btnQuit.pack(side=LEFT)

window.mainloop()