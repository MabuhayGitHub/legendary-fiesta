import copy

# deep copy

# method 1: list()

# scores = [10, 20, 30, 40, 50]
# values = list(scores)

# print(id(scores))
# print(id(values))

# values[2] = 33

# print(scores)
# print(values)


# method 2: deepcopy() or copy()

# scores = [10, 20, 30, 40, 50]
# values = deepcopy(scores)

# print(id(scores))
# print(id(values))

# values[2] = 33

# print(scores)
# print(values)

# scores = [10, 20, 30, 40, 50]
# values = copy.copy(scores)

# print(id(scores))
# print(id(values))

# values[2] = 33

# print(scores)
# print(values)


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
