def printInfo(name, age):
    print("==================================")
    print("이름: ", name)
    print("나이: ", age)
    print("==================================")
    return

end_Input = "y"

while True:
    if end_Input == "n":
        print("입력을 종료합니다.")
        break
    elif end_Input == "y":
        name = input("이름을 입력해 주세요. ")
        age = int(input("나이를 입력해 주세요. "))
        printInfo(name, age)
        
    end_Input = input("계속 입력하시겠습니까?(y/n)")