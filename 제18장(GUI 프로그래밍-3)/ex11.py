from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("파일 열기")
root.geometry("600x100")

lbl1 = Label(root, text="저장된 파일 이름")
lbl1.pack()

saveFp = asksaveasfile(parent=root, mode="w", defaultextension=".jpg", filetypes=(("JPG파일", "*.jpg"),("모든 파일", "*.*")))
lbl1.configure(text=saveFp)
saveFp.close()

root.mainloop()