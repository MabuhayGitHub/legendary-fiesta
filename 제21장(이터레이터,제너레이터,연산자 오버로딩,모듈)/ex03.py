# def MyCounterGen(low, high):
#     while low <= high:
#         yield low
#         low += 1

# if __name__ == "__main__":
#     for n in MyCounterGen(1, 10):
#         print(n, end=" ")

import time
def gen(count):
    start = 1
    while start <= count:
        yield start
        time.sleep(2)
        print("while 구문 내 start 값", start)
        start += 1
if __name__ == "__main__":
    for n in gen(3):
        print("for 구문 내", n, end=" ")