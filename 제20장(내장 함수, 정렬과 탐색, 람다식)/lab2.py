# 1~100 사이 3의 배수의 갯수
# mylist = [1 for k in range(1, 101) if k%3 ==0]
# print(mylist)
count = sum([1 for k in range(1, 101) if k%3 ==0])
print(count)

# -------------------------------------------------

n = eval(input("숫자를 입력하세요 "))
print(n)
