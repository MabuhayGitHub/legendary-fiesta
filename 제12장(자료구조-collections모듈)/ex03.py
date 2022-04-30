dic = {}
dic["a"] = 100
dic["b"] = 200
dic["c"] = 300
dic["d"] = 400
dic["e"] = 500

for k, v in dic.items():
    print(k, v)

print()

from collections import OrderedDict

dic = OrderedDict()
dic["a"] = 100
dic["b"] = 200
dic["c"] = 300
dic["d"] = 400
dic["e"] = 500

for k, v in dic.items():
    print(k, v)
