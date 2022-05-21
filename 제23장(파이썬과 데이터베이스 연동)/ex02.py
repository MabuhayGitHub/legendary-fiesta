import sqlite3

con, cur = None, None
data1, data2, data3, data4 = "", "", "", 0

con = sqlite3.connect("D:/_PYTHON/_Inflearn/제23장(파이썬과 데이터베이스 연동)/myDB")
cur = con.cursor()

while (True):
    data1 = input("사용자 ID : ")
    if data1 == "":
        break
    data2 = input("사용자 이름 : ")
    data3 = input("이메일 : ")
    data4 = input("출생연도 : ")
    
    # Statement
    # sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    # print(sql)
    # cur.execute(sql)

    # PreparedStatement    
    sql = "INSERT INTO userTable (id, userName, email, birthYear) values (?, ?, ?, ?)", (data1, data2, data3, data4)
    cur.execute("INSERT INTO userTable (id, userName, email, birthYear) values (?, ?, ?, ?)", (data1, data2, data3, data4))   

con.commit()

cur.execute("SELECT * FROM userTable")
while True:
    row = cur.fetchone()
    if row == None:
        break
    id          = row[0]
    userName    = row[1]
    email       = row[2]
    birthYear   = row[3]
    print("%5s %15s %15s %5d" % (id, userName, email, birthYear))

con.close()
