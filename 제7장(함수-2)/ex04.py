def change(dic):
    print(dic)
    print(id(dic))
    dic["몸무게"] = 42
    print(dic)
    print(id(dic))

dic = {"name":"신은혁", "age":14, "height":160}

print(dic)
print(dic["name"])
change(dic)
print(type(dic))
print(dic)