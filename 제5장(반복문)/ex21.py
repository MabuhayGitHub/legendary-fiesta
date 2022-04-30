statements = input("문자열을 입력하세요(영문/숫자/공백 허용) ")

cntAlpha = 0
cntDigit = 0
cntSpace = 0

for ch in statements:
    if ch.isalpha():
        cntAlpha += 1
    elif ch.isdigit():
        cntDigit += 1
    elif ch.isspace():
        cntSpace += 1
    else:
        print(ch, "영문, 숫자, 공백이 아닙니다.")
print(cntAlpha)
print(cntDigit)
print(cntSpace)