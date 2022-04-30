import turtle

t = turtle.Pen()

while True:
    direction = input("왼쪽=left, 오른쪽=right, 종료=quit 입력하세요.")

    if direction == "quit":
        print("종료")
        break
    if direction == "left":
        t.left(60)
        t.forward(50)
    if direction == "right":
        t.right(60)
        t.forward(50)

turtle.exitonclick()