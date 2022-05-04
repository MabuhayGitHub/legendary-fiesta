class Car:
    speed = 0
    def upSpeed(self, speed):
        self.speed += speed
        print("현재 속도(조상클래스)", self.speed)
    def __downSpeed(self, speed):
        self.speed -= speed
        print("현재 속도(조상클래스)", self.speed)

class Sedan(Car):
    def upSpeed(self, speed):
        self.speed =+ speed
        if self.speed > 150:
            self.speed = 150
            print("150 초과 불가")
        print("현재 속도(자손클래스)", self.speed)
    def __downSpeed(self, speed):
        self.speed -= speed
        print("현재 속도(자손클래스)", self.speed)
    def private(self):
        self.__downSpeed(100)

class Truck(Car):
    pass

if __name__ == "__main__":
    sedan1 = None
    truck1 = None
    sedan1 = Sedan()
    truck1 = Truck()
    print("승용차의 속도: ", end=" ")
    sedan1.upSpeed(200)
    print("트럭의 속도: ", end=" ")
    truck1.upSpeed(200)

    sedan1.private()