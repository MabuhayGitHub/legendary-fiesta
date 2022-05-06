from tkinter import *
from tkinter import font

class App(object):
    def __init__(self):
        root = Tk()
        
        self.customFont = font.Font(family="helverica", size=12)

        label = Label(root, text="Hello World", font=self.customFont)
        label.pack()

        bigger = Button(root, text="폰트 크기 증가", command=self.BigFont)
        smaller = Button(root, text="폰트 크기 감소", command=self.SmallFont)
        bigger.pack()
        smaller.pack()

        root.mainloop()

    def BigFont(self):
        size = self.customFont["size"]
        print(size)
        self.customFont.configure(size = size + 2)
        print(self.customFont)

    def SmallFont(self):
        size = self.customFont["size"]
        print(size)
        self.customFont.configure(size = size - 2)
        print(self.customFont)

if __name__ == "__main__":
    App()