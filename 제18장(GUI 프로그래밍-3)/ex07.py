from tkinter import *

root = Tk()

mainMenu = Menu(root)
root.config(menu=mainMenu)

fileMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="파일", menu=fileMenu)

fileMenu.add_command(label="열기")
fileMenu.add_separator()
fileMenu.add_command(label="종료")

root.mainloop()