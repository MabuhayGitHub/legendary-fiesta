from random import *

cnt = 0
num = randint(1,100)
print("발생한 난수 : ", num)
print("기회: 10회 이내")

while cnt <= 10:
    guess = int(input("숫자를 입력하세요 -> "))
    cnt += 1
    if guess < num:
        print("크게")
    elif guess > num:
        print("작게")
    elif guess == num:
        print("빙고")
        print("시도 횟수는 %s 입니다" % cnt)
        break