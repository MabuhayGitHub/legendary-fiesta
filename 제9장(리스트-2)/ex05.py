
def menu_print():
    print("1. 목록 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")

menu_choice = 0
friends = ["홍길동"]

while True:
    menu_print()
    menu_choice = int(input("메뉴를 선택하세요 "))
    if menu_choice == 9:
        print("프로그램을 종료합니다")
        break
    elif menu_choice == 1:
        print("친구 리스트입니다.")
        print(friends)
    elif menu_choice == 2:
        name = input("이름을 입력하세요 ")
        friends.append(name)
    elif menu_choice == 3:
        del_name = input("삭제할 이름을 입력하세요 ")
        if del_name in friends:
            friends.remove(del_name)
            print(del_name + "님이 삭제되었습니다.")
        else:
            print(del_name + "님은 존재하지 않습니다")
    elif menu_choice == 4:
        old_name = input("변경할 이름을 입력하세요 ")
        if old_name in friends:
            index = friends.index(old_name)
            new_name = input("이름을 입력하세요 ")
            friends.append(new_name)
    elif menu_choice ==9:
        print("프로그램을 종료합니다")
        break
