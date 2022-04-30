# FLAG
# [1] 증속
# [2] 감속
# [3] 중지

run = True
speed = 0

while run:
    print("--------------------------")
    print("[1] 증속 [2] 감속 [3] 중지")
    print("--------------------------")

    keyCode = int(input("선택: "))

    if keyCode == 1:
        speed += 10
        print("현재 속도: ", speed)
    elif keyCode == 2:
        if speed < 0:
            print("속도를 초기화 합니다!!")
            speed = 0
        speed -= 10
        print("현재 속도: ", speed)
    elif keyCode == 3:
        run = False
    else:
        print("입력값이 잘못 되었습니다 !!")
        break

    