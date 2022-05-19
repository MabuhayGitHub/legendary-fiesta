# 파이썬 최신 버전(3.10)에서 해결된 것으로 보임
# Lock 클래스
# Lock.aquire() : 잠금
# Lock.release() : 잠금 해제

import warnings
warnings.filterwarnings(action="ignore")

import threading

totalCount = 0

class CounterThread(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        global totalCount
        for _ in range(25000000):
            totalCount += 1
        print(threading.currentThread().getName(), "스레드 25000000 연산 종료")

if __name__ == "__main__":
    for _ in range(4):
        counterThread = CounterThread()
        counterThread.start()
    print("모든 스레드 종료까지 대기")
    
    mainThread = threading.currentThread()

    # print("현재 Active한 스레드 ", threading.enumerate())
    for thread in threading.enumerate():
        if thread is not mainThread:
            thread.join()
    
    totalCount = format(totalCount, ",")
    print("totalCount=", totalCount)
