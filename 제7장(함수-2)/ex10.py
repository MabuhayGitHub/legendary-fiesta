PI = 3.141592

def main():
    r = float(input("원의 반지름을 입력하세요. "))
    print("원의 둘레: ", cCir(r))
    print("원의 넓이: ", cArea(r))

def cArea(r):
    result = PI * r * r
    return result

def cCir(r):
    result = 2.0 * PI * r
    return result

main()