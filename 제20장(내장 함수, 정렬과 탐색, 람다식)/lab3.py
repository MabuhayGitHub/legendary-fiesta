orders = [
    ["1", "재킷", 5, 120000], 
    ["2", "셔츠", 6, 24000], 
    ["3", "바지", 3, 50000], 
    ["4", "코트", 6, 300000]
    ]

result = list(map(lambda x:  (x[0], x[2] * x[3]), orders))
print(result)
print()

# ----------------------------------------------------------

list1 = [("국어", 88), ("수학", 90), ("영어", 99), ("과학", 82)]
print(list1)
list1.sort(key=lambda x:x[1])
print(list1)
print()

# ----------------------------------------------------------

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums)
print(list(filter(lambda x : x % 2 == 0, nums )))
print(list(filter(lambda x : x % 2 == 1, nums )))
print()

# ----------------------------------------------------------

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x : x ** 3, nums)))
