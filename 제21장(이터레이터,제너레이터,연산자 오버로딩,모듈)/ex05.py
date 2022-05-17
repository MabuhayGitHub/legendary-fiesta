# 연산자 오버로딩: 객체에서 필요한 연산자 재정의

# str1 = "안녕하세요."
# str2 = "반갑습니다."

# print(str1.__add__(str2))
# print(str1 + str2)

# print(type(str1))
# print(type(str2))

# -------------------------------------------------

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, other):
        print("__add__()")
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    def __str__(self):
        print("__str__()")
        return "Point(" + str(self.x) + "," + str(self.y) + ")"

p1 = Point(1,2)
p2 = Point(3,4)

print(p1 + p2)


