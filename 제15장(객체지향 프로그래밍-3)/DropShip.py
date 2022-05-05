from Unit import *

class DropShip(Unit):
    mode = ""

    def move(self, x, y):
        self.x = x
        self.y = y
        print("DropShip 위치", self.x, self.y, "이동")
    
    def load(self):
        self.mode = "유닛 탑승"
        print(self.mode)

    def unload(self):
        self.mode = "유닛 하강"
        print(self.mode)