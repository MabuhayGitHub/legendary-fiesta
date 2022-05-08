from tkinter import *

window =Tk()

canvas = Canvas(window, width=500, height=500, bg="white")
canvas.pack()

line1 = canvas.create_line(0, 0, 500, 500, fill="blue")
line2 = canvas.create_line(0, 500, 500, 0, fill="red", width=5)

# 좌표 변경
canvas.coords(line1, 250, 250, 500, 500)
canvas.itemconfig(line2, fill="orange")

rect1 = canvas.create_rectangle(50, 50, 200, 200, fill="yellow")
rect2 = canvas.create_rectangle(200, 200, 300, 400, fill="red", outline="blue", width=10)

# 삭제
canvas.delete(rect1)
canvas.delete(ALL)

# 사각형에 내접한 부채꼴
canvas.create_arc(10, 10, 300, 300, extent=90, fill="red", outline="yellow", width=5)

# 타원
canvas.create_oval(50, 50, 250, 350)

# 다각형
canvas.create_polygon(10, 10, 150, 110, 250, 20, fill="blue")

# 텍스트
canvas.create_text(100, 350, text="안녕하세요", font=("고딕 15 bold"))

window.mainloop()