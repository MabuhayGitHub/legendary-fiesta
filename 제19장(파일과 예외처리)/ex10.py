import os


# dir = os.getcwd()
# print("현재 디렉토리: ", dir)
# print()


# for filename in os.listdir():
#     print(filename)
# print()


# for filename in os.listdir():
#     if os.path.isfile(filename):
#         print(filename)
# print()


files = os.listdir()
for name in files:
    if os.path.isfile(name):
        if name.endswith(".py"):
            print(name)