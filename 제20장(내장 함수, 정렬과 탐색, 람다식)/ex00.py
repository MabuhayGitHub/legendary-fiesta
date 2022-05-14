# # def myfilter(x):
# #     return x > 3

# # result = filter(myfilter, (1,2,3,4,5,6))
# # print(list(result))

# -------------------------------------------

# n = [1, 2, 3, 4]
# s = ["One", "Two", "Three", "Four"]
# print(list(zip(n, s)))

# -------------------------------------------

# names = ["Kim", "Lee", "Park"]
# scores = [100, 90, 80]
# for n, s in zip(names, scores):
#     print(n, s)

# -------------------------------------------

# mylist = [4, 2, 3, 5, 1]
# print(mylist)
# print(sorted(mylist))   # 리스트 자체에 영향 없음
# print()
# print(mylist)
# mylist.sort()   # 리스트 자체에 영향
# print(mylist)

# -------------------------------------------

# print(sorted("The health know not of their health, but only the sick".split(), key=str.lower))

# -------------------------------------------

# # lambda 매개변수(들): 수식
# f = lambda x, y: x + y
# print(f(10, 20))

# from tkinter import *
# window = Tk()
# btn1 = Button(window, text="1 출력", command=lambda: print(1, "버튼 클릭"))
# btn1.pack(side=LEFT)
# btn2 = Button(window, text="2 출력", command=lambda: print(2, "버튼 클릭"))
# btn2.pack(side=LEFT)
# btn3 = Button(window, text="3 출력", command=lambda: print(3, "버튼 클릭"))
# btn3.pack(side=LEFT)
# window.mainloop()


# list_a = [1, 2, 3, 4, 5]
# f = lambda x: 2*x
# result = map(f, list_a)
# print(list(result))

# list_a = [1, 2, 3, 4, 5, 6]
# result = filter(lambda x: x%2 ==0, list_a)
# print(list(result))

# -------------------------------------------
import functools
result = functools.reduce(lambda x,y:x+y, [i for i in range(1,101)])
print(result)