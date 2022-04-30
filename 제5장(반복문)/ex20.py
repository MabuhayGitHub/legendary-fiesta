# Prime Number

start_num = 0
num = 0
sum = 0
lastVal = 0

for num in range(2, 2001):
    for start_num in range(2, num+1):
        if num % start_num == 0:
            break
    if num == start_num:
        print("소수: ", start_num)
        sum += start_num
        lastVal = start_num
print(sum)
print(lastVal)
