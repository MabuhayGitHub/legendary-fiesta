# s = "A picture is worth a thounsand words."

def main():
    string = input("문자열을 입력하세요 : ")
    dic1 = {"alphas":0, "digits":0, "spaces":0}
    for i in string:
        if i.isalpha():
            dic1["alphas"] += 1
        if i.isdigit():
            dic1["digits"] += 1
        if i.isspace():
            dic1["spaces"] += 1
    print(dic1)

if __name__ == "__main__":
    main()

# 문자열을 입력하세요 : A picture is worth a thounsand words.
# {'alphas': 30, 'digits': 0, 'spaces': 6}