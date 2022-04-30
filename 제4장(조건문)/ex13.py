from random import *

rand_num = randint(1,100)
user_num = int(input("숫자를 입력하세요.(1~100)"))

print("생성된 숫자", rand_num)
while True:
    if user_num == rand_num:
        print("정답")
        break
    elif user_num > rand_num:
        print("커요")
    else:
        print("작아요")
    user_num = int(input("다시 입력해 주세요. "))