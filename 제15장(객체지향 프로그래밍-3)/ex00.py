# # 클래스 다중 상속

# class Person(object):
#     def greeting(self):
#         print("Person 클래스")

# class University(object):
#     def manage_credit(self):
#         print("University 클래스")

# class Undergraduate(Person, University):
#     def study(self):
#         print("Undergraduate 클래스")

# if __name__ == "__main__":
#     James = Undergraduate()
#     James.greeting()
#     James.manage_credit()
#     James.study()
# # Person 클래스
# # University 클래스
# # Undergraduate 클래스

# -------------------------------------------------------------------------------

# # 다이아몬드 상속

# class A(object):
#     def greeting(self):
#         print("A")
# class B(A):
#     def greeting(self):
#         print("B")
# class C(A):
#     def greeting(self):
#         print("C")
# class D(B, C):
#     pass
# x = D()
# # MRO: Method Resolution Order
# print(D.mro())
# x.greeting()
# # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# # B

# -------------------------------------------------------------------------------
