from re import I


sum = 1.0
fnum = int(input("정수를 입력하세요. "))

for i in range(fnum,0,-1):
    sum = sum * i
#   sum *= i
    print(sum)


fval = 1.0
fnum = int(input("정수를 입력하세요. "))
for i in range(i,fnum+1):
    fval = fval * i
#   sum *= i
    print(fval)