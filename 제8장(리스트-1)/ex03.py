# li1 = "강아지"
# print(li1)

# li1 = list("강아지")
# print(li1)

# li1 = ["강아지"]
# print(li1)

dogNames = []
while True:
    name = input("강아지 이름을 입력하세요.(종료시에는 엔터키)")
    if name == "":
        break
    dogNames.append(name)
print("강아지의 이름은", dogNames, "입니다.")
