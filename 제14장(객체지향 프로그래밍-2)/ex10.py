class Car:
    value = "조상 클래스 필드값"
    def carMethod(self):
        print("조상 클래스 메서드 호출")

class Sedan(Car):
    value = "자손 클래스 필드값"
    def carMethod(self):
        super().carMethod()
        print("자손 클래스 메서드 호출")
        print("조상 클래스 Value: ", super().value)
        print("자손 클래스 Value: ", self.value)

if __name__ == "__main__":
    sedan = Sedan()
    sedan.carMethod()
