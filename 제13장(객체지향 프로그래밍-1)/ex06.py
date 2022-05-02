
class Account:
    __balance = 0

    def __init__(self):
        self.__balance = 0
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self, value):
        print(format(value, ","), "원이 입금되었습니다")
        self.__balance += value
        print("현재 잔액은", format(self.getBalance(),","), "원 입니다.")

    def withdraw(self, value):
        if value > self.__balance:
            print("잔액이 부족합니다.")
            return
        print(format(value, ","), "원이 출금되었습니다")
        self.__balance -= value
        print("현재 잔액은", format(self.getBalance(),","), "원 입니다.")

if __name__ == "__main__":
    account = Account()
    account.deposit(1000000)
    print()
    account.withdraw(500000)

# 1,000,000 원이 입금되었습니다
# 현재 잔액은 1,000,000 원 입니다.
# 500,000 원이 출금되었습니다
# 현재 잔액은 500,000 원 입니다.