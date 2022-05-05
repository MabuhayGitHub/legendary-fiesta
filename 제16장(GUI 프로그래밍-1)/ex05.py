from tkinter import *

window = Tk()

counter = 0

def click():
    global counter
    counter += 1
    label["text"] = "버튼 클릭 횟수: " + str(counter)
def reset():
    global counter
    label["text"] = "리셋되었습니다: " + "0"

if __name__ == "__main__":
    label = Label(window, text="버튼을 클릭하세요")
    label.pack()
    button1 = Button(window, text="클릭", command=click)
    button1.pack()
    button2 = Button(window, text="리셋", command=reset)
    button2.pack()
    window.mainloop()