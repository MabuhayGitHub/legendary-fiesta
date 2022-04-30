# 시퀀스 자료형: 문자열, 바이트 시퀀스, 바이트 배열, 리스트, 튜플, range() 개체

# text = "Will is Power"
# print(text[0], text[3], text[-1])
# print(len(text))

# print(["hello"] * 3)

# shopping_list = ["두부", "양배추", "딸기", "사과", "토마토"]
# print(shopping_list[0])
# print(shopping_list[-1])

# shopping_list.append("")
# print(shopping_list)

# squares = [0, 1, 4, 9, 16, 25, 36, 49]

# print(squares[:])
# print(squares[:6])
# print(squares[3:])
# print(squares[3:6])

words = "nice to meet you!"
print(words[0], words[5], words[-1])

li = ["사과", "바나나", "복숭아", "토마토"]
# print(li[0], li[5], li[-1])
print(li[0], li[2], li[-1])

print(len(words))
print(len(li))

li1 = [1, 2]
print(id(li1))
li2 = [3, 4, 5]
print(id(li2))
li3 = li1 + li2
print(id(li3))
print(li3)

print(["안녕"] * 5)

print(10 in [1, 2, 3])