import time

def inf_sequence():
    num = 0
    while True:
        yield num
        time.sleep(0.01)
        num += 1

if __name__ == "__main__":
    for n in inf_sequence():
        print(n, end=" ")