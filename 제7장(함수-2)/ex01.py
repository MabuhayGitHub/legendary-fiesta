# def modify(n):
#     n = n + 1

# k = 10
# print("k = ", k)
# print(id(k))
# modify(k)
# print(id(k))
# print("k = ", k)
# print(id(k))

msg = "Happy"
print(msg)
print(id(msg))
msg = "BirthDay"
print(msg)
print(id(msg))

def modify2(li):
    li += [6, 7]

list = [1, 2, 3, 4, 5]
print(list)
print(id(list))
modify2(list)
print(list)
print(id(list))
