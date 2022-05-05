from tkinter import *

window = Tk()
window.geometry("600x100")
window.title = "여러 배치 관리자 혼용"


frame = Frame(window)

button1 = Button(frame, text="박스 #1", bg="red", fg="white", width=10, height=2)
button2 = Button(frame, text="박스 #2", bg="green", fg="white", width=10, height=2)
button3 = Button(frame, text="박스 #3", bg="orange", fg="white", width=10, height=2)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

label = Label(window, text="버튼 위에 배치")

label.pack()
frame.pack()

window.mainloop()