class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    def __str__(self):
        return "(%g, %g)" % (self.x, self.y)
    
if __name__ == "__main__":
    v1 = Vector2D(5, 2)
    v2 = Vector2D(5, 3)
    v3 = Vector2D(5, 4)
    result1 = v1 + v2
    print(result1.__str__())
    result2 = v1 - v2
    print(result2.__str__())
    result3 = v1 * v3
    print(result3.__str__())
    print(v1 == v2)
# (10, 5)
# (0, -1)
# (25, 8)
# False