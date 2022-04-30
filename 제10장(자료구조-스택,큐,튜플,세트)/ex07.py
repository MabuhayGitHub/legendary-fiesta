import math


def calcCircle(radius):
    area = math.pi * pow(radius, 2)
    circumstance = 2 * math.pi * radius
    return (area, circumstance)


if __name__ == "__main__":
    radius = float(input("원의 반지름: "))
    (area, circumstance) = calcCircle(radius)
    print("원둘레=", circumstance, "원넓이", area)
