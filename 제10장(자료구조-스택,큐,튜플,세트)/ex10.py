set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

print(set1 == set2)
print(set1 != set2)

print(set1 > set2)
print(set1 < set2)

print(set1.issubset(set2))
print(set2.issubset(set1))

print(set1.issuperset(set2))
print(set2.issuperset(set1))

print(1 in set1)
print(0 in set1)

print(set1 | set2)
print(set1.union(set2))
print()
print(set1 & set2)
print(set1.intersection(set2))
print()
print(set1 - set2)
print(set1.difference(set2))
print()
print(set2 - set1)
print(set2.difference(set1))
print()

set1 = {0, 1}
set2 = {0, 1}
print(all(set1))
print(any(set1))
print()

set1 = {0, 1}
set2 = {0, 1}
print(set1.isdisjoint(set2))

set1 = {0, 1}
set2 = {2, 3}
print(set1.isdisjoint(set2))

set1 = {0, 1, 2, 3, 4, 5}
set1.pop()
print(set1)

set1 = {0, 1, 2, 3, 4, 5}
for _ in range(len(set1)):
    print(set1.pop())
    # print(set1)
