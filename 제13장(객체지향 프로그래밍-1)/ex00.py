class car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value
    
    def downSpeed(self, value):
        self.speed -= value

myCar1 = car()
myCar1.color = "RED"
myCar1.speed = 0

myCar2 = car()
myCar2.color = "BLUE"
myCar2.speed = 0

myCar3 = car()
myCar3.color = "YELLOW"
myCar3.speed = 0

myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 시속 %dkm입니다" % (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s이며, 현재 속도는 시속 %dkm입니다" % (myCar2.color, myCar2.speed))

myCar1.upSpeed(0)
print("자동차3의 색상은 %s이며, 현재 속도는 시속 %dkm입니다" % (myCar3.color, myCar3.speed))
