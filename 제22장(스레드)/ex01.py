import threading
import time

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print("작업 스레드 시작: ", threading.current_thread())
        time.sleep(3)
        print("작업 스레드 종료: ", threading.current_thread())

if __name__ == "__main__":
    print("메인 스레드 시작")
    for i in range(5):
        name = "스레드 {}".format(i)
        t = Worker(name)    # 작업 스레드 생성
        t.start()           # 구현되어 있는 run() 호출
    print("메인 스레드 종료")
    
