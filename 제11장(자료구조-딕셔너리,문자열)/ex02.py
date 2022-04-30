# scores = {"국어":80, "수학":95, "영어":80}

# for subject in scores:
#     print(subject, end=" ")
# print()

# print(scores.keys())
# print(type(scores.keys()))
# for subject in scores.keys():
#     print(subject, end=" ")
# print()

# print(scores.values())
# print(type(scores.values()))
# for subject in scores.values():
#     print(subject, end=" ")
# print()

# print(scores.items())
# print(type(scores.items()))
# for subject in scores.items():
#     print(subject, end=" ")
# print()

# ------------------------------------------------------------------------------

# triples = {x:x*x*x for x in range(6)}
# print(type(triples))
# print(triples)

# ------------------------------------------------------------------------------

dic1 = {"bags":1, "books":5, "bottles":4, "coins":3, "cups":2, "pens":6}
print(dic1)

li1 = list(dic1.keys())
print(type(li1))
print(li1)
li2 = list(dic1.values())
print(type(li2))
print(li2)

print(sorted(dic1))
print(sorted(dic1.keys()))
print(sorted(dic1.values()))

print(dic1.__getitem__)
print(sorted(dic1, key=dic1.__getitem__))



