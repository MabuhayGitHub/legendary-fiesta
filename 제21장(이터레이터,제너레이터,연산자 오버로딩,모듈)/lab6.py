import random

# words = []
# words.append("파일썬")
# words.append("파이썬")
# words.append("파삼썬")
# words.append("파사썬")
# words.append("파오썬")
# words.append("파육썬")
# words.append("파칠썬")

# # print(words)

# result = []
# i = 0
# while True:
#     if i > 2:
#         break
#     val = random.choice(words)
#     if val not in result:
#         result.append(val)
#         i += 1

# print(result)

# --------------------------------------------------------------

# str1 = "abcdefghijklmnopqrstuvwxyz"
# for i in range(0, 10):
#     letter = random.choice(str1)    # 중복 제거 별도 처리 필요
#     print(letter, end=" ")


# --------------------------------------------------------------

print(random.sample([i for i in range(100,201,2)], 5))
print(random.sample([i for i in range(100,201) if i %2 == 0], 5))