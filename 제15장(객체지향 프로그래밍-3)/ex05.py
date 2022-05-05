# 다형성

class Product(object):
    price = 0
    bonusPoint = 0
    def __init__(self, price):
        self.price = price
        self.bonusPoint = int(self.price / 10.0)

class TV(Product):
    def __init__(self, price):
        super().__init__(price)
    def __str__(self):
        return "TV"

class Computer(Product):
    def __init__(self, price):
        super().__init__(price)
    def __str__(self):
        return "Computer"

class Audio(Product):
    def __init__(self, price):
        super().__init__(price)
    def __str__(self):
        return "Audio"

class Buyer(object):
    money = 1000
    bonusPoint = 0
    def buy(self, product):
        if self.money < product.price:
            print("잔액 부족")
            print("잔액:", self.money)
            return
        self.money -= product.price
        self.bonusPoint += product.bonusPoint
        print(product.__str__() + " 구매")
        print("잔액:", self.money)
        print("보너스 포인트:", self.bonusPoint)
        print()

if __name__ == "__main__":
    buyer = Buyer()
    tv = TV(300)
    computer = Computer(100)
    audio = Audio(50)
    # 메서드의 다형성
    buyer.buy(tv)
    buyer.buy(computer)
    buyer.buy(audio)
    # 형식의 다형성
    buyer.buy(TV(400))
    buyer.buy(Computer(100))
    buyer.buy(Audio(75))