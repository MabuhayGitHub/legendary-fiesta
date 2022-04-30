# colors = ("red", "blue", 'green')
# print(type(colors))
# print(colors)

# numbers = (1, 2, 3, 4, 5)
# print(type(numbers))
# print(numbers)

# tuple1 = (1, 1.2, "hi")
# print(type(tuple1))
# print(tuple1)

# tuple2 = ()
# print(type(tuple2))
# print(tuple2)

# tuple3 = (10)
# print(type(tuple3))
# print(tuple3)

# tuple3 = (10,)
# print(type(tuple3))
# print(tuple3)

# li1 = [1, 2, 3, 4, 5]
# tu1 = tuple(li1)
# print(tu1)

# t1 = (1, 2, 3)
# print(id(t1))
# t2 = t1, (4,)
# print(id(t2))
# print(id(t2[0]))
# print(id(t2[1]))

# t1 = (1, 2, 3)
# t2 = (4,)
# t3 = t1, t2
# print(id(t1))
# print(id(t2))
# print(id(t3))
# print(id(t3[0]))
# print(id(t3[1]))

# t4 = (1, 2, 3, 4, 5)
# t5 = (6, 7, 8, 9)
# print(len(t4))
# print(max(t4))
# print(min(t4))

# t6 = t4 + t5
# t7 = t4, t5
# print(t6, t7)

# t4 = (1, 2, 3, 4, 5)
# t5 = (6, 7, 8, 9)
# t8 = t4 * 2
# print(t8)
# if 5 in t5:
#     print("있음")

# tp1 = (1, 2, 3, "안녕", "철수", 5.5)
# for i in range(len(tp1)):
#     print(tp1[i])
# print(tp1[4:6])

c1 = (1, 2, 3)
c2 = (1, 2, 3)
print(dir(c1))
print(c1.__eq__(c2))
