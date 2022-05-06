from tkinter import *
import random
from turtle import title

answer = random.randint(1, 100)
print(answer)

def guessing():
    guess = int(guessField.get())
    if guess > answer:
        msg = "커요"
    elif guess < answer:
        msg = "작아요"
    else:
        msg = "정답!!"
    
    resultLabel["text"] = msg
    guessField.delete(0, 5)

def reset():
    global answer
    answer = random.randint(1, 100)
    print(answer)
    resultLabel["text"]="다시 도전"


window = Tk()
window.configure(bg="white")
window.title("숫자 추측 게임")
window.geometry("500x80")
titleLabel = Label(window, text="숫자 게임에 오신 것을 환영합니다")
titleLabel.pack()

guessField = Entry(window)
guessField.pack(side=LEFT, padx=15)

tryButton = Button(window, text="시도", fg="green", bg="white", command=guessing)
resetButton = Button(window, text="초기화", fg="red", bg="white", command=reset)
tryButton.pack(side=LEFT)
resetButton.pack(side=LEFT)

resultLabel = Label(window, text="1~100 사이 숫자를 입력하세요", bg="white")
resultLabel.pack(side=LEFT, padx=20)

window.mainloop()