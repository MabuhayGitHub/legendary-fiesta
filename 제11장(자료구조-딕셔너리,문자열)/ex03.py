eng_dict = dict()

eng_dict["one"] = "하나"
eng_dict["two"] = "둘"
eng_dict["three"] = "셋"
eng_dict["four"] = "넷"
eng_dict["five"] = "다섯"

print(eng_dict)

while True:
    word = input("단어를 입력하세요. 종료(Q) ")

    if word == "Q":
        print("프로그램을 종료합니다.")
        break

    if word in eng_dict:
        print(eng_dict.get(word))
    else:
        print("해당하는 자료가 없습니다.")



