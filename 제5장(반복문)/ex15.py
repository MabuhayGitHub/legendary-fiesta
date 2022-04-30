from operator import eq

total = 0
price = ""

while True:
    price = input("상품 금액을 입력하세요. ('끝'을 입력하면 종료됩니다.)")
    if eq(price, '끝'):
        print("상품의 총 가격: " + str(total) + "원")
        break
    total += int(price)
print(total)
