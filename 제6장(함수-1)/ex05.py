def isPrimeNumber(num):
    for i in range(2,num):
        temp = True
        if (num % i) == 0:
            temp = False
        else:
            temp = True
    return temp

print(isPrimeNumber(107))