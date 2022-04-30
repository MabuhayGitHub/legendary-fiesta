# grage module

# 사용자 성적 입력
def readList():
    flag = True
    scorelist = []
    while flag:
        score = int(input("성적을 입력하세요.(종료: 음수)"))
        if score < 0:
            flag = False
        else:
            scorelist.append(score)
    return scorelist

# 정렬
def sortList(scorelist):
    scorelist.sort()
    return scorelist 

# 출력
def showScore(scorelist):
    j = 0
    for i in scorelist:
        print((j+1),"번째 성적: ", i)
        j += 1

