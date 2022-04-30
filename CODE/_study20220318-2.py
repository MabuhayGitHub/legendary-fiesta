from turtle import *

speed(10)
up()
goto(-140,140)

for i in range(16):
    write(i, align='center')
    right(90)
    fd(10)
    down()
    fd(150)
    up()
    bk(160)
    left(90)
    fd(20)
    
finish_line =xcor() - 20
print(finish_line)
