# 손님
names   = ["신은혁", "김연아", "손연재", "손아섭"]
# 손님별 방문자 수
persons = [1, 3, 0, 6]

print(len(names))

print(sum(persons))

print(any(persons))

print(all(persons))

print(max(persons))

for n, p in zip(names, persons): print(n, p)