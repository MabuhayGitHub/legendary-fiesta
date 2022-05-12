# from tkinter import *

# window = Tk()

# def callback(event):
#     print(event.x, event.y, "마우스 이벤트 발생")

# frame = Frame(window, width=300, height=300)
# frame.bind("<Button-1>", callback)  # 왼쪽 버튼
# frame.bind("<Button-2>", callback)  # 휠
# frame.bind("<Button-3>", callback)  # 오른쪽 버튼
# frame.pack()

# window.mainloop()

## -----------------------------------------------------------------

# from tkinter import *

# window = Tk()

# def key(event):
#     print(repr(event.char), "키가 눌렸습니다")
# def callback(event):
#     frame.focus_set()
#     print(event.x, event.y, "마우스 이벤트 발생")

# frame = Frame(window, width=300, height=300)
# frame.bind("<Key>", key)
# frame.bind("<ButtonPress-1>", callback)
# frame.bind("<Double-Button-1>", callback)   # 더블클릭
# frame.bind("<B1-Motion>", callback)
# # frame.bind("<ButtonRelease-1>", callback)
# # frame.bind("<Enter>", callback)   # 마우스 포인터 위젯 진입
# # frame.bind("<Leave>", callback)   # 마우스 포인터 위젯 이탈
# # frame.bind("<FocusIn>", callback)   # 키보드 포커스 위젯 진입
# # frame.bind("<FocusOut>", callback)   # 키보드 포커스 위젯 이탈
# # frame.bind("<Return>", callback)   # 사용자의 엔터키 입력
# # frame.bind("<Double-Button-1>", callback)   # 더블클릭
# # frame.bind("<Key>", callback)   # 키입력
# # frame.bind("<Shift-Up>", callback)  # Shift + 위쪽 화살표
# # frame.bind("<Configure>", callback)     # 위젯 크기 변경
# frame.pack()

# window.mainloop()

# # -----------------------------------------------------------------

from tkinter import *
from tkinter import messagebox

def func_open():
    messagebox.showinfo("메뉴 선택", "열기 메뉴 선택")
def func_exit():
    window.quit()
    window.destroy()

window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label="편집", menu=editMenu)
editMenu.add_command(label="추가")
editMenu.add_separator()
editMenu.add_command(label="삭제")
editMenu.add_separator()

window.mainloop()
