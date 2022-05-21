import sqlite3

con, cur = None, None
pCode, pName, price, amount = "", "", 0, 0

con = sqlite3.connect("D:/_PYTHON/_Inflearn/제23장(파이썬과 데이터베이스 연동)/myDB")
cur = con.cursor()

sql = "CREATE TABLE IF NOT EXISTS productTable (pCode char(5), pName char(20), price int, amount int)"
print(sql)
cur.execute(sql)

while True:
    pCode = input("제품코드를 입력하세요: ")
    if pCode == "":
        break
    pName = input("제품명을 입력하세요: ")
    price = int(input("제품 가격을 입력하세요: "))
    amount = int(input("재고수량을 입력하세요: "))
    cur.execute("INSERT INTO productTable (pCode, pName, price, amount) VALUES (?, ?, ?, ?)", (pCode, pName, price, amount))

con.commit()

cur.execute("SELECT * FROM productTable")
print("제품코드         제품명      가격(만원)      재고수량")
print("-----------------------------------------------------")
while True:
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
