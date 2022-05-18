# import threading
# import time

# class Worker(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name    # thread 이름 지정
#     def run(self):
#         print(" sub thread start", threading.current_thread().getName)
#         time.sleep(3)
#         print(" sub thread end", threading.current_thread().getName)

# print("main thread start")
# for i in range(5):
#     name = "thread {}".format(i)
#     # print(name)
#     t = Worker(name)
#     t.start()
# print("main thread end")


# # main thread start
# # sub thread start <bound method Thread.getName of <Worker(thread 0, started 10236)>>
# # sub thread start <bound method Thread.getName of <Worker(thread 1, started 19356)>> 
# # sub thread start <bound method Thread.getName of <Worker(thread 2, started 22808)>> 
# # sub thread start <bound method Thread.getName of <Worker(thread 3, started 10804)>> 
# # sub thread start <bound method Thread.getName of <Worker(thread 4, started 11724)>> 
# # main thread end 
# # sub thread end <bound method Thread.getName of <Worker(thread 1, started 19356)>> 
# # sub thread end <bound method Thread.getName of <Worker(thread 2, started 22808)>>
# # sub thread end <bound method Thread.getName of <Worker(thread 0, started 10236)>>
# # sub thread end <bound method Thread.getName of <Worker(thread 4, started 11724)>>
# # sub thread end <bound method Thread.getName of <Worker(thread 3, started 10804)>>


import threading
import time

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name    # thread 이름 지정
    def run(self):
        print(" sub thread start", (threading.current_thread().getName()))
        time.sleep(3)
        print(" sub thread end", threading.current_thread().getName())

print("main thread start")
t1 = Worker("1")
t1.start()
t2 = Worker("2")
t2.start()
t1.join()
t2.join()

print("main thread post job")
print("main thread end")
