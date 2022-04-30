# 데이터 저장 방식 변천
# 변수 > 배열 > 구조체 > 클래스
# 리스트 <= 배열 + 구조체 유사

# scores = []
# print(scores)

# scores.append(10)
# print(scores)
# scores.append("안녕")
# print(scores)
# scores.append(3.14)
# print(scores)

# print(len(scores))

# scores[0] = "hello"
# print(scores)

# for i in range(len(scores)):
#     print(i, scores[i])

# for i in range(len(scores)):
#     scores[i] = i * 10
#     print(i, scores[i])

# scores = [0, 1, 2, 3, 4, 5]
# for i in scores:
#     print(i, scores[i])

# scores = "known unknown"
# for i in range(len(scores)):
#     print(i, scores[i])

# scores = "known unknown"
# for i in scores:
#     print(i, end="")
# print()

# nums = []
# for i in range(5):
#     nums.append(int(input("정수를 입력하세요 :")))
# print(nums)

###########################################################################################

li1 = list()
print(li1)

li2 = list("안녕")
print(li2)

li3 = list(range(0, 5, 2))
print(li3)

###########################################################################################

li1 = [12, 12.77, "안녕"]
print(li1)

li2 = [["서울", 10], ["파리", 20], ["뉴욕", 30]]
print(li2)

# print(li2[0][0])
# print(li2[1][0])
# print(li2[2][0])

for i in range(len(li2)):
    for j in range(len(li2[i])):
        print(li2[i][j])