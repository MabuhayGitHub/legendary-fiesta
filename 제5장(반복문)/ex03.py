num = int(input("숫자를 입력하세요: "))
sum = 0

for i in range(1,num+1):
    sum = sum + i
#   sum += i
print("1 부터", num,"까지의 합은 ", sum, "입니다.")