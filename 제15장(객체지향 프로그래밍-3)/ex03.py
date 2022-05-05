# 형식의 다형성 

class Animal(object):
    def __init__(self, name, age, weight, instance):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__instance = instance
    def show(self):
        print(self.__name)
        print(self.__instance.d_name)
        print(self.__age)
        print(self.__weight)
        self.__instance.sound()
        print("-----------------------------------------")
class Tiger:
    d_name = "호랑이"
    def sound(self):
        print("어흥")
class Dog:
    d_name = "개"
    def sound(self):
        print("멍멍")
class Cat:
    d_name = "고양이"
    def sound(self):
        print("야옹")

if __name__ == "__main__":
    ani1 = Animal("호돌이", 8, 180, Tiger())
    ani2 = Animal("포돌이", 4, 8, Dog())
    ani3 = Animal("냥이", 1, 2, Cat())
    
    ani1.show()
    ani2.show()
    ani3.show()