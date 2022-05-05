# Layout Manager

from tkinter import *

window = Tk()
window.title("배치 관리자")

button1 = Button(window, text="버튼1", width=30, height=10, bg="blue")
button2 = Button(window, text="버튼2", width=30, height=10, bg="yellow")
button3 = Button(window, text="버튼3", width=30, height=10, bg="red")

# button1.pack()
# button2.pack()
button1.pack(side=LEFT, padx=10, pady=20)
button2.pack(side=LEFT, padx=10, pady=20)
button3.pack(side=LEFT, padx=10, pady=20)

button1["text"] = "첫번째 버튼"
button2["text"] = "두번째 버튼"
button3["text"] = "세번째 버튼"

window.mainloop()