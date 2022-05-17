# yield from 사용

import time

def gen():
    list1 = [10, 20, 30]
    yield from list1
    # time.sleep(2)
    # print("gen() 내 요소", list1)

if __name__ =="__main__":
    test_gen = gen()
    n = next(test_gen)
    print("main() 내 요소 값", n)
    n = next(test_gen)
    print("main() 내 요소 값", n)
    n = next(test_gen)
    print("main() 내 요소 값", n)
    n = next(test_gen)  # StopIteration 발생
    print("main() 내 요소 값", n)