for i in [1, 2, 3, 4]:
    print(i, end=" ")
print()
for c in "python":
    print(c, end=" ")

# -----------------------------------------------
class MyCounter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            # print(self.current)
            self.current += 1
            return self.current - 1

c = MyCounter(1, 10)
for i in c:
    print(i, end=" ")
print()

# -----------------------------------------------

def MyCounterGen(low, high):
    while low <= high:
        yield low
        low += 1

for i in MyCounterGen(1, 10):
    print(i, end=" ")
print()

# -----------------------------------------------

import time

def gen(count):
    start = 1
    while start <= count:
        yield start
        time.sleep(1)
        start += 1

for i in gen(10):
    print(i, end=" ")