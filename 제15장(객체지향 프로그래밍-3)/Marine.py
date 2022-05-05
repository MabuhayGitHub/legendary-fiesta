from Unit import *

class Marine(Unit):
    mode = ""

    def move(self, x, y):
        self.x = x
        self.y = y
        print("Marine 위치", self.x, self.y, "이동")
    
    def stimPack(self):
        self.mode = "공격 모드(스팀팩)"
        print(self.mode)