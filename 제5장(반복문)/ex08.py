# num = int(input("출력하고 싶은 단을 입력하세요. "))

for i in range(1,10):
    print("*********", i, "단 *********")
    for num in range(1,10):
        print(i, "*", num, "=", (num*i))