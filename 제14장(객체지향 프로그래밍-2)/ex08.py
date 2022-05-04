class Car:
    def __init__(self):
        self.speed = 0
        self.door = 0
    def upSpeed(self, speed):
        self.speed += speed
        print("부모클래스", self.speed)
        print("보모클래스", self.door)

class Sedan(Car):
    def __init__(self, speed, door):
        Car.__init__(self)
        self.speed = speed
        self.door = door
    def downSpeed(self, speed):
        self.speed -= speed
        print("자식클래스", self.speed)

if __name__ == "__main__":
    sedan = Sedan(80, 4)
    sedan.upSpeed(100)
    sedan.downSpeed(60)
    print(id(sedan))
    print()
    car = Car()
    car.upSpeed(50)
    print(id(car))