from Shape import *

class Rectangle(Shape):
    width = 0
    height = 0

    def __init__(self, cx, cy):
        Shape.__init__(self)
        self.cx = cx
        self.cy = cy
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)
        print(self.width, self.height)

    def drawShape(self):
        # 좌측 상단 좌표
        sx1 = 0
        sy1 = 0
        # 우측 하단 좌표
        sx2 = 0
        sy2 = 0
        # 사각형 네 점의 좌표
        sx1 = self.cx - self.width  / 2
        sy1 = self.cy - self.height / 2
        sx2 = self.cx + self.width  / 2
        sy2 = self.cy + self.height / 2
        print(sx1, sy1, sx2, sy2)
        # 펜의 색상과 두께
        self.setPen()
        # 사각형 그리기
        self.myTurtle.penup()
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.pendown()
        self.myTurtle.goto(sx1, sy2)
        self.myTurtle.goto(sx2, sy2)
        self.myTurtle.goto(sx2, sy1)
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.penup()
