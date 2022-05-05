from tkinter import *
from turtle import onclick

# 루트 윈도우 생성
window = Tk()
# 레이블 위젯 생성
label1 = Label(window, text="라벨을 만들어 보았습니다")
# 레이블 위젯 배치
label1.pack()
# 윈도우 표시, 이벤트 대기
label1.mainloop()