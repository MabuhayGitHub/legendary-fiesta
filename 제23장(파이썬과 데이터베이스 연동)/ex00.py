# import sqlite3

# dbCon = sqlite3.connect("D:/_PYTHON/_Inflearn/제23장(파이썬과 데이터베이스 연동)/naverDB")

# myCusor = dbCon.cursor()

# # myCusor.execute("CREATE TABLE userTable (id char(4), userName char(15), email char(15), birthYear int)")
# # myCusor.execute("DROP TABLE userTable")

# # myCusor.execute("INSERT INTO userTable VALUES ('john', 'John Bann', 'john@naver.com', 1990)")
# # myCusor.execute("INSERT INTO userTable VALUES ('kim',  'Kim Chi',   'kim@daum.net',   1992)")
# # myCusor.execute("INSERT INTO userTable VALUES ('lee', 'Lee Pal', 'lee@paran.com', 1988)")
# # myCusor.execute("INSERT INTO userTable VALUES ('park', 'Park Su', 'park@gmail.com', 1980)")

# dbCon.commit()

# dbCon.close()

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
    sql = "INSERT INTO userTable VALUES('" + data1 + "'," + data2 + "'," + data3 + "'," + data4 + ")"
    # print(sql)
    cur.execute(sql)

con.commit()
con.close()
