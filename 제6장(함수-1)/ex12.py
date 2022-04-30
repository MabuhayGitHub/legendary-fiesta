def decTobin(num):
    binary = ""
    while num != 0:
        value = num % 2
        if value == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        num = num // 2
#        print(num)
    return binary

# val = int(input("변환할 10진수를 입력하세요. "))
print(decTobin(10))

print(bin(10))
print(oct(10))
print(hex(10))

print(int("0b1010", 2))
print(int("0o12", 8))
print(int("0xa", 16))
