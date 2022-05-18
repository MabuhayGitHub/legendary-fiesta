from enum import auto
import warnings
warnings.filterwarnings(action="ignore")

import threading
import time

class AutoSaveThread(threading.Thread):
    def __init__(self):
        super().__init__()
    def save(self):
        print("작업 내용 저장")
    def run(self):
        while True:
            time.sleep(1)
            self.save()

if __name__ == "__main__":
    autoSaveThread = AutoSaveThread()
    # print("AutoSaveThread 데몬?", autoSaveThread.isDaemon())
    autoSaveThread.daemon = True
    # print("AutoSaveThread 데몬?", autoSaveThread.isDaemon())
    autoSaveThread.start()
    time.sleep(5)
    print("메인 스레드 종료됨")