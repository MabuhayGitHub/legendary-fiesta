from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("파일 열기")
root.geometry("600x100")

lbl1 = Label(root, text="선택된 파일 이름")
lbl1.pack()

filename = askopenfilename(parent=root, filetypes=(("GIF파일", "*.gif"),("PNG파일", "*.png"),("JPG파일", "*.jpg"),("모든 파일", "*.*")))
lbl1.configure(text=str(filename))


root.mainloop()