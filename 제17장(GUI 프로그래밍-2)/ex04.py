# # Label의 텍스트 가져오기
# # #1 cget()

# # from tkinter import *
# import tkinter as tk

# class Test(object):
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("200x80")
#         self.label = tk.Label(self.root, text="레이블 예제")
#         self.button = tk.Button(self.root, text="레이블 텍스트 읽기", command=self.readLabelText)
#         self.button.pack()
#         self.label.pack()
#         self.root.mainloop()
#     def readLabelText(self):
#         print(self.label.cget("text"))

# if __name__ == "__main__":
#     app = Test()


# # Label의 텍스트 가져오기
# # #2 text 속성 이용

# # from tkinter import *
# import tkinter as tk

# class Test(object):
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("200x80")
#         self.label = tk.Label(self.root, text="레이블 예제")
#         self.button = tk.Button(self.root, text="레이블 텍스트 읽기", command=self.readLabelText)
#         self.button.pack()
#         self.label.pack()
#         self.root.mainloop()
#     def readLabelText(self):
#         print(self.label["text"])

# if __name__ == "__main__":
#     app = Test()


# Label의 텍스트 가져오기
# # Stringvar 클래스 이용

# from tkinter import *
import tkinter as tk

class Test(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x80")
        self.text = tk.StringVar()  # Stringvar 인스턴스 생성
        self.text.set("레이블 예제")    # Stringvar 문자열 지정
        self.label = tk.Label(self.root, textvariable=self.text)
        self.button = tk.Button(self.root, text="레이블 텍스트 읽기", command=self.readLabelText)
        self.button.pack()
        self.label.pack()
        self.root.mainloop()
    def readLabelText(self):
        print(self.text.get())

if __name__ == "__main__":
    app = Test()
