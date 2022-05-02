# 클래스 변수

class Car:
    # color = ""
    # speed = 0
    # 클래스 변수는 필드로 선언해야
    count = 0
    # 기본 생성자
    def __init__(self):
        self.color = "노랑"
        self.speed = 100
        Car.count += 1
    # 필드값 출력 메소드
    def __str__(self):
        print(self.color)
        print(self.speed)
        print(Car.count)

if __name__ == "__main__":
    print(Car.count)
    print(id(Car.count))
    car1 = Car()
    # car1.__str__()
    print(id(Car.count))
    car2 = Car()
    # car2.__str__()
    print(id(Car.count))

# 0
# 2074707820752
# 2074707820784
# 2074707820816