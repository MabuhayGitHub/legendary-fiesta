import warnings
warnings.filterwarnings(action="ignore")

import threading
import time

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print("작업 스레드 시작: ", threading.currentThread().getName())
        time.sleep(3)
        print("작업 스레드 종료: ", threading.currentThread().getName())

if __name__ == "__main__":
    print("메인 스레드 시작")
    for i in range(5):
        name = str(i)
        thread = Worker(name)
        print("thread 데몬 여부: ", thread.isDaemon())
        thread.daemon = True
        print("thread 데몬 여부: ", thread.isDaemon())
        thread.start()
    print("메인 스레드 종료")
