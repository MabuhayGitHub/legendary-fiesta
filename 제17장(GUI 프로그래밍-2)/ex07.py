from tkinter import *

window = Tk()
# window.geometry("700x700")

canvas = Canvas(window, width=500, height=500, bg="white")
canvas.pack()

canvas.create_line(0,0, 500, 500, fill="blue")
canvas.create_line(0,500, 500, 0, fill="red", width=5)

canvas.create_rectangle(50, 50, 200, 200, fill="yellow")
canvas.create_rectangle(200, 200, 300, 400, fill="red", outline="blue", width=10)

window.mainloop()