# deque : Queue + Stack

from collections import deque

# deque_list = deque()
# print(deque_list)
# # deque([])

# for i in range(5):
#     deque_list.append(i)
# print(deque_list)
# # deque([0, 1, 2, 3, 4])

# print(deque_list.pop())
# # 4
# print(deque_list)
# # deque([0, 1, 2, 3])

# print(deque_list.pop())
# # 3
# print(deque_list)
# # deque([0, 1, 2]

# deque_list.clear()
# for i in range(5):
#     deque_list.appendleft(i)
#     print(deque_list)
#     # deque([0])
#     # deque([1, 0])
#     # deque([2, 1, 0])
#     # deque([3, 2, 1, 0])
#     # deque([4, 3, 2, 1, 0])

# print(deque_list)
# # deque([4, 3, 2, 1, 0])

# print(deque_list.pop())
# # 0
# print(deque_list.pop())
# # 1
# print(deque_list.pop())
# # 2
# print(deque_list)
# # deque([4, 3])


deque_list = deque()
for i in range(5):
    deque_list.appendleft(i)
print(deque_list)
# deque([4, 3, 2, 1, 0])

deque_list.rotate(1)
print(deque_list)
# deque([0, 4, 3, 2, 1])

deque_list.rotate(-1)
print(deque_list)
# deque([4, 3, 2, 1, 0])

print(deque(reversed(deque_list)))
# deque([0, 1, 2, 3, 4])

print(deque_list)
# deque([4, 3, 2, 1, 0])
deque_list.extend([5, 6, 7])
print(deque_list)
# deque([4, 3, 2, 1, 0, 5, 6, 7])
deque_list.extendleft([5, 6, 7])
print(deque_list)
# deque([7, 6, 5, 4, 3, 2, 1, 0, 5, 6, 7])

deque_list.clear()
basedata = ["a", "b", "c", "d", "e"]
deque_list = deque(basedata, maxlen=3)
print(deque_list)
print(deque_list.popleft())
print(deque_list)
