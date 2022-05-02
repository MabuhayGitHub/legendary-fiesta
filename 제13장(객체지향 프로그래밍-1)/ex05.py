import math

class circle:

    __radius = 0

    def __init__(self, radius):
        self.__radius = radius
    
    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius
    
    def calcArea(self):
        area = math.pi * self.__radius * self.__radius
        return area
    
    def calcCircum(self):
        value = 2 * math.pi * self.__radius
        return value

if __name__ == "__main__":
    circle1 = circle(10)
    print(circle1.getRadius())
    print(circle1.calcArea())
    print(circle1.calcCircum())

# 10
# 314.1592653589793
# 62.83185307179586