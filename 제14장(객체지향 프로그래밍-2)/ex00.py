# from cgi import print_arguments
# from string import printable


# class Rectangle:
#     def __init__(self, side=0):
#         self.side = side
#     def getArea(self):
#         return self.side * self.side

# def printAreas(r, n):
#     while n >= 1:
#         print(r.side, "\t", r.getArea())
#         r.side = r.side + 1
#         n -= 1

# myRect = Rectangle()
# count = 5
# printAreas(myRect, count)
# print(myRect.side)
# print(count)
# # 0        0
# # 1        1
# # 2        4
# # 3        9
# # 4        16
# # 5
# # 5

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return "(%g, %g)" % (self.x, self.y)

u = Vector2D(0, 1)
v = Vector2D(1, 0)
w = Vector2D(1, 1)
a = u + v
print(a)
# (1, 1)