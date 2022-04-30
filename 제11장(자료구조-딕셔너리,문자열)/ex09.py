def main():
    string = input("문자열을 입력하세요 : ")
    acronym = ""
    
    for word in string.upper().split():
        acronym += word[0]
    print(acronym)

if __name__ == "__main__":
    main()
# 문자열을 입력하세요 : Korea Big Data Center
# KBDC