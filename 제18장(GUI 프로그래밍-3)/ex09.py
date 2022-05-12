from tkinter import *
from tkinter.simpledialog import *

root = Tk()
root.geometry("400x100")

lbl1 = Label(root, text="입력된 값")
lbl1.pack()
# askinteger, askstring, askfloat
value = askinteger("주사위", "주사위 숫자(1~6)를 입력하세요.", minvalue=1, maxvalue=6)
lbl1.configure(text=str(value))

root.mainloop()