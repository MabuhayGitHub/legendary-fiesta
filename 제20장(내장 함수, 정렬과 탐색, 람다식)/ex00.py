# # def myfilter(x):
# #     return x > 3

# # result = filter(myfilter, (1,2,3,4,5,6))
# # print(list(result))

# n = [1, 2, 3, 4]
# s = ["One", "Two", "Three", "Four"]
# print(list(zip(n, s)))

names = ["Kim", "Lee", "Park"]
scores = [100, 90, 80]
for n, s in zip(names, scores):
    print(n, s)