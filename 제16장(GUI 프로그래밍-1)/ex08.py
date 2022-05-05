# # Pack: 압축 배치 관리자

# from tkinter import *

# window = Tk()

# Button(window, text="박스 #1", bg="red", fg="white").pack()
# Button(window, text="박스 #2", bg="green", fg="white").pack()
# Button(window, text="박스 #3", bg="blue", fg="white").pack()
# Button(window, text="박스 #4", bg="black", fg="white").pack()

# window.mainloop()

# # ----------------------------------------------------------------

# # Grid: 격자 배치 관리자

# from tkinter import *

# window = Tk()

# b1 = Button(window, text="박스 #1", bg="red", fg="white")
# b2 = Button(window, text="박스 #2", bg="green", fg="white")
# b3 = Button(window, text="박스 #3", bg="blue", fg="white")
# b4 = Button(window, text="박스 #4", bg="black", fg="white")

# b1.grid(row=0, column=0)
# b2.grid(row=0, column=1)
# b3.grid(row=1, column=0)
# b4.grid(row=1, column=1)

# window.mainloop()

# ----------------------------------------------------------------

# Place: 절대 위치 배치 관리자

from tkinter import *

window = Tk()
window.geometry("500x500")

b1 = Button(window, text="박스 #1", bg="red", fg="white")
b1.place(x=10, y=10)
b2 = Button(window, text="박스 #2", bg="green", fg="white")
b2.place(x=50, y=50)
b3 = Button(window, text="박스 #3", bg="blue", fg="white")
b3.place(x=100, y=100)
b4 = Button(window, text="박스 #4", bg="black", fg="white")
b4.place(x=200, y=200)

window.mainloop()
