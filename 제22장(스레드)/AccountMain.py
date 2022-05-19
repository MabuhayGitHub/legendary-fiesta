# 실행 파일

# from Account import *
from WithDrawThread1 import *
from WithDrawThread2 import *

if __name__ == "__main__":

    account = Account(0)

    thread1 = WithDrawThread1(account)
    thread2 = WithDrawThread2(account)

    thread1.setAccount(account)
    thread2.setAccount(account)

    thread1.start()
    thread2.start()