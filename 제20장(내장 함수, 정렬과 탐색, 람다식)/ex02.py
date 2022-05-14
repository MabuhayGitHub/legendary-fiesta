# sort()
# sorted()

a = [4, 2, 1, 5, 7, -1]
b = sorted(a)
print(a)
print(b)
print(id(a))
print(id(b))
print()

x = [4, 2, 1, 5, 7, -1]
y = x.sort()    # 원본 리스트 변경 
print(x)
print(y)
print()

print(sorted({3:"D", 2:"B", 5:"B", 4:"E", 1:"A"}))
print()

print(sorted("주변을 잘 살피고 주의 하면서 플레이 해주십시오".split(), key=str.lower))
print()

students = [
    ("신은혁", 4.4, 20210701),
    ("김연아", 4.5, 20210630),
    ("손연재", 3.4, 20210702)
]
print(sorted(students, key=lambda students: students[1], reverse=True))
print(sorted(students, key=lambda students: students[1], reverse=False))
print()

# 정렬의 안정성

data = [(3,100), (1,200), (1,300), (2,100), (2,200)]
print(sorted(data, key=lambda data:data[0]))
