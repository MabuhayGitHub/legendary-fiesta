import turtle
import random

class Shape:
    
    myTurtle = None

    # 도형의 중심점
    cx = 0
    cy = 0

    # 기본 생성자
    def __init__(self):
        self.myTurtle = turtle.Turtle()
    
    # 펜 색상과 두께 임의 설정
    def setPen(self):
        r = random.random()
        g = random.random()
        b = random.random()
        print(r, g, b)
        self.myTurtle.pencolor((r, g, b)) # 펜의 색상
        penSize = random.randrange(1, 20) 
        self.myTurtle.pensize(penSize)    # 펜의 두께

    def drawShape(self):
        pass
