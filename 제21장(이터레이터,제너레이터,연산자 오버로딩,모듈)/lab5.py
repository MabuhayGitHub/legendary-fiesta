
class Figure(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Quadangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __add__(self, other):
        return Quadangle(self.width + other.width, self.height+other.height)

quad = Quadangle(2, 3)
figure = Figure(3, 4)

print("너비의 합: ", quad.width + figure.width)
print("높이의 합: ", quad.height + figure.height)

print("너비의 합: ", figure.width + quad.width)
print("높이의 합: ", figure.height + quad.height)