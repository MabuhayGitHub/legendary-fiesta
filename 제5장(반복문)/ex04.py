sum = 0
num = 100

for i in range(1, num+1):
    sum += i
    if sum >= 2000:
        print(i,"\t",sum)
        break
    
print("종료 시점의 값은", i, "합은 ", sum, "입니다.")
