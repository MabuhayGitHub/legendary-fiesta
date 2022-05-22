import sqlite3

con, cur = None, None
id, userName, email, birthYear = "", "", "", 1990
row = None
rows = None

if __name__ == "__main__":
    con = sqlite3.connect("D:/_PYTHON/_Inflearn/제23장(파이썬과 데이터베이스 연동)/myDB")
    cur = con.cursor()
    cur.execute("select * from userTable")
    # cur.execute("select * from userTable where birthYear >= 1990")
    # cur.execute("select * from userTable order by birthYear desc")
    print("사용자ID     사용자이름        이메일    출생년도")
    print("-------------------------------------------------")
    while True:
        row = cur.fetchone()
        # print(row)
        if row == None:
            break
        id = row[0]
        userName = row[1]
        email = row[2]
        birthYear = row[3]
        print("%5s %15s %20s %5d" % (id, userName, email, birthYear))
    
    # rows = cur.fetchall()
    # for data in rows:
    #     print(data)

    con.close()
