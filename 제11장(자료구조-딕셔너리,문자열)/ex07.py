# string = input("Python 소스를 입력해 주세요 : ")
# if string.endswith(".py"):
#     print("파이썬 파일")
# else:
#     print("파이썬 파일이 아닙니다")
# # Python 소스를 입력해 주세요 : hello.py
# # 파이썬 파일

# string = "2022년 데이터"
# if string.startswith("2022"):
#     print("2022년")
# else:
#     print("2022년이 아님")
# # 2022년

# string = input("영어 단어를 입력하세요 : ")
# print(string.upper())
# print(string.lower())
# print(string.capitalize())
# print(string.title())
# # 영어 단어를 입력하세요 : hello world
# # HELLO WORLD
# # hello world
# # Hello world
# # Hello World

# string = "{}b{}"
# print(string.format("a", "c"))
# # abc

# string = ["a", "b", "가"]
# print("!".join(string))
# # a!b!가

# string = "eunhyuk@gmail.com"
# print(string.partition("@"))
# # ('eunhyuk', '@', 'gmail.com')

# string = "aaaabbbbbccdd"
# print(string.count("a"))
# print(string.count("z"))
# # 4
# # 0

# string = "apple"
# print(string.find("p"))
# print(string.index("p"))
# print(string.find("z"))
# # 1
# # 1
# # -1

# string = " strip 함수의 특성에 대해 알아보자   \t"
# print(string.strip())
# print(string.lstrip())
# print(string.rstrip())
# # strip 함수의 특성에 대해 알아보자
# # strip 함수의 특성에 대해 알아보자
# #  strip 함수의 특성에 대해 알아보자

def main():
    string = input("문자열을 입력하세요 ")
    string.replace(" ", "")
    if check(string) == True:
        print(string, "회문입니다")
    else:
        print(string, "회문이 아닙니다")

def check(s):
    low = 0
    high = len(s) - 1
    
    while True:
        if low > high:
            return True

        s1 = s[low]
        s2 = s[high]
        # print(s1, s2)

        if s1 != s2:
            return False

        low  += 1
        high -= 1

if __name__ == "__main__":
    main()

# 문자열을 입력하세요 소주만병만주소
# 소주만병만주소 회문입니다

