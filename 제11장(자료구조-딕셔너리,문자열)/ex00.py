s = "Never put off till tomorrow what you can do today"
print(s.split())

s = "Mississippi"
print(s.split("i"))

s = "abcdef"
print(s.isalpha())

s = "123456"
print(s.isdigit())

# islower()
# isupper()
# isspace()
# isalnum()

# startswith()
# endswith()
# find()
# rfind()
# count()

# upper()
# lower()
# capitalize()
# title()
# replace()
# swapcase()
# format()
# join()
# partition()

# isdecimal()
# isdigit()
# isnumeric()

# strip()
# lstrip()
# rstrip()
# myDic = {   
#             "Kim" :"01012345678", 
#             "Park":"01012345679", 
#             "Lee" :"01012345680"
#         }
# print(myDic)
# print(type(myDic))
# print(id(myDic))

# # ---------------------------------------------------

# d1 = {1:"apple", 2:"banana"}
# print(type(d1))

# d2 = {}
# print(type(d2))

# ---------------------------------------------------

# contacts =  {   
#             "Kim" :"01012345678", 
#             "Park":"01012345679", 
#             "Lee" :"01012345680"
#             }
# print(contacts["Kim"])
# print(contacts.get("Kim"))

# print("Kim" in contacts)

# contacts["Choi"] = "01056781234"
# print(contacts)

# print(contacts.pop("Choi"))
# print(contacts)

# del contacts["Kim"]
# print(contacts)

# ---------------------------------------------------

# scores = {"Korean":80, "Math":90, "English":80}
# print(scores)

# for item in scores.items():
#     print(item, end=" ")

# ---------------------------------------------------

# squares = {1:1, 2:4, 3:9, 4:16, 5:25}
# print(1 in squares)

# ---------------------------------------------------

# triples = {x:x*x*x for x in range(6)}
# print(triples)

# ---------------------------------------------------

# dic = {"bags":1, "books":5, "bottles":4, "coins":7, "cups":2, "pens":3}
# print(dic)

# print(list(dic))

# print(sorted(dic))

# print(sorted(dic.values()))

# print(sorted(dic, key=dic.__getitem__))

# print(dic.keys())
# print(dic.values())

