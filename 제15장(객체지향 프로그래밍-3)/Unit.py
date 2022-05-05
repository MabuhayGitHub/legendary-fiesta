from abc import *

class Unit(metaclass=ABCMeta):
    x = 0
    y = 0
    name = ""

    @abstractmethod
    def move(self, x, y):
        pass

    def stop(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name
        print(self.name, "(멈춤) 현재 위치", self.x, self.y)