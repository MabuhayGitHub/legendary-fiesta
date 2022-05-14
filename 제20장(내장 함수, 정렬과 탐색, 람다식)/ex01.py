# # abs()

# i = -20
# print(abs(i))

# i = -20.5
# print(abs(i))

# ----------------------------------------------------------

# # all()
# mylist = [1, 4, 7, 10]
# print(all(mylist))

# mylist = [1, 4, 7, 0]
# print(all(mylist))

# ----------------------------------------------------------

# # any()

# mylist = [1, 4, 7, 10]
# print(any(mylist))

# mylist = [1, 4, 7, 0]
# print(any(mylist))

# mylist = [0, 0, 0, 0]
# print(any(mylist))

# ----------------------------------------------------------

# # bin()

# b = 255
# print(bin(b))

# ----------------------------------------------------------

# # eval()

# # str = input("수식을 입력하세요: ")
# # print(eval(str))

# x = 10
# y = 15
# print(eval("x*y"))

# ----------------------------------------------------------

# # sum()

# print(sum([1, 10, 100, 1000]))

# ----------------------------------------------------------

# # len()

# print(len("1234"))
# print(len(["a", "b", "c", "d", "e"]))
# print(len("Hello World"))
# print(len((1, 2, 3, 4)))
# dic = {"a":7, "b":4}
# print(len(dic))

# ----------------------------------------------------------

# # list()

# s = "abcdefg"
# print(list(s))

# ----------------------------------------------------------

# # map()

# def square(x):
#     return x*x

# mylist = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# result = map(square, mylist)
# print(list(result))

# ----------------------------------------------------------

# # dir()

# mylist = [1, 2, 3]
# result = dir(mylist)
# for v in result:
#     print(v)

# ----------------------------------------------------------

# # max()
# # min()

# mylist = [1, 2, 3, 4, 5, 6]
# print(max(mylist))
# print(min(mylist))

# ----------------------------------------------------------

# # enumerate()

# seasons = ["봄", "여름", "가을", "겨울"]
# print(list(enumerate(seasons)))

# seasons = ["봄", "여름", "가을", "겨울"]
# print(list(enumerate(seasons, start=1)))

# ----------------------------------------------------------

# # filter()

# def myfilter(x):
#     return x > 3

# mylist = [1, 2, 3, 4, 5, 6, 7]
# result = filter(myfilter, mylist)
# print(list(result))

# ----------------------------------------------------------

# zip()

list1 = [1, 2, 3, 4, 5]
list2 = ["가", "나", "다", "라", "마"]
print(list(zip(list1, list2)))

# list1 = [1, 2, 3, 4]
# list2 = ["가", "나", "다", "라", "마"]
# print(list(zip(list1, list2)))

for i, j in zip(list1, list2):
    print(i, j)

# ----------------------------------------------------------