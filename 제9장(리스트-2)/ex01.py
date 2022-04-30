# shallow copy

# from copy import deepcopy

# scores = [10, 20, 30, 40, 50]
# values = scores

# # print(id(scores))
# # print(id(values))

# values[2] = 33

# for element in scores:
#     print(element, end=" ")

# result
# 10 20 33 40 50

##############################################################################

# deep copy

# method 1: list()

# scores = [10, 20, 30, 40, 50]
# values = list(scores)

# print(id(scores))
# print(id(values))

# values[2] = 33

# for element in scores:
#     print(element, end=" ")
# print()
# for element in values:
#     print(element, end=" ")


# method 2: deepcopy() or copy()

# scores = [10, 20, 30, 40, 50]
# values = deepcopy(scores)

# print(id(scores))
# print(id(values))

# values[2] = 33

# for element in scores:
#     print(element, end=" ")
# print()
# for element in values:
#     print(element, end=" ")

# method 3: [:]

# scores = [10, 20, 30, 40, 50]
# values = scores[:]

# print(id(scores))
# print(id(values))

# values[2] = 33

# for element in scores:
#     print(element, end=" ")
# print()
# for element in values:
#     print(element, end=" ")

# Call-by-Value
# Call-by-Reference

# def func1(x):
#     print("x=", id(x))
#     x = 42
#     print("x=", id(x))

# y = 10
# print("y=", id(y))
# func1(y)
# print("y=", id(y))

# def func2(list):
#     print(id(list))
#     list[0] = 99
#     print(id(list))

# values = [0, 1, 1, 2, 3, 5, 8]
# print(id(list))
# print(values)
# func2(values)
# print(id(list))
# print(values)

# list1 = [ i * j for i in range(2, 10) for j in range(1, 10)]
# print(list1)

# list1 = [ i * j for i in range(2, 10) 
#                 for j in range(1, 10)]
# print(list1)

# list1 = ["Korea", "한국", "대한민국"]
# first_word = [word[0] for word in list1]
# print(first_word)

# list1 = ["Korea", "한국", "대한민국"]
# first_word = [word[len(word)-1] for word in list1]
# print(first_word)

list1 = [x for x in range(1, 10)]
list2 = [x for x in range(1, 10)]
list3 = [x*y for x in list1
             for y in list2]
print(list3)