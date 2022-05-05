class Person(object):
    def __init__(self):
        print("Person 클래스")
    def greeting(self):
        print("안녕 Person")

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        print("Student 클래스")
    def greeting(self):
        print("안녕 Student")

class Worker(Person):
    def __init__(self):
        Person.__init__(self)
        print("Worker 클래스")
    def greeting(self):
        print("안녕 Worker")

class PartTimer(Student, Worker):
    def __init__(self):
        Student.__init__(self)
        Worker.__init__(self)
        print("PartTimer 클래스")
    # def greeting(self):
    #     pass

if __name__ == "__main__":
    partTimer = PartTimer()
    print(PartTimer.__mro__)
    partTimer.greeting()
    
# Person 클래스
# Student 클래스
# Person 클래스
# Worker 클래스
# PartTimer 클래스
# [<class '__main__.PartTimer'>, <class '__main__.Student'>, <class '__main__.Worker'>, <class '__main__.Person'>, <class 'object'>]
# # 안녕 Student
