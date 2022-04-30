# i = 0
# while i < 11:
#     print(i)
#     i+=1

# i = 1
# sum = 0
# while i < 11:
#     sum += i
#     i += 1
# print(sum)


# i  = 1
# fac = 1

# while i <= 5:
#     fac *= i
#     i += 1
# print(fac)


# i = 1
# while i <= 9:
#     print("3 * %d = %2d" % (i, 3*i))
#     i += 1


# i = 1
# sum = 0
# while i <= 100:
#     if i % 3 == 0:
#         sum += i
#     i += 1
# print(sum)

num = 1234567890
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print(sum)