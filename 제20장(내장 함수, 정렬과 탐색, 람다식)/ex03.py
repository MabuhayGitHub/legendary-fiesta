# 람다 함수 정의
f = lambda x, y: x + y
print("정수의 합: ", f(10, 100))
print("정수의 합: ", f(10, 50))

print()

# 위 코드에서 일반 함수를 사용하면
def get_sum(x, y):
    return x + y
print("정수의 합: ", get_sum(10, 100))
print("정수의 합: ", get_sum(10, 50))
