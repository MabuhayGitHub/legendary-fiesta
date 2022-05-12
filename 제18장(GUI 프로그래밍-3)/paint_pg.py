from tkinter import *
from tkinter.colorchooser import askcolor

DEFAULT_PEN_SIZE = 1.0
DEFAULT_COLOR = "BLACK"

mode = "pen"
old_x = None
oly_y = None
myColor = DEFAULT_COLOR
erase_on = False

def use_pen():
    global mode
    mode = "pen"
    print("모드", mode)

def choose_color():
    global myColor
    myColor = askcolor(color=myColor)[1]
    print("색상", myColor)

def use_erase():
    global mode
    mode = "erase"
    print("모드", mode)

def paint(event):
    global var, erase_on, mode, old_x, old_y
    fill_color = "white" if mode == "erase" else myColor

    if old_x and old_y:
        canvas.create_line(old_x, old_y, event.x, event.y, capstyle=ROUND, width=var.get(), fill=fill_color)
    old_x = event.x
    old_y = event.y

def reset(event):
    global old_x, old_y
    old_x = None
    old_y = None

def clear_all():
    canvas.delete(ALL)

root = Tk()
var = DoubleVar()

penButton = Button(root, text="펜", command=use_pen)
# penButton.bind("<Button-1>", use_pen)
penButton.grid(row=0, column=0, sticky=W+E)

colorButton = Button(root, text="색상", command=choose_color)
# colorButton.bind("<Button-1>", choose_color)
colorButton.grid(row=0, column=1, sticky=W+E)

eraseButton = Button(root, text="지우개", command=use_erase)
# eraseButton.bind("<Button-1>", use_erase)
eraseButton.grid(row=0, column=2, sticky=W+E)

clearButton = Button(root, text="모두삭제", command=clear_all)
# clearButton.bind("<Button-1>", clear_all)
clearButton.grid(row=0, column=3, sticky=W+E)

scale = Scale(root, variable=var, orient=VERTICAL)
scale.grid(row=1, column=4, sticky=N+S)

canvas = Canvas(root, bg="white", width=600, height=500)
canvas.grid(row=1, columnspan=4)

canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", reset)

root.mainloop()