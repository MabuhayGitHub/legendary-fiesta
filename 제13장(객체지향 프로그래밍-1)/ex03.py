from person import *

if __name__ == "__main__":

    person1 = Person()
    person1.__str__()
    print()

    person2 = Person()
    person2.__str__()
    print()

    print(person1.getName())
    person1.setName("김길동")
    person1.age = 50
    print(person1.getName())

    print(person1.getAddress())
    print(person1.age)