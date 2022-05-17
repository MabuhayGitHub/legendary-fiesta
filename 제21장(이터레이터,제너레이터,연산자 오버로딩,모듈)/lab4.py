import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    def __gt__(self, other):
        return self.radius > other.radius
    def __lt__(self, other):
        return self.radius < other.radius
    def __str__(self):
        return "원의 반지름: " + str(self.radius)

if __name__ == "__main__":
    c1 = Circle(4)
    c2 = Circle(5)
    print("c1의 반지름:", c1.radius)
    print("c2의 반지름:", c2.radius)
    c3 = c1 + c2
    print("c3의 반지름:", c3.radius)
    print(c3 > c2)
    print(c3 < c2)
    print("c3의 면적", c3.area())


