import fibo

fibo.fib(100)
print(fibo.sum(10))


# from fibo import fib, sum
# from fibo import *
# fib(100)
# print(sum(10))

# __name __
print(fibo.__name__)
print(__name__)

if __name__ == "__main__":
    fibo.fib(1000)
    print(fibo.sum(100))