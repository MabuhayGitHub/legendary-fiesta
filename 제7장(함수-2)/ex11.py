def main():
    a, b, c = tuple_return()
    tuple_variable = tuple_return()
    print(a, b, c)
    print(tuple_variable)
    print(type(tuple_variable))

    li = list(tuple_variable)
    print(li)
    print(type(li))
    li.append("반갑습니다")
    return

def tuple_return():
    return 1, "안녕", 5

main()