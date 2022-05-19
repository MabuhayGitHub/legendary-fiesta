import warnings
warnings.filterwarnings(action="ignore")

# Account 클래스

import threading, time
# import time

lock = threading.Lock()

class Account(threading.Thread):
    def __init__(self, balance):
        super().__init__()
        self.balance = balance
    # 잔액 조회
    def getBalance(self):
        time.sleep(1)
        return self.balance
    # 입금 처리
    def setBalance(self, balance):
        lock.acquire()
        self.balance = balance
        time.sleep(2)
        print(threading.currentThread().getName(), "(이/가) 입금 : ", self.balance, "원")
        lock.release()
    # 출금 처리
    def WithDraw(self, money):
        lock.acquire()
        if self.balance >= money:
            time.sleep(1)
            self.balance -= money
            print(threading.currentThread().getName(), "(이/가) 출금 : ", money, "원")
            print("잔액 :" , self.getBalance(), "원")
        else:
            try:
                print(threading.currentThread().getName(), "(이/가)", money, "원 출금 시도")
                raise Exception()
            except Exception:
                print("잔액 부족")
        lock.release()
