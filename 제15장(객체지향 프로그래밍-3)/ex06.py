# 추상클래스는 인스턴스 생성 불가
# abc(abstract base class)
# @abstractmethod
# 추상메서드: 선언부만 존재, 구현부 없음

from abc import *
# 추상클래스 표기
class StudentBase(metaclass=ABCMeta):
    @abstractmethod     # 추상메서드 표기
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print("공부하기")

class Student1(Student):
    def go_to_school(self):
        print("학교가기")

if __name__ == "__main__":
    student1 = Student1()
    student1.study()
    student1.go_to_school()
# 공부하기
# 학교가기