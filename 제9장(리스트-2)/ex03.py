# Call-by-Value
# Call-by-Reference

def func1(x):
    print("x=", id(x))
    x = 42
    print("x=", id(x))

y = 10
print("y=", id(y))
func1(y)
print("y=", id(y))

def func2(list):
    print(id(list))
    list[0] = 99
    print(id(list))

values = [0, 1, 1, 2, 3, 5, 8]
print(id(list))
print(values)
func2(values)
print(id(list))
print(values)