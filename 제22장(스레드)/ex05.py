# 파이썬 최신 버전(3.10)에서 해결된 것으로 보임
# Lock 클래스
# Lock.aquire() : 잠금
# Lock.release() : 잠금 해제

import warnings
warnings.filterwarnings(action="ignore")

import threading

totalCount = None

class ThreadVariable():
    def __init__(self):
        self.lock = threading.Lock()    # Lock클래스 인스턴스 생성
        self.lockValue = 0
    def plus(self, value):
        self.lock.acquire()     # 타 스레드 접근 차단
        self.lockValue += 1
        self.lock.release()     # 타 스레드 접근 해제

class CounterThread(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        global totalCount
        for _ in range(250000):
            totalCount.plus(1)
        print("250000 연산 종료")

if __name__ == "__main__":
    totalCount = ThreadVariable()
    for _ in range(4):
        lockThread = CounterThread()
        lockThread.start()
    print("모든 스레드 종료까지 대기")
    
    mainThread = threading.currentThread()

    # print("현재 Active한 스레드 ", threading.enumerate())
    for thread in threading.enumerate():
        if thread is not mainThread:
            thread.join()
    
    total = format(totalCount.lockValue, ",")
    print("누적값(totalCount.lockValue)", total)
