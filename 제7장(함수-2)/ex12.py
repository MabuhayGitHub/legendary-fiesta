# Anonymous Function

# lamda 인수1, 인수1 : 수식

def main():
    print(get_sum(10, 50))
    print(get_sum(100, 200))
    print("람다식", sum(10, 50))
    print("람다식", sum(10, 150))

    print(lambda x, y: x + y)
    print((lambda x, y:x + y)(10, 50))
def get_sum(x, y):
    return x + y

sum = lambda x, y: x + y

li = [ lambda x : x ** 2, lambda x : x ** 3, lambda x : x ** 4]

for f in li:
    print(f(10))

main()