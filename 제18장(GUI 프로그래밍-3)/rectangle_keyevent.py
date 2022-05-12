from tkinter import *

def left(event):
    print("left")
    canvas.move(rect, -5, 0)
def right(event):
    print("right")
    canvas.move(rect, 5, 0)
def up(event):
    print("up")
    canvas.move(rect, 0, -5)
def down(event):
    print("down")
    canvas.move(rect, 0, 5)

root = Tk()

canvas = Canvas(root, bg="white", width=500, height=500)
canvas.pack()
rect = canvas.create_rectangle(100, 100, 200, 200, fill="red")

canvas.focus_set()
canvas.bind("<Left>", left)
canvas.bind("<Right>", right)
canvas.bind("<Up>", up)
canvas.bind("<Down>", down)


root.mainloop()