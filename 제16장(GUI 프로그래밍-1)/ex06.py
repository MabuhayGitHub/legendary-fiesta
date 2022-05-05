from tkinter import *

class App:
    def __init__(self):
        window = Tk()
        helloB = Button(window, text="HELLO", command=self.hello, fg="red")
        helloB.pack(side=LEFT)
        quitB = Button(window, text="QUIT", command=self.quit, fg="blue")
        quitB.pack(side=LEFT)
        window.mainloop()
    def hello(self):
        print("HELLO")
    def quit(self):
        print("QUIT")

if __name__ == "__main__":
    App()