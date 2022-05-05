# tkinter: 파이썬 GUI 모듈
# widget: Windows gadget

from tkinter import *

# window = Tk()
# label = Label(window, text="Hello Python")
# label.pack()
# window.mainloop()
# window.quit()

# window = Tk()
# button1 = Button(window, text="Python Button")
# button2 = Button(window, text="Python Button")
# button1.pack(side=LEFT, padx = 10, pady = 10)
# button2.pack(side=LEFT, padx = 10, pady = 10)
# button1["text"] = "ONE"
# button2["text"] = "TWO"
# window.mainloop()

def callback():
    button["text"] = "버튼이 클릭되었어요"

window = Tk()
label = Label(window, text="안녕하세요")
label.pack()
button = Button(window, text="클릭", command=callback)
button.pack()
window.mainloop()
