statement = """
계절이 지나가는 하늘에는
가을로 가득 차 있습니다.

나는 아무 걱정도 없이
가을 속의 별들을 다 헤일 듯합니다...

가슴 속에 하나 둘 새겨지는 별을
이제 다 못 헤는 것은
쉬이 아침이 오는 까닭이요,
내일 밤이 남은 까닭이요,
아직 나의 청춘이 다하지 않은 까닭입니다.

별 하나에 추억과
별 하나에 사랑과
별 하나에 쓸쓸함과
별 하나에 동경과
별 하나에 시와
별 하나에 어머니, 어머니

어머님, 나는 별 하나에 아름다운 말 한 마디씩 불러 봅니다. 소학교 때 책상을 같이했던 아이들의 이름과, 패, 경, 옥 이런 이국 소녀들의 이름과, 벌써 아기 어머니 된 계집애들의 이름과, 가난한 이웃 사람들의 이름과, 비둘기, 강아지, 토끼, 노새, 노루, '프랑시스 잠', '라이너 마리아 릴케', 이런 시인의 이름을 불러 봅니다.

이네들은 너무나 멀리 있습니다.
별이 아스라이 멀 듯이,

어머님,
그리고 당신은 멀리 북간도에 계십니다

나는 무엇인지 그리워
이 많은 별빛이 내린 언덕 위에
내 이름자를 써 보고,
흙으로 덮어 버리었읍니다.

딴은, 밤을 새워 우는 벌레는
부끄러운 이름을 슬퍼하는 까닭입니다.

그러나 겨울이 지나고 나의 별에도 봄이 오면
무덤 위에 파란 잔디가 피어나듯이
내 이름자 묻힌 언덕 위에도
자랑처럼 풀이 무성할 게외다.
"""

import sqlite3
con, cur = None, None
oneChar, count = "", 0
if __name__ == "__main__":
    con = sqlite3.connect("D:/_PYTHON/_Inflearn/제23장(파이썬과 데이터베이스 연동)/myDB")
    cur = con.cursor()
    cur.execute("drop table if exists countTable")
    cur.execute("create table countTable(oneChar char(4), count INT)")
    for ch in statement:
        if "가" <= ch and ch <= "힣":
            cur.execute("select * from countTable where oneChar =?", (ch))
            row = cur.fetchone()
            if row == None:
                cur.execute("insert into countTable values(?,?)",(ch, str(1)))
            else:
                cnt = row[1]
                cur.execute("update countTable set count=? where oneChar=?", (str(cnt+1), ch))
    con.commit()

    cur.execute("select * from countTable where count > 2 order by count desc")
    print("원문\n", statement)
    print("-----------------")
    print("문자\t빈도수")
    print("-----------------")
    while True:
        row = cur.fetchone()
        if row == None:
            break
        ch = row[0]
        cnt = row[1]
        print("%2s\t%3d" % (ch, cnt))
    con.close()