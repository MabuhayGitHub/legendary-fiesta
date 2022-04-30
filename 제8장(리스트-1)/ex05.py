li = ["안", "녕", "하", "세", "요"]
print(li[2])
print(li[-1])

li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s_li = li[2:5]
print(s_li)

li[:] = []
print(li)

words = list("abcde")
print(words)
print(words[1:3])
words[1:3] = ["B", "C", "D"]
print(words)

words = list("abcde")
print(id(words))
words = []
print(id(words))

words = list("abcde")
print(id(words))
words[:] = []
print(id(words))
