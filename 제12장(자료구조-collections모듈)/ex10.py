from collections import Counter

# text = list("high school")
# print(text)
# print(type(text))
# # ['h', 'i', 'g', 'h', ' ', 's', 'c', 'h', 'o', 'o', 'l']
# # <class 'list'>

# count = Counter(text)
# print(count)
# print(type(count))
# # Counter({'h': 3, 'o': 2, 'i': 1, 'g': 1, ' ': 1, 's': 1, 'c': 1, 'l': 1})
# # <class 'collections.Counter'

# print(count["h"])
# # 3

# count = Counter(b=2, c=5, a=3, A=7)
# print(count)
# print(sorted(count.elements()))
# # Counter({'A': 7, 'c': 5, 'a': 3, 'b': 2})
# # ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'c']

# count = Counter("인간으로서의 인간을 세계에 대한 인간적인 관계로서의 인간관계를 가정해보자")
# print(count)
# # Counter({' ': 7, '인': 5, '간': 4, '계': 3, '로': 2, '서': 2, '의': 2, '관': 2, '으': 1, '을': 1, '세': 1, '에': 1, '대': 1, '한': 1, '적': 1, '를': 1, '가': 1, '정': 1, '해': 1, '보': 1, '자': 1})

# text = "Hello World"
# print(text)
# print(text.lower())
# print(text.lower().split())
# print(Counter(text))
# # Hello World
# # hello world
# # ['hello', 'world']
# # Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})

count = Counter({"가":4, "나":3})
print(count)
print(list(count.elements()))
# Counter({'가': 4, '나': 3})
# ['가', '가', '가', '가', '나', '나', '나']