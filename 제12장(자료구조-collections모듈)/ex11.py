from collections import Counter

# # update()
# count = Counter()
# print(count)
# count.update("안녕하세요")
# print(count)
# count.update({"안":3, "요":5})
# print(count)
# print(list(count.elements()))
# # Counter()
# # Counter({'안': 1, '녕': 1, '하': 1, '세': 1, '요': 1})
# # Counter({'요': 6, '안': 4, '녕': 1, '하': 1, '세': 1})
# # ['안', '안', '안', '안', '녕', '하', '세', '요', '요', '요', '요', '요', '요']

# # most_common(n)
# count = Counter("apple, orange, grape")
# print(count.most_common())
# print(count.most_common(3))
# # [('a', 3), ('p', 3), ('e', 3), (',', 2), (' ', 2), ('r', 2), ('g', 2), ('l', 1), ('o', 1), ('n', 1)]
# # [('a', 3), ('p', 3), ('e', 3)]

# # subtract()
# c1 = Counter("안녕하세요. 반갑습니다. ")
# c2 = Counter("안녕. 반갑다. ")
# c1.subtract(c2)
# print(c1)
# # Counter({'하': 1, '세': 1, '요': 1, '습': 1, '니': 1, '안': 0, '녕': 0, '.': 0, ' ': 0, '반': 0, '갑': 0, '다': 0})

# # 
# c1 = Counter(["a", "b", "c", "d", "a"])
# c2 = Counter("apple")
# print(c1)
# print(c2)
# print(c1 + c2)
# # Counter({'a': 2, 'b': 1, 'c': 1, 'd': 1})
# # Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})
# # Counter({'a': 3, 'p': 2, 'b': 1, 'c': 1, 'd': 1, 'l': 1, 'e': 1})

# c1 = Counter(["a", "b", "c", "d", "a"])
# c2 = Counter("apple")
# print(c1)
# print(c2)
# print(c1 - c2)
# # Counter({'a': 2, 'b': 1, 'c': 1, 'd': 1})
# # Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})
# # Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})

# c1 = Counter("abcdefg")
# c2 = Counter("abcd가나다라")
# print(c1 & c2)
# print(c1 | c2)
# # Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})
# # Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, '가': 1, '나': 1, '다': 1, '라': 1})