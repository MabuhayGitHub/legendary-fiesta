# 동기화
# Calculator.py 
# User1.py
# User2.py
# CalculatorMain.py 


import warnings
warnings.filterwarnings(action="ignore")

# 공유 객체 생성
import threading
import time

lock = threading.Lock()

class Calculator():
    # 생성자
    def __init__(self, memory):
        super().__init__()
        self.memory = memory
    # getter()
    def getMemory(self):
        return self.memory
    # setter()
    def setMemory(self, memory):
        lock.acquire()
        self.memory = memory
        time.sleep(1)
        print(threading.currentThread().getName() + " : "  + str(self.memory))
        lock.release()