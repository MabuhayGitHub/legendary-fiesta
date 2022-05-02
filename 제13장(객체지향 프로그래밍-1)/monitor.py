# 매개변수가 있는 생성자

class Monitor:
    
    __company = ""
    __inch = 0
    __price = 0
    __color = ""

    # 생성자
    def __init__(self, company, inch, price, color):
        self.__company = company
        self.__inch = inch
        self.__price = price
        self.__color = color

    # getter method
    def getCompany(self):
        return self.__company
    def getInch(self):
        return self.__inch
    def getPrice(self):
        return self.__price
    def getColor(self):
        return self.__color
        
    # setter method
    def setCompany(self, company):
        self.__company = company
    def setInch(self, inch):
        self.__inch = inch
    def setPrice(self, price):
        self.__price = price
    def setColor(self, color):
        self.__color = color
    
    # 멤버변수값 출력
    def __str__(self):
        print(self.getCompany())
        print(self.getInch())
        print(self.getPrice())
        print(self.getColor())

