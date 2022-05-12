from tkinter import *
from tkinter.filedialog import *
import os

es = ""

def newFile():
    top.title("제목없음-메모장")
    ta.delete(1.0, END) # 1.0 -> 첫 번째 라인 첫 번째 문자

def openFile():
    file = askopenfilename(title="파일 열기", filetypes=(("텍스트 파일", "*.txt"), ("모든 파일", "*.*")))
    top.title(os.path.basename(file)+"-메모장")
    ta.delete(1.0, END) 
    f = open(file, "r")
    ta.insert(1.0, f.read())
    f.close()

def saveFile():
    f = asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:   # 무효화 처리
        return
    ts = str(ta.get(1.0, END))
    f.write(ts) # 파일 저장
    f.close()

def memo_exit():
    top.quit()
    top.destroy()

def cut():
    global es
    es = ta.get(SEL_FIRST, SEL_LAST)
    ta.delete(SEL_FIRST, SEL_LAST)

def copy():
    global es
    es = ta.get(SEL_FIRST, SEL_LAST)

def paste():
    global es
    ta.insert(INSERT, es)   # INSERT 상수 -> 커서의 위치 저장

def delete():
    ta.delete(SEL_FIRST, SEL_LAST)

def help():
    he = Toplevel(top)
    he.geometry("200x200")
    he.title("정보")
    lbl = Label(he, text="메모장 버전 1.0\n파이썬으로 만든 메모장")
    lbl.pack()

top = Tk()
top.title("메모장")
top.geometry("400x400")

ta = Text(top)
ta.pack()
sb = Scrollbar(ta)
sb.configure(command=ta.yview())
sb.pack(side=RIGHT, fill=Y)

top.grid_rowconfigure(0, weight=1)
top.grid_columnconfigure(0, weight=1)

ta.grid(sticky=N+E+S+W)

mb = Menu(top)
fi = Menu(mb, tearoff=False)
fi.add_command(label="새 파일", command=newFile)
fi.add_command(label="열기", command=openFile)
fi.add_command(label="저장", command=saveFile)
fi.add_separator()
fi.add_command(label="종료", command=memo_exit)
mb.add_cascade(label="파일", menu=fi)

ed = Menu(mb, tearoff=False)
ed.add_command(label="잘라내기", command=cut)
ed.add_command(label="복사", command=copy)
ed.add_command(label="붙여넣기", command=paste)
ed.add_command(label="삭제", command=delete)
ed.add_separator()
mb.add_cascade(label="편집", menu=ed)

he = Menu(mb, tearoff=False)
he.add_command(label="메모장 정보", command=help)
mb.add_cascade(label="도움말", menu=he)

top.config(menu=mb)

top.mainloop()