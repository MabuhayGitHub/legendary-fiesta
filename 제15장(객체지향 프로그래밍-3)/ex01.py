class Person(object):
    def __init__(self):
        pass
    def greeting(self):
        print("Person 클래스")

class University(object):
    def __init__(self):
        pass
    def manage_credit(self):
        print("University 클래스")

class Undergraduate(Person, University):
    def __init__(self):
        Person.__init__(self)
        University.__init__(self)    
    def study(self):
        print("Undergraduate 클래스")
    
if __name__ == "__main__":
    student = Undergraduate()
    student.greeting()
    student.manage_credit()
    student.study()