from tkinter import *
from turtle import width

class Canvas_Shape:
    def __init__(self):
        window = Tk()
        window.title("여러 도형 그리기")
        self.canvas = Canvas(window, width=600, height=400, bg="white")
        self.canvas.pack()
        # frame = Frame(window, bg="black", width=600, height=100)
        frame = Frame(window)
        frame.pack()

        btnRectange = Button(frame, text="사각형", command=self.displayRect)
        btnOval = Button(frame, text="원 그리기", command=self.displayOval)
        btnArc = Button(frame, text="호 그리기", command=self.displayArc)
        btnPolygon = Button(frame, text="다각형 그리기", command=self.displayPolygon)
        btnLine = Button(frame, text="라인 그리기", command=self.displayLine)
        btnString = Button(frame, text="문자열", command=self.displayString)
        btnClear = Button(frame, text="전체 삭제", command=self.clearCanvas)

        btnRectange.grid(row=1, column=1)
        btnOval.grid(row=1, column=2)
        btnArc.grid(row=1, column=3)
        btnPolygon.grid(row=1, column=4)
        btnLine.grid(row=1, column=5)
        btnString.grid(row=1, column=6)
        btnClear.grid(row=1, column=7)

        window.mainloop()
    
    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")
    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill="red", tags="oval")
    def displayArc(self):
        self.canvas.create_arc(10, 10, 190, 90, start=0, extent=90, fill="red", tags="arc")
    def displayPolygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50, fill="blue", tags="polygon")
    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, fill="blue", tags="line", width=9, arrow="last", activefill="black")
        self.canvas.create_line(10, 90, 190, 10, fill="blue", tags="line", width=9, arrow="last", activefill="black")
    def displayString(self):
        self.canvas.create_text(60, 20, text="반갑습니다", font=("times 10 bold underline"), tags="string")
    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")

if __name__ == "__main__":
    Canvas_Shape()