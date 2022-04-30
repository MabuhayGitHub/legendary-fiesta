import time

queue = []

for i in range(1, 11,1):
    queue.append(i)
    print(queue)
    time.sleep(1)

for _ in range(len(queue)):
    queue.pop(0)
    print(queue)
    time.sleep(1)