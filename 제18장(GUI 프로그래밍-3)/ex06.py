# 캔버스에 라인 그리기

from tkinter import *

def draw(event):
    global x, y
    canvas.create_line(x, y, event.x, event.y)
    x, y = event.x, event.y

def down(event):
    global x, y
    x, y = event.x, event.y

def up(event):
    global x, y
    if (x, y) == (event.x, event.y):
        canvas.create_line(x, y, x+1, y+1)

root = Tk()

canvas = Canvas(root, width=500, height=500, bg="white")


canvas.bind("<B1-Motion>", draw)
canvas.bind("<Button-1>", down)
canvas.bind("<ButtonRelease-1>", up)
canvas.pack()

root.mainloop()