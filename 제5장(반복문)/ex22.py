
statements = input("문자열을 입력하세요 : ")

s_reverse = ""
for ch in statements:
    s_reverse = ch + s_reverse
print(statements)
print(s_reverse)

s_list = list(statements)
s_list.reverse()
print("".join(s_list))


print("".join(reversed(statements)))

print(statements[::-1])