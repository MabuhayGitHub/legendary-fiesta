# from collections import deque
# from collections import OrderedDict
# from collections import defaultdict
# from collections import Counter
# from collections import namedtuple

# deque: double-ended queue

# deque_list1 = deque()
# for i in range(5):
#     deque_list1.append(i)
# print(deque_list1)
# print(type(deque_list1))

# print(deque_list1.pop())
# print(deque_list1.pop())
# print(deque_list1.pop())
# print(deque_list1)

# # deque([0, 1, 2, 3, 4])
# # <class 'collections.deque'>
# # 4
# # 3
# # 2
# # deque([0, 1])

# deque_list2 = deque()
# for i in range(5):
#     deque_list2.appendleft(i)
# print(deque_list2)
# print(type(deque_list2))
# deque_list2.rotate(2)
# print(deque_list2)
# deque_list2.rotate(2)
# print(deque_list2)
# deque_list2.rotate(-2)
# print(deque_list2)
# print(deque(reversed(deque_list2)))
# # deque([4, 3, 2, 1, 0])
# # <class 'collections.deque'>
# # deque([1, 0, 4, 3, 2])
# # deque([3, 2, 1, 0, 4])
# # deque([1, 0, 4, 3, 2])
# # deque([2, 3, 4, 0, 1])

# deque_list3 = deque()
# for i in range(5):
#     deque_list3.append(i)
# print(deque_list3)

# deque_list3.extend([5, 6, 7])
# print(deque_list3)

# deque_list3.extendleft([5, 6, 7])
# print(deque_list3)

# # deque([0, 1, 2, 3, 4])
# # deque([0, 1, 2, 3, 4, 5, 6, 7])
# # deque([7, 6, 5, 0, 1, 2, 3, 4, 5, 6, 7])

# d = {}
# d["가"] = 100
# d["다"] = 500
# d["나"] = 200
# d["라"] = 300
# print(d)
# for k, v in d.items():
#     print(k, v)

# from collections import defaultdict
# d = defaultdict(lambda: 0)
# print(d["first"])
# print(d)

# from collections import defaultdict
# d = defaultdict(int)
# d["a"] += 10
# print(d)

# def countLetters(word):
#     counter = {}
#     for letter in word:
#         if letter not in counter:
#             counter[letter] = 0
#         counter[letter] += 1
#     return counter

# vs. 

# from collections import defaultdict
# def countLetters(word):
#     counter = defaultdict(int)
#     for letter in word:
#         counter[letter] += 1
#     return counter

# --------------------------------------------------------------------------

# a = ("John", 28, "남")
# b = ("Sally", 24, "여")
# for n in [a, b]:
#     print("%s은(는) %d 세의 %s성 입니다." %n)

# vs.

# import collections
# person = collections.namedtuple("person", "name age gender")
# p1 = person(name="Jhon",  age = 28, gender="남")
# p2 = person(name="Sally", age = 24, gender="여")
# for n in [p1, p2]:
#     print("%s은(는) %d 세의 %s성 입니다." %n)
# print(p1.name, p1.age, p1.gender)
# print(p2.name, p2.age, p2.gender)
# # Jhon은(는) 28 세의 남성 입니다.
# # Sally은(는) 24 세의 여성 입니다.
# # Jhon 28 남
# # Sally 24 여


# import collections
# person = collections.namedtuple("person", "name age gender")
# p1 = person(name="Jhon",  age = 28, gender="남")
# p2 = person(name="Sally", age = 24, gender="여")
# p3 = person._make({"Tom", 24, "남"})
# for n in [p1, p2]:
#     print("%s은(는) %d 세의 %s성 입니다." %n)
# print(p1.name, p1.age, p1.gender)
# print(p2.name, p2.age, p2.gender)
# print(p3.name, p3.age, p3.gender)
# # Jhon은(는) 28 세의 남성 입니다.
# # Sally은(는) 24 세의 여성 입니다.
# # Jhon 28 남
# # Sally 24 여
# # 24 Tom 남