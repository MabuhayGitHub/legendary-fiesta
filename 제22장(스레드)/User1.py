# Calculator 공유 객체에 접근하는 스레드 클래스

from Calculator import *

class User1(threading.Thread):
    def __init__(self):
        super().__init__()
    def setCalculator(self, calculator):
        self.calculator = calculator
        self.setName("User-1")
    def run(self):
        self.calculator.setMemory(100)