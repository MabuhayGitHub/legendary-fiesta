class Person:
    name = ""
    age = 0
    height = 0
    weight = 0
    address = ""
    def __init__(self):
        self.name = "홍길동"
        self.age = 35
        self.height = 175
        self.weight = 70
        self.address = "경상북도"
        print("기본 생성자 호출")
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getHeight(self):
        return self.height
    def getWeight(self):
        return self.weight
    def getAddress(self):
        return self.address
    
    def setName(self, name):
        self.name = name
    
    def __str__(self):
        print(self.name)
        print(self.age)
        print(self.height)
        print(self.weight)
        print(self.age)
