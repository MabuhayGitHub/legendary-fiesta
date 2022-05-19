# 공유 객체를 사용하는 User-1, User-2 클래스 인스턴스 실행

from User1 import *
from User2 import *

if __name__ == "__main__":
    # 공유 객체 생성, memory = 0으로 초기화
    calculator = Calculator(0)

    user1 = User1()
    user1.setCalculator(calculator)

    user2 = User2()
    user2.setCalculator(calculator)

    user1.start()
    user2.start()