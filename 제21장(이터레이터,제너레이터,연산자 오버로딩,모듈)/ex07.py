# list1 = [1, 2, 3, 4, 5]
# print(id(list1))
# list2 = list1
# print(id(list2))

# # --------------------------------------------

# import copy

# list1 = [1, 2, 3, 4, 5]
# print(id(list1))
# list2 = copy.deepcopy(list1)
# print(id(list2))

# # --------------------------------------------

# import copy
# colors = ["red", "blue", "green"]
# clone = copy.deepcopy(colors)
# clone[0] = "white"
# print(colors)
# print(clone)

# --------------------------------------------

# import random

# # randint() 정수 범위의 난수
# print(random.randint(1, 6))
# print(random.randint(1, 6))
# print(random.randint(1, 6))

# # random() 0~1.0미만 범위의 난수
# print(random.random())
# print(random.random())
# print(random.random())

# # randrange() 시작, 종료 범위의 난수. step은 옵션

# print(random.randrange(0, 101))
# print(random.randrange(0, 101, 2))
# print(random.randrange(0, 101, 4))
# print(random.randrange(0, 101, 8))
# print(random.randrange(0, 101, 16))
# print(random.randrange(0, 101, 32))
# print(random.randrange(0, 101, 64))

# # choice() 랜덤 선택

# list1 = ["신은혁", "김연아", "손연재", "추신수"]
# print(random.choice(list1))

# # shuffle() 랜덤하게 섞기
# list2 = [[x] for x in range(10)]
# print(list2)
# random.shuffle(list2)
# print(list2)

# # --------------------------------------------

# import sys

# print(sys.prefix)
# print(sys.path)
# print(sys.version)

# # --------------------------------------------

# import time
# print(time.time())

# # import fibo
# # start = time.time()
# # fibo.fib_num(1000000)
# # end = time.time()
# # print(end-start)

# print(time.asctime())

# for i in range(10, 0, -1):
#     print(i, end=" ")
#     time.sleep(1)
# print("FIRE")

# # --------------------------------------------

import calendar
print(calendar.month(2022, 5))