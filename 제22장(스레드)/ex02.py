import threading
import time

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print("작업 스레드 시작: ", threading.current_thread().name)
        time.sleep(5)
        print("작업 스레드 종료: ", threading.current_thread().name)

if __name__ == "__main__":
    print("메인 스레드 시작")
    t1 = Worker("1")
    t1.start()
    t2 = Worker("2")
    t2.start()
    t3 = Worker("3")
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print("메인 스레드 종료")