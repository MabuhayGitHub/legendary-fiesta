def fib(n):
    n1 = 0
    n2 = 1
    n3 = n1 + n2
    while n3 < n:
        print(n3, end=" ")
        n3 = n1 + n2
        n1 = n2
        n2 = n3 
    print()

def sum(n):
    hap = 0
    for i in range(1, n+1):
        hap += i
    return hap