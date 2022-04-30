import tkinter
key = 0
def keyClick(e):
    global key
    key = e.keycode
    print("입력 코드 : " + str(key))

tk = tkinter.Tk()
tk.title("키 입력")
tk.bind("<Key>", keyClick)

tk.mainloop()
