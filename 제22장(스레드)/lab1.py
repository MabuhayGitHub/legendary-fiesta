import warnings
warnings.filterwarnings(action="ignore")

import winsound
import time
import threading

# fr = 2000   # 주파수(37~32767)
# du = 1000   # 지속 시간(ms)
# for i in range(3):
#     winsound.Beep(fr, du)
#     time.sleep(1)


# 싱글 스레드 환경
# print("현재 실행 중인 스레드: ", threading.currentThread().getName())
# fr = 2000   # 주파수(37~32767)
# du = 1000   # 지속 시간(ms)
# for i in range(3):
#     print("현재 실행 중인 스레드(첫번째 for문): ", threading.currentThread().getName())
#     winsound.Beep(fr, du)
#     time.sleep(1)
# for i in range(3):
#     print("현재 실행 중인 스레드(두번째 for문): ", threading.currentThread().getName())
#     print("삐~~~~~~~~")
#     time.sleep(1)

# 멀티 스레드 환경
class BeepThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print(threading.currentThread().getName())
        fr = 2000
        du = 1000
        for i in range(3):
            winsound.Beep(fr, du)
            time.sleep(1)

if __name__ == "__main__":
    thread = BeepThread("Beep Thread ")
    thread.start()
    print(threading.currentThread().getName())
    for i in range(3):
        print("삐~~~~~~~~~~~~~~~~~~")
        time.sleep(2)
    # thread.start()  # RuntimeError: threads can only be started once