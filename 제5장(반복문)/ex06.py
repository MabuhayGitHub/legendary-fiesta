n1 = 1
n2 = 1
n3 = 1

fi = int(input("정수를 입력하세요.(피보나치수열) "))

for i in range(1, fi):
    if i < 3:
        n3 = 1
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    if n3 < fi:
        print(n3, end=" ")

        
