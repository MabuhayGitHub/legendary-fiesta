from tkinter import *
import os
scriptpath = os.path.abspath(__file__) 
scriptdir = os.path.dirname(scriptpath)

window = Tk()

photo = PhotoImage(file=scriptdir+".\\images\\w2.gif")
label1 = Label(window, image=photo).pack(side=RIGHT)

msg = "상대자의 사랑을 받지 못하면서 사랑한다면\n \
        즉 사랑으로서의 사랑이 상대자의 사랑을 낳지 못한다면\n \
        즉 사랑하는 사람으로서의 자신의 생활적 표현으로써\n \
        자신을 사랑받는 사람으로 만들 수 없다면\n \
        그 사랑은 무력하며 그것은 불행이다."

msg1 = """상대자의 사랑을 받지 못하면서 사랑한다면\n 
        즉 사랑으로서의 사랑이 상대자의 사랑을 낳지 못한다면\n 
        즉 사랑하는 사람으로서의 자신의 생활적 표현으로써\n 
        자신을 사랑받는 사람으로 만들 수 없다면\n 
        그 사랑은 무력하며 그것은 불행이다."""

label2 = Label(window, justify=LEFT, padx=10, text=msg1).pack(side=LEFT)

window.mainloop()
