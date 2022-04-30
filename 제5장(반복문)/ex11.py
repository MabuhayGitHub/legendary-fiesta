# 코드 실행 이후 디스플레이 연결에 문제가 있는 것으로 보임

import turtle

t = turtle.Pen()

for i in range(72):
    t.left(5)

    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)

turtle.exitonclick()