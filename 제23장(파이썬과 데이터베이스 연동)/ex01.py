import sqlite3

con = None
cur = None

con = sqlite3.connect("D:/_PYTHON/_Inflearn/제23장(파이썬과 데이터베이스 연동)/myDB")

cur = con.cursor()

# 테이블 삭제
# sql = "DROP TABLE userTable"
# cur.execute(sql)

# 테이블 생성
sql = "CREATE TABLE IF NOT EXISTS userTable (id char(4), userName char(15), email char(15), birthYear int)"
cur.execute(sql)

# 테이블 목록 조회
# sql = "SELECT * FROM sqlite_master where type='table';"
# cur.execute(sql)
# print(cur.fetchall())

# 데이터 입력
sql = "INSERT INTO userTable VALUES ('john', 'john', 'john@naver.com', 1990)"
cur.execute(sql)
sql = "INSERT INTO userTable VALUES ('kim', 'Kim Chi', 'kim@daum.net', 1992)"
cur.execute(sql)
sql = "INSERT INTO userTable VALUES ('lee', 'Lee Pal', 'lee@paran.com', 1988)"
cur.execute(sql)
sql = "INSERT INTO userTable VALUES ('park', 'Park Su', 'park@gmail.com', 1980)"
cur.execute(sql)

# 입력 데이터 조회
sql = "SELECT * FROM userTable"
cur.execute(sql)
print(cur.fetchall())

con.commit()
con.close()