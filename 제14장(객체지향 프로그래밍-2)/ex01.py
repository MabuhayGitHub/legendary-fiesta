class Rectangle:
    def __init__ (self, side = 0):
        self.side = side
    def getArea(self):
        return self.side * self.side

def printArea(rectangle, cnt):
    print("함수 내부 인스턴트 주소 ", id(rectangle))
    while cnt >= 1:
        print(rectangle.side, rectangle.getArea())
        cnt -= 1
        rectangle.side += 1

if __name__ == "__main__":
    rectangle = Rectangle()
    print("함수 외부 인스턴트 주소 ", id(rectangle))
    cnt = 5
    printArea(rectangle, 5)
    print(rectangle.side)
    print(cnt)

