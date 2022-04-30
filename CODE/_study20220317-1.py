def add_num2():
    list1 = input("띄어쓰기로 나눠서 숫자를 4개만 입력하세요: ")
    a, b, c, d = list1.split()
    #a, b, c, d = int(a), int(b), int(c), int(d)
    #return a + b + c + d
    return int(a) + int(b) + int(c) + int(d)
