n1 = int(input("첫번째 수: "))
n2 = int(input("두번째 수: "))

for i in range(n1, n2+1):
    if (i % 3) == 0 and (i % 4) == 0:
#   if (i % 12) == 0
        continue
    print(i)