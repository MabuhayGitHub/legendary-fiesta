# 클래스
#   멤버변수(필드, 속성)
#   멤버메소드(기능)
#   생성자(필수)

class Car:
    color = ""
    speed = 0

    def upSpeed(self, speed):
        if speed < 0:
            print("속도가 음수입니다")
            return
        self.speed = speed
    def downSpeed(self, speed):
        if speed < 0:
            print("속도가 음수입니다")
            return
        self.speed = speed
        
    def printFields(self, myCar):
        print("%s 색상: %s, 속도: %d km/h" %(myCar, self.color, self.speed))

if __name__ == "__main__":
    myCar1 = Car()
    myCar2 = Car()
    myCar3 = Car()
    print(type(myCar1), id(myCar1))
    print(type(myCar2), id(myCar2))
    print(type(myCar3), id(myCar3))

    myCar1.color = "BLUE"
    myCar1.upSpeed(50)
    myCar1.printFields("myCar1")
    
    myCar2.color = "YELLOW"
    myCar2.upSpeed(60)
    myCar2.printFields("myCar2")
    
    myCar3.color = "RED"
    myCar3.upSpeed(-60)
    myCar3.downSpeed(60)
    myCar3.printFields("myCar3")