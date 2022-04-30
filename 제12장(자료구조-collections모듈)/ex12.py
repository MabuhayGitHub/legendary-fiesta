# # namedtuple

# a = ("John", 28, "남")
# b = ("Sally", 24, "여")
# for n in [a, b]:
#     print("%s은(는) %d세의 %s성입니다." %n)
# print(a[0])


from collections import namedtuple

# person = namedtuple(typename="person", field_names=("name age gender"))
# p1 = person(name="김연아", age=30, gender ="여")
# p2 = person(name="손연재", age=28, gender ="여")
# print(id(p1))
# for n in [p1, p2]:
#     print("%s는 %d세의 %s성입니다." %n)
# # John은(는) 28세의 남성입니다.
# # Sally은(는) 24세의 여성입니다.
# # John
# # 1931424787696
# # 김연아는 30세의 여성입니다.
# # 손연재는 28세의 여성입니다.

# person = namedtuple(typename="person", field_names=("name age gender"))

# p1 = person(name="김연아", age=30, gender ="여")
# p2 = person(name="손연재", age=28, gender ="여")
# p3 = person._make(("신은혁", 14, "남"))
# for n in [p1, p2, p3]:
#     print("%s는 %d세의 %s성입니다." %n)
# print(p3)
# p1 = p1._replace(name="강백호")
# for n in [p1, p2, p3]:
#     print("%s는 %d세의 %s성입니다." %n)
# print(p1)
# # 김연아는 30세의 여성입니다.
# # 손연재는 28세의 여성입니다.
# # 신은혁는 14세의 남성입니다.
# # person(name='신은혁', age=14, gender='남')
# # 강백호는 30세의 여성입니다.
# # 손연재는 28세의 여성입니다.
# # 신은혁는 14세의 남성입니다.
# # person(name='강백호', age=30, gender='여')

# from collections import namedtuple
# person = namedtuple(typename="person", field_names=("name age gender"))
# p1 = person(name="김연아", age=30, gender ="여")
# p2 = person(name="손연재", age=28, gender ="여")
# print(p1._fields)
# # ('name', 'age', 'gender')
# print(getattr(p1, "name"))
# # 김연아

dic = {"name":"신은혁", "age":15, "gender":"남", "addr":"대전"}
print(dic)
print(type(dic))
person = namedtuple(typename="person", field_names=("name age gender addr"))
p4 = person(**dic)
print(p4)