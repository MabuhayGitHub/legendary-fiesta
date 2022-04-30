# dic = {}
# dic["a"] = 100
# dic["b"] = 200
# dic["c"] = 300
# dic["d"] = 400
# dic["e"] = 500
# dic["f"] = 600
# dic["3"] = 700
# dic["h"] = 800
# dic["1"] = 900
# dic["j"] = 1000

# print(sorted(dic.keys()))
# print(sorted(dic.values()))

# --------------------------------------------------------------------------------

# from collections import OrderedDict

# def sort_by_key(t):
#     return(t[0])

# dic1 = {}
# dic1["a"] = 100
# dic1["b"] = 200
# dic1["c"] = 300
# dic1["d"] = 400

# for k, v in OrderedDict(sorted(dic1.items(), key=sort_by_key)).items():
#     print(k, v)

# print(sorted(dic1.items(), key=sort_by_key))

# --------------------------------------------------------------------------------

dic1 = {"가":1, "나":2, "다":3}
dic2 = {"나":1, "다":2, "가":2}

print(id(dic1))
print(id(dic2))
print(dic1 == dic2)




from collections import OrderedDict

def sort_by_key(t):
    return(t[0])

odic1 = OrderedDict({"가":1, "나":2, "다":3})
odic2 = OrderedDict({"나":1, "다":2, "가":2})

print(id(odic1))
print(id(odic2))
print(odic1 == odic2)

print(sorted(odic1.items(), key=sort_by_key))
