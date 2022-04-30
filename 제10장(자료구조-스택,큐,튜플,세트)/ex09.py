set1 = {2, 1, 3, 5, 4}
print(set1)

set2 = {"사람", "자동차", "동물"}
print(set2)

print(len(set1))
print(len(set2))

set3 = {2, 3, "사람", "자동차", "동물", 1, 2, "자동차", "동물", 3}
print(set3)
if "자동차" in set3:
    print(True)

set4 = set()
for i in range(101):
    set4.add(i)
print(set4)
set4.clear()

set5 = {1.1, 2, "자동차", (10, 20)}
print(set5)

set6 = set()
set6.update(["인간", 1, 3, 5, 15])
print(set6)
# set6.update("인간", [1, 3, 5, 15])
# print(set6)
# set6.clear()

set6.discard("인간")
print(set6)

set6.remove(15)
print(set6)

set6.clear()
