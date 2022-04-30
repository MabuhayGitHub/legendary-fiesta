from collections import deque
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

from collections import defaultdict
d = defaultdict(int)
d["a"] += 10
print(d)