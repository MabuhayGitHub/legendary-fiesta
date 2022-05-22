import sqlite3

con, cur = None, None
pCode, pName, price, amount = "", "", 0, 0
row = None

if __name__ == "__main__":
    con = sqlite3.connect("D:/_PYTHON/_Inflearn/제23장(파이썬과 데이터베이스 연동)/myDB")
    cur = con.cursor()
    cur.execute("SELECT * FROM productTable")
    print("-----------------------------------------------------")
    print("제품코드         제품명      가격(만원)      재고수량")
    print("-----------------------------------------------------")
    # while True:
    while(True):
        row = cur.fetchone()
        if row == None:
            break
        pCode    = row[0]
        pName    = row[1]
        price    = row[2]
        amount   = row[3]
        print("%5s %15s %10d %15d" % (pCode, pName, price, amount))
    print("-----------------------------------------------------")

    con.close()
