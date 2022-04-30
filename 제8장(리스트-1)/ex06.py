# values = [1, 2, 3] * 3
# print(values)

# shopping_list = ["두부", "양배추", "딸기"]
# print(shopping_list)
# print(shopping_list[1])
# shopping_list.insert(1, "생수")
# print(shopping_list)
# print(shopping_list[1])

# heroes = ["스파이더맨", "슈퍼맨", "헐크", "아이언맨", "배트맨"]
# if "배트맨" in heroes:
#     print("배트맨은 영웅입니다.")

# heroes = ["스파이더맨", "슈퍼맨", "헐크", "아이언맨", "배트맨"]
# index = heroes.index("슈퍼맨")
# print(index)

# heroes = ["스파이더맨", "슈퍼맨", "헐크", "아이언맨", "배트맨"]
# print(heroes.pop(1))
# print(heroes)

# heroes = ["스파이더맨", "슈퍼맨", "헐크", "아이언맨", "배트맨"]
# print(heroes.remove("헐크"))
# print(heroes)

# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# print(list1 == list2)

# list1 = [1, 3, 2, 5, 4]
# list1.sort()
# print(list1)

# list1 = [1, 3, 2, 5, 4]
# print(sorted(list1))
# print(list1)

# list1 = sorted(" A picture is worth a thousand word.")
# print(list1)

# list1 = sorted(" A picture is worth a thousand word.".split())
# print(list1)

# list1 = sorted(" A picture is worth a thousand word.".split(), key=str.lower)
# print(list1)


# list1 = [1, 3, 2, 5, 4]
# list1.sort(reverse=False)
# print(list1)
# list1.sort(reverse=True)
# print(list1)


# list1 = [1, 3, 2, 5, 4]
# print(sorted(list1, reverse=True))
# print(list1)


# statement = "Where there is a will, there is a way"
# list1 = statement.split()
# print(list1)


# statement = "Where there is a will, there is a way"
# list1 = statement.split(",")
# print(list1)


# append() / insert()

# li1 = ["TV", "오디오", "PC", "키보드"]
# print(id(li1))
# print(li1)

# li1.append("마우스")
# print(id(li1))
# print(li1)

# li1.insert(1, "휴대폰")
# print(id(li1))
# print(li1)

# li2 = li1
# print(id(li2))
# print(li2)

# if "PC" in li2:
#     print("있어요")

# index = li2.index("오디오")
# print(index)

# if "키보드" in li2:
#     index = li2.index("키보드")
#     print(index)
# else:
#     print("존재하지 않아요")

# 리스트에서 요소 삭제
# pop() remove() delete()
# li1 = ["TV", "오디오", "PC", "키보드"]

# print(li1)
# temp1 = li1.pop(1)
# print(temp1)
# print(li1)

# # remove() 중복된 요소가 있을 경우 인덱스가 작은 요소만 제거
# li1.remove("PC")
# print(li1)


li1 = ["TV", "오디오", "PC", "키보드"]

print(li1)
del li1[1]
print(li1)

del li1[:]
print(li1)

li1 = ["TV", "오디오", "PC", "키보드"]
print(li1)
li1.clear()
print(li1)


li1 = ["TV", "오디오", "PC", "키보드"]
print(li1.count("오디오"))

li1 = [1, 3, 5]
li2 = [2, 4, 6]
print(li1 + li2)

li1 = [1, 3, 5]
li2 = [2, 4, 6]
li1 += li2
print(li1)

li1 = [1, 3, 5]
li2 = [2, 4, 6]
li1.extend(li2)
print(li1)