# data = []
# fp = open("C:\\Python\\Inflearn\\python\\제9장(리스트-2)\\data.txt", mode = "r", encoding="UTF-8")
# # print(type(fp))

# for line in fp.readlines():
#     print(line.strip())
#     data.append(line.strip())

# fp.close()

# print(data)



# fp = open("C:\\Python\\Inflearn\\python\\제9장(리스트-2)\\data.txt", mode = "w", encoding="UTF-8")

# fp.write("1. 우리는 파이썬을 공부합니다\n")
# fp.write("2. 우리는 파이썬을 공부합니다\n")
# fp.write("3. 우리는 파이썬을 공부합니다\n")
# fp.write("4. 우리는 파이썬을 공부합니다\n")

# fp.close()


# fp = open("C:\\Python\\Inflearn\\python\\제9장(리스트-2)\\data.txt", mode = "a", encoding="UTF-8")

# fp.write("1. 우리는 파이썬을 공부합니다\n")
# fp.write("2. 우리는 파이썬을 공부합니다\n")
# fp.write("3. 우리는 파이썬을 공부합니다\n")
# fp.write("4. 우리는 파이썬을 공부합니다\n")

# fp.close()

import csv

fp = open("C:\\Python\\Inflearn\\python\\제9장(리스트-2)\\data.csv", mode = "r", encoding="UTF-8")
reader = csv.reader(fp)
for txt in reader:
    print(txt)
# print(reader)

fp.close()