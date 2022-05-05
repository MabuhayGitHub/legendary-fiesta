from Unit import *

class Tank(Unit):
    mode = ""

    def move(self, x, y):
        self.x = x
        self.y = y
        print("Tank 위치", self.x, self.y, "이동")
    
    def siegeMode(self):
        self.mode = "시즈모드"
        print(self.mode)