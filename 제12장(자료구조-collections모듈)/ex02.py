from collections import deque
import time

deque_test = deque()
start = time.time()     # 시작 시간 저장(초)
for i in range(10000000):
    deque_test.append(i)
end = time.time()       # 종료 시간 저장(초)
print("deque append", end - start)

list_test = list()
start = time.time()     # 시작 시간 저장(초)
for i in range(10000000):
    list_test.append(i)
end = time.time()       # 종료 시간 저장(초)
print("list append", end - start)