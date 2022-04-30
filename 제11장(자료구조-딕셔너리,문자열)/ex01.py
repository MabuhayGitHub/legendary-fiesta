dic1 = {1:"사과", 2:"토마토", 3:"토마토"}
print(dic1)

dic2 = {}
print(type(dic2))

dic3 = {1:"사과", 2:"토마토", 3:"토마토"}
print(dic3[1])
print(dic3.get(1))

print(dic3.get(5))

a = dic3.get(4, "파인애플")
print(a)

print(1 in dic3)
print(1 not in dic3)


dic3 = {1:"사과", 2:"배", 3:"토마토"}
dic3[4] = "파인애플"
print(dic3)


dic4 = {1:"사과", 2:"배", 3:"토마토"}
a = dic4.pop(1)
print(a)

dic5 = {1:"사과", 2:"배", 3:"토마토"}
del dic5[1]
print(dic5)


dic6 = {1:"사과", 2:"배", 3:"토마토"}
dic6.clear()
print(dic6)