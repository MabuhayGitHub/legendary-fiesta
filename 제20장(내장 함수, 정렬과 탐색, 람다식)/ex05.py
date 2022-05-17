# map()

list1 = [1, 2, 3, 4, 5]
f = lambda x : x * 2
result = map(f, list1)
# result = map(lambda x : x * 2, list1)
print(list(result))

# filer()

list2 = [1, 2, 3, 4, 5, 6, 7]
result = filter(lambda x : x % 2 ==0, list2)
print(list(result))

# 키 지정

data = [(1, 100), (1, 200), (2, 200), (1, 300)]
print(sorted(data, key=lambda data:data[0]))

# reduce(func, seq)

import functools
result = functools.reduce(lambda x, y : x + y, [1, 2, 3, 4])
print(result)