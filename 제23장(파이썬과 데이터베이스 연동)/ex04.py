from tkinter import *
from tkinter import messagebox
import sqlite3

def insertData():
    con, cur = None, None
    id, userName, email, birthYear = "", "", "", ""
    sql=""
    con = sqlite3.connect("D:/_PYTHON/_Inflearn/제23장(파이썬과 데이터베이스 연동)/myDB")
    cur = con.cursor()
    id = edit1.get();    userName = edit2.get();    email = edit3.get();    birthYear = edit4.get();
    try:
        sql = "INSERT INTO userTable VALUES ('" + id + "','" + userName + "','" + email + "'," + birthYear + ")"
        print(sql)
        con.execute(sql)
    except:
        messagebox.showerror("오류", "데이터 입력 오류 발생")
    else:
        messagebox.showinfo("성공", "데이터 입력 성공")
    con.commit()
    con.close()
    selectData()

def selectData():
    strData1, strData2, strData3, strData4 = [], [], [], []
    con = sqlite3.connect("D:/_PYTHON/_Inflearn/제23장(파이썬과 데이터베이스 연동)/myDB")
    cur = con.cursor()
    cur.execute("SELECT * FROM userTable")
    strData1.append("사용자 ID");   strData1.append("-------------")
    strData2.append("사용자 이름"); strData2.append("-------------")
    strData3.append("이메일");      strData3.append("-------------")
    strData4.append("출생연도");    strData4.append("-------------")
    while(True):
        row = cur.fetchone()
        if row == None:
            break
        strData1.append(row[0]) 
        strData2.append(row[1])
        strData3.append(row[2])
        strData4.append(row[3])
    listData1.delete(0, listData1.size()-1)
    listData2.delete(0, listData2.size()-1)
    listData3.delete(0, listData3.size()-1)
    listData4.delete(0, listData4.size()-1)
    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
        listData1.insert(END, item1)
        listData2.insert(END, item2)
        listData3.insert(END, item3)
        listData4.insert(END, item4)
    con.close()

def Quit():
    window.quit()

window = Tk()
window.geometry("600x300")
window.title("GUI 데이터 입력")

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

edit1 = Entry(editFrame, width=10); edit1.pack(side=LEFT, padx=10, pady=10)
edit2 = Entry(editFrame, width=10); edit2.pack(side=LEFT, padx=10, pady=10)
edit3 = Entry(editFrame, width=10); edit3.pack(side=LEFT, padx=10, pady=10)
edit4 = Entry(editFrame, width=10); edit4.pack(side=LEFT, padx=10, pady=10)

btnInsert = Button(editFrame, text="입력", command=insertData); btnInsert.pack(side=LEFT, padx=10, pady=10)
btnSelect = Button(editFrame, text="조회", command=selectData); btnSelect.pack(side=LEFT, padx=10, pady=10)
btnQuit   = Button(editFrame, text="종료", command=Quit);       btnQuit.pack(side=LEFT, padx=10, pady=10)

listData1 = Listbox(listFrame, bg="yellow"); listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame, bg="yellow"); listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame, bg="yellow"); listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame, bg="yellow"); listData4.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()