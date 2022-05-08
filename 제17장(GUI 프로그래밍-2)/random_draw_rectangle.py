import random
import time
from tkinter import *

window = Tk()

canvas = Canvas(window, width=600, height=500, bg="white")
canvas.pack()

color = ["red", "orange", "black", "yellow", "violet", "green"]

def draw_rect():
    # canvas.delete(ALL)
    x = random.randint(0, 600)
    y = random.randint(0, 500)
    w = random.randrange(100)
    h = random.randrange(100)
    canvas.create_rectangle(x, y ,w, h, outline=random.choice(color))

# for i in range(10):
#     draw_rect()

button = Button(window, text="사각형 그리기", width=20, height=3, command=draw_rect)
button.pack()

for i in range(10000):
    draw_rect()

window.mainloop()