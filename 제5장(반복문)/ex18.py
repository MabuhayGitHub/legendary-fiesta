# for i in range(5):
#     for j in range(10):
#         print("*", end="")
#     print("")

# for i in range(1,6):
#     print("*"*i)

# for i in range(5):
#     for j in range(i+1):
#         print("*", end="")
#     print("")

# print("정숫값: {}, string: {}, float: {}".format(10,"안녕", 3.14))
# print("정숫값: {0}, string: {1}, float: {2}".format(10,"안녕", 3.14))
# print("정숫값: {2}, string: {1}, float: {0}".format(10,"안녕", 3.14))

# print("숫자 '{:>5d}'".format(300))
# print("숫자 '{:<5d}'".format(300))

# for i in range(5):
#     print("{:<5}".format("*" * (i+1)))

# for i in range(5):
#     print("{:>5}".format("*" * (i+1)))

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print("")

for i in range(6, 0, -1):
        print("{:<05}".format("*" * (i-1)))

for i in range(6, 0, -1):
        print("{:>05}".format("*" * (i-1)))