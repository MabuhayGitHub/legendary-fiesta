class Circle:
    def __init__(self, radius = 0):
        self.radius = radius
    def __eq__(self, other):
        return self.radius == other.radius
    def __add__(self, other):
        return self.radius + other.radius

if __name__ =="__main__":
    circle1 = Circle(10)
    circle2 = Circle(10)
    if circle1 == circle2:
        print("원의 반지름이 같습니다.")
